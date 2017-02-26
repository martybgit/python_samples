# Return a reader object which will iterate over lines in the given csvfile
# Each row read from the csv file is returned as a list of strings

import csv

with open('c:/Data/Downloads/weather-stations20140101-20141231.csv', newline='') as csvfile:
	sr = csv.reader(csvfile, delimiter=',')
	for row in sr:
		print(', '.join(row))