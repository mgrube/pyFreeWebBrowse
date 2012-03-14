#!/usr/bin/python

import json

print "Web URL to match?"
url = raw_input()

print "Allow anyone to request this URL (y/n)?"
allowAny = raw_input()

allowList = []
if allowAny == 'n':
	while True:
		print "Type name of friend to add to allow list:"
		friend = raw_input()
		allowList.append(friend)
		print "Add another (y/n)?"
		resp = raw_input()
		if resp != 'y':
			break

# read current rules list
try:
	f = open('rules.conf', 'r')
	f_text = f.read()
	f.close()
	rules = json.loads(f_text)
except IOError as e:
	rules = {}

rule = {"allow_any": allowAny, "allow_list": allowList}

# append new rule to rules list
rules[url] = rule

# write new rules list to disk
text = json.dumps(rules)
f = open('rules.conf', 'w')
f.write(text)
f.close()

