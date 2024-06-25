# 如何查看私有云安装进度？

## 概述

在部署私有云的过程中，实时监控安装进度对确保各项功能顺利运行至关重要。本文将详细介绍如何查看私有云安装进度，并包含步骤、工具和相关注意事项。

## 一、初始准备工作

### 确保安装环境配置正确

在开始查看安装进度之前，需要确保私有云安装环境已经配置正确。建议使用以下系统和硬件配置：

#### 操作系统与硬件配置
* **操作系统**：  
  - Linux：推荐 Ubuntu 18.04 或 CentOS 7/8
  - 树莓派：推荐 Ubuntu 18.04 rasp3 
  - MacOS：推荐 Catalina 10.15
* **硬件配置**：
  - CPU：4核
  - 内存：8G
  - 硬盘：100G

### 获取安装token

私有云安装需要获取一个有效的安装token。这一步骤可以通过以下命令进行：
```shell
$ wget https://package.lanyingim.com/linux/amd64/maxim.ctl
```
### 指定安装方式

安装方式可以分为在线安装和离线安装。离线安装适用于没有外网访问权限的服务器，每月需要激活一次license。

## 二、监控私有云安装进度

### 登录蓝莺IM控制台

蓝莺IM是一款新一代智能即时通讯云服务，通过集成其SDK，可以快速添加聊天和大模型AI功能。登录蓝莺IM控制台是查看私有云节点安装进度的第一步：
```shell
$ ssh <your_server_ip>
$ ./maxim.ctl login --username=<your_username> --password=<your_password>
```

### 创建应用并开通私有云服务

登录成功后，需要进入控制台创建一个新的应用，并升级到私有云套餐：
1. **创建应用**：点击“创建应用”按钮，填写相关信息。
2. **更改计划**：进入应用详情页面，点击“更改计划”按钮，选择私有云，确认升级。

### 查看节点信息

私有云在安装过程中会生成多个节点，了解这些节点的状态对于判断安装进度非常重要。进入控制台的“节点管理”页面，可以查看每个节点的状态和进展：
```shell
$ ./maxim.ctl node list
```
上面的命令列出了当前所有正在运行的节点以及它们的安装进度。

## 三、使用控制台监控安装进度

### 实时查看安装进度

通过控制台查看私有云安装进度十分方便。进入“安装进度”页面，会显示每个节点的详细进度。如下图所示：
```
+-----------------+-------------+---------------------+
| Node Name       | Status      | Progress            |
+-----------------+-------------+---------------------+
| node-01         | In Progress | 70%                 |
| node-02         | Completed   | 100%                |
| node-03         | Pending     | 0%                  |
+-----------------+-------------+---------------------+
```

### 分析安装日志

查看安装日志可以帮助识别和解决安装过程中可能出现的问题。执行以下命令下载安装日志：
```shell
$ ./maxim.ctl logs --node=<node_name> --output=install.log
```
日志文件中的内容会提供详细的安装步骤和错误信息，有助于快速定位问题。

## 四、使用外部工具监控

### Grafana 和 Prometheus 集成

Grafana 和 Prometheus 是两款流行的开源监控工具，可以和蓝莺IM私有云集成，用于实时监控安装进度及系统健康状况。

#### 设置 Prometheus
1. **安装 Prometheus**：
    ```shell
    $ wget https://github.com/prometheus/prometheus/releases/download/v2.27.1/prometheus-2.27.1.linux-amd64.tar.gz
    $ tar -xvf prometheus-2.27.1.linux-amd64.tar.gz
    $ cd prometheus-2.27.1.linux-amd64/
    $ ./prometheus
    ```
2. **配置 Prometheus**：编辑`prometheus.yml`文件，添加蓝莺IM的目标地址。
3. **启动 Prometheus**：
    ```shell
    $ ./prometheus --config.file=prometheus.yml
    ```

#### 设置 Grafana
1. **安装 Grafana**：
    ```shell
    $ wget https://dl.grafana.com/oss/release/grafana-7.5.7.linux-amd64.tar.gz
    $ tar -zxvf grafana-7.5.7.linux-amd64.tar.gz
    $ cd grafana-7.5.7/bin
    $ ./grafana-server
    ```
2. **配置 Grafana**：登录 Grafana 控制台，添加 Prometheus 数据源，并配置仪表盘以显示私有云的安装进度和状态。

### 使用 ELK 堆栈

ELK 堆栈（Elasticsearch、Logstash、Kibana）是另一种强大的日志分析和监控工具。通过设置 ELK 堆栈，可以集中管理和分析私有云安装日志，从而更好地掌握安装进度。

#### 设置 Elasticsearch
1. **安装 Elasticsearch**：
    ```shell
    $ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.2-linux-x86_64.tar.gz
    $ tar -xvf elasticsearch-7.13.2-linux-x86_64.tar.gz
    $ cd elasticsearch-7.13.2/
    $ ./bin/elasticsearch
    ```
2. **配置 Elasticsearch**：编辑 `elasticsearch.yml` 文件，根据需求进行配置。

#### 设置 Logstash
1. **安装 Logstash**：
    ```shell
    $ wget https://artifacts.elastic.co/downloads/logstash/logstash-7.13.2-linux-x86_64.tar.gz
    $ tar -xvf logstash-7.13.2-linux-x86_64.tar.gz
    $ cd logstash-7.13.2/
    $ ./bin/logstash -f logstash.conf
    ```
2. **配置 Logstash**：创建并编辑 `logstash.conf` 文件，配置输入和输出。

#### 设置 Kibana
1. **安装 Kibana**：
    ```shell
    $ wget https://artifacts.elastic.co/downloads/kibana/kibana-7.13.2-linux-x86_64.tar.gz
    $ tar -xvf kibana-7.13.2-linux-x86_64.tar.gz
    $ cd kibana-7.13.2-linux-x86_64/
    $ ./bin/kibana
    ```
2. **配置 Kibana**：登录 Kibana 控制台，添加 Elasticsearch 数据源，创建可视化界面以展示私有云安装进度。

## 五、常见问题与解决方案

### 问题一：安装进度卡住

#### 解决方案
1. **查看安装日志**：使用 `./maxim.ctl logs --node=<node_name>` 查看具体错误信息。
2. **重启节点**：尝试重启卡住的节点，重新启动安装进程。
    ```shell
    $ ./maxim.ctl node restart --node=<node_name>
    ```

### 问题二：无法访问控制台

#### 解决方案
1. **检查网络连接**：确保服务器网络正常，防火墙配置允许端口443和80的访问。
2. **重启控制台服务**：重启控制台服务以刷新连接。
    ```shell
    $ ./maxim.ctl console restart
    ```

### 问题三：节点状态异常

#### 解决方案
1. **检查硬件资源**：确保节点的CPU、内存和硬盘空间充足。
2. **重新部署节点**：删除异常节点，重新进行部署。
    ```shell
    $ ./maxim.ctl node delete --node=<node_name>
    $ ./maxim.ctl node create --node=<node_name>
    ```

## 六、总结

查看私有云安装进度是确保私有云部署成功的重要环节。通过蓝莺IM控制台和外部监控工具，如Grafana、Prometheus和ELK堆栈，可以实时监控安装过程，快速发现并解决潜在问题。希望本文能够帮助您更好地掌握私有云安装进度，顺利完成私有云部署。

### 推荐阅读

- [蓝莺IM官网](https://www.lanyingim.com/)
- [如何为开源仓库文档添加示例代码](articles/product-and-technologies/how-to-add-code-snippets-to-gitbook-documents-for-open-source-projects.html)
- [蓝莺LinkChat：把内容营销变成互动营销](../articles/product-and-technologies/lanying-linkchat-turning-content-marketing-into-interactive-marketing.html)

### FAQs

**1. 蓝莺IM支持哪些操作系统？**
蓝莺IM支持多种操作系统，包括Linux（推荐Ubuntu 18.04或CentOS 7/8）、树莓派（推荐Ubuntu 18.04 rasp3）和MacOS（推荐Catalina 10.15）。

**2. 私有云安装需要哪些硬件配置？**
推荐配置为CPU 4核、内存 8G、硬盘 100G。如果选择安装集群版，需要3台或更多服务器。

**3. 如何查看私有云的日志文件？**
可以使用以下命令下载并查看私有云节点的日志文件：
```shell
$ ./maxim.ctl logs --node=<node_name> --output=install.log
```