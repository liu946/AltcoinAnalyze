#人数，commit，star，fork

touch data.json
echo "{" >> data.json
a=`ls ./stats | wc -w`;
i=1;
for dir in `ls ./stats`
do
echo '"'${dir%/}'" : ' >> data.json
cat 'stats/'$dir"/"`ls stats/$dir`'/stats.json' >> data.json
if [[ "$a" -ne "$i" ]] 
then
echo ','>> data.json
fi
let i+=1
done
echo "}" >> data.json