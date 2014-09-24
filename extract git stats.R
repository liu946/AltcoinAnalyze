#!/usr/bin/env Rscript
library(jsonlite)
if(file.exists("config.json")){
  JSONconfig <- fromJSON("config.json")
}
if(!file.exists(JSONconfig$repo_dir)){
  q("no",0)
}
if(file.exists(JSONconfig$cache_dir)){
  file.remove(JSONconfig$cache_dir)
}
dir.create(JSONconfig$cache_dir)
for(i in dir(JSONconfig$repo_dir)){
  for(j in dir(file.path(JSONconfig$repo_dir,i))){
    system(paste("./git-stats-json",file.path(JSONconfig$repo_dir,i,j),file.path(JSONconfig$cache_dir,i)))
    file.remove(file.path(JSONconfig$cache_dir,i,"gitstats.cache"))
    file.rename(file.path(JSONconfig$cache_dir,i,"stats.json"),file.path(JSONconfig$cache_dir,i,paste0(j,".json")))
  }
}
