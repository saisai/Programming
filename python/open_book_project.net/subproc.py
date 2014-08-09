#!/usr/bin/env python

import subprocess
import re

#subprocess.call(['ls', '-l'])

comm = "df -hv"
ducomm = "du -h"

proc = subprocess.Popen(comm, stdout=subprocess.PIPE, shell=True)
stddata = proc.communicate()

proc2 = subprocess.Popen(ducomm, stdout=subprocess.PIPE, shell=True)
stddu = [proc2.communicate()]

for s in stddata:
	print "" # s
 

for i in stddu:
	print i
	matchObj = re.match(r'(.*)[M|K|G]\t', i, re.I)

	if matchObj:
		print "matchObj.group(1) : ", matchObj.group()
	else:
		print "Nothing found!!"

#print stddata

#subprocess.check_call(['df', '-vh'])
