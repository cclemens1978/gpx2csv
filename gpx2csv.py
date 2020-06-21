#!/usr/bin/env python3
""" ... converts the waypoints from a GPX file into an alphabetically sorted CSV file.
"""

import sys
import os
import time
import xmltodict

if len(sys.argv) != 2:
    print("ERROR: This script expects exactly one input file.")
    sys.exit()

GPXFILE = sys.argv[1]
GPXTIME = os.path.getmtime(GPXFILE)

with open(GPXFILE, 'r') as tmp_file_obj:
    GPXDATA = xmltodict.parse(tmp_file_obj.read())

CSVDATA = []

for tmp_wpt in GPXDATA['gpx']['wpt']:
    CSVDATA.append(
        '"' + tmp_wpt['type'] + '", ' +
        '"' + tmp_wpt['name'] + '", ' +
        tmp_wpt['@lat'] + ', ' +
        tmp_wpt['@lon']
    )

CSVDATA.sort()

CSVFILE = time.strftime('waypoints_%Y%m%d_%H%M%S.csv', time.localtime(GPXTIME))

with open(CSVFILE, 'w') as tmp_file_obj:
    tmp_file_obj.write('"type", "name", @lat, @log' + '\n')
    for tmp_wpt in CSVDATA:
        tmp_file_obj.write(tmp_wpt.encode('utf8') + '\n')

os.utime(CSVFILE, (GPXTIME, GPXTIME))
