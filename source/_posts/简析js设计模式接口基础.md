---
title: 简析js设计模式接口基础
date: 2013-12-02 19:56:41
---
简析js设计模式接口基础
===
by bibodeng 2013-12-02

想起要对js设计模式中一些基础的代码做一个简单分析，让自己印象更加深刻。例如接口，继承，闭包等等，方便以后要的时候直接拿来。

## 接口

接口，学过Java的同学肯定知道，声明一个接口，里面有若干方法，而一个类负责实现（`implements`）它，语言本身的机制会强制该类必须实现接口中声明的所有方法，否则就会报错。实现接口的目的是为了提供一组通用的叫法，让不同的对象实现它。很常见的就是在组合模式中，父元素和子元素都实现了相同的接口，从而可以很直接地将请求从任意一层传递下去。总之，接口能够提供一个通用的方法库，也要保证各类都有实现所有方法。接口在js中的实现方法有三种： 

* 注释法 （就是用注释来说明）
* 属性检查法
* duck type(会呱呱叫的都是鸭子)

## 属性检查法

注释法就不详细看了，因为它就是用注释声明一些接口，而不做任何检查，完全靠人工检查是否实现了相应的方法。而属性检查法，相对来讲严格一点，它将一组接口的名字都放入一个数组中。

    // 这是后面组合模式表单的一个例子
    var ClassA = function(){
        // 声称自己有一组接口
        this.interfaces = ['Composite', 'FormItem'];
    }
    
为了检查是否实现了相应的接口，就检查该类的实例是否具有某个接口，这个某个接口是作为字符串传入需要检查的接口名。

    // 模仿implements
    function implements(obj){
        // 对传入的参数（接口名进行检查）
        for (var i=1; i < arguments.length; i++)
        {
            var interfaceName = arguments[i];
            var interfaceFound = false;
            // 检查声称的接口 比对两个数组需要两个循环
            for (var j=0; j<obj.interfaces.length; j++){
                if (obj.interfaces[j] == interfaceName){
                    interfaceFound = true;  // 接口j找到了
                    break;
                }
            }
            // 只要有一个接口没有实现
            if(!interfaceFound){
                throw {
                    name: 'interface error',
                    msg: 'some interfaces not found in obj'
                }
                return false;
            }
        }
        return true;    // 全部通过检查
    }
    
    // 调用方法
    if (!implements(obj, 'Composite', 'FormItem')){
        ...
    }
    
这次只是把这些接口名都放到一个数组中，但是还是没有确保在`ClassA`中实现接口中的方法（还是以注释的方式说明）。在实践中看起来也没啥用处。我们需要的是真正能够检查对象的方法，我们瞬间想到了`for (var index in obj)` 对每个方法进行检查。而我们的接口，也应该放在一个像这样的对象中，它能够维护接口的名字和各种方法名。

    {
        interfaceName: 'Composite',
        methods: ['add', 'remove', 'getChild']
    }
    
初步的思想是有了，但是实现要灵活，能够生成一个如上的对象。`duck typing`就是这样做的：

## 鸭式辨形

会呱呱叫的两只脚走路的会游泳的就是鸭子。我们生活中常常是一个经验主义者，通过这样的方法来判断事物。所有，理解起来也不是很难：

    // 接口对象
    var Composite = new Interface('Composite', ['add', 'remove', 'getChild']);
    
    // 要得到上面的对象，我们写一个构造函数专门用来新建接口对象
    function Interface(interfaceName, methods){
        this.interfaceName = interfaceName;
        this.methods = methods;
        // new操作将返回this
    }
    
    // 如果要严密一点，就需要检查参数的个数和类型
 
这次就不用注释了，而且代码很明了。声明了一个接口对象Composite,它的名字叫做`Composite`,具有`add`，`remove`，`getChild`三个方法。那么如何声明实现了该接口，并且用什么来确保对象实现了我们接口声明的方法呢？

这次都不用声明实现了该接口，只要实现了相应的方法就是实现了该接口。所以不用显式地声明`implements`了什么。而是在某个方法之前用`ensureImplements`来检查。至于设计成`Interface`的内置方法，还是普通函数，都是可以的。

    // obj, interf1, interf2
    Interface.ensureImplements = function(obj){
        if (arguments.length < 2){
            throw new Error("arguments require for at least 2");
        }
        
        // 依次检查 这次的参数是interface实例，不再是字符串
        // 而一个字符串数组也变成了真正的对象的属性
        for (var i=1; i<arguments.length; i++){
            var interface = arguments[i];
            // 严格的类型检查
            if (interface.constructor !== Interface){
                throw new Error("argument " + i + " is not the instance of Interface Class");
            }
            
            for (var j=0; j<interface.methods.length; j++){
                var method = interface.methods[j];
                if (!obj[method] || typeof obj[method] !== 'function'){
                    throw new Error("ensureImplements error: method" + interface.methods[j] +
                        ' in interface '+ interface.interfaceName + ' was not found.');
                }
            }
        }
    }
    
    // 调用示例
    function foo(formObj){
        // 不满足条件回报错
        Interface.ensureImplements(formObj, Composite, FormItem);
        
        // 使用接口中的方法
        formObj.remove();
        ...
    }

主要就是实现一个`Interface`类，供生成实例，也提供一个`ensureImplement`方法。只要引入了这个类，就可以使用new一个Interface，然后检查的方式严格要求类实现了接口中的方法。但是我总觉得少了一步，就是声明一下某个类实现了某个接口。当然也可以用数组将所实现的接口都存一个对应的应用，如`{'Composite': Composite}`。但是这样看起来就不像是鸭式辨型了。

---
end