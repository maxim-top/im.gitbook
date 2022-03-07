---
title: floo::BMXPushServiceListener

---

# floo::BMXPushServiceListener





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)**()<br>构造函数  |
| virtual | **[~BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md#function-~bmxpushservicelistener)**()<br>析构函数  |
| virtual void | **[onPushStart](classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstart)**(const std::string bmxToken)<br>Push初始化完成通知。  |
| virtual void | **[onPushStop](classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstop)**()<br>Push功能停止通知。  |
| virtual void | **[onCertRetrieved](classfloo_1_1_b_m_x_push_service_listener.md#function-oncertretrieved)**(const std::string cert)<br>Push初始化完成后获取推送证书。  |
| virtual void | **[onSetTags](classfloo_1_1_b_m_x_push_service_listener.md#function-onsettags)**(const std::string & operationId)<br>设置用户推送成功回调。  |
| virtual void | **[onGetTags](classfloo_1_1_b_m_x_push_service_listener.md#function-ongettags)**(const std::string & operationId)<br>获取用户推送成功回调。  |
| virtual void | **[onDeleteTags](classfloo_1_1_b_m_x_push_service_listener.md#function-ondeletetags)**(const std::string & operationId)<br>删除用户推送成功回调。  |
| virtual void | **[onClearTags](classfloo_1_1_b_m_x_push_service_listener.md#function-oncleartags)**(const std::string & operationId)<br>清空用户推送成功回调。  |
| virtual void | **[onReceivePush](classfloo_1_1_b_m_x_push_service_listener.md#function-onreceivepush)**(const BMXMessageList & list)<br>接收到新的Push通知。  |
| virtual void | **[onStatusChanged](classfloo_1_1_b_m_x_push_service_listener.md#function-onstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>发送Push上行消息状态变化通知。  |
| void | **[registerPushService](classfloo_1_1_b_m_x_push_service_listener.md#function-registerpushservice)**([BMXPushService](classfloo_1_1_b_m_x_push_service.md) * service)<br>注册BMXPushServiceListener绑定到的BMXPushService（SDK内部自动注册）  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXPushService](classfloo_1_1_b_m_x_push_service.md) * | **[mService](classfloo_1_1_b_m_x_push_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXPushServiceListener

```cpp
inline BMXPushServiceListener()
```

构造函数 

### function ~BMXPushServiceListener

```cpp
inline virtual ~BMXPushServiceListener()
```

析构函数 

### function onPushStart

```cpp
inline virtual void onPushStart(
    const std::string bmxToken
)
```

Push初始化完成通知。 

**Parameters**: 

  * **bmxToken** 当前push使用bmxToken 


### function onPushStop

```cpp
inline virtual void onPushStop()
```

Push功能停止通知。 

### function onCertRetrieved

```cpp
inline virtual void onCertRetrieved(
    const std::string cert
)
```

Push初始化完成后获取推送证书。 

**Parameters**: 

  * **cert** 从服务器获取的推送证书 


### function onSetTags

```cpp
inline virtual void onSetTags(
    const std::string & operationId
)
```

设置用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onGetTags

```cpp
inline virtual void onGetTags(
    const std::string & operationId
)
```

获取用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onDeleteTags

```cpp
inline virtual void onDeleteTags(
    const std::string & operationId
)
```

删除用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onClearTags

```cpp
inline virtual void onClearTags(
    const std::string & operationId
)
```

清空用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onReceivePush

```cpp
inline virtual void onReceivePush(
    const BMXMessageList & list
)
```

接收到新的Push通知。 

**Parameters**: 

  * **list** Push通知列表 


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


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800