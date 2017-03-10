import csv
import sys

parameters = sys.argv
with open(parameters[1], 'rb') as fp:
	reader = csv.reader(fp)

	c = 0
	print reader['goodForGroups']

