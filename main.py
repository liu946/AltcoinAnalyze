# -*- coding: UTF-8 -*-

from downloader import Downloader

from analyzer import Analyzer
import webbrowser
# import analyzer.py
# import visualizer.py
import os
import json
import time
import httplib2

while True:
	try:
		fp = open('config.json', 'r')
		config = json.loads(fp.read())
		sync = config['sync']
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
	A = Analyzer()
	
	# Visualize
	# -----------------
	A.exportjs()
	A.coinhtml()

	if not sync:

		webbrowser.open('./html/main.html', new=0, autoraise=True)
		exit(0)

	time.sleep(sync_rate)
