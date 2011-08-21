#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from datetime import datetime, timedelta, date
import time
import sqlite3

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

#c.description()
c.execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
print c.fetchall()

c.execute("SELECT ZSTARTDATE, ZSTOPDATE, ZWORKEDMINUTES FROM ZLISTING")
x = c.fetchone()

print x[0]
print time.time()
print (datetime.fromtimestamp(x[0]) + (date(2011,01,01) - date(1980,01,01)))
print datetime.utcfromtimestamp(x[0])
#print datetime.fromordinal(x[0])
print datetime.fromtimestamp(x[1])
print time.ctime(x[0])
print time.gmtime(x[0])
print time.localtime(x[0])
print x[2]