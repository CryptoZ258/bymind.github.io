---
title: 使用Nginx+uWSGI+Supervisor部署Flask应用
date: 2016-10-12 15:20:01
---
# 使用Nginx+uWSGI+Supervisor部署Flask应用

## 前言
许多团队使用的是Nginx和uWSGI的方式来部署Python网页应用，ViaBTC的站点采用的是简单高性能的Flask开发的，那么究竟怎么才能让Flask开发的网站能够正确部署到Nginx中呢，刚好，bibo接手了网站应用的开发，刚好通过这次实验介绍一下这个步骤。

先简单介绍一下这些工具：

* Nginx ——高效的web服务器
* uWSGI ——WebServiceGatewayInterface的一种实现，是Web服务器到Python应用的桥梁
* Supervisor ——一款强大的进程监控管理工具，它能够启动uWSGI

## 准备和安装

我们将会以[Flaskr-demo](http://docs.jinkan.org/docs/flask/tutorial/index.html)  为例子，将它作为一个Web服务启动起来，让它的页面能够被用户访问。假设你已经有了服务器，首先要安装Python环境，我们推荐Virtual env，它能够提供一个虚拟的Python运行环境，要使用什么Python包都得在venv模式下安装，对应这个Python运行版本，组件一套软件包，从而保证在这个环境下应用可以独立运行，避免了在全局安装使用同一个Python版本，那样会造成混乱和各软件包不兼容。

	// 安装准备工具
	sudo apt-get install python-setuptools
	sudo easy_install pip
	sudo pip install virtualenv

	// 安装python
	sudo add-apt-repository ppa:nginx/stable
	sudo apt-get update &amp;&amp; sudo apt-get upgrade
	sudo apt-get install build-essential python python-dev

接下来安装并启动Nginx：


        sudo apt-get install nginx
        sudo service nginx start


`nginx`安装好之后，我们可以通过访问web服务器来验证是否安装正确，这个时候应该能看到Nginx的欢迎页：


        curl http://localhost


## 实现功能

假如你的代码已经实现好了，只要拷贝到 `/var/www/` 目录下并修改目录权限，程序对脚本要有读和执行权限，如果没有这个目录，通过`mkdir`命令建立一个即可，这里我们从0开始实现Flasker这个例子，然后将它启动起来。Nginx为我们提供了一个托管静态页面的站点，但是它不能直接运行Python代码，所以应由uWSGI和Nginx配合共同呈现动态的页面。

可以参考Flask的文档逐步实现，实现好之后的目录如下，其中`flaskr.py`是整个程序的代码，我们可以尝试运行一下这个demo，将会提示已经在 `http://127.0.0.1:5000`  调试运行了，访问这个网址将会呈现出它的页面。但是这并不是我们要的，我们需要让它运行在Web服务器上，并提供给所有人访问。

        |---------flaskr/---------
	|--static/
	|--templates/
	|--__init__.py
	|--flaskr.py
	|--schema.sql


运行调试模式`python flaskr.py`将显示下面提示：

	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	* Restarting with stat
	* Debugger is active!


##配置Nginx

下面使用uWSGI和Nginx配合，让uWSGI执行Python程序，并将结果输出到Nginx服务器，它们将通过一个socket进行通信，首先，要安装uWSGI：


        sudo pip install uwsgi


我们在项目目录下建立一个`config`目录，并新建一个配置文件 `demo_nginx.conf` 来配置nginx，当然我们

        server {
	    listen 80;
	    server_name demo.viabtc.com;
	 
	    location /static/ {
	        alias /var/www/flask_demo/app/static/;
	    }  
	 
	    location / {
	        include uwsgi_params;
	        uwsgi_pass unix:/tmp/demo.uwsgi.sock;
	        uwsgi_param UWSGI_PYHOME /var/www/flask_demo/venv;
	        uwsgi_param UWSGI_CHDIR /var/www/flask_demo;
	        uwsgi_param UWSGI_SCRIPT run:app;
	        uwsgi_read_timeout 100;
	    }  
	}

以上配置表示服务器监听 `demo.viabtc.com:80`，并配置了 static 目录的位置，当然你也可以配置其它自己添加的目录，还可以看到uwsgi和Nginx是通过 /tmp/demo.uwsgi.sock 这个文件来进行转接的，也即当Nginx接收到请求后，将请求传递到 demo.uwsgi.sock，由uwsgi去处理。

此外，由于uWSGI不会像`python flaskr.py`这样以`__main__`的名义运行程序，故而我们配置了运行入口是`run:app`，也即我们定义了一个`run`模块（即`run.py`文件），运行的时候`app context`就是`run`模块的`app`。

        #!/usr/bin/python
	# -*- coding: utf-8 -*-

	'''run.py is simple'''
	from flaskr import app as application
	app = application           

别忘了脚本都要赋予执行权限：


        sudo chmod +x run.py


然后将该`demo_nginx.conf`配置文件链接到Nginx的配置文件包含目录`/etc/nginx/conf.d/`下，并重启Nginx查看效果：


        sudo ln -s /var/www/demoapp/demoapp_nginx.conf /etc/nginx/conf.d/
        sudo service nginx restart


下面在客户端机器中配置你的访问hosts，例如我的是：


        112.74.164.155 bibo.viabtc.com


访问服务器站点 `demo.viabtc.com`，会发现报了502 BadGateway错误，那是因为我们没有配置uWSGI，所以在Gateway这个环节出错了，我们下面直接通过Supervisor来启动uWSGI解决这个问题。

## 配置Supervisor并运行uWSGI

首先，要安装Supervisor，安装Supervisord（服务端），会自动配套安装Supervisorctl（客户端），Supervisord负责控制那些需要托管的进程。

        sudo apt-get install supervisor

安装完成后，我们可以查看Supervisor的配置文件 `/etc/supervisor/supervisor.conf`，一般无需改动全局配置文件，但是对于supervisor的包含配置文件，也即运行时需要查找的应用配置，放在`/etc/supervisor/conf.d`，和Nginx是类似的，我们也需要在这个目录下添加站点的配置文件，我们同样使用链接的方式。

在项目文件夹的`config/`目录下新建一个`demo-uwsgi.conf`文件，内容是app的配置：

        [program:demo_uwsgi]
	command         = uwsgi -w run:app --master --processes 4 --socket /tmp/demo.uwsgi.sock --chmod-socket=777
	directory       = /var/www/flask_demo
	autostart       = true
	autorestart     = true
	stdout_logfile  = /var/log/uwsgi.demo_web.log
	redirect_stderr = true
	stopsignal      = INT 

其实Supervisord就是运行了这样一个命令将uWSGI启动起来了，并且指定了日志输出等配置，我们通过软链接方式将这个配置文件放到`/etc/supervisor/conf.d`，然后启动Supervisord，并启动我们站点：

	sudo ln -s /var/www/demoapp/demoapp_nginx.conf /etc/nginx/conf.d/
	sudo service supervisord start
	sudo supervisorctl start demo_uwsgi


这个时候项目的整体目录看起来像下面这样：

        |---------flaskr/---------
	|--config/
	|--|--demo_nginx.conf
	|--|--demo_uwsgi.conf
	|--static/
	|--templates/
	|--flaskr.py
	|--run.py
	|--schema.sql
	|--venv/

这个时候再次访问`demo.viabtc.com`应该就可以正常访问了，不再出现502错误，以后将要新建一个站点的时候我们可以按照上面的方法依法炮制，只需要重新定义一套`**_nginx.conf` 和 `**_uwsgi.conf` 并放到对应的地方即可。如果碰到问题，不妨先查看一下Nginx和Supervisor及uWSGI的日志，日志地址就是上面配置文件中我们定义的。

bibodeng 2016-10-12