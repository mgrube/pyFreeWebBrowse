from fcp import node
import sys

# mostly copied from pyFreenet's get.py
def fcp_get(key_uri):
	# default job options
	fcpHost = node.defaultFCPHost
	fcpPort = node.defaultFCPPort
	Global = False
	verbosity = node.ERROR

	if not key_uri.startswith("freenet:"):
		key_uri = "freenet:" + key_uri

	# create the node
	n = node.FCPNode(host=fcpHost,
			 port=fcpPort,
			 Global=Global,
			 verbosity=verbosity,
			 logfile=sys.stderr)

	# retrieve the key
	mimetype, data, msg = n.get(key_uri)
	n.shutdown()

	return data

if __name__ == "__main__":
	key_uri = "USK@nwa8lHa271k2QvJ8aa0Ov7IHAV-DFOCFgmDt3X6BpCI,DuQSUZiI~agF8c-6tjsFFGuZ8eICrzWCILB60nT8KKo,AQACAAE/sone/51/"
	data = fcp_get(key_uri)
	print data

