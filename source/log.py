# log.py

import time
import re

class Logger:
	def __init__(self):
		self.logs = list()
		self.start_time = time.time()
		self.filters = []

	def log(self, text):
		self.logs.append("[" + str(round(time.time() - self.start_time, 3)) + "] " + text)

	def filter(self, term):
		for i in range(len(self.logs)):
			if re.search(term, self.logs[i]):
				if not self.logs[i] in self.filters:
					self.filters.append(self.logs[i])

	def clear_filter(self):
		self.filters = []

	def get_logs(self):
		if len(self.filters) > 0:
			return "\n".join(self.filters)

		return "\n".join(self.logs)
