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

	def loadRulesList(self):
		try:
			f = open('rules.conf', 'r')
			f_text = f.read()
			f.close()
			self.rulesList = json.loads(f_text)
		except IOError as e:
			self.rulesList = []

	def checkAllFriendRequests(self):
		for friend in self.friendList:
			if 'key' in friend:
				self.checkRequestPage(friend['key'])
		pass

	def checkRequestPage(self, requestUri):
		# fetch page at requestUri
		# parse request list
		# for each request
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
	node.loadRulesList()
	node.checkAllFriendRequests()
	pass

