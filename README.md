AltcoinAnalyze
==============

Judge altcoin's value by
- analyze its development activity frequency
- how its source codes are similar to others

### How we design
1. Download all to be analyzed altcoins' repos and use gitstats to get those info
2. Analyze ...
3. Visualize ...

### How to use
`python main.py`

### Lib Required
pip: 
`apt-get install python-pip python-dev build-essential`
`pip install --upgrade pip`

scrapy: 
`pip install Scrapy`

pandas, numpy, pylab, matplotlib: 
`apt-get install python-numpy python-scipy python-matplotlib python-pandas`
