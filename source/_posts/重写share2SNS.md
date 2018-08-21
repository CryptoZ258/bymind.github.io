---
title: 重写share2SNS
date: 2013-11-21 10:48:04
---
重写share2SNS
===

by bibodeng 2013-11-20

## 前言

前段时间，@myunlessor 兄跟我讨论的时候提到我之前用的那个分享到SNS网站的js写得并不够优雅，有许多冗余的地方。而我最近也在看javascript的设计模式，发现代理模式非常适合这种用来发送一组GET请求的情况，尤其是参数较少的时候。于是我就试着实现一个代理模式实现的版本。

## 代理模式版本

代理，顾名思义就是起到一个控制作用，实现的是和本体一样的接口方法，只是在发送请求的时候，进行参数的检查，或者是动态生成本体对象，然后向服务器发送请求。@myunlesser 兄指点我用js模板方法，这个方法高明了很多，因为每个SNS平台的url参数很不一样，如果每次都要检测这么多参数，将会非常麻烦。然而它们只是名字不同而已，我们可以赋予相同的标签如`{title}`，这样可以起到一个转接的作用。故而可以使用模板的方法，将匹配到的参数填充到url中。只需要在传入参数时指定参数对，然后用`fetchData`方法组装起来。

    var share2SNS = (function(){
	
	    // 所有url集中在一处，而且表示方法很自由
	    // 如sina的title是title+content 那么 使用${title} ${content}就能够将它们组合在一起，模板的威力可见一斑
        	var urls = {
        		sina: "http://v.t.sina.com.cn/share/share.php?pic=${pics}&title=${title} ${content}&url=${url}",
        		douban: "http://www.douban.com/recommend/?url=${url}&title=${title}"
        		// ...
        	};
        	
        	function _openWindow(url, name, properties) {
        		properties = (properties || "");
        		if (!window.open(url, name, properties)) {
        			window.self.location.href = url;
        		}
        		return false;
        	};
        	
        	// build the url 
        	function _fetchData(platform, params){
        		// fetch and replace
        		var baseUrl = ''+urls[platform];
        		var exp = /\$\{([^\{\}]+)\}/g;  // 括号里面的是分组
        		var tmp = '';
        		// 对url的参数进行填充
        		baseUrl = baseUrl.replace(exp, function(a, match){	
        		    // a is the whole match: ${abc}, match is the group:abc
        			tmp = (params||{})[match]  || '';	// get the proper params
        			return encodeURIComponent(tmp);	
        		});
        		return baseUrl;
        	}
        	
        	
        	// return proxy
        	return {
        		// public 
        		// params {title, content, url, pics} 唯一要知道的接口
        		shareTo : function (platform, params){
        			params['title'] = params['title'] || undefined, 
        			params['content'] = params['content'] || undefined,
        			params['url'] = params['url'] || undefined,
        			params['pics'] = params['pics'] || undefined;
        			
        			var surl = _fetchData(platform, params);
        			// console.log(surl);
        			_openWindow(surl, platform);
        		}
        	};
        	
    })();

使用闭包的立即执行函数返回一个share2SNS的单体，外部只能通过shareTo方法调用：

    share2SNS.shareTo('sina', {
        	title: 'IT小小鸟',
        	url: 'http://bibodeng.com',
        	content: '我们的大学生活',
        	pics: 'http://bibodeng.com/bibodeng/IT_birds/img/daoluan.png'
    });

可以说比较核心的方法就是js模板，我曾经想过让用户传入特定的参数对，例如`{href:'http://bibodeng.com'， pic: 'daoluan.png'}` 等名字不一的键值对，然后通过join操作用&连起来，但是那样会增大接口使用者的负担，而且没有起到解耦的作用。

一个程序员，要把复杂的事情变简单，这才是能力。又长又臭的代码，谁都可以写，但是优雅简洁的代码不是随便能写出来的。最近在学习《javascript设计模式》，里面的很多的东西都能够把事情变得简单，虽然一些模式本身就挺复杂的，但是掌握了其框架之后，写出来的代码明显优雅了很多。之前在实习的过程中碰到稍复杂的功能需求时感觉力不从心，很大程度就是不懂设计模式，看的过程种很多次都会发出这样的感慨，原来我不知不觉用过一些模式，而且有些模式用了之后整个app就简单了很多。继续攻书。

by bibodeng 2013-11-21