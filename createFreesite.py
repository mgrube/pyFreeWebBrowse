#!/usr/bin/python

import os, urllib

from fcp.sitemgr import SiteMgr, fixUri

# create a new freesite
# freesite files  must be stored in a folder with an index.html
# mostly copied from freesitemgr
def createFreesite(sitemgr, sitename, sitedir):

	if not sitemgr.node:
		raise Exception("Cannot connect to node on %s:%s" % (sitemgr.fcpHost, sitemgr.fcpPort))

	if sitemgr.hasSite(sitename):
		raise Exception("Freesite '%s' already exists" % sitename)

	if not sitedir:
		raise Exception("Invalid sitedir")

	sitedir = os.path.abspath(sitedir)
	if not os.path.isdir(sitedir):
		raise Exception("'%s' is not a directory" % sitedir)
	elif not os.path.isfile(os.path.join(sitedir, sitemgr.index)):
		raise Exception("'%s' has no %s" % (sitedir, sitemgr.index))

	uriPub, uriPriv = sitemgr.node.genkey()
	uriPub = fixUri(uriPub, sitename)
	uriPriv = fixUri(uriPriv, sitename)

	sitemgr.addSite(name=sitename, dir=sitedir, uriPub=uriPub, uriPriv=uriPriv)
	print "Added new freesite: '%s' => %s" % (sitename, sitedir)

if __name__ == "__main__":
	sitemgr = SiteMgr()
	sitename = "fwb-test"
	sitedir = os.path.abspath(sitename)

	if sitemgr.hasSite(sitename):
		sitemgr.removeSite(sitename)

	if not os.path.exists(sitedir):
		os.makedirs(sitedir)
	urllib.urlretrieve("https://secure.wikimedia.org/wikipedia/en/wiki/Main_Page", sitedir + "/index.html")
	createFreesite(sitemgr, sitename, sitedir)

