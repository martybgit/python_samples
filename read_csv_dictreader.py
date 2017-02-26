# Create an object that operates like a regular reader 
#  but maps the information in each row to an OrderedDict 
#  whose keys are given by the optional fieldnames parameter.
# As of Python 3.6 - Returned rows are type OrderedDict.
# https://docs.python.org/3/library/csv.html

import csv

with open('c:/Data/repos/python_scripts/data/names.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['first_name'], row['last_name'])
		print(row)