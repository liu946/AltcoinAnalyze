set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'lines_of_code_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Lines"
set xtics rotate
set bmargin 6
plot 'lines_of_code_by_author.dat' using 1:2 title "Daniel Larimer" w lines, 'lines_of_code_by_author.dat' using 1:3 title "dnotestein" w lines, 'lines_of_code_by_author.dat' using 1:4 title "vogel76" w lines, 'lines_of_code_by_author.dat' using 1:5 title "grzegorzs" w lines, 'lines_of_code_by_author.dat' using 1:6 title "Jeffrey Lee" w lines, 'lines_of_code_by_author.dat' using 1:7 title "Eric Frias" w lines, 'lines_of_code_by_author.dat' using 1:8 title "clar" w lines, 'lines_of_code_by_author.dat' using 1:9 title "batmaninpink" w lines, 'lines_of_code_by_author.dat' using 1:10 title "HackFisher" w lines, 'lines_of_code_by_author.dat' using 1:11 title "David Andersen" w lines, 'lines_of_code_by_author.dat' using 1:12 title "Yuvaraj Gogoi" w lines, 'lines_of_code_by_author.dat' using 1:13 title "Yuvaraj" w lines, 'lines_of_code_by_author.dat' using 1:14 title "Tzadik Vanderhoof" w lines, 'lines_of_code_by_author.dat' using 1:15 title "BrownBear2" w lines, 'lines_of_code_by_author.dat' using 1:16 title "skchaudhari" w lines, 'lines_of_code_by_author.dat' using 1:17 title "alt" w lines, 'lines_of_code_by_author.dat' using 1:18 title "Gandalf-the-Grey" w lines, 'lines_of_code_by_author.dat' using 1:19 title "yuvarajgogoi" w lines, 'lines_of_code_by_author.dat' using 1:20 title "synapticad developer" w lines, 'lines_of_code_by_author.dat' using 1:21 title "root" w lines
