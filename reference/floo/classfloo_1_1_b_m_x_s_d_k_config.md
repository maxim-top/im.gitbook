---
title: floo::BMXSDKConfig
summary: SDK settings management 

---

# floo::BMXSDKConfig



SDK settings management 


`#include <bmx_sdk_config.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**(BMXClientType type, const std::string & vsn, const std::string & dataDir, const std::string & cacheDir, const std::string & SDKVersion, const std::string & pushCertName, const std::string & userAgent, bool deliveryAck =false)<br>Constructor  |
| | **[BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**(BMXClientType type, const std::string & vsn, const std::string & dataDir, const std::string & cacheDir, const std::string & SDKVersion, const std::string & pushCertName, const std::string & userAgent, const std::string & appId, const std::string & appSecret, bool deliveryAck =false)<br>Constructor  |
| virtual | **[~BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-~bmxsdkconfig)**()<br>Destructor  |
| const std::string & | **[getDataDir](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdatadir)**()<br>Get storage path of chat data, including messages, attachments, and more  |
| const std::string & | **[getCacheDir](classfloo_1_1_b_m_x_s_d_k_config.md#function-getcachedir)**()<br>Get storage path of cached data, including user avatar and more  |
| BMXClientType | **[getClientType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getclienttype)**()<br>Client type  |
| const std::string & | **[getVsn](classfloo_1_1_b_m_x_s_d_k_config.md#function-getvsn)**()<br>Client OS version  |
| const std::string & | **[getSDKVersion](classfloo_1_1_b_m_x_s_d_k_config.md#function-getsdkversion)**()<br>SDK version  |
| const std::string & | **[getPushCertName](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushcertname)**()<br>Get Push certificate name  |
| void | **[setPushCertName](classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushcertname)**(const std::string & )<br>Set Push certificate name  |
| const std::string & | **[getUserAgent](classfloo_1_1_b_m_x_s_d_k_config.md#function-getuseragent)**()<br>Get user proxy information  |
| bool | **[carryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage)**()<br>**to-be-translate**  |
| void | **[setCarryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage)**(bool )<br>**to-be-translate**  |
| bool | **[enableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack)**()<br>Whether to send message delivery receipt  |
| void | **[setEnableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack)**(bool )<br>Set whether to send message delivery receipt  |
| BMXLogLevel | **[getLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloglevel)**()<br>Log output level  |
| void | **[setLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloglevel)**(BMXLogLevel )<br>Set Log output level  |
| bool | **[getConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput)**()<br>Whether to output Log to Console.  |
| void | **[setConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput)**(bool )<br>Set whether to output Log to Console  |
| void | **[setHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-sethostconfig)**(const [HostConfig] & config)<br>Set server configuration  |
| const [HostConfig] & | **[getHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-gethostconfig)**()<br>Get server configuration  |
| bool | **[getLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations)**()<br>Whether to create all sessions based on the unread list returned by server.  |
| void | **[setLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations)**(bool enable =false)<br>Whether to create all sessions based on the unread list returned by server, default false to create sessions with unread only.  |
| const std::string & | **[getDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid)**()<br>Get the unique identifier of device  |
| void | **[setDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid)**(const std::string & uuid)<br>**to-be-translate**  |
| const std::string & | **[getDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey)**()<br>**to-be-translate**  |
| void | **[setDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey)**(const std::string & cryptoKey)<br>**to-be-translate**  |
| bool | **[getVerifyCertificate](classfloo_1_1_b_m_x_s_d_k_config.md#function-getverifycertificate)**()<br>Whether need to verify server-side certificate when get https request.  |
| void | **[setVerifyCertificate](classfloo_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate)**(bool verify =true)<br>Set whether https request verify server-side certificate.  |
| bool | **[getEnableDNS](classfloo_1_1_b_m_x_s_d_k_config.md#function-getenabledns)**()<br>Whether to enable dns function for get.  |
| void | **[setEnableDNS](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledns)**(bool enable =true)<br>Set whether to enable dns function for get, default enabled.  |
| std::string | **[getUserDNSAddress](classfloo_1_1_b_m_x_s_d_k_config.md#function-getuserdnsaddress)**()<br>Get user-defined dns server address.  |
| void | **[setUserDNSAddress](classfloo_1_1_b_m_x_s_d_k_config.md#function-setuserdnsaddress)**(const std::string & dns)<br>Set user-defined dns server address, preferring user dns if dns server has been set.  |
| std::string | **[getAppID](classfloo_1_1_b_m_x_s_d_k_config.md#function-getappid)**()<br>Get user's appID.  |
| void | **[setAppID](classfloo_1_1_b_m_x_s_d_k_config.md#function-setappid)**(const std::string & appID)<br>Set user's appID.  |
| std::string | **[getAppSecret](classfloo_1_1_b_m_x_s_d_k_config.md#function-getappsecret)**()<br>Get user's appSecret.  |
| void | **[setAppSecret](classfloo_1_1_b_m_x_s_d_k_config.md#function-setappsecret)**(const std::string & appSecret)<br>Set user's appSecret.  |
| BMXPushProviderType | **[getPushProviderType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushprovidertype)**()<br>Get user's Push provider type.  |
| void | **[setPushProviderType](classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushprovidertype)**(BMXPushProviderType type)<br>Set user's Push provider type.  |
| BMXPushEnvironmentType | **[getPushEnvironmentType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushenvironmenttype)**()<br>Get user's Push environment type.  |
| void | **[setEnvironmentType](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenvironmenttype)**(BMXPushEnvironmentType type)<br>Set user's Push environment type.  |
| int64_t | **[getDebugLogReceiverId](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdebuglogreceiverid)**()<br>Get debug log receiving account (for SDK debugging only, used for receiving client log)  |
| void | **[setDebugLogReceiverId](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdebuglogreceiverid)**(int64_t uid)<br>Set debug log receiving account (for SDK debugging only, used for receiving client log)  |

## Public Functions Documentation

### function BMXSDKConfig

```cpp
BMXSDKConfig(
    BMXClientType type,
    const std::string & vsn,
    const std::string & dataDir,
    const std::string & cacheDir,
    const std::string & SDKVersion,
    const std::string & pushCertName,
    const std::string & userAgent,
    bool deliveryAck =false
)
```

Constructor 

**Parameters**: 

  * **type** Client type 
  * **vsn** Client OS version 
  * **dataDir** Storage path of chat data 
  * **cacheDir** Storage path of cached data 
  * **SDKVersion** SDK version 
  * **pushCertName** Push certificate name 
  * **userAgent** User agent information 
  * **deliveryAck** Whether to send message delivery receipt 


### function BMXSDKConfig

```cpp
BMXSDKConfig(
    BMXClientType type,
    const std::string & vsn,
    const std::string & dataDir,
    const std::string & cacheDir,
    const std::string & SDKVersion,
    const std::string & pushCertName,
    const std::string & userAgent,
    const std::string & appId,
    const std::string & appSecret,
    bool deliveryAck =false
)
```

Constructor 

**Parameters**: 

  * **type** Client type 
  * **vsn** Client OS version 
  * **dataDir** Storage path of chat data 
  * **cacheDir** Storage path of cached data 
  * **SDKVersion** SDK version 
  * **pushCertName** Push certificate name 
  * **userAgent** User agent information 
  * **appId** User's appId 
  * **appSecret** User's appSecret (for users using push, both appId and appSecret must be set) 
  * **deliveryAck** Whether to send message delivery receipt 


### function ~BMXSDKConfig

```cpp
virtual ~BMXSDKConfig()
```

Destructor 

### function getDataDir

```cpp
const std::string & getDataDir()
```

Get storage path of chat data, including messages, attachments, and more 

**Return**: std::string 

### function getCacheDir

```cpp
const std::string & getCacheDir()
```

Get storage path of cached data, including user avatar and more 

**Return**: std::string 

### function getClientType

```cpp
BMXClientType getClientType()
```

Client type 

**Return**: BMXClientType 

### function getVsn

```cpp
const std::string & getVsn()
```

Client OS version 

**Return**: std::string 

### function getSDKVersion

```cpp
const std::string & getSDKVersion()
```

SDK version 

**Return**: std::string 

### function getPushCertName

```cpp
const std::string & getPushCertName()
```

Get Push certificate name 

**Return**: std::string 

### function setPushCertName

```cpp
void setPushCertName(
    const std::string & 
)
```

Set Push certificate name 

**Return**: std::string 

### function getUserAgent

```cpp
const std::string & getUserAgent()
```

Get user proxy information 

**Return**: std::string 

### function carryUsernameInMessage

```cpp
bool carryUsernameInMessage()
```

**to-be-translate** 

**Return**: bool 

### function setCarryUsernameInMessage

```cpp
void setCarryUsernameInMessage(
    bool 
)
```

**to-be-translate** 

**Parameters**: 

  * **bool** **to-be-translate** 


### function enableDeliveryAck

```cpp
bool enableDeliveryAck()
```

Whether to send message delivery receipt 

**Return**: bool 

### function setEnableDeliveryAck

```cpp
void setEnableDeliveryAck(
    bool 
)
```

Set whether to send message delivery receipt 

**Parameters**: 

  * **bool** Whether to send message delivery receipt 


### function getLogLevel

```cpp
BMXLogLevel getLogLevel()
```

Log output level 

**Return**: BMXLogLevel 

### function setLogLevel

```cpp
void setLogLevel(
    BMXLogLevel 
)
```

Set Log output level 

**Parameters**: 

  * **BMXLogLevel** Log output level 


### function getConsoleOutput

```cpp
bool getConsoleOutput()
```

Whether to output Log to Console. 

**Return**: bool 

### function setConsoleOutput

```cpp
void setConsoleOutput(
    bool 
)
```

Set whether to output Log to Console 

**Parameters**: 

  * **bool** Set whether to output Log to Console 


### function setHostConfig

```cpp
void setHostConfig(
    const HostConfig & config
)
```

Set server configuration 

**Parameters**: 

  * **config** Server configuration 


### function getHostConfig

```cpp
const HostConfig & getHostConfig()
```

Get server configuration 

**Return**: [HostConfig]

### function getLoadAllServerConversations

```cpp
bool getLoadAllServerConversations()
```

Whether to create all sessions based on the unread list returned by server. 

**Return**: bool 

### function setLoadAllServerConversations

```cpp
void setLoadAllServerConversations(
    bool enable =false
)
```

Whether to create all sessions based on the unread list returned by server, default false to create sessions with unread only. 

**Parameters**: 

  * **enable** Whether to create all sessions based on the unread list returned by server 


### function getDeviceUuid

```cpp
const std::string & getDeviceUuid()
```

Get the unique identifier of device 

**Return**: std::string 

### function setDeviceUuid

```cpp
void setDeviceUuid(
    const std::string & uuid
)
```

**to-be-translate** 

**Parameters**: 

  * **uuid** Unique identifier of device. 


### function getDBCryptoKey

```cpp
const std::string & getDBCryptoKey()
```

**to-be-translate** 

**Return**: std::string 

### function setDBCryptoKey

```cpp
void setDBCryptoKey(
    const std::string & cryptoKey
)
```

**to-be-translate** 

**Parameters**: 

  * **cryptoKey** **to-be-translate**. 


### function getVerifyCertificate

```cpp
bool getVerifyCertificate()
```

Whether need to verify server-side certificate when get https request. 

**Return**: bool 

### function setVerifyCertificate

```cpp
void setVerifyCertificate(
    bool verify =true
)
```

Set whether https request verify server-side certificate. 

**Parameters**: 

  * **verify** Whether https request verify server-side certificate 


### function getEnableDNS

```cpp
bool getEnableDNS()
```

Whether to enable dns function for get. 

**Return**: bool 

### function setEnableDNS

```cpp
void setEnableDNS(
    bool enable =true
)
```

Set whether to enable dns function for get, default enabled. 

**Parameters**: 

  * **enable** Whether to enable dns function 


### function getUserDNSAddress

```cpp
std::string getUserDNSAddress()
```

Get user-defined dns server address. 

**Return**: std::string 

### function setUserDNSAddress

```cpp
void setUserDNSAddress(
    const std::string & dns
)
```

Set user-defined dns server address, preferring user dns if dns server has been set. 

**Parameters**: 

  * **dns** User-defined dns server address 


### function getAppID

```cpp
std::string getAppID()
```

Get user's appID. 

**Return**: std::string 

### function setAppID

```cpp
void setAppID(
    const std::string & appID
)
```

Set user's appID. 

**Parameters**: 

  * **appID** User's appID 


### function getAppSecret

```cpp
std::string getAppSecret()
```

Get user's appSecret. 

**Return**: std::string 

### function setAppSecret

```cpp
void setAppSecret(
    const std::string & appSecret
)
```

Set user's appSecret. 

**Parameters**: 

  * **appID** User's appSecret 


### function getPushProviderType

```cpp
BMXPushProviderType getPushProviderType()
```

Get user's Push provider type. 

**Return**: BMXPushProviderType 

### function setPushProviderType

```cpp
void setPushProviderType(
    BMXPushProviderType type
)
```

Set user's Push provider type. 

**Parameters**: 

  * **type** User's push provider type 


### function getPushEnvironmentType

```cpp
BMXPushEnvironmentType getPushEnvironmentType()
```

Get user's Push environment type. 

**Return**: BMXPushEnvironmentType 

### function setEnvironmentType

```cpp
void setEnvironmentType(
    BMXPushEnvironmentType type
)
```

Set user's Push environment type. 

**Parameters**: 

  * **type** User's push environment type 


### function getDebugLogReceiverId

```cpp
int64_t getDebugLogReceiverId()
```

Get debug log receiving account (for SDK debugging only, used for receiving client log) 

**Return**: int64_t 

### function setDebugLogReceiverId

```cpp
void setDebugLogReceiverId(
    int64_t uid
)
```

Set debug log receiving account (for SDK debugging only, used for receiving client log) 

**Parameters**: 

  * **uid** Debug log receiver id 


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800