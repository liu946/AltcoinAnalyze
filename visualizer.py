# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

def plot(altcoins, activity, marketcap):
	sum = len(altcoins)
	wid = 10
	fig = plt.figure()

	# Activity
	ax1 = fig.add_subplot(111)
	ax1.legend(loc = 1)
	ax1.set_ylabel('Activity')
	ax1.bar(left = [i * wid * 2 for i in range(sum)], height = activity, width = wid - 1, color = 'skyblue')


	# Market Cap
	ax2 = ax1.twinx()
	ax2.bar(left = [i * wid * 2 + wid - 1 for i in range(sum)], height = marketcap, width = wid - 1, color = 'green')
	ax2.legend(loc = 2)
	ax2.set_ylabel('Market Cap')
	plt.xticks([i * wid * 2 + wid - 1 for i in range(sum)], altcoins)
	plt.show()


altcoins = ['bitcoin', 'litecoin', 'dogecoin', 'nxt']
activity = [100, 10, 5, 1]
marketcap = [200, 5, 1, 1]

plot(altcoins, activity, marketcap)
