#!/usr/bin/env python
#-*- coding: utf-8 -*-

import yaml
import os

def getConfig():
	__dir__ = os.path.dirname(__file__)
	return yaml.safe_load(open(__dir__ + '/config.yaml'))

def getForForward():
	config = getConfig()
	forward = config['FORWARD'].replace(', ', ',')
	forwards = forward.split(',')
	del(forward)
	res = []
	for forward in forwards:
		portDomain = forward.split(':')
		sshLikeConf = portDomain[0] + ':' + portDomain[1] + ':' + portDomain[0]
		res.append(sshLikeConf)
	return res

def getCmdPrefix():
	config = getConfig()
	if config['AUTOSSH'] == True:
		cmd = 'autossh'
	else:
		cmd = 'ssh'
	if config['SERVER_PORT'] != 22:
		cmd += ' -p ' + str(config['SERVER_PORT'])
	cmd += ' -fN'
	cmd += ' -i ' + config['SERVER_KEY']
	return cmd

def getCmdSuffix():
	config = getConfig()
	suffix = config['SERVER_USER'] + '@' + config['SERVER_IP']
	return suffix

def getTunels():
	prostredek = []
	forwards = getForForward()
	for forward in forwards:
		prostredek.append(forward)
	return prostredek

def getBadIP():
	return getConfig()['BAD_IP']

def getDomains():
	domains = []
	forwards = getForForward()
	for forward in forwards:
		domains.append(forward.split(':')[1])
	return domains
