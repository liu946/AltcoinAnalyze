# -*- coding: UTF-8 -*-
##use - pybrain

# from github API 
# "coin" "size" "star" "network" "subscriber"
import json
import httplib2
# from pybrain.tools.shortcuts import buildNetwork
# from pybrain.datasets import supervised

# net = buildNetwork(12,15,1)
# ds = supervised.SupervisedDataSet(12,1)

# coindata = json.load(open("data.json"))
# coininfo = json.load(open("altcoinsinfo.json"))

# Download form GITHUB API
def firstkey(dic):
	for i in dic:
		return i
#https://api.github.com/repos/bitcoin/bitcoin
coinurl={}

coinurlinfo = json.load(open("altcoins.json"))
for coin in coinurlinfo:
	url=firstkey(coinurlinfo[coin]["repo_url"])
	url=url.replace(".git","")
	url=url.replace("https://github.com/","https://api.github.com/repos/")
	print url
	r,c = httplib2.Http().request(url)
	data = json.load(c)




# for coin in coindata:
# 	print coin , " - " #, coindata[coin]

# 	ds.addSample(())
# for coin in coininfo:
# 	print coin , " - "
