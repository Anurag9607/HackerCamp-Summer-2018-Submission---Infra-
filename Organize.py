import os
import sys
import hashlib


def makeFolders(downloadDirectory, fileTypes):
    for fileType in fileTypes:
        directory = downloadDirectory + "/" + fileType+ "/"
        
        if not os.path.exists(directory):
            os.mkdir(directory)

def moveFile(moveFile, downloadDirectory, fileTypes):

    
    if "." in moveFile:
        temp = moveFile.split(".")
        fileFormat = temp[-1] 
    else:
        return

    for fileType in fileTypes.keys():
        if fileFormat.lower() in fileTypes[fileType].lower():
            srcPath = downloadDirectory + "/" + moveFile
            dstPath = downloadDirectory + "/" + fileType + "/" + moveFile

            
            if not os.path.isfile(dstPath):
                os.rename(srcPath, dstPath)
            
            elif os.path.isfile(dstPath) and \
                 checkSum(srcPath) == checkSum(dstPath):
                os.remove(srcPath)
                print "removed " + srcPath
	    return


def main():

    fileTypes = {}
    
    #this line contains the directory of the desktop
    downloadDirectory = '/home/anurag/Downloads/Innovaccer'  #here anurag is to be replaced by username or path of desktop is to be needed
    downloadFiles = os.listdir(downloadDirectory)
    for f in downloadFiles:
        _,c=os.path.splitext(f)
        if (c[1:len(c)].lower()!='lnk') & (c[1:len(c)].lower()!='url'):
            fileTypes[c[1:len(c)].lower()]=c.lower()
        

    makeFolders(downloadDirectory, fileTypes)
    for filename in downloadFiles:
        moveFile(filename, downloadDirectory, fileTypes)

main()