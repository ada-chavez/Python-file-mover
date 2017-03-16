## Version: Python 2.7
##
## Date: 03/16/17
##
## Author: Ada Chavez http://adachavez.com
##
## Purpose: (Drill given by The Tech Academy) This program moves files from folder A to folder B on the desktop.

import shutil
import os

def start():
    # prompt user for input
    user_input = raw_input("Please press M to move files from Folder A to Folder B or E to exit program: ").capitalize()

    if user_input == 'M':
        folderA = "/Users/techacademy/Desktop/A"
        folderB = "/Users/techacademy/Desktop/B"
        # moves files from folder a to folder b
        for fileList in os.listdir(folderA):
            source = os.path.join(folderA,fileList)
            dst = os.path.join(folderB,fileList)
            shutil.move(source,dst)
            print("\n" + source + " has been transfered to Folder B.")
    # exits program       
    elif user_input == 'E':
        print("\n See you later!")
        exit()
    # got invalid input from user
    else:
        print("\nWrong Button.Please try again!")
        start()

        



if __name__ == '__main__':
    start()

