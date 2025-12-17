---
title: floo::BMXClient
summary: Client
---

# floo::BMXClient

Client

`#include <bmx_client.h>`

Inherits from [floo::BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md)

## Public Functions

|                                                                     | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BMXClientPtr                                                        | <p><a href="classfloo_1_1_b_m_x_client.md#function-create"><strong>create</strong></a>(BMXSDKConfigPtr config)<br>Create BMXClient</p>                                                                                                                                                                                                                                                                                                                                                          |
| virtual                                                             | <p><a href="classfloo_1_1_b_m_x_client.md#function-~bmxclient"><strong>~BMXClient</strong></a>()<br>Destructor</p>                                                                                                                                                                                                                                                                                                                                                                              |
| virtual BMXSDKConfigPtr                                             | <p><a href="classfloo_1_1_b_m_x_client.md#function-getsdkconfig"><strong>getSDKConfig</strong></a>() =0<br>Get SDK settings</p>                                                                                                                                                                                                                                                                                                                                                                 |
| virtual [BMXUserService](classfloo_1_1_b_m_x_user_service.md) &     | <p><a href="classfloo_1_1_b_m_x_client.md#function-getuserservice"><strong>getUserService</strong></a>() =0<br>Get user Service</p>                                                                                                                                                                                                                                                                                                                                                             |
| virtual [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) &     | <p><a href="classfloo_1_1_b_m_x_client.md#function-getchatservice"><strong>getChatService</strong></a>() =0<br>Get chat Service</p>                                                                                                                                                                                                                                                                                                                                                             |
| virtual [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) &   | <p><a href="classfloo_1_1_b_m_x_client.md#function-getgroupservice"><strong>getGroupService</strong></a>() =0<br>Get group Service</p>                                                                                                                                                                                                                                                                                                                                                          |
| virtual [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) & | <p><a href="classfloo_1_1_b_m_x_client.md#function-getrosterservice"><strong>getRosterService</strong></a>() =0<br>Get roster Service</p>                                                                                                                                                                                                                                                                                                                                                       |
| virtual [BMXPushService](classfloo_1_1_b_m_x_push_service.md) &     | <p><a href="classfloo_1_1_b_m_x_client.md#function-getpushservice"><strong>getPushService</strong></a>() =0<br>Get push Service</p>                                                                                                                                                                                                                                                                                                                                                             |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-signupnewuser"><strong>signUpNewUser</strong></a>(const std::string &#x26; username, const std::string &#x26; password, BMXUserProfilePtr &#x26; bmxUserProfilePtr) =0<br>To register a new user, username and password are required</p>                                                                                                                                                                                                     |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-signinbyname"><strong>signInByName</strong></a>(const std::string &#x26; name, const std::string &#x26; password) =0<br>Login by username</p>                                                                                                                                                                                                                                                                                                |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-signinbyid"><strong>signInById</strong></a>(int64_t , const std::string &#x26; password) =0<br>Login by user ID</p>                                                                                                                                                                                                                                                                                                                          |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-fastsigninbyname"><strong>fastSignInByName</strong></a>(const std::string &#x26; name, const std::string &#x26; password) =0<br>Quick login by username (requires a successful previous login, faster login)</p>                                                                                                                                                                                                                             |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-fastsigninbyid"><strong>fastSignInById</strong></a>(int64_t uid, const std::string &#x26; password) =0<br>Quick login by user ID (requires a successful previous login, faster login)</p>                                                                                                                                                                                                                                                    |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-signout"><strong>signOut</strong></a>(int64_t uid =0, bool ignoreUnbindDevice =false) =0<br>Log out</p>                                                                                                                                                                                                                                                                                                                                      |
| virtual BMXConnectStatus                                            | <p><a href="classfloo_1_1_b_m_x_client.md#function-connectstatus"><strong>connectStatus</strong></a>() =0<br>Get the current connection state with server</p>                                                                                                                                                                                                                                                                                                                                   |
| virtual BMXSignInStatus                                             | <p><a href="classfloo_1_1_b_m_x_client.md#function-signinstatus"><strong>signInStatus</strong></a>() =0<br>Get the current login state</p>                                                                                                                                                                                                                                                                                                                                                      |
| virtual void                                                        | <p><a href="classfloo_1_1_b_m_x_client.md#function-reconnect"><strong>reconnect</strong></a>() =0<br>Force reconnection</p>                                                                                                                                                                                                                                                                                                                                                                     |
| virtual void                                                        | <p><a href="classfloo_1_1_b_m_x_client.md#function-onnetworkchanged"><strong>onNetworkChanged</strong></a>(BMXNetworkType type, bool reconnect) =0<br>Process network changes in messaging</p>                                                                                                                                                                                                                                                                                                  |
| virtual void                                                        | <p><a href="classfloo_1_1_b_m_x_client.md#function-disconnect"><strong>disconnect</strong></a>() =0<br>Disconnect</p>                                                                                                                                                                                                                                                                                                                                                                           |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-changeappid"><strong>changeAppId</strong></a>(const std::string &#x26; appId, const std::string &#x26; appSecret ="") =0<br>Change the appId of SDK, which also update the appId in BMXConfig.</p>                                                                                                                                                                                                                                           |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_client.md#function-initializeserverconfig"><strong>initializeServerConfig</strong></a>(bool isLocal) =0<br>Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.</p>                                                                                                                                                         |
| virtual void                                                        | <p><a href="classfloo_1_1_b_m_x_client.md#function-sendmessage"><strong>sendMessage</strong></a>(BMXMessagePtr msg) =0<br>When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.</p> |

## Protected Functions

|   | Name                                                                |
| - | ------------------------------------------------------------------- |
|   | [**BMXClient**](classfloo_1_1_b_m_x_client.md#function-bmxclient)() |

## Additional inherited members

**Public Functions inherited from** [**floo::BMXNetworkListener**](classfloo_1_1_b_m_x_network_listener.md)

|         | Name                                                                                               |
| ------- | -------------------------------------------------------------------------------------------------- |
| virtual | [**\~BMXNetworkListener**](classfloo_1_1_b_m_x_network_listener.md#function-~bmxnetworklistener)() |

## Public Functions Documentation

### function create

```cpp
static BMXClientPtr create(
    BMXSDKConfigPtr config
)
```

Create BMXClient

**Parameters**:

* **config** BMXSDKConfig SDK configuration object created by local client-side already

**Return**: BMXClientPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function \~BMXClient

```cpp
inline virtual ~BMXClient()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getSDKConfig

```cpp
virtual BMXSDKConfigPtr getSDKConfig() =0
```

Get SDK settings

**Return**: BMXSDKConfigPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getUserService

```cpp
virtual BMXUserService & getUserService() =0
```

Get user Service

**Return**: [BMXUserService](classfloo_1_1_b_m_x_user_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getChatService

```cpp
virtual BMXChatService & getChatService() =0
```

Get chat Service

**Return**: [BMXChatService](classfloo_1_1_b_m_x_chat_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getGroupService

```cpp
virtual BMXGroupService & getGroupService() =0
```

Get group Service

**Return**: [BMXGroupService](classfloo_1_1_b_m_x_group_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getRosterService

```cpp
virtual BMXRosterService & getRosterService() =0
```

Get roster Service

**Return**: [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function getPushService

```cpp
virtual BMXPushService & getPushService() =0
```

Get push Service

**Return**: [BMXPushService](classfloo_1_1_b_m_x_push_service.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function signUpNewUser

```cpp
virtual BMXErrorCode signUpNewUser(
    const std::string & username,
    const std::string & password,
    BMXUserProfilePtr & bmxUserProfilePtr
) =0
```

To register a new user, username and password are required

**Parameters**:

* **username** Username
* **password** User password
* **bmxUserProfilePtr** After successful registration, get the profile of the newly registered user from this function, and initially passed in a pointing-to-empty shared\_ptr object.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function signInByName

```cpp
virtual BMXErrorCode signInByName(
    const std::string & name,
    const std::string & password
) =0
```

Login by username

**Parameters**:

* **name** Username
* **password** User password

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function signInById

```cpp
virtual BMXErrorCode signInById(
    int64_t ,
    const std::string & password
) =0
```

Login by user ID

**Parameters**:

* **int64\_t** User id
* **password** User password

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function fastSignInByName

```cpp
virtual BMXErrorCode fastSignInByName(
    const std::string & name,
    const std::string & password
) =0
```

Quick login by username (requires a successful previous login, faster login)

**Parameters**:

* **name** Username
* **password** User password (for sdk to automatically update user token when internal token expires)

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function fastSignInById

```cpp
virtual BMXErrorCode fastSignInById(
    int64_t uid,
    const std::string & password
) =0
```

Quick login by user ID (requires a successful previous login, faster login)

**Parameters**:

* **uid** User id
* **password** User password (for sdk to automatically update user token when internal token expires)

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function signOut

```cpp
virtual BMXErrorCode signOut(
    int64_t uid =0,
    bool ignoreUnbindDevice =false
) =0
```

Log out

**Parameters**:

* **uid** UID of logged out user (default 0 to logout the current user)
* **ignoreUnbindDevice** Whether the unbind device operation is ignored when the user logout. Set to true when server's unbinding device operation is ignored and forced to logout directly when some servers are inaccessible.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function connectStatus

```cpp
virtual BMXConnectStatus connectStatus() =0
```

Get the current connection state with server

**Return**: BMXConnectStatus

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function signInStatus

```cpp
virtual BMXSignInStatus signInStatus() =0
```

Get the current login state

**Return**: BMXSignInStatus

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function reconnect

```cpp
virtual void reconnect() =0
```

Force reconnection

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function onNetworkChanged

```cpp
virtual void onNetworkChanged(
    BMXNetworkType type,
    bool reconnect
) =0
```

Process network changes in messaging

**Parameters**:

* **type** Changed network type
* **reconnect** Network needs to reconnect or not

**Reimplements**: [floo::BMXNetworkListener::onNetworkChanged](classfloo_1_1_b_m_x_network_listener.md#function-onnetworkchanged)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function disconnect

```cpp
virtual void disconnect() =0
```

Disconnect

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function changeAppId

```cpp
virtual BMXErrorCode changeAppId(
    const std::string & appId,
    const std::string & appSecret =""
) =0
```

Change the appId of SDK, which also update the appId in BMXConfig.

**Parameters**:

* **appId** Newly changed appId

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function initializeServerConfig

```cpp
virtual BMXErrorCode initializeServerConfig(
    bool isLocal
) =0
```

Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.

**Parameters**:

* **isLocal** True to use locally cached DNS configuration, false to get the latest configuration from server.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function sendMessage

```cpp
virtual void sendMessage(
    BMXMessagePtr msg
) =0
```

When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.

**Parameters**:

* **msg** Message to be sent

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>

```

### function BMXClient

```cpp
BMXClient()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXClient'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
