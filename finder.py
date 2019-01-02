#Program to obtain a printed list of all files with a similar keyword

#imports
from __future__ import print_function
import os,sys

#search function
#uses tail-end recursion to print out a list of file paths
def search(path, keyword):
    files = os.listdir(path)
    for name in files:
        if (os.path.isfile(path + "\\"+ name)):
            if(keyword in name):
                print(path + "\\"+ name)
        elif (os.path.isdir(path + "\\"+ name)):
            try:
                search(path + "\\"+ name, keyword)
            except IOError:
                pass

#main function
# prints out instruction on how to use the search file
def main():
    print("Function 'search' will print a list of files that has similar names to your specified keyword.\neg. search(path, keyword), where path can be 'c:', the path and keyword must be strings")

main()
