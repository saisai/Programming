#!/usr/bin/env python

""" 
Purpose: This program will convert the given temperature
	 from Fahrenheit to Celsius or vice-versa.
"""

def convertToCelcius( Tf ):
	"This function calculates fahrenheit temperature to celcius."

	Tc = (5/9)*(float(Tf) - 32)
	return Tc

def convertToFahrenheit( Tc ):
	"This function calculates celcius temperature to fahrenheit."
	
	Tf = (9/5)*(float(Tc) + 32)
	return Tf

####### PROGRAM START BELOW ########

temp = raw_input("Enter a temperature: ")
choice =  raw_input("Convert to (F)ahrenheit or (C)elsius? ")

if choice == "F":
	print "%s Fahrenheit is %5.2f Celcius" %(temp, convertToFahrenheit(temp))
elif choice == "C":
	print "%s Celcius is %5.2f Fahrenheit" %(temp, convertToCelcius(temp))
else:
	print "...Error:Please enter the correct input."
