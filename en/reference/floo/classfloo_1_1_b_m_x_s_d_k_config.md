---
title: floo::BMXSDKConfig
summary: SDK settings management
---

# floo::BMXSDKConfig

SDK settings management

`#include <bmx_sdk_config.h>`

## Public Functions

|                        | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                        | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig"><strong>BMXSDKConfig</strong></a>(BMXClientType type, const std::string &#x26; vsn, const std::string &#x26; dataDir, const std::string &#x26; cacheDir, const std::string &#x26; SDKVersion, const std::string &#x26; pushCertName, const std::string &#x26; userAgent, bool deliveryAck =false)<br>Constructor</p>                                                                     |
|                        | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig"><strong>BMXSDKConfig</strong></a>(BMXClientType type, const std::string &#x26; vsn, const std::string &#x26; dataDir, const std::string &#x26; cacheDir, const std::string &#x26; SDKVersion, const std::string &#x26; pushCertName, const std::string &#x26; userAgent, const std::string &#x26; appId, const std::string &#x26; appSecret, bool deliveryAck =false)<br>Constructor</p> |
| virtual                | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-~bmxsdkconfig"><strong>~BMXSDKConfig</strong></a>()<br>Destructor</p>                                                                                                                                                                                                                                                                                                                                  |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdatadir"><strong>getDataDir</strong></a>()<br>Get storage path of chat data, including messages, attachments, and more</p>                                                                                                                                                                                                                                                                          |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getcachedir"><strong>getCacheDir</strong></a>()<br>Get storage path of cached data, including user avatar and more</p>                                                                                                                                                                                                                                                                                 |
| BMXClientType          | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getclienttype"><strong>getClientType</strong></a>()<br>Client type</p>                                                                                                                                                                                                                                                                                                                                 |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getvsn"><strong>getVsn</strong></a>()<br>Client OS version</p>                                                                                                                                                                                                                                                                                                                                         |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getsdkversion"><strong>getSDKVersion</strong></a>()<br>SDK version</p>                                                                                                                                                                                                                                                                                                                                 |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushcertname"><strong>getPushCertName</strong></a>()<br>Get Push certificate name</p>                                                                                                                                                                                                                                                                                                               |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushcertname"><strong>setPushCertName</strong></a>(const std::string &#x26; )<br>Set Push certificate name</p>                                                                                                                                                                                                                                                                                      |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getuseragent"><strong>getUserAgent</strong></a>()<br>Get user proxy information</p>                                                                                                                                                                                                                                                                                                                    |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage"><strong>carryUsernameInMessage</strong></a>()<br>Whether the config sends message carrying</p>                                                                                                                                                                                                                                                                                 |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage"><strong>setCarryUsernameInMessage</strong></a>(bool )<br>Set whether the config sends message carrying username</p>                                                                                                                                                                                                                                                         |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack"><strong>enableDeliveryAck</strong></a>()<br>Whether to send message delivery acknowledgement</p>                                                                                                                                                                                                                                                                                    |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack"><strong>setEnableDeliveryAck</strong></a>(bool )<br>Set whether to send message delivery acknowledgement</p>                                                                                                                                                                                                                                                                     |
| BMXLogLevel            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getloglevel"><strong>getLogLevel</strong></a>()<br>Log output level</p>                                                                                                                                                                                                                                                                                                                                |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setloglevel"><strong>setLogLevel</strong></a>(BMXLogLevel )<br>Set Log output level</p>                                                                                                                                                                                                                                                                                                                |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput"><strong>getConsoleOutput</strong></a>()<br>Whether to output Log to Console.</p>                                                                                                                                                                                                                                                                                                     |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput"><strong>setConsoleOutput</strong></a>(bool )<br>Set whether to output Log to Console</p>                                                                                                                                                                                                                                                                                             |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-sethostconfig"><strong>setHostConfig</strong></a>(const [HostConfig] &#x26; config)<br>Set server configuration</p>                                                                                                                                                                                                                                                                                    |
| const \[HostConfig] &  | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-gethostconfig"><strong>getHostConfig</strong></a>()<br>Get server configuration</p>                                                                                                                                                                                                                                                                                                                    |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations"><strong>getLoadAllServerConversations</strong></a>()<br>Whether to create all conversations based on the unread list returned by server.</p>                                                                                                                                                                                                                            |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations"><strong>setLoadAllServerConversations</strong></a>(bool enable =false)<br>Whether to create all conversations based on the unread list returned by server, default false to create conversations with unread only.</p>                                                                                                                                                  |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid"><strong>getDeviceUuid</strong></a>()<br>Get the unique identifier of device</p>                                                                                                                                                                                                                                                                                                         |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid"><strong>setDeviceUuid</strong></a>(const std::string &#x26; uuid)<br>Set the unique ID of the device, which should always be consistent before the app is uninstalled. Different device IDs can be generated when the app is deleted and installed again.</p>                                                                                                                           |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey"><strong>getDBCryptoKey</strong></a>()<br>Get the local database encryption key for the device.</p>                                                                                                                                                                                                                                                                                     |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey"><strong>setDBCryptoKey</strong></a>(const std::string &#x26; cryptoKey)<br>Set the encryption key of the local database, which should always be kept until the app is uninstalled, and a different key can be generated when the app is deleted and installed again. Used for local database encryption.</p>                                                                           |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getverifycertificate"><strong>getVerifyCertificate</strong></a>()<br>Whether need to verify server-side certificate when get https request.</p>                                                                                                                                                                                                                                                        |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate"><strong>setVerifyCertificate</strong></a>(bool verify =true)<br>Set whether https request verify server-side certificate.</p>                                                                                                                                                                                                                                                    |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getenabledns"><strong>getEnableDNS</strong></a>()<br>Whether to enable dns function for get.</p>                                                                                                                                                                                                                                                                                                       |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledns"><strong>setEnableDNS</strong></a>(bool enable =true)<br>Set whether to enable dns function for get, default enabled.</p>                                                                                                                                                                                                                                                                 |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getuserdnsaddress"><strong>getUserDNSAddress</strong></a>()<br>Get user-defined dns server address.</p>                                                                                                                                                                                                                                                                                                |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setuserdnsaddress"><strong>setUserDNSAddress</strong></a>(const std::string &#x26; dns)<br>Set user-defined dns server address, preferring user dns if dns server has been set.</p>                                                                                                                                                                                                                    |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getappid"><strong>getAppID</strong></a>()<br>Get user's appID.</p>                                                                                                                                                                                                                                                                                                                                     |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setappid"><strong>setAppID</strong></a>(const std::string &#x26; appID)<br>Set user's appID.</p>                                                                                                                                                                                                                                                                                                       |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getappsecret"><strong>getAppSecret</strong></a>()<br>Get user's appSecret.</p>                                                                                                                                                                                                                                                                                                                         |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setappsecret"><strong>setAppSecret</strong></a>(const std::string &#x26; appSecret)<br>Set user's appSecret.</p>                                                                                                                                                                                                                                                                                       |
| BMXPushProviderType    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushprovidertype"><strong>getPushProviderType</strong></a>()<br>Get user's Push provider type.</p>                                                                                                                                                                                                                                                                                                  |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushprovidertype"><strong>setPushProviderType</strong></a>(BMXPushProviderType type)<br>Set user's Push provider type.</p>                                                                                                                                                                                                                                                                          |
| BMXPushEnvironmentType | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushenvironmenttype"><strong>getPushEnvironmentType</strong></a>()<br>Get user's Push environment type.</p>                                                                                                                                                                                                                                                                                         |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenvironmenttype"><strong>setEnvironmentType</strong></a>(BMXPushEnvironmentType type)<br>Set user's Push environment type.</p>                                                                                                                                                                                                                                                                      |
| int64\_t               | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdebuglogreceiverid"><strong>getDebugLogReceiverId</strong></a>()<br>Get debug log receiving account (for SDK debugging only, used for receiving client log)</p>                                                                                                                                                                                                                                     |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdebuglogreceiverid"><strong>setDebugLogReceiverId</strong></a>(int64_t uid)<br>Set debug log receiving account (for SDK debugging only, used for receiving client log)</p>                                                                                                                                                                                                                          |

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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function \~BMXSDKConfig

```cpp
virtual ~BMXSDKConfig()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getDataDir

```cpp
const std::string & getDataDir()
```

Get storage path of chat data, including messages, attachments, and more

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getCacheDir

```cpp
const std::string & getCacheDir()
```

Get storage path of cached data, including user avatar and more

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getClientType

```cpp
BMXClientType getClientType()
```

Client type

**Return**: BMXClientType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getVsn

```cpp
const std::string & getVsn()
```

Client OS version

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getSDKVersion

```cpp
const std::string & getSDKVersion()
```

SDK version

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getPushCertName

```cpp
const std::string & getPushCertName()
```

Get Push certificate name

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getUserAgent

```cpp
const std::string & getUserAgent()
```

Get user proxy information

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function carryUsernameInMessage

```cpp
bool carryUsernameInMessage()
```

Whether the config sends message carrying

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function enableDeliveryAck

```cpp
bool enableDeliveryAck()
```

Whether to send message delivery acknowledgement

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getLogLevel

```cpp
BMXLogLevel getLogLevel()
```

Log output level

**Return**: BMXLogLevel

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getConsoleOutput

```cpp
bool getConsoleOutput()
```

Whether to output Log to Console.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getHostConfig

```cpp
const HostConfig & getHostConfig()
```

Get server configuration

**Return**: \[HostConfig]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getLoadAllServerConversations

```cpp
bool getLoadAllServerConversations()
```

Whether to create all conversations based on the unread list returned by server.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getDeviceUuid

```cpp
const std::string & getDeviceUuid()
```

Get the unique identifier of device

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getDBCryptoKey

```cpp
const std::string & getDBCryptoKey()
```

Get the local database encryption key for the device.

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getVerifyCertificate

```cpp
bool getVerifyCertificate()
```

Whether need to verify server-side certificate when get https request.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getEnableDNS

```cpp
bool getEnableDNS()
```

Whether to enable dns function for get.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getUserDNSAddress

```cpp
std::string getUserDNSAddress()
```

Get user-defined dns server address.

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getAppID

```cpp
std::string getAppID()
```

Get user's appID.

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getAppSecret

```cpp
std::string getAppSecret()
```

Get user's appSecret.

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getPushProviderType

```cpp
BMXPushProviderType getPushProviderType()
```

Get user's Push provider type.

**Return**: BMXPushProviderType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getPushEnvironmentType

```cpp
BMXPushEnvironmentType getPushEnvironmentType()
```

Get user's Push environment type.

**Return**: BMXPushEnvironmentType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

### function getDebugLogReceiverId

```cpp
int64_t getDebugLogReceiverId()
```

Get debug log receiving account (for SDK debugging only, used for receiving client log)

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
