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
| bool | **[carryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage)**()<br>Whether the config sends message carrying  |
| void | **[setCarryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage)**(bool )<br>Set whether the config sends message carrying username  |
| bool | **[enableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack)**()<br>Whether to send message delivery acknowledgement  |
| void | **[setEnableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack)**(bool )<br>Set whether to send message delivery acknowledgement  |
| BMXLogLevel | **[getLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloglevel)**()<br>Log output level  |
| void | **[setLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloglevel)**(BMXLogLevel )<br>Set Log output level  |
| bool | **[getConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput)**()<br>Whether to output Log to Console.  |
| void | **[setConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput)**(bool )<br>Set whether to output Log to Console  |
| void | **[setHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-sethostconfig)**(const [HostConfig] & config)<br>Set server configuration  |
| const [HostConfig] & | **[getHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-gethostconfig)**()<br>Get server configuration  |
| bool | **[getLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations)**()<br>Whether to create all conversations based on the unread list returned by server.  |
| void | **[setLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations)**(bool enable =false)<br>Whether to create all conversations based on the unread list returned by server, default false to create conversations with unread only.  |
| const std::string & | **[getDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid)**()<br>Get the unique identifier of device  |
| void | **[setDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid)**(const std::string & uuid)<br>Set the unique ID of the device, which should always be consistent before the app is uninstalled. Different device IDs can be generated when the app is deleted and installed again.  |
| const std::string & | **[getDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey)**()<br>Get the local database encryption key for the device.  |
| void | **[setDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey)**(const std::string & cryptoKey)<br>Set the encryption key of the local database, which should always be kept until the app is uninstalled, and a different key can be generated when the app is deleted and installed again. Used for local database encryption.  |
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
  * **deliveryAck** Whether to send message delivery acknowledgement 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
```
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
  * **deliveryAck** Whether to send message delivery acknowledgement 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
```
### function ~BMXSDKConfig

```cpp
virtual ~BMXSDKConfig()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="~BMXSDKConfig" %}{% endlanying_code_snippet %}
```
### function getDataDir

```cpp
const std::string & getDataDir()
```

Get storage path of chat data, including messages, attachments, and more 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getDataDir" %}{% endlanying_code_snippet %}
```
### function getCacheDir

```cpp
const std::string & getCacheDir()
```

Get storage path of cached data, including user avatar and more 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getCacheDir" %}{% endlanying_code_snippet %}
```
### function getClientType

```cpp
BMXClientType getClientType()
```

Client type 

**Return**: BMXClientType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getClientType" %}{% endlanying_code_snippet %}
```
### function getVsn

```cpp
const std::string & getVsn()
```

Client OS version 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getVsn" %}{% endlanying_code_snippet %}
```
### function getSDKVersion

```cpp
const std::string & getSDKVersion()
```

SDK version 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getSDKVersion" %}{% endlanying_code_snippet %}
```
### function getPushCertName

```cpp
const std::string & getPushCertName()
```

Get Push certificate name 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getPushCertName" %}{% endlanying_code_snippet %}
```
### function setPushCertName

```cpp
void setPushCertName(
    const std::string & 
)
```

Set Push certificate name 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setPushCertName" %}{% endlanying_code_snippet %}
```
### function getUserAgent

```cpp
const std::string & getUserAgent()
```

Get user proxy information 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getUserAgent" %}{% endlanying_code_snippet %}
```
### function carryUsernameInMessage

```cpp
bool carryUsernameInMessage()
```

Whether the config sends message carrying 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="carryUsernameInMessage" %}{% endlanying_code_snippet %}
```
### function setCarryUsernameInMessage

```cpp
void setCarryUsernameInMessage(
    bool 
)
```

Set whether the config sends message carrying username 

**Parameters**: 

  * **bool** Set whether the config sends message carrying username 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setCarryUsernameInMessage" %}{% endlanying_code_snippet %}
```
### function enableDeliveryAck

```cpp
bool enableDeliveryAck()
```

Whether to send message delivery acknowledgement 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="enableDeliveryAck" %}{% endlanying_code_snippet %}
```
### function setEnableDeliveryAck

```cpp
void setEnableDeliveryAck(
    bool 
)
```

Set whether to send message delivery acknowledgement 

**Parameters**: 

  * **bool** Whether to send message delivery acknowledgement 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setEnableDeliveryAck" %}{% endlanying_code_snippet %}
```
### function getLogLevel

```cpp
BMXLogLevel getLogLevel()
```

Log output level 

**Return**: BMXLogLevel 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getLogLevel" %}{% endlanying_code_snippet %}
```
### function setLogLevel

```cpp
void setLogLevel(
    BMXLogLevel 
)
```

Set Log output level 

**Parameters**: 

  * **BMXLogLevel** Log output level 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setLogLevel" %}{% endlanying_code_snippet %}
```
### function getConsoleOutput

```cpp
bool getConsoleOutput()
```

Whether to output Log to Console. 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getConsoleOutput" %}{% endlanying_code_snippet %}
```
### function setConsoleOutput

```cpp
void setConsoleOutput(
    bool 
)
```

Set whether to output Log to Console 

**Parameters**: 

  * **bool** Set whether to output Log to Console 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setConsoleOutput" %}{% endlanying_code_snippet %}
```
### function setHostConfig

```cpp
void setHostConfig(
    const HostConfig & config
)
```

Set server configuration 

**Parameters**: 

  * **config** Server configuration 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setHostConfig" %}{% endlanying_code_snippet %}
```
### function getHostConfig

```cpp
const HostConfig & getHostConfig()
```

Get server configuration 

**Return**: [HostConfig]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getHostConfig" %}{% endlanying_code_snippet %}
```
### function getLoadAllServerConversations

```cpp
bool getLoadAllServerConversations()
```

Whether to create all conversations based on the unread list returned by server. 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### function setLoadAllServerConversations

```cpp
void setLoadAllServerConversations(
    bool enable =false
)
```

Whether to create all conversations based on the unread list returned by server, default false to create conversations with unread only. 

**Parameters**: 

  * **enable** Whether to create all conversations based on the unread list returned by server 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### function getDeviceUuid

```cpp
const std::string & getDeviceUuid()
```

Get the unique identifier of device 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getDeviceUuid" %}{% endlanying_code_snippet %}
```
### function setDeviceUuid

```cpp
void setDeviceUuid(
    const std::string & uuid
)
```

Set the unique ID of the device, which should always be consistent before the app is uninstalled. Different device IDs can be generated when the app is deleted and installed again. 

**Parameters**: 

  * **uuid** Unique identifier of device. 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setDeviceUuid" %}{% endlanying_code_snippet %}
```
### function getDBCryptoKey

```cpp
const std::string & getDBCryptoKey()
```

Get the local database encryption key for the device. 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getDBCryptoKey" %}{% endlanying_code_snippet %}
```
### function setDBCryptoKey

```cpp
void setDBCryptoKey(
    const std::string & cryptoKey
)
```

Set the encryption key of the local database, which should always be kept until the app is uninstalled, and a different key can be generated when the app is deleted and installed again. Used for local database encryption. 

**Parameters**: 

  * **cryptoKey** Local database encryption key. 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setDBCryptoKey" %}{% endlanying_code_snippet %}
```
### function getVerifyCertificate

```cpp
bool getVerifyCertificate()
```

Whether need to verify server-side certificate when get https request. 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getVerifyCertificate" %}{% endlanying_code_snippet %}
```
### function setVerifyCertificate

```cpp
void setVerifyCertificate(
    bool verify =true
)
```

Set whether https request verify server-side certificate. 

**Parameters**: 

  * **verify** Whether https request verify server-side certificate 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setVerifyCertificate" %}{% endlanying_code_snippet %}
```
### function getEnableDNS

```cpp
bool getEnableDNS()
```

Whether to enable dns function for get. 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getEnableDNS" %}{% endlanying_code_snippet %}
```
### function setEnableDNS

```cpp
void setEnableDNS(
    bool enable =true
)
```

Set whether to enable dns function for get, default enabled. 

**Parameters**: 

  * **enable** Whether to enable dns function 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setEnableDNS" %}{% endlanying_code_snippet %}
```
### function getUserDNSAddress

```cpp
std::string getUserDNSAddress()
```

Get user-defined dns server address. 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getUserDNSAddress" %}{% endlanying_code_snippet %}
```
### function setUserDNSAddress

```cpp
void setUserDNSAddress(
    const std::string & dns
)
```

Set user-defined dns server address, preferring user dns if dns server has been set. 

**Parameters**: 

  * **dns** User-defined dns server address 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setUserDNSAddress" %}{% endlanying_code_snippet %}
```
### function getAppID

```cpp
std::string getAppID()
```

Get user's appID. 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getAppID" %}{% endlanying_code_snippet %}
```
### function setAppID

```cpp
void setAppID(
    const std::string & appID
)
```

Set user's appID. 

**Parameters**: 

  * **appID** User's appID 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setAppID" %}{% endlanying_code_snippet %}
```
### function getAppSecret

```cpp
std::string getAppSecret()
```

Get user's appSecret. 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getAppSecret" %}{% endlanying_code_snippet %}
```
### function setAppSecret

```cpp
void setAppSecret(
    const std::string & appSecret
)
```

Set user's appSecret. 

**Parameters**: 

  * **appID** User's appSecret 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setAppSecret" %}{% endlanying_code_snippet %}
```
### function getPushProviderType

```cpp
BMXPushProviderType getPushProviderType()
```

Get user's Push provider type. 

**Return**: BMXPushProviderType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getPushProviderType" %}{% endlanying_code_snippet %}
```
### function setPushProviderType

```cpp
void setPushProviderType(
    BMXPushProviderType type
)
```

Set user's Push provider type. 

**Parameters**: 

  * **type** User's push provider type 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setPushProviderType" %}{% endlanying_code_snippet %}
```
### function getPushEnvironmentType

```cpp
BMXPushEnvironmentType getPushEnvironmentType()
```

Get user's Push environment type. 

**Return**: BMXPushEnvironmentType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getPushEnvironmentType" %}{% endlanying_code_snippet %}
```
### function setEnvironmentType

```cpp
void setEnvironmentType(
    BMXPushEnvironmentType type
)
```

Set user's Push environment type. 

**Parameters**: 

  * **type** User's push environment type 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setEnvironmentType" %}{% endlanying_code_snippet %}
```
### function getDebugLogReceiverId

```cpp
int64_t getDebugLogReceiverId()
```

Get debug log receiving account (for SDK debugging only, used for receiving client log) 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="getDebugLogReceiverId" %}{% endlanying_code_snippet %}
```
### function setDebugLogReceiverId

```cpp
void setDebugLogReceiverId(
    int64_t uid
)
```

Set debug log receiving account (for SDK debugging only, used for receiving client log) 

**Parameters**: 

  * **uid** Debug log receiver id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXSDKConfig",function="setDebugLogReceiverId" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800