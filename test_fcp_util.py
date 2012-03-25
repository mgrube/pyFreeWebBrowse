#!/usr/bin/python

from fcp_util import *
import unittest

class TestFcpUtil(unittest.TestCase):
	def test_fcp_get(self):
		key_uri = "USK@nwa8lHa271k2QvJ8aa0Ov7IHAV-DFOCFgmDt3X6BpCI,DuQSUZiI~agF8c-6tjsFFGuZ8eICrzWCILB60nT8KKo,AQACAAE/sone/51/"
		mimetype, data, msg = fcp_get(key_uri)
		self.assertIsNotNone(mimetype)
		self.assertIsNotNone(data)
		self.assertIsNotNone(msg)

if __name__ == '__main__':
	unittest.main()

