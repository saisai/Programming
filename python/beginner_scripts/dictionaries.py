#!/usr/bin/env python


myExample = {'someItem': 2, 'otherItem': 20}
print(myExample['otherItem'])


myExample['newItem'] = 400


for a in myExample:
	print(a, myExample[a])
