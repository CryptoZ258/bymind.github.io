---
title: 从装配线到DNA比对——神器动态规划
date: 2012-04-24 08:08:11
---
{% raw %}
<div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">【前言】</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">对于一个问题，我们如果可以枚举所有的解，那么这个解空间我们是知道的。那么如何在解空间里面找到最优解呢？这时有一个非常好的方法，从底向上地构造整个解，而每一步都是从地层寻求最优解，这样就能保证在最终得到的一定是最优解。这就是最优子结构，有这种结构的问题，通常都可以用动态规划的办法来寻求最优解。而且它是从小规模（子问题）到大规模问题的构造，而常常这样的解法能够用一张表直观地表现出来。表中的元素是一个表达式的某个特定值，这个表达式表现的是问题和子问题的关系，也就是如何在子问题中的解中寻找最优的关系，这样的关系在例子中会非常地明了。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">【装配流水线】</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;&#39;, &#39;microsoft yahei&#39;, &#39;&#39;"><span style="font-size:14px">&nbsp;</span></span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">往往最经典的算法书里面都会讲最经典的“装配流水线”问题。因为它相对来说比较简单，一个问题，只有两个个子问题，那就是两条流水线选哪条路径。即使是最简单的例子也会有一大通的表达式搞得头有点晕，不过多看几遍应该是可以克服的。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">假设一个工厂有两条装配线：装配线0&nbsp;和&nbsp;装配线1&nbsp;，这两个装配线中有相同数量的装配站用于装配元件。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">可以用下面的图表示两个装配站：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">可以用S</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i,j&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">表示第i条装配线（i&nbsp;为0或1）的第j个装配站。从一个装配线转移到另一个装配线的下一站需要消耗时间T</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i,j</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">,例如从第一条线的第一站到第二条线的下一站（即第二站）所用的时间为T</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1,1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">。表明是从一线一站出发，而不用标记下一站是几，因为下一战一定是另一条线的j+1站。我们可以选择第一条线还是第二条线，来使得最终出线的时候，用时最短。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">可能用语言表达很混乱，那么就用图像说明一下这些符号吧：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;<a href="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/234bfc7a97210c63f4c59cafe1cb98bc201204211514312340.jpg" target="_blank"><img src="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/234bfc7a97210c63f4c59cafe1cb98bc201204211514312340.jpg" alt="点击查看原图" width="480" height="360" border="0" /></a></span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px"><span style="color:#009900">对于动态规划的解法，有一个可以遵循的套路</span>：</span></div><ol style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><li><p><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">理清楚是怎样获得最短用时的（最优解），这里是两条线，可以选择，要求最后用时最短</span></p></li><li><p><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">用递归来表示解的通式</span></p></li><li><p><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">计算（比较）得到最短时间（如何从两条线中选取）</span></p></li><li><p><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">回溯得到这条路径</span></p></li></ol><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">什么也不说了，先找出最重要的递归式，然后填表：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">最短用时&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">=&nbsp;min(F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[n])+x1,&nbsp;F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[n]+x2)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x0,x1&nbsp;表示最后一站到终点用时，F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[n]表示第i条线的第n站。&nbsp;比较最终谁用时最短</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j]&nbsp;=&nbsp;&nbsp;min(F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j-1]+a</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0,j&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j-1]&nbsp;+&nbsp;t</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1,j-1&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">+&nbsp;a</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0,j</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;表示到1线j站的最短时间是上一站是一线直接过来的，要么就是二线转移过来的，转移的时候付出的代价是t</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1,j-1。</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">对于二线的时候是一样的</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j]&nbsp;=&nbsp;&nbsp;min(F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j-1]+a</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1,j&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j-1]&nbsp;+&nbsp;t</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">0,j-1&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">+&nbsp;a</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1,j</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-----------------------------1</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">而F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[j]&nbsp;比较特殊，因为一开始只能从一条路径进入，用时为e</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">(i&nbsp;为0或1)</span></div><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">F</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">[0]&nbsp;=&nbsp;e</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i&nbsp;</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">+&nbsp;a</span><sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">i,0</span></sub><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-----------------------------2</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">在这里，我直接将ei也计入了第0个站中，因为进站和出站是不能换线的。</span></p><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">这样1式和2式，共同表达了一个递归关系，其含义也不难理解。</span><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">下面用底向上方法构造一条路径，动态规划很多时候是先用某种方法求得那种是最好的，再回溯把该路径求出来。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">先给出填表算法：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;&#39;, &#39;microsoft yahei&#39;, &#39;&#39;"><span style="font-family:&#39;&#39;, &#39;microsoft yahei&#39;, &#39;&#39;"><span style="font-size:14px">&nbsp;</span></span></span><pre class="brush:cpp; toolbar:true; auto-links:false;">void findWay(int *a[],int *t[],int *line[],int &amp;finalLine,int n) //n 个站点
{
	int **f = new int*[2];
	for(int k=0;k&lt;2;k++)//总共有两条流水线，流水线0 和流水线 1
	{
		f[k] = new int[n];
	}
	f[0][0] = a[0][0];  
	f[1][0] = a[1][0];  

	for(int i=1;i&lt;n;i++)   //从站点1开始到第n-1个站点
	{
		if(f[0][i-1]+a[0][i] &lt;= f[1][i-1]+t[1][i-1] + a[0][i] )                //line zero	其实可以去掉共同部分a[0][i]
		{
			f[0][i] = f[0][i-1] + a[0][i];   
			line[0][i] = 0;
		}
		else
		{
			f[0][i] = f[1][i-1] + t[1][i-1] + a[0][i];
			line[0][i] = 1;
		}


		if(f[1][i-1] + a[1][i] &lt;= f[0][i-1] + t[0][i-1] + a[1][i])			//line one
		{
			f[1][i] = f[1][i-1] + a[1][i] ;
			line[1][i] = 1;
		}
		else
		{
			f[1][i] = f[0][i-1] + t[0][i-1] + a[1][i];
			line[1][i] = 0;
		}
	}

	if(f[0][n-1] &lt;=  f[1][n-1])
	{
		finalLine = 0; 
	}
	else
	{
		 finalLine = 1;
	}
}</pre></div><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">然后再给出递归调用的回溯（利用填表的过程中记录的路径），得到顺序的解：</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">void printStations(int *line[],int finalLine,int n)   //递归输出经过的站点
{
	int i = finalLine;
	int j = n-1;
	if(j&gt;0)
	printStations(line,line[i][j],j);    //递归产生顺序路径

	cout &lt;&lt;"装配线"&lt;&lt; i &lt;&lt; "装配站"&lt;&lt;j&lt;&lt;endl;
}</pre><p>&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">假设有一个用例数据如上面的图片所示。则调用主函数</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">void main()
{
	int n = 0;
	int k = 0;			//k and g用于循环子
	int g = 0; 
	int e0 =0;			//enter
	int e1 =0;
	int x0 = 0;		//exit
	int x1 = 0;
	cout &lt;&lt;"总共有2条相同站点的装配线，请输入装配线的站点数 ： "&lt;&lt;endl;
	cin&gt;&gt; n;       

	cout &lt;&lt;"请输入进入装配线0,1的时间花费： "&lt;&lt;endl;
	cin&gt;&gt; e0 &gt;&gt; e1;     

	cout &lt;&lt;"请输入退出装配线0,1的时间花费： "&lt;&lt;endl;
	cin&gt;&gt; x0 &gt;&gt; x1;    
	
	int **a = new int*[2];      //站点花费时间
   int **t = new int*[2];       //换线花费时间
	int **line = new int*[2];   //记录路线轨迹

	for(k=0;k&lt;2;k++)			//总共有两条流水线，流水线0 和流水线 1
	{
		a[k]  = new int[n];        //n个站点的流水线
		t[k] = new int[n];			//n个站点之间的交叉路线花费时间——换线时间
		line[k] = new int[n];		 //用于记录路径
	}
		

	//------------------------------------装配时间----------------------------------------
	cout &lt;&lt;"请输入进入站点以及在站点内装配的时间"&lt;&lt;endl;
	for( k=0;k&lt;2;k++)
	{
		for(g=0;g&lt;n;g++)
		{
			cout &lt;&lt;"\n输入装配线"&lt;&lt;k&lt;&lt;"的第"&lt;&lt;g&lt;&lt;"个站点所花费的时间 : ";
			cin &gt;&gt; a[k][g];
		}
	}
	a[0][0] += e0;			//将进入时间花费和第0号站点绑定
	a[0][n-1] += x0;		//将出线时间花费和第n-1号站点绑定 今后不用计算
	a[1][0] += e1;
	a[1][n-1] +=x1;   

	//------------------------------换线时间------------------------------------------------
   for( k=0;k&lt;2;k++)
	{
		for(g=0;g&lt;n-1;g++)
		{
			cout &lt;&lt;"\n输入装配线"&lt;&lt;k&lt;&lt;"的"&lt;&lt;g&lt;&lt;"站到另一条线的"&lt;&lt;g+1&lt;&lt;"站点所花费的时间 : ";
			cin &gt;&gt; t[k][g];
		}
	}
   cout &lt;&lt; endl;

   int finalLine = 0;  //初始化
   findWay(a,t,line,finalLine,n);  //动态规划查找路径
   printStations(line,finalLine,n);  //打印路径
   system("pause");
}</pre><p>&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">那么结果是</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><img id="WizImageID" src="../admin/ueditor/themes/default/images/spacer.gif" align="middle" border="0" word_img="file:///C:/Users/bibodeng/AppData/Local/Temp/Wiz/c9a1fbb9-a25c-446a-a2ea-5972c6480774_1_files/13888031.png" style="background:url(../admin/ueditor/themes/default/images/localimage.png) no-repeat center center;border:1px solid #ddd" /></p><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span><img id="WizImageID" src="../admin/ueditor/themes/default/images/spacer.gif" align="middle" border="0" word_img="file:///C:/Users/bibodeng/AppData/Local/Temp/Wiz/c9a1fbb9-a25c-446a-a2ea-5972c6480774_0_files/13888031.png" style="background:url(../admin/ueditor/themes/default/images/localimage.png) no-repeat center center;border:1px solid #ddd" /><a href="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/4548ab6b8b99ab3fba033f1566146ea2201204211516393213.png" target="_blank"><img src="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/4548ab6b8b99ab3fba033f1566146ea2201204211516393213.png" alt="点击查看原图" width="379" height="121" border="0" /></a></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">【装配线的小结】</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">装配线问题的解空间比较小，故算法比较快就完成了求用时最少的路径。重要的是求解的过程有一个套路。那就是求递归表达式——&gt;根据递归式填表——&gt;回溯求得解路径。接下来就过渡到一个比较难一点的问题——DNA序列检测，就原理上来讲是万变不离其宗。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">【DNA序列比对】</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">由于DNA序列十分庞大，故而需要非常大的内存空间来存储这个字符串，然而真正能用的软件是不可能无节制地使用内存，用来比对相对较短的序列还行。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">要比对DNA的相似度最大的子串，则必须要有一种机制来评价怎样最大，因而选取一种计分的方法来评定两个字符串的相似度，越相似的得分越高。具体的评分标准是这样的，至于为什么是这样很有必要思考一下：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">1、匹配一个得5分</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">2、不匹配一个扣1分</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">3、无法匹配（需要插入空格）扣掉2分&nbsp;&nbsp;&nbsp;</span></div><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;<a href="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/b4db723a36ec8a06e618abdb54ea2acc201204211525423667.png" target="_blank"><img src="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/b4db723a36ec8a06e618abdb54ea2acc201204211525423667.png" alt="点击查看原图" width="480" height="246" border="0" /></a></span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-size:14px;font-family:&#39;microsoft yahei&#39;">其递归意义就是在三种情况中选最大值，max&nbsp;应该在大括号前面，这里图片没有画好。</span></p><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">比较难理解的是无法匹配的情况，举个例子就比较好说明了</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">假如有一个DNA串为&nbsp;GTAC</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">而另外一个字符串为&nbsp;&nbsp;GAC</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">显然一一对应的时候（最后插入一个空格）得分是不高的，只有1分</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">而在第二个字符的前面插入一个空格，得到G_AC&nbsp;这样得分为13分，高吧？</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">所以，就要考虑在哪里插入空格的复杂问题。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">为了想清楚这个问题，还是用填表的方法比较直观发现问题。</span><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">我们每次比对总是选取一个得分最高的方案，这个方案可能是串S1插入一个空格，或者是S2插入一个空格，或者进行比匹配了，或者进行比对不匹配。对于那些长度不想等的两个字符串，总要填入&nbsp;|s1.length()&nbsp;-&nbsp;s2.length()|个空格。于是先将第0行和第0列填成&nbsp;-2&nbsp;*&nbsp;i&nbsp;和&nbsp;-2*j&nbsp;(这里i和j分别对于行和列的索引)。</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">这样，每次计算要求a[i-1][j-1],a[i-1][j],a[i][j-1]这三个元素要先填好。于是我们就用从i=1，j=1&nbsp;一行行填的办法可以满足这个条件。最终能够得到这样一幅图：</span></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><img src="../admin/ueditor/themes/default/images/spacer.gif" border="0" word_img="file:///C:/Users/bibodeng/AppData/Local/Temp/Wiz/8725437.png" style="background:url(../admin/ueditor/themes/default/images/localimage.png) no-repeat center center;border:1px solid #ddd" /></div><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;<a href="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/0c159b34f779c5628240a3058f949a902012042115203932322.png" target="_blank"><img src="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/0c159b34f779c5628240a3058f949a902012042115203932322.png" alt="点击查看原图" width="424" height="312" border="0" /></a></span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">void dynamic_programming(int *a[],const string &amp;s1,const string &amp;s2)
{
	//initial the array 
	for(unsigned int k=0;k&lt;=s1.length();k++)//the first colunm
	{
		a[k][0] = INDEL*k;
	}
	for(unsigned int g=0;g&lt;=s2.length();g++)
	{
		a[0][g] = INDEL*g;
	}
	//next step: fill the table
	for(unsigned int i=1;i&lt;=s1.length();i++)//row
	{
		for(unsigned int j=1;j&lt;=s2.length();j++)//col
		{
			int tmp1 = 0;
			int tmp2 = 0;
			int tmp3 = 0;
			tmp1 = a[i-1][j-1] + isMatch(s1[i-1],s2[j-1]);
			tmp2 = a[i-1][j] + INDEL;
			tmp3 = a[i][j-1] + INDEL; 
			a[i][j] = max(tmp1,tmp2,tmp3);
		}
	}

	for(unsigned int r=0;r&lt;=s1.length();r++)//row
	{
		for(unsigned int s=0;s&lt;=s2.length();s++)//col
		{
				cout &lt;&lt;setw(4)&lt;&lt; a[r][s] ;
		}
		cout &lt;&lt; endl;
	}
}

int max(const int &amp;a,const int &amp;b,const int &amp;c)
{
	if(a &gt; b)
	{
		if(a &gt; c)
			return a;
		else
			return c;
	}
	else // a&lt;b
	{
		if(b &gt; c)
			return b;
		else
			 return c;
	}
}</pre><pre class="brush:cpp; toolbar:true; auto-links:true;">int isMatch(char ch1,char ch2)
{
	if(ch1 == ch2)
		return MATCH;
	else 
		return MISMATCH;
}</pre><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;其中用到了一个求三个数的最大值的子函数</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">接下来就回溯，一一检测递归表达式中的三种情况，然后在结果中进行相应的操作.</span><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">如果匹配或者不匹配，放入结果串中。</span><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">如果需要插入空格，则插入空格，另外一个插入对应的S1[i]或者S2[j],因为是从对角线上找，所以一定是三种情况有且仅有一种。但是注意特殊情况，当到了i&nbsp;=&nbsp;0&nbsp;或者j=0&nbsp;的时候，也就是说到了第零行或者第零列的时候，优先考虑遍历完所有两条DNA串，而不是插入空格。例如，在蓝色线上的3，虽然不匹配，但是a[1][0]那里刚好是3&nbsp;+&nbsp;5&nbsp;=&nbsp;-2，造成了误解。所以我们的计分方法也是可以商榷的。这里的解决办法是INDEL（插入空格）优先。</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px"><a href="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/76945ab3a2c9961f9edaf89ab56434802012042115215714707.png" target="_blank"><img src="http://bibodeng.web-149.com/content/plugins/kl_album/upload/201204/76945ab3a2c9961f9edaf89ab56434802012042115215714707.png" alt="点击查看原图" width="340" height="249" border="0" /></a><br /></span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">所有代码如下：</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">void trace_back(int *a[],const string &amp;s1,const string &amp;s2)
{
	vector &lt;char&gt; ans1;
	vector &lt;char&gt; ans2;
	ans1.push_back(' ');
	ans2.push_back(' ');
	for(int i=s1.length(),j = s2.length();i&gt;0;)
	{
		
		 if(a[i][j] == a[i-1][j] + INDEL)
		{
			ans2.push_back('-');
			ans1.push_back(s1[i-1]);
			i--;
		}
		else if(a[i][j] == a[i][j-1] + INDEL)
		{
			ans1.push_back('-');
			ans2.push_back(s2[j-1]);
			j--;
		}
		else if(a[i][j] == a[i-1][j-1] + MATCH || a[i][j] == a[i-1][j-1]+MISMATCH) //这三个if else 语句，这条不能放到最先
		{ 
			ans1.push_back(s1[i-1]);
			ans2.push_back(s2[j-1]);
			i--;
			j--;
		}
	}

	cout &lt;&lt; endl;
	for(unsigned int i=ans1.size()-1 ;i&gt;0;i--)
		cout &lt;&lt; ans1.at(i);
	cout &lt;&lt;endl&lt;&lt; endl;
	for(unsigned int j=ans2.size()-1;j&gt;0;j--)
		cout &lt;&lt; ans2.at(j);
	cout &lt;&lt; endl;

	//finally print out the string
}</pre><p>&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">主函数很简单，产生两个待传入的参数即可：</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">#define INDEL -2    //insert an blank
#define MISMATCH -1  
#define MATCH  5

int main()
{
	string s2 ="AGTCCCC";
	string s1 ="ACGTATCC";
	//string s2 ="ACCGTGTCATGGGTCCACTTT";
	//string s1 ="ACAATGTTGGGTCGCTAT";
	/*string s1,s2;
	cin &gt;&gt; s1;
	cin &gt;&gt; s2;*/

	//apply a two degree matrix
	int **a = new int *[s1.length()+1]; //行			额外多一个空格
	for(unsigned int g=0;g&lt;s1.length()+1;g++)
		a[g] = new int[s2.length()+1];	//列		额外多一个空格

	//call the function to compute the score
	dynamic_programming(a, s1, s2); 
	trace_back(a, s1, s2);

	system("pause");
	return 0;
}</pre><p>&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><pre class="brush:cpp; toolbar:true; auto-links:true;">如果传入的两个字符串是</pre><pre class="brush:cpp; toolbar:true; auto-links:true;"><span style="font-size:14px"><span style="color:#009900">//string&nbsp;s2&nbsp;=&quot;ACCGTGTCATGGGTCCACTTT&quot;;</span></span></pre><p style="margin:5px 0px;"><span style="font-size:14px;color:#009900">//string&nbsp;s1&nbsp;=&quot;ACAATGTTGGGTCGCTAT&quot;;</span></p><p style="margin:5px 0px;"><span style="font-size:14px">那么可以获得这样的解：</span></p><p style="margin:5px 0px;"><span style="font-size:14px;color:#003399">ACAATGT--TGGGTCG-CTAT</span></p><p style="margin:5px 0px;"><span style="font-size:14px;color:#003399">ACCGTGTCATGGGTCCACTTT</span></p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><p style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;margin:5px 0px;">&nbsp;</p><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><p style="margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">【小结】</span></p><p style="margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">动态规划算法复杂度是O(N<sup>2)，</sup>从装配线到DNA序列比对，动态规划算法都表现得十分完美，总是返回给我们一个最优的解。而我们也不得不佩服算法的伟大，在现实的生活中无处不在，改变着我们的世界。动态规划算法是一项高级技术，很多书本上还有许多例子，如子串问题，矩阵连乘等问题（矩阵的运算是计算机都不能承受之重，能减少一点负担是一点）。在我看来，动态规划最重要的还是找到递归式子，找准问题和子问题的关系。找到之后就能填表了，表填好了就可以回溯得到解了。</span></p><p style="margin:5px 0px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">&nbsp;</span></p></div><div style="font-family:&#39;sans serif&#39;, tahoma, verdana, helvetica;font-size:12px;line-height:18px;"><span style="font-family:&#39;microsoft yahei&#39;;font-size:14px">by&nbsp;bibodeng&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2012-04-21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;原载于&nbsp;<a href="http://bibodeng.web-149.com/">bibodeng&nbsp;think&nbsp;beyond</a></span></div>{% endraw %}
