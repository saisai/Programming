#!/usr/bin/env python 

"""
Program Name: Leap year finder

Input: Your program should take a year as input

Output: Your program should print whether the year is or is not a leap year.
"""

a = raw_input("What year: ");
year = int(a)

if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
 print "%.d is a leap year" % year
elif year % 4 == 0:
 print "%.d is a leap year" % year
else:
 print "%.d is not a leap year" % year
 

