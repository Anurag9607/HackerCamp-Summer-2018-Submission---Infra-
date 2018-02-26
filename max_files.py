import os
import heapq
import win32api


def get_size():

    total_size = 0
    maxm=0
    h=[]
    q=0

    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        dirpath = drive
    
        for dirpath, dirnames, filenames in os.walk(dirpath):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                q += 1

                
                try:
                    b= os.path.getsize(fp)
                    total_size += b
                    print(q)
                    if len(h) < 10:
                            heapq.heappush(h, (float(b)/1000000,f))
                    else:
                            heapq.heappushpop(h,(float(b)/1000000,f))	

                except OSError:
                    continue
        
        return h

        

c=get_size()

for a in c:
	print(a)
