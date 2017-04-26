#!/usr/bin/python
import sys

current_key = None
current_count_ontime = 0
current_count_delayed = 0

for line in sys.stdin:
	line = line.strip()
	
	key, count = line.split('\t')
	
	try:
		count = int(count)
	except ValueError:
		continue

	if current_key == key :
		if count == 0 :
			current_count_ontime += 1
		else :
			current_count_delayed += 1
	else :
		if current_key :
			if current_count_ontime > 0 :
				print '%s,%s' % (current_key, current_count_ontime)
			else :
				print '%s,%s' % (current_key, current_count_delayed)
		if count == 0 :
                        current_count_ontime += 1
                else :
                        current_count_delayed += 1
		current_key = key

if current_key == key:
	 if current_count_ontime > 0 :
		print '%s,%s' % (current_key, current_count_ontime)
	 else :
		print '%s,%s' % (current_key, current_count_delayed)



