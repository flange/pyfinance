# encoding: UTF-8

import modules.helper as helper

class Logger:
	"""
	Generic Logger.
	"""

	def __init__(self, log_dir, log_file_name):
		self.log_file_name = log_file_name
		self.log_dir       = log_dir
		self.log_file_path = log_dir + "/" + log_file_name


	def log(self, log_msg):
		"""
		Write log_msg to the associated log file
		"""

		# open fetch log file and write log entry
		self.log_file = open(self.log_file_path, "a")

		try:
			self.log_file.write(log_msg)

		except IOError as e:
			print("Error @ Logger.log():")
			print("Couldn't write to log file")
			print(e)

		finally:
			self.log_file.close()

