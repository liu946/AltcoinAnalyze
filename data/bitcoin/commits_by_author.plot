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
plot 'commits_by_author.dat' using 1:2 title "Wladimir J. van der Laan" w lines, 'commits_by_author.dat' using 1:3 title "Gavin Andresen" w lines, 'commits_by_author.dat' using 1:4 title "Pieter Wuille" w lines, 'commits_by_author.dat' using 1:5 title "Philip Kaufmann" w lines, 'commits_by_author.dat' using 1:6 title "Jeff Garzik" w lines, 'commits_by_author.dat' using 1:7 title "s_nakamoto" w lines, 'commits_by_author.dat' using 1:8 title "Matt Corallo" w lines, 'commits_by_author.dat' using 1:9 title "Gregory Maxwell" w lines, 'commits_by_author.dat' using 1:10 title "Luke Dashjr" w lines, 'commits_by_author.dat' using 1:11 title "Cory Fields" w lines, 'commits_by_author.dat' using 1:12 title "Cozz Lovan" w lines, 'commits_by_author.dat' using 1:13 title "Peter Todd" w lines, 'commits_by_author.dat' using 1:14 title "Giel van Schijndel" w lines, 'commits_by_author.dat' using 1:15 title "jtimon" w lines, 'commits_by_author.dat' using 1:16 title "Nils Schneider" w lines, 'commits_by_author.dat' using 1:17 title "Eric Lombrozo" w lines, 'commits_by_author.dat' using 1:18 title "sirius-m" w lines, 'commits_by_author.dat' using 1:19 title "Satoshi Nakamoto" w lines, 'commits_by_author.dat' using 1:20 title "Michael Ford" w lines, 'commits_by_author.dat' using 1:21 title "Jonas Schnelli" w lines
