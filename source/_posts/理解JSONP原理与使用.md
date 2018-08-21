---
title: 理解JSONP原理与使用
date: 2013-10-10 23:51:00
---
关于JSONP
===
by bibodeng 2013-10-10

## 写在前面
之前也不知道什么东东是JSONP（尽情笑话我吧）,只是听我的导师说前端和后台分开放，但是其绑定了不同的子域名，于是需要使用jQuery里面的JSONP支持，给服务端发送请求的时候给一个callback=?参数，然后返回的时候用callback包裹里面的数据。当我看到这篇关于 [跨域JSON请求](http://www.ibm.com/developerworks/cn/web/wa-aj-jsonp1/) 的文章的时候我才理解了这个做法。

## 什么是JSONP
到底什么是JSONP，其原理如何呢？
JSONP 是英文 json in padding,json就是javascript的字符串表现形式，服务器端可以对json进行收发解析。上面的文章给出了很详尽的解释，我就我学习中遇到的困难进行说明。

由于无法无法从不同源头的网站上直接获取JSON，但是我们平常的`<script>`标签是能够获取到别的网站的js文件，想想我们常常使用google的jquery吧，就像图片一样，可以随意使用。那么我们是不是可以将这个脚本的地址指向一个动态生成JSON的脚本呢？从而让它能够将生成的东西传到前端。显然这是可以的，和引入js相比只是动态与不动态的区别而已。但是传回来的东西应该是js代码，JSON不能直接使用，于是就用一个回调函数进行包裹。当它传回前端的时候就可以直接执行了。

维基百科的解释很容易懂，尤其是这个padding的意思：

这个时候，把 `<script>` 元素的 src 属性设成一个回传 JSON 的 URL 是可以想像的，这也代表从 HTML 页面透过 script 元素抓取 JSON 是可能的。然而，一份 JSON 文件并不是一个 JavaScript 程式。为了让浏览器可以在`<script>`元素执行，从 src 里 URL 回传的必须是可执行的 JavaScript。在 JSONP 的使用模式里，该 URL 回传的是由函数呼叫包起来的动态生成 JSON，这就是JSONP 的“填充（padding）”或是“前辍（prefix）”的由来。

## padding的形象体验
我在实际的编程中也用到了JSONP，本来可以直接使用`$callback.'('.json_encode($data).')';`的方式直接返回的，但是这样每次都要写括号，很难看。于是我就将它写成了一个函数，并且支持多个参数：

    // PHP代码
    
    // 带回调的响应
	function callbackResponse($callback, $status=200, $data="", $extra=array())
	{
	    // 这里就是padding了,中间的JSON被夹起来了！形象吧
		echo $callback.'('.ajaxResponse($status, $data, $extra).')';
		// include callback return of server end json data
		exit(0);
	}
	
	// 还是应该对返回内容进行merge后encode
	function ajaxResponse($status=200, $data="", $extra=array()) {
		$ret = array("status"=>$status, "data"=>$data);
		$ret = array_merge($ret, $extra);
		return json_encode($ret);
	}
	
	// ————————调用的例子————————
	$callback = $_GET['callback'];
	callbackResponse($callback, 200, "我爱编程");
	
在客户端可以是这样请求并处理的：

    // js代码
    // callback作为一个参数传到服务端
    $.getJSON(php_path+'php/index.php?callback=?', function(ret_data) {
		if (ret_data.status == 200) 
		{
		    console.log(ret_data['data']); // 我爱编程
			return;
		}
	});
	
## jQuery的做法

上面看到jQuery中的$.getJSON方法支持在链接中直接放入callback函数，并且callback=?,其实它是把$.getJSON的第二个参数（一个匿名函数）作为一个callback函数，我们查看服务器返回的数据常常能够看到 `jQuery152042227689944248825_1317400799214({"status": 200,"data":"我爱编程"})`形式的包。本来是一个名字的，例如一个叫parseData的函数，callback=parseData,当JSONP返回之后，将直接执行`parseData({"status": 200,"data":"我爱编程"})`,也就是回调了。而jQuery直接帮我们处理了匿名函数的问题，相当于产生了一个名字随机的对象，让它等于这个匿名的回调函数。具体的还得看jQuery的源代码（笔者才看了一点，还没到能够解决这个问题的程度）。

如下jQuery源码:

    // 获取时间戳
    var jsc = jQuery.now(), 
    jsre = /(\=)\?(&|$)|\?\?/i;
    
    // 默认的jsonp设置
    jQuery.ajaxSetup({
      jsonp: "callback",   // 默认使用callback
      jsonpCallback: function() {
        return jQuery.expando + "_" + ( jsc++ );    // 构造回调前缀
      }
    });
    // 下面的代码，额。。
    jQuery.ajaxPrefilter( "json jsonp", function( s, originalSettings, jqXHR ) {

      var inspectData = s.contentType === "application/x-www-form-urlencoded" &&
        ( typeof s.data === "string" );
    
      if ( s.dataTypes[ 0 ] === "jsonp" ||
        s.jsonp !== false && ( jsre.test( s.url ) ||
            inspectData && jsre.test( s.data ) ) ) {
        
        // 设置jsonCallback,当回调时，就能直接调用了
        var responseContainer,
          jsonpCallback = s.jsonpCallback =
            jQuery.isFunction( s.jsonpCallback ) ? s.jsonpCallback() : s.jsonpCallback,
          previous = window[ jsonpCallback ],
          url = s.url,
          data = s.data,
          replace = "$1" + jsonpCallback + "$2";
    
        if ( s.jsonp !== false ) {
          url = url.replace( jsre, replace );
          if ( s.url === url ) {
            if ( inspectData ) {
              data = data.replace( jsre, replace );
            }
            if ( s.data === data ) {
              url += (/\?/.test( url ) ? "&" : "?") + s.jsonp + "=" + jsonpCallback;
            }
          }
        }
    
        s.url = url;
        s.data = data;
    
        window[ jsonpCallback ] = function( response ) {
          responseContainer = [ response ];
        };
    
        jqXHR.always(function() {
    
          window[ jsonpCallback ] = previous;
    
          if ( responseContainer && jQuery.isFunction( previous ) ) {
            window[ jsonpCallback ]( responseContainer[ 0 ] );
          }
        });
    
        s.converters["script json"] = function() {
          if ( !responseContainer ) {
            jQuery.error( jsonpCallback + " was not called" );
          }
          return responseContainer[ 0 ];
        };
    
        s.dataTypes[ 0 ] = "json";
    
    
        return "script";
      }
    });

// TODO: 读通源代码
	
## 参考链接
[wikipadia](http://zh.wikipedia.org/wiki/JSONP)