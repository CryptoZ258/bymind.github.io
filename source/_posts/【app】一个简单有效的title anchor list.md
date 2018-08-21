---
title: 【app】一个简单有效的title anchor list
date: 2012-10-18 16:54:37
---
{% raw %}
<p><span style="font-size:14px;">上次看到思愿君写了一个pc端的软件用来搜索一遍html文件，然后输出一个新的html文件，而这个文件是包含了标题锚点列表的。例如有时候我们想写一些文章，分为很多部分，每个部分需要有一个标题，让文章看起来非常的有条理。有了这个想法，那么我们就非常自然地想到要用更加方便的方法来输出这个带有锚点的列表到文档里面了，很自然地也就想到了javascript（很高兴我知道js能干些什么）。将下列的代码复制到你的博文的html源代码中，你就可以完成这个任务了，是不是造福了广大博客爱好者啊？</span></p>
<pre class="brush:js; toolbar: true; auto-links: true;">&lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"&gt;&lt;/script&gt;
&lt;script type="text/javascript" &gt;
// when the page is loaded
$(document).ready( function(){
		
		//  first create the ul element

		$('body').prepend('&lt;ul id="title_anchors"&gt;&lt;/ul&gt;');
		// alert($('body').html());
		// first give you an cycle to search for the title
		// only list h3 
		var count = 1;
		$('h3').each(function(){
			// give the title an anchor address
			$(this).attr('id', 'title'+count);
			$(this).attr('name', 'title'+count);
			
			// add the anchor list to the ul
			var list_item = $(this).text();  		// get the text and write into the list	
			$('ul#title_anchors').append('&lt;li&gt; &lt;a href="#title'  +count+ ' "&gt;'+list_item+' &lt;/a&gt;&lt;/li&gt;');  // add to the ul list	
			count ++; 				// increase the count
		});
			
	}); 
	
&lt;/script&gt;</pre><pre><span style="font-size:14px;">这个代码的原理就是选取出所有的h3 元素（是的，就是h3,也就是说你的标题要是h3的，如果不想用h3,你可以将上面的代码中的$('h3')改为 $('hx')，其中x是数字1,2等</span><span style="font-size:14px;">）</span></pre><pre><span style="font-size:14px;">这也是缺陷之一，要手工改代码，但是我一想，简单一点有简单一点的好处，即使能搞出一个嵌套的标题列表（大标题嵌入小标题</span><span style="font-size:14px;">），</span></pre><pre><span style="font-size:14px;">也就成了目录了，那么博文也不叫博文，而叫book了。哈哈，其实你明白的我只是技术不济而已。其原理就是选取DOM中的h3元素，然后</span></pre><pre><span style="font-size:14px;">向其中添加id和name属性，然后建立一个带链接的列表，每个链接都是一个锚点，对应着一个h3</span><span style="font-size:14px;">。</span></pre><pre><span style="font-size:14px;">下面做一个实例：<a href="/bibodeng/web_test/titleAchor.html">example</a></span></pre> <ol>
<li><span style="font-size:14px;">写好一篇文章，为所有的标题写好标签&lt;h3&gt; &lt;/h3&gt;</span></li>
<li><span style="font-size:14px;">将代码复制到你的文章源代码中，一般编辑器中都有一个“html</span><span style="font-size:14px;">源代码”按钮</span></li>
<li><span style="font-size:14px;">还要干什么，不用了，发布你的文章吧</span></li>
</ol>
<p></p>
<p><span style="font-size:14px;">by bibodeng 2012-10-18    </span></p>{% endraw %}
