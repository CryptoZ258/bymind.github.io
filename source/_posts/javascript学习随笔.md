---
title: javascript学习随笔
date: 2012-09-15 23:43:27
---
{% raw %}
<div><h3>疯狂读书，疯狂编程</h3>
</div>
<div>&nbsp;</div>
<div>大三了，该抽出点时间来疯狂读书，疯狂学习一些技能了，当然也不能太过操之心切，将春天的期望，夏天的燥热都混杂在一起，想去追求秋天的收获。这几天想要正儿八经地学习一下javascript，这样就可以看懂别人写的代码，同时也可以自己开发web应用。其实我还是挺享受学习基础的时间，而不是为了掌握某项技能而想着去开发应用，学习的事情，心急不了，好好读几本书吧。</div>
<div>&nbsp;</div>
<div><h3>从C++到javascript</h3>
</div>
<div>&nbsp;</div>
<div>一个C++的程序员转到学习javascript语言，会感到javascript很简单很灵活，但是有些东西又需要特别小心区别。因为javascript作为一门脚本语言，有许多C++所不具有的特性，比如说函数式编程，自动垃圾回收等，这就使得一些javascript的编写代码的方法会有很大不同，但是同是高级的面向对象的语言，还是可以从中得出一些相通的思想。所以，没有学过javascript的人看到js的代码可能很大一部分都能认识，比如 
var a = 0;&nbsp; if(a == b)&nbsp;... else 
...毕竟编程语言都是这些语法，不同的是一些特殊的机制以及库的功能。当然也会碰到一些不懂的代码，例如：</div>
<div>&nbsp;</div>
<div>Array.prototype.hello = function() {</div>
<div>alert("hello world");</div>
<div>}<div>var a = new Array(1,2,3);</div>
<div>a.hello();</div>
</div>
<div>&nbsp;</div>
<div>alert("hello world");是弹出窗口提示hello 
world，这没有什么稀奇的，稀奇的是javascript的内置对象Array的原型方法hello。 这样就可以为所有的Array 
实例都可以调用hello原型方法了。这和C++是不同的，C++的继承是必须要一代代继承下来的，而javascript可以为对象的原型提供我们编写的一些方法，这样可以极大地扩展我们使用javascript内置对象的方便程度。</div>
<div>&nbsp;</div>
<div>还有那传说中的函数式编程，早在大一的时候就听说过了《冒号课题》介绍的函数式编程，所以学的时候也有了一点心理准备。那就是函数也是数据。的确的，存储在计算机里面的所有符号的集合都可以看做是数据，之前C/C++的观念认为数据归数据，函数归函数（属性归属性，方法归方法）。而在javascript中，函数也可以参与运算了，可以作为参数直接传入，也可以作为构造函数来创建对象，也可以在函数内封装函数（即闭包）。所以，很经常就可以看到如下的代码:</div>
<div>&nbsp;</div>
<div>function f (x,y) {</div>
<div>&nbsp;</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;function e(a,b){</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return a+b;</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;}</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;return e(1,2) + x + y;</div>
<div>}</div>
<div>&nbsp;</div>
<div>alert(f(3,6));</div>
<div>&nbsp;</div>
<div>虽然说用法上和C++有很大不同，但是根本上都是一些能够对数据进行操作的代码。只不过这些javascript的函数可以操作它本身类型的数据（也就是函数）。</div>
<div>&nbsp;</div>
<div>javascript的灵活性以及其带来的混乱性</div>
<div>&nbsp;</div>
<div>javascript作为web浏览器的脚本语言，具有很高的灵活性，比如声明函数的方法就有很多种，如 
function关键字静态声明法，Function内置对象实例化法，以及直接function直接量。所以我们可以看到三种不同的方法：</div>
<div>&nbsp;</div>
<div>function foo(){</div>
<div>&nbsp;alert("hello javascript");</div>
<div>}</div>
<div>&nbsp;</div>
<div>或者</div>
<div>&nbsp;</div>
<div>var foo = new Function("alert(hello)");</div>
<div>&nbsp;</div>
<div>或者</div>
<div>var foo = function(){</div>
<div>alert("hello world");</div>
<div>}</div>
<div>&nbsp;</div>
<div>而且这三种方法之间有很多细小的差别，比如内部的作用域，由于new 
Function();方法是动态生成的函数数据引用类型，故而等于是一个变量，具有顶级作用域，可以操纵上下文的数据。而静态声明的函数，只能操纵函数内部的数据，这样就使得其他两种只有函数作用域。</div>
<div>&nbsp;</div>
<div>再比如javascript的array有很多很灵活的方法，例如声明 var a = [1,2]; 或者var a = new Array(); 
都可以，而且其长度很自由，可以随意地在某个位置插入一个值，或者删除一个值。随意修改数组的长度，或者将其反转，排序，定制排序等。d但是这种灵活性是有代价的，那就是我们程序员经常会被各种情况搞晕，函数什么时候有什么样的作用域，或者有没有闭包，有没有嵌套执行。数组的排序到底是应该返回1还是返回-1，以及Function.prototype 
== 
object.prototype&nbsp;到底是谁构造了谁，谁继承于谁,混乱不堪。真心觉得这些关系很复杂，而javascript一开始的实现也是bug百出，可能设计它的人为它的灵活性丰富性付出了很大的代价吧。javascript完全没有C那么纯粹，容易接受。但是用起来，谁都很容易包含一个jquery的库，然后写出一个事件绑定语句 
$("header").click(function(){/*...*/})。或者用正则表达式来检验表单。但是真正要深入javascript的细节，其复杂程度还是够我受的了。当然javascript有它独特的方法，而这些方法也十分地强大，强大到我必须重新思考一下程序是什么这样的“哲学问题”了。</div>
<div>&nbsp;</div>
<div>接触了函数式编程，以及js中很多动态的特性，让我感觉到，程序是可变的，同时程序代码本身也是一种数据，数据可以由它而生，也可以寄生在它里面。而函数其实也就是一个对象，对象可以被动态地执行，故而程序也就灵活了。</div>
<div>&nbsp;</div>
<div><h3>一门语言与它的库</h3>
</div>
<div>&nbsp;</div>
<div>一门语言，要变得强大，它必须要有强大的库，语言的库极大地丰富和方便了我们的编程方法，例如js的jquery和jqtouch库，使得开发html5的移动应用变得很方便，C++也有强大的STL以及boost等库支持，使得我们写程序方便了很多。库就是语言的延伸，使语言的触角探出到纯粹语法之外的更加复杂的功能。当今web开发有很多开源的代码，可供借鉴参考，而我还是决定从头学起，老老实实地把握好基础，然后再去想框架、开发的事情。当年明月写《明朝那些事》之前，每天都读古籍，技术也是一样，只有真正积累了，才能发出来。</div>
<div>&nbsp;</div>
<div>by bibodeng&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2012-09-15</div>
<style type="text/css">
h3{
background-color: black;
font-size: 18px;
color: white;
padding: 10px;
}
</style>{% endraw %}
