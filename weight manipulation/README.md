###使用

```
$cp ../stats.json ./stats.json
$rscript normalization.R
$coffee ploter.coffee
$firefox wm.html
```
###修改

* 增删竞争币：不需要修改代码，重复一遍获取ploter.js的流程即可
* 增删字段：修改wm.js和wm.html两个文件中对应的部分
* 修改权值计算方法：修改ploter.coffee最后的那两个小函数