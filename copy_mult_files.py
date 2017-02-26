# **********************************************************************************
# Created by:			     Joseph Marty Badiola
# Date:					     February 2017
#
# Purpose:                   Copy/Move multiple files in a directory
#
# Displays knowledge in:	 Command-Line Arguments (sys, getopt)
#                            File Operations (shutil)
#                            Global (glob)
#                            OOP: Classes and Class Variables
# **********************************************************************************

import glob
import shutil
import os
import sys, getopt

file_search_pattern = ''
source_path = 'C:\\data\\repos\\python_scripts\\'
destination_path = 'C:\\data\\repos\\python_scripts\\move\\'

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hp:s:d:", ["pattern=","spath=","dpath="])
   
	except getopt.GetoptError:
		print('usage: test.py -p <pattern_to_find> -i <source_path> -o <destination_path>')
		sys.exit(2)
   
	for opt, arg in opts:
   		#help
		if opt == '-h':
			print('usage: test.py -p <pattern_to_find> -i <source_path> -o <destination_path>')
			sys.exit()
		elif opt in ("-p", "--pattern"):
			file_search_pattern = arg
			print("file_search_pattern = " + file_search_pattern)
		#input
		elif opt in ("-s", "--spath"):
			source_path = arg
		#output
		elif opt in ("-d", "--dpath"):
			destination_path = arg

print('Argument List:', str(sys.argv))
main(sys.argv[1:])

print("file_search_pattern = " + file_search_pattern)
for file_name in glob.glob(source_path + file_search_pattern):
    if not os.path.isdir(file_name):
    	print(file_name + " copying to " + destination_path + file_name)
    	shutil.copy(file_name, destination_path)
    else:
    	print("Directory " + file_name + " found - ignoring")