library(jsonlite)
library(plyr)
fromJSON("./stats.json") -> x
y <- ldply(x,function(x)data.frame(x))
for(i in 2:ncol(y)){
  scale(y[i]) -> s
  t <- s / max(abs(s))
  y[i] <- (t + 1) / 2
}
colnames(y)[1] <- "coinname"
x <- toJSON(dlply(y,.(coinname),function(x)c(x)[-c(1)]),pretty=T,auto_unbox=T)
write(x,"normalizeddata.json")