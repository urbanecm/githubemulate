#!/usr/bin/env python
#-*- coding: utf-8 -*-

import helper
import os.path, os
import sys
import requests
import json

if os.path.isfile('/etc/emulateBadPorts') == False:
	print "Nothing needs to be changed"
	sys.exit()
	print "Removing system file that indicate the tunels are set already"
os.system('rm /etc/emulateBadPorts')
print "Unseting tunels"
os.system('killall autossh')
print "Updating /etc/hosts"
domains = helper.getDomains()
f = open('/etc/hosts', 'r')
lines = f.readlines()
f.close()
newfile = []
for line in lines:
	atleastone = False
	for domain in domains:
		if domain in line:
			atleastone = True
			break
	if atleastone == False:
		newfile.append(line)
	f = open('/etc/hosts', 'w')
for line in newfile:
	f.write(line)
f.close()
