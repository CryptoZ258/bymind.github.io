---
title: 【GTD】项目收尾
date: 2013-04-02 14:21:06
---
{% raw %}
<p><span style="font-size:16px;">【折腾的痛】</span></p>
<p><span style="font-size:16px;">GTD将在今年5月就要解题了，就像@daoluan 说的，经过了一番的折腾，终于将这个东西给搞出来了。但是总体还是很生涩的，尤其是对于整个系统的架构，“代码跟着数据走”——为了积累这句话的经验，我们付出了惨痛的代价。在一开始，不知道要怎样与服务器交互，数据库的设计千疮百孔，而我负责的web端，随着采用框架，慢慢地解决了。中期审察的时候，老师指出了，我们应该先弄出一个服务器端和客户端，才来写那些花俏的界面。</span></p>
<p><span style="font-size:16px;"><br />
</span></p>
<p><span style="font-size:16px;">【软件开发的过程】</span></p>
<p><span style="font-size:16px;">GTD项目给我最大的礼物就是，认识到了软件开发整个过程是很有规律可循的，软件工程这门课就专门讲这个问题。我们的需求制定得非常模糊，只是说了要使得服务器/PC客户端/android客户端实现随时随地的同步，而因为没有真正深入地探讨这个任务管理软件应该做到什么样子而搞得很多时候都是在被动，左右修改代码，而且造成我们的用户体验不统一。有一款非常优秀的task管理我非常欣赏——</span><span style="font-size:16px;"><a href="http://pomotodo.com/ ">pomotodo</a></span><span style="font-size:16px;">界面很简单，但是用起来很舒服，虽然统计方面有bug，但是我还是觉得很棒。另外安卓端的<a href="http://www.any.do/">anyDO</a></span><span style="font-size:16px;line-height:1.5;">也非常地好用，于是我们就按照这样的“需求”来做。这样看起来很小打小闹不是么？真正的软件工程，是一定要获得真正的用户的认可，需要做出一个原型，让后开发人员不断改进，这样做出的产品，才能够满足用户，才能够算是成功的项目。</span></p>
<p><span style="font-size:16px;line-height:1.5;">详细地回忆一下我们的web端开发过程：</span></p>
<p><span style="font-size:16px;line-height:1.5;">做了一个本地测试版本的应用程序-&gt;确定数据库设计-&gt;采用speedphp框架-&gt;再次设计GTD数据库-&gt;编写交互的js和php程序-&gt;做部分美化。</span></p>
<p><span style="font-size:16px;line-height:1.5;">在这个过程中，犯的很大的一个过错就是过早地进行了界面设计，由于网页设计方面琐碎的细节很多，网页要做得漂亮，少不了各种折腾，写js和css代码，渲染整个页面。而经过整个项目，才真正体会到，这本来是两拨人干的，但是却由同一拨人兼任了。而且由于需求的不明朗，对于交互界面修修改改，耗费了我们大量的时间。直到最后</span><span style="font-size:16px;line-height:24px;">使用MVC框架，</span><span style="font-size:16px;line-height:1.5;">完成所有的逻辑，才发现还有很多工作要做。这不是高效的开发方式，<span style="color:#e53333;">高效的开发应该是一切都是明确的</span>。明确的需求，然后就可以明确地设计模版，然后后台php就可以大胆地搭建逻辑，而需要紧紧盯住的就是前端和后台衔接的地方，还有后台与数据库衔接的地方。其实我们，应该找来那些开源项目，看看人家是怎么干的，是怎么写出逻辑清楚的代码的。</span></p>
<p><span style="font-size:16px;line-height:1.5;"><br />
</span></p>
<p><span style="font-size:16px;line-height:1.5;">【资源与工具】</span></p>
<p><span style="font-size:16px;line-height:1.5;color:#009900;">speedphp框架：</span></p>
<p><span style="font-size:16px;line-height:1.5;">在制作网页的过程中，我发现了很多帮助我们的工具，一个就是采用框架。经过师兄点拨，我在项目上应用了speedphp这个框架，它果然很容易上手，一个星期后就可以拿来项目上用了。很多时候我们浪费了大量时间在瞎琢磨，但是却不知道别人早已经给你写好了工具给你，只是你没有发现。<span style="color:#e53333;">Don't repeat yourself. &nbsp;<span style="color:#000000;">当然，这是我们自学能力的不足，没有主动去各种论坛，博客去发现自己想要的资源。</span></span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">使用别人的框架很方面，但是要警惕框架也有可能把你变成只会做一些粗浅工作的码农，而不是一个思考的程序员。</span></span></p>
<p><span style="font-size:16px;line-height:1.5;"><span style="color:#e53333;"><span style="color:#009900;">背景和css生成：</span></span></span></p>
<p><span style="font-size:16px;"><a href="http://www.websbook.com/alltext/userexperience/5gwybjtpzzwz_17643.html">五款在线背景生成器</a></span></p>
<p><span style="font-size:16px;"><a href="http://blog.jobbole.com/16375/">在线css生成器</a></span></p>
<p><span style="font-size:16px;">网站很多圆角和阴影的css都是用这些工具生成的。</span></p>
<p>&nbsp;</p>
<p><span style="font-size:16px;">【遇到的困难】</span></p>
<p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">在开发过程中还碰到了很多困难，比如团队代码托管,SVN很强大，但是入门需要很大的努力。由于是在linux下，于是就简单学了一下svn的命令行命令——svn co, ci, update等，有时候为了搭建本地环境，还需要创建符号链接到另外一个文件夹下面，因为sae使用的speedphp核心和本地开发用的是不同的，但是其他controller/model/templete都是一样的。参看这篇——<a href="/admin"><span style="font-size:16px;">搭建sae本地开发环境</span></a>, 后来发现改动了许多代码，但是svn上面不能commit了，一怒之下，就重新上传代码包到sae上面，后来要重新建造一个本地开发环境，又一怒之下，写了一个脚本，下次碰到这事情，就运行一下脚本就行了，能自动化的事情，就果断自动化，美国有个哥们雇了一个中国团队开发，自己去冲浪就是一个很好的例子。不动手或者少动手就能够搞定一切事情，这才是高手：P</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;"><br />
</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">当然不仅仅碰到代码部署的困难，还碰到了很尴尬的困难——看了code complete之后，发现自己写的很多代码都特别看不下去了，于是就按照书上面的设计原则： 封装/隐藏/命名要顾名思义 等，改了一阵子才纠正过来，后来的开发过程，果然轻松很多。虽然还是很多缺陷，但是比以前要好多了。</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;font-size:16px;">【收尾】</span></span></p>
<span style="font-size:16px;"> </span><p><span style="font-size:16px;">&nbsp;雨一直下，GTD要收尾了。思愿同学做了很好的总结，很多东西一下子惊醒了梦中人。对于PC客户端，因为之前用Qt的时候发现它的网络功能还挺强的，而且整个结构十分清晰，这边怎么发，服务器端相应地怎么做处理。对于本地怎么记录离线操作（之后要同步的），使用log的方式是最好的，每个log记录一条操作，就像数据库管理系统的日志一样，可以undo/redo，这样才能体现其维护数据的灵活和一致性。可惜，我们的项目很粗浅，不能做到面面俱到，只是经过这次，学到了做项目的方法——看别人怎么做——》想想自己怎么做——》开做——》做得更好！ 这也是人活着成长的方式。可惜，我在开发过程中，没有注意要写些博客来记录整个过程，供读者参看。下面是简单的开发过程记录：</span></p>
<p></p>
<h2 class="con_title" style="margin:0px 0px 1em;padding:0px;font-weight:400;font-size:16px;line-height:1.6em;color:#202f0c;font-family:'Microsoft Yahei', Tahoma, Arial, Helvetica, STHeiti;letter-spacing:1px;"><a href="/?post=70">[GTD]开发9月下旬到10月下旬</a></h2>
<div><h2 class="con_title" style="margin:0px 0px 1em;padding:0px;font-weight:400;font-size:16px;line-height:1.6em;color:#202f0c;font-family:'Microsoft Yahei', Tahoma, Arial, Helvetica, STHeiti;"><a href="/?post=80">[GTD]关于开发的一些感想</a></h2>
</div>
<div><p><a href="/?post=83"><span style="font-size:16px;">[GTD]搭建本地speedphp for sae开发环境</span></a></p>
<p><span style="font-size:16px;"><a href="http://daoluan.net/blog/gtd-summary/">参看思愿更详细的记录</a></span></p>
<p>by bibodeng 2013-04-02</p>
<p>&nbsp;</p>
</div>
<p></p>{% endraw %}
