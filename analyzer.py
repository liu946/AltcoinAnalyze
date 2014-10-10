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
from math import *
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
	
# table 型数据

df=pd.DataFrame(globaldata,index=datalist)

##############
#归一化整理
#方法1，标准分
dt = (df-df.describe().loc['mean',:])/df.describe().loc['std',:]

#方法2，/最大值
do = df / df.describe().loc['max',:]


# ##############
# #主成分分析
# x,y,evals,evecs = pca(globaldatalist,1)

# # 贡献律
# gxpersent = evals/sum(evals)
# print "贡献率：\n"
# for i in range(0,gxpersent.__len__()):
# 	print maindatacol[i]," : ",gxpersent[i],"\n"

# 一维化数据
dattest={}
print "一维化数据方式1（主成分分析）：\n"
for i in range(0,x[0].__len__()):
	print datalist[i]," : ",x[0][i],"\n"
	dattest[datalist[i]] =x[0][i]

maklist= json.load(open("altcoinsinfo.json")) 
for i in maklist:
	if i["name"] in dattest:
		print i['name'] , " : ",dattest[i['name']]

############
# 雷达图面积法
# 贡献角度 平均。

#准备角度
sita = 2 * 3.142 / datalist.__len__()
#准备列
sumarray=[]
for i in range(0, do.index.__len__() ):
	sumarea=0
	for j in range(0, do.columns.__len__()):
		sumarea+= do.iloc[i,j] * do.iloc[i,j-1] * sin(sita)

	sumarray.append(sumarea)

do.loc[:,'area']=sumarray


print "方式2（雷达图面积）：\n"
# 输出雷达图面积
for i in maklist:
	if i["name"] in datalist:
		print i['name'] , " : ",do.loc[i['name'],'area']

# # 输出雷达图 html 图形
# filehandle = open("./html/radar_data.js","w")

# for i in maklist:
# 	if i["name"] in datalist:
# 		filehandle.write("")

# 		print i['name'] , " : ",do.loc[i['name'],'area']

# filehandle.write("")


# filehandle.close()
