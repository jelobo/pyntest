#! /usr/bin/python
# -*-coding:utf-8 -*

""" Scan Wifi and detect AP vi BSS frame
	Cf. http://https://www.shellvoide.com/python/how-to-code-a-simple-wireless-sniffer-in-python/"""

import threading, os, time, random
from scapy.all import *

F_bssids = []    # Found BSSIDs

def monitor(iface):
	os.system('ifconfig %s down' %iface)
	os.system('iwconfig %s mode monitor' %iface)
	os.system('ifconfig %s up' %iface)

def hopper(iface):
	n = 1
	stop_hopper = False
	while not stop_hopper:
        	time.sleep(0.50)
	        os.system('iwconfig %s channel %d' % (iface, n))
        	dig = int(random.random() * 14)
	        if dig != 0 and dig != n:
        	    n = dig

def findSSID(pkt):
	if pkt.haslayer(Dot11Beacon):
		if pkt.getlayer(Dot11).addr2 not in F_bssids:
			F_bssids.append(pkt.getlayer(Dot11).addr2)
			ssid = pkt.getlayer(Dot11Elt).info
			if ssid == '' or pkt.getlayer(Dot11Elt).ID != 0:
				print "Hidden Network Detected"
			print "Network Detected: %s" % (ssid)

if __name__ == "__main__":
	interface = "wlan0"
	monitor(interface)
	thread = threading.Thread(target=hopper, args=(interface, ), name="hopper")
	thread.daemon = True
	thread.start()

	sniff(iface=interface, prn=findSSID)
