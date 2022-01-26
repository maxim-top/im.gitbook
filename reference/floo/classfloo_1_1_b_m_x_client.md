---
title: floo::BMXClient
summary: 客户端 

---

# floo::BMXClient



客户端 


`#include <bmx_client.h>`

Inherits from [floo::BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| BMXClientPtr | **[create](classfloo_1_1_b_m_x_client.md#function-create)**(BMXSDKConfigPtr config)<br>创建BMXClient  |
| virtual | **[~BMXClient](classfloo_1_1_b_m_x_client.md#function-~bmxclient)**()<br>析构函数  |
| virtual BMXSDKConfigPtr | **[getSDKConfig](classfloo_1_1_b_m_x_client.md#function-getsdkconfig)**() =0<br>获取SDK设置  |
| virtual [BMXUserService](classfloo_1_1_b_m_x_user_service.md) & | **[getUserService](classfloo_1_1_b_m_x_client.md#function-getuserservice)**() =0<br>获取用户Service  |
| virtual [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) & | **[getChatService](classfloo_1_1_b_m_x_client.md#function-getchatservice)**() =0<br>获取聊天Service  |
| virtual [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) & | **[getGroupService](classfloo_1_1_b_m_x_client.md#function-getgroupservice)**() =0<br>获取群组Service  |
| virtual [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) & | **[getRosterService](classfloo_1_1_b_m_x_client.md#function-getrosterservice)**() =0<br>获取好友Service  |
| virtual [BMXPushService](classfloo_1_1_b_m_x_push_service.md) & | **[getPushService](classfloo_1_1_b_m_x_client.md#function-getpushservice)**() =0<br>获取推送Service  |
| virtual BMXErrorCode | **[signUpNewUser](classfloo_1_1_b_m_x_client.md#function-signupnewuser)**(const std::string & username, const std::string & password, BMXUserProfilePtr & bmxUserProfilePtr) =0<br>注册新用户，username和password是必填参数  |
| virtual BMXErrorCode | **[signInByName](classfloo_1_1_b_m_x_client.md#function-signinbyname)**(const std::string & name, const std::string & password) =0<br>通过用户名登录  |
| virtual BMXErrorCode | **[signInById](classfloo_1_1_b_m_x_client.md#function-signinbyid)**(int64_t , const std::string & password) =0<br>通过用户ID登录  |
| virtual BMXErrorCode | **[fastSignInByName](classfloo_1_1_b_m_x_client.md#function-fastsigninbyname)**(const std::string & name, const std::string & password) =0<br>通过用户名快速登录（要求之前成功登录过，登录速度较快）  |
| virtual BMXErrorCode | **[fastSignInById](classfloo_1_1_b_m_x_client.md#function-fastsigninbyid)**(int64_t uid, const std::string & password) =0<br>通过用户ID快速登录（要求之前成功登录过，登录速度较快）  |
| virtual BMXErrorCode | **[signOut](classfloo_1_1_b_m_x_client.md#function-signout)**(int64_t uid =0, bool ignoreUnbindDevice =false) =0<br>退出登录  |
| virtual BMXConnectStatus | **[connectStatus](classfloo_1_1_b_m_x_client.md#function-connectstatus)**() =0<br>获取当前和服务器的连接状态  |
| virtual BMXSignInStatus | **[signInStatus](classfloo_1_1_b_m_x_client.md#function-signinstatus)**() =0<br>获取当前的登录状态  |
| virtual void | **[reconnect](classfloo_1_1_b_m_x_client.md#function-reconnect)**() =0<br>强制重新连接  |
| virtual void | **[onNetworkChanged](classfloo_1_1_b_m_x_client.md#function-onnetworkchanged)**(BMXNetworkType type, bool reconnect) =0<br>处理网络状态发送变化  |
| virtual void | **[disconnect](classfloo_1_1_b_m_x_client.md#function-disconnect)**() =0<br>断开网络连接  |
| virtual BMXErrorCode | **[changeAppId](classfloo_1_1_b_m_x_client.md#function-changeappid)**(const std::string & appId, const std::string & appSecret ="") =0<br>更改SDK的appId，本操作会同时更新BMXConfig中的appId。  |
| virtual BMXErrorCode | **[initializeServerConfig](classfloo_1_1_b_m_x_client.md#function-initializeserverconfig)**(bool isLocal) =0<br>获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。  |
| virtual void | **[sendMessage](classfloo_1_1_b_m_x_client.md#function-sendmessage)**(BMXMessagePtr msg) =0<br>发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXClient](classfloo_1_1_b_m_x_client.md#function-bmxclient)**() |

## Additional inherited members

**Public Functions inherited from [floo::BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md#function-~bmxnetworklistener)**() |


## Public Functions Documentation

### function create

```cpp
static BMXClientPtr create(
    BMXSDKConfigPtr config
)
```

创建BMXClient 

**Parameters**: 

  * **config** 客户端本地已经创建好的BMXSDKConfig SDK配置对象 


**Return**: BMXClientPtr 

### function ~BMXClient

```cpp
inline virtual ~BMXClient()
```

析构函数 

### function getSDKConfig

```cpp
virtual BMXSDKConfigPtr getSDKConfig() =0
```

获取SDK设置 

**Return**: BMXSDKConfigPtr 

### function getUserService

```cpp
virtual BMXUserService & getUserService() =0
```

获取用户Service 

**Return**: [BMXUserService](classfloo_1_1_b_m_x_user_service.md)

### function getChatService

```cpp
virtual BMXChatService & getChatService() =0
```

获取聊天Service 

**Return**: [BMXChatService](classfloo_1_1_b_m_x_chat_service.md)

### function getGroupService

```cpp
virtual BMXGroupService & getGroupService() =0
```

获取群组Service 

**Return**: [BMXGroupService](classfloo_1_1_b_m_x_group_service.md)

### function getRosterService

```cpp
virtual BMXRosterService & getRosterService() =0
```

获取好友Service 

**Return**: [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)

### function getPushService

```cpp
virtual BMXPushService & getPushService() =0
```

获取推送Service 

**Return**: [BMXPushService](classfloo_1_1_b_m_x_push_service.md)

### function signUpNewUser

```cpp
virtual BMXErrorCode signUpNewUser(
    const std::string & username,
    const std::string & password,
    BMXUserProfilePtr & bmxUserProfilePtr
) =0
```

注册新用户，username和password是必填参数 

**Parameters**: 

  * **username** 用户名 
  * **password** 用户密码 
  * **bmxUserProfilePtr** 注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared_ptr对象即可。 


**Return**: BMXErrorCode 

### function signInByName

```cpp
virtual BMXErrorCode signInByName(
    const std::string & name,
    const std::string & password
) =0
```

通过用户名登录 

**Parameters**: 

  * **name** 用户名 
  * **password** 用户密码 


**Return**: BMXErrorCode 

### function signInById

```cpp
virtual BMXErrorCode signInById(
    int64_t ,
    const std::string & password
) =0
```

通过用户ID登录 

**Parameters**: 

  * **int64_t** 用户id 
  * **password** 用户密码 


**Return**: BMXErrorCode 

### function fastSignInByName

```cpp
virtual BMXErrorCode fastSignInByName(
    const std::string & name,
    const std::string & password
) =0
```

通过用户名快速登录（要求之前成功登录过，登录速度较快） 

**Parameters**: 

  * **name** 用户名 
  * **password** 用户密码(用于sdk在内部token到期时自动更新用户token) 


**Return**: BMXErrorCode 

### function fastSignInById

```cpp
virtual BMXErrorCode fastSignInById(
    int64_t uid,
    const std::string & password
) =0
```

通过用户ID快速登录（要求之前成功登录过，登录速度较快） 

**Parameters**: 

  * **uid** 用户id 
  * **password** 用户密码(用于sdk在内部token到期时自动更新用户token) 


**Return**: BMXErrorCode 

### function signOut

```cpp
virtual BMXErrorCode signOut(
    int64_t uid =0,
    bool ignoreUnbindDevice =false
) =0
```

退出登录 

**Parameters**: 

  * **uid** 退出用户的uid（默认输入0则退出当前登陆用户） 
  * **ignoreUnbindDevice** 用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true 


**Return**: BMXErrorCode 

### function connectStatus

```cpp
virtual BMXConnectStatus connectStatus() =0
```

获取当前和服务器的连接状态 

**Return**: BMXConnectStatus 

### function signInStatus

```cpp
virtual BMXSignInStatus signInStatus() =0
```

获取当前的登录状态 

**Return**: BMXSignInStatus 

### function reconnect

```cpp
virtual void reconnect() =0
```

强制重新连接 

### function onNetworkChanged

```cpp
virtual void onNetworkChanged(
    BMXNetworkType type,
    bool reconnect
) =0
```

处理网络状态发送变化 

**Parameters**: 

  * **type** 变化后的网络类型 
  * **reconnect** 网络是否需要重连 


**Reimplements**: [floo::BMXNetworkListener::onNetworkChanged](classfloo_1_1_b_m_x_network_listener.md#function-onnetworkchanged)


### function disconnect

```cpp
virtual void disconnect() =0
```

断开网络连接 

### function changeAppId

```cpp
virtual BMXErrorCode changeAppId(
    const std::string & appId,
    const std::string & appSecret =""
) =0
```

更改SDK的appId，本操作会同时更新BMXConfig中的appId。 

**Parameters**: 

  * **appId** 新变更的appId 


**Return**: BMXErrorCode 

### function initializeServerConfig

```cpp
virtual BMXErrorCode initializeServerConfig(
    bool isLocal
) =0
```

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。 

**Parameters**: 

  * **isLocal** 为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。 


**Return**: BMXErrorCode 

### function sendMessage

```cpp
virtual void sendMessage(
    BMXMessagePtr msg
) =0
```

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。 

**Parameters**: 

  * **msg** 发送的消息 


## Protected Functions Documentation

### function BMXClient

```cpp
BMXClient()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800