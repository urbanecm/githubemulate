#!/usr/bin/env python
#-*- coding: utf-8 -*-

import helper
import os.path, os
import sys
import requests
import json

url = 'https://api.ipify.org?format=json'
jsonData = requests.get(url).content
data = json.loads(jsonData)

if data['ip'] == helper.getBadIP():
	if os.path.isfile('/etc/emulateBadPorts'):
		print "Nothing needs to be changed"
		sys.exit()

	print "Creating system file that indicate the tunels are set already"
	os.system('touch /etc/emulateBadPorts')

	prefix = helper.getCmdPrefix()
	suffix = helper.getCmdSuffix()
	prostredky = helper.getTunels()
	ipprefix = '127.0.0.'
	if len(prostredky) >= 255:
		print "We are sorry. This emulation app allows only up to 254 things to emulate due to technical limits"
		sys.exit(1)

	cmds = []
	i = 1
	for prostredek in prostredky:
		cmd = prefix + ' -L ' + ipprefix + str(i) + ':' +  prostredek + ' ' + suffix
		i += 1
		cmds.append(cmd)

	hosts = []
	i = 1
	domains = helper.getDomains()
	for domain in domains:
		host = ipprefix + str(i) + '\t' + domain + '\n'
		i += 1
		hosts.append(host)

	print "Creating tunels"
	for cmd in cmds:
		os.system(cmd)

	print "Updating /etc/hosts"
	f = open('/etc/hosts', 'r')
	lines = f.readlines()
	f.close()
	newfile = []
	for line in lines:
		newfile.append(line)
	for host in hosts:
		newfile.append(host)
	f = open('/etc/hosts', 'w')
	for host in newfile:
		f.write(host)
	f.close()

else:
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
