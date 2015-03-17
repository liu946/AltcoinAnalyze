	function drawRadarxyLable (canvas,size,array,wei) {
		var c=document.getElementById(canvas);
		var cxt=c.getContext("2d");
		cxt.translate(size/2,size/2);
		cxt.strokeStyle = "rgba(0,0,0,1)"
		cxt.lineWidth="2";
		cxt.fillStyle="#000";

		angletotle=0;
		for (var i = 0 ; i < array.length; i++) {
			{//写坐标轴lable，移动过去把角度转回来，再写，再恢复
				cxt.translate(0,size*0.45);
				cxt.rotate(-angletotle);
				
				cxt.fillText(array[i],0,0);
				cxt.rotate(angletotle);
				cxt.translate(0,-size*0.45);
			}
			
			cxt.rotate(6.2831853*wei[i]);
			angletotle+=6.2831853*wei[i];
		};
		cxt.translate(-size/2,-size/2);
	}
	function drawRadarData (canvas,size,array,wei) {
		var c=document.getElementById(canvas);
		var cxt=c.getContext("2d");
		cxt.fillStyle="#FF8800";
		cxt.strokeStyle = "rgba(255,100,0,0.5)"
		cxt.translate(size/2,size/2);
		cxt.lineWidth="5";
		cxt.lineCap="round";
		cxt.beginPath();
		for (var i = 0 ; i < array.length; i++) {
			cxt.lineTo(0,size*0.5*array[i]);
			cxt.rotate(6.2831853*wei[i]);
		};
		cxt.lineTo(0,size*0.5*array[0]);
		cxt.stroke();
		cxt.strokeStyle = "rgba(255,100,0,0.8)"
		cxt.lineWidth="6";
		for (var i = 0 ; i < array.length; i++) {
			cxt.beginPath();
			cxt.lineTo(0,size*0.5*array[i%array.length]);
			cxt.lineTo(0,size*0.5*array[i%array.length]+1);
			cxt.stroke();
			cxt.rotate(6.2831853*wei[i%array.length]);
		};
		cxt.translate(-size/2,-size/2);
	}
	function drawRadarxy (canvas,size,arraylength,wei) {
		var c=document.getElementById(canvas);
		var cxt=c.getContext("2d");
		cxt.fillStyle="#000000";
		cxt.strokeStyle = "rgba(0,0,0,0.1)"
		cxt.translate(size/2,size/2);
		cxt.lineWidth="3";
		cxt.lineCap="round";
		for (var i = 0 ; i <= 5; i++) {
			cxt.beginPath();
			for (var j = 0 ; j < arraylength; j++) {
				cxt.lineTo(0,size*0.5*0.2*i);
				cxt.rotate(6.2831853*wei[j]);
			};
			cxt.lineTo(0,size*0.5*0.2*i);
			cxt.stroke();
		};
		for (var i = 0 ; i < arraylength; i++) {
			cxt.beginPath();
			cxt.lineTo(0,0);
			cxt.lineTo(0,size*0.5);
			cxt.stroke();
			cxt.rotate(6.2831853*wei[i%arraylength]);
		};
		cxt.translate(-size/2,-size/2);
	}
	function drawRadar (canvas,size,data,wei,arrlable) {

		var c=document.getElementById(canvas);
		if(c!=null){
			var cxt=c.getContext("2d");
			cxt.clearRect(0,0,size*2,size*2);
			drawRadarxyLable(canvas,size,arrlable,wei);

			cxt.translate(size*0.1,size*0.1);
			drawRadarxy(canvas,size*0.8,data.length,wei);
			drawRadarData(canvas,size*0.8,data,wei);
			cxt.translate(-size*0.1,-size*0.1);			
		}


	}
	function _calArea (data,weight) {
		var area=0;
		for (var i =0; i<weight.length ; i++) {
			//console.log(i+' '+weight[i]);
			area+=data[i] * data[(i+1)%weight.length] * Math.sin(6.2831853*weight[i]);
		};
		return area;
	}
	function showArea (coinname,data,weight) {
		var p = document.getElementById(coinname+'area');
		if (p!=null) {
			p.innerHTML=coinname + ' has area ' + Math.floor(_calArea(data,weight)*100000)/100000;
		
		};
	}
	function loadpage(weight) {
		// data=new Array(0.7,0.5,0.2,0.7,0.6,1);
		// arrlable=new Array("star","fork","3..","4..","5..","6..");
		// wei=new Array(0.1,0.1,0.1,0.3,0.2,0.2);
		// drawRadar ("myCanvas",300,data,wei,arrlable) ;
		for(var coin in datalist){
			//console.log(datalist[coin]);
			//clearcanvas(datalist[coin],500);
			drawRadar(datalist[coin],400,divmax[datalist[coin]],weight,meandatacol);
			showArea(datalist[coin],divmax[datalist[coin]],weight);
		}
	}
	function weightSetForm () {
		var table = document.getElementById('weightset');
		var str='<tr>';
		for (var i=0;i<meandatacolweight.length;i++) {
			str+='<td>'+meandatacol[i]+'</td>'+
			'<td><input id= "weight'+i+'" for="'+meandatacol[i]+'" type="range" /></td>'+
			'<td id="weightnum'+i+'">'+meandatacolweight[i]+'<td>';
			if((i%2))str+='</tr><tr>'
		};
		str+='</tr>';
		table.innerHTML=str;
		for (var i=0;i<meandatacolweight.length;i++) {
			var range = document.getElementById('weight'+i);
			range.value=meandatacolweight[i]*100;
			//绑定函数
			range.onchange=resetweight;
		};
	}
	function resetweight () {
		var sum=0.0;
		for (var i=0;i<meandatacolweight.length;i++) {
			var range = document.getElementById('weight'+i);
			sum+=eval(range.value);
		}
		for (var i=0;i<meandatacolweight.length;i++) {
			var td = document.getElementById('weightnum'+i);
			var range = document.getElementById('weight'+i);
			td.innerHTML=Math.floor(range.value/sum*1000)/1000;
			meandatacolweight[i]=range.value/sum;
			
		}

	}

	window.onload=function (argument) {
		//加载权重填充
		weightSetForm()
		//初始化数据
		loadpage(meandatacolweight);


	}




