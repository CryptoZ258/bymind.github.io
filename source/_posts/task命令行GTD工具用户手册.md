---
title: task命令行GTD工具用户手册
date: 2014-01-25 17:57:29
---
task命令行GTD工具用户手册
---
by bibodeng 2014-01-25

###名字（NAME）

    task - 一款命令行的todo任务管理软件
   
###命令（SYNOPSIS）

    task 过滤符 子命令 [<mods>|<args>]    //调用task子命令
    task --version                      //可以获得task的版本号
 
###描述（DESCRIPTION）

taskwarrior是一个命令行式的任务列表管理软件。它可以维持一个你的任务列表，允许你添加/删除/修改任务。它具有丰富的子命令，可以做你想不到的事情。当然，在底层，它是一个任务列表排程程序。你添加文字任务和关于任务的描述，当你用日期来排列时它就是一个日程表，当你用优先级排列时，它就是你的做事顺序。你还可以添加标签，项目组，方便你管理你的这些任务。
    
###过滤符（FILTER）

过滤符号由0或多个查找特征组成，用来选择你想要查看或修改的任务，例如，列出所有`Home`项目下的任务：

    task project:Home list  // list是一个子命令，列出tasks
    
你可以指定多个过滤符号：

    task project:Home +weekend graden list

该例中，有三个过滤符： `Home`项目，weekend标签，还有描述中必须包含`garden`。当然也可以理解为：

    description.contains:garden

当没有过滤符号的时候，意味着所有tasks都将被选中，这时候你就要小心了，因为修改的时候是应用到所有tasks的，而且不能回滚。例如：

    task modify +work
    this command has no filter, and will modify all tasks. Are you sure?(yes/no)
    
将会为所有tasks都添加一个work标签，当然前提是你选择了yes。

更多例子如下：

    task                                        子命令 操作内容
    task 28                                     子命令 操作内容    // 选中第28个task（ID为28）
    task +weekend                               子命令 操作内容    // 选中带weekend标签的
    task project:Home due.before:today          子命令 操作内容    // 选中Home项目，且在今天之前的
    task ebeeab00-ccf8-464b-8b58-f7f2d606edfb   子命令 操作内容    // 选中UUID为这个序列的
    
默认情况下，过滤器的各个条件是and（与）的，当然or（或）和xor（异或）也是可以用的，如下括弧里面的是支持的：

    task '(/[Cc]at|[Dd]og/ or /[0-9]+/)' 子命令 操作内容  // 这里用到了正则表达式,不懂正则。。那忽略吧，只要注意这里用了括号和or就行了
    
下面举些用到了ID和UUID的例子：

    task 1,2,3              delete
    task 1-3                info
    task 1,2-5,19           modify pri:H
    task 4-7 ebeeab00-ccf8-464b-8b58-f7f2d606edfb   info
    
###修改内容（MODIFICATIONS）

修改内容可以由0个或多个修改组成，如下：
    
    task 过滤符 子命令 project:Home
    task 过滤符 子命令 +weekend +garden due:tomorrow
    task 过滤符 子命令 Description/annotation text
    task 过滤符 子命令 /from/to/

###子命令（SUBCOMMANDS）

taskwarrior支持很多子命令，包含 读命令，写命令，杂项命令 和 脚本帮助命令。读命令不允许修改task，写命令对命令进行修改，脚本帮助命令帮助你写附加的脚本，例如shell的自动补全等。

####读子命令（READ SUBCOMMANDS）

reports是读子命令。输出和其它一些行为可以在配置文件里面配置，也有一些读子命令不是关于reports的。

    task --version              // 查看task的版本
    
    task 过滤符                // 查看满足条件的tasks
    
    task 过滤符 active         // 查看已经start，正处于激活状态的task
    
    task 过滤符 all            // 显示满足条件的所有tasks，包括递归task的父task
    
    task 过滤符 blocked        // 显示那些依赖于其它task的tasks
    
    task 过滤符 burndown.daily     // 绘制日统计图像
    
    task 过滤符 burndown.weekly    // 绘制周视图
    
    task 过滤符 burndown.monthly   // 绘制月视图
    
    task calendar [due|<month> <year> | <year>] [y] 
    // 尖括号包含的内容替换成相应的量，显示一个月的日历,如果给出年，则显示一年的，如2014，如果给出年月，如`2 2014`则会从2014年2月份开始的几个月的日历。如果是due，则会显示预期最早的task。
    
    task colors [sample | legend]   // 显示支持的颜色，有简单版和完全版之分

    task columns                // 显示所有列和样式，在导出报表的时候非常有用
    
    task 过滤符 completed      // 显示已经完成的tasks
    
    task 过滤符 count          // 计算已经完成的tasks数量
    
    task 过滤符 export         // 将选中的task导出成json格式，可以重定向到某个文件里面
    
    task 过滤符 ghistory.annual    // 年报表视图,完成情况
    
    task 过滤符 ghistory.monthly   // 月报表视图
    
    task help   // 获取帮助
    
    task 过滤符 history.annual     // 年报表
    
    task 过滤符 history.monthly    // 月报表
    
    task 过滤符 ids    // 获取被选中项目的id序列，如1-3或2，3这样
    // 当用在修改特定的task时，它可是十分强大的，例如：
    task $(task project:Home ids) modify priority:H
    // 对Home project中的task进行修改，都添加一个高优先级,译者测试不成功，并且有点多此一举，不如用下面的：
    task project:Home modify priority:H
    
    task 过滤符 uuids      // 得到uuid的序列，用逗号分割
    
    task 过滤符 information    // 也写作info，得到选中task的详细信息
    
    task 过滤符 list       // 得到一个标准的列表，包含一些列
    
    task 过滤符 ls         // 得到一个精简了列的task列表
    
    task 过滤器 minimal    // 极简列表
    
    task 过滤符 newest     // 得到最新的tasks
    
    task 过滤符 next       // 显示最紧急的一批tasks,按照urgency这个计算得来的指标排序
    
    task 过滤符 ready      // ready的tasks，指没在时间表中，或者已经过期了的
    
    task 过滤符 oldest     // 最早的tasks,按age排序
    
    task 过滤符 overdue    // 在超出预期未完成的
    
    task 过滤符 projects    // 列出所有的projects
    
    task 过滤符 recurring      // 查找递归
    
    task 过滤符 unblocked      // 没有依赖性的
    
    task 过滤符 waitting       // 显示正在等待的tasks,和顺序有关
    
    
####写子命令（WRITE SUBCOMMANDS）

    task add 内容 // 添加一个任务到列表
    
    task 过滤符 annotate 操作内容    // 为task添加注释
    
    task 过滤符 append 内容          // 追加文本到已经存在的task尾部
    
    task 过滤器 delete 操作内容      // 删除满足条件的task
    
    task 过滤符 denotate 操作内容    // 当内容和task原有的notate相符时，则删除notate
    
    task 过滤符 done 操作内容        // 将task标记为已经完成
    
    task 过滤符 duplicate 操作内容 // 复制原有的task,并可以修改,如有操作内容是作为notation
    
    task import &lt;文件1&gt; [&lt;文件2&gt;]   // 从文件中导入tasks
    
    task log 操作内容     // 添加一个新的但是已经完成了的任务,等于做记录
    
    task merge <url>    // 远程合并task数据库，如
    ssh://[user@]host.xz[:port]/path/to/.task/
    rsync://[user@]host.xz[:port]/path/to/.task/
    [user@]host.xz:path/to/.task/
    /path/to/local/.task/
    
    你甚至可以在.taskrc配置文件中对常用的url进行别名设置。
    
    task 过滤符 modify 操作内容    // 修改现有的tasks，操作可以有添加标签，修改project，优先级等
    
    task 过滤符 prepend 操作内容   // 为task添加文字到头部
    
    task pull <url>     // 拉取远程的数据覆盖本地数据库
    
    task push <url>     // 推送自己的版本到远程，这和版本库很类似啊，下次你搭建一个服务器，随处都可以访问了
    
    task 过滤符 start 操作内容   // 标记为开始
    
    task 过滤符 stop 操作内容   // 移除开始标记，暂停
    
###杂项子命令（MISCELLANEOUS SUBCOMMANDS）
    
    
    task config [name [value|'']] // 查看或者修改某项配置
    
    task diagnostics    // 诊断
    
    task execute 外部命令`// 执行外部命令
    
    task logo       // 显示taskwarrior的logo
    
    task reports    // 列举所有支持的报告项，包括系统报告和用户自定义报告
    
    task shell      // 进入task的命令行，可以直接list这样运行执行
    
    task show [all | substring]     // 显示当前设置
    
    task 过滤符 stats  // 显示统计信息，包括空间及其它状态信息
    
    task 过滤符 tags   // tags的统计信息
    
    task 过滤符 projects   // projects的统计信息
    
    task timesheet [weeks]      // 得到一个周报表，哪些做完了，哪些开始了
    
    task undo   // 撤销最近的动作
    
    task version    // 显示版本号的详细信息
    
###帮助子命令 （HELPER SUBCOMMANDS）

    ... 不想翻译了，翻完上面的手都酸了，我都会用了，原谅我的懒惰...
    
---
end
    </url></url></url></year></year></month></args></mods>