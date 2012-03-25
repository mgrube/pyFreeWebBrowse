#!/usr/bin/python

from fcp_util import *
import unittest

class TestFcpUtil(unittest.TestCase):
	def test_fcp_get(self):
		key_uri = "USK@nwa8lHa271k2QvJ8aa0Ov7IHAV-DFOCFgmDt3X6BpCI,DuQSUZiI~agF8c-6tjsFFGuZ8eICrzWCILB60nT8KKo,AQACAAE/sone/51/"
		data = fcp_get(key_uri)
		self.assertIsNotNone(data)

if __name__ == '__main__':
	unittest.main()

