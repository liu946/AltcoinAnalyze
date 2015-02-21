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
		drawRadarxyLable(canvas,size,arrlable,wei);
		var c=document.getElementById(canvas);
		var cxt=c.getContext("2d");
		cxt.translate(size*0.1,size*0.1);
		drawRadarxy(canvas,size*0.8,data.length,wei);
		drawRadarData(canvas,size*0.8,data,wei);
		cxt.translate(-size*0.1,-size*0.1);

	}
	window.onload=function (argument) {
		// data=new Array(0.7,0.5,0.2,0.7,0.6,1);
		// arrlable=new Array("star","fork","3..","4..","5..","6..");
		// wei=new Array(0.1,0.1,0.1,0.3,0.2,0.2);
		// drawRadar ("myCanvas",300,data,wei,arrlable) ;
		for(var coin in datalist){
			console.log(datalist[coin]);
			drawRadar(datalist[coin],400,divmax[datalist[coin]],meandatacolweight,meandatacol);
		}
	}
