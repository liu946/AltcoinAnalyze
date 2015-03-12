meaningitem=['ActiveDays','TotalAuthors','TotalCommits','OpenIssuesCount','ActiveDays%','SubscribersCount','StargazersCount','Forks' ]
r=[[1,0.9387,0.9161,0.3366,0.4101,0.8672,0.4849,0.4552],
[0.9387,1,0.7546,0.3063,0.4903,0.6967,0.5661,0.5547],
[0.9161,0.7546,1,0.3572,0.3970,0.9219,0.4546,0.4155],
[0.3366,0.3063,0.3572,1,0.5885,0.4727,0.7513,0.6891],
[0.4101,0.4903,0.3970,0.5885,1,0.4322,0.9370,0.9366],
[0.8672,0.6967,0.9219,0.4727,0.4322,1,0.4396,0.3793],
[0.4849,0.5661,0.4546,0.7513,0.9370,0.4396,1,0.9928],
[0.4552,0.5547,0.4155,0.6891,0.9366,0.3793,0.9928,1]]

filehandle=open("./html/table/relation_data.html","w")
filehandle.write(open("./html/tpl/header.html").read())
filehandle.write('''
	<style type=\"text/css\">th{width:%s%%;}</style>
	<table><tbody><tr><th>Items</th>'''% int(100/(1+meaningitem.__len__())))
for i in meaningitem:
	filehandle.write("<th>%s</th>"%i)

filehandle.write("</tr>")
for i in range(len(r)):
	filehandle.write("<tr><th>%s</th>"%meaningitem[i])
	for j in range(len(r[i])):
		
			
		filehandle.write("<td style=\"background-color: rgba(255,125,0,%2f);\">%1f</td>"% ((r[i][j])**2 if i!=j else 0,r[i][j]))
		
	filehandle.write("</tr>")

filehandle.write("</tbody></table>")
filehandle.write(open("./html/tpl/footer.html").read())
filehandle.close()