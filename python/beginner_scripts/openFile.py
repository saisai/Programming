#!/usr/bin/env python

f = open("test.txt", "r") # opens file with name of "test.txt"

myList = []

for line in f:
	myList.append(line)
print(myList)

#print(f.readline())
#print(f.readline())

f.close()
