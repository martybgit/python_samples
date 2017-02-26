# **********************************************************************************
# Created by:			     Joseph Marty Badiola
# Date:					     February 2017
#
# Purpose:                   Copy 1 file
#
# Displays knowledge in:	 Command-Line Arguments (sys, getopt)
#                            File Operations (shutil)
#                            OOP: Classes and Class Variables
# **********************************************************************************

import sys, getopt      #command-line args
import shutil           #file copy operations
import os               #for debug only

#debug
#print('Argument List:', str(sys.argv))
#print(os.getcwd())

class CopySingleFile:
	'Common base-class for JMB file operations'

	#class-level var's
	source_file = ''
	destination_file = ''

	#assign paramemter values to class variables
	#class constructor or initialization method called on creation of new instance of this class
	def __init__(self):
		#get the command-line param's
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hs:d:", ["sfile=","dfile="])
	   
		except getopt.GetoptError:
			print('GetoptError: filename.py -s <source_file> -d <destination_file>')
			sys.exit(2)

		#assign command-line parameter values to class-level variables
		for opt, arg in opts:
	   		#help
			if opt == '-h':
				print('usage: filename.py -s <source_file> -d <destination_file>')
				sys.exit()
			#input
			elif opt in ("-s", "--sfile"):
				CopySingleFile.source_file = arg
				print('Input file is ' + CopySingleFile.source_file)
			#output
			elif opt in ("-d", "--dfile"):
				CopySingleFile.destination_file = arg
				print('Output file is ' + CopySingleFile.destination_file)

	#perform the file copy operation
	def copyFile(self):
	    try:
	        shutil.copy(CopySingleFile.source_file, CopySingleFile.destination_file)

	    #eg src and dest are the same file
	    except shutil.Error as e:
	        print('shutil Error: %s' % e)
	    #eg source or destination doesn't exist
	    except IOError as e:
	        print('IOError Error: %s' % e.strerror)
   
	#class destructor
	def __del__(self):
		class_name = self.__class__.__name__
		#print(class_name, "destroyed")

copy_file = CopySingleFile()
copy_file.copyFile()