#!/usr/bin/env python
# encoding: UTF-8

import urllib.request as url_req
import csv


# url with all the dax companies + stock values
dax_url = "http://de.finance.yahoo.com/d/quotes.csv?s=@%5EGDAXI&f=sa&"
dax_snapshot = {}


# get dax data and put it into csv-form by decoding it to UTF-8
# (answer is now 1 giant string)
request = url_req.urlopen(dax_url)
answer  = request.read().decode('utf-8')


# write to obtained data into a csv-file
snapshot_file = open('snapshot.csv', "w")

try:
	snapshot_file.write(answer)

except IOError as e:
	print("Error: Couldn't write to file")
	print(e)

finally:
	snapshot_file.close()


# parse the cvs file to a dictionary using the cvs-module
with open('snapshot.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')


	for row in reader:
		try:
			dax_snapshot[row[0]] = row[1]
		except Exception as e:
			pass


# print the current dax snap shot which is the same as the content of the
# snapshot file
for k in dax_snapshot.keys():
	print(k, dax_snapshot[k])
