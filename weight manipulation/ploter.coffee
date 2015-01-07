fs = require 'fs'
fs.readFile 'normalizeddata.json',encoding: 'utf8',(err,data) ->
    data = JSON.parse data
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
    obj = "makeChart = function(weights){\n  multiplyweight=#{multiplyweight.toString()}\n  var fuck = #{makeChart.toString()};\n  fuck(#{JSON.stringify dataProvider,null,'  '},#{JSON.stringify graphs,null,'  '},weights)\n}"
    fs.writeFileSync 'ploter.js',obj
makeChart = (dataProvider,graphs,weights) ->
    multiplyweight dataProvider,weights
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
multiplyweight = (dataProvider,weights) ->
    for coinname, coininfo of dataProvider
        coininfo[i] = Math.floor(coininfo[i] * weights[i] * 10000) / 10000 for i of coininfo when weights[i]?

    