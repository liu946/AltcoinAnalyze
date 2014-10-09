# -*- coding: UTF-8 -*-

import os
import json
import time
import httplib2

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
		
		return config['repo_dir'], config['cache_dir'], config['gitstats_dir'], altcoins
	
	def get_altcoinsinfo(self):
		os.popen('rm altcoinsinfo.json; cd altcoinsinfo; scrapy crawl altcoins -o ../altcoinsinfo.json; cd ..' )
		info = json.load(open('altcoinsinfo.json', 'r'))
		
		# fix the info format
		for i in info:
			i['market_cap'] = int(i['market_cap'][0].replace(' ', '').replace(r'\n', '').replace(',', '').replace('$', ''))
			i['name'] = i['name'][0]
			i['rank'] = int(i['rank'][0].replace(' ', '').replace('\n', '').replace(',', ''))

		json.dump(info, open('altcoinsinfo.json', 'w'))
	
	def extract_gitstats(self, src, dst):
		os.system('./git-stats-json "%s" "%s"' % (src, dst))
	
	def download(self):
		# Initialize
		print 'Download start at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
		repo_dir, cache_dir, gitstats_dir, altcoins = self.init()
		print 'Initialized successful!'
		altcoins_sum = len(altcoins)
		print '%d altcoins repos to be cloned/synced:' % altcoins_sum
		
		# Clone/Sync altcoins repo
		dur_a = time.time()
		
		stats = {}
		obj = {}
		altcoins_count = 1
		for altcoin in altcoins.keys():
			stats[altcoin] = {}
			obj[altcoin] = {}
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
				
				print 'Gathering data of "%s"-"%s"' % (altcoin, repo_name)
				self.extract_gitstats(repo_dir + altcoin + '/' + repo_name, gitstats_dir + altcoin + '/' + repo_name)
				
				try:
					fp = open(gitstats_dir + altcoin + '/' + repo_name + '/stats.json', 'r')
					stats[altcoin][repo_name] = json.loads(fp.read())
					fp.close()
				except:
					print 'Failed to read ' + gitstats_dir + altcoin + '/' + repo_name + '/stats.json'
				
				url = repo.replace(".git","").replace("https://github.com/","https://api.github.com/repos/")
				tmp1, tmp2 = httplib2.Http().request(url)
				stats[altcoin][repo_name].update(json.loads(tmp2))
				
				print 'Done!'
				
				obj[altcoin][repo_name] = {'repo_dir': repo_dir + altcoin + '/' + repo_name, 'update_date': time.strftime('%Y-%m-%d %H:%M:%S')}
				repos_count += 1
			altcoins_count += 1
		
		try:
			fp = open('cache.json', 'w')
			fp.write(json.dumps(obj, indent = 4))
			fp.close()
		except:
			print 'Failed to create/open cache.json!'
			
		try:
			fp = open('stats.json', 'w')
			fp.write(json.dumps(stats, indent = 4))
			fp.close()
		except:
			print 'Failed to create/open stats.json!'
		
		
		print '\nAll altcoins repos have been cloned/synced at %s.' % time.strftime('%Y-%m-%d %H:%M:%S')
		print '\nFetching altcoins rank and market cap...'
		self.get_altcoinsinfo()
		print 'Successful!'
		dur_b = time.time()
		print 'Time used %fs.' % (dur_b - dur_a)
