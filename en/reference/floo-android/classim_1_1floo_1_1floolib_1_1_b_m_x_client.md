---
title: im::floo::floolib::BMXClient
summary: Client
---

# im::floo::floolib::BMXClient

Client

Inherits from [im.floo.floolib.BMXNetworkListener](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md)

## Public Functions

|                                                                            | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                          | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-delete)()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md)       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getsdkconfig"><strong>getSDKConfig</strong></a>()<br>Get SDK settings</p>                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getuserservice"><strong>getUserService</strong></a>()<br>Get user Service</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatservice"><strong>getChatService</strong></a>()<br>Get chat Service</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupservice"><strong>getGroupService</strong></a>()<br>Get group Service</p>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrosterservice"><strong>getRosterService</strong></a>()<br>Get roster Service</p>                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushservice"><strong>getPushService</strong></a>()<br>Get push Service</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getusermanager"><strong>getUserManager</strong></a>()<br>Get user Manager</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getchatmanager"><strong>getChatManager</strong></a>()<br>Get chat Manager</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getgroupmanager"><strong>getGroupManager</strong></a>()<br>Get group Manager</p>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getrostermanager"><strong>getRosterManager</strong></a>()<br>Get roster Manager</p>                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md)     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-getpushmanager"><strong>getPushManager</strong></a>()<br>Get push Manager</p>                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signupnewuser"><strong>signUpNewUser</strong></a>(String username, String password, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> bmxUserProfilePtr)<br>To register a new user, username and password are required</p>                                                                                                                                                                                                                                           |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyname"><strong>signInByName</strong></a>(String name, String password)<br>Login by username</p>                                                                                                                                                                                                                                                                                                                                                                                               |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinbyid"><strong>signInById</strong></a>(long arg0, String password)<br>Login by user ID</p>                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyname"><strong>fastSignInByName</strong></a>(String name, String password)<br>Quick login by username (requires a successful previous login, faster login)</p>                                                                                                                                                                                                                                                                                                                            |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-fastsigninbyid"><strong>fastSignInById</strong></a>(long uid, String password)<br>Quick login by user ID (requires a successful previous login, faster login)</p>                                                                                                                                                                                                                                                                                                                                    |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout"><strong>signOut</strong></a>(long uid, boolean ignoreUnbindDevice)<br>Log out</p>                                                                                                                                                                                                                                                                                                                                                                                                           |
| \[BMXErrorCode]                                                            | [**signOut**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)(long uid)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \[BMXErrorCode]                                                            | [**signOut**](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signout)()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \[BMXConnectStatus]                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-connectstatus"><strong>connectStatus</strong></a>()<br>Get the current connection state with server</p>                                                                                                                                                                                                                                                                                                                                                                                              |
| \[BMXSignInStatus]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-signinstatus"><strong>signInStatus</strong></a>()<br>Get the current login state</p>                                                                                                                                                                                                                                                                                                                                                                                                                 |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-reconnect"><strong>reconnect</strong></a>()<br>Force reconnection</p>                                                                                                                                                                                                                                                                                                                                                                                                                                |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-onnetworkchanged"><strong>onNetworkChanged</strong></a>([BMXNetworkType] type, boolean reconnect)<br>Process network changes in messaging</p>                                                                                                                                                                                                                                                                                                                                                        |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-disconnect"><strong>disconnect</strong></a>()<br>Disconnect</p>                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid"><strong>changeAppId</strong></a>(String appId, String appSecret)<br>Change the appId of SDK, which also update the appId in BMXConfig.</p>                                                                                                                                                                                                                                                                                                                                              |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-changeappid"><strong>changeAppId</strong></a>(String appId)<br>Change the appId of SDK, which also update the appId in BMXConfig.</p>                                                                                                                                                                                                                                                                                                                                                                |
| \[BMXErrorCode]                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-initializeserverconfig"><strong>initializeServerConfig</strong></a>(boolean isLocal)<br>Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.</p>                                                                                                                                                                                                                 |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-sendmessage"><strong>sendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.</p> |
| [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md)                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_client.md#function-create"><strong>create</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md">BMXSDKConfig</a> config)<br>Create BMXClient</p>                                                                                                                                                                                                                                                                                                                                                  |

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

Get SDK settings

**Return**: BMXSDKConfigPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getUserService

```java
inline BMXUserService getUserService()
```

Get user Service

**Return**: [BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getChatService

```java
inline BMXChatService getChatService()
```

Get chat Service

**Return**: [BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getGroupService

```java
inline BMXGroupService getGroupService()
```

Get group Service

**Return**: [BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getRosterService

```java
inline BMXRosterService getRosterService()
```

Get roster Service

**Return**: [BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getPushService

```java
inline BMXPushService getPushService()
```

Get push Service

**Return**: [BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getUserManager

```java
inline BMXUserManager getUserManager()
```

Get user Manager

**Return**: [BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getChatManager

```java
inline BMXChatManager getChatManager()
```

Get chat Manager

**Return**: [BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getGroupManager

```java
inline BMXGroupManager getGroupManager()
```

Get group Manager

**Return**: [BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getRosterManager

```java
inline BMXRosterManager getRosterManager()
```

Get roster Manager

**Return**: [BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function getPushManager

```java
inline BMXPushManager getPushManager()
```

Get push Manager

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

To register a new user, username and password are required

**Parameters**:

* **username** Username
* **password** User password
* **bmxUserProfilePtr** After successful registration, get the profile of the newly registered user from this function, and initially passed in a pointing-to-empty shared\_ptr object.

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

Login by username

**Parameters**:

* **name** Username
* **password** User password

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

Login by user ID

**Parameters**:

* **arg0** User id
* **password** User password

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

Quick login by username (requires a successful previous login, faster login)

**Parameters**:

* **name** Username
* **password** User password (for sdk to automatically update user token when internal token expires)

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

Quick login by user ID (requires a successful previous login, faster login)

**Parameters**:

* **uid** User id
* **password** User password (for sdk to automatically update user token when internal token expires)

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

Log out

**Parameters**:

* **uid** UID of logged out user (default 0 to logout the current user)
* **ignoreUnbindDevice** Whether the unbind device operation is ignored when the user logout. Set to true when server's unbinding device operation is ignored and forced to logout directly when some servers are inaccessible.

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

Get the current connection state with server

**Return**: \[BMXConnectStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

Get the current login state

**Return**: \[BMXSignInStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function reconnect

```java
inline void reconnect()
```

Force reconnection

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

Process network changes in messaging

**Parameters**:

* **type** Changed network type
* **reconnect** Network needs to reconnect or not

**Reimplements**: [im::floo::floolib::BMXNetworkListener::onNetworkChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_network_listener.md#function-onnetworkchanged)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXClient'></div>

```

### function disconnect

```java
inline void disconnect()
```

Disconnect

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

Change the appId of SDK, which also update the appId in BMXConfig.

**Parameters**:

* **appId** Newly changed appId
* **appSecret** Newly changed appSecret

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

Change the appId of SDK, which also update the appId in BMXConfig.

**Parameters**:

* **appId** Newly changed appId

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

Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.

**Parameters**:

* **isLocal** True to use locally cached DNS configuration, false to get the latest configuration from server.

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

When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.

**Parameters**:

* **msg** Message to be sent

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

Create BMXClient

**Parameters**:

* **config** BMXSDKConfig SDK configuration object created by local client-side already

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
