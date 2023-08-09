---
title: floo::BMXClient
summary: Client 

---

# floo::BMXClient



Client 


`#include <bmx_client.h>`

Inherits from [floo::BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| BMXClientPtr | **[create](classfloo_1_1_b_m_x_client.md#function-create)**(BMXSDKConfigPtr config)<br>Create BMXClient  |
| virtual | **[~BMXClient](classfloo_1_1_b_m_x_client.md#function-~bmxclient)**()<br>Destructor  |
| virtual BMXSDKConfigPtr | **[getSDKConfig](classfloo_1_1_b_m_x_client.md#function-getsdkconfig)**() =0<br>Get SDK settings  |
| virtual [BMXUserService](classfloo_1_1_b_m_x_user_service.md) & | **[getUserService](classfloo_1_1_b_m_x_client.md#function-getuserservice)**() =0<br>Get user Service  |
| virtual [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) & | **[getChatService](classfloo_1_1_b_m_x_client.md#function-getchatservice)**() =0<br>Get chat Service  |
| virtual [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) & | **[getGroupService](classfloo_1_1_b_m_x_client.md#function-getgroupservice)**() =0<br>Get group Service  |
| virtual [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) & | **[getRosterService](classfloo_1_1_b_m_x_client.md#function-getrosterservice)**() =0<br>Get roster Service  |
| virtual [BMXPushService](classfloo_1_1_b_m_x_push_service.md) & | **[getPushService](classfloo_1_1_b_m_x_client.md#function-getpushservice)**() =0<br>Get push Service  |
| virtual BMXErrorCode | **[signUpNewUser](classfloo_1_1_b_m_x_client.md#function-signupnewuser)**(const std::string & username, const std::string & password, BMXUserProfilePtr & bmxUserProfilePtr) =0<br>To register a new user, username and password are required  |
| virtual BMXErrorCode | **[signInByName](classfloo_1_1_b_m_x_client.md#function-signinbyname)**(const std::string & name, const std::string & password) =0<br>Login by username  |
| virtual BMXErrorCode | **[signInById](classfloo_1_1_b_m_x_client.md#function-signinbyid)**(int64_t , const std::string & password) =0<br>Login by user ID  |
| virtual BMXErrorCode | **[fastSignInByName](classfloo_1_1_b_m_x_client.md#function-fastsigninbyname)**(const std::string & name, const std::string & password) =0<br>Quick login by username (requires a successful previous login, faster login)  |
| virtual BMXErrorCode | **[fastSignInById](classfloo_1_1_b_m_x_client.md#function-fastsigninbyid)**(int64_t uid, const std::string & password) =0<br>Quick login by user ID (requires a successful previous login, faster login)  |
| virtual BMXErrorCode | **[signOut](classfloo_1_1_b_m_x_client.md#function-signout)**(int64_t uid =0, bool ignoreUnbindDevice =false) =0<br>Log out  |
| virtual BMXConnectStatus | **[connectStatus](classfloo_1_1_b_m_x_client.md#function-connectstatus)**() =0<br>Get the current connection state with server  |
| virtual BMXSignInStatus | **[signInStatus](classfloo_1_1_b_m_x_client.md#function-signinstatus)**() =0<br>Get the current login state  |
| virtual void | **[reconnect](classfloo_1_1_b_m_x_client.md#function-reconnect)**() =0<br>Force reconnection  |
| virtual void | **[onNetworkChanged](classfloo_1_1_b_m_x_client.md#function-onnetworkchanged)**(BMXNetworkType type, bool reconnect) =0<br>Process network changes in messaging  |
| virtual void | **[disconnect](classfloo_1_1_b_m_x_client.md#function-disconnect)**() =0<br>Disconnect  |
| virtual BMXErrorCode | **[changeAppId](classfloo_1_1_b_m_x_client.md#function-changeappid)**(const std::string & appId, const std::string & appSecret ="") =0<br>Change the appId of SDK, which also update the appId in BMXConfig.  |
| virtual BMXErrorCode | **[initializeServerConfig](classfloo_1_1_b_m_x_client.md#function-initializeserverconfig)**(bool isLocal) =0<br>Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.  |
| virtual void | **[sendMessage](classfloo_1_1_b_m_x_client.md#function-sendmessage)**(BMXMessagePtr msg) =0<br>When send a message, the change of message status will be notified by listener. In the case of sending a group message in a specified group with group read acknowledgement enabled, the interface will automatically obtain the group member list id and fill it in the message config, without the need for the client to fill the group member list by itself.  |

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

Create BMXClient 

**Parameters**: 

  * **config** BMXSDKConfig SDK configuration object created by local client-side already 


**Return**: BMXClientPtr 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="create" %}{% endlanying_code_snippet %}
```
### function ~BMXClient

```cpp
inline virtual ~BMXClient()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="~BMXClient" %}{% endlanying_code_snippet %}
```
### function getSDKConfig

```cpp
virtual BMXSDKConfigPtr getSDKConfig() =0
```

Get SDK settings 

**Return**: BMXSDKConfigPtr 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getSDKConfig" %}{% endlanying_code_snippet %}
```
### function getUserService

```cpp
virtual BMXUserService & getUserService() =0
```

Get user Service 

**Return**: [BMXUserService](classfloo_1_1_b_m_x_user_service.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getUserService" %}{% endlanying_code_snippet %}
```
### function getChatService

```cpp
virtual BMXChatService & getChatService() =0
```

Get chat Service 

**Return**: [BMXChatService](classfloo_1_1_b_m_x_chat_service.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getChatService" %}{% endlanying_code_snippet %}
```
### function getGroupService

```cpp
virtual BMXGroupService & getGroupService() =0
```

Get group Service 

**Return**: [BMXGroupService](classfloo_1_1_b_m_x_group_service.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getGroupService" %}{% endlanying_code_snippet %}
```
### function getRosterService

```cpp
virtual BMXRosterService & getRosterService() =0
```

Get roster Service 

**Return**: [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getRosterService" %}{% endlanying_code_snippet %}
```
### function getPushService

```cpp
virtual BMXPushService & getPushService() =0
```

Get push Service 

**Return**: [BMXPushService](classfloo_1_1_b_m_x_push_service.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="getPushService" %}{% endlanying_code_snippet %}
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
  * **bmxUserProfilePtr** After successful registration, get the profile of the newly registered user from this function, and initially passed in a pointing-to-empty shared_ptr object. 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="signUpNewUser" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="signInByName" %}{% endlanying_code_snippet %}
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

  * **int64_t** User id 
  * **password** User password 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="signInById" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="fastSignInByName" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="fastSignInById" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="signOut" %}{% endlanying_code_snippet %}
```
### function connectStatus

```cpp
virtual BMXConnectStatus connectStatus() =0
```

Get the current connection state with server 

**Return**: BMXConnectStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="connectStatus" %}{% endlanying_code_snippet %}
```
### function signInStatus

```cpp
virtual BMXSignInStatus signInStatus() =0
```

Get the current login state 

**Return**: BMXSignInStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="signInStatus" %}{% endlanying_code_snippet %}
```
### function reconnect

```cpp
virtual void reconnect() =0
```

Force reconnection 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="reconnect" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="onNetworkChanged" %}{% endlanying_code_snippet %}
```
### function disconnect

```cpp
virtual void disconnect() =0
```

Disconnect 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="disconnect" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="changeAppId" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="initializeServerConfig" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="sendMessage" %}{% endlanying_code_snippet %}
```
### function BMXClient

```cpp
BMXClient()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXClient",function="BMXClient" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800