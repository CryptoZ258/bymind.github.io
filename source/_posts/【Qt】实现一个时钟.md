---
title: 【Qt】实现一个时钟
date: 2012-11-18 08:48:11
---
{% raw %}
<p><span style="font-family:'Microsoft YaHei';font-size:14px;">从前接触Qt都太马虎了，从来没有怎么动手去做一个程序，但是最近我摸索到一个学习的很重要的窍门就是要好好地看别人写的教程或者视频，有时候一本书讲的比较理论，而教程比较有连续性，更能掌握技能。学习有两点：一是学习的输入，另外一个是学习的时间。学习的输入若很纯正很强大，那么短时间的学习也能让你掌握不少东西。如果再加上长期的坚持的话，很可能会有比较强的功力。正儿八经地学习Qt，实现的第一个实例就是一个简单的时钟。</span></p>
<p><span style="font-family:'Microsoft YaHei';font-size:14px;"><br />
</span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">思路如下：</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">要实现一个时钟，就得用Qt的画笔在窗口中画出一个表盘，三个指针（时分秒）。首先选择比较合适的坐标，以方便绘图。我们选择窗口的正中（假设窗口是一个固定边长的正方形），这样那些表盘刻度以及指针的相对位置就好确定了。对于表盘，则用一个循环12次，每次先将坐标系顺时针旋转30度（360/12），然后绘制一条短线。而对于指针来说，则绘制一个多边形呈日常见到的指针模样，这样就需要确定四个点，然后绘制出来。</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;"><br />
</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">关键在于怎样让时钟能够动起来，而且能够准确地反映时间。我们则用一个定时器，在1秒时间间隔后触发一次窗口重绘事件，根据系统的时间，这样整个表盘和指针就重新绘制了，速度很快，所以我们基本上认为指针是在连续运转的。</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;"><br />
</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">下面是效果图：</span></span></p>
<p style="text-align:center;"><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;"><a target="_blank" href="/content/plugins/kl_album/upload/201211/4ff7b02bb5a881657342972ffa4493972012111801052625478.png"><img src="/content/plugins/kl_album/upload/201211/4ff7b02bb5a881657342972ffa4493972012111801052625478.png" width="284" height="286" alt="点击查看原图" border="0" /></a></span></span></p>
<p style="text-align:center;"><span style="font-family:''Microsoft YaHei'';"><br />
</span></p>
<p style="text-align:left;"><span style="font-family:''Microsoft YaHei'';">核心代码：</span></p>
<p style="text-align:left;"></p>
<pre class="brush:cpp; toolbar: true; auto-links: true;">Clock::Clock(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Clock)
{
    QTimer *timer = new QTimer(this);
    timer-&gt;start(1000);

    connect(timer,SIGNAL(timeout()), this, SLOT(update())); // 链接信号和槽

    ui-&gt;setupUi(this);
    resize(200,200);
    setMinimumSize( 200, 200 );
    setMaximumSize( 200, 200 );
}</pre><br />
<p></p>
<p style="text-align:left;"></p>
<pre class="brush:cpp; toolbar: true; auto-links: true;">void Clock::paintEvent(QPaintEvent *)
{
    QPainter painter(this);         // 在该窗口中创建一个画笔
    painter.setRenderHints(QPainter::Antialiasing);     // 去除锯齿
    /*painter.drawLine(QPoint(0,0),QPoint(100,100));*/
    painter.translate(100,100);

    QTime time = QTime::currentTime();      // 获取当前时间
    painter.setBrush(Qt::red);
    painter.setPen(Qt::red);
    painter.save();    // save the x y
    painter.rotate(6.0*time.second());
    painter.drawConvexPolygon(sec,4);   // 绘制一个多边形
    painter.restore();

    painter.setBrush(Qt::blue);
    painter.setPen(Qt::blue);
    painter.save();
    painter.rotate(6.0*(time.minute()+time.second()/60));
    painter.drawConvexPolygon(min,4);   // 绘制一个多边形
    painter.restore();

    painter.setBrush(Qt::black);
    painter.setPen(Qt::black);
    painter.save();
    painter.rotate(30*(time.hour()+time.minute()/60));
    painter.drawConvexPolygon(hour,4);   // 绘制一个多边形
    painter.restore();

    for(int i=0; i&lt;12; i++)                // 绘制表盘刻度
    {

        painter.drawLine(QPoint(0,-80),QPoint(0,-90));
        painter.rotate(30);
    }
}</pre><br />
<p></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">对于Qt来说，可以采用C++就编写出很棒的程序，在ubuntu下用Qt creator就可以很方便地写代码。下面是源程序的代码下载链接：</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;"><a href="http://vdisk.weibo.com/s/iiirc">点击下载Clock Qt源代码</a></span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;"><br />
</span></span></p>
<p><span style="font-family:''Microsoft YaHei'';"><span style="font-size:14px;line-height:21px;">by bibodeng &nbsp;2012-11-18</span></span></p>{% endraw %}
