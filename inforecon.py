#! /usr/bin/python3

""" Inforecon: from Udemy "Python for Penetration Testers: section 1"   """

import sys
import requests
import socket
import json

if len (sys.argv) < 2:
	print("Usage:  ", sys.argv[0], "<url>")
	sys.exit(1)

req = requests.get("http://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is " + gethostby_)

req_two = requests.get("http://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)

print("\nLocation: " + resp_['loc'])
print("\nRegion: " + resp_['region'])
print("\nCity: " + resp_['city'])
print("\nCountry: " + resp_['country'] + "\n")

