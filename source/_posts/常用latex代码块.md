---
title: 常用latex代码块
date: 2013-11-03 16:27:17
---
#常用latex代码块

by bibodeng 2013-11-3

## 为啥搞latex

其实接触`latex`也有些日子了，本来是一直打算用它来排版我们自己的简历，论文，还有我们业余写的电子书。最近和思愿在折腾这个东西，故而觉得有必要整理出一篇常用的latex代码块出来，然后结合我们的需要发挥。

宿舍一个哥们总是说我折腾，linux，latex，Qt，折腾的东西真的不少。我自己也问我自己是不是浪费了太多时间在这些不必要的折腾上，后来意识到任何东西都有好处也有不好，就看我们用的人的心态，用的方式了。latex如果用得好，将来写毕业论文的时候必定是让老师眼前一亮，不排除这有点装逼嫌疑，但是我是喜欢酷的，喜欢与众不同。即使是排版，我也觉得用代码什么排出来的会非常漂亮。

## 常用代码
有了下面的一些常用代码，我们很容易就解决排版中的一些基本问题，除此之外，建议阅读《一份不太简短的latex说明》。[百度](http://wenku.baidu.com/view/754ab741a8956bec0975e3b2.html)和[新浪](http://ishare.iask.sina.com.cn/download/explain.php?fileid=18921996)提供下载。

### 嵌入代码块
如果文档或书籍中带有代码，那么我们常常要使得代码缩进，并且着色。

	%　先在文档声明区加入必需的包
	\documentclass[11pt,oneside]{book}
	\usepackage{CJKutf8}
	\usepackage[utf8]{inputenc}
	... % 下面这些是重点
	\usepackage{listings}
	\usepackage{xcolor}
	\lstset{basicstyle=\ttfamily,
	  showstringspaces=false,
	  commentstyle=\color{red},
	  keywordstyle=\color{blue}
	}

然后我们就可以直接在一个章节里面插入代码了，以C++为例，也可以使用Java等其它语言：

	\begin{lstlisting}[language=C++,caption={C++ version}]
	void main()
	{
		printf("hello world");
	}
	\end{lstlisting}
	
上面这段代码向文中嵌入代码。可以看到关键字被染色了，如果有注释的话，还会被染成红色。

![代码示例](http://bibodeng.com/content/plugins/kl_album/upload/201311/96a79f2b7967bfd2a1b6e7766520f9972013110307335829475.png)

### 嵌入图片

我们的文档常常有一些图片要嵌入，以达到图文并茂的效果。特别是在一些论文中，以图形作为说明。latex具有强大的图形绘制能力，但是我们这里只介绍如何嵌入外来图片。
	
	% 同样是先包含包
	\usepackage{subfig}
	\usepackage{wrapfig}	% 图文包围的时候用到
	\usepackage{graphicx}
下面在上下文中嵌入一张图片：
	
	% 省略上文（此为注释）
	\begin{figure}[!htp]
	\centering
	\includegraphics[angle=10,
	width=0.7\textwidth]{pic/junxun.jpg}
	\caption{三连南僧激动地和对面二连拉歌}
	\end{figure}
	% 省略下文
效果如下：

![插入图片](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/f3333114456e25b0240818f67c08f3ce2013110307432017124.png)

`htp`是为了让图片不要落在边界，顶部等特殊地方，而是在正文中。`centering`死让图片居中，然后是最核心的`includegraphics`将图片包含进来，并且制定角度为10°，宽度为页面总宽度的70%，`caption`即为标题。然后注意要闭合嵌入的`figure`元素。
	
### 嵌入文字包围的图片

那如果要嵌入文字包围的图片，该怎么弄呢？我们要的效果是只在图片存在的地方，文字绕道，但是过了这个位置，则包围了文字。先看别人的[经典效果](http://www.ctex.org/documents/latex/graphics/node115.html)：

	\begin{wrapfigure}{r}{4.5cm}
	\includegraphics[width=4cm, clip]{pic/face.jpg}
	\end{wrapfigure} 
	\mbox{}我们的爱情，就像春天盛开的鲜花，无比热情。每当我见到你，就沉醉于其中，快乐无比。我就像那在浅浅柔波中的水草，享受着康桥的水的轻抚。

效果如下：
![图文混排](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/e46b2f87875b8674726d66673259641d2013110308225412500.png)
如果没有`\mbox{}`那么就会出现文字出现在图片上的效果。`wrapfigure`的效果就像是二者可以叠加，也可以互相排斥开来。

更多的latex代码块，还是看教程比较靠谱吧（比如那看起来很高级的数学公式）。

---
end