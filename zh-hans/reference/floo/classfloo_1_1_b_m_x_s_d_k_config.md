---
title: floo::BMXSDKConfig
summary: SDK设置管理 

---

# floo::BMXSDKConfig



SDK设置管理 


`#include <bmx_sdk_config.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**(BMXClientType type, const std::string & vsn, const std::string & dataDir, const std::string & cacheDir, const std::string & SDKVersion, const std::string & pushCertName, const std::string & userAgent, bool deliveryAck =false)<br>构造函数  |
| | **[BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**(BMXClientType type, const std::string & vsn, const std::string & dataDir, const std::string & cacheDir, const std::string & SDKVersion, const std::string & pushCertName, const std::string & userAgent, const std::string & appId, const std::string & appSecret, bool deliveryAck =false)<br>构造函数  |
| virtual | **[~BMXSDKConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-~bmxsdkconfig)**()<br>析构函数  |
| const std::string & | **[getDataDir](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdatadir)**()<br>获取聊天数据存储路径，包含消息、附件等  |
| const std::string & | **[getCacheDir](classfloo_1_1_b_m_x_s_d_k_config.md#function-getcachedir)**()<br>获取缓存数据存储路径，比如用户头像  |
| BMXClientType | **[getClientType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getclienttype)**()<br>客户端类型  |
| const std::string & | **[getVsn](classfloo_1_1_b_m_x_s_d_k_config.md#function-getvsn)**()<br>客户端OS版本  |
| const std::string & | **[getSDKVersion](classfloo_1_1_b_m_x_s_d_k_config.md#function-getsdkversion)**()<br>SDK版本  |
| const std::string & | **[getPushCertName](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushcertname)**()<br>获取Push证书名字  |
| void | **[setPushCertName](classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushcertname)**(const std::string & )<br>设置Push证书名字  |
| const std::string & | **[getUserAgent](classfloo_1_1_b_m_x_s_d_k_config.md#function-getuseragent)**()<br>获取用户代理信息  |
| bool | **[carryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage)**()<br>发送消息的config中是否携带  |
| void | **[setCarryUsernameInMessage](classfloo_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage)**(bool )<br>设置发送消息的config中是否携带用户名  |
| bool | **[enableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack)**()<br>是否发送消息送达回执  |
| void | **[setEnableDeliveryAck](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack)**(bool )<br>设置是否发送消息送达回执  |
| BMXLogLevel | **[getLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloglevel)**()<br>Log输出等级  |
| void | **[setLogLevel](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloglevel)**(BMXLogLevel )<br>设置Log输出等级  |
| bool | **[getConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput)**()<br>Log是否输出到Console.  |
| void | **[setConsoleOutput](classfloo_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput)**(bool )<br>设置Log是否输出到Console  |
| void | **[setHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-sethostconfig)**(const [HostConfig] & config)<br>设置服务器配置  |
| const [HostConfig] & | **[getHostConfig](classfloo_1_1_b_m_x_s_d_k_config.md#function-gethostconfig)**()<br>获取服务器配置  |
| bool | **[getLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations)**()<br>是否根据服务器返回未读列表创建所有会话.  |
| void | **[setLoadAllServerConversations](classfloo_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations)**(bool enable =false)<br>是否根据服务器返回未读列表创建所有会话，默认为false，只会创建有未读消息的会话。  |
| const std::string & | **[getDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid)**()<br>获取设备的唯一识别码  |
| void | **[setDeviceUuid](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid)**(const std::string & uuid)<br>设置设备的唯一识别码，在app卸载之前应该始终保持一致，app删除后再次安装时可以产生不同的设备识别码。  |
| const std::string & | **[getDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey)**()<br>获取设备的本地数据库加密密钥。  |
| void | **[setDBCryptoKey](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey)**(const std::string & cryptoKey)<br>设置本地数据库的加密密钥，在app卸载之前应该始终保持一直，app删除后再次安装时可以产生不同的密钥。用于本地数据库加密。  |
| bool | **[getVerifyCertificate](classfloo_1_1_b_m_x_s_d_k_config.md#function-getverifycertificate)**()<br>获取https请求是否验证服务器端证书。  |
| void | **[setVerifyCertificate](classfloo_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate)**(bool verify =true)<br>设置https请求是否验证服务器端证书。  |
| bool | **[getEnableDNS](classfloo_1_1_b_m_x_s_d_k_config.md#function-getenabledns)**()<br>获取是否启用dns功能。  |
| void | **[setEnableDNS](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenabledns)**(bool enable =true)<br>设置是否启用dns功能，默认是开启的。  |
| std::string | **[getUserDNSAddress](classfloo_1_1_b_m_x_s_d_k_config.md#function-getuserdnsaddress)**()<br>获取用户自定义dns服务器地址。  |
| void | **[setUserDNSAddress](classfloo_1_1_b_m_x_s_d_k_config.md#function-setuserdnsaddress)**(const std::string & dns)<br>设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。  |
| std::string | **[getAppID](classfloo_1_1_b_m_x_s_d_k_config.md#function-getappid)**()<br>获取用户的appID。  |
| void | **[setAppID](classfloo_1_1_b_m_x_s_d_k_config.md#function-setappid)**(const std::string & appID)<br>设置用户的appID。  |
| std::string | **[getAppSecret](classfloo_1_1_b_m_x_s_d_k_config.md#function-getappsecret)**()<br>获取用户的appSecret。  |
| void | **[setAppSecret](classfloo_1_1_b_m_x_s_d_k_config.md#function-setappsecret)**(const std::string & appSecret)<br>设置用户的appSecret。  |
| BMXPushProviderType | **[getPushProviderType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushprovidertype)**()<br>获取用户的推送提供商类型。  |
| void | **[setPushProviderType](classfloo_1_1_b_m_x_s_d_k_config.md#function-setpushprovidertype)**(BMXPushProviderType type)<br>设置用户的推送提供商类型。  |
| BMXPushEnvironmentType | **[getPushEnvironmentType](classfloo_1_1_b_m_x_s_d_k_config.md#function-getpushenvironmenttype)**()<br>获取用户的推送环境类型。  |
| void | **[setEnvironmentType](classfloo_1_1_b_m_x_s_d_k_config.md#function-setenvironmenttype)**(BMXPushEnvironmentType type)<br>设置用户的推送环境类型。  |
| int64_t | **[getDebugLogReceiverId](classfloo_1_1_b_m_x_s_d_k_config.md#function-getdebuglogreceiverid)**()<br>获取调试log接收着账号(仅用于SDK调试，接收客户端log日志使用)  |
| void | **[setDebugLogReceiverId](classfloo_1_1_b_m_x_s_d_k_config.md#function-setdebuglogreceiverid)**(int64_t uid)<br>设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)  |

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


### function ~BMXSDKConfig

```cpp
virtual ~BMXSDKConfig()
```

析构函数 

### function getDataDir

```cpp
const std::string & getDataDir()
```

获取聊天数据存储路径，包含消息、附件等 

**Return**: std::string 

### function getCacheDir

```cpp
const std::string & getCacheDir()
```

获取缓存数据存储路径，比如用户头像 

**Return**: std::string 

### function getClientType

```cpp
BMXClientType getClientType()
```

客户端类型 

**Return**: BMXClientType 

### function getVsn

```cpp
const std::string & getVsn()
```

客户端OS版本 

**Return**: std::string 

### function getSDKVersion

```cpp
const std::string & getSDKVersion()
```

SDK版本 

**Return**: std::string 

### function getPushCertName

```cpp
const std::string & getPushCertName()
```

获取Push证书名字 

**Return**: std::string 

### function setPushCertName

```cpp
void setPushCertName(
    const std::string & 
)
```

设置Push证书名字 

**Return**: std::string 

### function getUserAgent

```cpp
const std::string & getUserAgent()
```

获取用户代理信息 

**Return**: std::string 

### function carryUsernameInMessage

```cpp
bool carryUsernameInMessage()
```

发送消息的config中是否携带 

**Return**: bool 

### function setCarryUsernameInMessage

```cpp
void setCarryUsernameInMessage(
    bool 
)
```

设置发送消息的config中是否携带用户名 

**Parameters**: 

  * **bool** 设置是否在送消息的config中携带用户名 


### function enableDeliveryAck

```cpp
bool enableDeliveryAck()
```

是否发送消息送达回执 

**Return**: bool 

### function setEnableDeliveryAck

```cpp
void setEnableDeliveryAck(
    bool 
)
```

设置是否发送消息送达回执 

**Parameters**: 

  * **bool** 是否发送消息送达回执 


### function getLogLevel

```cpp
BMXLogLevel getLogLevel()
```

Log输出等级 

**Return**: BMXLogLevel 

### function setLogLevel

```cpp
void setLogLevel(
    BMXLogLevel 
)
```

设置Log输出等级 

**Parameters**: 

  * **BMXLogLevel** Log输出等级 


### function getConsoleOutput

```cpp
bool getConsoleOutput()
```

Log是否输出到Console. 

**Return**: bool 

### function setConsoleOutput

```cpp
void setConsoleOutput(
    bool 
)
```

设置Log是否输出到Console 

**Parameters**: 

  * **bool** 设置Log是否输出到Console 


### function setHostConfig

```cpp
void setHostConfig(
    const HostConfig & config
)
```

设置服务器配置 

**Parameters**: 

  * **config** 服务器配置 


### function getHostConfig

```cpp
const HostConfig & getHostConfig()
```

获取服务器配置 

**Return**: [HostConfig]

### function getLoadAllServerConversations

```cpp
bool getLoadAllServerConversations()
```

是否根据服务器返回未读列表创建所有会话. 

**Return**: bool 

### function setLoadAllServerConversations

```cpp
void setLoadAllServerConversations(
    bool enable =false
)
```

是否根据服务器返回未读列表创建所有会话，默认为false，只会创建有未读消息的会话。 

**Parameters**: 

  * **enable** 是否根据服务器返回未读列表创建所有会话 


### function getDeviceUuid

```cpp
const std::string & getDeviceUuid()
```

获取设备的唯一识别码 

**Return**: std::string 

### function setDeviceUuid

```cpp
void setDeviceUuid(
    const std::string & uuid
)
```

设置设备的唯一识别码，在app卸载之前应该始终保持一致，app删除后再次安装时可以产生不同的设备识别码。 

**Parameters**: 

  * **uuid** 设备的唯一识别码。 


### function getDBCryptoKey

```cpp
const std::string & getDBCryptoKey()
```

获取设备的本地数据库加密密钥。 

**Return**: std::string 

### function setDBCryptoKey

```cpp
void setDBCryptoKey(
    const std::string & cryptoKey
)
```

设置本地数据库的加密密钥，在app卸载之前应该始终保持一直，app删除后再次安装时可以产生不同的密钥。用于本地数据库加密。 

**Parameters**: 

  * **cryptoKey** 本地数据库的加密密钥。 


### function getVerifyCertificate

```cpp
bool getVerifyCertificate()
```

获取https请求是否验证服务器端证书。 

**Return**: bool 

### function setVerifyCertificate

```cpp
void setVerifyCertificate(
    bool verify =true
)
```

设置https请求是否验证服务器端证书。 

**Parameters**: 

  * **verify** https请求是否验证服务器端证书 


### function getEnableDNS

```cpp
bool getEnableDNS()
```

获取是否启用dns功能。 

**Return**: bool 

### function setEnableDNS

```cpp
void setEnableDNS(
    bool enable =true
)
```

设置是否启用dns功能，默认是开启的。 

**Parameters**: 

  * **enable** 是否启用dns功能 


### function getUserDNSAddress

```cpp
std::string getUserDNSAddress()
```

获取用户自定义dns服务器地址。 

**Return**: std::string 

### function setUserDNSAddress

```cpp
void setUserDNSAddress(
    const std::string & dns
)
```

设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。 

**Parameters**: 

  * **dns** 用户自定义dns服务器地址 


### function getAppID

```cpp
std::string getAppID()
```

获取用户的appID。 

**Return**: std::string 

### function setAppID

```cpp
void setAppID(
    const std::string & appID
)
```

设置用户的appID。 

**Parameters**: 

  * **appID** 用户的appID 


### function getAppSecret

```cpp
std::string getAppSecret()
```

获取用户的appSecret。 

**Return**: std::string 

### function setAppSecret

```cpp
void setAppSecret(
    const std::string & appSecret
)
```

设置用户的appSecret。 

**Parameters**: 

  * **appID** 用户的appSecret 


### function getPushProviderType

```cpp
BMXPushProviderType getPushProviderType()
```

获取用户的推送提供商类型。 

**Return**: BMXPushProviderType 

### function setPushProviderType

```cpp
void setPushProviderType(
    BMXPushProviderType type
)
```

设置用户的推送提供商类型。 

**Parameters**: 

  * **type** 用户的推送提供商类型 


### function getPushEnvironmentType

```cpp
BMXPushEnvironmentType getPushEnvironmentType()
```

获取用户的推送环境类型。 

**Return**: BMXPushEnvironmentType 

### function setEnvironmentType

```cpp
void setEnvironmentType(
    BMXPushEnvironmentType type
)
```

设置用户的推送环境类型。 

**Parameters**: 

  * **type** 用户的推送环境类型 


### function getDebugLogReceiverId

```cpp
int64_t getDebugLogReceiverId()
```

获取调试log接收着账号(仅用于SDK调试，接收客户端log日志使用) 

**Return**: int64_t 

### function setDebugLogReceiverId

```cpp
void setDebugLogReceiverId(
    int64_t uid
)
```

设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用) 

**Parameters**: 

  * **uid** 调试log接收者id 


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800