# !/usr/bin/env python
# -*- coding: utf-8 -*-
class A:
	def __init__(self):
		self.a = 1
		self.b = 2

	def to_list(self):
		return [self.a, self.b]
		 
	def __list__(self):
		return [self.a, self.b]
		 
 
a = A()
lst1 = a.to_list()
lst2 = list(a) # 调用__list__