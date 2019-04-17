# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sched, time

s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
	print("From print_time", time.time())

def print_some_times():
	print(time.time())
	try:
		while 1:
			s.enter(2, 1, print_time)
			s.run()
			print(time.time())
	except KeyboardInterrupt:
		print(time.time())

# print_some_times()