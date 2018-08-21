---
title: js设计模式基础——继承
date: 2013-12-04 23:59:39
---
js设计模式基础——继承
===

by bibodeng 2013-12-04

## js中的继承

js中的继承分为几种：

* 类式继承 （构造函数的prototype链扩展） extend
* 原型式继承 （从对象的角度） clone
* 掺元类 （混合多个类）

## 类式继承

使用原型链的方式，让构造函数的原型指向另外一个对象（注意是对象）。我们平常做的比较多的，就是创建一个新类，然用用prototype扩展这个类，然后生成的类的对象实例则具备了原型链对象中的方法和属性了。

让一个类继承另外一个类的四部曲：

* 设置原型对象
* 恢复构造函数
* 执行构造函数（构造函数也执行父类构造函数）
* 生成新对象

然而在new的过程中，将会调用自身的构造函数，让一个类继承另外一个类，就需要它调用一次父类的构造函数，从而在this中声明各种属性。并且把构造函数设置回自己的构造函数（因为会覆盖掉）。现在为了实现两个类之间的继承，实现一个模拟继承：

    function extend(subClass, superClass){
        var F = function() {};
        F.prototype = superClass.prototype; // 这句挺巧妙
        subClass.prototype = new F();   // 相当于调用过了superClass的构造函数，并且将F的对象实例赋给了subClass的prototype对象
        subClass.prototype.constructor = subClass; // 恢复构造函数
    }
    
## 原型式继承

从原有对象的基础上进行修改变换。类的基础是一个对象:

    var Person = {
        name: 'ren',
        talk: function(){
            console.log("hi, my name is "+this.name);
        }
    }
    
    // 克隆方法，将obj放到新对象的原型链中
    function clone(obj){
        function F(){};
        F.prototype = obj;
        return new F;
    }
    
    // 原型继承
    newObj = clone(Person);

在clone之后，对于从原型继承而来的属性，直接更改的话会改变原型对象中的数据，会对别的子类产生影响，而如果给一个属性赋值的方式，如obj.name = "bibo" 将会新建一个新对象自己的属性。所以，要改变某个属性之前，先为它创建新的副本，而不是让它默认使用原型的值，这也能够解决上面所谓的**读写不对称** ，这多少和我们之前的继承认识有所不同。不过可以使用hasOwnProperty来区分是实际成员还是继承的成员，因为hasOwnProperty是不把原型链中的属性或方法算在内的。

## 多类继承（混合两个类）

使用的是将一个类中的属性拷贝到另外一个类中。这样就把两个类（一个函数）的属性给混在一起了。

    function mix(receivingClass, givingClass){
        if(arguments[2])
        {
            // 可能不止一个类掺入，存起所有prototype
            for(var i=0, len = arguments.length; i < len; i++){
                receivingClass.prototype[arguments[i]] = givingClass.prototype[arguments[i]];
            }
        }
        else
        {
            for(methodName in givingClass.prototype){
                if(!receivingClass.prototype[methodName]){
                    receivingClass.prototype[methodName] = givingClass.prototype[methodName];
                }
            }
        }
    }
    
上面的函数用于掺杂多个类的prototype属性。一般是继承prototype对象里面的东西：

    var ClassA = function(){};
    ClassA.prototype = {
        // 这里的才是prototype对象中的属性和方法
        method1: function(){console.log("method 1 call")}
    }
    
    // 假设有另外一个类：
    
    var ClassB = function(){};
    
    mix(ClassB, ClassA); // 将method1给混到ClassB中去
    

大部分代码都是从书中摘抄的，这里只是稍微梳理一下各种代码。其实最根本的还是弄清原型链的关系。对于问题的敏锐性，是能够注意到事物之间的关联，理清关键联系，这样能够朝着目标解决问题。

---
end