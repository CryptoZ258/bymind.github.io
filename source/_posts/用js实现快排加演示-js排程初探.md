---
title: 用js实现快排加演示-js排程初探
date: 2013-10-25 08:27:58
---
用js实现快排加演示
===

by bibodeng 2013-10-24

## 缘起
有很多时候，我们都是需要重新做一个轮子，才知道轮子究竟是什么样子的，然后就可以在下一次碰到这种情况时能够立马写出来，并且能写得很好。本来我打算写一个快排，然后在页面中进行演示，我知道已经有很牛的人实现过了，但是我做这个的时候，遇到了一些困难，使我想起了前段时间想要写某个锁机制队列的时候，后来发现已经有一个同事已经实现了。

## 实现快排
先来写个快速排序吧。

	var qsort =  function(arr, p, q)
	{
		var x;
		if (p < q)	// 需要排序的元素个数不为0
		{
			x = partition(arr, p, q);	// 对数组进行partion处理
			qsort(arr, p, x-1);			// x之前部分  x是该轮确定位置的元素
			qsort(arr, x+1, q);			// 2次递归
		}
	};

	var partition = function(arr, p, q)
	{

		var tmp = 0,
			i 	= p,
			j 	= q + 1,
			base = arr[p];	// 首元素作为基准

		// 将数组分成两部分，大于base的，小于base的
	
		while (1)
		{
			
			while (arr[++i] <= base && i < q)；
			
			while (arr[--j] > base);		// 向中间逼近

			if (i >= j)	// 交叉了
			{
				break;
			}
			// 否则就交互两个数，正好比base大的和比base小的换了一下
			
			// swap(arr[i], arr[j]);
			tmp = arr[j];
			arr[j] = arr[i];
			arr[i] = tmp;
		}
		// 	交互基准值和中值

		arr[p] = arr[j];	// 将中间元素放到首部
		arr[j] = base;		// 将基准元素放到中间
		return j;		// 返回这个位置
	};

没什么特别的，几乎和C++的一模一样，其中swap在js下，因为不是传入参数不是引用类型，故而不起作用，故而直接引入tmp变量进行交换。下面是调用部分：

	$.(function(){
		// 进行测试
	
		var myArr = [],
			total = 50；
	
		for (var i = 0; i < total; i++)
		{
			myArr.push(parseInt((Math.random() * 450)));	// 0 - 450
		}
	
		// 绘制方格
		qsort(myArr, 0, myArr.length-1); 
	});

为了能够体现出排序的可视化效果，我打算绘制一些小方格排列在一起，就像下面这样：

![排序可视化](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/6666f6b0ea50298df61bfe5cad57efce2013102411275015768.png)

实现的代码并不麻烦，在ready中加入绘制方格的代码：

	// 绘制方格
	var str = '';
	for (var j = 0; j < total; j++)
	{
		str += "<li class='normal' style='height:"+myArr[j]+"px;'></li>";	// 添加元素
	}
	$partent.html(str);
	var $list = $('#sort_list').find('li');

其html代码，主要是提供容器，还有CSS样式。

	<html>
	<head>
	<style type="text/css">
	.normal{
		background-color: #222;
	}
	
	.base{
		background-color: #f22;
	}
	
	.selected{
		background-color: #22f;
	}
	
	#main{
		width: 1000px;
		height: 600px;
		margin: 10px auto;
		-webkit-transform: rotate(180deg);
	    -moz-transform: rotate(180deg);
	    -o-transform: rotate(180deg);
	    transform: rotate(180deg);
	}
	
	#sort_list li{
		float: left;
		width: 10px;
		margin: 1px;
		list-style: none;
	}
	
	</style>
	<title>快速排序</title>
	</head>
	<body>
		<div id="main">
			<ul id="sort_list">
			</ul>
		</div>
	</body>
	</html>

接下来就要实现排序过程中的动态效果了，这是一个很麻烦的事情。初步实现的例子是[这样的]()。尽管我试着在`partition`每一步中进行延时，但是排序算法始终太快了，而使用setTimeout的方法进行异步延时，得到的动画效果将和排序结果不兼容的。修改后的代码，增大了递归的时间间隔，但是夹逼的效果闪烁太快了，没有流动的动画效果。这其实是因为代码执行和DOM元素操作不同步引起的。

	var qsort =  function(arr, p, q)
	{
		var x;
		if (p < q)	// 需要排序的元素个数不为0
		{
			x = partition(arr, p, q);	// 对数组进行partion处理
			
			setTimeout(function(){
				qsort(arr, p, x-1);		// x之前部分  x是该轮确定位置的元素
			}, 1000);
			
			setTimeout(function(){
				qsort(arr, x+1, q);		// 2次递归
			}, 2000);
			
		}

		console.log('after sort', arr);
	};

并且setTimeout这东西，在循环下，是很耗费内存的，会导致页面奔溃，并且它之内将逻辑包围在一个函数参数里面，不太好。当把for循环换成setInterval调用时，元素操作效果倒是流畅了，但是排序结果却不正确了。原因是后续代码已经开始运行了。

## 异步的麻烦与解决办法

异步的麻烦，是真麻烦。我思考了一下，将排序算法和DOM操作混在一起是很野蛮的做法，没有做到数据加工和体现的分离。而当前状态又需要重绘，才能体现出其动态效果，但是重绘的代价也太大了，左思右想，没有想到好的解决办法，于是找到陈皓提到的日本程序员写的[排序可视化](http://coolshell.cn/articles/3933.html)，太强大了，效果也是一级棒，不过要细细剖析源码才知道它是如何实现的，这个改天再一探究竟，今天我要隆重介绍一下一个相当优雅的排程小程序，个人觉得写得相当优雅。

我们做很多编程工作时，往往想要同步（这里的同步指的是确定顺序，而不是不确定），例如在进行ajax请求时，回调结果往往要等一段时间才能返回，但是我们的程序的`return`却不知道要从哪里返回，如果在回调的外面，则等不到结果就返回了，如果在回调函数里面，则又返回不到正确的地方，这个时候就很有必要同步了。而一个排程的程序，对各个操作进行同步互斥，则可以让它们乖乖一个接一个按顺序执行，这就好比操作系统里面对资源的锁。具体可以参看[myunlessor写的排程策略详解](http://myunlessor.me/)。直接上代码吧：

	// 排程策略 - 全局定义
	var schedule = (function (self) {
	  var paused = false, // 标记状态
	      queue  = [];     // 队列

	  // 入队
	  self.join = function (fn, params) {
	    params = params || {};
	    var args = [].concat(params.args);

	    queue.push(function (_) {
	      _.pause();
	      setTimeout(function () {
	        fn.apply(params.context || null, args);
	        _.resume();
	      }, params.delay || 1);
	    });

	    return exec();
	  };

	  self.pause = function () {
	    paused = true;  // 忙碌
	    return this;
	  };

	  // ready and call next
	  self.resume = function () {
	    paused = false; // 空闲
	    setTimeout(exec, 1);
	    return this;
	  };

	  function exec() {
	    if (!paused && queue.length) {
	      queue.shift()(self);  // 出队
	      if (!paused) self.resume();
	    }
	    return self;
	  }

	  return self;
	}(schedule || {}));	// 立即执行，self就是schedule本身

我对着这个程序看了十来分钟，越看越有味道，从这个程序中可以看到javascript的很多good part,暂时没有看到缺陷，例如[]，用成了活生生的队列，使用push和shift进行入队出队操作。还有闭包，直接返回一个self，本身参数传的是schedule，而schedule本身是刚刚定义的，需要赋值的，这一切看起来多么地神奇，还有返回this，强大的链式调用，有木有，额有点跑题了。下面我们就应用到我们的排序中：
	
	var qsort =  function(arr, p, q)
	{
		var x;
		if (p < q)	// 需要排序的元素个数不为0
		{
			x = partition(arr, p, q);	// 对数组进行partion处理
			
			schedule
			.join(qsort,{
				delay: 100,
				args: [arr, p, x-1]
			})
			.join(qsort, {
				delay: 100,
				args: [arr, x+1, q]
			});
		}
	};

一切都相当优雅。当我打开浏览器测试时，发现，有了排程，而不是死板的setTimeout，动画变得流畅了很多。接下来的目标是接着优化`partition`里面的代码，使得这个过程也看起来很流畅。

	var partition = function(arr, p, q)
	{

		var tmp = 0,
			i 	= p,
			j 	= q + 1,
			base = arr[p];	// 首元素作为基准

		$list.attr('class', 'normal');
		schedule
		.join(showBase, {
			delay: 0,
			args: [p]
		});

		while (1)
		{
			
			while (arr[++i] <= base && i < q)
			{
				;// 只要是小于base且没到结尾就一直前进
				schedule.
				join(moveSelectedRight,{
					delay: 50,
					args : [i]
				});
			}

			while (arr[--j] > base){
				schedule.
				join(moveSelectedRight,{
					delay: 50,
					args : [j]
				});
			}

			if (i >= j)	// 交叉了
			{
				break;
			}
			// 否则就交互两个数，正好比base大的和比base小的换了一下
			
			tmp = arr[j];
			arr[j] = arr[i];
			arr[i] = tmp;

			// 交换两元素的位置，这里耍了点小聪明，用高度代替
			schedule
			.join(exchangeHeight,{
				delay: 50,
				args: [$list.get(i), $list.get(j)]
			});
		}
			
		
		// 	交互基准值和中值

		arr[p] = arr[j];	// 将中间元素放到首部
		arr[j] = base;		// 将基准元素放到中间

		schedule
		.join(exchangeHeight,{
			delay: 50,
			args: [$list.get(p), $list.get(j)]
		});

		$list.attr('class', 'normal');
		return j;		// 返回这个位置
	};

	// 将标志右移 只改颜色
	var moveSelectedRight = function(i){
		$('.selected').attr('class', 'normal');
		$($list.get(i)).attr('class', 'selected');
	};

	// 将标志左移
	var moveSelectedLeft = function(j){
		$('.selected').attr('class', 'normal');
		$($list.get(j)).attr('class', 'selected');
	};

	var showBase = function(base){
		$('.base').attr('class', 'normal');
		$($list.get(base)).attr('class', 'base');		// 将base染色
	};

	// 交换两个元素的位置 A 前 B 后
	var exchange = function(elemA, elemB){
		var m = $(elemA).next(),
			n = $(elemB).prev();

		console.log('交换');
		setTimeout(function(){
			$(elemB).insertBefore(m);
			$(elemA).insertAfter(n);
		}, 50);
		
	};

	// 只交换两者的高度
	var exchangeHeight = function(elemA, elemB)
	{
		var tmp = parseInt($(elemA).css('height'));

		$(elemA).css('height', $(elemB).css('height'));
		$(elemB).css('height', tmp+'px');
	};	

最后的效果，可以看[这里](http://bibodeng.com/bibodeng/js-algorithms/qsort/index.html)。但是显然这种DOM操作和算法混在一起的日子是不长久的，鬼群里面有人建议使用[D3一个数据DOM体现的插件](http://d3js.org/ "jquery-d3插件")，有待继续探索。勇敢的骚年，快去创造奇迹！！

## 参考

[js排程策略](http://myunlessor.me/blog/2013/06/04/strategy-for-scheduling-javascript-asynchronous-code/)

[可视化排序](http://coolshell.cn/articles/3933.html)

[jQuery D3](http://d3js.org/)

---
end