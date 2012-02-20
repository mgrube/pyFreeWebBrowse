#!/usr/bin/python

import sys, time, json
import os, errno

from fcp.sitemgr import SiteMgr, fixUri

# add a request for a web site to be uploaded to freenet
def addRequest(url):
	# read current request list
	try:
		f = open('fwb-requests/requests.json', 'r')
		f_text = f.read()
		f.close()
		requestList = json.loads(f_text)
	except IOError as e:
		requestList = []

	# build the request
	now = time.time()
	request = {"url": url, "request-time": now}

	# append new request to request list
	requestList.append(request)

	# write new request list to disk
	text = json.dumps(requestList)
	try:
		os.makedirs('fwb-requests')	# create folder
	except OSError, e:
		if e.errno != errno.EEXIST:	# folder already exists, np
			raise
	f = open('fwb-requests/requests.json', 'w')
	f.write(text)
	f.close()

	# TODO: add or update freesite for request list
	pass

if __name__ == "__main__":
	if (len(sys.argv) == 1):
		print "Usage: ./addRequest <url>"
	else:
		addRequest(sys.argv[1])

