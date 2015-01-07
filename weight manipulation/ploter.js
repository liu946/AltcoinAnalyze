makeChart = function(weights){
  multiplyweight=function (dataProvider, weights) {
    var coininfo, coinname, i, _results;
    _results = [];
    for (coinname in dataProvider) {
      coininfo = dataProvider[coinname];
      _results.push((function() {
        var _results1;
        _results1 = [];
        for (i in coininfo) {
          if (weights[i] != null) {
            _results1.push(coininfo[i] = Math.floor(coininfo[i] * weights[i] * 10000) / 10000);
          }
        }
        return _results1;
      })());
    }
    return _results;
  }
  var fuck = function (dataProvider, graphs, weights) {
    multiplyweight(dataProvider, weights);
    return AmCharts.makeChart("chartdiv", {
      type: 'serial',
      theme: 'none',
      legend: {
        horizontalGap: 8,
        maxColumns: 1,
        position: 'right',
        useGraphSettings: true,
        markerSize: 10
      },
      dataProvider: dataProvider,
      valueAxes: [
        {
          stackType: 'regular',
          axisAlpha: 0.3,
          gridAlpha: 0
        }
      ],
      graphs: graphs,
      categoryField: 'coinname',
      categoryAxis: {
        gridPosition: 'start',
        axisAlpha: 0,
        gridAlpha: 0,
        position: 'left'
      },
      exportConfig: {
        menuTop: '20px',
        menuRight: '20px',
        menuItems: [
          {
            format: 'png'
          }
        ]
      }
    });
  };
  fuck([
  {
    "ActiveDays": 1,
    "TotalAuthors": 1,
    "TotalCommits": 0.7038,
    "open_issues_count": 1,
    "ActiveDaysPercentage": 0.7544,
    "watchers_count": 1,
    "stargazers_count": 1,
    "forks": 1,
    "coinname": "Bitcoin"
  },
  {
    "ActiveDays": 0.1516,
    "TotalAuthors": 0.2546,
    "TotalCommits": 0.297,
    "open_issues_count": 0.446,
    "ActiveDaysPercentage": 0.169,
    "watchers_count": 0.4503,
    "stargazers_count": 0.4503,
    "forks": 0.4568,
    "coinname": "BitcoinDark"
  },
  {
    "ActiveDays": 0.7302,
    "TotalAuthors": 0.6749,
    "TotalCommits": 0.5451,
    "open_issues_count": 0.4445,
    "ActiveDaysPercentage": 0.5626,
    "watchers_count": 0.4576,
    "stargazers_count": 0.4576,
    "forks": 0.4607,
    "coinname": "BitShares-PTS"
  },
  {
    "ActiveDays": 0.2768,
    "TotalAuthors": 0.3303,
    "TotalCommits": 1,
    "open_issues_count": 0.4431,
    "ActiveDaysPercentage": 1,
    "watchers_count": 0.4528,
    "stargazers_count": 0.4528,
    "forks": 0.4585,
    "coinname": "BitSharesX"
  },
  {
    "ActiveDays": 0.738,
    "TotalAuthors": 0.6529,
    "TotalCommits": 0.5403,
    "open_issues_count": 0.4489,
    "ActiveDaysPercentage": 0.5603,
    "watchers_count": 0.4553,
    "stargazers_count": 0.4553,
    "forks": 0.4639,
    "coinname": "BlackCoin"
  },
  {
    "ActiveDays": 0.1698,
    "TotalAuthors": 0.2766,
    "TotalCommits": 0.3002,
    "open_issues_count": 0.4489,
    "ActiveDaysPercentage": 0.2149,
    "watchers_count": 0.454,
    "stargazers_count": 0.454,
    "forks": 0.4725,
    "coinname": "Bytecoin"
  },
  {
    "ActiveDays": 0.1549,
    "TotalAuthors": 0.257,
    "TotalCommits": 0.2974,
    "open_issues_count": 0.4445,
    "ActiveDaysPercentage": 0.1612,
    "watchers_count": 0.4553,
    "stargazers_count": 0.4553,
    "forks": 0.4572,
    "coinname": "Counterparty"
  },
  {
    "ActiveDays": 0.834,
    "TotalAuthors": 0.7483,
    "TotalCommits": 0.5893,
    "open_issues_count": 0.4577,
    "ActiveDaysPercentage": 0.6314,
    "watchers_count": 0.4579,
    "stargazers_count": 0.4579,
    "forks": 0.462,
    "coinname": "Darkcoin"
  },
  {
    "ActiveDays": 0.9527,
    "TotalAuthors": 0.9438,
    "TotalCommits": 0.6609,
    "open_issues_count": 0.5046,
    "ActiveDaysPercentage": 0.7288,
    "watchers_count": 0.5438,
    "stargazers_count": 0.5438,
    "forks": 0.5145,
    "coinname": "Dogecoin"
  },
  {
    "ActiveDays": 0.7944,
    "TotalAuthors": 0.7385,
    "TotalCommits": 0.652,
    "open_issues_count": 0.4621,
    "ActiveDaysPercentage": 0.6037,
    "watchers_count": 0.5387,
    "stargazers_count": 0.5387,
    "forks": 0.5463,
    "coinname": "Litecoin"
  },
  {
    "ActiveDays": 0.234,
    "TotalAuthors": 0.2986,
    "TotalCommits": 0.314,
    "open_issues_count": 0.5955,
    "ActiveDaysPercentage": 0.4891,
    "watchers_count": 0.4595,
    "stargazers_count": 0.4595,
    "forks": 0.4619,
    "coinname": "Mastercoin"
  },
  {
    "ActiveDays": 0.1996,
    "TotalAuthors": 0.3157,
    "TotalCommits": 0.3163,
    "open_issues_count": 0.4944,
    "ActiveDaysPercentage": 0.3489,
    "watchers_count": 0.454,
    "stargazers_count": 0.454,
    "forks": 0.4637,
    "coinname": "Monero"
  },
  {
    "ActiveDays": 0.391,
    "TotalAuthors": 0.4525,
    "TotalCommits": 0.3572,
    "open_issues_count": 0.4519,
    "ActiveDaysPercentage": 0.3379,
    "watchers_count": 0.4572,
    "stargazers_count": 0.4572,
    "forks": 0.4577,
    "coinname": "Namecoin"
  },
  {
    "ActiveDays": 0.5842,
    "TotalAuthors": 0.5674,
    "TotalCommits": 0.478,
    "open_issues_count": 0.5032,
    "ActiveDaysPercentage": 0.4716,
    "watchers_count": 0.4698,
    "stargazers_count": 0.4698,
    "forks": 0.4723,
    "coinname": "Peercoin"
  },
  {
    "ActiveDays": 0.1737,
    "TotalAuthors": 0.2717,
    "TotalCommits": 0.3007,
    "open_issues_count": 0.4489,
    "ActiveDaysPercentage": 0.2044,
    "watchers_count": 0.4552,
    "stargazers_count": 0.4552,
    "forks": 0.463,
    "coinname": "Quark"
  },
  {
    "ActiveDays": 0.4844,
    "TotalAuthors": 0.367,
    "TotalCommits": 0.4918,
    "open_issues_count": 0.4826,
    "ActiveDaysPercentage": 0.6712,
    "watchers_count": 0.5661,
    "stargazers_count": 0.5661,
    "forks": 0.5127,
    "coinname": "Ripple"
  },
  {
    "ActiveDays": 0.7159,
    "TotalAuthors": 0.3963,
    "TotalCommits": 0.8011,
    "open_issues_count": 0.5354,
    "ActiveDaysPercentage": 0.8491,
    "watchers_count": 0.471,
    "stargazers_count": 0.471,
    "forks": 0.4614,
    "coinname": "Stellar"
  },
  {
    "ActiveDays": 0.1568,
    "TotalAuthors": 0.2546,
    "TotalCommits": 0.2994,
    "open_issues_count": 0.4445,
    "ActiveDaysPercentage": 0.1633,
    "watchers_count": 0.4499,
    "stargazers_count": 0.4499,
    "forks": 0.4564,
    "coinname": "XCurrency"
  },
  {
    "ActiveDays": 0.7581,
    "TotalAuthors": 0.6994,
    "TotalCommits": 0.5555,
    "open_issues_count": 0.4431,
    "ActiveDaysPercentage": 0.5782,
    "watchers_count": 0.4515,
    "stargazers_count": 0.4515,
    "forks": 0.4585,
    "coinname": "Zetacoin"
  }
],[
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "ActiveDays",
    "type": "column",
    "color": "#000000",
    "valueField": "ActiveDays"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "TotalAuthors",
    "type": "column",
    "color": "#000000",
    "valueField": "TotalAuthors"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "TotalCommits",
    "type": "column",
    "color": "#000000",
    "valueField": "TotalCommits"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "open_issues_count",
    "type": "column",
    "color": "#000000",
    "valueField": "open_issues_count"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "ActiveDaysPercentage",
    "type": "column",
    "color": "#000000",
    "valueField": "ActiveDaysPercentage"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "watchers_count",
    "type": "column",
    "color": "#000000",
    "valueField": "watchers_count"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "stargazers_count",
    "type": "column",
    "color": "#000000",
    "valueField": "stargazers_count"
  },
  {
    "balloonText": "<b>[[title]]</b><br><span style='font-size:14px'>[[category]]: <b>[[value]]</b></span>",
    "fillAlphas": 0.8,
    "labelText": "[[value]]",
    "lineAlpha": 0.3,
    "title": "forks",
    "type": "column",
    "color": "#000000",
    "valueField": "forks"
  }
],weights)
}