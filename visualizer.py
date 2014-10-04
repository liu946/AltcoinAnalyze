# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

# plot one activity
def plot(altcoins, activity, marketcap):
	wid = 10
	sum = len(altcoins)
	fig = plt.figure()

	# Activity
	ax1 = fig.add_subplot(111)
	ax1.set_ylabel('Activity')
	ax1_left = [i * wid * 2 for i in range(sum)]
	activity_bar = ax1.bar(left = ax1_left, height = activity, width = wid - 1, color = 'skyblue')

	# Market Cap
	ax2 = ax1.twinx()
	ax2.set_ylabel('Market Cap')
	ax2_left = [i + wid - 1 for i in ax1_left]
	marketcap_bar = ax2.bar(left = ax2_left, height = marketcap, width = wid - 1, color = 'green')
	
	plt.legend((activity_bar, marketcap_bar), ('Activity', 'Market Cap'))
	plt.xticks(ax2_left, altcoins)
	plt.show()

# plot all activities
def plots(altcoins, activities_name, activities, marketcap):
	wid = 10
	sum = len(altcoins)
	colors = ['red', 'orange', 'yellow', 'skyblue', 'blue', 'purple']
	fig = plt.figure()

	# Activity
	ax1 = fig.add_subplot(111)
	ax1.set_ylabel('Activity')
	
	ax1_left = [i * wid * 2 for i in range(sum)]
	btm = [0] * sum
	c = 0
	activity_bar = []
	for act in activities:
		# Plot each activity in one bar
		activity_bar.append(ax1.bar(left = ax1_left, height = act, width = wid - 1, bottom = btm, color = colors[c]))
		btm = [(x + y) for x, y in zip(act, btm)]
		if colors[c] == colors[-1]:
			c = 0
		else:
			c += 1

	# Market Cap
	ax2 = ax1.twinx()
	ax2.set_ylabel('Market Cap')
	ax2_left = [i + wid - 1 for i in ax1_left]
	marketcap_bar = ax2.bar(left = ax2_left, height = marketcap, width = wid - 1, color = 'green')
	
	plt.legend(tuple(activity_bar[::-1]) + (marketcap_bar, ), tuple(activities_name) + ('Market Cap', ))
	plt.xticks(ax2_left, altcoins)
	plt.show()

# Test Data
altcoins = ['Bitcoin', 'Litecoin', 'Dogecoin', 'Nxt']
activity = [100, 10, 5, 1]
activities_name = ['Commits', 'Star', 'Fork', 'Watch']
activities = [[20, 5, 2, 1], [30, 3, 1, 1], [10, 2, 1, 1], [40, 1, 1, 1]]
marketcap = [200, 5, 1, 1]

# Test
#plot(altcoins, activity, marketcap)
plots(altcoins, activities_name, activities, marketcap)
