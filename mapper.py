#!/usr/bin/python

import sys

for line in sys.stdin:

	line = line.strip()
	row = line.split(',')
	s1 = str(row[3])
	s1 = s1.replace('"','')
	s2 = row[5]
	s2 = s2.replace('"','')
	key = s1 + ',' + s2
	if row[7] < 15 : 
		print '%s\t%s' %(key,0)
	else :
		print '%s\t%s' %(key,1)

