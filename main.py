#! /usr/bin/env/python3
import argparse, re, sys

# handle arguments
parser = argparse.ArgumentParser(
    description='A tree clone written in python. This program will take a directory path and recursively print all sub folders and files')

parser.add_argument('directory', help='directory to parse') 
parser.add_argument('-a', help='All files are printed, including hidden ones')
parser.add_argument('-d', help='List directories only')
parser.add_argument('-f', help='Prints the full path prefix for each file') 
parser.add_argument('-v', '--verbose', help='log more verbosely', action='store_true')

args = parser.parse_args() 
 
 