# Import OS for help with file access
import os, sys, re
from stat import *
# user input to create or access folders and files
filePath = input("type path of directory, example c:/user/name/Documents/ or any other drive you want to access: ")
fileName = filePath + input("create file with .txt ending: ")
# to create directories is not already there
if not os.path.exists(filePath):
    os.makedirs(filePath)
open(fileName, 'a+')
# check for files and folders
os.path.isfile(fileName) #will return true if the file exists
os.path.isdir(filePath) # will return true if the directory exists
os.path.exists(fileName) #will return true if the file or directory passed to the function exists

# visual check for directories and files
if os.path.isfile(fileName):
    # check if file exists
    print('File Exists')
if os.path.isdir(filePath):
    # check if file path exists
    print('Directory Exists')

# Menu setup with 3 options. first option create information. Name, address, and phone number
def option1():
    file = open(fileName,'a+')
    file.write(input("Write Full Name: "))
    file.write(", ")
    file.write(input("Write address: "))
    file.write(", ")
    file.write(int(input("Write phone number: ")))
    file.write("\n")
    file.close()
# read file
def option2():
    file = open(fileName, "r")
    print(file.read())
# menu choices with error check for wrong number picked
if __name__ == "__main__":
    while True:
        n = input("\n1. Writing text to a file\n2. Read Data from a file\n3. Quit the program\nEnter your choice: ")
        if n == "1":
            option1()
        elif n == "2":
            option2()
        elif n == "3":
            file = open(fileName)
            print(file.read())
            break
        else:
            print("Wrong Choice!!")