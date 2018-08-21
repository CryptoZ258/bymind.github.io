---
title: Ubuntu环境下迁移MySQL硬盘数据
date: 2016-12-13 08:11:49
---
Linux的文件系统可谓是非常地直观，一切设备挂载之后，都是一个文件，如果说我们的机器硬盘容量不够了，给扩充了一个硬盘，那么如何将MySQL中的数据库安全迁移到新的磁盘上呢？其实借用Linux的软链接方式只需要简单的几步，就可以将数据移动到新磁盘，但却对程序透明，从而做到无感扩容。

##挂载硬盘并格式化
将硬盘安装到电脑上，或者是在购买了云服务器的硬盘，那么接下来就应该将它挂载在系统的某个位置，才能开始存储文件。进入终端命令行，运行fdisk -l 查看数据盘的情况，这个时候应该会发现你新安装了一个硬盘，假设是叫 /dev/xvdb，那么按照流程给该分区进行预分区：

运行 fdisk /dev/xvdb，对数据盘进行分区。根据提示，依次输入 n，p，1，两次回车，wq，分区就开始了。
![fdisk-1](http://www.bibodeng.com/content/plugins/kl_album/upload/201612/731d985b71f8dcf2a8f4d57695598880201612130820405175.jpg)

运行 fdisk -l 命令，查看新的分区。新分区 xvdb1 已经创建好。如下面示例中的/dev/xvdb1。
![fdisk-2](http://www.bibodeng.com/content/plugins/kl_album/upload/201612/ea62804573b7725e76470d8b3d93f56e201612130820397478.jpg)

运行 mkfs.ext3 /dev/xvdb1，对新分区进行格式化。格式化所需时间取决于数据盘大小。建议采用更新的ext4，一般较新的Ubuntu都支持ext4了。
![fdisk-3](http://www.bibodeng.com/content/plugins/kl_album/upload/201612/085f42e7273041c42bb3f7ae8973ef6d2016121308203916081.jpg)

 运行 echo /dev/xvdb1 /mnt ext3 defaults 0 0 &gt;&gt; /etc/fstab 写入新分区信息。完成后，可以使用 cat /etc/fstab 命令查看。运行 mount /dev/xvdb1 /mnt 挂载新分区，然后执行 df -h 查看分区。如果出现数据盘信息，说明挂载成功，可以使用新分区了。

##转移数据
假设现在我们要将mysql的数据库内容，即/var/lib/mysql/下的内容迁移到/mnt/mysql/目录下

先停止mysql

    service mysql stop

移动数据:
安全起见先使用cp，完成之后再将/var/lib/mysql/原本删除

    cp -rf /var/lib/mysql/* /mnt/mysql/
    chown mysql:mysql /mnt/mysql

删除/var/lib/mysql/目录

    rm -rf /var/lib/mysql/

创建软连接:

    ln -s /mnt/mysql/ /var/lib/mysql/

##配置工作
这个时候，尝试启动mysql

    service mysql start

如果存在报错的情况，很可能是迁移之后数据库程序没有权限访问新的文件夹了，具体的报错原因可以找`/var/log/mysql/error.log`，如果真的是：

    InnoDB: The error means mysqld does not have the access rights to the directory.

则说明真的是没有权限，需要我们人工配置一下，编辑mysql的一个配置文件：

    vim /etc/apparmor.d/usr.sbin.mysqld

在配置文件中/var/lib/mysql/** rwk 下方添加两行：

    /mnt/mysql/** rwk,
    /mnt/mysql/  r,

授予程序新目录的访问权限。再次启动mysql，即可看到成功信息：

    service mysql start

后面即可连接mysql进行数据库操作了：

    mysql -uuser -p