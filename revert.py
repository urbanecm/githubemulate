#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path
import os

print "Reverting changes"
print "Removing the system config file that indicates this tunel is set on"
os.system('rm /etc/schoolGithubEmulate')
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
