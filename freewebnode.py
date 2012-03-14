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
			if u'key' in friend:
				self.checkRequestPage(friend)
		pass

	def checkRequestPage(self, friend):
		# fetch page at friend[u'key']
		# parse request list
		# for each request
			# if checkRules(friend[u'name'], requestUrl):
				# fulfillRequest(requestUrl)
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

