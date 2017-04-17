# log.py

import time

class Logger:
	def __init__(self):
		self.logs = list()
		self.start_time = time.time()

	def log(self, text):
		self.logs.append("[" + str(round(time.time() - self.start_time, 3)) + "] " + text)

	def get_logs(self):
		return "\n".join(self.logs)
