---
title: 本地安装NuGet包
date: 2015-07-01 10:56:02
---
#本地安装NuGet包

由于内部开发时使用的是开发域的网络，Visual Studio中的包管理器无法通过网络访问NuGet仓库，故而我们需要想办法来通过下载到包，然后手动安装到我们的项目中。

##第一步 下载NuGet包

可以通过NuGet网站 `https://www.nuget.org/` 来查找要安装的包，记住包名PackageId。


    https://www.nuget.org/api/v2/package/{packageId}/{version}


以包 `Microsoft.AspNet.WebApi` 为例，下面通过链接来下载该包的5.2.3版本，在浏览器中输入


    https://www.nuget.org/api/v2/package/Microsoft.AspNet.WebApi/5.2.3


将下载到的NuGet包拷贝到开发机中的本地硬盘某个位置。

##第二步 安装NuGet包

要安装NuGet包，需要在项目中打开NuGet Manager, 选中项目，右键点击菜单，选中Manage NuGet Package，然后点击 Setting进入到设置界面， 配置添加一个源到Package Source中，待会在安装中即可选择这个本地源了。

![Manage NuGet Package界面](http://www.bibodeng.com/content/plugins/kl_album/upload/201507/216964db532c1a9231695eed0bac46c5201507011058361414530903.png)


Manage NuGet Package界面

![添加本地源](http://www.bibodeng.com/content/plugins/kl_album/upload/201507/6e85d7818d8da83fd4f6cba85313c94c201507011058361170095749.png)

添加本地源

添加完本地源后，例子中我们添加了一个localNuGet，地址是E盘下的nuget目录。刚刚我们把下载到的NuGet包放在了这里，今后要安装包，从这里选择即可。再次打开Manage NuGet Package界面，即可看到Online菜单下面有我们添加的localNuget源了，从里面可以选中我们要安装的包进行安装。

![从本地源安装包](http://www.bibodeng.com/content/plugins/kl_album/upload/201507/ca3e2db8d762a134508a330ceef67def201507011058361783180342.png)

从本地源安装包


##后记
在安装一些依赖很多的包的时候，常常出现无法解决依赖的错误，依赖无法满足则包不能被安装成功。所以本地源手动安装包非常麻烦，需要把依赖的包都安装好后，才能安装自己想要安装的那个包，不像联网的时候需要什么包就自动去根据依赖去获取，而且这些包的依赖，各种版本虽然能够对应，但保不齐不出什么问题。所以能够联网安装包尽量联网安装，这样省心省力。

另外，推荐一个Web API文档自动生成的工具swagger，可以通过NuGet安装Swashbuckle来引入，祝开发愉快！

by bibodeng 2015-07-01