---
title: 【linux】ubuntu下语音报时
date: 2013-03-08 10:55:03
---
{% raw %}
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';"><span style="font-size:16px;line-height:21px;">【需要报时】</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">我们工作或者学习到一段时间，需要暂停一下，检视自己的方向是否有错误。windows下有人家已经写好的报时程序，但是在linux下，要打造报时就要费劲但有趣得多了。</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">【方案一】机器语音</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">使用ubuntu系统自带的语音功能，然后将date命令的输出内容念出来。命令如下：</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:Tahoma, Helvetica, Arial, STHeiti;font-size:16px;line-height:21px;"><span style="color:#e56600;font-size:16px;">espeak -v zh "现在时间是`date +%T|sed -e 's/:/时/1;s/:/分/1;s/$/秒/'`"</span> &nbsp; #电脑发音</span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:16px;line-height:21px;">保存成shell文件，然后放到某个目录下，例如我放到/usr/bin下，名字叫做saytime.sh。</span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:Tahoma, Helvetica, Arial, STHeiti;font-size:16px;line-height:21px;">在终端直接输入橙色字体的命令就能听到报时，但是要自动报时，还得写点程序，或者依赖他人的程序。这里需要用到的是一个叫做“计划任务”的软件，或者叫做“scheduled tasks”，在ubuntu的软件中心可以获得。然后填写一项定时重复的任务就可以了。如下所示：</span></p>
<p style="text-align:center;"><span style="color:#454545;font-family:Tahoma, Helvetica, Arial, STHeiti;font-size:16px;line-height:21px;"><a target="_blank" href="/content/plugins/kl_album/upload/201303/5e559949bc22c7f0f13ab2ca1e4884c22013030805403413869.png"><img src="/content/plugins/kl_album/upload/201303/5e559949bc22c7f0f13ab2ca1e4884c22013030805403413869.png" width="320" height="360" alt="点击查看原图" border="0" /></a><br />
</span></p>
<span style="font-size:16px;"> </span><p>&nbsp;</p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';"><span style="font-size:16px;line-height:21px;"><br />
</span></span></p>
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';"><span style="font-size:16px;line-height:21px;">这样每个小时就能听见不太悦耳的报时了。</span></span></p>
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';"><span style="font-size:16px;line-height:21px;">【方案二】播放录音</span></span></p>
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">机器语音的报时实在是太难听了，那么就自己录制一些报时音，然后编写脚本播放出来吧。其实这个程序并不复杂，有人已经写好了，本文尾部提供下载。</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">做法和上面一样，在scheduled task软件中增加一项，定每个小时执行一次脚本。将下载的文件包解压，然后可以看到一个wavs文件夹和一个saytime.sh的脚本文件，这个脚本文件的路径名要填写在command那一个空中。这样就能听见悦耳的整点报时了。</span></span></p>
<span style="font-size:16px;"> </span><p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;font-size:16px;">脚本的大概原理就是遇到什么字就播放什么名字的wav文件，这样连起来就成了报时语音。下面是saytime.sh的代码：</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">#!/bin/bash
cmd="date +%T|sed 's/CST//;s/年/ &amp;\n/;s/月/ &amp;/;s/日/ &amp;/;s/:/ 点 /;s/:/ 分 /;s/$/ 秒 /;s/星期/&amp; /;s/ 0/ /g'|sed '/年/s/[0-9]/&amp; /g'"
#cmd = "date +%T|sed -e 's/:/ 点 /1;s/:/ 分 /1;s/$/ 秒 /'"
#cmd = "date +%T|sed -e ''"  
time=($(eval $cmd))		# 对命令行求值

wavs_dir="$(dirname "$0")/wavs"
aplay "${wavs_dir}/xianzaishijian.wav"
for i in ${time[@]};do
    aplay "${wavs_dir}/$i.wav"
done</pre><p></p>
<p><span style="font-size:16px;">动手试试吧，是不是非常妙呢？</span><span style="color:#454545;font-family:Tahoma, Helvetica, Arial, STHeiti;font-size:medium;line-height:21px;">要想报出date命令的全部字符，则把第二行cmd字符串的“+%T”去掉就可以了，我是嫌全部报出来太长了才限定它只报时分秒。</span></p>
<p><span style="color:#454545;font-family:Tahoma, Helvetica, Arial, STHeiti;font-size:medium;line-height:21px;">by bibodeng 2013-03-08&nbsp;</span></p>
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;">下载链接：</span></span></p>
<p><span style="color:#454545;font-family:'Tahoma, Helvetica, Arial, STHeiti';font-size:small;"><span style="line-height:21px;"><a href="http://vdisk.weibo.com/s/sVdsA">saytime包</a></span></span></p>{% endraw %}
