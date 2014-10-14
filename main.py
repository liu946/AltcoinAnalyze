# -*- coding: UTF-8 -*-

from downloader import Downloader
#import analyzer.py
# import visualizer.py
import os
import json
import time
import httplib2

while True:
	try:
		fp = open('config.json', 'r')
		config = json.loads(fp.read())
		sync_rate = config['sync_rate']
		fp.close()
	except:
		print 'Read config.json failed!'
		exit(1)
	
	# Download
	D = Downloader()
	D.download()
	
	# Analyze
	# -----------------
	
	# Visualize
	# -----------------
	
	time.sleep(sync_rate)