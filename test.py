#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import csv
import datetime

HOURS_PER_WEEK = 8
HOURS_PER_MONTH = 35 # 4 * HOURS_PER_WEEK

def datefromstring(string):
	tmp = string.split('.', 2)
	if len(tmp[2]) <= 2:
		tmp[2] = int(tmp[2]) + 2000
	return datetime.date(tmp[2], int(tmp[1]), int(tmp[0]))

def timedeltafromstring(string):
	tmp = string.split(':', 1)
	return datetime.timedelta(hours=int(tmp[0]), minutes=int(tmp[1]))

if len(sys.argv) != 2:
	print("Please specify filename")
	sys.exit(1)

list = []

with open(sys.argv[1],'r') as f:
	reader = csv.reader(f,delimiter=';')
	
	headers = reader.next()[:-1]
	#print headers
	
	for row in reader:
		#print row
		
		if row[0] == '':
			break
		
		dict = {}
		for i in range(len(headers)):
			dict[headers[i]] = row[i]
		print dict
		list.append(dict)

for item in list:
	datum = datefromstring(item['Datum'])
	print datum
	item['Datum'] = datum
	
	delta = timedeltafromstring(item['Dauer'])
	print delta
	item['Dauer'] = delta

print list

try:
	weeks = {}
	it = iter(list)
	next = it.next()
	while True:
		cur = next
		startdate = cur['Datum'] - datetime.timedelta(days=cur['Datum'].weekday())
		print startdate
		weeks[startdate] = cur['Dauer']
		#print cur['Datum'].weekday()
		next = it.next()
		while next['Datum'] - cur['Datum'] < datetime.timedelta(days=6):
			print " %s" % next['Datum']
			weeks[startdate] += next['Dauer']
			next = it.next()
			continue
		continue
		
except StopIteration:
	pass
finally:
	print [(str(date),str(time)) for (date,time) in weeks.items()]

sum = datetime.timedelta(minutes=0)
for i in weeks.values():
	sum += i
print sum