---
description: 修改k8s安装时的DNS服务器配置以确保集群稳定和安全，可能遇到的问题及解决方案
keywords: k8s, 修改DNS, IM SDK, APP内聊天功能
---
# 如何在国内安装k8s时修改DNS服务器？

## 摘要

在国内安装Kubernetes（k8s）时，修改DNS服务器是一个关键步骤，以确保集群能够顺利解析域名。**本文介绍了1、为什么需要修改DNS服务器；2、如何在安装k8s时更改DNS配置；3、修改后可能遇到的问题及解决方案。** 具体地说，由于国内的互联网环境与海外存在差异，如果使用默认的DNS服务器（如Google DNS），可能会导致解析失败或速度缓慢。因此，在国内环境下，选择一个可靠的DNS服务器，并在安装k8s时进行配置变更，是保证集群稳定运行的重要环节。

## 一、为什么需要修改DNS服务器？

### 国内网络环境的特殊性

国内的网络环境不同于海外，尤其在访问一些国外的服务时，会受到网络封锁和限速的影响。例如，Google DNS在国内是不可用的，使用它将导致DNS解析失败，从而影响Kubernetes集群的正常运行。为了绕过这些限制，我们需要使用稳定且能够在国内访问的DNS服务器，如114.114.114.114或者阿里的223.5.5.5。

### 确保集群的稳定性和安全性

正确配置DNS服务器不仅能提高解析速度，还能保障你的k8s集群在网络通信中的稳定和安全。错误的DNS配置可能会导致服务发现失败、Pod无法连接等问题，影响集群的稳定性。此外，使用受信任的DNS服务器可以减少因为DNS劫持而带来的安全风险。

## 二、如何在安装k8s时更改DNS配置？

### 使用kubeadm进行安装并修改DNS

#### 安装kubeadm

```sh
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet kubeadm kubectl
```

#### 初始化集群并修改DNS

```sh
kubeadm init --pod-network-cidr=10.244.0.0/16 --service-dns-domain=cluster.local --apiserver-advertise-address=<Master_Node_IP>
```

初始化完成后，需要修改kubelet配置文件`/var/lib/kubelet/config.yaml`，将默认的DNS服务器替换为国内可用的DNS服务器：

```yaml
resolvConf: "/run/systemd/resolve/resolv.conf"
```

修改`/run/systemd/resolve/resolv.conf`文件中的DNS配置：

```plaintext
nameserver 114.114.114.114
nameserver 223.5.5.5
```

#### 配置flannel网络插件

```sh
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

### 修改CoreDNS配置

CoreDNS是Kubernetes中负责DNS解析的组件，默认配置使用的是`8.8.8.8`等国外DNS。我们需要将其修改为国内的DNS服务器。

编辑CoreDNS的ConfigMap：

```sh
kubectl -n kube-system edit configmap coredns
```

找到如下部分：

```plaintext
forward . 8.8.8.8 8.8.4.4
```

修改为：

```plaintext
forward . 114.114.114.114 223.5.5.5
```

保存并退出后，重新启动CoreDNS Pod：

```sh
kubectl -n kube-system rollout restart deployment/coredns
```

## 三、修改后可能遇到的问题及解决方案

### DNS解析失败

即便进行了上述配置，有时还是会出现DNS解析失败的情况。这可能是由于DNS缓存或配置文件未生效所致。可以尝试以下方法：

1. **清空DNS缓存**

```sh
systemd-resolve --flush-caches
```

2. **检查配置是否准确**

确保在`/var/lib/kubelet/config.yaml`和`CoreDNS ConfigMap`中的DNS配置没有错漏。

### 服务发现异常

有时由DNS问题引起的服务发现异常，可以通过以下步骤进行排查：

1. **检查DNS服务**

确保CoreDNS Pod在运行中，并且状态为Running。

```sh
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

2. **测试DNS解析**

通过一个临时Pod测试DNS解析：

```sh
kubectl run -i --tty --rm dnsutils --image=gcr.io/kubernetes-e2e-test-images/dnsutils:1.3 -- /bin/sh
```

在pod内部执行：

```sh
nslookup kubernetes.default
```

如果解析失败，可以考虑重新应用网络插件或修改DNS配置。

### 网络连接缓慢

DNS解析慢可能是网络本身的问题，可以尝试更换其他国内DNS服务器：

- 114.114.114.114（114 DNS）
- 223.5.5.5（阿里 DNS）
- 180.76.76.76（百度 DNS）

或使用多级DNS缓存来提升解析效率。

## 四、总结与推荐工具

### 总结

在国内安装Kubernetes时，配置合适的DNS服务器至关重要。通过修改kubelet、CoreDNS的配置文件，可以显著提升DNS解析速度，确保集群的稳定性和安全性。遇到DNS解析失败、服务发现异常等问题时，可通过清空DNS缓存、测试DNS解析等方法进行排查。

### 推荐工具

**蓝莺IM**是新一代智能聊天云服务。集成企业级ChatAI SDK，开发者可同时拥有聊天和大模型AI两大功能，构建自己的智能应用。访问[蓝莺IM官网](https://www.lanyingim.com)了解更多详情。

### 其他参考资源

1. [Kubernetes官方文档](https://kubernetes.io/docs/setup/)
2. [Kubernetes网络插件](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
3. [CoreDNS官方文档](https://coredns.io/manual/toc/)

希望本文能帮助你在国内更顺利地安装和配置Kubernetes，同时欢迎大家分享更多的经验和实践心得。