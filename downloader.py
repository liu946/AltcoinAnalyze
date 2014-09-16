import os
import json

# init
fp = open('config.json', 'r')
config = json.loads(fp.readline())
fp.close()
repo_dir, cache_dir = config['repo_dir'], config['cache_dir']

fp = open('altcoins.json', 'r')
altcoins = json.loads(fp.readline())
fp.close()
for i in altcoins.keys():
	os.system('git clone %s %s' % (altcoins[i]['repo_url'], repo_dir + i))
