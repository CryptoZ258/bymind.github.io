---
title: TEG编码大赛，Show me the code
date: 2015-11-01 18:03:45
---
#TEG Code大赛

九月份的时候参加了TEG Code编程大赛，在腾讯，TEG素来以专研技术在各BG中而名，故而有时候会比较强调码农做的事情，有时候也搞一些比较有意思的比赛，具有浓烈的geek风范。技术从来都是疯狂的程序员所热衷所在，否则就不会走上计算机编程这条不归之路。我们两个鲜肉，联合了两个T3-2的大腿也参加了比赛，干脆就取名叫“大腿鲜肉队”。

![TEG Code](http://www.bibodeng.com/content/plugins/kl_album/upload/201511/350685835b307ccc05375c75a0ae3ecf201511011801141163677904.jpg)

初赛的题目是要从一个远程的服务器拉取文件到本地，文件包含家政服务的信息，需要解析并清洗出订单和服务员两种实体，分别存储到数据库的两个表中（也可以不存储），最后按照规则计算如何分配订单和服务员，才能够让收益最大化。下面是具体的题目，由于我们只做了文件传输和解析部分，故而就远程拉取文件和解析给出我们的答案，有机会再将匹配算法给出。

##文件服务端
第一步，首先要将服务器端的文件读取到内存中，然后通过网络连接将资料通过TCP协议传送到客户端。根据这个思想，我们用C语言实现了一个单线程的版本，如果要尽量快地发送数据，那就要开多个线程将文件包发送出去。首先计算出文件的大小，然后划分成若干个块，分次读取到内存buffer中，而最后一块比较特殊，因为未必能够填满完整的size内存。读取完后，循环监听TCP请求

    //
    //  main.c
    //  TEG code
    //
    //  Created by feihongliu on 15/8/22.
    //  Copyright (c) 2015年 feihongliu. All rights reserved.
    //

    ////////////////////////////////////
    //服务器代码
    ///////////////////////////////////
    //本文件是服务器的代码

    #include <netinet in.h="">    // for sockaddr_in
    #include <sys types.h="">     // for socket
    #include <sys socket.h="">    // for socket
    #include <stdio.h>         // for printf
    #include <stdlib.h>        // for exit
    #include <string.h>        // for bzero
    #include <time.h>          //for time_t and time

    #define SERVER_PORT 7754
    #define LENGTH_OF_LISTEN_QUEUE 20
    #define BUFFER_SIZE 1024

    #define _FILE_OFFSET_BITS 64
    #define MemoryChunk 16777216
    #define FILE_PATH "data/1.dat"

    int main(int argc, char **argv)
    {
        //设置一个socket地址结构server_addr, 代表服务器internet地址, 端口
        struct sockaddr_in server_addr;
        bzero(&amp;server_addr, sizeof(server_addr)); //把一段内存区的内容全部设置为0
        server_addr.sin_family = AF_INET;
        server_addr.sin_addr.s_addr = htons(INADDR_ANY);
        server_addr.sin_port = htons(SERVER_PORT);
        
        //创建用于internet的流协议(TCP)socket, 用server_socket代表服务器socket
        int server_socket = socket(AF_INET, SOCK_STREAM, 0);
        if (server_socket &lt; 0)
        {
            printf("Create Socket Failed!");
            exit(1);
        }
        
        //把socket和socket地址结构联系起来
        if (bind(server_socket, (struct sockaddr*)&amp;server_addr, sizeof(server_addr)))
        {
            printf("Server Bind Port : %d Failed!", SERVER_PORT);
            exit(1);
        }
        
        //server_socket用于监听
        if (listen(server_socket, LENGTH_OF_LISTEN_QUEUE))
        {
            printf("Server Listen Failed!");
            exit(1);
        }
        
        printf("Start file read");
        FILE * pFile;
        long lSize;
        
        pFile = fopen(FILE_PATH, "rb");
        fseek(pFile, 0, SEEK_END);
        lSize = ftell(pFile);
        rewind(pFile);
        
        int mount = lSize / MemoryChunk + 1;
        char ** memaddr_array = (char**)malloc(sizeof(char*)*mount);
        for (int i = 0; i &lt; mount; i++)
        {
            char * buffer;
            buffer = (char*)malloc(sizeof(char)*MemoryChunk);
            memaddr_array[i] = buffer;
        }
        
        //load file to memery
        for (int i = 0; i &lt; mount - 1; i++)
        {
            fread(memaddr_array[i], MemoryChunk, 1, pFile);
        }
        int last_size = lSize - ftell(pFile);
        fread(memaddr_array[mount - 1], 1, last_size, pFile);
        
        printf("End file read");
        
        
        //服务器端要一直运行
        while (1)
        {
            struct sockaddr_in client_addr;
            socklen_t length = sizeof(client_addr);
            int new_server_socket = accept(server_socket, (struct sockaddr*)&amp;client_addr, &amp;length);
            if (new_server_socket &lt; 0)
            {
                printf("Server Accept Failed!\n");
                break;
            }
            //首次发送文件大小
            char filelength[64];
            sprintf(filelength, "%ld", lSize);
            send(new_server_socket, filelength, 64, 0);
            //发送文件内容
            for (int i = 0; i &lt; mount - 1; i++)
            {
                send(new_server_socket, memaddr_array[i], MemoryChunk, 0);
            }
            send(new_server_socket, memaddr_array[mount - 1], last_size, 0);
            
            //关闭与客户端的连接
            close(new_server_socket);
        }
        
        //释放资源 关闭监听用的socket
        close(server_socket);
        fclose(pFile);
        for (int i = 0; i &lt; mount; i++)
        {
            free(memaddr_array[i]);
        }
        free(memaddr_array);
        return 0;
    }

如上所示，最初版本的读取文件和发送都是串行的，后面将会继续优化。

##文件读取客户端

有了服务端，那么我们就要想办法连接TCP，然后将收到的信息存到文件中去。其处理次序与发送相逆，当recv到数据后，append到文件中去，然后对数据进行逐条解析。

    //客户端代码

    //本文件是客户机的代码
    #include <netinet in.h="">    // for sockaddr_in
    #include <sys types.h="">    // for socket
    #include <sys socket.h="">    // for socket
    #include <stdio.h>        // for printf
    #include <stdlib.h>        // for exit
    #include <string.h>        // for bzero
    #include <time.h>                //for time_t and time
    #include <arpa inet.h="">

    #define SERVER_PORT    7754         // server port
    #define BUFFER_SIZE 1024            // write to file buffer

    #define FILE_OFFSET_BITS 64         // filesize string offset
    #define MEMORY_CHUNK_SIZE 16777216  // 16MB
    #define DEFAULT_SERVER_IP "127.0.0.1"
    #define FILE_PATH  "data/1.client.dat"

    // 钟点工
    struct Worker{
        int _id;
        char _gender;
        char _age;
        float _score;
    };

    // 订单
    struct Bill{
        int _id;
        double _px;
        double _py;
        char _time;
        char _time_require;
        int _begin_time;
        char* _image;
        
    };



    // download module
     // by bibo 2015-08-25
    void download_file(char* server_ip, int port)
    {
        time_t start, end;
        time(&amp;start);
        
        FILE *stream;
        
        //设置一个socket地址结构client_addr,代表客户机internet地址, 端口
        struct sockaddr_in client_addr;
        bzero(&amp;client_addr, sizeof(client_addr)); //把一段内存区的内容全部设置为0
        client_addr.sin_family = AF_INET;    //internet协议族
        client_addr.sin_addr.s_addr = htons(INADDR_ANY);//INADDR_ANY表示自动获取本机地址
        client_addr.sin_port = htons(0);    //0表示让系统自动分配一个空闲端口
        
        //创建用于internet的流协议(TCP)socket,用client_socket代表客户机socket
        int client_socket = socket(AF_INET, SOCK_STREAM, 0);
        if( client_socket &lt; 0) {
            printf("Create Socket Failed!\n");
            exit(1);
        }
        //把客户机的socket和客户机的socket地址结构联系起来
        if( bind(client_socket, (struct sockaddr*)&amp;client_addr, sizeof(client_addr))) {
            printf("Client Bind Port Failed!\n");
            exit(1);
        }
        
        //设置一个socket地址结构server_addr,代表服务器的internet地址, 端口
        struct sockaddr_in server_addr;
        bzero(&amp;server_addr, sizeof(server_addr));
        server_addr.sin_family = AF_INET;
        //服务器的IP地址来自程序的参数
        if(inet_aton(server_ip, &amp;server_addr.sin_addr) == 0) {
            printf("Server IP Address Error!\n");
            exit(1);
        }
        
        server_addr.sin_port = htons(port);
        socklen_t server_addr_length = sizeof(server_addr);
        
        //向服务器发起连接, 连接成功后client_socket代表了客户机和服务器的一个socket连接
        if (connect(client_socket, (struct sockaddr*)&amp;server_addr, server_addr_length) &lt; 0) {
            printf("Can Not Connect To %s!\n", server_ip);
            exit(1);
        }
        
        char buffer[BUFFER_SIZE];
        bzero(buffer, BUFFER_SIZE);
        
        //从服务器接收数据到buffer中
        int length = recv(client_socket, buffer, BUFFER_SIZE, 0);
        
        if(length &lt; 0) {
            printf("Recieve Data From Server %s Failed!\n", server_ip);
            exit(1);
        }
        
        // 先接收长度
        long lSize;
        lSize = sscanf(buffer,"%ld", &amp;lSize); // char array to long
        
        printf("\n%s\n", buffer);
        bzero(buffer, BUFFER_SIZE);
        
        // open or create file
        if ((stream = fopen("data","wb+")) == NULL) {
            printf("The file 'data' was not opened! \n");
        }
        else
        {
            bzero(buffer, BUFFER_SIZE);
        }
        
        length = 0;
        // 后续是否使用多线程 TODO
        while (length = recv(client_socket, buffer, BUFFER_SIZE, 0)) {
            if (length &lt; 0) {
                printf("Recieve Data From Server %s Failed!\n", server_ip);
                break;
            }
            
            int write_length = fwrite(buffer, sizeof(char), length, stream);
            if (write_length &lt; length) {
                printf("File is Write Failed\n");
                break;
            }
            
            printf("write data to file!\n");
            
            bzero(buffer, BUFFER_SIZE);
        }
        printf("Recieve File From Server[%s] Finished\n", server_ip);
        
        fclose(stream);
        close(client_socket);
        
        time(&amp;end);
        double t = difftime(end, start);
        printf("download file use: %f ", t);

    }


    //解析文件
    // by bibo 2015-08-25

    void parse_file()
    {
        time_t start, end;
        time(&amp;start);
        
        //--------parse---------
        
        FILE* stream;
        if ((stream = fopen( FILE_PATH , "rb")) == NULL)
        {
            printf("The file 'data' was not opened! \n");
            exit(0);
        }
        
        
        // 钟点工 = 长度 + 记录类型（0） + ID + 性别 + 年龄 + 评分
        // 15 字节 = 4 + 1 + 4 + 1 + + 1 + 4
        
        // 需求 = 长度 + 记录类型 （1）+ ID + 横坐标 + 纵坐标 + 时长 + 时间要求 + 起始时间 + 图片？
        // ? = 4 + 1 + 4 + 8 + 8 + 1 + 1 + 4 + ？
        
        
        printf("int %ld \n", sizeof(int));
        printf("short %ld \n", sizeof(short));
        printf("float %ld \n", sizeof(float));
        printf("long %ld \n", sizeof(long));
        printf("char %ld \n", sizeof(char));
        
        char buffer[BUFFER_SIZE];
        bzero(buffer, BUFFER_SIZE);
        
        
        int record_size = 0;
        long length = 0;
        
        int bill_num = 0;
        int worker_num = 0;
        
        // TODO 想办法将结构树体放到某个数据结构中去存储并计算
        // 2G数据，必须要进行分治才能高效计算
        
        // 读取文件到内存中
        while (length = fread(&amp;record_size, sizeof(int), 1, stream)) {
            
            // 长度
            // printf("record size: %d \n", record_size);
            char type = 0;
            
            //
            int i = 0;
            char c = 0;
            long l = 0;
            float f = 0;
            double d = 0;
            
            
            length = fread(&amp;type, sizeof(char), 1, stream);
            
            // type
            if (type == 0)
            {
                struct Worker worker;
                
                fread(&amp;i, sizeof(int), 1, stream); // ID
                worker._id = i;
                
                fread(&amp;c, sizeof(char), 1, stream); // gender
                worker._gender = c;
                
                fread(&amp;c, sizeof(char), 1, stream); // age
                worker._age = c;
                
                fread(&amp;f, sizeof(float), 1, stream); // score
                worker._score = f;
                
                printf("get a worker: %d, %d, %d, %f \n", worker._id, worker._gender, worker._age, worker._score);
                
                // free(&amp;worker);
                
                worker_num++;
                
            }
            else if (type == 1)
            {
                struct Bill bill;
                
                fread(&amp;i, sizeof(int), 1, stream); // ID
                bill._id = i;
                
                fread(&amp;d, sizeof(double), 1, stream); // px
                bill._px = d;
                
                fread(&amp;d, sizeof(double), 1, stream);// py
                bill._py = d;
                
                fread(&amp;c, sizeof(char), 1, stream); // time
                bill._time = c;
                
                fread(&amp;c, sizeof(char), 1, stream); // time_require
                bill._time_require = c;
                
                if (bill._time_require == 1) // 有时间要求
                {
                    fread(&amp;i, sizeof(int), 1, stream);
                    bill._begin_time = i;
                    
                    // 直接略过
                    fseek(stream, sizeof(char) * ( record_size - 27 - 4), SEEK_CUR);
                    
                    // bill._image = (char*) malloc(sizeof(char) * (record_size - 27 - 4));
                    // fread(bill._image, sizeof(char), record_size - 27 - 4, stream);
                }
                else
                {
                    bill._begin_time = 0;
                    
                    // 直接略过
                    fseek(stream, sizeof(char) * ( record_size - 27), SEEK_CUR);
                    
                    // bill._image = (char*)malloc(sizeof(char) * (record_size - 27));
                    // fread(bill._image, sizeof(char), record_size - 27 , stream);
                    
                }
                
                printf("get a bill: %d, %f, %f, %d, %d, %d, %s \n", bill._id, bill._px, bill._py, bill._time, bill._time_require, bill._begin_time, bill._image);
                
                // 暂时不存储
                free(bill._image);
                
                bill_num ++;
            }
        }
        
        
        
        
        //---------------------
        // show time
        time(&amp;end);
        double t = difftime(end, start);
        printf("parse file use time: %lf \n", t);
        
        printf("total worker num: %d \n", worker_num);
        printf("total bill num: %d \n", bill_num);
        
        scanf("pleas press key to exit: %lf \n ", &amp;t);
        return;
    }

    // 解析记录
    void parse_record()
    {
        return;
    }

    //---------------------Main-----------------------
    int main(int argc, char **argv)
    {
        if (argc != 2) {
            printf("Usage: ./%s ServerIPAddress\n", argv[0]);
            argv[1] = DEFAULT_SERVER_IP;
            // exit(1);
        }
        
       
        download_file(argv[1], SERVER_PORT);
            
        parse_file();
        
        return 0;
    }

最终，此次兴趣比赛，因为我们个人没有时间最终没有提交完整的代码。不过，我们最终还是得到了一件文化衫，当时报名也就是为了一件 `Talk is cheap , Show me the code` 的 T-Shirt，因为于Linux的服务器编程，我们IT部并不在行，而架构平台部，安全平台部比较在行，在决赛的晚会中，他们展示的方案想法其实也差不多，就看谁能够有这么强的代码能力付诸实现。

--end--
by biboedeng 2015-11-01</arpa></time.h></string.h></stdlib.h></stdio.h></sys></sys></netinet></time.h></string.h></stdlib.h></stdio.h></sys></sys></netinet>