---
title: 字符串匹配——RK算法
date: 2012-10-21 00:09:02
---
{% raw %}
<div><span style="font-size:18px;">【RK算法】</span></div>
<span style="font-size:14px;"> </span><p><span style="font-size:14px;">RK字符串匹配算法，在思想上是很简单易懂的，将字符串当成是一串数字，可以进行计算，若其值相等，那么字符串也便相等了。字符串视为数字有一个好处那就是减少了运算，在前面“朴素的字符串匹配”中，我们可以看到，如果按照一个个比对的办法将会花费 
m *(n -m+1)的时间，但是如果是数字的话，从 T = “125025”中要匹配P = “25”则可以按如下过程进行计算：</span></p>
<p style="text-align:center;"><a target="_blank" href="/content/plugins/kl_album/upload/201210/6d689ec29701bbc33d8f02dfd9a17901201210201616014944.png"><img src="/content/plugins/kl_album/upload/201210/6d689ec29701bbc33d8f02dfd9a17901201210201616014944.png" width="480" height="267" alt="点击查看原图" border="0" /></a></p>
<span style="font-size:14px;"> </span><div align="center"><img src="file:///C:/Users/bibodeng/AppData/Local/Temp/%E4%B8%BA%E7%9F%A5%E7%AC%94%E8%AE%B0/8fdec06d-1139-4492-95d8-84ccb5195892_0_files/2076656.png" /></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">1、开始从1进行匹配，而计算得到 t0 = 12 // t i的长度和要匹配的模式P相同，皆为m = 2</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">2、t0 不等于 模式P的对应值 25，故而继续往下计算，得 t1 = 25&nbsp; // 其计算过程为 t1 = {t0 - 
T[1]*10^(&nbsp;m-1)} * 10 + T[2]&nbsp;</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">3、 t1 与P的值相同，故而匹配，继续往下，知道T的末尾</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">&nbsp;</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">这个方法的核心思想就是将匹配计算通过式子 t(i+1) = {t( i) - T[i]*10^(&nbsp;m-1)]}*10 + T[i+m] 
来减少匹配的运算。但是这个方法有一个局限，那就是该方法对于图形字符不太方便。但我们可以将字符也看成一个数字，比如可以取它的ASCII码来做该字符对应的数值，而对于计算出来的数值可能不适合存放在较小的空间中，故而要对q取模，但是还是不可避免的有可能值相等的时候字符串并不相等q最好是一个足够大的素数，如果真的不幸是一次伪匹配，那么还是需要进行从头至尾的一对一比对，当然这样的计算量还是比朴素法小，最糟情况就是遇到的全部是伪匹配，其复杂度为 
m *(n -m+1)。</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">&nbsp;</span></div>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">闲话少说，上代码：</span></div>
<div>
<div><span style="color:#008000;font-size:13pt;">// Rabin-Karp 
算法将字符当做数字来运算</span></div>
<div><span style="color:#0000ff;font-size:13pt;">void<span style="color:windowtext;"> RKStringFetch(</span>const<span style="color:windowtext;"> string &amp;context,</span>const<span style="color:windowtext;"> string &amp;parten)</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> n = context.length();</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> m = parten.length();</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">if</span>(n&lt;m)</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">return</span>;</span></div>
<div></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> q = 29; <span style="color:#008000;">// 
挑选一个足够大的素数</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> h = ((<span style="color:#0000ff;">int</span>)pow(10.0, m-1)) % q; <span style="color:#008000;">// 为减少运算量，从而先对^m-1做模运算</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> p = 0;</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">int</span> t = 0;</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">char</span> x,y; <span style="color:#008000;">// 
用来存当前字符转换成的数字</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">for</span>(<span style="color:#0000ff;">int</span> i = 0; 
i&lt;m ; i++)</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = 
parten[i];</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y = 
context[i];</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p = (10*p + 
atoi(&amp;x) ) % q; <span style="color:#008000;">// 计算模式的值</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t = (10*t + 
atoi(&amp;y)) % q;</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;}</span></div>
<div></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">for</span>( <span style="color:#0000ff;">int</span> s= 0; 
s&lt;= n-m; s++) <span style="color:#008000;">// 
从字符串开头到末尾（n-m+1位置）</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">if</span>( p == t) <span style="color:#008000;">// 
如果值相等了</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">for</span>(<span style="color:#0000ff;">int</span> len=0; 
len&lt;m; len++) <span style="color:#008000;">// 还要进行一一匹配</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">if</span>(context[s+len] != parten[len])</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">break</span>; <span style="color:#008000;">// 
伪匹配</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0000ff;">if</span>(len == m-1)</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout 
&lt;&lt;s&lt;&lt;endl;</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<span style="color:#008000;">// if end</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = context[s]; <span style="color:#008000;">// s</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y= 
context[s+m];&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#008000;">// 存放s+m处的字符</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t = 10*(t - 
atoi(&amp;x)*h) +( atoi(&amp;y) % q); <span style="color:#008000;">// 
计算下一个</span></span></div>
<div><span style="color:windowtext;font-size:13pt;">&nbsp;&nbsp;&nbsp;&nbsp;}</span></div>
<div></div>
<div><span style="color:windowtext;font-size:13pt;">}</span></div>
</div>
<div>&nbsp;</div>
<div><span style="font-size:14px;">对于图形字符，例如0-9 
A-F可以看成是十六进制，有一个相对应的关系，任何进制在本质上都是一样的。对于ASCII码中的所有字符，可以看成是一个256进制的来计算。</span></div>
<span style="font-size:14px;"> </span><p><span style="font-size:14px;">&nbsp;</span></p>
<p><span style="font-size:14px;">上一篇 朴素的字符串匹配</span><a href="/?post=72">http://bibodeng.web-149.com/?post=72</a></p>
<span style="font-size:14px;"> </span><div><span style="font-size:14px;">by bibodeng&nbsp; 2012-10-21 &nbsp;欢迎探讨</span></div>{% endraw %}
