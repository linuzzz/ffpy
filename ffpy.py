#!/usr/bin/python3.6

import os
import sys

#subprocess con ffmpeg non funziona...
#import subprocess

#modulo per parsing argomenti linea di comando
import argparse

#modulo per file di configurazione
import configparser

parser = argparse.ArgumentParser(description='ffmpeg simple editor wrapper')

#opzioni della linea di comando
parser.add_argument('-c', '--ctime', action='store', dest='ctime', type=int, help='start time in seconds for cutting video', default=0)
parser.add_argument('-d', '--duration', action='store', dest='duration', type=int, help='duration in seconds for cutting video')
parser.add_argument('-t', '--title', action='store', dest='title', type=str, help='title of the video')
#se non specifico un default si intende tipo str
#per gli argomenti obbligatori, che non sono opzioni il dest è il nome della variabile e non deve essere specificata
parser.add_argument('inputfile', action='store', help='input file')
parser.add_argument('outputfile', action='store', help='output file')

args = parser.parse_args()

#nome del programma
exename = sys.argv[0]
#nome del file di configurazione
cfgname = os.path.splitext(exename)[0] + '.cfg'

duration = args.duration
ctime = args.ctime
title = args.title
inputfile = args.inputfile
outputfile = args.outputfile

#leggo il file di configurazione
config = configparser.RawConfigParser()
config.read(cfgname)

'''debug cfgname
for each_section in config.sections():
    for (each_key, each_val) in config.items(each_section):
        print(each_key)
        print(each_val)
        print("\n")
'''

#parametri di conversione per ffmpeg
ffspeed = config.get('ffmpeg','speed')
ffquality = config.get('ffmpeg','quality')

#parametri generali 
fffont = config.get('global','font')

#main

#opzioni di cut (t0,t1,t2,t3)
#tratto di video intermedio da t1 a t2
if duration and ctime > 0:
	# i parametri -ss e -t vanno prima dell'input file altrimenti non funziona	
	cmd = "ffmpeg -ss %s -t %s -i %s -c copy %s" % (ctime, duration, inputfile, outputfile)
		
	#print(cmd)
	os.system(cmd)

#tratto di video iniziale da t0 a t1
if duration and ctime == 0:
	cmd = "ffmpeg -t %s -i %s -c copy %s" % (ctime, duration, inputfile, outputfile)
	os.system(cmd)

	#subprocess.call(['ffmpeg','-i', args.inputfile, '-ss', str(args.ctime), '-t', str(args.duration), '-c copy', args.outputfile])
	#subprocess.call(['ffmpeg', '-ss', str(args.ctime), '-t', str(args.duration), '-i', args.inputfile, '-c copy', args.outputfile])
	#subprocess.call(['ffmpeg', '-i gigidag_crop.mp4 -ss 1 -t 2 -c copy gigione.mp4'])
	#subprocess.call(['ls','-l',args.outputfile])







