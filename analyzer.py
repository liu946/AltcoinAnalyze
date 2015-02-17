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
from pylab import * # 此处引入pylab出错，暂时注释
from math import *
class Analyzer:
	"""docstring for Analyzer"""
	globaldata=[] # 用于创造dataframe的准备数据 [{},{},{},{}]型
	globaldatalist=[]	# 用于主成分分析 [[],[],[]] 型
	datalist=[]   # 币名（list）
	meandatacol=[] # 评判项
	meandatacolweight=[]#归一化权重
	meandatacolweightOrigin=[]#原始权重用于乘方
	def __init__(self, arg="config.json"):
		'''loading data '''
		self.config=json.load(open(arg))
		self.maklist= json.load(open("altcoinsinfo.json")) 
		self.reloadfile("stats.json")
		self.refreshdatalist()
		self.normalization()
		self.summarypca()
		self.summaryradar()
		self.exportjs()
		self.coinhtml()

		
	def reloadfile(self,filename):
		'''重新加载数据'''
		# 获取github api数据
		# 获取gitstats 数据文件
		self.coindata = json.load(open(filename))

		# 人为挑选有意义的数据项，数据文件在 config.json
		# maindatacol 为 全部数据项名（list）
		self.meaningcol=self.config["stats_factors"]
		self.meaningcolinsf=self.config["api_factors"]
		self.meandatacol=self.meaningcol+self.meaningcolinsf
		self.meandatacolweightOrigin=self.config["stats_factors_weight"]+self.config["api_factors_weight"]
		sumweight=sum(self.meandatacolweightOrigin)/1.0;
		self.meandatacolweight=[ i/sumweight for i in self.meandatacolweightOrigin ]
		print self.globaldata,"\n\n\n", self.globaldatalist

	def pca(self,data,nRedDim=0,normalise=1):
   
	    # 数据标准化
	    m = mean(data,axis=0)# mean axis=0 可以计算每一列的平均值
	    data -= m
	    # 协方差矩阵
	    C = cov(transpose(data)) #转置之后， 计算相关性矩阵covariance，协方差R={rij}
	    # 计算特征值特征向量，按降序排序
	    evals,evecs = linalg.eig(C)
	    # print evals
	    indices = argsort(evals) # 按照labuda排序 eval是labuda
	    indices = indices[::-1] # 倒序
	    evecs = evecs[:,indices] # 利用index排序

	    revals=[]
	    revals.extend( evals)
	    evals = evals[indices] 
	    if nRedDim>0:
	        evecs = evecs[:,:nRedDim]
	   
	    if normalise:
	        for i in range(shape(evecs)[1]):
	            evecs[:,i] / linalg.norm(evecs[:,i]) * sqrt(evals[i])
	    # 产生新的数据矩阵
	    x = dot(transpose(evecs),transpose(data)) #dot 点乘
	    # 重新计算原数据
	    y=transpose(dot(evecs,x))+m
	    return x,y,revals,evecs

	def refreshdatalist(self):
		for xcoin in self.coindata:
			_data={} #生成globaldata中的子{}
			_datalist=[] #生成 globaldatalist 中的子 []
			for xcol in self.meaningcol:
				_data[xcol] = self.coindata[xcoin][xcol]
				_datalist.append(self.coindata[xcoin][xcol])
			for xcol in self.meaningcolinsf:
				if xcol in self.coindata[xcoin]:
					_data[xcol] = self.coindata[xcoin][xcol]
					_datalist.append(self.coindata[xcoin][xcol])
				else:
					print xcoin ,xcol,"<!!! error : 无法匹配载入，github api数据文件没有“",xcoin,"”>"
			# print xcoin," : ",_data
			self.datalist.append(xcoin)
			self.globaldata.append(_data)
			self.globaldatalist.append(_datalist)
		# table 型数据
		self.datafream=pd.DataFrame(self.globaldata,index=self.datalist)

	def normalization(self):
		##############
		#归一化整理
		#方法1，标准分
		self.stdscore = (self.datafream-self.datafream.describe().loc['mean',:])/self.datafream.describe().loc['std',:]

		#方法2，/最大值
		self.divmax = self.datafream / self.datafream.describe().loc['max',:]

	def summarypca(self):
		##############
		#主成分分析
		x,y,evals,evecs = self.pca(self.globaldatalist,1)

		# # 贡献律
		# gxpersent = evals/sum(evals)
		# print "贡献率：\n"
		# for i in range(0,gxpersent.__len__()):
		# 	print maindatacol[i]," : ",gxpersent[i],"\n"

		# 一维化数据
		dattest={}
		print "一维化数据方式1（主成分分析）：\n"
		for i in range(0,x[0].__len__()):
			print self.datalist[i]," : ",x[0][i],"\n"
			dattest[self.datalist[i]] =x[0][i]

		for i in self.maklist:
			if i["name"] in dattest:
				print i['name'] , " : ",dattest[i['name']]

	def summaryradar(self):
		
		#准备角度
		sita = [ 2 * 3.142 * i for i in  self.meandatacolweight]
		#准备列
		sumarray=[]
		mularray=[]
		for i in range(0, self.divmax.index.__len__() ):
			sumarea=0
			mul=1
			for j in range(0, self.divmax.columns.__len__()):
				sumarea+= self.divmax.iloc[i,j] * self.divmax.iloc[i,j-1] * sin(sita[j])
				mul*= (self.divmax.iloc[i,j]+1) ** self.meandatacolweightOrigin[j]
			sumarray.append(sumarea)
			mularray.append(mul)
		self.datafream.loc[:,'area']=sumarray
		self.datafream.loc[:,"mul"]=mularray
		self.divmax.loc[:,"area"]=[i/float(max(sumarray)) for i in sumarray]
		self.divmax.loc[:,"mul"]=[i/float(max(mularray)) for i in mularray]

		print "方式2（雷达图面积）：\n"
		# 输出雷达图面积
		for i in self.maklist:
			if i["name"] in self.datalist:
				print i['name'] , " : ",self.datafream.loc[i['name'],'area']

		# 输出雷达图 html 图形
		filehandle = open("./html/radar_data.js","w")

		for i in self.maklist:
			if i["name"] in self.datalist:
				filehandle.write(''' var %s = AmCharts.makeChart("%s", {
						type: "radar",
						theme: "chalk",
						dataProvider: [\t
					''' %(i["name"],i["name"]))
				for j in range(0,self.datafream.columns.__len__()-1):
					filehandle.write('''{
								"item": "%s",
								"data": %lf
						}'''%(self.datafream.columns[j],self.divmax.loc[i['name'],:][j]))
					if j!= self.datafream.columns.__len__()-2:
						filehandle.write(',')
				filehandle.write(open("./html/tpl/jsconfig.tpl").read())
		filehandle.close()
		filehandle=open("./html/radar_data.html","w")
		filehandle.write(open("./html/tpl/header.html").read())
		for i in self.maklist:
			if i["name"] in self.datalist:
				filehandle.write("<div>%s<pre>%s</pre></div>"% (i['name'],self.datafream.loc[i['name'],:]))
				filehandle.write("<div>%s<pre>%s</pre></div>"% (i['name'],self.divmax.loc[i['name'],:]))
				filehandle.write('''<div id="%s" style="width:600px; height:400px;"></div>\n<hr>'''% i['name'])
		
		filehandle.write(open("./html/tpl/footer.html").read())
		filehandle.close()

		#################
		# 第二版 table展示
		#################
		filehandle=open("./html/table_data.html","w")
		filehandle.write(open("./html/tpl/header.html").read())
		filehandle.write('''
			<style type=\"text/css\">th{width:%s%%;}</style>
			<table><tbody><tr><th>CoinName</th>'''% int(100/(1+self.datafream.iloc[0,:].__len__())))
		for i in self.meandatacol:
			filehandle.write("<th>%s</th>"%i)

		filehandle.write("<th>RadarArea</th><th>Mul</th>")
		filehandle.write("</tr>")
		for i in self.maklist:
			if i["name"] in self.datalist:
				filehandle.write("<tr><th>%s</th>"%i["name"])
				for j in range(0,self.datafream.loc[i['name'],:].__len__()):
					filehandle.write("<td style=\"background-color: rgba(255,125,0,%2f);\">%1f</td>"% (self.divmax.loc[i['name'],:][j],self.datafream.loc[i['name'],:][j]))
					
				filehandle.write("</tr>")

		filehandle.write("</tbody></table>")
		filehandle.write(open("./html/tpl/footer.html").read())
		filehandle.close()

	def exportjs(self):
		jsfile = open('html/data.js','w')
		#jsfile.write('globaldata = '+json.dumps(self.globaldata)+';')
		divdata ={}
		tempdic = self.divmax.T.to_dict()
		for k,v in zip(tempdic.iterkeys(), tempdic.itervalues()):
			divdata[k]=v.values()

		jsfile.write('divmax = '+json.dumps(divdata)+';')
		#jsfile.write('globaldatalist = '+json.dumps(self.globaldatalist)+';')
		jsfile.write('datalist = '+json.dumps(self.datalist)+';')
		jsfile.write('meandatacol = '+json.dumps(self.meandatacol)+';')
		jsfile.write('meandatacolweight = '+json.dumps(self.meandatacolweight)+';')
		#jsfile.write('meandatacolweightOrigin = '+json.dumps(self.meandatacolweightOrigin)+';')
		jsfile.close()

	def coinhtml(self):
		coinfile = open('html/radar.html','w');
		coinfile.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>coin data with radar graphic </title>
	<script type="text/javascript" src='data.js'></script>
</head>
<body>''')
		for coin in self.datalist:
			coinfile.write("	<canvas id='%s' width='500' height='500'></canvas>\n" %coin)
		
		coinfile.write('''	<script type="text/javascript" src='radarhtml5.js'></script>
</body>
</html>
		''')
		coinfile.close()

if __name__ == "__main__":
	Analyzer()
