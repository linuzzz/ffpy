#!/usr/bin/python3

import os
import sys

#subprocess con ffmpeg non funziona...
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


def getLength(input_video):
	#senza shell=True non funziona...
	result = subprocess.Popen(['ffprobe -i %s -show_entries format=duration -v quiet -of csv="p=0"' % input_video], stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
	output = result.communicate()
	return float(output[0])


#main

#opzioni di cut (t0,t1,t2,t3)
#tratto di video da t0 a t1, oppure da t1 a t2
if duration:
	# i parametri -ss e -t vanno prima dell'input file
	# con stream copy i parametri di durata hanno problemi con formato mp4
	# se l'output file fosse in un formato diverso da mp4 dovrei specificare le librerie audio/video per la conversione
	cmd = "ffmpeg -y -ss %s -t %s -i %s -crf %s -preset %s %s" % (ctime, duration, inputfile, ffquality, ffspeed, outputfile)
		
	#print(cmd)
	os.system(cmd)

#tratto di video finale da t2 a t3, non specifico la durata
if duration is None and ctime > 0:
	cmd = "ffmpeg -y -ss %s -i %s -crf %s -preset %s %s" % (ctime, inputfile, ffquality, ffspeed, outputfile)
	os.system(cmd)

	#subprocess.call(['ffmpeg','-i', args.inputfile, '-ss', str(args.ctime), '-t', str(args.duration), '-c copy', args.outputfile])
	#subprocess.call(['ffmpeg', '-ss', str(args.ctime), '-t', str(args.duration), '-i', args.inputfile, '-c copy', args.outputfile])
	#subprocess.call(['ffmpeg', '-i gigidag_crop.mp4 -ss 1 -t 2 -c copy gigione.mp4'])
	#subprocess.call(['ls','-l',args.outputfile])


print(str(getLength(inputfile)))


