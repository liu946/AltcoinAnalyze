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
plot 'lines_of_code_by_author.dat' using 1:2 title "Wladimir J. van der Laan" w lines, 'lines_of_code_by_author.dat' using 1:3 title "Gavin Andresen" w lines, 'lines_of_code_by_author.dat' using 1:4 title "Pieter Wuille" w lines, 'lines_of_code_by_author.dat' using 1:5 title "Philip Kaufmann" w lines, 'lines_of_code_by_author.dat' using 1:6 title "Jeff Garzik" w lines, 'lines_of_code_by_author.dat' using 1:7 title "s_nakamoto" w lines, 'lines_of_code_by_author.dat' using 1:8 title "Matt Corallo" w lines, 'lines_of_code_by_author.dat' using 1:9 title "Gregory Maxwell" w lines, 'lines_of_code_by_author.dat' using 1:10 title "Luke Dashjr" w lines, 'lines_of_code_by_author.dat' using 1:11 title "Cory Fields" w lines, 'lines_of_code_by_author.dat' using 1:12 title "Cozz Lovan" w lines, 'lines_of_code_by_author.dat' using 1:13 title "Peter Todd" w lines, 'lines_of_code_by_author.dat' using 1:14 title "Giel van Schijndel" w lines, 'lines_of_code_by_author.dat' using 1:15 title "jtimon" w lines, 'lines_of_code_by_author.dat' using 1:16 title "Nils Schneider" w lines, 'lines_of_code_by_author.dat' using 1:17 title "Eric Lombrozo" w lines, 'lines_of_code_by_author.dat' using 1:18 title "sirius-m" w lines, 'lines_of_code_by_author.dat' using 1:19 title "Satoshi Nakamoto" w lines, 'lines_of_code_by_author.dat' using 1:20 title "Michael Ford" w lines, 'lines_of_code_by_author.dat' using 1:21 title "Jonas Schnelli" w lines
