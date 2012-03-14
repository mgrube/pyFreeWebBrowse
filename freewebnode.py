#!/usr/bin/python

import json

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
			if 'key' in friend:
				self.checkRequestPage(friend['key'])
		pass

	def checkRequestPage(self, requestPageUri):
		# fetch page at requestPageUri
		# parse request list
		# for each request
			# if rules allow it,
				# fulfillRequest(url)
		pass

	def fulfillRequest(self, url):
		# urllib.urlretrieve(url, dest)
		# uriPub = createFreesite(sitemgr, sitename, sitedir)
		# publish fulfillment list???
		pass

if __name__ == "__main__":
	# test
	node = FreeWebNode()
	node.loadFriendList()
	node.loadRules()
	node.checkAllFriendRequests()
	pass

