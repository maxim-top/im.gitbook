---
title: floo::BMXPushServiceListener
---

# floo::BMXPushServiceListener

## Public Functions

|              | Name                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener"><strong>BMXPushServiceListener</strong></a>()<br>构造函数</p>                                                                                                                      |
| virtual      | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-~bmxpushservicelistener"><strong>~BMXPushServiceListener</strong></a>()<br>析构函数</p>                                                                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstart"><strong>onPushStart</strong></a>(const std::string bmxToken)<br>Push初始化完成通知。</p>                                                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstop"><strong>onPushStop</strong></a>()<br>Push功能停止通知。</p>                                                                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-oncertretrieved"><strong>onCertRetrieved</strong></a>(const std::string cert)<br>Push初始化完成后获取推送证书。</p>                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onsettags"><strong>onSetTags</strong></a>(const std::string &#x26; operationId)<br>设置用户推送成功回调。</p>                                                                                                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-ongettags"><strong>onGetTags</strong></a>(const std::string &#x26; operationId)<br>获取用户推送成功回调。</p>                                                                                                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-ondeletetags"><strong>onDeleteTags</strong></a>(const std::string &#x26; operationId)<br>删除用户推送成功回调。</p>                                                                                               |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-oncleartags"><strong>onClearTags</strong></a>(const std::string &#x26; operationId)<br>清空用户推送成功回调。</p>                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onreceivepush"><strong>onReceivePush</strong></a>(const BMXMessageList &#x26; list)<br>接收到新的Push通知。</p>                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>发送Push上行消息状态变化通知。</p>                                                                                  |
| void         | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-registerpushservice"><strong>registerPushService</strong></a>(<a href="classfloo_1_1_b_m_x_push_service.md">BMXPushService</a> * service)<br>注册BMXPushServiceListener绑定到的BMXPushService（SDK内部自动注册）</p> |

## Protected Attributes

|                                                          | Name                                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [BMXPushService](classfloo_1_1_b_m_x_push_service.md) \* | [**mService**](classfloo_1_1_b_m_x_push_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXPushServiceListener

```cpp
inline BMXPushServiceListener()
```

构造函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function \~BMXPushServiceListener

```cpp
inline virtual ~BMXPushServiceListener()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onPushStart

```cpp
inline virtual void onPushStart(
    const std::string bmxToken
)
```

Push初始化完成通知。

**Parameters**:

* **bmxToken** 当前push使用bmxToken

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onPushStop

```cpp
inline virtual void onPushStop()
```

Push功能停止通知。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onCertRetrieved

```cpp
inline virtual void onCertRetrieved(
    const std::string cert
)
```

Push初始化完成后获取推送证书。

**Parameters**:

* **cert** 从服务器获取的推送证书

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onSetTags

```cpp
inline virtual void onSetTags(
    const std::string & operationId
)
```

设置用户推送成功回调。

**Parameters**:

* **operationId** 操作id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onGetTags

```cpp
inline virtual void onGetTags(
    const std::string & operationId
)
```

获取用户推送成功回调。

**Parameters**:

* **operationId** 操作id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onDeleteTags

```cpp
inline virtual void onDeleteTags(
    const std::string & operationId
)
```

删除用户推送成功回调。

**Parameters**:

* **operationId** 操作id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onClearTags

```cpp
inline virtual void onClearTags(
    const std::string & operationId
)
```

清空用户推送成功回调。

**Parameters**:

* **operationId** 操作id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onReceivePush

```cpp
inline virtual void onReceivePush(
    const BMXMessageList & list
)
```

接收到新的Push通知。

**Parameters**:

* **list** Push通知列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

发送Push上行消息状态变化通知。

**Parameters**:

* **msg** 发生状态变化的上行消息
* **error** 状态错误码

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function registerPushService

```cpp
inline void registerPushService(
    BMXPushService * service
)
```

注册BMXPushServiceListener绑定到的BMXPushService（SDK内部自动注册）

**Parameters**:

* **service** [BMXPushService](classfloo_1_1_b_m_x_push_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXPushService * mService;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
