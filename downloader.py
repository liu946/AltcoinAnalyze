import os
import json
import time

while True:
	print 'Downloading started at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
	dur_a = time.time()
	
	# Read config.json
	try:
		fp = open('config.json', 'r')
		config = json.loads(fp.readline())
		fp.close()
		repo_dir, cache_dir, sync_rate = config['repo_dir'], config['cache_dir'], config['sync_rate']
	except:
		print 'Read config.json failed!'
		exit(1)
	
	# Read altcoins.json
	try:
		fp = open('altcoins.json', 'r')
		altcoins = json.loads(fp.readline())
		fp.close()
	except:
		print 'Read altcoins.json failed!'
		exit(1)
	
	# Clone or sync altcoins repo
	try:
		fp = open('cache.json', 'w')
	except:
		print 'Failed to create/open cache.json!'
		
	fp.write('{')
	for i in altcoins.keys():
		if os.path.exists('./%s' % i):
			print 'Syncing "%s" repo...' % i
			try:
				os.popen('cd %s; git fetch; cd ..' % (repo_dir + i), 'r')
				print 'Repo "%s" synced successful!' % i
			except:
				print 'Repo "%s" synced failed!' % i
		else:
			print 'Cloning "%s" repo...' % i
			try:
				os.system('git clone %s %s' % (altcoins[i]['repo_url'], repo_dir + i))
				print 'Repo "%s" cloned successful!' % i
			except:
				print 'Repo "%s" cloned failed!' % i
		fp.write('"%s": {"repo_dir": "%s", "update_date": "%s"}%s' % (i, repo_dir + i, time.strftime('%Y-%m-%d %H:%M:%S'), "" if i == altcoins.keys()[-1] else ", "))
	fp.close()
	
	print '\nAll altcoins repos have been cloned/synced at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
	dur_b = time.time()
	print 'Time used %fs.' % (dur_b - dur_a)
	time.sleep(sync_rate)
	print '\n'
