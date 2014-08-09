#!/usr/bin/env python


import subprocess


parameters = []
command = raw_input("Enter the command you would like to execute: ");

p = "-";
s = "-";

while (p != 'Y' ):
	p = raw_input("Enter a parameter (Press 'Y' to exit): ");

	s+= p
	parameters.append(p)


print s[:-1]
subprocess.call([command,s[:-1]])


#subprocess.call(["df", "-hTaBG"])


