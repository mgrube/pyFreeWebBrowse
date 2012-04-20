#!/usr/bin/python

import sys, time, json
import os, errno

from freesitetools import *
from fcp.sitemgr import SiteMgr, fixUri

# add a request for a web site to be uploaded to freenet
def addRequest(url):
	sitename = 'fwb-requests'
	sitemgr = SiteMgr()

	# read current request list
	try:
		f = open(sitename + '/requests.json', 'r')
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
		os.makedirs(sitename)		# create folder
	except OSError, e:
		if e.errno != errno.EEXIST:	# folder already exists
			raise
	f = open(sitename + '/requests.json', 'w')
	f.write(text)
	f.close()

	# add index if it doesn't already exist
	try:
		f = open(sitename + '/index.html', 'r')
	except IOError as e:
		f = open(sitename + '/index.html', 'w')
		f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
	<title>pyFreeWebBrowse Request Page</title>
</head>

<body>
	<a href="requests.json">Requests</a>
</body>
</html>
			''')
		f.close()

	# add or update freesite for request list
	if sitename in getFreesiteNames(sitemgr):
		updateFreesite(sitemgr, sitename)
	else:
		uriPub = createFreesite(sitemgr, sitename, sitename)
		return uriPub


if __name__ == "__main__":
	if (len(sys.argv) == 1):
		print "Usage: ./addRequest <url>"
	else:
		uriPub = addRequest(sys.argv[1])
		if uriPub == None:
			print '\nPublished request'
		else:
			print '\nPublished request to:', uriPub
			f = open('request-key.txt', 'w')
			f.write(uriPub)
			f.close()

