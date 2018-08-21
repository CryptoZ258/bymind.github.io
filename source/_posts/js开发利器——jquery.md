---
title: js开发利器——jquery
date: 2012-10-16 19:38:05
---
{% raw %}
<p></p>
<h3>【js开发的烦恼】</h3>
<p></p>
<p>作为一个js学习者，在平时的练习与学习中，所不能避免的一件事就是“浏览器兼容”问题。因为实在是让人头痛，所以记忆深刻。在开发中，时常要小心谨慎地测试。就在上次开发的视力app中，就有不兼容的问题，在ubuntu下用开源chrome打开app则会看到那个焦点块飞走了！！真是干瞪眼，白着急。好在有开发利器jQuery,这个集以下作用于一身的工具：</p>
<p>1、弥合浏览器兼容性的中间体</p>
<p>2、众多实用功能的API提供者</p>
<p>3、良好的封装体，利于扩展的平台</p>
<p>有了jQuery可以很方便地选取元素，修改内容，实用AJAX，以及做出非常漂亮的UI。下面一一回顾一下这周所学的jQuery知识点，当然也可以参考jQuery的<a href="http://www.w3school.com.cn/jquery/index.asp">学习站点w3school</a>。</p>
<p></p>
<h3>【jquery的选择器】</h3>
<p></p>
<p>jquery实现了一个非常方便的选择器，其形式如同CSS的选择器一般：</p>
<p>假设页面中有如此一段文档：</p>
<p></p>
<blockquote>
<p>&lt;form&gt;</p>
<p>&lt;input type="text" id="task"&gt;</p>
<p>&lt;input type="submit" id="add_btn"&gt;</p>
<p>&lt;/form&gt;</p>
<p></p>
<p>&lt;ul id="task_list"&gt;</p>
<p>&nbsp; &nbsp; &lt;li&gt;go shopping 7:00 pm&lt;/li&gt;</p>
<p>&nbsp; &nbsp; &lt;li&gt;send email to Mr Chen&lt;/li&gt;</p>
<p>&lt;/ul&gt;</p>
<p>&nbsp;</p>
</blockquote>
<p>那么如下代码，可以方便地选取列表中元素，然后绑定点击事件。</p>
<blockquote>
<p>$('ul#task_list li').bind('click', function(){</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; this. addClass();</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;});</p>
</blockquote>
<p>&nbsp;说明： $() 是选取符号，可以选取文档对象和集合。例如$(document).ready(); $(this).addClass();</p>
<p>当然该符号也表示对对象进行jQuery的封装，这样就可以调用jQuery库里面的各种函数API了。</p>
<p>再例如下面的代码，将选取task的内容：</p>
<p>$('input:text').attr('value')</p>
<p>然后用该获取的数据赋值或者加工以备使用。可以说jQuery的选择符非常地方便。当然还有find（）、siblings（）查找兄弟节点、next（），prev（），parent（）、children（）等非常有用的API用来选取和过滤元素。还是到用时多翻几次工具书，写过几次便熟悉了。</p>
<p></p>
<h3>【jQuery的事件绑定方法】</h3>
<p></p>
<p>一般情况下，我们可以使用DOM的 addEventListener()，delegate()或者click()等函数为文档元素添加事件监视，但是这样做可能会不兼容（IE的可能是attachEvent() ，甚至其他浏览器还有不同的API）.而jQuery 提供了强大的事件API:</p>
<p>bind('事件名'，回调函数);&nbsp;</p>
<p>$('input:submit').trigger('click'); &nbsp;// 这句模拟触发click事件</p>
<p>jQuery提供非常丰富的事件API: click() , blur(), focus(), mouseout(), mouseover(),hover(函数一，函数二), toggle(函数一，函数二)</p>
<p></p>
<h3>【jQuery访问内容和属性】</h3>
<p></p>
<p>jQuery要能方便地读取和修改文档的内容，这样交互起来才让用户觉得其中的体验大大超过查看静态的文档。要访问html文档中的内容可以使用如下的API：</p>
<p>&nbsp;attr(); // 传入一个参数，获取参数名对应的属性值，可以传入名值对可以设置属性</p>
<p>例如 attr('id', 'tmpID');</p>
<p>attr(</p>
<p>{title:'helloworld',&nbsp;</p>
<p>id: 'tmpId'</p>
<p>});</p>
<p>text() // 访问该元素的文本，不含标记</p>
<p>html() // 访问该元素内的html内容，包含标记</p>
<p>append() // 在当前元素的子元素中追加，prepend()为在最首添加。例如 $('ul').prepend('&lt;li&gt;hello&lt;/li&gt;');</p>
<p>after() &nbsp;// 添加到当前元素之后</p>
<p>before() // 添加到当前元素之前</p>
<p>insertAfter() // 将选择集插入到另外一个选择集中之后</p>
<p>wrap() // 包装为元素 wrap('&lt;div&gt;&lt;/div&gt;');</p>
<p></p>
<h3>【jQuery的CSS接口】</h3>
<p></p>
<p>$('div').css('font-size'); &nbsp;// 获取div元素的文字大小css属性</p>
<p>outerWidth() / outerHeight() &nbsp; &nbsp; // 获取大小 包括</p>
<p>&nbsp;</p>
<p></p>
<h3>【ajax】</h3>
<p></p>
<p>$.get('xml文件名', 回调函数function($xml){相关操作}); &nbsp; // get xml文档</p>
<p>要传输一些数据，可以在第二个参数作为参数传输到服务器</p>
<p>$.getJSON() // 同上，只不过第一个参数请求的是JSON文件，而function里面也可以对JSON数据直接像对象一样操作</p>
<p>$.load() // 直接加载html文档，同上</p>
<p>$.post() // 使用post方法</p>
<p>使用AJAX可以异步传输数据，所谓异步传输，就是不重新加载整个页面，而是一部分内容进行修改，这样页面就可以动态响应用户的操作。例如一个上传文件功能，按下提交按钮后，则悄悄上传了文件，而不必重新加载整个页面。又如注册的时候异步检测用户名是否已经存在。</p>
<p>&nbsp;</p>
<p></p>
<h3>【小结】</h3>
<p></p>
<p>另外，jQuery 还有一些非常有用的扩展，例如jQuery UI 还有 移动终端开发HTML5 app的jQTouch。这些工具都很容易上手，往往调用一个API，传入几个参数就可以完成非常复杂的功能。 jQuery所提供的以上功能，能够满足我们的大部分需要，最重要的是使我们免受浏览器兼容之苦，当然以后自己编写jQuery插件的时候，也需要考虑这个问题。有了jQuery开发之后，一些功能变得简单许多，开源的库有的就是这个优点。另外我们的GTD项目，接下来的目标是配合后台PHP打开数据和界面之间的通道。</p>
<p>&nbsp;</p>
<p>by bibodeng 2012-10-16</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<style type="text/css">
body{
font-size: 14px;
letter-spacing: 1px;
line-height: 1.3em;
}

h3{
background-color:#000000;
color:#FFFFFF;
padding: 10px;
}

blockquote{
background-color:#CCFF99;
-webkit-border-radius: 5px;
}

.part_head{
background-color:#99FF33;
padding: 10px;
}

.example{
background-color:#CCCCCC;
font-size:1.2em;
-webkit-border-radius: 5px;
}

.small_title{
font:italic;
padding: 5px;
}
</style>{% endraw %}
