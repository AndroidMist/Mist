#/usr/bin/python
#coding=utf-8

import os
import sys
import time


if __name__ == '__main__' :
	app_dir = os.path.abspath(sys.argv[1])
	pea_dir = os.path.abspath(sys.argv[2])
	manifest_dir = os.path.abspath(sys.argv[3])
	ser_dir = os.path.abspath(sys.argv[4])
	if not os.path.exists(ser_dir):
		os.makedirs(ser_dir)
	#print app_dir
	fn = "history_"+ser_dir.split("/")[-1]+".txt"
	if not os.path.exists(fn):		
		print 'creat'
		f = open(fn, "w")
		f.close()
		
	#get apks
	f = open(fn, "r")
	app_set = set()
	lines = f.readlines()
	f.close()
	
	#add into set
	for x in lines:
		app_set.add(x.strip())	
	print app_set
	
	#for each app
	apks = os.listdir(app_dir)
	for  apk in apks :
		#if apk in app_set:
		#	print apk , "has been analyzed."
		#	continue
		command = 'java  -jar lib/Mist.jar '+app_dir+ ' ' +apk + ' ' +pea_dir+ ' ' + manifest_dir+ ' '  +ser_dir
		print command +"\n"
		os.system(command)
		print "write apk ",apk
		f = open(fn, "a")
		f.write(apk+"\n")
		f.close()
		# rm sootOutput
		command = 'rm -r sootOutput'
		#print command
		os.system(command)
		
	

	
