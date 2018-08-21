---
title: 带微信功能的sae博客
date: 2013-05-09 17:21:34
---
{% raw %}
<div class="art_content" style="font-size:15px;letter-spacing:1px;line-height:1.3em;"><h3 style="background-color:#222222;color:#ffffff;padding:10px;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';">﻿准备</h3>
<p style="font-family:'Times New Roman';">在安装之前，需要准备好博客系统的源代码（含微信响应功能，使用python为sae定制），这可以从github上下载：</p>
<p style="font-family:'Times New Roman';">pyweixin_saelog:&nbsp;</p>
<p style="font-family:'Times New Roman';">会用git的同学可以直接cd到想要放置的命令，如/home/bibodeng/git/下，然后在终端运行如下命令：</p>
<blockquote style="background-color:#ccff99;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';"><p>git clone https://github.com/bibodeng/pyWeiXin_SAElog.git</p>
</blockquote>
<p style="font-family:'Times New Roman';">&nbsp;如果不会用git的同学，就到<a href="https://github.com/bibodeng/pyWeiXin_SAElog/blob/master/pyweixin_saelog.zip" target="_blank">这里</a>下载压缩包(直接点view raw下载)，解压缩到你想要的任意文件夹下。接下来就进入配置与部署过程。</p>
<h3 style="background-color:#222222;color:#ffffff;padding:10px;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';">安装过程</h3>
<h4 style="font-family:'Times New Roman';">配置</h4>
<p style="font-family:'Times New Roman';"><span style="font-size:16px;">修改 /config.yaml 把 name:&nbsp;<strong>appname</strong></span><span style="font-size:16px;">&nbsp;改为自己的appname，如scnuwriter；<br />
修改 setting.py 的相关设置，每项后面都有说明,包括邮箱，还有数据库密码等。</span></p>
<p style="font-family:'Times New Roman';"><span style="font-size:16px;">还有如果不想把自己的博客设为debug状态，可以在</span><span style="font-size:16px;">index.wsgi文件setting里面，将debug选项改成false。</span></p>
<h4 style="font-family:'Times New Roman';"><span style="font-size:16px;">部署</span></h4>
<p style="font-family:'Times New Roman';"><span style="font-size:16px;">接下来<br />
到SAE 后台开通相关服务（mysql/Storage/Memcache/Task Queue）<br />
这些服务SAE 是不会自己开通，需要到后台手动完成：<br />
</span></p>
<blockquote style="background-color:#ccff99;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';"><p><span style="font-size:16px;"># 1 初始化 Mysql （这是必要的）<br />
# 2 建立一个名为&nbsp;</span><strong>attachment</strong>的 Storage （发帖时上传图片或附件用的）<br />
# 3 启用Memcache，初始化大小为<strong><span style="font-size:16px;">1M</span></strong><span style="font-size:16px;">&nbsp;的 mc，大小可以调，日后文章多了，PV多了可酌情增加，让你的博客响应更快。<br />
# 4 创建一个 名为&nbsp;</span><strong><span style="font-size:16px;">default</span></strong><span style="font-size:16px;">&nbsp;的 Task Queue 这个是用来做发提醒邮件，选择</span><strong><span style="font-size:16px;">顺序队列</span></strong><span style="font-size:16px;">&nbsp;等级 为</span><strong><span style="font-size:16px;">1</span></strong></p>
&nbsp;</blockquote>
<p style="font-family:'Times New Roman';"><span style="font-size:16px;">打包程序，在SAE 后台通过打包上传代码,注意压缩包下面必须是所有的目录与文件，因为上传展开的是压缩包内的结构；</span><span style="font-size:16px;">打开 http://your_app_id.sinaapp.com/install 如果出错刷新两三次就可以，</span><span style="font-size:16px;">提示要输入管理员帐号。</span></p>
<h3 style="background-color:#222222;color:#ffffff;padding:10px;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';">结果</h3>
<p style="font-family:'Times New Roman';">就这样你的带微信响应功能的博客就搭好了，如果还没有微信的公众号，赶紧去 微信 申请一个吧，然后将blog里面的微信地址填到开发模式的url和token里面，token默认为bibodeng，可以到源代码下察看blog.py源文件下的TOKEN全局变量的值,甚至可以自行修改。默认的如下：</p>
<blockquote style="background-color:#ccff99;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';"><p>url：<a href="http:" target="_blank"></a><a href="http://your_app_id/" target="_blank"></a><a href="http://your_app_id.sinaapp.com/weixin" target="_blank">http://your_app_id.sinaapp.com/weixin</a></p>
<p>token：bibodeng</p>
</blockquote>
<p style="font-family:'Times New Roman';">点击验证，通过后启用开发者模式就可以让你的博客响应微信用户的请求了，可以把你的微信公众帐号推广给其他人，这里就不详述了。enjoy it !</p>
<h3 style="background-color:#222222;color:#ffffff;padding:10px;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';">END</h3>
<p style="font-family:'Times New Roman';">&nbsp;参考链接：&nbsp;<a href="http://saepy.sinaapp.com/topic/50/saepy-log-v0-0-2-%E4%BD%BF%E7%94%A8%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97" target="_blank">SAEpy-log安装指南</a>&nbsp;&nbsp;本文有部分内容引用于此</p>
<p style="font-family:'Times New Roman';"></p>
<p style="font-family:'Times New Roman';">by bibodeng 2013-05-09</p>
</div>{% endraw %}
