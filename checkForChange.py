import os
import time



class Monkey(object):
	def __init__(self):
		self._cached_stamp = 0
		self.filename = 'emails.txt'

	def ook(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self._cached_stamp:
			print("Updated")
			self._cached_stamp = stamp
			# File has changed, so do something...

monkey = Monkey()

while(True):
	monkey.ook()
	time.sleep(5)

