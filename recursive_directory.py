# **********************************************************************************
# Created by:			     Joseph Marty Badiola
# Date:					     February 2017
#
# Purpose:                   List contents of a directory/folder
#
# Displays knowledge in:	 Command-Line Arguments (sys, getopt)
#                            File Operations (os)
#                            OOP: Classes and Class Variables
#                            Recursive Function Calls
# **********************************************************************************

import os
import sys, getopt

class GetParameters:
	'Class to get command-line parameters'

	directory_full_path = ''

	def directory_parameter(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hd:")
	   
		except getopt.GetoptError:
			print('usage: test.py -d <directory_full_path>')
			sys.exit(2)
	   
		for opt, arg in opts:
	   		#help
			if opt == '-h':
				print('usage: test.py -d <directory_full_path>')
				sys.exit()
			#input
			elif opt in ("-d", "--dpath"):
				#print("-d paramter value is " + arg)
				directory_full_path = arg

		return directory_full_path

class RecursiveDirectoryList:
	'Lists contents of a Directory/Folder'

	def print_directory_contents(self, str_path):
	    #print("Listing contents of " + str_path)
	    for str_object in os.listdir(str_path):                
	        str_child_path = os.path.join(str_path, str_object)

	        # if the object is a Folder/Directory, then do a recursive call
	        if os.path.isdir(str_child_path):
	            #print("Directory found - " + str_child_path)
	            RecursiveDirectoryList.print_directory_contents(self, str_child_path)
	        # if the object is a file, then show it
	        else:
	            print(str_child_path)

	#class destructor
	def __del__(self):
		class_name = self.__class__.__name__
		#print(class_name, "destroyed")

#print('Argument List:', str(sys.argv))

#get the directory
get_params = GetParameters()
directory_value = get_params.directory_parameter()
#print("The parameter values is " + directory_value)

#iterate through the directory - list folders and files
get_dir_list = RecursiveDirectoryList()
get_dir_list.print_directory_contents(directory_value)