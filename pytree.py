#! /usr/bin/env/python3
import argparse
import re
import sys  
import os
from pathlib import Path

# handle arguments
parser = argparse.ArgumentParser(
    description='A tree clone written in python. This program will take a directory path and recursively print all sub folders and files')

parser.add_argument('directory', help='directory to parse', action='store') 
parser.add_argument('-a',  help='All files are printed, including hidden ones', action='store_true')
parser.add_argument('-d', help='List directories only', action='store_true')
parser.add_argument('-f', help='Prints the full path prefix for each file', action='store_true') 
parser.add_argument('-v', '--verbose', help='log more verbosely', action='store_true')

args = parser.parse_args() 

directory = Path(args.directory)
 
# Recursively print files/directories based on options
def printItemsRecursively(path):
    for child in path.iterdir():
        if child.is_dir():
            # Check if object is a hidden directory
            if str(child)[0] == '.':
                # Check flag to verify we want to print hidden directories and files
                if args.a:
                    print(child.resolve())
                    printItemsRecursively(child)
            else:
                print(child.resolve())
                printItemsRecursively(child)
         # Check if object is a file and if we want to print out files based on flag
        elif child.is_file and not args.d:
            print(child.resolve())

# Make sure it's a valid directory
if directory.exists():
    printItemsRecursively(directory)
