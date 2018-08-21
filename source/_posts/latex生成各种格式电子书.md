---
title: latex生成各种格式电子书
date: 2013-11-09 23:36:29
---
# 使用latex源码生成各种格式电子书

by bibodeng 2013-11-09

## 前言

为了让电子书能够在更多的平台上被阅读，那么则需要生成各种版本的电子书，这个过程真的有点蛋疼，但是通过各种非常有用的工具，干起来也非常快。下面主页记录一下常用的格式的生成：

    PDF，mobi， epub， html

其中PDF是最容易的，latex编译默认就输出PDF，所以我们很容易获得。而且上篇已经提及了如何生成6吋版的PDF电子书。所以下面着重讲一下其它三种格式的生成。

## epub

epub格式是一种在苹果手机，平板上使用的通用格式，目前kindle还不支持，但是有些kindle的系统——如多看，已经支持epub格式的电子书了。在ubuntu下，可以使用pandoc这个工具，从latex文件直接生成epub格式电子书。

首先，我们要安装pandoc：

    sudo apt-get install pandoc
    
这样就安装好了。它的详细使用方法见[这里](http://johnmacfarlane.net/pandoc/epub.html)。我们直接使用pandoc命令转换格式：

    pandoc book.tex -o book.epub

可以看到立马生成了一个book.epub文件，将该书籍导入到calibre里面查看，可以看到转换的格式还行,稍微有一点瑕疵，大体上还是ok的。

![epub版](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/279d39080390d5733af232089be3a0082013110907505713841.png)

## mobi

mobi格式可以使用calibre直接从epub格式进行转换，安装完该软件后，直接对文件进行转换。等待一段时间，等其转换完成，打开发现mobi格式和epub几乎一样。

## html

### tex2page
要生成html有许多工具，但是我们先介绍一种——tex2page，这里有一份王垠写的[教程](http://docs.huihoo.com/homepage/shredderyin/tex2page/intro.html)。
    
    tex2page book.tex
    
一般是可以编译成功的。如果在文档目录下新建一个和tex文档同名的.hdir文件，里面添加一行

    pages

则会在生成网页的同时能够把文件都放在pages下面，而不会在当前目录搞乱你的文档。


### tex4ht

还有一种办法是安装一个tex4ht，然后使用htlatex命令来转换。

    sudo apt-get install tex4ht
    htlatex mydocument.tex 
    
这样会生成一个html文件。

### pandoc

pandoc真的是一个神器啊，可以转换各种格式，这里有个[示例](http://johnmacfarlane.net/pandoc/demos.html)。

    pandoc -s -S --toc -c book.css book.tex  -o book.html
可以使用自定义的样式为生成的html进行排版。这样的效果会好一点：

![IT小小鸟网页版](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/61661a8b55f13cc8bf9de521300735352013110915351330487.png)

---
end