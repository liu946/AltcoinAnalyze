fs = require 'fs'
fs.readFile 'normalizeddata.json',encoding: 'utf8',(err,data) ->
    return console.log err if err?
    data = JSON.parse data
    #把名字提取出来作为一个字段，然后把所有币形成一个表。这是为了和amchart适应
    dataProvider = for coinname,coininfo of data
        temp = {}
        temp[k] = v for k,v of coininfo
        temp.coinname = coinname
        temp
    graphs = for x of dataProvider[0] when x isnt 'coinname'
        balloonText: "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>"
        fillAlphas: 0.8
        labelText: "[[value]]"
        lineAlpha: 0.3
        title: x
        type: "column"
        color: "#000000"
        valueField: x
    obj = """makeChart = function(weights){
                var multiplyweight = #{multiplyweight.toString()}
                var pipe = #{pipe.toString()}
                var fuck = #{makeChart.toString()};
                fuck(#{JSON.stringify dataProvider,null,'  '},
                #{JSON.stringify graphs,null,'  '},weights)
            }"""
    fs.writeFileSync 'ploter.js',obj
makeChart = (dataProvider,graphs,weights) ->
    multiplyweight dataProvider,weights
    dataProvider = pipe dataProvider
    AmCharts.makeChart "chartdiv",
        type: 'serial'
        theme: 'none'
        legend:
            horizontalGap: 8
            maxColumns: 1
            position: 'right'
            useGraphSettings: true
            markerSize: 10
        dataProvider: dataProvider
        valueAxes: [
            stackType: 'regular'
            axisAlpha: 0.3
            gridAlpha: 0
        ]
        graphs: graphs
        categoryField: 'coinname'
        categoryAxis: 
            gridPosition: 'start'
            axisAlpha: 0
            gridAlpha: 0
            position: 'left'
        exportConfig:
            menuTop: '20px'
            menuRight: '20px'
            menuItems: [
                format: 'png'
            ]
#要修改权值的计算方法只需要改这个小函数即可
multiplyweight = (dataProvider,weights) ->
    for coinname, coininfo of dataProvider
        coininfo[i] = Math.floor(coininfo[i] * weights[i] * 10000) / 10000 for i of coininfo when weights[i]?
pipe = (dataProvider) ->
    x = dataProvider.map (coininfo) ->
        s = for k,v of coininfo when k isnt 'coinname'
            v
        s = s.reduce (x,y) -> x+y
        key:s
        value:coininfo
    x.sort (x,y) -> y.key-x.key
    x.map (x) -> x.value