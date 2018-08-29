---
title: 解密比特币改善提案BIP21
date: 2018-08-29 08:34:26
tags: [BCH, BIP, 比特币]
---
## BIP及提案过程
BIP全称Bitcoin Improvement Proposal，意为比特币改善提案，是人们提出的改进比特币及其应用的一个工具，通过收集各种提案，通过讨论，大家能够推进比特币的发展和改良。有意思的是，BIP的第一个提案，就是关于BIP的详细提案规则。

BIP的提案过程如下：
![](https://en.bitcoin.it/w/images/en/e/ea/BIP_Workflow.png)

## BIP21
我们今天使用比特币钱包能如此方便，要感谢BIP21，接下来我们详细分析一下BIP21。

这个提案要解决的是比特币应用层（这里指钱包）的一个扫码及链接支付的标准提议。该提议介绍了一种URI的语法，这种URI语法可以使得用户可以通过一个链接来发起一笔交易，交易里面指定了一些参数，如金额、备注等，当然这个链接也可以编码成一个二维码，用户通过钱包扫码，就能理解获得一个支付地址。BIP21使得比特币的支付非常简单和普及，该标准使得可以在众多钱包中相互转账，甚至在页面里面实现点击链接转账。

对于请求支付的人来说，应该按照这个标准来构造这样一个URI，或者是二维码，而对于支付方，则需要能够解析对方给出的URI，把里面的关键信息提取出来，完成后续的转账操作。其实这两个步骤，一般都不需要用户介入，钱包商会搞定一切，最终钱包用起来就像是微信支付一样，非常方便。

### BIP32协议内容
提案提议的格式如下：

```
// 协议:地址?参数串
"bitcoin": bitcoinaddress [ "?" bitcoinparams ]
// 地址为base58编码的字符串
bitcoinaddress = *base58
// 参数串由一个个参数用&连接起来
 bitcoinparams  = bitcoinparam [ "&" bitcoinparams ]
// 参数类型
 bitcoinparam   = [ amountparam / labelparam / messageparam / otherparam / reqparam ]
// amount 参数：amount=数字
 amountparam    = "amount=" *digit [ "." *digit ]
// label 参数：label=字符串
 labelparam     = "label=" *qchar
// message 参数：message=字符串
 messageparam   = "message=" *qchar
// 其它自定义参数：参数名=参数值
 otherparam     = qchar *qchar [ "=" *qchar ]
// req参数：req-参数名=参数值 req表示是不可缺参数
 reqparam       = "req-" qchar *qchar [ "=" *qchar ]

```
从上面的定义和注释我们可以看出它和网页URL很相似，也是一个协议，加地址，再带上若干参数。实际上除了双斜杠之外，其它基本是一样的，而且该提案定义了几个参数，如amount/label/message等。

bitcoin协议名可以大写也可以小写，但是各个参数名是大小写敏感的，不能随便更改。

### 简化版本
上面的协议其实还是略微复杂难懂，简化版本如下：
```
 bitcoin:<address>[?amount=<amount>][?label=<label>][?message=<message>]
```

### 例子
举个例子，bibo请求一个20.3BTC的捐赠：
```
 bitcoin:175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W?amount=20.3&label=bibo&message=donation
```
扫码者，将通过钱包支付给比特币地址`175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W`一笔`20.3 BTC`的转账，标记为`bibo`，备注为`donation`。

### BIP21的若干语言实现：
* Javascript - https://github.com/bitcoinjs/bip21
* Java - https://github.com/SandroMachado/BitcoinPaymentURI
* Swift - https://github.com/SandroMachado/BitcoinPaymentURISwift

