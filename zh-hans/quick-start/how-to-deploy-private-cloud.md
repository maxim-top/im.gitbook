---
description: 私有云部署文档概述 创建应用 开通私有云服务 安装私有云 单机版 集群版 阿里云版 redis-server为redis的服务地址， redis-password为redis的密码 redis-cache-server为redis的服务地址， redis-cache-password为redis的密码 mysql-server为rds的服务地址， mysql-username为rds的用户名, mysql-password为rds的密码 kafka-server为kafka的服务地址，kafka-user为kafka的用户名， kafka-password为kafka的密码 file-storage-access-key-id为阿里云子账号ID file-storage-access-key-secret为阿里云子账号密码 file-storage-access-endpoint为阿里云接入点地址 file-storage-bucket-chat-file为阿里云OSS的bucket名字 file-storage-bucket-user-profile为阿里云OSS的bucket名字
keywords: 私有云, 阿里云版, IM SDK, APP内聊天功能
---
# 私有云部署文档

## 概述

蓝莺IM私有云可以一键安装，省心高效。使用私有云，你将完全掌控你的数据和服务，并毫无限制地访问所有服务。

借助于最先进的容器技术，蓝莺IM所有的服务有已完成云原生改造，这是私有云可以稳定可靠地运行在从裸机服务器、私有云计算平台到各种内部容器平台环境中的重要依靠。

蓝莺IM私有部署提供两种部署模式：单机版和集群版。三步操作，十分钟安装，控制台提供了简洁的状态监控页面，系统运行状态实时掌控。

## 创建应用

[登录控制台](https://console.lanyingim.com) 点击创建应用。应用创建默认为免费版套餐，也可以升级为商业版。

![创建应用](../assets/1-1.create_app.png)

## 开通私有云服务

1.应用创建成功后，进入应用详情页面。

![应用信息](../assets/1-2.app_info.png)

2.点击更改计划，选择私有云，点击“继续”。

![开通私有云服务](../assets/1-3.select_private_plan.png)

3.点击私有云图标，进入私有云详情页面，下载安装包 maxim.ctl

```
$ wget https://package.lanyingim.com/linux/amd64/maxim.ctl
```

![私有云部署](../assets/1-4.deploy.png)

4.获取安装token。可以复制到粘贴板，也可以下载到本地文件备用，安装脚本里我们用 maxim.token.XXXXXX.txt 演示。

![获取私有云安装token](../assets/1-5.get_install_token.png)

## 安装私有云

安装准备

* 操作系统：

> Linux 推荐 Ubuntu 18.04 或 Ubuntu 20.04

> 树莓派 推荐 Ubuntu 18.04 rasp3 

> MacOS 推荐 Catalina 10.15

* 硬件配置：

> CPU 4核 内存 8G 硬盘100G

* 如果选择安装集群版， 需要3台或更多服务器

* 安装方式分为在线安装和离线安装。离线安装不需要访问外网，适合没有外网的服务器来安装，但需要每个月激活一次license， 现在只支持Ubuntu 18.04

* 端口：

```
需要开放每台机器的端口：

80/443

音视频需要：
允许 TCP 3478 访问
允许 UDP 3478 访问
允许 UDP 10000-60000 访问
```

### 单机版

1.首先，准备好一台用来私有部署的服务器，将ssh登录到这台服务器上。 然后，执行下载安装脚本命令，并增加可执行权限。命令如下：

```
wget https://package.lanyingim.com/linux/amd64/maxim.ctl && sudo chmod u+x maxim.ctl
```

执行结果截图：

![单机版安装步骤一](../assets/2-1.install_single_s1.png)

2.运行安装

* 安装服务器已有公网IP，执行如下命令开始安装。

```
sudo ./maxim.ctl install --token INSTALL_TOKEN
```

注意：提示“Enter maxim install token:”，请输入已复制的安装Token，继续执行安装。

开始执行的截图：

![单机版安装步骤二](../assets/2-2.install_single_s2.png)

安装完成的截图：

![单机版安装步骤三](../assets/2-3.install_single_s3.png)

* 本地环境不可进行外部访问，安装时需要添加参数 --net internal 提示安装程序选择内网IP注册。

执行如下命令开始安装

```
sudo ./maxim.ctl install --net internal --token INSTALL_TOKEN
```

提示：安装脚本会提示“Enter maxim install token:”，请输入已复制的安装Token，继续执行安装。

开始执行的截图：

![单机版安装步骤四](../assets/2-4.install_single_s4.png)

安装完成的截图：

![单机版安装步骤五](../assets/2-5.install_single_s5.png)

提示：等待安装完成，耗时15分钟左右，即可安装完成。

### 集群版
1.配置集群访问权限

配置第一台主机对其余主机的ssh权限，以三台主机 172.16.0.78 、172.16.0.79 、172.16.0.80 为例。

注意： 需要修改每台主机的hostname 分别为 node-1 node-2 node-3 ，也可使用其他类似的前缀。

ssh登录master节点（172.16.0.78）

执行如下命令,生成ssh用的公私钥：

```
sudo ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
```

执行结果截图：

![集群权限步骤一](../assets/3-1-1.config_cluster_s1.png)

执行如下命令, 将命令的输出分别在主机172.16.0.78 ，172.16.0.79 ，172.16.0.80上执行

```
sudo echo "sudo echo \"`cat ~/.ssh/id_rsa.pub`\" >> ~/.ssh/authorized_keys"
```

命令输出结果截图：

![集群权限步骤二](../assets/3-1-2.config_cluster_s2.png)

命令输出在172.16.0.78的执行结果：

![集群权限步骤三](../assets/3-1-3.config_cluster_s3.png)

命令输出在172.16.0.79的执行结果：

![集群权限步骤四](../assets/3-1-4.config_cluster_s4.png)

命令输出在172.16.0.80的执行结果：

![集群权限步骤五](../assets/3-1-5.config_cluster_s5.png)

2.ssh登录到第一台主机172.16.0.78上 执行如下命令下载安装脚本，并增加可执行权限

```
wget https://package.lanyingim.com/linux/amd64/maxim.ctl && sudo chmod u+x maxim.ctl
```

执行结果截图：

![集群版安装步骤一](../assets/3-2-1.install_cluster_s1.png)

* 服务器已有公网IP，执行如下命令开始安装。

```
sudo ./maxim.ctl install --nodelist 172.16.0.78 172.16.0.79 172.16.0.80 --token INSTALL_TOKEN
```

提示：安装脚本会提示“Enter maxim install token:”，请输入已复制的安装Token，继续执行安装。

开始执行的截图：

![集群版安装步骤二](../assets/3-2-2.install_cluster_s2.png)

安装完成的截图：

![集群版安装步骤三](../assets/3-2-3.install_cluster_s3.png)

* 本地环境不可进行外部访问，安装时需要添加参数 --net internal 提示安装程序选择内网IP注册。

执行如下命令开始安装。

```
sudo ./maxim.ctl install --nodelist 172.16.0.78 172.16.0.79 172.16.0.80 --net internal --token INSTALL_TOKEN
```

提示：安装脚本会提示“Enter maxim install token:”，请输入已复制的安装Token，继续执行安装。

开始执行的截图：

![集群版安装步骤四](../assets/3-2-4.install_cluster_s4.png)

安装完成的截图：

![集群版安装步骤五](../assets/3-2-5.install_cluster_s5.png)

提示：等待安装完成，耗时20分钟左右，即可安装完成。

### 阿里云版

单机版和集群版支持使用阿里云的redis/rds/kafka/oss，如果需要使用可以在单机版和集群版步骤2的install命令之前执行如下命令：

* 使用阿里云redis做存储

```
## redis-server为redis的服务地址， redis-password为redis的密码
sudo ./maxim.ctl set_config --config redis-server=r-xxx.redis.rds.aliyuncs.com:6379 redis-password=xxx
```

* 使用阿里云redis做缓存

```
## redis-cache-server为redis的服务地址， redis-cache-password为redis的密码
sudo ./maxim.ctl set_config --config redis-cache-server=r-xxx.redis.rds.aliyuncs.com:6379 redis-cache-password=xxx
```

* 使用阿里云rds

```
## mysql-server为rds的服务地址， mysql-username为rds的用户名, mysql-password为rds的密码
sudo ./maxim.ctl set_config --config mysql-server=rm-xxx.mysql.rds.aliyuncs.com:3306 mysql-username=xxx mysql-password=xxx
```

* 使用阿里云kafka

```
## kafka-server为kafka的服务地址，kafka-user为kafka的用户名， kafka-password为kafka的密码
sudo ./maxim.ctl set_config --config kafka-server=172.16.1.10:9092,172.16.1.9:9092,172.16.1.11:9092 kafka-user=xxx kafka-password=xxx
```

* 使用阿里云oss

```
## file-storage-access-key-id为阿里云子账号ID
## file-storage-access-key-secret为阿里云子账号密码
## file-storage-access-endpoint为阿里云接入点地址
## file-storage-bucket-chat-file为阿里云OSS的bucket名字
## file-storage-bucket-user-profile为阿里云OSS的bucket名字
## file-storage-bucket-chat-history为阿里云OSS的bucket名字
## file-storage-bucket-chat-file-chatroom为阿里云OSS的bucket名字
sudo ./maxim.ctl set_config --config file-storage-type=oss file-storage-access-key-id=xxx file-storage-access-key-secret=xxx file-storage-access-endpoint=oss-cn-beijing.aliyuncs.com file-storage-bucket-chat-file=chat-xxx file-storage-bucket-user-profile=profile-xxx file-storage-bucket-chat-history=history-xxx file-storage-bucket-chat-file-chatroom=chat-file-chatroom-xxx
```

### 单机版(离线安装)

1.下载[离线安装包](https://package.lanyingim.com/lanying-im/lanying-im-server.iso), 并上传到用来私有部署的服务器上。

2.执行下面命令挂载离线安装包，并添加maxim.ctl到可执行路径。

```
mkdir -p /lanying && mount -o loop lanying-im-server*.iso /lanying && cp /lanying/maxim.ctl /usr/bin/
```
运行截图为：

![挂载离线安装包，并添加maxim.ctl到可执行路径](../assets/offline_mount_and_add_exec.png)

3.生成离线配置文件

[登录控制台](https://console.lanyingim.com)，选择APP, 进入私有云页面，生成离线配置文件,并上传到服务器上。

操作截图为：

![生成离线配置文件](../assets/generate_offline_install_configration.png)

4.运行安装

```
sudo maxim.ctl install --config-file maxim.*.conf
```

开始执行的截图：

![单机版(离线安装）开始安装](../assets/single_offline_start_install.png)

安装完成的截图：

![单机版(离线安装）安装完成](../assets/single_offline_finish_install.png)

提示：等待安装完成，耗时15分钟左右，即可安装完成。

5.生成集群LicenseKey
```
sudo maxim.ctl export license-key
```
命令截图为：

![生成集群LicenseKey](../assets/single_offline_export_license_key.png)

6.激活集群

在控制台私有云页面点击激活集群，在弹出的对话框中，选择集群规格，输入LicenseKey, 点击"激活集群", 然后将获取的激活命令在集群中执行

操作截图为：

![控制台私有云页面点击激活集群，选择集群规格，输入LicenseKey, 点击"激活集群"](../assets/single_offline_activate.png)

![激活命令](../assets/single_offline_activate_success.png)

![在集群中执行激活命令](../assets/single_offline_exec_activate.png)

7.激活完成后每个月都要执行步骤5和步骤6来更新集群的License,否则集群会因为License过期而阻止用户登录。如果在控制台修改了配置或管理员Token, 也需要执行步骤5和步骤6来更新到集群。

### 集群版(离线安装)

1.配置集群访问权限

配置第一台主机对其余主机的ssh权限，以三台主机 172.16.0.78 、172.16.0.79 、172.16.0.80 为例。

ssh登录master节点（172.16.0.78）

执行如下命令,生成ssh用的公私钥：

```
sudo ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
```

执行结果截图：

![集群权限步骤一](../assets/3-1-1.config_cluster_s1.png)

执行如下命令, 将命令的输出分别在主机172.16.0.78 ，172.16.0.79 ，172.16.0.80上执行

```
sudo echo "sudo echo \"`cat ~/.ssh/id_rsa.pub`\" >> ~/.ssh/authorized_keys"
```

命令输出结果截图：

![集群权限步骤二](../assets/3-1-2.config_cluster_s2.png)

命令输出在172.16.0.78的执行结果：

![集群权限步骤三](../assets/3-1-3.config_cluster_s3.png)

命令输出在172.16.0.79的执行结果：

![集群权限步骤四](../assets/3-1-4.config_cluster_s4.png)

命令输出在172.16.0.80的执行结果：

![集群权限步骤五](../assets/3-1-5.config_cluster_s5.png)

2.下载[离线安装包](https://package.lanyingim.com/lanying-im/lanying-im-server.iso), 并上传到用来私有部署的服务器上。

3.执行下面命令挂载离线安装包，并添加maxim.ctl到可执行路径。

```
mkdir -p /lanying && mount -o loop lanying-im-server*.iso /lanying && cp /lanying/maxim.ctl /usr/bin/
```
运行截图为：

![挂载离线安装包，并添加maxim.ctl到可执行路径](../assets/offline_mount_and_add_exec.png)

4.生成离线配置文件

[登录控制台](https://console.lanyingim.com)，选择APP, 进入私有云页面，生成离线配置文件,并上传到服务器上。

操作截图为：

![生成离线配置文件](../assets/generate_offline_install_configration.png)

5.运行安装

```
sudo maxim.ctl install --config-file maxim.*.conf --nodelist 172.16.0.78 172.16.0.79 172.16.0.80
```

开始执行的截图：

![集群版(离线安装）开始安装](../assets/multi_offline_start_install.png)

安装完成的截图：

![集群版(离线安装）安装完成](../assets/multi_offline_finish_install.png)

提示：等待安装完成，耗时20分钟左右，即可安装完成。

6.生成集群LicenseKeys
```
sudo maxim.ctl export license-key
```
命令截图为：

![生成集群LicenseKey](../assets/single_offline_export_license_key.png)

7.激活集群

在控制台私有云页面点击激活集群，在弹出的对话框中，选择集群规格，输入LicenseKey, 点击"激活集群", 然后将获取的激活命令在集群中执行

操作截图为：

![控制台私有云页面点击激活集群，选择集群规格，输入LicenseKey, 点击"激活集群"](../assets/single_offline_activate.png)

![激活命令](../assets/single_offline_activate_success.png)

![在集群中执行激活命令](../assets/single_offline_exec_activate.png)

8.激活完成后每个月都要执行步骤6和步骤7来更新集群的License,否则集群会因为License过期而阻止用户登录。如果在控制台修改了配置或管理员Token, 也需要执行步骤6和步骤7来更新到集群。

## 安装须知

1. 服务安装完后，服务器会自动进行状态检查，检查结果可以在控制台系统状态页面查看，检查通过会自动迁移，迁移完成就可以使用了。如果确定本地环境不可进行外部访问，安装时需要添加参数 --net internal 提示安装程序选择内网IP注册。
2. 如果机器有防火墙，需要保证端口443和80允许访问。
3. 如何查看私有云安装进度，以及数据迁移状态？

![安装进度点击“私有云”，通过节点信息的进度可以查看安装进度](../assets/4-1.install_progress.png)

1. 安装完成后，打开蓝莺IM控制台进入系统状态页面。

![如果所有检查项的状态都为正常，则表示服务已经正常](../assets/4-2.service_status.png)
