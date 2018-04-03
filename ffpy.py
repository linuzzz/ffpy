#!/usr/bin/python3

import os
import sys
import subprocess

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

#debug argparser
print('time in seconds for cutting video duration: ', args.duration)
print('title of the video: ', args.title)
print('input video: ', args.inputfile)
print('output video: ', args.outputfile)

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

#print(fffont)
#print(ffspeed)
#print(ffquality)

#main

#opzione di cut
if args.duration:
	#subprocess.call(['ffmpeg','-i', args.inputfile, '-ss', str(args.ctime), '-t', str(args.duration), '-c copy', args.outputfile])
	subprocess.call(['ffmpeg','-i', args.inputfile, '-ss', str(args.ctime), '-t', str(args.duration), args.outputfile])
	#subprocess.call(['ls','-l',args.outputfile])







