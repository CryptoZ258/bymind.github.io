---
title: 【python】写一个统计代码行数的codeCounter
date: 2013-03-31 14:49:18
---
{% raw %}
<p><span style="font-size:16px;">某一天过去SY那儿，突发奇想说要写一个统计代码行数的小程序。说干就干，约定了一个时间——周六，来把这个想法给实现了。当然这个项目人家做过的也未必，google一下，果然有非常优秀的win下面的代码统计工具sourceCounter。当然我们是用python来写，确定了数据结构和算法之后，我们就开始实现了。</span></p>
<p><span style="font-size:16px;"><br />
</span></p>
<p><span style="font-size:16px;">我们要实现的是一个能够遍历指定的文件夹或文件，数出有多少行，然后好好将这个信息放到树的节点里面。总之，这是一个N叉树，N取决于该目录下面，有多少个子目录或子文件。我们使用列表list来模拟树型结构：</span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">parentDir</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">&nbsp; &nbsp; subDir<br />
</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">在数据结构里面就是 [{counter: co, name: parentDir}, [{couter:co2, name:subDir}[]]]。当然这是最简单的情况，复杂一点就是，很多层嵌套，视目录深度而决定。总之就是发现了一个文件或者目录，就递归地扩展下去。上代码：</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">def walk_dir(self,folder_tree, topdown=True):
		for root, dirs, files in os.walk(folder_tree[0]['name'], topdown):
			for name in files:
				if name[0] == '.':
					continue
				
				if self.my_pattern.match(name):
				
					path_name = os.path.join(root,name)
					if os.path.islink(path_name):
						continue
					# calculate the summry of the file
					count_result = self.count_code_of_file(path_name)
					# insert into the tree
					
					sub_folder_tree = [{'name':path_name,'counter': count_result},[]]
					folder_tree[1].append(sub_folder_tree)
					# sum
					folder_tree[0]['counter'] = folder_tree[0]['counter'] + count_result
				
			for name in dirs:
				if name[0] == '.':
					continue
				path_name = os.path.join(root,name)
				# print(path_name)
				sub_folder_tree = [{'name':path_name,'counter': 0},[]]
				folder_tree[1].append(sub_folder_tree)
				self.walk_dir(sub_folder_tree, topdown)
				# sum
				folder_tree[0]['counter'] = folder_tree[0]['counter'] + sub_folder_tree[0]['counter']
			return</pre><p><span style="font-size:small;"><span style="line-height:24px;">这就是整个算法的核心部分，用os.walk整个dir，得到一棵树。一开始我们提出了两种方案：一，先生成树，再统计代码，因为需要回填；二，在生成树的同时，计算出代码行数。SY很敏捷，一下自己想出直接在后面加上folder_tree[0]['counter'] = folder_tree[0]['counter'] + sub_folder_tree[0]['counter']. 也就是每次遍历完一棵子树，就更新父节点的counter数据。这其中使用了递归的原理。code complete里面说，递归不是用来求求阶乘和斐波那契数列的，而是需要使用在更有效的需要栈的地方，我想说，这里就是。其核心原理就是每一层，构造一个[{counter:co, name:na }[]], 插入到父节点的[]中，构造树的过程，也完成了有关的计算。</span></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">接下来就是实现驱动脚手架了（一些数据输入和函数调用），然后实现打印模块，打印模块，需要表现缩进，故而有一个参数是tabs次数。具体实现如下：</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">def print_tree(self,folder_tree, tabs = 0,topdown=True):
		if os.path.isdir(folder_tree[0]['name']):
			print ' '
			print '   '*tabs,'+',folder_tree[0]['name'] , ' : ' ,folder_tree[0]['counter']
			
		else:
			file_name = os.path.split(folder_tree[0]['name'])
			print '   '*tabs,'+',file_name[1], ' : ' ,folder_tree[0]['counter']
			return
		if folder_tree[1]:
			
			for sub_tree in folder_tree[1]:
				self.print_tree(sub_tree,tabs +1)
		else:
			return</pre><p><span style="font-size:small;"><span style="line-height:24px;">一切就是这么简单，然后就定义一下有哪些文件类型了，这个可以用正则表达式来完成：</span></span></p>
<p></p>
<pre class="brush:python; toolbar: true; auto-links: true;">my_pattern = re.compile(r'[a-zA-Z1-9]+.(py|c|java|php|cpp|css|html|xml|htm|js|cs|h|asm|sh|ruby|perl)$')</pre><p><span style="font-size:small;"><span style="line-height:24px;">很显然是普通文件名，如果要加入下划线则在把字符串改成‘</span></span><span style="line-height:24px;">[a-zA-Z1-9]+[a-zA-Z1-9_.]* .(py|c|java省略</span><span style="line-height:24px;font-size:medium;">’。</span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">最后，如果想要把树打印到文件里面也是可以的，之需要在print前面加上&gt;&gt;log_file变成 print &gt;&gt;log_file。总体代码不超过100行。当然使用linux下面的shell一句就能搞定：</span></span></p>
<p></p>
<pre class="brush:shell; toolbar: true; auto-links: true;">find /a -name "*.c" |xargs cat|grep -v ^$|wc -l</pre><p><span style="font-size:small;"><span style="line-height:24px;">当然这其实是linux应用程序的组合使用，grep等等强大的工具，表示还没有到那个神级别。好吧，窗外的雨下个不停，可是我的手指敲击键盘的声音，却要渐渐停息了。</span></span></p>
<p><span style="font-size:14px;">github : <a href="https://github.com/bibodeng/pyCodeCounter/blob/master/codeCounter.py">pyCodeCounter代码[daoluan-bibodeng]</a></span></p>
<p><span style="font-size:small;"><span style="line-height:24px;">by bibodeng 2013-3-31</span></span></p>
<p></p>
<p></p>
<p></p>
<p></p>{% endraw %}
