# Private Cloud Deployment documentation

## Profile

One-click installation makes Maximtop Proprietary Cloud worry-free and efficient. With Private Cloud, you can complete control over your data and services, and access to all services unlimitedly.

With cutting-edge container technology, all Maximtop services have completed Cloud-native transformation, commit to smooth, stable and reliable operation of bare-metal servers, private cloud platforms, and other on-premise container platforms.

Maximtop Private Deployment provides two deployment modes: Single server version and cluster version. 3 operates, 10 minutes to setup, the Console provides a concise state monitoring page for controlling system running state in real-time.

## Create application

[Login Console](https://console.maximtop.com) Click to create application. Your application will use Free Edition package by default, or can be upgraded to Business Edition.

![Create application](<../assets/1-1.create_app (1).png>)

## Enable Private Cloud Services

1. After application created, go to Application Details page.

![Application information](<../assets/1-2.app_info (1).png>)

1. Click to change plan, select Private Cloud and then “Continue”.

![Enable Private Cloud Services](../assets/1-3.select_private_plan.png)

1. Click the Private Cloud icon, go to the Private Cloud Details page, download installation package maxim.ctl

```
$ wget https://package.maximtop.com/linux/amd64/maxim.ctl
```

![Private Cloud Deployment](../assets/1-4.deploy.png)

1. Get the installation token, which can be copied to clipboard or downloaded as a local file for later use. In the installation script, we use maxim.token.XXXXXXX.txt to demonstrate.

![Get Private Cloud installation token](../assets/1-5.get_install_token.png)

## Setup Private Cloud

Installation prerequisites

* OS：

> Linux: Ubuntu 18.04 or CentOS 7/8 recommended Raspberry Pie: Ubuntu 18.04 rasp3 recommended MacOS: Catalina 10.15 recommended

* Hardware configuration：

> Quad-core CPU, 8 G RAM, 100 G hard disk

* 3 or more servers required if you choose to install Cluster version
* Download installation package maxim.ctl

### Single server version

1. First, get a server ready for Private Deployment and log ssh on to it. Then, execute the download installation script command and elevate the executable permissions. The command is as follows:

```
wget https://package.maximtop.com/linux/amd64/maxim.ctl && sudo chmod u+x maxim.ctl
```

Screenshot of execution result:

![Single server version installation: Step 1](../assets/2-1.install_single_s1.png)

1. Run installation

* Ensure your server to install on has a public network IP, and execute the following command to start.

```
sudo ./maxim.ctl install --token INSTALL_TOKEN
```

Note: “Enter maxim install token” hint, means please enter your copied installation token to continue.

Screenshot of execution started:

![Single server version installation: Step 2](../assets/2-2.install_single_s2.png)

Screenshot of installation completed

![Single server version installation: Step 3](../assets/2-3.install_single_s3.png)

* The local environment is not accessible externally, and the parameter --net internal needs to be added during installation to prompt the installer to select intranet IP registration.

Execute the following command to start installation

```
sudo ./maxim.ctl install --net internal --token INSTALL_TOKEN
```

Hint: The installation script hints “Enter maxim install token”, means please enter the copied installation token to continue.

Screenshot of execution started:

![Single server version installation: Step 4](../assets/2-4.install_single_s4.png)

Screenshot of installation completed

![Single server version installation: Step 5](../assets/2-5.install_single_s5.png)

Hint: Wait for the installation to complete, which takes about 15 minutes.

### Cluster version

1. Configure cluster access

Configure the ssh permission of the first host to the remaining hosts, taking three hosts, 172.16.0.78, 172.16.0.79, 172.16.0.80 as examples.

ssh login master node (172.16.0.78)

Execute the following command to generate public and private key for ssh:

```
sudo ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
```

Screenshot of execution result:

![Cluster permission configuration: Step 1](../assets/3-1-1.config_cluster_s1.png)

Execute the output of the following commands on hosts 172.16.0.78, 172.16.0.79, 172.16.0.80, respectively

```
sudo echo "sudo echo \"`cat ~/.ssh/id_rsa.pub`\" >> ~/.ssh/authorized_keys"
```

Screenshot of command output:

![Cluster permission configuration: Step 2](../assets/3-1-2.config_cluster_s2.png)

Execution result of the command output at 172.16.0.78:

![Cluster permission configuration: Step 3](../assets/3-1-3.config_cluster_s3.png)

Execution result of the command output at 172.16.0.79:

![Cluster permission configuration: Step 4](../assets/3-1-4.config_cluster_s4.png)

Execution result of the command output at 172.16.0.80:

![Cluster permission configuration: Step 5](../assets/3-1-5.config_cluster_s5.png)

1. ssh login on to the first host 172.16.0.78, execute the following command to download installation script and elevate executable permission:

```
wget https://package.maximtop.com/linux/amd64/maxim.ctl && sudo chmod u+x maxim.ctl
```

Screenshot of execution result:

![Cluster version installation: Step 1](../assets/3-2-1.install_cluster_s1.png)

* Ensure the sever has a public network IP, execute the following command to start.

```
sudo ./maxim.ctl install --nodelist 172.16.0.78 172.16.0.79 172.16.0.80 --token INSTALL_TOKEN
```

Hint: The installation script hints “Enter maxim install token”, means please enter the copied installation token to continue.

Screenshot of execution started:

![Cluster version installation: Step 2](../assets/3-2-2.install_cluster_s2.png)

Screenshot of installation completed

![Cluster version installation: Step 3](../assets/3-2-3.install_cluster_s3.png)

* The local environment is not accessible externally, and the parameter --net internal needs to be added during installation to prompt the installer to select intranet IP registration.

Execute the following command to install.

```
sudo ./maxim.ctl install --nodelist 172.16.0.78 172.16.0.79 172.16.0.80 --net internal --token INSTALL_TOKEN
```

Hint: The installation script hints “Enter maxim install token”, means please enter the copied installation token to continue.

Screenshot of execution started:

![Cluster version installation: Step 4](../assets/3-2-4.install_cluster_s4.png)

Screenshot of installation completed

![Cluster version installation: Step 5](../assets/3-2-5.install_cluster_s5.png)

Hint: Wait for the installation to complete, which takes about 20 minutes.

### Alibaba Cloud version

Single server version and Cluster version support using Alibaba Cloud's redis/rds/kafka/oss，please execute the following command before Single server version and Cluster versions's "Step 2: install" as needs:

* Use Alibaba Cloud's redis as Storage

```
## redis-server is redis' service Address， redis-password is redis' Password
sudo ./maxim.ctl set_config --config redis-server=r-xxx.redis.rds.aliyuncs.com:6379 redis-password=xxx
```

* Use Alibaba Cloud redis as cache

```
## redis-cache-server为redis的服务Address， redis-cache-password为redis的Password
sudo ./maxim.ctl set_config --config redis-cache-server=r-xxx.redis.rds.aliyuncs.com:6379 redis-cache-password=xxx
```

* Use Alibaba Cloud rds

```
## mysql-server is rds' service Address， mysql-username is rds' Username, mysql-password is rds' Password
sudo ./maxim.ctl set_config --config mysql-server=rm-xxx.mysql.rds.aliyuncs.com:3306 mysql-username=xxx mysql-password=xxx
```

* Use Alibaba Cloud kafka

```
## kafka-server is kafka's Address，kafka-user is kafka's Username， kafka-password is kafka's Password
sudo ./maxim.ctl set_config --config kafka-server=172.16.1.10:9092,172.16.1.9:9092,172.16.1.11:9092 kafka-user=xxx kafka-password=xxx
```

* Use Alibaba Cloud oss

```
## file-storage-access-key-id is Alibaba Cloud sub-account ID
## file-storage-access-key-secret Alibaba Cloud sub-account Password
## file-storage-access-endpoint is Alibaba Cloud access point Address
## file-storage-bucket-chat-file is Alibaba Cloud OSS's bucket name
## file-storage-bucket-user-profile is Alibaba Cloud OSS's bucket name
## file-storage-bucket-chat-history is Alibaba Cloud OSS's bucket name
## file-storage-bucket-chat-file-chatroom is Alibaba Cloud OSS's bucket name
sudo ./maxim.ctl set_config --config file-storage-type=oss file-storage-access-key-id=xxx file-storage-access-key-secret=xxx file-storage-access-endpoint=oss-cn-beijing.aliyuncs.com file-storage-bucket-chat-file=chat-xxx file-storage-bucket-user-profile=profile-xxx file-storage-bucket-chat-history=history-xxx file-storage-bucket-chat-file-chatroom=chat-file-chatroom-xxx
```

## Other considerations

1. After the service is installed, you need to contact the server for self-inspection. If it is determined that the local environment cannot be accessed externally, you need to add the parameter --net internal to prompt the installer to select intranet IP registration.
2. If the host has a firewall, you need to ensure that ports 443 and 80 are accessible.
3. How to check Private Cloud installation progress and data migration status?

![Click “Private Cloud” to view the installation progress through the progress of node information](../assets/4-1.install_progress.png)

1. After installation completed, open Maximtop Console to enter System Status page.

![If all checks are normal, means the service is normal](../assets/4-2.service_status.png)
