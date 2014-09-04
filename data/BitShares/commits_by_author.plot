set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Daniel Larimer" w lines, 'commits_by_author.dat' using 1:3 title "dnotestein" w lines, 'commits_by_author.dat' using 1:4 title "vogel76" w lines, 'commits_by_author.dat' using 1:5 title "grzegorzs" w lines, 'commits_by_author.dat' using 1:6 title "Jeffrey Lee" w lines, 'commits_by_author.dat' using 1:7 title "Eric Frias" w lines, 'commits_by_author.dat' using 1:8 title "clar" w lines, 'commits_by_author.dat' using 1:9 title "batmaninpink" w lines, 'commits_by_author.dat' using 1:10 title "HackFisher" w lines, 'commits_by_author.dat' using 1:11 title "David Andersen" w lines, 'commits_by_author.dat' using 1:12 title "Yuvaraj Gogoi" w lines, 'commits_by_author.dat' using 1:13 title "Yuvaraj" w lines, 'commits_by_author.dat' using 1:14 title "Tzadik Vanderhoof" w lines, 'commits_by_author.dat' using 1:15 title "BrownBear2" w lines, 'commits_by_author.dat' using 1:16 title "skchaudhari" w lines, 'commits_by_author.dat' using 1:17 title "alt" w lines, 'commits_by_author.dat' using 1:18 title "Gandalf-the-Grey" w lines, 'commits_by_author.dat' using 1:19 title "yuvarajgogoi" w lines, 'commits_by_author.dat' using 1:20 title "synapticad developer" w lines, 'commits_by_author.dat' using 1:21 title "root" w lines
