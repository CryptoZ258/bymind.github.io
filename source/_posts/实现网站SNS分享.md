---
title: 实现网站SNS分享
date: 2013-08-22 09:19:45
---
{% raw %}
<div>网页开发中，经常要实现将内容分享到sns网站，以获得更多的关注。在前段时间做活动页的过程中，多次用到了引入微博分享功能，要将一个分享写得优雅，正确，还真的需要一定的经验。平常的网页中，都有一些分享的js插件，只需要在页面中嵌入第三方的js代码就ok了。本文将讲讲怎样实现一个社交分享功能。</div>
<div>&nbsp;</div>
<div>方法一： 使用微博提供的接口，直接部署分享组件。</div>
<div>&nbsp;</div>
<div>在 <a href="http://open.weibo.com/widgets">http://open.weibo.com/widgets</a> 
这个页面中，有介绍各种常用的微博组件。按照文档，直接在该页面定制组件，生成代码，贴到我们的网页中去就可以了。</div>
<div>&nbsp;</div>
<div>方法二： 使用第三方的组件</div>
<div>&nbsp;</div>
<div>不直接在开放平台引入接口，而是用第三方的集成了多种社交网络的功能组件。例如 <a href="http://www.jiathis.com/">http://www.jiathis.com/</a>&nbsp;这里，也可以定制你常用的分享组件，和方法一差不多，都是嵌入一段代码。</div>
<div>&nbsp;</div>
<div>&nbsp;</div>
<div>方法三 ： 自己动手写js代码</div>
<div>&nbsp;</div>
<div>有时候网站设计上要求各种元素要丰富有个性，往往组件什么的就太简陋了，不太适用。那么就需要自己动手写一个分享功能。比如，在某些时候，我们的网页设计师给程序猿设计好了一个漂亮的分享按钮，但是是图片，那么这时候嵌入组件显然不太合适，那么就写一段代码，通过各种SNS网站的接口发布出去。我们发现，其实微博分享，也不过是构造一个url带有各种参数，传递到该页，然后打开一个新窗口，供用户发布就ok了。</div>
<div>&nbsp;<p><span style="line-height:1.5;">以新浪微博为例：</span></p>
</div>
<pre class="brush:js; toolbar: true; auto-links: true;">var Share = {
    openWindow: function(url, name, properties) {
        properties = (properties || "");
        if (!window.open(url, name, properties)) {
            window.self.location.href = url;
        }
        return false;
    },
    tsina:  function (title, href, content) {
        title = (title || "" );
        href = (href || window.self.location.href);
        content = (content || "" );
         var url = "http://v.t.sina.com.cn/share/share.php?c=spr_web_bd_tudou_weibo&amp;title=" + encodeURIComponent(title + "\n" + content) + "&amp;url=" + encodeURIComponent(href);
         return Share.openWindow(url, "Sina" );
    }
};</pre> <div>写一个函数，只要传入title，url，还有要分享的content，那么就可以构造一个分享的链接了。分享的链接格式，所带参数名称都要参考对应的开放平台的文档。依次类推，就可以写出一个自己的Share库了，这样就可以调用Share.tsina()这样进行分享了，极大地方便了js编写分享功能。对于url进行了encodeURIComponent()处理，将一些在url中的控制字符转换成为安全的编码格式。你将会看到编码成这样的奇怪的url：<a href="http://share.sina.com/index.php?title=%E9%87%91%E7%AB%8B%E5%AE%98%E7%BD%91">http://share.sina.com/index.php?title=%E9%87%91%E7%AB%8B%E5%AE%98%E7%BD%91</a></div>
<div>&nbsp;</div>
<div>有了这个基础，就可以做选择某部分文本进行分享，点击某按钮进行分享了。更多微博控件，可以参考<a href="http://open.weibo.com/widgets" style="line-height:1.5;font-family:'sans serif', tahoma, verdana, helvetica;">http://open.weibo.com/widgets</a></div>
<div>&nbsp;</div>
<div>by bibodeng</div>{% endraw %}
