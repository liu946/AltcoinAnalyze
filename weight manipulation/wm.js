var weight = {
	ActiveDays: 1,
	TotalAuthors: 1,
	TotalCommits: 1,
	open_issues_count: 1,
	ActiveDaysPercentage: 1,
	watchers_count: 1,
	stargazers_count: 1,
	forks: 1
};
window.onload = function(){
	var foo = function(i){
		var tip = document.getElementById(i+'Tip');
		tip.textContent = weight[i] = Math.floor(Math.pow(this.value / 50,4)*10000)/10000;
		makeChart(weight);
	};
	for(var i in weight){
		// 由于i在循环中发生了改变，所以必须先toString再new出function，把现在的i的值变成新的function的字面量，而不能通过闭包来引用i。这个问题在ES6以后可以通过let关键字得到更好的解决
		document.getElementById(i).onchange = new Function("("+foo.toString()+").call(this,'"+i+"')");
	}
};

