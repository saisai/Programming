#!/usr/bin/env python

"""
The computer will pick a number between 1 and 100. (You can chose 
any high number you want.) The purpose of the game is to guess the
number the computer picked in as few guesses as possible.
"""
import random
import time

# using the seconds as a seed for the random function.
sec = int( time.strftime('%S', time.localtime())) 

random.seed(sec)

r = random.randint(1 , 100)
g = raw_input("Enter a number between 1 and 100: ") 
g = int(g)
count = 0

while (g != r):
	count+= 1

	if g > r:
		g = raw_input("Too high. Try again: ")
	elif g < r:
		g = raw_input("Too low. Try again: ")
	g = int(g)
 
print "Congratulations...You guess the correct number: ", r
print "And it only took you %d guesses! " %(count)
