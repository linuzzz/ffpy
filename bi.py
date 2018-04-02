#!/usr/bin/python3

import os
import sys
import getopt

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
	else:
            assert False, "unhandled option"

#sys.exit(1)


