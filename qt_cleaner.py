# removes the .user files from projects

import sys, os, glob

def getPath():
    strPath = ''
    if(len(sys.argv) >= 2):
        strPath = sys.argv[1]
        print("Path set to: " + strPath)

    if(len(sys.argv) < 2):
        print('Enter the path to scan')
        strPath = input("Path:")

    if(strPath.endswith('/') == False):
        strPath += '/'

    print(strPath)
    return strPath

def scanPath(strPath):
    print('Scaning ' + strPath)
    lst = []

    for filename in glob.iglob(strPath + '**/*.user', recursive=True):
        lst.append(filename)

    return lst

def checkpath(strPath):
    if(os.path.exists(strPath) == False):
        print('Path does not exist!')
        sys.exit(1)

def checkList(lst):
    if (len(lst) == 0):
        print('No files found!')
        sys.exit(0)

def verifyRemoval(lst):
    l = len(lst)
    print('Would you like to remove ', l, ' files?')
    strResponse = input("Y or N:")

    if(strResponse.upper() != 'Y'):
        sys.exit(0)

def removeFiles(lst):
    for f in lst:
        print(f)
        os.remove(f)


if __name__ == '__main__':
    print('Project cleaners for Qt projects (removes .user files)')
    strPath = getPath()

    checkpath(strPath)

    lst = scanPath(strPath)
    checkList(lst)
    verifyRemoval(lst)

    print('Removing files...')
    removeFiles(lst)



