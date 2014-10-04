# -*- coding: UTF-8 -*-
# ---------
# Author liu 
# 14.10.4
# ---------
# some meaning cols : "stargazers_count","subscribers_count","network_count","open_issues_count"
# 						--star 				--watching			--fork		
#
# 			"TotalCommits","ActiveDays","ActiveDaysPercentage","TotalAuthors","TotalTags"
# ---------

import json
import pandas as pd
from numpy import *
from pylab import *
from pca import pca

# 获取github api数据文件
data=json.load(open("starfork.json"))
# 获取gitstats 数据文件
coindata = json.load(open("data.json"))

# 人为挑选有意义的数据项
# maindatacol 为 全部数据项名（list）
mainingcol=["TotalCommits","ActiveDays","ActiveDaysPercentage","TotalAuthors","TotalTags"]
mainingcolinsf=["stargazers_count","watchers_count","forks","open_issues_count"]
maindatacol=mainingcol+mainingcolinsf

globaldata=[] # 用于创造dataframe的准备数据 [{},{},{},{}]型
globaldatalist=[]	# 用于主成分分析 [[],[],[]] 型
datalist=[]   # 币名（list）

for xcoin in coindata:
	_data={} #生成globaldata中的子{}
	_datalist=[] #生成 globaldatalist 中的子 []
	for xcol in mainingcol:
		_data[xcol] = coindata[xcoin][xcol]
		_datalist.append(coindata[xcoin][xcol])
	for xcol in mainingcolinsf:
		if xcol in data[xcoin]:
			_data[xcol] = data[xcoin][xcol]
			_datalist.append(data[xcoin][xcol])
		else:
			print xcoin ,xcol,"<!!! error : 无法匹配载入，github api数据文件没有“",xcoin,"”>"
	# print xcoin," : ",_data
	datalist.append(xcoin)
	globaldata.append(_data)
	globaldatalist.append(_datalist)
	
# print globaldatalist
# table 型数据
summary= []
df=pd.DataFrame(globaldata,index=datalist)
for i in datalist:
	summary.append( (df.loc[i,:]-df.describe().loc['mean',:])/df.describe().loc['std',:] )
dt = pd.DataFrame( summary, index=datalist )

x,y,evals,evecs = pca(globaldatalist,1)

# # 贡献律
# gxpersent = evals/sum(evals)
# print "贡献率：\n"
# for i in range(0,gxpersent.__len__()):
# 	print maindatacol[i]," : ",gxpersent[i],"\n"

# 一维化数据
dattest={}
print "一维化数据：\n"
for i in range(0,x[0].__len__()):
	print datalist[i]," : ",x[0][i],"\n"
	dattest[datalist[i]] =x[0][i]

maklist= json.load(open("altcoinsinfo.json")) 
for i in maklist:
	if i["name"] in dattest:
		print i['name'] , " : ",dattest[i['name']]


