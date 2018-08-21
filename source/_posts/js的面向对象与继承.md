---
title: js的面向对象与继承
date: 2013-05-12 21:20:50
---
{% raw %}
<link type="text/css" rel="stylesheet" href="/content/plugins/bibo_mark/article_bibo.css"> <div class="art_content">
    <h3>
        基础
    </h3>
    <p>
        js包含三部分：1，ECMAScript语法 2，DOM  3,BOM. 应该说ECMAScript这种东西，语法和许多概念都是源于那些高级语言（C/C++， Java），单就面向对象和继承来说，js又属于比较特殊的，它的类是一个构造函数，函数又属于一种对象，而它又不支持直接的继承，故而就需要使用prototype或者是冒充对象来实现继承和多态。有人说js是属于一种基于对象的，而不是面向对象，因为面向对象要有三要素： 1， 封装  2，继承 3，多态。 而js的多态是通过给不同的对象添加不同的属性而实现的。其实本质上还是用子类的方法覆盖父类的方法。<br />
    </p>
    <h3>
        js的面向对象与继承<br />
    </h3>
    <h4>
        js的面向对象
    </h4>
    <p>
        js的类是用函数包裹的，里面定义了属性和方法，也就是闭包，google一下什么是闭包：<br />
    </p>
    <p>
        <br />
    </p>
    <blockquote>
        <p>
            在<a href="http://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6" title="计算机科学">计算机科学</a>中，<strong>闭包</strong>（<em>Closure</em>）是<strong>词法闭包</strong>（<em>Lexical Closure</em>）的简称，是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。<br />
        </p>
  
    </blockquote>
    <p>
        <br />
    </p>
    <p>
          也就是说数据与函数建立了联系并共同组成一个实体，且运行离开该函数后，这些数据依然存在。coolshell有一篇文章专门介绍 <a href="http://coolshell.cn/articles/6731.html">javascript的闭包</a>。那么看看代码是怎么写的吧：
    </p>
    <p>
        <strong>典型的工厂模式:</strong><br />
    </p>
    <pre class="brush:js;toolbar:false;">        function sayName(){
        alert("hi, I am "+ this.name);
    }
    // 工厂模式
    function createUser(name,age){
        var user = new Object;
        // 进行装配
        user.name = name;
        user.age = age;
        user.sayName = sayName;
        return user;
    }
                                                                                                                                                               
    var bibo = createUser("bibo", 20);
    bibo.sayName();
    </pre>     <p>
        整个过程就是新建一个对象，然后动态地为对象添加各种属性方法，就连方法也可以预先定义好，到时候予以赋值。这就很像工厂里面进行装配，装配完就返回——出厂，于是也叫“工厂模式”。
    </p>
    <p>
        <br />
    </p>
    <p>
        <strong>构造函数方式：</strong>     </p>
    <p>
        就是在一个函数内将所有东西都生产出来，而不是从外面拿。故而函数什么的要在里面定义，这就形成了一个很奇特的现象——函数里面包函数。一般C++里面不会出现这样的东西，但是我们要有一种观念，对象既然是构造函数造出来的，那么这个类和造这个类的函数就可以划等号了。而C++的方式叫做“对象模板”会相当贴切。
    </p>
    <pre class="brush:js;toolbar:false;">        // class User
    function User(name, age){
        this.name = name;
        this.age = age;
        // 定义方法
        this.sayName = function(){
            alert("hi, I am "+ this.name);
        }
    }
                                                                                                                               
    var bibo = new User("bibo", 20);
    bibo.sayName();
    </pre>     <p>
        有几个比较明显不同的地方，如在构造函数内使用this引用，指代该对象。然后在新建的时候用了new操作符，相比工厂模式的new Object，显得更加精简了一些。其他方面大体相同，这有点像妈妈怀孕一样，在“肚子”里把你整个给形成了（今天恰好是母亲节~）。
    </p>
    <p style="text-align:center;">
        <img src="http://www.wiz.cn/unzip/3eb90c0e-f584-11e0-a072-00237def97cc/52df8f2c-467c-dd36-1f1d-dd22808fd577.7517/index_files/83b468b13bb97e8744a7baa7eafb322d.png" /><br />
    </p>
    <p style="text-align:left;">
        <strong>原型方式：</strong>     </p>
    <p style="text-align:left;">
        原型方式是使用prototype来定义类所包含的属性和方法，它使用的是一个空构造函数，然后把整个构造函数的过程实现，使得它能够造出一个对象。用代码说话吧，因为暂时找不到恰当的隐喻来说明:<strong><br />
        </strong>     </p>
    <pre class="brush:js;toolbar:false;">        function User(){
    }
                                                                                                           
    User.prototype.name = "bibo";
    User.prototype.age = 20;
    User.prototype.sayName = function(){
        alert("hi, I am "+ this.name);
    }
                                                                                                           
    var bibo = new User();
    bibo.sayName();
    </pre>     <p style="text-align:left;">
        可以发现，这在写好构造函数后，依然可以修改构造函数实现的方法，故而能够达到定制的目的。js的多态是使用这个实现的，因为prototype只有一个，新的会覆盖旧的。
    </p>
    <p style="text-align:left;">
        <br />
    </p>
    <p style="text-align:left;">
        以上三种很自由的对象构造方法，各有优缺点，可以混合使用，因此会非常灵活。<span style="line-height:1.3em;">另外很可能会引出如动态原型方法（动态检测是否含有原型方法，否则添加</span><span style="line-height:1.3em;">）等更加复杂的方式，其实都是这三种演变而来。</span>     </p>
    <h4>
        js的继承
    </h4>
    <p>
        js的继承可以使用假冒对象和原型继承的方式（一个类的原型是另外一个类）
    </p>
    <p>
        对象冒充：
    </p>
    <pre class="brush:js;toolbar:false;">        // class A
    function User(name, age){
        this.name = name;
        this.age = age;
        // 定义方法
        this.sayName = function(){
            alert("hi, I am "+ this.name);
        }
    }
                                                                        
    // class B
    function VIP_User(name, age, money){
        this.newMethod = User;      // 拷贝一份构造函数
        this.newMethod(name, age);  // 用构造函数运行
        delete this.newMethod;
        // 继承完毕
                                                                            
        // 新的属性/方法
        this.money = money;
        this.pay = function(){
            alert("pay");
        }
                                                                            
    }
                                                                        
    var bibo = new VIP_User("bibo", 20, 10000);
    bibo.sayName();     // 继承的
    bibo.pay();         // 自己的
    </pre>     <p>
        核心部分就在13-15行，咋一看，是拷贝一份构造函数，然后运行该方法，然后删除该方法，玄妙就在于14行，在该函数内运行了一遍class A的构造函数后，class 产生的对象中就带有了A的血液。因为等于把代码贴过来，运行一遍。
    </p>
    <p>
        <br />
    </p>
    <p>
        还有一种使用call和apply来运行父类的构造函数的方法，但是要传入一个this对象。是这样写的，把核心的13-15行换成：
    </p>
    <pre class="brush:js;toolbar:false;">        User.call(this, name, age);
    </pre>     <p>
        下面讨论另外一种不同的方式
    </p>
    <p>
        原型链继承：
    </p>
    <pre class="brush:js;toolbar:false;">        // Class A
    function User(){
    }
                                              
    User.prototype.name = "bibo";
    User.prototype.age = 20;
    User.prototype.sayName = function(){
        alert("hi, I am "+ this.name);
    }
    // Class B
    function VIP_User(){
    }
                                              
    VIP_User.prototype = new User(); // 用A的实例来作为B的原型
    VIP_User.prototype.pay = function(){
        alert("pay");
    }
                                              
    var bibo = new VIP_User();
    bibo.sayName();
    bibo.pay();
    </pre>     <p>
        继承的在前，然后添加子类的新的方法或属性。VIP_User以User的实例为原型，然后才予以扩展的。
    </p>
    <p>
        <br />
    </p>
    <p>
        以上两种继承的方法也可以混合使用，只要理解了这两种继承的思想，就不难在复杂的继承中混合使用这两种方法。
    </p>
    <p>
        <br />
    </p>
    <h3>
        小结
    </h3>
    <p>
        刚刚接触js，就面向对象这两件东西比较难理解，其他语法很多都和C++相似，又和动态脚本语言如python有点相似。有函数式编程的味道。以上观点如有不正确，欢迎评论指正。
    </p>
    <h3>
        END
    </h3>
    <p>
        by bibodeng   2013-05-12
    </p>
    <p>
        <br />
    </p>
    <p>
        <br />
    </p>
</div>{% endraw %}
