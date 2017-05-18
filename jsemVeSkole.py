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
else:
	print "Doing nothing"
