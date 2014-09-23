#!/usr/bin/env Rscript
if(!file.exists("altcoins")){
  q("no",0)
}
if(file.exists("result")){
  file.remove("result")
}
dir.create("result")
for(i in dir("altcoins")){
  for(j in dir(file.path("altcoins",i))){
    system(paste("./git-stats-json",file.path("altcoins",i,j),file.path("result",i)))
    file.remove(file.path("result",i,"gitstats.cache"))
    file.rename(file.path("result",i,"stats.json"),file.path("result",i,paste0(j,".json")))
  }
}
