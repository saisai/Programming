#!/usr/bin/env python


import sys

def chop(target, array_of_int):
	size = len(array_of_int)
	half = int(size/2)
	#print "Half",half
	
	if size == 0:
		return -1
		#sys.exit()
	
	if target > array_of_int[half]:
		return chop(target, array_of_int[half+1:size])
	elif target < array_of_int[half-1]:
		return chop(target, array_of_int[:half])
	else:
		return array_of_int.index(target)
	

arr = []

for i in range(1, 100000):
	arr.append(i)
	
print chop(1, [1,3,5])
print chop(3, [1, 3, 5])
print chop(5, [1, 3, 5])
print chop(0, [1, 3, 5])
print chop(7, [1, 3, 5, 7])