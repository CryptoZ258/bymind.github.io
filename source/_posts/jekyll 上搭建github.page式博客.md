---
title: jekyll 上搭建github.page式博客
date: 2013-09-14 12:12:59
---
jekyll 上搭建github.page式博客
===
之前独立博客上的各种各样的问题，例如垃圾评论，模板不支持代码高亮， 彻底惹恼了我，所以准备投奔jekyll的怀抱，直接到github page上写博客。折腾了一天，总算弄得差不多了。
 
###第一步 建立自己的项目
首先，要有github账号，新建一个github的项目，叫做 username.github.com, 现在github为了不让github page 影响性能，专门用 github.io域名提供page服务。在自己的github主页上新建一个repo，然后就可以了。
 
 
###第二步 clone别人的项目
我是直接把别人已经搭建好的jekyll项目，包括模板主题和建好的目录等。在终端运行下面命令：
 
    $ git clone https://github.com/plusjade/jekyll-bootstrap.git USERNAME.github.com 
    $ cd USERNAME.github.com 
    $ git remote set-url origin git@github.com:USERNAME/USERNAME.github.com.git 
    $ git push origin master
 
 这样就可以就算部署成功了。过几分钟后，访问 [`http://USERNAME.github.io`](http://USERNAME.github.io) 你就能看到生成的页面了，如果不能生成，可能是你的index.yml文件出错了，github会发邮件给你。
 
###第三步 搭建jekyll本地环境
jekyll是基于ruby的，所以你要先安装ruby，我的机器是ubuntu13.04， 已经预装了ruby1.9.1
 
    sudo apt-get install rubygems
    sudo gems install jekyll
 
但是我发现会碰到这样的问题：
    
    Unable to install gem - Failed to build gem native extension - cannot load such file— mkmf (LoadError)
 
 
报告说某个包找不到了，可能是我们的版本不够高，stack overflow 上有类似的[问题](http://stackoverflow.com/questions/13767725/unable-to-install-gem-failed-to-build-gem-native-extension-cannot-load-such)
 
解决办法是安装 ruby1.9.1-dev:
    
    sudo apt-get install ruby1.9.1-dev
 
可能之后还要解决一些问题，例如配置博客config.yml:
 
    author:
        name: USERNAME
        email: USERNAME@gmail.com
        github: USERNAME
        ...
 
更加详细的配置参考[jekyll的评论，google统计](http://jekyllbootstrap.com/usage/blog-configuration.html)
 
###第四步 开始在本地写博文
现在可以开始在本地写博文了，使用如下命令：
 
    rake post title = "hello world"
 
你将看到_post下面为你自动生成了一个.md后缀文件，编辑它就是写文章了。你会发现生成的文件都是这样的开头：
 
    ---
    layout: post
    title: "hello world"
    description: ""
    category: 这里填分类（需要是post下的一个文件夹）
    tags: [标签1, 标签2]
    ---
    {% include JB/setup %}
    这里开始是正文
 
也可以新建页面：
 
    rake page name = "about.md"
 
写完了，可以在本地测试：
 
    cd USERNAME.github.com
    jekyll serve
 
访问`http://localhost:4000` 就可以访问你的博文了。
 
###第五步 用git上传博文
我们就三板斧就够了：
 
    git add .     // 添加当前目录所有内容
    git commit -m "add passage x"
    git push origin master
 
这样就成功提交了自己的文章，在github项目中可以看到自己上传的文件，而在你的博客  `http://USERNAME.github.io`  中也生成成功了。
enjoy yourself。
 
###进阶 写作
使用markdown教程
 
一开始会很折腾，但是熟练了之后，的确可以专注于写作。
 
参考链接：
 
[利用jekyll搭建个人博客](http://www.mceiba.com/develop/jekyll-introduction.html)
 
[markdown 手册](http://wowubuntu.com/markdown/#link)
 
[github page 极简教程](http://yanping.me/cn/blog/2012/03/18/github-pages-step-by-step/)
 
[jekyllboostrap 项目](http://jekyllbootstrap.com/)

[我的github博客](http://bibodeng.github.io)
 
by bibodeng 2013-9-6