#!/usr/bin/python

import json

print "Friend's nickname?"
name = raw_input()

print "Friend's request page USK?"
key = raw_input()

# read current friend list
try:
	f = open('friends.conf', 'r')
	f_text = f.read()
	f.close()
	friendList = json.loads(f_text)
except IOError as e:
	friendList = []

friend = {"name": name, "key": key}

# append new friend to friend list
friendList.append(friend)

# write new friend list to disk
text = json.dumps(friendList)
f = open('friends.conf', 'w')
f.write(text)
f.close()

