---
title: AssertUtil断言式异常处理
date: 2016-06-08 11:43:01
---
#AssertUtil断言式异常处理

在程序开发中，异常处理是最常见的，但是经过了两年的工作，我才慢慢理解到异常处理应该怎么做，在学校的时候并没有做异常处理的习惯和成熟的方法。加入弹性福利的开发以来，编写了许多关于异常处理的代码，对于异常处理，怎么样处理得优雅得体，对于一个项目来说，还是比较重要的，尤其是在运营阶段，如果不断被异常轰炸，是会令人崩溃的。

##异常的结构
在阅读一些计算机编程经典的时候，常常被教导写代码要用`try...catch...finally`格式，try里面放可能出错的代码，catch后面应该多跟具体的异常，里面放异常的处理，尽量不要过长，避免在异常处理的时候出现异常，finally里面放结尾工作，例如关闭文件、清理资源等。但是平时写代码的时候，常常有一个疑问，那就是何时处理异常，何时抛出异常？其实，这个答案，我至今还不知道。目前能给出的答案是，我们在容易出错的地方捕捉异常，在捕捉异常的时候，我们尽量在同一个层次去处理异常，如果本层次处理不了，那就抛出到更高的层次做处理。对于抛出异常的情况，我们更多是定义业务上的异常（程序本身可能并没有抛出异常），或者将异常包装以后抛出给上个层次处理，这样子异常的层次就比较整齐。实际上throw和GOTO一样，都是一种破坏结构性的代码跳跃，使得我们的整洁性被破坏。

    try{
        // 可能出错或者希望不要出错的逻辑代码
    }
    catch(MyException1 myException1){
        // 处理第一种情况异常
    }
    catch(Exception exception){
        // 处理剩余情况异常
    }
    finally{
        // 扫尾清理
    }  

以上就是异常处理的经典结构，try包围了想要确保正确的代码，第一个catch只处理第一种异常情况，第二种处理剩余异常情况，二者只有一个会执行，在逻辑复杂的情况下，有可能发生多种异常情况，而不同情况的处理方法并不相同，所以尽量定义详细的异常，方便catch到之后处理。如果以大而全的Exception来替代多个详细catch的话，如果要处理详细的异常，就得这样写：

    try{
        // 可能出错或者希望不要出错的逻辑代码
    }
    catch(Exception exception){
        // 处理所有异常情况
        if (exception is MyException1){
            // 处理异常情况1
        }
        else if (exception is MyException2){
            // 处理异常情况2
        }
        // 处理其它情况异常
    }
    finally{
        // 扫尾清理
    }  

这样写有个弊端，嵌套的层次多了，还不如直接catch来得简洁直接，另外一个，当你修改了内部抛出的异常类型，你不能直观发现到底这种异常被catch处理了没有，还得看看if语句里面的条件。

##处理业务异常
目前我们还存在的问题是，每个层次的代码都有可能抛出异常，每个层次的异常又可能有两种不同的处理方法，一种是被catch镇压了，一种就是被throw上报了。我们希望，那些上层逻辑不关心的异常，被catch镇压，但是如果碰到上层关心的异常，务必要上报出来做处理，而且尽量以业务异常的方式抛出，而不是以一个大而泛的Exception概括。

外层的catch能起作用，是因为内层代码抛出了异常，要么就是自己写的代码里throw，要么在所调用的函数中有throw。那么一般是什么情况下才会throw呢？因为throw之后，程序是不会继续按顺序执行的，而是跳出来外部的catch中执行，所以只有出现异常执行不下去的时候，会选择抛出。例如，某个输入有误不是我们要的，或者网络发生错误重试后仍然报错，再比如很常见的该方法未实现，这些情况都是要抛出来给外层处理的。

为了方便，有时候我们也需要定义自己的业务异常，以和其它异常区分开来，碰到这种业务异常，处理成为返回失败，然后将异常消息返回。

##使用断言式异常
断言，是使用`assert` 条件，不符合条件后执行语句的方式，通过当前运行中的变量做一些推断，例如运行到一个赋值`a=b;`语句后，我推断`a == b`，如果不成立，那程序有问题，不能执行下去。当然现实生活中的例子更加复杂一点，例如对支付的金额是这样断言的  `assert cost &gt; 0 , throw BizException("支付金额须大于0") `。通过这样的断言式异常，我们可以方便地对数据和当前的变量条件做判断，从而确保不正确的时候不会继续运行下去。于是我们实现了一个模块，专门判断各种条件，用`IsTrue`, `IsFalse`, `IsInEnum`等方式来判断各种我们想要判断的条件，这样通过校验，基本上能够让程序准确无误地运行下去，一旦发生错误，这个异常必然被捕获，报告到开发人员那里。

    public sealed class Validator
    {
        private IList<string> exceptionMessageList = new List<string>();
        private Validator() { }
        /// <summary>         /// 获取实例
        /// </summary>         public static Validator Instance { get { return new Validator(); } }
        #region 抛出断言异常
        /// <summary>         /// 抛出异常
        /// </summary>         /// <param name="msg" />异常消息
        public Validator Fault(string msg)
        {
            exceptionMessageList.Add(msg);
            return this;
        }
        /// <summary>         /// 检验完成
        /// </summary>         public void Done()
        {
            if (exceptionMessageList.Count &gt; 0)
            {
                throw new AssertException(string.Join("~", exceptionMessageList.ToArray()), exceptionMessageList);
            }
        }
        #endregion
        /// <summary>         /// 断言对象不为空
        /// </summary>         /// <typeparam name="T">对象类型</typeparam>         /// <param name="o" />对象
        /// <param name="message" />异常提示信息
        public Validator IsNotNull<t>(T o, string message = "传入参数不能为空！")
        {
            if (o == null)
                Fault(message);
            return this;
        }
    } 

Validator实现了一个类，包含了一个异常消息列表，一个Fault判断函数，将错误的消息加入到异常消息列表中。 该Validator内可以实现自己的判断逻辑，如IsNotNull，判断该传入的对象o是否为null，如果是null，则将异常信息放入异常消息列表。

    /// <summary>     /// 断言对象不为空
    /// </summary>     /// <typeparam name="T">对象类型</typeparam>     /// <param name="o" />对象
    /// <param name="message" />异常提示信息
    public static void IsNotNull<t>(T o, string message = "传入参数不能为空！")
    {
        Validator.Instance.IsNotNull(o, message).Done();
    }  

实际应用时，使用一个static类AssertUtil实现若干类似static IsNotNull的方法，使用时，直接在代码中加入断言式判断如果碰到异常情况，将会抛出一个`AssertException`，外层代码对该`AssertException`进行处理即可。

    JsonResultEntity result = new JsonResultEntity();
    try
    {
        AssertUtil.IsNotNull(obj, "参数不能为空！");
        //AssertUtil.IsTrue(obj.PointValue &gt; 0, @"积分数必须大于0");
        // ...
    
    }
    catch (AssertException ex)
    {
        result.resultMsg = ex.Message;
    }
    catch (Exception ex){
        MessageCenter.Instance.SendAppWebErrorMail(CurrStaff.FullName, ex.Message, this.Request.Url.ToString(), ex);
    }
    return result; 

##结语
异常的处理方法，如果是业务类的异常（如业务不允许非正式员工下单）或输入类的异常（用户支付了一个-1元），我们一般是记录一个日志，然后封装成为消息返回给用户。而如果是程序级的错误，如除于0，类型转换错误了，服务器500了，我们都会通过日志或者邮件的方式通知管理员，这里发生异常了，程序有问题哦。当然，异常消息的通报频次，通报级别有赖于自己实现程序控制。最终，监控的目的是为了正确，做异常处理能够做到，只要发生异常，就能定位所在地方，只要推送了异常消息，就必定是我们关心的（有用的异常），那么程序将会运行得很健壮，因为各种情况你都考虑到了，并有严密的通报机制，所以有错误也很快被纠正。

做了异常处理，你的程序不会以崩溃的方式退出，即使有错，也是优雅地退出，而优雅的AssertUtil断言式异常，则让异常处理更加优雅。

by bibodeng 2016-6-6</t></t></string></string>