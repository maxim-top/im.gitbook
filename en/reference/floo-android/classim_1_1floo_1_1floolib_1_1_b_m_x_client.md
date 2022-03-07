---
title: im::floo::floolib::BMXClient
summary: Client 

---

# im::floo::floolib::BMXClient



Client 

Inherits from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-delete)**() |
| [BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md) | **[getSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getsdkconfig)**()<br>Get SDK settings  |
| [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) | **[getUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getuserservice)**()<br>Get user Service  |
| [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) | **[getChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatservice)**()<br>Get chat Service  |
| [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) | **[getGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupservice)**()<br>Get group Service  |
| [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) | **[getRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrosterservice)**()<br>Get roster Service  |
| [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) | **[getPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushservice)**()<br>Get push Service  |
| [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md) | **[getUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getusermanager)**()<br>Get user Manager  |
| [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md) | **[getChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatmanager)**()<br>Get chat Manager  |
| [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md) | **[getGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupmanager)**()<br>Get group Manager  |
| [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md) | **[getRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrostermanager)**()<br>Get roster Manager  |
| [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md) | **[getPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushmanager)**()<br>Get push Manager  |
| [BMXErrorCode] | **[signUpNewUser](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signupnewuser)**(String username, String password, [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) bmxUserProfilePtr)<br>To register a new user, username and password are required  |
| [BMXErrorCode] | **[signInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyname)**(String name, String password)<br>Login by username  |
| [BMXErrorCode] | **[signInById](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyid)**(long arg0, String password)<br>Login by user ID  |
| [BMXErrorCode] | **[fastSignInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyname)**(String name, String password)<br>Quick login by username (requires a successful previous login, faster login)  |
| [BMXErrorCode] | **[fastSignInById](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyid)**(long uid, String password)<br>Quick login by user ID (requires a successful previous login, faster login)  |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**(long uid, boolean ignoreUnbindDevice)<br>Log out  |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**(long uid) |
| [BMXErrorCode] | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)**() |
| [BMXConnectStatus] | **[connectStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-connectstatus)**()<br>Get the current connection state with server  |
| [BMXSignInStatus] | **[signInStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinstatus)**()<br>Get the current login state  |
| void | **[reconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-reconnect)**()<br>Force reconnection  |
| void | **[onNetworkChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-onnetworkchanged)**([BMXNetworkType] type, boolean reconnect)<br>Process network changes in messaging  |
| void | **[disconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-disconnect)**()<br>Disconnect  |
| [BMXErrorCode] | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid)**(String appId, String appSecret)<br>Change the appId of SDK, which also update the appId in BMXConfig.  |
| [BMXErrorCode] | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid)**(String appId)<br>Change the appId of SDK, which also update the appId in BMXConfig.  |
| [BMXErrorCode] | **[initializeServerConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-initializeserverconfig)**(boolean isLocal)<br>Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.  |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-sendmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.  |
| [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-create)**([BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md) config)<br>Create BMXClient  |

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

Get SDK settings 

**Return**: BMXSDKConfigPtr 

### function getUserService

```java
inline BMXUserService getUserService()
```

Get user Service 

**Return**: [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)

### function getChatService

```java
inline BMXChatService getChatService()
```

Get chat Service 

**Return**: [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)

### function getGroupService

```java
inline BMXGroupService getGroupService()
```

Get group Service 

**Return**: [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)

### function getRosterService

```java
inline BMXRosterService getRosterService()
```

Get roster Service 

**Return**: [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md)

### function getPushService

```java
inline BMXPushService getPushService()
```

Get push Service 

**Return**: [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)

### function getUserManager

```java
inline BMXUserManager getUserManager()
```

Get user Manager 

**Return**: [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)

### function getChatManager

```java
inline BMXChatManager getChatManager()
```

Get chat Manager 

**Return**: [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)

### function getGroupManager

```java
inline BMXGroupManager getGroupManager()
```

Get group Manager 

**Return**: [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)

### function getRosterManager

```java
inline BMXRosterManager getRosterManager()
```

Get roster Manager 

**Return**: [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md)

### function getPushManager

```java
inline BMXPushManager getPushManager()
```

Get push Manager 

**Return**: [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)

### function signUpNewUser

```java
inline BMXErrorCode signUpNewUser(
    String username,
    String password,
    BMXUserProfile bmxUserProfilePtr
)
```

To register a new user, username and password are required 

**Parameters**: 

  * **username** Username 
  * **password** User password 
  * **bmxUserProfilePtr** After successful registration, get the profile of the newly registered user from this function, and initially passed in a pointing-to-empty shared_ptr object. 


**Return**: [BMXErrorCode]

### function signInByName

```java
inline BMXErrorCode signInByName(
    String name,
    String password
)
```

Login by username 

**Parameters**: 

  * **name** Username 
  * **password** User password 


**Return**: [BMXErrorCode]

### function signInById

```java
inline BMXErrorCode signInById(
    long arg0,
    String password
)
```

Login by user ID 

**Parameters**: 

  * **arg0** User id 
  * **password** User password 


**Return**: [BMXErrorCode]

### function fastSignInByName

```java
inline BMXErrorCode fastSignInByName(
    String name,
    String password
)
```

Quick login by username (requires a successful previous login, faster login) 

**Parameters**: 

  * **name** Username 
  * **password** User password (for sdk to automatically update user token when internal token expires) 


**Return**: [BMXErrorCode]

### function fastSignInById

```java
inline BMXErrorCode fastSignInById(
    long uid,
    String password
)
```

Quick login by user ID (requires a successful previous login, faster login) 

**Parameters**: 

  * **uid** User id 
  * **password** User password (for sdk to automatically update user token when internal token expires) 


**Return**: [BMXErrorCode]

### function signOut

```java
inline BMXErrorCode signOut(
    long uid,
    boolean ignoreUnbindDevice
)
```

Log out 

**Parameters**: 

  * **uid** UID of logged out user (default 0 to logout the current user) 
  * **ignoreUnbindDevice** Whether the unbind device operation is ignored when the user logout. Set to true when server's unbinding device operation is ignored and forced to logout directly when some servers are inaccessible. 


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

Get the current connection state with server 

**Return**: [BMXConnectStatus]

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

Get the current login state 

**Return**: [BMXSignInStatus]

### function reconnect

```java
inline void reconnect()
```

Force reconnection 

### function onNetworkChanged

```java
inline void onNetworkChanged(
    BMXNetworkType type,
    boolean reconnect
)
```

Process network changes in messaging 

**Parameters**: 

  * **type** Changed network type 
  * **reconnect** Network needs to reconnect or not 


**Reimplements**: [im::floo::floolib::BMXNetworkListener::onNetworkChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-onnetworkchanged)


### function disconnect

```java
inline void disconnect()
```

Disconnect 

### function changeAppId

```java
inline BMXErrorCode changeAppId(
    String appId,
    String appSecret
)
```

Change the appId of SDK, which also update the appId in BMXConfig. 

**Parameters**: 

  * **appId** Newly changed appId 
  * **appSecret** Newly changed appSecret 


### function changeAppId

```java
inline BMXErrorCode changeAppId(
    String appId
)
```

Change the appId of SDK, which also update the appId in BMXConfig. 

**Parameters**: 

  * **appId** Newly changed appId 


### function initializeServerConfig

```java
inline BMXErrorCode initializeServerConfig(
    boolean isLocal
)
```

Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in. 

**Parameters**: 

  * **isLocal** True to use locally cached DNS configuration, false to get the latest configuration from server. 


### function sendMessage

```java
inline void sendMessage(
    BMXMessage msg
)
```

When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself. 

**Parameters**: 

  * **msg** Message to be sent 


### function create

```java
static inline BMXClient create(
    BMXSDKConfig config
)
```

Create BMXClient 

**Parameters**: 

  * **config** BMXSDKConfig SDK configuration object created by local client-side already 


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