---
title: im::floo::floolib::BMXClient
summary: 客户端
---

# im::floo::floolib::BMXClient

客户端

Inherits from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

## Public Functions

|                                                                            | Name                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                          | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-delete)()                                                                                                                                                                                                                                         |
| [BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md)       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getsdkconfig"><strong>getSDKConfig</strong></a>()<br>获取SDK设置</p>                                                                                                                                                                                   |
| [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getuserservice"><strong>getUserService</strong></a>()<br>获取用户Service</p>                                                                                                                                                                           |
| [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatservice"><strong>getChatService</strong></a>()<br>获取聊天Service</p>                                                                                                                                                                           |
| [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupservice"><strong>getGroupService</strong></a>()<br>获取群组Service</p>                                                                                                                                                                         |
| [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrosterservice"><strong>getRosterService</strong></a>()<br>获取好友Service</p>                                                                                                                                                                       |
| [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushservice"><strong>getPushService</strong></a>()<br>获取推送Service</p>                                                                                                                                                                           |
| [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getusermanager"><strong>getUserManager</strong></a>()<br>获取用户Manager</p>                                                                                                                                                                           |
| [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatmanager"><strong>getChatManager</strong></a>()<br>获取聊天Manager</p>                                                                                                                                                                           |
| [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupmanager"><strong>getGroupManager</strong></a>()<br>获取群组Manager</p>                                                                                                                                                                         |
| [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrostermanager"><strong>getRosterManager</strong></a>()<br>获取好友Manager</p>                                                                                                                                                                       |
| [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushmanager"><strong>getPushManager</strong></a>()<br>获取推送Manager</p>                                                                                                                                                                           |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signupnewuser"><strong>signUpNewUser</strong></a>(String username, String password, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> bmxUserProfilePtr)<br>注册新用户，username和password是必填参数</p>                       |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyname"><strong>signInByName</strong></a>(String name, String password)<br>通过用户名登录</p>                                                                                                                                                       |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyid"><strong>signInById</strong></a>(long arg0, String password)<br>通过用户ID登录</p>                                                                                                                                                            |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyname"><strong>fastSignInByName</strong></a>(String name, String password)<br>通过用户名快速登录（要求之前成功登录过，登录速度较快）</p>                                                                                                                           |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyid"><strong>fastSignInById</strong></a>(long uid, String password)<br>通过用户ID快速登录（要求之前成功登录过，登录速度较快）</p>                                                                                                                                 |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout"><strong>signOut</strong></a>(long uid, boolean ignoreUnbindDevice)<br>退出登录</p>                                                                                                                                                            |
| \[BMXErrorCode]                                                            | [**signOut**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)(long uid)                                                                                                                                                                                                                               |
| \[BMXErrorCode]                                                            | [**signOut**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)()                                                                                                                                                                                                                                       |
| \[BMXConnectStatus]                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-connectstatus"><strong>connectStatus</strong></a>()<br>获取当前和服务器的连接状态</p>                                                                                                                                                                           |
| \[BMXSignInStatus]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinstatus"><strong>signInStatus</strong></a>()<br>获取当前的登录状态</p>                                                                                                                                                                                 |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-reconnect"><strong>reconnect</strong></a>()<br>强制重新连接</p>                                                                                                                                                                                          |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-onnetworkchanged"><strong>onNetworkChanged</strong></a>([BMXNetworkType] type, boolean reconnect)<br>处理网络状态发送变化</p>                                                                                                                                |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-disconnect"><strong>disconnect</strong></a>()<br>断开网络连接</p>                                                                                                                                                                                        |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid"><strong>changeAppId</strong></a>(String appId, String appSecret)<br>更改SDK的appId，本操作会同时更新BMXConfig中的appId。</p>                                                                                                                         |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid"><strong>changeAppId</strong></a>(String appId)<br>更改SDK的appId，本操作会同时更新BMXConfig中的appId。</p>                                                                                                                                           |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-initializeserverconfig"><strong>initializeServerConfig</strong></a>(boolean isLocal)<br>获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。</p>                                                                                                       |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-sendmessage"><strong>sendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。</p> |
| [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md)                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-create"><strong>create</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md">BMXSDKConfig</a> config)<br>创建BMXClient</p>                                                                                                     |

## Protected Functions

|      | Name                                                                                                                                            |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXClient**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-bmxclient)(long cPtr, boolean cMemoryOwn)                               |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-finalize)()                                                              |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getcptr)([BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) obj) |

## Additional inherited members

**Public Functions inherited from** [**im.floo.floolib.BMXNetworkListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

|      | Name                                                                                                                 |
| ---- | -------------------------------------------------------------------------------------------------------------------- |
| void | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigreleaseownership)() |
| void | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigtakeownership)()       |
|      | [**BMXNetworkListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-bmxnetworklistener)()     |

**Protected Functions inherited from** [**im.floo.floolib.BMXNetworkListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

|      | Name                                                                                                                                          |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXNetworkListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-bmxnetworklistener)(long cPtr, boolean cMemoryOwn) |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-swigdirectordisconnect)()                      |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXNetworkListener::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-delete)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getSDKConfig

```java
inline BMXSDKConfig getSDKConfig()
```

获取SDK设置

**Return**: BMXSDKConfigPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getUserService

```java
inline BMXUserService getUserService()
```

获取用户Service

**Return**: [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getChatService

```java
inline BMXChatService getChatService()
```

获取聊天Service

**Return**: [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getGroupService

```java
inline BMXGroupService getGroupService()
```

获取群组Service

**Return**: [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getRosterService

```java
inline BMXRosterService getRosterService()
```

获取好友Service

**Return**: [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getPushService

```java
inline BMXPushService getPushService()
```

获取推送Service

**Return**: [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getUserManager

```java
inline BMXUserManager getUserManager()
```

获取用户Manager

**Return**: [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getChatManager

```java
inline BMXChatManager getChatManager()
```

获取聊天Manager

**Return**: [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getGroupManager

```java
inline BMXGroupManager getGroupManager()
```

获取群组Manager

**Return**: [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getRosterManager

```java
inline BMXRosterManager getRosterManager()
```

获取好友Manager

**Return**: [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getPushManager

```java
inline BMXPushManager getPushManager()
```

获取推送Manager

**Return**: [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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
* **bmxUserProfilePtr** 注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared\_ptr对象即可。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function signOut

```java
inline BMXErrorCode signOut(
    long uid
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function signOut

```java
inline BMXErrorCode signOut()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function connectStatus

```java
inline BMXConnectStatus connectStatus()
```

获取当前和服务器的连接状态

**Return**: \[BMXConnectStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

获取当前的登录状态

**Return**: \[BMXSignInStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function reconnect

```java
inline void reconnect()
```

强制重新连接

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function disconnect

```java
inline void disconnect()
```

断开网络连接

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function changeAppId

```java
inline BMXErrorCode changeAppId(
    String appId
)
```

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

**Parameters**:

* **appId** 新变更的appId

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function initializeServerConfig

```java
inline BMXErrorCode initializeServerConfig(
    boolean isLocal
)
```

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

**Parameters**:

* **isLocal** 为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function sendMessage

```java
inline void sendMessage(
    BMXMessage msg
)
```

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。

**Parameters**:

* **msg** 发送的消息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function BMXClient

```java
inline BMXClient(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXNetworkListener::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-finalize)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXClient obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
