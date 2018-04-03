#!/usr/bin/python3

import os
import sys

#modulo per parsing argomenti linea di comando
import argparse

#modulo per file di configurazione
import configparser

parser = argparse.ArgumentParser(description='ffmpeg simple editor wrapper')

parser.add_argument('-c', '--ctime', action='store', dest='cutime', type=int, help='time in seconds for cutting video')
parser.add_argument('-t', '--title', action='store', dest='title', type=str, help='title of the video')

args = parser.parse_args()

#nome del programma
exename = sys.argv[0]
#nome del file di configurazione
cfgname = os.path.splitext(exename)[0] + '.cfg'

#debug argparser
print('time in seconds for cutting video: ', args.cutime)
print('title of the video: ', args.title)

#leggo il file di configurazione
config = configparser.RawConfigParser()
config.read(cfgname)

#debug cfgname
for each_section in config.sections():
    for (each_key, each_val) in config.items(each_section):
        print(each_key)
        print(each_val)
        print("\n")

#parametri di conversione per ffmpeg
ffspeed = config.get('ffmpeg','speed')
ffquality = config.get('ffmpeg','quality')

#parametri generali 
fffont = config.get('global','font')

print(fffont)
print(ffspeed)
print(ffquality)







