% commit star issue
data=[3862, 3, 0, 653326; 6827, 6604, 455, 3945470610; 3762, 68, 7, 1209081; 327, 55, 46, 4124223; 2, 0, 0, 764890; 2441, 151, 36, 3572028; 58, 47, 5, 1929932; 1014, 77, 6, 5366220; 66, 60, 4, 435855; 8459, 276, 68, 11058373; 105, 3, 0, 468218; 44, 0, 1, 269421; 5959, 988, 12, 74412188; 94, 41, 0, 2215849; 1771, 502, 13, 12216155; 126, 3, 0, 1253774; 4895, 130, 34, 553469; 3039, 223, 53, 8818467; 6107, 1061, 97, 13909520; 113, 2, 0, 646270; 4, 6, 2, 1221558; 4165, 80, 0, 302499; 4502, 12, 18, 988422; 4341, 19, 0, 127314; 2, 0, 0, 1468234; 3358, 0, 0, 848121; 289, 115, 116, 1420147; 456, 12, 1, 725682; 3272, 1278, 24, 349752825; 4631, 152, 20, 15530571];
% value=rand(1,19);
% cor=corrcoef(data(:,1),value);
% cor(1,2)
rmax=0;
r=zeros(101,101);
for i=1:101
    for j=1:102-i
            k=103-i-j;
            area = (data(:,1)*(i-1)+data(:,2)*(j-1)+data(:,3)*(k-1))*0.01;
            cor=corrcoef(area,data(:,4));
            r(i,j)=cor(1,2);
            if cor(1,2)>rmax
                rmax=cor(1,2);
                weight=[i,j,k];
            end
    end
end

[x,y]=meshgrid(1:101);
figure;
hold on;
meshc(x,y,r);
