% 2015-03-17
data=[777, 137, 139, 3862, 6, 0, 40.51094890510949, 3, 636894;1476, 348, 4650, 8050, 864, 456, 72.85291214215202, 6631, 4050836583;1014, 169, 139, 4054, 48, 9, 50.44776119402985, 67, 1221121;143, 34, 69, 653, 31, 47, 29.72972972972973, 55, 5373782;1, 1, 0, 2, 2, 0, 100.0, 0, 632500;367, 27, 97, 2441, 43, 37, 87.79904306220095, 151, 3558347;31, 10, 220, 58, 36, 5, 10.163934426229508, 48, 2072036;372, 82, 121, 1014, 15, 6, 24.0, 77, 5352221;43, 8, 54, 79, 37, 4, 7.426597582037997, 60, 473796;916, 63, 48, 8594, 67, 68, 74.0501212611156, 277, 11176149;54, 12, 3, 105, 4, 1, 13.5678391959799, 3, 289939;11, 1, 1, 44, 1, 1, 4.365079365079365, 0, 253141;997, 199, 4650, 5967, 241, 12, 50.815494393476044, 989, 75980593;24, 6, 18, 95, 20, 0, 5.454545454545454, 41, 2536130;555, 42, 93, 1773, 134, 12, 52.90753098188751, 504, 11432877;41, 10, 220, 126, 5, 0, 9.647058823529411, 3, 1342748;1069, 207, 4650, 4895, 134, 34, 53.2901296111665, 129, 555155;670, 129, 4650, 3039, 63, 55, 39.044289044289044, 223, 8833212;1287, 293, 484, 6290, 157, 81, 65.42958820538891, 1062, 14432720;27, 12, 8, 113, 3, 0, 5.31496062992126, 2, 646509;3, 1, 5, 4, 2, 2, 5.0, 6, 1316757;895, 173, 4650, 4165, 56, 0, 49.284140969163, 80, 238162;1050, 178, 139, 4502, 10, 18, 51.95447798119743, 12, 959431;2, 1, 0, 2, 2, 0, 20.0, 0, 1545999;853, 158, 0, 3358, 1, 0, 46.13304488912926, 0, 586458;147, 19, 45, 334, 48, 116, 31.34328358208955, 115, 1196574;63, 10, 18, 456, 13, 1, 16.8, 12, 711827;672, 64, 472, 4949, 994, 23, 66.27218934911242, 1278, 348246741;1299, 281, 4650, 7033, 68, 16, 64.6268656716418, 154, 17055748];
coinname={'Novacoin'; 'Bitcoin'; 'BlackCoin'; 'Monero'; 'FuelCoin'; 'Counterparty'; 'Bytecoin'; 'Namecoin'; 'Quark'; 'Stellar'; 'Mintcoin'; 'XCurrency'; 'Litecoin'; 'MonaCoin'; 'MaidSafeCoin'; 'DarkNote'; 'ReddCoin'; 'Peercoin'; 'Dogecoin'; 'Unobtanium'; 'BitcoinDark'; 'BitShares-PTS'; 'Clams'; 'DNotes'; 'Ethercoin'; 'Mastercoin'; 'DigiByte'; 'Ripple'; 'Darkcoin'};
items={'ActiveDays', 'TotalAuthors', 'network_count', 'TotalCommits', 'subscribers_count', 'open_issues_count', 'ActiveDaysPercentage', 'stargazers_count'};
[trash,index]=sort(-data(:,9));
[cn,trash]=size(data(:,1:8));
[trash,in]=size(items);
nin=zeros(cn,1);
for i=1:cn
nin(index(i),1)=i;
end
index=nin;
index=[38, 1, 26, 13, 39, 15, 21, 14, 47, 9, 64, 74, 3, 18, 8, 24, 44, 11, 6, 37, 25, 76, 31, 22, 40, 27, 35, 2, 5];
pred=[];
cor=zeros(in,in);
weight=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3];
% for i=1:in
%     for j=1:in
%         c=corrcoef(data(:,i),data(:,j));
%         cor(i,j)=c(1,2);
%     end
% end
maxcor=0;
mincor=0;
step=0.02;
for actday=0:step:0.04

for sub=0:step:1-actday
for issue=0:step:1-actday-sub
actdayper=1-actday-sub-issue;
%pred=[];
sum=data(:,1).*actday+data(:,5).*sub+data(:,6).*issue+data(:,7).*actdayper;
%                  for i=1:cn
%                      for j=i+1:cn
%                           pred=[pred;index(i)-index(j),data(1).*actday+data(3).*network+data(5).*sub+data(6).*issue+data(7).*actdayper];
%                      end
%                  end
cor=corrcoef(index,sum);
if cor(1,2)>maxcor
maxcor=cor(1,2);
maxw=[actday,sub,issue,actdayper];
end
if cor(1,2)<mincor
mincor=cor(1,2);
minw=[actday,sub,issue,actdayper];
end
end

end
end
% answer 2%actday  0%fork  14%sub 12%issue 72%actdayper;===-0.4806
