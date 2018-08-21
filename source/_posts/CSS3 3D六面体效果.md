---
title: CSS3 3D六面体效果
date: 2013-10-23 17:55:01
---
CSS 3D效果
===

by bibodeng 2013-10-23

## 碎碎念

无意之中看到[beiyuu](http://beiyuu.com/)写的CSS3动画详解，而我之前没有怎么系统学习过CSS3和HTML5，故而对其炫酷的效果非常动心，并且觉得这个技术在一些地方肯定非常棒。他的讲解例子很丰富，但是我还是花了一些功夫去理解。轻松获得的东西，也容易轻松失去，如果其中过程很难忘，那么的确可以学到一些东西。而这个折腾的过程，我也动手亲自实践了一下，一起来吧！

![成为最强的人](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/8d3daa4bfcfccc75819d06cf1f79bce42013102307565821497.png)

一直觉得很自卑，想要成为一个很强的人 : P

## CSS3 3D

如果突然给个例子你，很可能会消磨掉你的耐性，一切应当在愉悦的氛围下学习，但是也要留下深刻的印象，其基础是理解，这样很容易就知道如何写一个3D的东西了，将来也可以写更加复杂的效果（如果你数学好的话）。

### 3D坐标系

计算机技术源于数学，而3D坐标系，是3D空间的基础。2D空间中，容易理解，就是一个十字，横向为x轴，纵向为y轴。如下：

![二维坐标轴](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/282308e18cf25d10bf245c2d511a642d2013102308173126290.png)

三维的坐标轴稍有不同，举起你的右手，手心对着你的脸，大拇指头就是x, 中指是z， 而食指是y轴。如下图所示：

![三维坐标轴](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/6b2ef4260a2a5c0d2e4525830869303b2013102309193132740.png)

下面将会理解怎么布局3维的东西，这个图对于理解rotate（旋转）， transform（位移）都将有帮助。也可以看看这里的[分步过程](http://desandro.github.io/3dtransforms/examples/cube-01-steps.html),分为以下步骤：

1. 形成平面叠加
2. 平面旋转，上下左右，前后，但是还有一些重叠在一起
3. 对平面进行位移，形成3维视觉效果
4. 整体旋转3D物体

### 将元素转化为3D空间

假设我们正在做一个骰子一样的六面体，我们希望它的六个面能够像坐标中的那个立方体一样。首先写出如下的html代码，构建出基本元素。

	<div id="cube-con"> <!-- 主容器 -->
		<div id="cube">
			<figure class="front">1</figure>
			<figure class="back">2</figure>
			<figure class="right">3</figure>
			<figure class="left">4</figure>
			<figure class="top">5</figure>
			<figure class="bottom">6</figure>
		</div>
	</div>

	<div id="cube_btns">	<!-- 用于控制翻转的按钮,供js调用 -->
		<input type="button" value="前" id="cube_btn1">
		<input type="button" value="后" id="cube_btn2">
		<input type="button" value="右" id="cube_btn3">
		<input type="button" value="左" id="cube_btn4">
		<input type="button" value="上" id="cube_btn5">
		<input type="button" value="下" id="cube_btn6">
	</div>

下面要写CSS3代码，整出3D效果：

	#cube-con {
	    width: 200px;
	    height: 200px;
	    position: relative;
	    margin: 40px auto 40px;
	    -webkit-perspective:1000px;	/*从多远的距离进行观察，值越大，立体部分拉升越小*/
	       -moz-perspective:1000px;
	         -o-perspective:1000px;
	            perspective:1000px;
	}
	#cube {
	    width: 100%;
	    height: 100%;
	    position: absolute;
	    -webkit-transform-style:preserve-3d; /*转换成3D空间！*/
	       -moz-transform-style:preserve-3d;
	         -o-transform-style:preserve-3d;
	            transform-style:preserve-3d;
	    -webkit-transition:-webkit-transform 1s;
	       -moz-transition:-moz-transform 1s;
	         -o-transition:-o-transform 1s;
	            transition:transform 1s;
	    -webkit-transform:translateZ( -100px );
	       -moz-transform:translateZ( -100px );
	         -o-transform:translateZ( -100px );
	            transform:translateZ( -100px );
	}
	
	#cube figure {
	    width:196px;
	    height:196px;
	    display:block;
	    margin: 0; /* 如果没有这个，各个面可能不居中，导致翻转不绕中心*/
	    position:absolute;	/*应该使用绝对定位，因为它已经不是DOM流的形式了，更像float*/
	    border:2px solid black;
	    color:#fff;
	    font-size:130px;
	    font-weight:bold;
	    text-align:center;
	    line-height:190px;
	    opacity:0.8;
	}

所谓`translateZ`就是指在该轴方向进行位移，负值表示往正方向相反的方向移动，故而`translateZ(-100px)`的作用是往后推100个像素，浏览器会自动进行根据拉伸进行计算实际的尺寸。在这里是为了中点维持在中心，因为待会各个面还需要位移，以使得体现立体效果。
### 移动，旋转元素

现在所有的面都像一个普通平面图形一样面对着我们，接着对各个面进行处理，把各个面给拉开距离，并且旋转到合适的角度。俯视示意图如下：

![四面示意图](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/27945e857498ff05eb14e830e98e84a3201310230919311155.png)

其中正方体的边长为**200px**。

	#cube .front {		/*绕y轴旋转为0，故而正对我们，并且向前一步走（100像素）*/
	    background:#1abc9c;
	    -webkit-transform:rotateY(0deg) translateZ(100px);
	       -moz-transform:rotateY(0deg) translateZ(100px);
	         -o-transform:rotateY(0deg) translateZ(100px);
	            transform:rotateY(0deg) translateZ(100px);
	}
	#cube .back {   	/*绕x轴旋转180度，并且向前位移100，这个稍微有点难理解，看正文*/
	    background:#3498db;
	    -webkit-transform: translateZ(100px) rotateX(180deg);
	       -moz-transform: translateZ(100px) rotateX(180deg);
	         -o-transform: translateZ(100px) rotateX(180deg);
	            transform: translateZ(100px) rotateX(180deg);
	}
	#cube .right {		/*绕y轴转90度*/
	    background:#8e44ad;
	    -webkit-transform: translateZ(100px) rotateY(90deg);
	       -moz-transform: translateZ(100px) rotateY(90deg);
	         -o-transform: translateZ(100px) rotateY(90deg);
	            transform: translateZ(100px) rotateY(90deg);
	}
	#cube .left {		
	    background:#34495e;
	    -webkit-transform: translateZ(100px) rotateY(-90deg);
	       -moz-transform: translateZ(100px) rotateY(-90deg);
	         -o-transform: translateZ(100px) rotateY(-90deg);
	            transform: translateZ(100px) rotateY(-90deg);
	}
	#cube .top {		
	    background:#f39c12;
	    -webkit-transform: translateZ(100px) rotateX(90deg);
	       -moz-transform: translateZ(100px) rotateX(90deg);
	         -o-transform: translateZ(100px) rotateX(90deg);
	            transform: translateZ(100px) rotateX(90deg);
	}
	#cube .bottom {		
	    background:#c0392b;
	    -webkit-transform: translateZ(100px) rotateX(-90deg);
	       -moz-transform: translateZ(100px) rotateX(-90deg);
	         -o-transform: translateZ(100px) rotateX(-90deg);
	            transform: translateZ(100px) rotateX(-90deg);
	}

重点解释一下`translateZ(100px)`,尤其是在背面的时候，不是应该后退一步么？那是因为它的角度的问题，想象一下你站在原地，要以原点为对称点翻个身到后面的100px距离处，是不是先要向前一步走，然后翻到后面去。这就是为什么是向前一步走，而不是退后一步了。侧面也很好理解，由于本身是在xy平面的（0,0）处的，所以要往前站半个边长，才能让x轴正对身体中部。这些完全是坐标的关系导致的必须遵守的规则。

这样六个面就形成了。下面进行整体的旋转。

### 整体的旋转

是对cube整体的旋转和位移，六个面作为一个整体一起运动。注意是对cube添加css布局类。

	#cube.show-front {
	  -webkit-transform:translateZ(-100px); /* -100px 表示将cube拉后到z为0的平面，这样大小就不会变化了*/
	     -moz-transform:translateZ(-100px);
	       -o-transform:translateZ(-100px);
	          transform:translateZ(-100px);
	}
	#cube.show-back {
	  -webkit-transform:  rotateX(-180deg) translateZ(-100px);
	     -moz-transform: rotateX(-180deg) translateZ(-100px);
	       -o-transform: rotateX(-180deg) translateZ(-100px);
	          transform: rotateX(-180deg) translateZ(-100px);
	}
	#cube.show-right {
	  -webkit-transform: rotateY(-90deg) translateZ(-100px);
	     -moz-transform: rotateY(-90deg) translateZ(-100px);
	       -o-transform: rotateY(-90deg) translateZ(-100px);
	          transform: rotateY(-90deg) translateZ(-100px);
	}
	#cube.show-left {
	  -webkit-transform: rotateY(90deg) translateZ(-100px);
	     -moz-transform: rotateY(90deg) translateZ(-100px);
	       -o-transform: rotateY(90deg) translateZ(-100px);
	          transform: rotateY(90deg) translateZ(-100px);
	}
	#cube.show-top {
	  -webkit-transform: rotateX(-90deg) translateZ(-100px);
	     -moz-transform: rotateX(-90deg) translateZ(-100px);
	       -o-transform: rotateX(-90deg) translateZ(-100px);
	          transform: rotateX(-90deg) translateZ(-100px);
	}
	#cube.show-bottom {
	  -webkit-transform: rotateX(90deg) translateZ(-100px);
	     -moz-transform: rotateX(90deg) translateZ(-100px);
	       -o-transform: rotateX(90deg) translateZ(-100px);
	          transform: rotateX(90deg) translateZ(-100px);
	}

想象一下，怎样翻转会让各个面转动到面对着你。以`.show-right`为例吧，我们需要让它绕y轴反方向转动90度，总之面是怎么旋转的，我们现在只要对cube反着来就可以了。
	
	/*右面的旋转角度*/
	rotateY(90deg)

	/*把它转回正面，我们就反着来*/
	rotateY(-90deg)

这样就能达到整体的效果了。剩下的就是绑定事件，需要旋转时，给它设置对应的css类就ok了。下面是事件绑定的js代码：

	$(function(){
		// 省略其他
		// for cube
		var cubeClassArray = [
			'show-front',
			'show-back',
			'show-right',
			'show-left',
			'show-top',
			'show-bottom'
		];
	
		$('#cube_btns input').click(function(){
			var i = $(this).index();
			$('#cube').attr('class', cubeClassArray[i]);	// 设置cube的css类，进行旋转
		});

	});

好，一切大工告成了，你可以看到一个很酷的旋转六面体。

![3D cube](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/51d8fd0bc5f9f4258f731e504edbd0572013102309512713254.png)

参考：

+ 了解transform和animation[css3动画详解](http://beiyuu.com/css3-animation/)

---
end