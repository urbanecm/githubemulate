#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
import os

url = 'https://api.ipify.org?format=json'
jsonData = requests.get(url).content
data = json.loads(jsonData)
if data['ip'] == '195.113.165.66':
	print "Stopping local ssh"
	os.system('service ssh stop')
	print "Starting ssh tunel for GitHub"
	os.system('autossh -p 2222 -f -i /home/martin/.ssh/id_rsa_tunelar -NL 22:github.com:22 tunelar@vps.urbanec.cz')
	os.system('autossh -p 2222 -f -i /home/martin/.ssh/id_rsa_tunelar -NL 443:github.com:443 tunelar@vps.urbanec.cz')
	os.system('autossh -p 2222 -f -i /home/martin/.ssh/id_rsa_tunelar -NL 80:github.com:80 tunelar@vps.urbanec.cz')
	print "Editing /etc/hosts to force state that Github.com is 127.0.0.1"
	f = open('/etc/hosts', 'r')
	lines = f.readlines()
	f.close()
	
	lines.append('127.0.0.1\tgithub.com\n')
	
	f = open('/etc/hosts', 'w')
	for line in lines:
		f.write(line)
	f.close()
else:
	print "Reverting changes"
	print "Reverting changes in /etc/hosts"

	f = open('/etc/hosts', 'r')
	lines = f.readlines()
	f.close()
	
	newfile = []
	for line in lines:
		if 'github' not in line:
			newfile.append(line)
	
	f = open('/etc/hosts', 'w')
	for line in newfile:
		f.write(line)
	f.close()

	print "Killing tunels"
	os.system('killall autossh')
