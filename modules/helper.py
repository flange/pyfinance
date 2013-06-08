# encoding: UTF-8

import csv
import time
import os
from datetime import datetime


class Bool_Wrapper:
	def __ini__(self):
		self.running = None



def get_timestamp():
	"""
	Generates a timestamp based on the seconds counted from
	the beginning of UNIX
	"""

	sec_since_UNIX  = time.time()
	convert_to_time = datetime.fromtimestamp(sec_since_UNIX)

	timestamp = convert_to_time.strftime('[%Y-%m-%d %H:%M:%S]')

	return timestamp


def parse_dax_data(data_file, thread_lock):

	dax_data = {}
	thread_lock.acquire()

	with open(data_file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')

		for row in reader:
			try:
				dax_data[row[0]] = row[1]
			except Exception as e:
				pass

	thread_lock.release()

	return dax_data


def float_string_to_int(string):
	# float -> int
	string = string.replace('.', '')

	# string -> int
	return int(string)


def int_to_float_string(num):
	num = str(num)
	num_len = len(num)

	num_euro = num[0:(num_len - 2)]
	num_cent = num[(num_len - 2):num_len]

	return ".".join([num_euro, num_cent])
