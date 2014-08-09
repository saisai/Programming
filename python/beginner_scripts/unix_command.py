#!/usr/bin/env python

import os
import sys

#os.system("date")

disk = os.popen("df -h", 'w', 1)
#print "Your disk usage is: %s" % disk

print disk
