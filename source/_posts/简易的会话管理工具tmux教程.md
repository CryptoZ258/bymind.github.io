---
title: 简易的会话管理工具tmux教程
date: 2017-03-15 09:29:04
---
##为啥要用tmux
在我们远程连接服务器的时候，往往终端连接的ssh因为网络问题非常容易中断，所以聪明的工程师发明了一个即使连接中断了，但是这个会话并没有结束，你重新连上去，依然还是上次你断开连接时候的样子，你可以继续做的你的编辑或者其它工作，它依然在等着你，听着是不是很酷？

## tmux命令
要使用tmux，首先你需要在远程服务器中安装一个tmux:


	apt-get install tmux


tmux有一组子命令，用来管理会话，从新建一个会话，到重命名会话，到结束一个会话，都有对应的命令可用。在连上远程服务器后，用如下命令创建一个会话：


	tmux new -s vim // 创建了一个叫做 vim 的会话
	tmux // 创建一个系统自动编号的会话


会话新建后会进入自己专有的命令行交互。如果你做了很多别的，改变了这个session的用途，比如之前进行vim编辑的session，被你用来运行`python manage.py runserver`了,那么你可以重命名它：


	tmux rename-session -t vim runserver


这样vim就变成runserver了，你可以通过下面的命令查看所有的会话：


	tmux ls


你将看到一个列表，展示了所有会话的名字和占用状态，如果是attach，那么说明已经被连接。
假如我们想要退出一个会话，直接关闭ssh窗口即可，那么下次回来你通过attach来重回会话：


	tmux attach -t vim
	// 或 tmux a -t vim
	// 或 tmux at -t vim


如果这个session已经不再使用了，可以用如下命令退出当前session：


	exit


这样你通过`tmux ls`就看不到这个会话了，它被删除了。

另外，想要查看当前的会话名称，可以运行下面的命令：

	tmux display-message -p '#S'

也可以使用alias来减少输入的字符，比如只用tmux_curr即可代表上述命令:

	alias tmux_curr='tmux display-message -p "#S"

也可以vim .bashrc 编辑bash配置，这样每次登录时会自动配置alais，在.bashrc中上面一行。

## 结语
程序员应该通过一些工具提升自己的工作效率，减少一些不必要的麻烦，tmux就是这样的一种工具，可以存储和恢复会话。有兴趣的同学可以研究一下tmux的更多命令和原理，它实际上是模拟了一个登录会话，并且常驻在服务器中，当attach的时候，相当于是通过tmux代理来连接真正的会话。

by bibodeng 2017-03-15