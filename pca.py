#-*- coding:utf-8 -*-
from pylab import *
from numpy import *
def pca(data,nRedDim=0,normalise=1):
   
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