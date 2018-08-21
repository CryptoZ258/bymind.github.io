---
title: ubuntu环境下安装比特币软件
date: 2016-12-01 13:26:53
---
windows及mac等环境安装比特币软件方法不在本篇阐述，本篇介绍如何在ubuntu 14.04环境下搭建比特币的核心程序。

##准备
首先，添加比特币的程序PPA源

    add-apt-repository ppa:bitcoin/bitcoin
    apt-get update

如果你支持bitcoin unlimited，支持更大的区块，想安装比特币的unlimited版本，则将以上语句换成：

    sudo add-apt-repository ppa:bitcoin-unlimited/bu-ppa
    apt-get update

还需要安装一些依赖：

    apt-get install libboost-all-dev libdb4.8-dev libdb4.8++-dev

##安装
安装很简单，只需要执行下面命令：

    apt-get install bitcoind bitcoin-qt 

##运行
将二进制程序纳入到path所涵盖的目录中，这样无需输入完整路径就能够运行程序了。

    ln -s /usr/bin/bitcoind /usr/local/bin/bitcoind

我的系统将bitcoind安装到了/usr/bin/bitcoind了，以上是将/usr/bin/bitcoind 软链接到 /usr/local/bin目录中，也可以不链接。
运行之前，先创建一bitcoin目录，添加一个配置文件bitcoin.conf，bitcoind运行时自动会读取配置文件。

    cd ~/
    mkdir .bitcoin
    cd .bitcoin
    vim bitcoin.conf

编辑配置文件的内容：

    server=1
    daemon=1
    testnet=1
    rpcuser=UNIQUE_RPC_USERNAME
    rpcpassword=UNIQUE_RPC_PASSWORD

rpcuser和rpcpassword可以任意填写，但是二者不能相同，testnet表示同步的将是testnet的数据，去除该配置，则从正式环境比特币区块链中同步数据，具体的配置文件模板可以参考[bitcoin.conf模板](http://we.lovebitco.in/bitcoin-qt/configuration-file/)
配置文件写好后，则可以直接运行比特币的服务程序了。

    bitcoind

##测试
比特币核心节点运行起来后，我们可以使用bitcoin-cli来跟bitcoind通信，获取其中同步的数据，运行下面命令，可以测试比特币核心是否运行起来了。

    bitcoin-cli getinfo 

getinfo可以看到类似如下信息，表明了比特币核心的运行情况：

        {
	  "version": 130100,
	  "protocolversion": 70014,
	  "walletversion": 130000,
	  "balance": 0.00000000,
	  "blocks": 151998,
	  "timeoffset": 0,
	  "connections": 8,
	  "proxy": "",
	  "difficulty": 1203461.926379965,
	  "testnet": false,
	  "keypoololdest": 1480560958,
	  "keypoolsize": 100,
	  "paytxfee": 0.00000000,
	  "relayfee": 0.00001000,
	  "errors": ""
	}

通过尝试，你可以使用更多命令，如getblockhash, getblock, getrawtransaction 等，具体的命令列表参考 [bitcoin rpc命令](https://bitcoin.org/en/developer-reference#bitcoin-core-apis)

祝玩比特币愉快~