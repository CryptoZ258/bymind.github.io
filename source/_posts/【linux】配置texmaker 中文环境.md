---
title: 【linux】配置texmaker 中文环境
date: 2013-03-08 12:24:41
---
{% raw %}
<p><span style="font-size:16px;">texmaker是一款用来编排文本（书籍/报告/信件）的软件，tex开始是由《TAOCP》的作者开发的，后来发展出很多latex啊等等，在ubuntu下，我想要将我的三年多的博客文章编排成一本电子书，虽然规好发现了一个自动生成的工具，但是我还是坚持试试这个据说很难又很cool的工具。上网查了一些教程，发现学过html的同学不会觉得难，如果是那些标记要记住的话，到时候翻手册还是可以的。在本文的后面附了电子书的下载地址。</span></p>
<p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">【安装texmaker】</span></span></p>
<span style="font-size:16px;"> </span><p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">在软件中心查找 texmaker，点击安装即可。</span></span></p>
<span style="font-size:16px;"> </span><p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">【使用texmaker】</span></span></p>
<span style="font-size:16px;"> </span><p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">texmaker使用比较简单，使用向导就很容易生成我们需要的文档，下面自己键入如下代码，并保存成.tex文件，然后选择构建，或者保存后按下F2，然后按F3。如果编译没有出问题的话，那么就可以看到效果了。</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">\documentclass[12pt landscape]{book}
\begin{document}</pre><pre class="brush:python; toolbar: true; auto-links: true;">this is my first tex.</pre><pre class="brush:python; toolbar: true; auto-links: true;">\end{document}</pre> <span style="font-size:16px;"> </span><p><span style="font-size:16px;"><br />
</span></p>
<p><span style="font-size:16px;">【中文支持】</span></p>
<p><span style="font-size:16px;">但是如果要使用中文，还要自己安装中文支持。首先要安装CJK宏包。在终端输入：</span></p>
<p><span style="font-size:16px;line-height:24px;color:#e56600;">sudo apt-get install latex-cjk-chinese</span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">即可完成安装。然后试试能不能输出中文，新建一个tex文件，输入如下代码：</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">\documentclass[12pt landscape]{book}
\usepackage{CJKutf8}
\begin{document}
\begin{CJK*}{UTF8}{gbsn}
\huge 女生节游戏——心有灵犀 
\end{CJK*}
\end{document}</pre><p></p>
<p><span style="font-size:small;"><span style="line-height:24px;">效果如下所示：</span></span></p>
<p style="text-align:center;"><a target="_blank" href="/content/plugins/kl_album/upload/201303/decafd4e8d53893c6f1fd5540a485920201303080444492861.png"><img src="/content/plugins/kl_album/upload/201303/decafd4e8d53893c6f1fd5540a485920201303080444492861.png" width="480" height="294" alt="点击查看原图" border="0" /></a></p>
<span style="font-size:16px;"> </span><p><span style="font-size:small;"><span style="line-height:24px;">latex教程：</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;"><a href="http://vdisk.weibo.com/s/sURX6">一本不太简短的tex介绍</a></span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;"><a href="http://vdisk.weibo.com/s/sUVSy">tex入门指南</a></span></span></p>
<span style="font-size:16px;"> </span><p>&nbsp;</p>
<p><span style="font-size:small;"><span style="line-height:24px;">by bibodeng &nbsp; &nbsp;2013-03-08</span></span></p>
<span style="font-size:16px;"> </span><p>&nbsp;</p>{% endraw %}
