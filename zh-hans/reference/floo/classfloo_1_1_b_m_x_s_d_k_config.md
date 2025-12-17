---
title: floo::BMXSDKConfig
summary: SDK设置管理
---

# floo::BMXSDKConfig

SDK设置管理

`#include <bmx_sdk_config.h>`

## Public Functions

|                        | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                        | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig"><strong>BMXSDKConfig</strong></a>(BMXClientType type, const std::string &#x26; vsn, const std::string &#x26; dataDir, const std::string &#x26; cacheDir, const std::string &#x26; SDKVersion, const std::string &#x26; pushCertName, const std::string &#x26; userAgent, bool deliveryAck =false)<br>构造函数</p>                                                                     |
|                        | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig"><strong>BMXSDKConfig</strong></a>(BMXClientType type, const std::string &#x26; vsn, const std::string &#x26; dataDir, const std::string &#x26; cacheDir, const std::string &#x26; SDKVersion, const std::string &#x26; pushCertName, const std::string &#x26; userAgent, const std::string &#x26; appId, const std::string &#x26; appSecret, bool deliveryAck =false)<br>构造函数</p> |
| virtual                | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-~bmxsdkconfig"><strong>~BMXSDKConfig</strong></a>()<br>析构函数</p>                                                                                                                                                                                                                                                                                                                                 |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdatadir"><strong>getDataDir</strong></a>()<br>获取聊天数据存储路径，包含消息、附件等</p>                                                                                                                                                                                                                                                                                                                        |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getcachedir"><strong>getCacheDir</strong></a>()<br>获取缓存数据存储路径，比如用户头像</p>                                                                                                                                                                                                                                                                                                                        |
| BMXClientType          | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getclienttype"><strong>getClientType</strong></a>()<br>客户端类型</p>                                                                                                                                                                                                                                                                                                                                |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getvsn"><strong>getVsn</strong></a>()<br>客户端OS版本</p>                                                                                                                                                                                                                                                                                                                                            |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getsdkversion"><strong>getSDKVersion</strong></a>()<br>SDK版本</p>                                                                                                                                                                                                                                                                                                                                |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushcertname"><strong>getPushCertName</strong></a>()<br>获取Push证书名字</p>                                                                                                                                                                                                                                                                                                                       |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushcertname"><strong>setPushCertName</strong></a>(const std::string &#x26; )<br>设置Push证书名字</p>                                                                                                                                                                                                                                                                                              |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getuseragent"><strong>getUserAgent</strong></a>()<br>获取用户代理信息</p>                                                                                                                                                                                                                                                                                                                               |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage"><strong>carryUsernameInMessage</strong></a>()<br>发送消息的config中是否携带</p>                                                                                                                                                                                                                                                                                                   |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage"><strong>setCarryUsernameInMessage</strong></a>(bool )<br>设置发送消息的config中是否携带用户名</p>                                                                                                                                                                                                                                                                                   |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack"><strong>enableDeliveryAck</strong></a>()<br>是否发送消息送达回执</p>                                                                                                                                                                                                                                                                                                                   |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack"><strong>setEnableDeliveryAck</strong></a>(bool )<br>设置是否发送消息送达回执</p>                                                                                                                                                                                                                                                                                                      |
| BMXLogLevel            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getloglevel"><strong>getLogLevel</strong></a>()<br>Log输出等级</p>                                                                                                                                                                                                                                                                                                                                  |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setloglevel"><strong>setLogLevel</strong></a>(BMXLogLevel )<br>设置Log输出等级</p>                                                                                                                                                                                                                                                                                                                    |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput"><strong>getConsoleOutput</strong></a>()<br>Log是否输出到Console.</p>                                                                                                                                                                                                                                                                                                               |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput"><strong>setConsoleOutput</strong></a>(bool )<br>设置Log是否输出到Console</p>                                                                                                                                                                                                                                                                                                         |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-sethostconfig"><strong>setHostConfig</strong></a>(const [HostConfig] &#x26; config)<br>设置服务器配置</p>                                                                                                                                                                                                                                                                                              |
| const \[HostConfig] &  | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-gethostconfig"><strong>getHostConfig</strong></a>()<br>获取服务器配置</p>                                                                                                                                                                                                                                                                                                                              |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations"><strong>getLoadAllServerConversations</strong></a>()<br>是否根据服务器返回未读列表创建所有会话.</p>                                                                                                                                                                                                                                                                                 |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations"><strong>setLoadAllServerConversations</strong></a>(bool enable =false)<br>是否根据服务器返回未读列表创建所有会话，默认为false，只会创建有未读消息的会话。</p>                                                                                                                                                                                                                                         |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid"><strong>getDeviceUuid</strong></a>()<br>获取设备的唯一识别码</p>                                                                                                                                                                                                                                                                                                                           |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid"><strong>setDeviceUuid</strong></a>(const std::string &#x26; uuid)<br>设置设备的唯一识别码，在app卸载之前应该始终保持一致，app删除后再次安装时可以产生不同的设备识别码。</p>                                                                                                                                                                                                                                                    |
| const std::string &    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey"><strong>getDBCryptoKey</strong></a>()<br>获取设备的本地数据库加密密钥。</p>                                                                                                                                                                                                                                                                                                                    |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey"><strong>setDBCryptoKey</strong></a>(const std::string &#x26; cryptoKey)<br>设置本地数据库的加密密钥，在app卸载之前应该始终保持一直，app删除后再次安装时可以产生不同的密钥。用于本地数据库加密。</p>                                                                                                                                                                                                                                    |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getverifycertificate"><strong>getVerifyCertificate</strong></a>()<br>获取https请求是否验证服务器端证书。</p>                                                                                                                                                                                                                                                                                                   |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate"><strong>setVerifyCertificate</strong></a>(bool verify =true)<br>设置https请求是否验证服务器端证书。</p>                                                                                                                                                                                                                                                                                  |
| bool                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getenabledns"><strong>getEnableDNS</strong></a>()<br>获取是否启用dns功能。</p>                                                                                                                                                                                                                                                                                                                           |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledns"><strong>setEnableDNS</strong></a>(bool enable =true)<br>设置是否启用dns功能，默认是开启的。</p>                                                                                                                                                                                                                                                                                                   |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getuserdnsaddress"><strong>getUserDNSAddress</strong></a>()<br>获取用户自定义dns服务器地址。</p>                                                                                                                                                                                                                                                                                                             |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setuserdnsaddress"><strong>setUserDNSAddress</strong></a>(const std::string &#x26; dns)<br>设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。</p>                                                                                                                                                                                                                                                       |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getappid"><strong>getAppID</strong></a>()<br>获取用户的appID。</p>                                                                                                                                                                                                                                                                                                                                    |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setappid"><strong>setAppID</strong></a>(const std::string &#x26; appID)<br>设置用户的appID。</p>                                                                                                                                                                                                                                                                                                      |
| std::string            | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getappsecret"><strong>getAppSecret</strong></a>()<br>获取用户的appSecret。</p>                                                                                                                                                                                                                                                                                                                        |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setappsecret"><strong>setAppSecret</strong></a>(const std::string &#x26; appSecret)<br>设置用户的appSecret。</p>                                                                                                                                                                                                                                                                                      |
| BMXPushProviderType    | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushprovidertype"><strong>getPushProviderType</strong></a>()<br>获取用户的推送提供商类型。</p>                                                                                                                                                                                                                                                                                                            |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushprovidertype"><strong>setPushProviderType</strong></a>(BMXPushProviderType type)<br>设置用户的推送提供商类型。</p>                                                                                                                                                                                                                                                                                    |
| BMXPushEnvironmentType | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushenvironmenttype"><strong>getPushEnvironmentType</strong></a>()<br>获取用户的推送环境类型。</p>                                                                                                                                                                                                                                                                                                       |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setenvironmenttype"><strong>setEnvironmentType</strong></a>(BMXPushEnvironmentType type)<br>设置用户的推送环境类型。</p>                                                                                                                                                                                                                                                                                    |
| int64\_t               | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-getdebuglogreceiverid"><strong>getDebugLogReceiverId</strong></a>()<br>获取调试log接收着账号(仅用于SDK调试，接收客户端log日志使用)</p>                                                                                                                                                                                                                                                                                  |
| void                   | <p><a href="classfloo_1_1_b_m_x_s_d_k_config.md#function-setdebuglogreceiverid"><strong>setDebugLogReceiverId</strong></a>(int64_t uid)<br>设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)</p>                                                                                                                                                                                                                                                                        |

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

构造函数

**Parameters**:

* **type** 客户端类型
* **vsn** 客户端OS版本
* **dataDir** 聊天数据存储路径
* **cacheDir** 缓存数据存储路径
* **SDKVersion** SDK版本
* **pushCertName** Push证书名字
* **userAgent** 用户代理信息
* **deliveryAck** 是否发送消息送达回执

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

构造函数

**Parameters**:

* **type** 客户端类型
* **vsn** 客户端OS版本
* **dataDir** 聊天数据存储路径
* **cacheDir** 缓存数据存储路径
* **SDKVersion** SDK版本
* **pushCertName** Push证书名字
* **userAgent** 用户代理信息
* **appId** 用户的appId
* **appSecret** 用户的appSecret（对于使用推送的用户，必须同时设置appId和appSecret）
* **deliveryAck** 是否发送消息送达回执

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function \~BMXSDKConfig

```cpp
virtual ~BMXSDKConfig()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getDataDir

```cpp
const std::string & getDataDir()
```

获取聊天数据存储路径，包含消息、附件等

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getCacheDir

```cpp
const std::string & getCacheDir()
```

获取缓存数据存储路径，比如用户头像

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getClientType

```cpp
BMXClientType getClientType()
```

客户端类型

**Return**: BMXClientType

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getVsn

```cpp
const std::string & getVsn()
```

客户端OS版本

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getSDKVersion

```cpp
const std::string & getSDKVersion()
```

SDK版本

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getPushCertName

```cpp
const std::string & getPushCertName()
```

获取Push证书名字

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

设置Push证书名字

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getUserAgent

```cpp
const std::string & getUserAgent()
```

获取用户代理信息

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function carryUsernameInMessage

```cpp
bool carryUsernameInMessage()
```

发送消息的config中是否携带

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

设置发送消息的config中是否携带用户名

**Parameters**:

* **bool** 设置是否在送消息的config中携带用户名

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function enableDeliveryAck

```cpp
bool enableDeliveryAck()
```

是否发送消息送达回执

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

设置是否发送消息送达回执

**Parameters**:

* **bool** 是否发送消息送达回执

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getLogLevel

```cpp
BMXLogLevel getLogLevel()
```

Log输出等级

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

设置Log输出等级

**Parameters**:

* **BMXLogLevel** Log输出等级

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getConsoleOutput

```cpp
bool getConsoleOutput()
```

Log是否输出到Console.

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

设置Log是否输出到Console

**Parameters**:

* **bool** 设置Log是否输出到Console

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

设置服务器配置

**Parameters**:

* **config** 服务器配置

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getHostConfig

```cpp
const HostConfig & getHostConfig()
```

获取服务器配置

**Return**: \[HostConfig]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getLoadAllServerConversations

```cpp
bool getLoadAllServerConversations()
```

是否根据服务器返回未读列表创建所有会话.

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

是否根据服务器返回未读列表创建所有会话，默认为false，只会创建有未读消息的会话。

**Parameters**:

* **enable** 是否根据服务器返回未读列表创建所有会话

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getDeviceUuid

```cpp
const std::string & getDeviceUuid()
```

获取设备的唯一识别码

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

设置设备的唯一识别码，在app卸载之前应该始终保持一致，app删除后再次安装时可以产生不同的设备识别码。

**Parameters**:

* **uuid** 设备的唯一识别码。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getDBCryptoKey

```cpp
const std::string & getDBCryptoKey()
```

获取设备的本地数据库加密密钥。

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

设置本地数据库的加密密钥，在app卸载之前应该始终保持一直，app删除后再次安装时可以产生不同的密钥。用于本地数据库加密。

**Parameters**:

* **cryptoKey** 本地数据库的加密密钥。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getVerifyCertificate

```cpp
bool getVerifyCertificate()
```

获取https请求是否验证服务器端证书。

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

设置https请求是否验证服务器端证书。

**Parameters**:

* **verify** https请求是否验证服务器端证书

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getEnableDNS

```cpp
bool getEnableDNS()
```

获取是否启用dns功能。

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

设置是否启用dns功能，默认是开启的。

**Parameters**:

* **enable** 是否启用dns功能

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getUserDNSAddress

```cpp
std::string getUserDNSAddress()
```

获取用户自定义dns服务器地址。

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

设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。

**Parameters**:

* **dns** 用户自定义dns服务器地址

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getAppID

```cpp
std::string getAppID()
```

获取用户的appID。

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

设置用户的appID。

**Parameters**:

* **appID** 用户的appID

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getAppSecret

```cpp
std::string getAppSecret()
```

获取用户的appSecret。

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

设置用户的appSecret。

**Parameters**:

* **appID** 用户的appSecret

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getPushProviderType

```cpp
BMXPushProviderType getPushProviderType()
```

获取用户的推送提供商类型。

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

设置用户的推送提供商类型。

**Parameters**:

* **type** 用户的推送提供商类型

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getPushEnvironmentType

```cpp
BMXPushEnvironmentType getPushEnvironmentType()
```

获取用户的推送环境类型。

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

设置用户的推送环境类型。

**Parameters**:

* **type** 用户的推送环境类型

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>

```

### function getDebugLogReceiverId

```cpp
int64_t getDebugLogReceiverId()
```

获取调试log接收着账号(仅用于SDK调试，接收客户端log日志使用)

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

设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)

**Parameters**:

* **uid** 调试log接收者id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXSDKConfig'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
