---
title: im::floo::floolib::BMXClient
summary: 客户端 

---

# im::floo::floolib::BMXClient



客户端 

Inherits from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-delete)**() |
| [BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md) | **[getSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getsdkconfig)**()<br>获取SDK设置  |
| [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) | **[getUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getuserservice)**()<br>获取用户Service  |
| [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) | **[getChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatservice)**()<br>获取聊天Service  |
| [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) | **[getGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupservice)**()<br>获取群组Service  |
| [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) | **[getRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrosterservice)**()<br>获取好友Service  |
| [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) | **[getPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushservice)**()<br>获取推送Service  |
| [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md) | **[getUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getusermanager)**()<br>获取用户Manager  |
| [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md) | **[getChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatmanager)**()<br>获取聊天Manager  |
| [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md) | **[getGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupmanager)**()<br>获取群组Manager  |
| [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md) | **[getRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrostermanager)**()<br>获取好友Manager  |
| [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md) | **[getPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushmanager)**()<br>获取推送Manager  |
| [BMXErrorCode] | **[signUpNewUser](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signupnewuser)**(String username, String password, [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) bmxUserProfilePtr)<br>注册新用户，username和password是必填参数  |
| [BMXErrorCode] | **[signInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyname)**(String name, String password)<br>通过用户名登录  |
| [BMXErrorCode] | **[signInById](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyid)**(long arg0, String password)<br>通过用户ID登录  |
| [BMXErrorCode] | **[fastSignInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyname)**(String name, String password)<br>通过用户名快速登录（要求之前成功登录过，登录速度较快）  |
| [BMXErrorCode] | **[fastSignInById](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyid)**(long uid, String password)<br>通过用户ID快速登录（要求之前成功登录过，登录速度较快）  |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**(long uid, boolean ignoreUnbindDevice)<br>退出登录  |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**(long uid) |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**() |
| [BMXConnectStatus] | **[connectStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-connectstatus)**()<br>获取当前和服务器的连接状态  |
| [BMXSignInStatus] | **[signInStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinstatus)**()<br>获取当前的登录状态  |
| void | **[reconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-reconnect)**()<br>强制重新连接  |
| void | **[onNetworkChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-onnetworkchanged)**([BMXNetworkType] type, boolean reconnect)<br>处理网络状态发送变化  |
| void | **[disconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-disconnect)**()<br>断开网络连接  |
| [BMXErrorCode] | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid)**(String appId, String appSecret)<br>更改SDK的appId，本操作会同时更新BMXConfig中的appId。  |
| [BMXErrorCode] | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid)**(String appId)<br>更改SDK的appId，本操作会同时更新BMXConfig中的appId。  |
| [BMXErrorCode] | **[initializeServerConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-initializeserverconfig)**(boolean isLocal)<br>获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。  |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-sendmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。  |
| [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-create)**([BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md) config)<br>创建BMXClient  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-bmxclient)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getcptr)**([BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) obj) |

## Additional inherited members

**Public Functions inherited from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)**

|                | Name           |
| -------------- | -------------- |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigtakeownership)**() |
| | **[BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-bmxnetworklistener)**() |

**Protected Functions inherited from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-bmxnetworklistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigdirectordisconnect)**() |


## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplements**: [im::floo::floolib::BMXNetworkListener::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-delete)


### function getSDKConfig

```java
inline BMXSDKConfig getSDKConfig()
```

获取SDK设置 

**Return**: BMXSDKConfigPtr 

### function getUserService

```java
inline BMXUserService getUserService()
```

获取用户Service 

**Return**: [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)

### function getChatService

```java
inline BMXChatService getChatService()
```

获取聊天Service 

**Return**: [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)

### function getGroupService

```java
inline BMXGroupService getGroupService()
```

获取群组Service 

**Return**: [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)

### function getRosterService

```java
inline BMXRosterService getRosterService()
```

获取好友Service 

**Return**: [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md)

### function getPushService

```java
inline BMXPushService getPushService()
```

获取推送Service 

**Return**: [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)

### function getUserManager

```java
inline BMXUserManager getUserManager()
```

获取用户Manager 

**Return**: [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)

### function getChatManager

```java
inline BMXChatManager getChatManager()
```

获取聊天Manager 

**Return**: [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)

### function getGroupManager

```java
inline BMXGroupManager getGroupManager()
```

获取群组Manager 

**Return**: [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)

### function getRosterManager

```java
inline BMXRosterManager getRosterManager()
```

获取好友Manager 

**Return**: [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md)

### function getPushManager

```java
inline BMXPushManager getPushManager()
```

获取推送Manager 

**Return**: [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)

### function signUpNewUser

```java
inline BMXErrorCode signUpNewUser(
    String username,
    String password,
    BMXUserProfile bmxUserProfilePtr
)
```

注册新用户，username和password是必填参数 

**Parameters**: 

  * **username** 用户名 
  * **password** 用户密码 
  * **bmxUserProfilePtr** 注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared_ptr对象即可。 


**Return**: [BMXErrorCode]

### function signInByName

```java
inline BMXErrorCode signInByName(
    String name,
    String password
)
```

通过用户名登录 

**Parameters**: 

  * **name** 用户名 
  * **password** 用户密码 


**Return**: [BMXErrorCode]

### function signInById

```java
inline BMXErrorCode signInById(
    long arg0,
    String password
)
```

通过用户ID登录 

**Parameters**: 

  * **arg0** 用户id 
  * **password** 用户密码 


**Return**: [BMXErrorCode]

### function fastSignInByName

```java
inline BMXErrorCode fastSignInByName(
    String name,
    String password
)
```

通过用户名快速登录（要求之前成功登录过，登录速度较快） 

**Parameters**: 

  * **name** 用户名 
  * **password** 用户密码(用于sdk在内部token到期时自动更新用户token) 


**Return**: [BMXErrorCode]

### function fastSignInById

```java
inline BMXErrorCode fastSignInById(
    long uid,
    String password
)
```

通过用户ID快速登录（要求之前成功登录过，登录速度较快） 

**Parameters**: 

  * **uid** 用户id 
  * **password** 用户密码(用于sdk在内部token到期时自动更新用户token) 


**Return**: [BMXErrorCode]

### function signOut

```java
inline BMXErrorCode signOut(
    long uid,
    boolean ignoreUnbindDevice
)
```

退出登录 

**Parameters**: 

  * **uid** 退出用户的uid（默认输入0则退出当前登陆用户） 
  * **ignoreUnbindDevice** 用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true 


**Return**: [BMXErrorCode]

### function signOut

```java
inline BMXErrorCode signOut(
    long uid
)
```


### function signOut

```java
inline BMXErrorCode signOut()
```


### function connectStatus

```java
inline BMXConnectStatus connectStatus()
```

获取当前和服务器的连接状态 

**Return**: [BMXConnectStatus]

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

获取当前的登录状态 

**Return**: [BMXSignInStatus]

### function reconnect

```java
inline void reconnect()
```

强制重新连接 

### function onNetworkChanged

```java
inline void onNetworkChanged(
    BMXNetworkType type,
    boolean reconnect
)
```

处理网络状态发送变化 

**Parameters**: 

  * **type** 变化后的网络类型 
  * **reconnect** 网络是否需要重连 


**Reimplements**: [im::floo::floolib::BMXNetworkListener::onNetworkChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-onnetworkchanged)


### function disconnect

```java
inline void disconnect()
```

断开网络连接 

### function changeAppId

```java
inline BMXErrorCode changeAppId(
    String appId,
    String appSecret
)
```

更改SDK的appId，本操作会同时更新BMXConfig中的appId。 

**Parameters**: 

  * **appId** 新变更的appId 
  * **appSecret** 新变更的appSecret 


### function changeAppId

```java
inline BMXErrorCode changeAppId(
    String appId
)
```

更改SDK的appId，本操作会同时更新BMXConfig中的appId。 

**Parameters**: 

  * **appId** 新变更的appId 


### function initializeServerConfig

```java
inline BMXErrorCode initializeServerConfig(
    boolean isLocal
)
```

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。 

**Parameters**: 

  * **isLocal** 为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。 


### function sendMessage

```java
inline void sendMessage(
    BMXMessage msg
)
```

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。 

**Parameters**: 

  * **msg** 发送的消息 


### function create

```java
static inline BMXClient create(
    BMXSDKConfig config
)
```

创建BMXClient 

**Parameters**: 

  * **config** 客户端本地已经创建好的BMXSDKConfig SDK配置对象 


**Return**: BMXClientPtr 

## Protected Functions Documentation

### function BMXClient

```java
inline BMXClient(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXNetworkListener::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXClient obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800