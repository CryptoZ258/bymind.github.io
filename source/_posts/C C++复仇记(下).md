---
title: C C++复仇记(下)
date: 2013-04-20 16:45:42
---
{% raw %}
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';letter-spacing:1px;line-height:19.5px;"><br class="Apple-interchange-newline" />
看好书</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">​自从上次写了《C/C++复仇记(下)》以来，我继续看《C语言深度剖析》，理解了几个之前不懂的知识点，例如指针数组，数组指针，函数指针（平时从来不用）等。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">我甚至觉得C语言是一门很难的语言，之前认为容易，是因为只接触了容易的部分，当然这是相对而言的（python，java等高级语言都没有指针啥的，而且内存管理也轻松很多）。但是C作为我们大学里面学习的第一门语言，也是面试，笔试，考试，竞赛等等最常用到的语言，没有理由不好好学习之。而学习它，更多的是语言实现细节，不仅仅是语法细节，而实现细节在语言上的反映就是编译器的做法，比如函数，比如一个malloc函数，理解了它的实现，就可以知道为什么申请后要进行转化成特定类型的指针（因为用到了void*指针类型）等等，这些都需要深入理解，甚至是动手调试。</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';letter-spacing:1px;line-height:19.5px;">C的指针和数组</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">指针与数组的区别</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">书里面讲的很明白，数组和指针是完全不同的东西，相互之间也没有什么关联。只是它们的某些操作方法很相似，所以常常令我们迷惑。指针是一个地址，指向的是内存中的一块内存，它的类型只是表示它怎么解读内存里面的内容。如int *p = &amp;a[0]; 使得p指向数组的首元素的首地址，然后*(p+1)则表示下一个int型，是跨越了4个字节的（32位机）。当然也可以用下标的方式来访问： p[1]，其等价于 *（p+1），这就是迷惑我们的地方，因为数组也可以这样来访问。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;"></p>
<h4 style="font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">几个要说明的问题</h4>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">对指针进行加&nbsp;1&nbsp;操作,得到的是下一个元素的地址，而不是直接下一个字节的地址。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">假设有 int a[10] = {0};</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">数组名a作为右值：</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">int (*p)[10]&nbsp;= &amp;a; &nbsp; // 将整个数组的首地址赋予数组指针， +1解读为跳10个int类型大小。指针是按照类型来确定下一个元素的位置的。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">当 int *p = &amp;a;&nbsp;&nbsp; &nbsp; // 编译器将会警告，说类型转换，把数组地址赋给了int* p</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">当a作为右值时，和&amp;a[0]是一样的。也就是说可以这样用：</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">int x = *(a+1); &nbsp; &nbsp; &nbsp;// 表示数组的第二个元素赋值给x</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">区别指针数组和数组的指针：</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">A),int&nbsp;*p1[10];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// 指针数组 int* p1[10] &nbsp;，[]的优先级比*高。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">B),int&nbsp;(*p2)[10];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; // 数组指针 int (*)[10] &nbsp;p2, 指向10个元素数组的一个指针</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">理解指针和数组，最重要的是理解，指针是一个地址，指向一片内存，怎么解读内存关键在于起始地址和指针类型。而数组则是作为一个整体存在的，可以访问数组内的单个元素，但是其本身可以作为一种类型，可以有指向这种类型的指针。</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';letter-spacing:1px;line-height:19.5px;">一种意识</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">学习一种语言，到了一定的程度，应该养成了察觉错误的意识。错过一次后，找到犯错误的原因，也就不会错了。而往往我们犯错误，是因为我们的认知没有到位，没有搞清各个元素之间的关系。我们学习一样技能，总是克服原有的思维方法，重新确定其表达方式，归根结底都是一种映射，但是这种映射和我们潜意识中的内容可能有偏差，而阅读更多的知识，做更多的练习是减少这种偏差的唯一方法。加油！</p>
<h3 style="background-color:#000000;color:#ffffff;padding:10px;font-family:'Times New Roman';letter-spacing:1px;line-height:19.5px;">END</h3>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:15px;letter-spacing:1px;line-height:19.5px;">by bibodeng&nbsp;2013-04-20&nbsp;16:44:12</p>{% endraw %}
