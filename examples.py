#! /usr/bin/env python3

import sqlite3
import tables;

from os.path import expanduser
home = expanduser("~")

conn = sqlite3.connect(home+'/.config/dogepartyd/dogepartyd.9.db')
c = conn.cursor()

# global statistics
# get number of assets registered
c.execute('select count(distinct(asset)) from issuances;')
print ("Total assets: "+str(c.fetchone()[0]))

# get number of assets that have been locked 
c.execute('select count(distinct(asset)) from issuances where locked = 1;')
print ("Locked assets: "+str(c.fetchone()[0]))

# get number of assets that have had a quantity sent at least once
c.execute('select count(distinct(issuances.asset)) from issuances inner join sends on sends.asset = issuances.asset;')
print ("Assets distributed at least once: "+str(c.fetchone()[0]))

# queries about an asset
# get lock status of an asset
asset = ("DOGEPARTYTALK",)
c.execute('SELECT asset, locked FROM issuances where asset = ? order by tx_index desc limit 1',asset)
row = c.fetchone()
print ("\nAsset name: "+str(row[0]))
print ("Locked: "+str(row[1]))
