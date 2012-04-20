#!/usr/bin/python

from fcp_util import *
from freesitetools import *
from fcp.sitemgr import SiteMgr
import json
import urllib
import os, shutil, time
import hashlib

class FreeWebNode:

	def loadFriendList(self):
		try:
			f = open('friends.conf', 'r')
			f_text = f.read()
			f.close()
			self.friendList = json.loads(f_text)
		except IOError as e:
			self.friendList = []

	def loadRules(self):
		try:
			f = open('rules.conf', 'r')
			f_text = f.read()
			f.close()
			self.rules = json.loads(f_text)
		except IOError as e:
			self.rules = {}

	def checkAllFriendRequests(self):
		for friend in self.friendList:
			if u'key' in friend:
				self.checkRequestPage(friend)
		pass

	def checkRequestPage(self, friend):
		# fetch friend's request list
		try:
			mimetype, data, msg = fcp_get(friend[u'key'])
		except:
			# TODO: log error message
			return

		# parse request list
		requestList = json.loads(data)

		for request in requestList:
			requestUrl = request[u'url']
			if checkRules(friend[u'name'], requestUrl):
				uriPub = fulfillRequest(requestUrl)
		if uriPub != None:
			f = open('fulfill-key.txt', 'w')
			f.write(uriPub)
			f.close()

			# TODO: forward this request to other friends if not fulfilled here?
		pass

	# returns true if allowed, false if denied
	def checkRules(self, friendName, requestUrl):

		# check if we can match the whole url
		if requestUrl in self.rules:
			rule = self.rules[requestUrl]
			if rule[u'allow_any'] == 'y':
				return True
			if friendName in rule[u'allow_list']:
				return True
			return False

		# check to match longest left-side portion of the url
		for i in range(len(requestUrl)):
			if requestUrl[:-(i+1)] in self.rules:
				rule = self.rules[requestUrl[:-(i+1)]]
				if rule[u'allow_any'] == 'y':
					return True
				if friendName in rule[u'allow_list']:
					return True
				return False
		return False

	def fulfillRequest(self, url):
		m = hashlib.md5()
		m.update(url)
		sitename = m.hexdigest()
		sitedir = 'fwb-temp'
		sitemgr = SiteMgr()

		# publish requested url
		if os.path.exists(sitedir):
			if os.path.isdir(sitedir):
				shutil.rmtree(sitedir)
			else:
				os.remove(sitedir)
		os.makedirs(sitedir)
		urllib.urlretrieve(url, sitedir + "/index.html")
		if sitename in getFreesiteNames(sitemgr):
			updateFreesite(sitemgr, sitename)
		else:
			uriPub = createFreesite(sitemgr, sitename, sitedir)

		# publish fulfillment list
		fsitename = 'fwb-fulfill'

		# read current fulfill list
		try:
			f = open(fsitename + '/fulfill.json', 'r')
			f_text = f.read()
			f.close()
			fulfillList = json.loads(f_text)
		except IOError as e:
			fulfillList = []
		pass

		# build the fulfill object
		now = time.time()
		found = False
		for f in fulfillList:
			if f["www-url"] == url:
				f["fulfill-time"] = now
				found = True
		if found == False:
			fulfill = {"www-url": url, "key-uri": uriPub, "fulfill-time": now}
			fulfillList.append(fulfill)

		# write new fulfill list to disk
		text = json.dumps(fulfillList)
		try:
			os.makedirs(fsitename)		# create folder
		except OSError, e:
			if e.errno != errno.EEXIST:	# folder already exists
				raise
		f = open(fsitename + '/fulfill.json', 'w')
		f.write(text)
		f.close()

		# add index if it doesn't already exist
		try:
			f = open(fsitename + '/index.html', 'r')
		except IOError as e:
			f = open(fsitename + '/index.html', 'w')
			f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
        <title>pyFreeWebBrowse Fulfill Page</title>
</head>

<body>
        <a href="fulfill.json">Fulfilled Requests</a>
</body>
</html>
				''')
			f.close()

		# add or update freesite for fulfill list
		if fsitename in getFreesiteNames(sitemgr):
			updateFreesite(sitemgr, fsitename)
		else:
			uriPub = createFreesite(sitemgr, fsitename, fsitename)
			return uriPub


if __name__ == "__main__":
	# test
	node = FreeWebNode()
	node.loadFriendList()
	node.loadRules()
	node.checkAllFriendRequests()
	pass

