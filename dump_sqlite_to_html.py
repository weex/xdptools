#! /usr/bin/env python3

import sqlite3
import tables;

from os.path import expanduser
home = expanduser("~")

conn = sqlite3.connect(home+'/.config/dogepartyd/dogepartyd.9.db')
c = conn.cursor()

for table in tables.tables:
	print ( "\n<br /><br /><h2>"+table+"</h2>" )
	c.execute('SELECT * FROM '+table)
	
	rows = c.fetchall()
	if rows :
		print ("<table>")
		for row in rows :
			print ("<tr>")
			for field in row :
				print ("<td>"+str(field)+"</td>")
			print ("</tr>")

		print ("<table>")
