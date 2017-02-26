#import sys

#print('Number of arguments: ' + str(len(sys.argv)) + ' arguments.')
##print 'Number of arguments:', len(sys.argv), 'arguments.'
#print('Argument List:', str(sys.argv))

#https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''

	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
   
	except getopt.GetoptError:
		print('usage: test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
   
	for opt, arg in opts:
   		#help
		if opt == '-h':
			print('usage: test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		#input
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		#output
		elif opt in ("-o", "--ofile"):
			outputfile = arg
   
	print('Input file is ' + inputfile)
	print('Output file is ' + outputfile)

#main(sys.argv[1:])

if __name__ == "__main__":
#	main(sys.argv[1:])
	print(str(sys.argv))