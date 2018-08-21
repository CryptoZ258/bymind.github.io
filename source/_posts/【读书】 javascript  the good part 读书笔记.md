---
title: 【读书】 javascript  the good part 读书笔记
date: 2013-09-16 22:49:18
---
javascript: the good part 读书笔记
====

###对象的声明方式
var obj = {
    firstname : 'bibo',
    lastname: 'deng'
}

var obj = {
    "firstname": 'bibo',
    "lastname": 'deng'
}

访问的方式也有对应的两种，obj['firstname'], obj.firstname, 这其中涉及到关键字的问题，因为关键字是不能赤裸裸地作为变量或者对象的属性使用，好歹给个包装吧（“”）。且对象都是以引用的方式存在于程序中，也就是内存中只保留一份该对象。

###自省
hasOwnProperty() 判断是否有某个属性，与prototype链无关

typeof 关键字能够得到对象的类型名称字符串

###原型链

对于所有的继承者，都是可见的，这种灵活性，是那些extends所不具有的

###避免全局
封装起来，自成一体。这个可以在接下来的项目中使用。

###删除的穿透性
删除了对象当前的某属性，它会自动取其prototype的该属性的值作为新值？ write an example ,and ask for my teacher.

###函数
函数，由其上下文和代码决定。
四种调用方式：

* 方法式
* 函数式   new , 返回了函数这个object，也就是this
* 构造函数式
* func.apply(obj,array) / func.call(obj,args) 式（移花接木）

函数在内部获取参数：

arguments[i] 获得第i个参数，甚至不需要声明需要多少个参数，但是它不是一个数组

js对于参数是相当宽松的，多了不抱怨，少了也不嫌

给函数添加属性：

    Function.prototype.method = function (name, func) { 
        this.prototype[name] = func; 
        return this; 
    };

    Number.method('integer', function (  ) { 
        return Math[this < 0 ? 'ceiling' : 'floor'](this); 
        // 又见到了这个表达 floor(-2.3)是等于-3的
    }); 
    
必须使用prototype来进行扩展。

###作用域
C语言类似的可以保持block范围作用域，用花括号括起来的部分，除了这个范围，就不能使用了。javascript却不支持块作用域，却会覆盖外层作用域的声明，但是它支持函数作用域，也就是离开了当前函数，外面就不能访问函数内部定义的数据了。所以javascript中的应用，一般是要用到就先在最前面声明好。

###闭包

>A function literal can appear anywhere that an expression can appear. Functions can be defined inside of other functions. An inner function of course has access to its parameters and variables. An inner function also enjoys access to the parameters and variables of the functions it is nested within. *The function object created by a function literal contains a link to that outer context. This is called closure.*This is the source of enormous expressive power.

在其他一些语言，如C/C++中，函数里面不能再定义函数了，当然也没有很明显的函数式编程思想。有一次我用在我看来不可思议的方式来写一个setInterval：

    $(document).ready(function(){
        var t = setInterval( function(){
            // some other code here
            var i = 0;
            i ++;
            console.log(i);
            if (true)
            {
                clearInterval(t);
            }
        }, 100);
    });
    
审慎地判断一下，这属于闭包吗？ 里面用到的t的确是在上一层空间定义的,的确只运行了一次console.log()就停止了，去掉clearInterval之后，可以运行多次，但是i一直是1，那是因为每进入一次都是不同的环境了,这可能不是一个很好的例子。我问了一下我的导师，他说闭包是可运行的代码和其运行环境共同组成的，常见的表现形式就是函数包函数。我继续问，那么这个闭包内的生存期有多长，他回答应该是随着外部变量的消亡而灭亡。因为它带有对改上下文的引用，这样确保了函数作用域和信息的隐藏。

闭包的例子：

    var myObject = function (  ) { 
        var value = 0; 
     
        return { 
            increment: function (inc) { 
                value += typeof inc === 'number' ? inc : 1; 
            }, 
            getValue: function (  ) { 
                return value; 
            } 
        } 
    }(  );
    
能够起到隐藏的功能。定义的value,当myObject构造好了之后，依然可以通过myObject.getValue（）的方式来使用value。这令我感到很神奇。返回后的对象还能够使用原来函数的东西，好像嫁出去的女儿，可以回娘家一样（可以使用的东西有 参数，内部变量）。我实验了一下，去掉函数的立即执行，新建两个对象来进行比对，然后发现每一个新生成的obj对象，都具有不同的运行环境，也具有独立的value,这相当于是面向对象的一个替代封装，但是具有其本身的灵活性，并且可以将来可以使用prototype来进行扩展:
    
    $(document).ready(function(){
        var myObject = function (  ) { 
            		var value = 0; 
            	 
        		return { 
        			increment: function (inc) { 
        				value += typeof inc === 'number' ? inc : 1; 
        			}, 
        			getValue: function (  ) { 
        				return value; 
        			} 
        		} 
        	};
        	
        	var obj1 = myObject();
        	obj1.increment(1);
        	obj1.increment(1);
        	console.log(obj1.getValue()); // 2
        	var obj2 = myObject();
        	obj2.increment(1);
        	obj2.increment(1);
        	obj2.increment(1);
        	console.log(obj2.getValue()); // 3
    });

接下来我将读一点《jQuery源码剖析》来深入理解javascript的这种机制。

###异常
异常的检测及throw:

    var add = function (a, b) { 
        if (typeof a !== 'number' || typeof b !== 'number') { 
            throw {     // throw a exception object
                name: 'TypeError', 
                message: 'add needs numbers' 
            } 
        } 
        return a + b; 
    }
    
###数组
数组与对象不同，它无需字典那样定义索引，而是以自然数为索引，并且有length这个属性，以及其他有用的操作。它不会超界，而是会自动扩展到足够大以容纳最大界限。

typeof arr 得到的是“object“，故而需要进一步检查constructor === Array 才能判断arr确实是一个数组。数组人仍然是object。

###正则表达式
常见方法：

> * regexp.test(str)
  * regexp.exec(str)        // 匹配结果从1开始
  * string.match(regexp)
  * string.replace(regexp)
  * string.search(regexp)
  * string.split(regexp)
  

这个是书上的例子：

    var parse_url = /^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/; 

实在是有点长，之前有点regexp基础，所以能够看懂一些，但是对于表达式中的`?:`需要解释一下，它是non-capture-group标志，也就是这个括号看起来像个分组，但是在exec匹配的结果中不要显示它，例如匹配协议名的`(?:([A-Za-z]+):)` 虽然匹配了后面的冒号，但是结果中并不包含，如果是http:匹配了只得到http，这样就避免了得到不想要的分组。

控制字符：
> \ / [ ] ( ) { } ? + * | . ^ $

尾部标识：
> * g       —— 全局匹配
  * i       —— 大小写通吃
  * m       —— 多行 $可匹配行尾
  
转义：
 
> * \d \b \s \w 匹配相应文法 数字 单字 空白字符 字符0-9a-zA-Z
  * \D \B \S \W 上面对应集合的非\D = [^\d] 
  * \u00FF 双字节字符
  * \1 表示前面匹配到的第一分组`（）`只对capturing-group生效
  
[]定义的字符类内的转义与上面的有点不一样，`\b`变成了退格符号，就不能在用来表示字了，相应的`\B`就没有了。

计数:
> * {m,n} 匹配m到n次
  * {m} 相当于{m,m}
  * \* 匹配任意次
  * \+ 匹配至少一次
  * ？ 匹配或者不匹配，它就在那里
  
###内置方法

* array

    - array.concat（elem1, elem2, ...） 追加 数组追加数组，会合并，而不是直接加入数组 
    - array.join(separator) 用数组元素组成一个用separator分隔开的字符串 ['I', 'am', 'bibo'] => "I am bibo"
    - array.push(elem) 这才是真正的追加，单个被加入，数组也被视为单个对象
    - array.pop() 获取最后一个元素
    - array.reverse() 翻转元素顺序
    - array.shift() 返回并删除第一个元素
    - array.slice(start, end) 截取数组片段
    - array.sort(compareFunc) 排序,传入一个比较函数，默认按字符序
    > compareFunc 讲得很清楚，传入两个参数，相等返回0, 第一个参数在前，返回负数，第二个参数在前，返回一个正数，例如最经典的是比较整数return a-b 从小到大排列
    
    - array.splice(start, deleteCount, item...) 删除若干，并从删除位置添加
    - array.unshift(item,...) 从前面加
  
* string

    - str.entityify 特殊字符html编码化 '&' => '&amp';
    - str.charAt(pos) 返回pos位置上的字符
    - str.charCodeAt(pos) 返回字符ASCII码
    - str.concat(str1, str2...) 链接字符串
    - str.indexOf(str1, pos) 查找某个字符串，pos起始位置可选，-1没找到，这个函数很常见 
    - str.lastIndexOf(str1, pos) 从后开始查找
    - str.localeCompare(str1) 比较字符，str < str1 则返回负数，比较规则字母序
    - str.match(regexp) 做匹配，结果与regexp.exec(str)一样,如果有g则返回一组匹配值，但是不会返回分组
    - str.replace(val-old, val-new) 替换字符内的字符，就像编辑器的替换一样，可以使用全局的regexp,这样可以替换所有匹配的值， val-new中$有特殊含义
    
    >- $$	     :  $
    - $& 	 :   The matched text
    - $number:	Capture group text
    - $`	     :  The text preceding the match
    - $'	     : The text following the match
    
    - str.search(regexp) 查找第一个匹配位置
    - str.slice(pos1, pos2) 截取字符串,第一个参数为负，会自动加一次str.length,超过str.length则会当作0看待
    - str.split(separator, limit) 分片字符串，limit为分片数限制
    - str.substring(begin, end) 求子串,没有slice那么强大
    - str.toLocaleLowerCase()   带本地化的字母小写化
    - str.toLocaleUpperCase()
    - str.toLowerCase()         字母小写化
    - str.toUpperCase()
    - String.fromCharCode(code1,...) 从数码转成字符串
        
* number

    - number.toExponential(小数位数)  返回一个科学计数的字符串
    - number.toFixed(小数位数) 返回一个定点表示的实数字符串
    - number.toPrecision(实数长度) 返回一个实数字符串
    - number.toString(进制)
    
* object
    
    - hasOwnProperty(pname) 是否具有某属性，不追溯到prototype
    
* regExp

    - exp.exec(string) 对字符进行匹配，返回数组，0是整个匹配值，后面的按分组返回结果
    > 如果exp带有g标志，也就是全局标志，则是从exp.lastIndex开始匹配的,匹配成功则                lastIndex为匹配段后的第一个字符位置，也就是说有一个记录功能，可以接着从这个位置匹配，这就可以在一个exp上循环地开始匹配了。如果匹配不成功则lastIndex为0。
    - exp.test(string) 匹配返回true,否则返回false
    
###style

命名，表达式，块，都有一些规则可以使得更加优雅并且能避免错误。尽量做到逻辑明晰，自我阐述。

Sometimes I think about comments as a time machine that I use to send important messages to future me. 这句话讲得好贴切啊。

javascript 没有块作用域，也就是说块内的东西不算是块私有的，而C块内声明的变量只能在块内使用，这样尽量延后声明时间可以具有更合适的作用域，但是javascript不是这样，故而经常可以看到一些高手是在函数开头就把所有变量声明好。

    if (true)
    {
        	var sum = 0;
        	for (var i=0; i<10; i++)
        	{
        		var name = 'aa';
        		sum += i;
        	}
        	console.log(sum, name);
        	//输出 45 "aa"
    }
    
    
    if (my_value && typeof my_value === 'object') { 
        // my_value is an object or an array! 
    }
    因为typeof null是 object, 但是可以用 my_value是否为假来加以判断
    
    不要依赖js自动帮你加分号
    
    减少全局变量的使用，它会搞乱变量的关系，我自己在开发中也遇到这样的问题
    
    parseInt("08", 10) 应该提供第二个参数指定进制  
    
    NaN 是一个number,不等于任何数，包括它自身的number，这是有多纠结呢，用isNaN（NaN）来判断  
    
    isFinite() 接受所有不是NaN, Infinity的数字
    
    if (my_value && typeof my_value === 'object' && 
        my_value.constructor === Array) { 
        // 判断是否是数组
    }
    
蛋疼的类型判断(typeof)：
    
    Value	  |    Type
    --------------------
    0	      |    Number
    NaN	      |   (not a number)	Number
    ''	      |   (empty string)	String
    false	  |    Boolean
    null      |    Object
    undefined |	   Undefined
    
使用=== 和 ！== 类型要相同才能比较

>The worst features of a language aren't the features that are obviously dangerous or useless. Those are easily avoided. The worst features are the attractive nuisances, the features that are both useful and dangerous.

    (function (  ) { 
        var hidden_variable; 
     
        // This function can have some impact on 
        // the environment, but introduces no new 
        // global variables. 
    })(  );
    // 这样写可以避免新建一个function全局对象
    
使用[JSLint]( http://www.JSLint.com/.)来提高代码质量,使自己变成一个更好的程序员。

eval is evil ,当然我们有时候会发现在服务器返回的是字符串格式的JSON的时候，eval(json)将会非常有用。但是书中说这涉及安全问题，应该对JSON进行parse,也就是写一个解析器解析一遍。代码有点复杂，下次单独分离出来进行分析。

读完这本书，我才对javascript有更清晰的认识，一开始接触js的时候，觉得它很奇怪，虽然语法和C很相似，但是其用法，尤其是函数式编程，还有prototype,闭包很难理解。现在终于有种拨开迷雾见天日的感觉。本书还教导我们怎样避免一些容易犯错的地方，来使自己成为一个更好的js程序员。

by bibodeng 2013-09-16