# -*- coding: UTF-8 -*-

# ---------
# Author liu 
# 14.10.2
# ---------
# For downloading data form github api
# some meaning cols : "stargazers_count","subscribers_count","network_count","open_issues_count"
# 						--star 				--watching			--fork		
# --------
# output file
# starfork.json
# ---------

import json
import httplib2
def count(dicorlist):
	i=0;

	for a in dicorlist:
		i+=1

	return i

def firstkey(dic):
	for i in dic:
		return i
coinurl={}
data={}
coinurlinfo = json.load(open("altcoins.json"))
for coin in coinurlinfo:
	url=firstkey(coinurlinfo[coin]["repo_url"])
	url=url.replace(".git","")
	url=url.replace("https://github.com/","https://api.github.com/repos/")
	print url
	r,c = httplib2.Http().request(url)
	data[coin] = json.loads(c)

f=open("starfork.json",'w')
f.write(json.dumps(data))