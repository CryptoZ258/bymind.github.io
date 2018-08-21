---
title: C C++复仇记(上)
date: 2013-04-16 21:46:27
---
{% raw %}
<div class="art_content" style="font-size:15px;letter-spacing:1px;line-height:1.3em;"><p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">由于前几天的笔试很大程度上刺激了我，让我越发感觉到自己的C/C++基础十分地薄弱，故而想要找几本经典的C/C++书本来深入了解一下C/C++语言特性，以及其中需要注意的问题。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">google了一下C语言经典著作，得到了我想要的结果：</p>
<blockquote style="background-color:#ccff99;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';"><p style="margin-top:0px;margin-bottom:0px;">《C专家编程》</p>
<p style="margin-top:0px;margin-bottom:0px;">《C语言详解》</p>
<p style="margin-top:0px;margin-bottom:0px;">《C语言核心技术》</p>
<p style="margin-top:0px;margin-bottom:0px;">《C陷阱与缺陷》</p>
<p style="margin-top:0px;margin-bottom:0px;">《C和指针》</p>
</blockquote>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">&nbsp;&nbsp;详细请到<a href="http://www.360doc.com/content/12/0331/06/9452699_199493153.shtml" target="_blank" data_ue_src="http://www.360doc.com/content/12/0331/06/9452699_199493153.shtml">C经典著作</a>书单察看介绍。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">正是我想要补的，之前学习C语言，只是泛泛地学习了一些语言特性，然后编写了若干行的代码,知道了怎么使用指针，数组，结构体，以及用它编写二叉树，线性表等数据结构，还有实现了一遍大部分排序算法。</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';">语言细节&nbsp;AND&nbsp;正确的程序</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">常常遇到这样的情况，程序写到一半，忘了这个代码的语言细节是什么的，例如++自增的使用，而这往往涉及到程序的正确性。有经验的程序员往往会发现i++和++i在很多情况下有很大不同，一时的麻痹或者粗心，都有可能造成重大的错误。记得之前有一个这样的故事：</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">美国宇航局发射航天飞机，但是因为一个程序员将“；”写成了“，”&nbsp;，最后造成了飞机失事。据说这是最昂贵的错误。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">代码是人编写的，难免会有错误，但是很多错误都是我们不清楚语言细节，或者某个语言的陷阱，从而失足跌倒。现实生活中很多代码都有错误，而黑客总是能够利用各种程序中的缺陷和漏洞，攻破我们的系统，拿走我们的数据和金钱。（我想起了《鹿鼎记》里面的，我们的财宝和女人，哈哈）。所以要写可靠的代码，必须要懂得一些常用的语言细节和规避陷阱的方法。</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';">具体的问题</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">我们编程的时候往往运行出结果就ok了，抛下程序去玩了。这是很不正确的学习方法，正确的学习方法应该深入理解程序在计算机程序在编译和运行时做了什么，故而多跟踪调试程序是有好处的。看看每一步都发生了什么，察看内存中的数据起了什么变化。</p>
<h4 style="font-family:'Times New Roman';">关于高级语言的内存管理</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"><a href="http://www.cnblogs.com/chenleiustc/archive/2011/04/08/2009994.html" target="_blank" data_ue_src="http://www.cnblogs.com/chenleiustc/archive/2011/04/08/2009994.html">这里</a>有一篇关于内存管理的很好的说明了哪些数据是存储在什么区的。学习过汇编语言的我们，很容易就想起来我们的程序包括一些段：数据段，代码段，堆栈段。那么在高级语言中，这些数据又是怎样存储的呢？如下：</p>
<blockquote style="background-color:#ccff99;border-top-left-radius:5px;border-top-right-radius:5px;border-bottom-right-radius:5px;border-bottom-left-radius:5px;font-family:'Times New Roman';"><p style="margin-top:0px;margin-bottom:0px;">栈stack：&nbsp;存放局部变量，栈表示的是一种后进先出，表达了我程序调用的顺序，故而栈里面存放的是我们的函数中的局部变量，包括变量，指针，参数等等。栈内数据是共享的，回收工作是由内存管理来做的。</p>
<p style="margin-top:0px;margin-bottom:0px;"></p>
<p style="margin-top:0px;margin-bottom:0px;">堆heap：&nbsp;说白了就是程序申请的内存区，这里一块，那里一块，堆是受到保护的，不能互相访问。而回收的时候，我们要收回指向他们的指针，然后GC（gabage&nbsp;collection）来处理。一般malloc，或者是new的对象都是存储在堆里面的。</p>
<p style="margin-top:0px;margin-bottom:0px;"></p>
<p style="margin-top:0px;margin-bottom:0px;">（全局）静态区：&nbsp;全局区和静态区是是在一起的。包括全局变量global修饰的变量，static修饰的变量。有的时候，尽管没有static修饰，也算是静态区的。例如&nbsp;char&nbsp;*p&nbsp;=&nbsp;"hello";&nbsp;&nbsp;字符串"hello"就属于静态区的，因为没有专门为它分配空间，若是char&nbsp;c_arr[]&nbsp;=&nbsp;"hello";&nbsp;则有为字符串分配内存，故而是在栈区。</p>
<p style="margin-top:0px;margin-bottom:0px;"></p>
<p style="margin-top:0px;margin-bottom:0px;">文字常量区：常量字符串就是放在这里的。例如cout&lt;&lt;&nbsp;"hello&nbsp;world"&lt;&lt;endl;&nbsp;那么字符串hello&nbsp;world就存放在常量区。</p>
<p style="margin-top:0px;margin-bottom:0px;"></p>
<p style="margin-top:0px;margin-bottom:0px;">程序代码区：存放程序的二进制代码。</p>
</blockquote>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">深刻理解程序和数据的存储，会更加明白如何编写节省资源和高效的程序，特别是分析由于存储问题带来的性能瓶颈问题，这在web和服务器编程上都很重要。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<h4 style="font-family:'Times New Roman';">关于C语言的sizeof</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">我做了以下实验，对指针进行了sizeof关键字操作，以及指针的加法操作。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<table border="0" cellpadding="0" cellspacing="0" class=" noBorderTable ke-zeroborder" style="clear:both;margin-bottom:10px;word-break:break-all;color:#000000;font-family:'Times New Roman';font-size:15px;line-height:19.5px;"><tbody><tr><td class="gutter" style="border:1px dashed #dddddd !important;"><div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
</td>
<td class="code" style="border:1px dashed #dddddd !important;"><div class="container"><div class="line number1 index0 alt2"><code class="cpp comments">//&nbsp;关于数组的sizeof运算</code></div>
<div class="line number2 index1 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp color1 bold">int</code>&nbsp;<code class="cpp plain">a[100]={0,1};</code></div>
<div class="line number3 index2 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(a));&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//&nbsp;打印的是数组的很多信息，</code></div>
<div class="line number4 index3 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(a[100]));&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//</code></div>
<div class="line number5 index4 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(&amp;a));&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//&nbsp;是a的地址</code></div>
<div class="line number6 index5 alt1"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(&amp;a[0]));&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//&nbsp;</code></div>
<div class="line number7 index6 alt2"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp plain">fun(a);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp comments">//&nbsp;作为参数传递的数组，其实是个指针</code></div>
</div>
</td>
</tr>
</tbody>
</table>
<span style="font-family:'Times New Roman';">fun的定义如下：</span><p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<div id="highlighter_826335" class="syntaxhighlighter cpp" highlighter="brush:cpp;toolbar:false;" style="font-family:'Times New Roman';"><table border="0" cellpadding="0" cellspacing="0" class=" noBorderTable ke-zeroborder" style="clear:both;margin-bottom:10px;word-break:break-all;"><tbody><tr><td class="gutter" style="border:1px dashed #dddddd !important;"><div class="line number1 index0 alt2" style="height:20px;">1</div>
<div class="line number2 index1 alt1" style="height:20px;">2</div>
<div class="line number3 index2 alt2" style="height:20px;">3</div>
<div class="line number4 index3 alt1" style="height:20px;">4</div>
</td>
<td class="code" style="border:1px dashed #dddddd !important;"><div class="container"><div class="line number1 index0 alt2" style="height:20px;"><code class="cpp keyword bold">void</code>&nbsp;<code class="cpp plain">fun(</code><code class="cpp color1 bold">int</code>&nbsp;<code class="cpp plain">b[100])</code></div>
<div class="line number2 index1 alt1" style="height:20px;"><code class="cpp plain">{</code></div>
<div class="line number3 index2 alt2" style="height:20px;"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(b));</code></div>
<div class="line number4 index3 alt1" style="height:20px;"><code class="cpp plain">}</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">我得到的结果是：</p>
<div id="highlighter_228111" class="syntaxhighlighter cpp" highlighter="brush:cpp;toolbar:false;" style="font-family:'Times New Roman';"><table border="0" cellpadding="0" cellspacing="0" class=" noBorderTable ke-zeroborder" style="clear:both;margin-bottom:10px;word-break:break-all;"><tbody><tr><td class="gutter" style="border:1px dashed #dddddd !important;"><div class="line number1 index0 alt2" style="height:20px;">1</div>
<div class="line number2 index1 alt1" style="height:20px;">2</div>
<div class="line number3 index2 alt2" style="height:20px;">3</div>
<div class="line number4 index3 alt1" style="height:20px;">4</div>
<div class="line number5 index4 alt2" style="height:20px;">5</div>
<div class="line number6 index5 alt1" style="height:20px;">6</div>
</td>
<td class="code" style="border:1px dashed #dddddd !important;"><div class="container"><div class="line number1 index0 alt2" style="height:20px;"><code class="cpp comments">//&nbsp;得到的结果是</code></div>
<div class="line number2 index1 alt1" style="height:20px;"><code class="cpp comments">//&nbsp;400 &nbsp;</code></div>
<div class="line number3 index2 alt2" style="height:20px;"><code class="cpp comments">//&nbsp;4</code></div>
<div class="line number4 index3 alt1" style="height:20px;"><code class="cpp comments">//&nbsp;4</code></div>
<div class="line number5 index4 alt2" style="height:20px;"><code class="cpp comments">//&nbsp;4</code></div>
<div class="line number6 index5 alt1" style="height:20px;"><code class="cpp comments">//&nbsp;4</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">要是想在子函数中得到数组的大小，那么使用下面的fun:</p>
<div id="highlighter_670844" class="syntaxhighlighter cpp" highlighter="brush:cpp;toolbar:false;" style="font-family:'Times New Roman';"><table border="0" cellpadding="0" cellspacing="0" class=" noBorderTable ke-zeroborder" style="clear:both;margin-bottom:10px;word-break:break-all;"><tbody><tr><td class="gutter" style="border:1px dashed #dddddd !important;"><div class="line number1 index0 alt2" style="height:20px;">1</div>
<div class="line number2 index1 alt1" style="height:20px;">2</div>
<div class="line number3 index2 alt2" style="height:20px;">3</div>
<div class="line number4 index3 alt1" style="height:20px;">4</div>
</td>
<td class="code" style="border:1px dashed #dddddd !important;"><div class="container"><div class="line number1 index0 alt2" style="height:20px;"><code class="cpp keyword bold">void</code>&nbsp;<code class="cpp plain">fun(</code><code class="cpp color1 bold">int</code>&nbsp;<code class="cpp plain">(*a)[100])</code></div>
<div class="line number2 index1 alt1" style="height:20px;"><code class="cpp plain">{</code></div>
<div class="line number3 index2 alt2" style="height:20px;"><code class="cpp spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="cpp functions bold">printf</code><code class="cpp plain">(</code><code class="cpp string">"%d\n"</code><code class="cpp plain">,</code><code class="cpp keyword bold">sizeof</code><code class="cpp plain">(*a));</code></div>
<div class="line number4 index3 alt1" style="height:20px;"><code class="cpp plain">}</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">调用的时候是</p>
<div id="highlighter_36073" class="syntaxhighlighter cpp" highlighter="brush:cpp;toolbar:false;" style="font-family:'Times New Roman';"><table border="0" cellpadding="0" cellspacing="0" class=" noBorderTable ke-zeroborder" style="clear:both;margin-bottom:10px;word-break:break-all;"><tbody><tr><td class="gutter" style="border:1px dashed #dddddd !important;"><div class="line number1 index0 alt2" style="height:20px;">1</div>
</td>
<td class="code" style="border:1px dashed #dddddd !important;"><div class="container"><p style="margin-top:0px;margin-bottom:0px;"><code class="cpp plain">fun(&amp;a);</code></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">故而能够得到预期的400。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<h4 style="font-family:'Times New Roman';">关于数据类型的溢出和转换</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">各种数据类型的转换，某些情况下系统是能够自动类型转换的，如赋值，表达式，循环条件判断中。遵循的是从低精度变到高精度的原则。而从高精度强制转换到低精度，则需要损失一部分的数据，所以应该斟酌为之，特别是不确定转换结果的情况下。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">只要弄明白了数据类型在计算机里面怎么存储，就能够明白什么样的转换是行的，什么样的转换是不行的。整形数据在内存中，存储的都是补码。对于负数，补码是反码+1，而对正数补码就是本身的码。例如char类型的（默认是unsigned）可以表示[0,255]&nbsp;,如果是signed，那么就可以表示[-128,127],也就是说分了一半去表示负数。int同理，一般的程序中，不会有太多的类型转换，因为这潜在着不安全因素，例如if里面的表达式就是一个很好的例子。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">对于bool型的，假如有个checked表示某个步骤是否通过检查，&nbsp;用if(checked)。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">对于int型，直接if(&nbsp;0&nbsp;==&nbsp;num)&nbsp;比较</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">对于浮点型，用&nbsp;if&nbsp;(&nbsp;0-EP&lt;num&nbsp;&amp;&amp;&nbsp;num&nbsp;&gt;&nbsp;0+EP)&nbsp;来确定是否和0相等</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">所以，我们要用同样类型的去比较，C中可以while(a),&nbsp;a是一个int型，Java就比较严格，不允许将int转换为bool类型做判断。</p>
<h4 style="font-family:'Times New Roman';">关于运算符的优先级<br />
</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">这个就要参考程序语言的手册了，我们自己写程序的时候，最保险的就是给各种表达式都加上括号，以避免意外的求值出现。同级的按结合顺序来判断。例如+，-，*，/&nbsp;,&nbsp;%是左结合；而对于！，=这样的，就属于右结合。有什么规律可循呢？所有的优先级中，只有三个优先级是从右至左结合的，它们是单目运算符、条件运算符、赋值运算符。其它的都是从左至右结合。当然，运算符是有级别的，级别高的先执行。具体请参考<a href="http://baike.baidu.com/view/1516130.htm" target="_blank" data_ue_src="http://baike.baidu.com/view/1516130.htm">百度百科C运算符</a>。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
<h4 style="font-family:'Times New Roman';">关于C语言的特别运算符号</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">自增++等，++的位置很重要，i++,表示用完i再自增1；而++i表示先做自增，然后再使用新的i值。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">自减--，同理。这两个很有技巧的运算符使用时要特别小心。有时候让i用完，自增1很有用，例如最寻常的for循环，以及排序里面，上次做一道题目，是插入排序，其中我就搞岔了++i和i++。看来还需要好好修炼哪~</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';">END</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';">by&nbsp;bibodeng&nbsp;2013-04-16&nbsp;21:45:44&nbsp;​</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';"></p>
</div>{% endraw %}
