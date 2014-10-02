# -*- coding: UTF-8 -*-
# ---------
# Author liu 
# 14.10.2
# ---------
# some meaning cols : "stargazers_count","subscribers_count","network_count","open_issues_count"
# 						--star 				--watching			--fork		
#
# 			"TotalCommits","ActiveDays","ActiveDaysPercentage","TotalAuthors","TotalTags"
# ---------

import json
import pandas as pd
import numpy as np

data=json.load(open("starfork.json"))
globaldata=[]
mainingcol=["TotalCommits","ActiveDays","ActiveDaysPercentage","TotalAuthors","TotalTags"]
mainingcolinsf=["stargazers_count","watchers_count","forks","open_issues_count"]
coindata = json.load(open("data.json"))
datalist=[]
coinindex=[]
for xcoin in coindata:
	_data={}
	for xcol in mainingcol:
		_data[xcol] = coindata[xcoin][xcol]
	for xcol in mainingcolinsf:
		if xcol in data[xcoin]:
			_data[xcol] = data[xcoin][xcol]
		else:
			print xcoin ,xcol
	# print xcoin," : ",_data
	datalist.append(xcoin)
	globaldata.append(_data)
	
df=pd.DataFrame(globaldata,index=datalist)
summary=[]
for i in datalist:
	summary.append( (df.loc[i,:]-df.describe().loc['mean',:])/df.describe().loc['std',:] )

print pd.DataFrame( summary, index=datalist )



