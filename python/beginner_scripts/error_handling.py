#!/usr/bin/env python


var1 = '1'


try:
	var2 = var1 + 1 # since var1 is a string, it cannot be added to 
			# the number 1

except:	
	var2 = int(var1) + 1

print(var2)
