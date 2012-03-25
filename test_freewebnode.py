#!/usr/bin/python

from freewebnode import FreeWebNode
import unittest

class TestFreeWebNode(unittest.TestCase):

	def setUp(self):
		self.freewebnode = FreeWebNode()
		self.freewebnode.loadFriendList()
		self.freewebnode.loadRules()

	def test_loadFriendList(self):
		self.freewebnode.loadFriendList()
		self.assertIsNotNone(self.freewebnode.friendList)

	def test_loadRules(self):
		self.freewebnode.loadRules()
		self.assertIsNotNone(self.freewebnode.rules)

	def test_checkAllFriendRequests(self):
		self.freewebnode.checkAllFriendRequests()

	def test_checkRequestPage(self):
		self.freewebnode.checkRequestPage('Bob')

	def test_checkRules(self):
		allowed = self.freewebnode.checkRules('Bob', 'http://en.wikipedia.org/')
		self.assertFalse(allowed)

	def test_fulfillRequest(self):
		self.freewebnode.fulfillRequest('http://en.wikipedia.org/')

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()

