---
title: 【python】解决project euler题目的乐趣
date: 2013-03-21 18:38:00
---
{% raw %}
<span class="Apple-style-span" style="border-collapse:separate;font-family:宋体;font-size:14px;line-height:normal;border-spacing:0px;"><p><span style="font-size:16px;">寒假期间学习了python，现在基本上就能上手使用它来解决project euler里面的题目了，用python真的是没得说的，一个字“赞”。在C++中需要用一大堆代码实现的算法，在python中，只需要那么短短几行。而且还有惊艳的运行速度。借用《可爱的python》里面的一句话：“人生苦短，我用python”。</span></p>
<p>&nbsp;</p>
<p><span style="font-size:16px;">【project euler 055】</span></p>
<p><span style="font-size:16px;">求经过一系列规则不能得到回文数的数的个数。题目在此：</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">Not all numbers produce palindromes so quickly. For example,</span></p>
<p style="margin-left:50px;font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">349 + 943 = 1292,</span><br />
<span style="font-size:16px;">1292 + 2921 = 4213</span><br />
<span style="font-size:16px;">4213 + 3124 = 7337</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">That is, 349 took three iterations to arrive at a palindrome.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">How many Lychrel numbers are there below ten-thousand?</span></p>
<p class="info" style="position:relative;cursor:help;font-size:16px;font-family:'trebuchet ms', sans-serif;"><span style="font-size:16px;">NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.</span></p>
<p>&nbsp;</p>
<p><span style="font-size:16px;">思路：从1到10000进行逐个扫描，对于每个数进行判断，是否经过上述规则都不能产生回文数。在python中，有很方便的做法判断一个数是否是回文数。只需比较对称的列表位置是否相同 arr[i] == arr[lenth-1-i], i从0开始。当然做完之后发现有牛人用几行代码就把一切搞定了。不信请看：</span></p>
<p><pre class="brush:python; toolbar: true; auto-links: true;">def Lycheck(n):
   for i in range(0,50):
       n = n+int(str(n)[::-1])
       if str(n)==str(n)[::-1]: return False
   return True
len([n for n in range(10000) if Lycheck(n)])</pre></p>
<p><span style="font-size:16px;">python给我的一个印象就是列表操作很方便，类型转换超级自由，而且对于大数的运算非常快。这道题目用python解只用了1s。amazing！ 另外一个很特别的是，python支持函数式编程，lambda算子可以创建函数对象，传入某个程式里面，非常了得。本人在DES的程序中，也看到了类似lambda(x,y: x^y)的函数，非常地神奇，能够对map里面的元素都执行这个操作。</span></p>
<p>&nbsp;</p>
<p><span style="font-size:16px;">【project euler 056】</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">A&nbsp;googol&nbsp;(10</span><sup><span style="font-size:16px;">100</span></sup><span style="font-size:16px;">)&nbsp;is&nbsp;a&nbsp;massive&nbsp;number:&nbsp;one&nbsp;followed&nbsp;by&nbsp;one-hundred&nbsp;zeros;&nbsp;100</span><sup><span style="font-size:16px;">100</span></sup><span style="font-size:16px;">&nbsp;is&nbsp;almost&nbsp;unimaginably&nbsp;large:&nbsp;one&nbsp;followed&nbsp;by&nbsp;two-hundred&nbsp;zeros.&nbsp;Despite&nbsp;their&nbsp;size,&nbsp;the&nbsp;sum&nbsp;of&nbsp;the&nbsp;digits&nbsp;in&nbsp;each&nbsp;number&nbsp;is&nbsp;only&nbsp;1.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">Considering&nbsp;natural&nbsp;numbers&nbsp;of&nbsp;the&nbsp;form,&nbsp;</span><em><span style="font-size:16px;">a</span><sup><span style="font-size:16px;">b</span></sup></em><span style="font-size:16px;">,&nbsp;where&nbsp;</span><em><span style="font-size:16px;">a,&nbsp;b</span></em><span style="font-size:16px;">&nbsp;</span><img src="http://projecteuler.net/images/symbol_lt.gif" width="10" height="10" alt="&lt;" border="0" data_ue_src="http://projecteuler.net/images/symbol_lt.gif" style="border-top-width:0px;border-right-width:0px;border-bottom-width:0px;border-left-width:0px;border-style:initial;border-color:initial;vertical-align:middle;" /><span style="font-size:16px;">&nbsp;100,&nbsp;what&nbsp;is&nbsp;the&nbsp;maximum&nbsp;digital&nbsp;sum?</span></p>
<p><span style="font-size:16px;">思路： 很明显，这个位的和要大，显然要够长。既要够长，每位数字的数字也要够长。我脑海里面立马蹦出了99的99次方这样的数字。但是不能想当然，我还是从91开始，计算到100，铁定能够找到那个各位和最大的数。程序如下：<pre class="brush:python; toolbar: true; auto-links: true;"># project euler 56
# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def power_digit_sum():
	max_digits_sum = 0
	for i in range(91,100):
		for j in range(91,100):
			power_num = pow(i,j)
			print power_num
			digits_sum = sum_digits(power_num)
			print digits_sum
			if digits_sum &gt; max_digits_sum:
				max_digits_sum = digits_sum
	print max_digits_sum
			
			
def sum_digits( power_num):
	digits_sum = 0
	while power_num != 0 :
		rear_num = power_num % 10
		power_num = power_num / 10
		digits_sum += rear_num
	return digits_sum
	#return sum(map(int, power_num))


power_digit_sum()</pre></span></p>
<p><span style="font-size:16px;">运行就能够找到答案了。</span></p>
<p><span style="font-size:16px;">【project euler 057】</span></p>
<p></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">It&nbsp;is&nbsp;possible&nbsp;to&nbsp;show&nbsp;that&nbsp;the&nbsp;square&nbsp;root&nbsp;of&nbsp;two&nbsp;can&nbsp;be&nbsp;expressed&nbsp;as&nbsp;an&nbsp;infinite&nbsp;continued&nbsp;fraction.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;text-align:center;"><img src="http://projecteuler.net/images/symbol_radic.gif" width="14" height="16" alt="√" border="0" data_ue_src="http://projecteuler.net/images/symbol_radic.gif" style="border-top-width:0px;border-right-width:0px;border-bottom-width:0px;border-left-width:0px;border-style:initial;border-color:initial;vertical-align:middle;" /><span style="font-size:16px;">&nbsp;2&nbsp;=&nbsp;1&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;...&nbsp;)))&nbsp;=&nbsp;1.414213...</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">By&nbsp;expanding&nbsp;this&nbsp;for&nbsp;the&nbsp;first&nbsp;four&nbsp;iterations,&nbsp;we&nbsp;get:</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">1&nbsp;+&nbsp;1/2&nbsp;=&nbsp;3/2&nbsp;=&nbsp;1.5</span><br />
<span style="font-size:16px;">1&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/2)&nbsp;=&nbsp;7/5&nbsp;=&nbsp;1.4</span><br />
<span style="font-size:16px;">1&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/2))&nbsp;=&nbsp;17/12&nbsp;=&nbsp;1.41666...</span><br />
<span style="font-size:16px;">1&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/(2&nbsp;+&nbsp;1/2)))&nbsp;=&nbsp;41/29&nbsp;=&nbsp;1.41379...</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">The&nbsp;next&nbsp;three&nbsp;expansions&nbsp;are&nbsp;99/70,&nbsp;239/169,&nbsp;and&nbsp;577/408,&nbsp;but&nbsp;the&nbsp;eighth&nbsp;expansion,&nbsp;1393/985,&nbsp;is&nbsp;the&nbsp;first&nbsp;example&nbsp;where&nbsp;the&nbsp;number&nbsp;of&nbsp;digits&nbsp;in&nbsp;the&nbsp;numerator&nbsp;exceeds&nbsp;the&nbsp;number&nbsp;of&nbsp;digits&nbsp;in&nbsp;the&nbsp;denominator.</span></p>
<p style="font-family:'trebuchet ms', sans-serif;font-size:16px;"><span style="font-size:16px;">In&nbsp;the&nbsp;first&nbsp;one-thousand&nbsp;expansions,&nbsp;how&nbsp;many&nbsp;fractions&nbsp;contain&nbsp;a&nbsp;numerator&nbsp;with&nbsp;more&nbsp;digits&nbsp;than&nbsp;denominator?</span></p>
<p><span style="font-size:16px;">思路：找规律，发现只要用几个变量就可以完全表示好这个式子的模式，从下往上看，有相当一部分x=（1/（2+1/2）），是由上一步产生的，而每步都是1+1/（2+x)组成的，而x的产生可以是递归的。另外第一次i=0的时候，比较特殊，是1+x的模式。</span></p>
<p><span style="font-size:16px;">总结规律如下：</span></p>
<p></p>
<p><pre class="brush:python; toolbar: true; auto-links: true;"># 计算展开式 e
# count 第几次展开, 采用递归法则
def cal_expansion(count,a,b):
   c = 1   
   d = 1    
   e = 2   # (2 + 1/2) 加号前的2
   if count == 0:  # first time is special
     c = b + a
     d = b
     return a,b,c,d   # 递归最底层
   elif count &gt; 0:  # the second time is special
     a = (b*e) + a
     a,b = swap(a,b)
     #print count,a,b
     count = 0            ​# 因为采用了自上而下，故而不这里的递归需要有所修改，直接奔第0次
     return  cal_expansion(count,a,b) #递归调用
 
# swap function
def swap(a, b):
    b,a = a,b
    return a,b


TIMES = 1000
# every time 
a,b,c,d = 1,2,1,1
count = 0
strc,strd ="",""
for i in range(0,TIMES):
    print i,"(",a,"/",b,")",c,d
    a,b,c,d = cal_expansion(i,a,b)   # 重复传递的a/b部分,如1/2， 2/5，5/12等，以及整个式子的结果c/d，如3/2
    strc,strd = str(c),str(b)
    if len(strc) &gt; len(strd):  #位数比较
        count +=1
print count</pre></p>
<p><span style="font-size:16px;">程序采用了递归，但是考虑到从上往下计算将会节省很多时间，故而用迭代进行计算。原以为迭代和递归是矛盾的，不能同时使用的，但是我先计算出的成果，从是能够运用到下一步的计算当中。这令我非常有成就感。下面是运行的例子：</span></p>
<p style="text-align:center;"><span style="font-size:16px;"><a target="_blank" href="/content/plugins/kl_album/upload/201303/3e434d96aefab6aa95f7e7edf8a865152013032110412618163.png"><img src="/content/plugins/kl_album/upload/201303/3e434d96aefab6aa95f7e7edf8a865152013032110412618163.png" width="480" height="284" alt="点击查看原图" border="0" /></a><br />
</span></p>
</span>{% endraw %}
