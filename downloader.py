# -*- coding: UTF-8 -*-

import os
import json
import time

class Downloader():
	def init(self):
		# Read config.json
		try:
			fp = open('config.json', 'r')
			config = json.loads(fp.read())
			fp.close()
		except:
			print 'Read config.json failed!'
			exit(1)
		
		# Read altcoins.json
		try:
			fp = open('altcoins.json', 'r')
			altcoins = json.loads(fp.read())
			fp.close()
		except:
			print 'Read altcoins.json failed!'
			exit(1)
		
		return config['repo_dir'], config['cache_dir'], config['sync_rate'], altcoins
	
	def get_altcoinsinfo(self):
		os.popen('rm altcoinsinfo.json; cd altcoinsinfo; scrapy crawl altcoins -o ../altcoinsinfo.json; cd ..' )
		info = json.load(open('altcoinsinfo.json', 'r'))
		for i in info:
			i['market_cap'] = int(i['market_cap'][0].replace(' ', '').replace(r'\n', '').replace(',', '').replace('$', ''))
			i['name'] = i['name'][0]
			i['rank'] = int(i['rank'][0].replace(' ', '').replace('\n', '').replace(',', ''))

		json.dump(info, open('altcoinsinfo.json', 'w'))
	
	def download(self):
		while True:
			print 'Download start at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
			repo_dir, cache_dir, sync_rate, altcoins = self.init()
			print 'Initialized successful!'
			altcoins_sum = len(altcoins)
			print '%d altcoins repos to be cloned/synced:' % altcoins_sum
			
			# Clone/Sync altcoins repo
			dur_a = time.time()
			
			try:
				fp = open('cache.json', 'w')
			except:
				print 'Failed to create/open cache.json!'
				
			fp.write('{')
			altcoins_count = 1
			for altcoin in altcoins.keys():
				fp.write('"%s": {' % altcoin)
				print 'Start Cloning/Syncing "%s" repo...(%d of %d)' % (altcoin, altcoins_count, altcoins_sum)
				if not os.path.exists('%s' % (repo_dir + altcoin)):
					os.system('mkdir "%s"' % (repo_dir + altcoin))
				
				repos_sum = len(altcoins[altcoin]['repo_url'])
				repos_count = 1
				for repo in altcoins[altcoin]['repo_url'].keys():
					repo_name = repo.split('/')[-1][:-4]
					if os.path.exists('%s/%s' % (repo_dir + altcoin, repo_name)):
						print 'Syncing "%s"-"%s"...(%d/%d)' % (altcoin, repo_name, repos_count, repos_sum)
						os.popen('cd "%s/%s"; git fetch' % (repo_dir + altcoin, repo_name))
						print 'Repo "%s"-"%s" synced successful!' % (altcoin, repo_name)
					else:
						print 'Cloning "%s"-"%s"...(%d/%d)' % (altcoin, repo_name, repos_count, repos_sum)
						os.system('git clone %s "%s/%s"' % (repo, repo_dir + altcoin, repo_name))
						print 'Repo "%s"-"%s" cloned successful!' % (altcoin, repo_name)
						
					fp.write('"%s": {"repo_dir": "%s", "update_date": "%s"%s' % (repo_name, repo_dir + altcoin + '/' + repo_name, time.strftime('%Y-%m-%d %H:%M:%S'), "}" if repo == altcoins[altcoin]['repo_url'].keys()[-1] else "}, "))
					repos_count += 1
				fp.write("%s" % "}}" if altcoin == altcoins.keys()[-1] else "}, ")
				altcoins_count += 1
			fp.close()
			
			print '\nAll altcoins repos have been cloned/synced at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
			print '\nFetching altcoins rank and market cap...'
			self.get_altcoinsinfo()
			print 'Successful!'
			dur_b = time.time()
			print 'Time used %fs.' % (dur_b - dur_a)
			time.sleep(sync_rate)
			print '\n'

D = Downloader()
D.download()
