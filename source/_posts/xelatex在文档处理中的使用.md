---
title: xelatex在文档处理中的使用
date: 2013-11-09 13:18:02
---
# xelatex在文档处理中的使用

by bibodeng 2013-11-09

## latex和pdflatex的问题

使用latex来直接编译，在有`\tableofcontent`的情况下会出现一些怪异的`unicode char \u8之`这样的错误，使得目录不完整。其原因是使用的`CJKutf8`的宏包所包含的utf8字符是不完整的，故而有些中文字符支持不完整。但是诡异的是同一个字符，在某些地方是ok的，在另外一些地方就是不行，可能是第一次编译输出的时候出错。如下的代码为`latex`文档：

    \documentclass[12pt,oneside]{book}
    \usepackage{CJKutf8}
    \usepackage[utf8]{inputenc}
    \usepackage[titletoc]{appendix}
    \usepackage{indentfirst}  % first paragraph indent
    \setlength{\parindent}{2em}
    \pagestyle{plain} % set the footer simple ,only a page number headings
    
    \begin{document}
    
    \begin{CJK*}{UTF8}{gkai} % gkai gbsn
    
    \protect\setcounter{tocdepth}{1}
    \tableofcontents  % 目录，二次编译
    
    \section{中国} % 含有中文字符，在生成tableofcontent的时候可能出错
    \begin{verbatim}
    我爱你中国   
    \end{verbatim}
    
    \end{CJK*}
    \end{document}

将会产生如下的错误：

![unicode没设置报错](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/ba66d70c572c38dc44f202b3b8752f812013110904382232028.png)

尝试过在`\end{CJK*}`之前以及文档结尾加`\newpage`,都没有效果，在`stack exchange`也没有找到合适的答案。后来发现`texlive`可以解决这个问题。而需要安装`texlive`工具包，然后使用这个新的发行版的引擎来编译文档，所以文档需要重写了。

## 安装和使用texlive

要安装texlive，必须要有安装的介质，所以需要下载文件等，然后予以安装，这里有一个教程可供[参考](http://seisman.info/texlive-2013-under-linux.html)。中文支持可以暂时不理，到后面我们会使用`ubuntu`系统自带的中文字体做编译。

安装好之后，就让我们看看其文档结构：

    \documentclass[12pt,a4paper]{article}
    \usepackage{fontspec,xunicode,xltxtra}
    \usepackage{titlesec}
    \usepackage[top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}
    
    \titleformat{\section}{\Large\hei}{\thesection}{1em}{}
    
    \XeTeXlinebreaklocale "zh"
    \XeTeXlinebreakskip = 0pt plus 1pt minus 0.1pt
    
    \newfontfamily\hei{WenQuanYi Micro Hei}  % 使用系统的中文字体
    \setmainfont{AR PL UKai CN}              % 这3行定义文档字体，本行正文
    \setmonofont{WenQuanYi Micro Hei}        % 标题等

    \begin{document}
    
    \title{\hei XeTeX使用小结}
    \author{\hei 小明}
    \date{\hei 2009年6月21日}
    
    \maketitle
    
    \section{简介}
    以前使用CJK进行中文的排版，需要自己生成字体库，近日，出现了XeTeX，可以比较好的解决中文字体问题，不需要额外生成LaTeX字体库，直接使用计算机系统里的字体。
    
    \section{字体列表}
    本文使用了大量本机自带的字体。
    
    \centering
    你好！
    
    \end{document}

可以看到我们的文档中使用了自己系统中的字体，而不是使用各种各样的字体宏包。我们可以使用命令：

    fc-list :lang=zh-cn
    
来查看系统中都有什么中文字体：
![fc-list命令结果](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/4901815145f36d1d475207eef5bb44b52013110904593212245.png)

我们要使用的是字体的名字，例如`WenQuanYi Micro Hei`和`AR PL UKai CN`,也就是两个冒号之间的那个名字。这样我们果然可以编译出漂亮的使用系统字体的文档了。再把之前latex的文档中的`preamble`（声明usepackage的地方）部分中的代码拷贝过来放到对应的`\begin{document}`之前就可以了。然后我们就可以运行 `xelatex article.tex`来编译文档了，编译后可以看到生成的pdf文件，不会再出现之前的目录错误了。

    % preamble示意
    \documentclass{class}
    … preamble部分
    \begin{document}
    … 正文内容 …
    \end{document}

目录正确显示效果:

![目录ok了](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/e711308f47cbe55a01abd951d4aa3e682013110905133112413.png)
## 使用latex生成各种尺寸的pdf

假如我们要生成适合`kindle`阅读的PDF 6吋版，那么在latex中将非常地方便。因为只需要在`preamble`中加入如下代码就ok了：

    \usepackage[paperwidth=9cm, paperheight=12cm, top=0.1cm, bottom=0.2cm, left=0.2cm, right=0.2cm]{geometry}
    \special{papersize=9cm,12cm}
    
而且这个尺寸可以随意更改。所以可以针对特定的屏幕大小进行编译。我编译的6吋版本效果如下：

![pdf六吋版本效果](http://www.bibodeng.com/content/plugins/kl_album/upload/201311/26bbead36d401f3407f6de55cac89ad42013110905101210145.png) 

## 小结

折腾那么久`tex`,现在才发现一个好的发行版有多么重要，这样让我们做的工作的轻松起来，而不是捉襟见肘地去解决那些对中文的支持问题。而我们也将使用这个工具，继续我们《IT小小鸟外传》的编写，竭尽全力地制作出良好阅读体验的电子书，并且生成各种版本以支持更多的设备。

---
end