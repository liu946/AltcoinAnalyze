for dir in $(ls  Altcoin/) 
do
	gitstats/gitstats Altcoin/$dir data/$dir
done
