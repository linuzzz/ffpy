#!/usr/bin/python3

import os
import sys
import csv
import getopt

from netaddr import IPNetwork, IPAddress

try:
	opts, args = getopt.getopt(sys.argv[1:],"i:o:n:",["ifile=","ofile=","netdata="])
except getopt.GetoptError:
	print(sys.argv[0] + ' -i <ifile> -o <ofile> -n <netdata>')
	sys.exit(0)

if len(opts) < 3:
	print(sys.argv[0] + ' -i <ifile> -o <ofile> -n <netdata>')
	sys.exit(0)

for opt, arg in opts:
	if opt in ("-i", "--ifile"):
		fname = arg
	elif opt in ("-o", "--ofile"):
		ofile = arg
	elif opt in ("-n", "--netdata"):
		ipdbname = arg
   
with open(fname, "r") as f:
	for line in f:
		ipv4 = IPAddress(line.rstrip())
		#print(line.rstrip())

		
		with open(ipdbname, 'r') as csvf:
			csvfile = csv.DictReader(csvf, delimiter=',', quotechar='"')
			#print(csvfile.fieldnames)
			#headers = next(csvfile)[1:]
			netDict = {}
			for row in csvfile:
				#print(', '.join(row))
				#print("-----" + row['Net'])
				netv4 = IPNetwork(row['Net'])
				if ipv4 in netv4:
					netDict[netv4.size] = str(netv4) + "," + row['Site'] + "," + row['txtDescription']
					#print("ipsize: " + str(netv4.size))
					#print(str(ipv4) + "------" + str(netv4) + "," + row['Site'] + "," + row['txtDescription'])
			low = min(netDict.keys())
			#print("/////////////////// " + str(low))
			print(str(ipv4) + ","  + str([v for k, v in netDict.items() if k == low]))
			netDict.clear()		
		
		#with open(ipdbname, "r") as f2:
		#	for line2 in f2:
		#		netv4 = IPNetwork(line2.rstrip())
		#		if ipv4 in netv4:
		#			print(str(ipv4) + "------" + str(netv4))


f.close()

#sys.exit(1)


