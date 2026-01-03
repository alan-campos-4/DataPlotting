"""
The csv that we are working with, for some reason, gets exported with an extra comma in most of the lines.
This program is to get rid of it.
"""

import csv

COL_NUM = 8
new_lines = []

with open('Album.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if len(row)!=COL_NUM:
			diff = len(row)-COL_NUM
			row = row[:-diff]
		#print(', '.join(row))
		new_lines.append(row)

with open('AlbumLog_corrected.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for row in new_lines:
		writer.writerow(row)


