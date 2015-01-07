library(jsonlite)
library(plyr)
fromJSON("./stats.json") -> x 
y <- ldply(x,function(x)data.frame(x))
for(i in 2:ncol(y)){
  scale(y[i]) -> s
  t <- s / max(abs(s)) #这里可能有点不科学，这么处理的话是取不到接近0的点的
  y[i] <- (t + 1) / 2 #不过相对大小是没有问题的，而且不接近0的话也好画图一些
}
x <- toJSON(dlply(y,.(.id),function(x)c(x)[-c(1)]),pretty=T,auto_unbox=T)
write(x,"normalizeddata.json")