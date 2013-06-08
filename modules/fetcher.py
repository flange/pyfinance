# encoding: UTF-8

import csv
import time
import urllib.request as url_req

import modules.logger as logger
import modules.helper as helper

class Fetcher:
	"""
	Periodically polls stock values from 'Yahoo Finance'.
	The 'fetch_dax_data()' function is supposed to be run as a thread."
	"""

	def __init__(self, url, data_dir, data_file_name, log_dir, log_file_name):
		self.dax_url  = url
		self.data_dir = data_dir
		self.data_file_name = data_file_name
		self.data_file_path = data_dir + "/" + data_file_name

		self.logger   = logger.Logger(log_dir, log_file_name)

	def fetch_dax_data(self, sleep_interval, lock):
		while True:
			# get current time for logging
			ts = helper.get_timestamp()

			# get dax data and put it into csv-form by decoding it to UTF-8
			# (answer is 1 giant string)
			request = url_req.urlopen(self.dax_url)
			answer  = request.read().decode('utf-8')


			# concurrency
			lock.acquire()

			# write to obtained data into a csv-file
			snapshot_file = open(self.data_file_path, "w")

			try:
				snapshot_file.write(answer)

			except IOError as e:
				print("Error @ Fetcher.fetch_dax_data:")
				print("Could not write fetched data to cvs file!")
				print(e)

				self.logger.log(ts + " fetch FAILED\n")

			finally:
				snapshot_file.close()

			lock.release()

			# log successful fetch
			self.logger.log(ts + " fetch OK\n")

			time.sleep(sleep_interval)

