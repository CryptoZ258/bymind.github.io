---
title: 学习SVN
date: 2013-04-14 21:09:23
---
{% raw %}
<link type="text/css" rel="stylesheet" href="/content/plugins/bibo_mark/article_bibo.css"> <div class="art_content"><p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">​2013-04-02&nbsp;&nbsp;因为svn出现冲突，不能上传代码，很想砸电脑。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">一个好的工具就像一柄神剑，如果你不会用，往往会伤到自己，现在我想说，SVN就是这样一柄神器。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">长痛不如短痛，所以我打算一次性把SVN给搞懂，要不然就把电脑给砸了，很显然我只有一个选择。秉持着刘未朋的三个问题：&nbsp;本质是什么？有什么原则？有什么方法？&nbsp;（记不得是不是这三个问题了）我试着去克服svn这个困难。记得大二和师兄一起做项目的时候用上了svn，那时候还在windows下，用一个图形界面的svn在提交代码。现在想起来真的很可笑，当时每次我都去checkout，而不是update，而且每次checkout出来的代码，我都单独地放到一个文件夹下面，好好保存，当时我在想，这样就足够安全了。但是，现在我明白了，完全没有这个必要，因为版本库里面已经有每个版本的记录，可以拿到任何一个版本的代码。好吧，废话讲完了，让我们好好学习svn吧！</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<h3>SVN本质是什么？</h3>
<p></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">SVN是一个文件服务器，但是它是一个强大的文件服务器，能够记录所作的更改，使用于代码托管。有了SVN就能很大方便团队开发，各人都可以提交自己的代码。最重要的是，它能够按照修改来维护若干个版本，便于回复和更新。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">在我们的团队里面，就当作一个代码库管理工具来使用，将代码提交上去，但是我碰到的问题是，不会使用svn来维护多个版本，且遇到冲突的时候不知道如何解决。所以svn命令到了一半就运行不下去了，频频报错，搞得头大。半桶水害死人啊！使用的方法不对，所以搞得整天都在做解决冲突的问题，而且这冲突是我一个人制造出来的，那是因为我上传了一个代码包，这个代码包里面包含有大量的临时文件。所以，读《版本控制之道》到“如果你不小心上传了一堆临时文件到版本库中的话，你的项目经理会杀了你~”的时候，我会会心一笑。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">SVN的基本原理</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">SVN就是要求文件同步共享，最新的代码总是可以通过一个命令提交上去，甚至到了做了修改自动提交的。如git，以及ubuntu的软件中心都有着相似性，都是管理着一个库，其命令也具有相似性，如&nbsp;apt-get&nbsp;install&nbsp;xxx，&nbsp;git&nbsp;clone&nbsp;xxx,&nbsp;svn&nbsp;co&nbsp;xxx。但是这简单命令，根本满足不了开发人员的需求。SVN的难点就在于，如果两个client都做了修改，系统将怎样维护一致性。有的系统采用锁来同步，即排斥他人同时操作文件，必须一个个按照顺序来。如果有人做了修改，必须将新文件下载下来，然后处理矛盾，合并后上传到服务器。这样的合作方式，需要人为地处理冲突。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">SVN用户维护的工作拷贝，往往是代码库中的某一个版本，而且是版本库的一个子目录，例如1，2，3这样的目录就是某个版本。svn&nbsp;checkout&nbsp;&nbsp;PATH可以获得一份工作拷贝。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">试验一下：&nbsp;cd&nbsp;/var/www</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">&nbsp;svn&nbsp;checkout&nbsp;<a href="https://svn.sinaapp.com/bibodeng" target="_blank" data_ue_src="https://svn.sinaapp.com/bibodeng">https://svn.sinaapp.com/bibodeng</a></p>
<p style="text-align:center;margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"><img src="http://www.wiz.cn/unzip/3eb90c0e-f584-11e0-a072-00237def97cc/6605ccfa-15cd-928a-0b00-365bdeba972f.5117/index_files/d2c46b4204ca182382637b43d4854edb.png" data_ue_src="http://www.wiz.cn/unzip/3eb90c0e-f584-11e0-a072-00237def97cc/6605ccfa-15cd-928a-0b00-365bdeba972f.5117/index_files/d2c46b4204ca182382637b43d4854edb.png" /></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">获取了版本1的工作拷贝，在我的/var/www目录下面。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">做了修改之后，则svn&nbsp;commit&nbsp;-m&nbsp;"上传时的日志消息&nbsp;Message"，叫做提交修改。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">每做一次修改，且提交了，就能够看到版本号+1了。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">update会对那些过期的在本地工作拷贝下未修改过的进行更新，但是不会修改我们修改过的文件，这样保证了我们不愿意的修改svn不会自动帮我们做修改。修改过的文件可以commit，但是如果不是最新的，那么不能commit，因为会影响服务器端的修改，故而需要人update然后检查并且解决冲突，才能再次提交。&nbsp;&nbsp;commit只会提交更改过的那部分，而不会自动更新其余部分，所以这是一个混合版本，有些文件是老版本，有些是最新版的。我现在想要学会的就是怎么让我的编程很容易提交，而且很容易撤销，有了冲突的时候，能够及时地处理。到时候，叫SVN往前就往前，回滚就回滚，有种掌控历史的快感。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<h3>SVN原则</h3>
<p></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">好，这里停顿一下，问问SVN有什么原则。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">我现在体会到了SVN的原则就是KISS，懂得合作的原理，然后小心的更新提交。在做一件事情之前，考虑一下自己的目标，这样做的后果。比如我修改了一个文件Number.txt，假如要提交。那么我们最好先知道别人对网络版本库中的该文件做了什么，然后我们再看我们做的修改能否合并进去。所以就要先update，解决若干冲突，再commit。这样才能保证版本库的纯正。当然，在提交的时候，要尽可能逻辑整体的，而且频繁的更新。比如我在某个文件下面添加了一个函数，有那么十几行，在本地测试过了，可以很好运行，ok，提交，而且svn&nbsp;ci&nbsp;-m&nbsp;"添加了xx函数"&nbsp;记下几笔日记。这个频率大概是1小时1次，将来在小组里搞开发，可能大家都很高效，那么频繁提交可以让你的修改更早让人家看到，可以查出错误或者使用你的成果，有很大的好处。原则就是&nbsp;合作，保持整体简洁。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">next&nbsp;what？真正开始用SVN</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">老实说我之前还不会import命令，但是现在我知道了用它来导入一个本地文件作为版本库的一部分，这有点像git的init。然后会初始化checkout一次，然后做修改，提交。而且最好主干版本放在trunk下面，然后branches放分支，好吧，我承认自己不懂，继续看书。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">svn里面的几个命令是基础的，最常用的。例如status,&nbsp;update,commit,checkout,revert,resolved,log,diff等等。这里的命令一概不解释，网络上有很好的文档和教程，真正坐住板凳来看，绝对是可以学的很扎实的。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">我发现svn甚至可以用diff来做一个补丁，也就是一个标示不同版本之间的不同之处的文件。而这个补丁，可以用patch命令来打补丁，全自动，比洗衣机还方便。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">还有一个意外就是，我居然可以追究到哪行代码是谁写的，使用svn&nbsp;blame&nbsp;可以看到文件中每一行的作者。这样统计谁写了多少代码，谁编写了错误的程序，谁要对代码负责&nbsp;追究起来就轻而易举了。当然我们使用这个不仅仅是为了追究责任，而是为了更好的“合作"。当我们知道这是谁写的代码时，结合svn&nbsp;log我们就可以追踪错误所在，从而更快地排除错误，获得正确的版本。我相信，这在web开发中是相当有用的。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">我犯过一个错误，那就是用操作系统的命令修改了svn工作目录下的文件和目录，例如用rm，mv&nbsp;一通瞎搞，然后搞得整个版本库乱七八糟，无法使用。看了文档才发现，原来要让svn管理一切，必须要让它知道我所做的所有动作。故而命令前面要加一个svn，变成这样：&nbsp;svn&nbsp;rm&nbsp;xxx。或者做了修改，让svn知道一下，例如拷贝了，要用svn&nbsp;add进到版本库中来。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">一切为了合作，一切为了共享，一切为了更加简单。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<h3>SVN方法</h3>
<p></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">此处，沉默是金~</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">基本命令参考<a href="http://www.subversion.org.cn/tsvndoc/" data_ue_src="http://www.subversion.org.cn/tsvndoc/">这个教程</a>。</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">update,&nbsp;checkout,&nbsp;commit,&nbsp;add,&nbsp;remove,&nbsp;move,&nbsp;copy,&nbsp;status,&nbsp;diff&nbsp;,&nbsp;revert,&nbsp;update,&nbsp;resolved.</p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;"></p>
<p style="margin-top:0px;margin-bottom:0px;font-family:'Times New Roman';font-size:medium;line-height:normal;">by bibodeng &nbsp; 2013-04-14</p>
<div><br />
</div>
</div>{% endraw %}
