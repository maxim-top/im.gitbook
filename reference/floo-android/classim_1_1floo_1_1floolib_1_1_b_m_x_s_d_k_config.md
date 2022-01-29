---
title: im::floo::floolib::BMXSDKConfig
summary: SDK settings management 

---

# im::floo::floolib::BMXSDKConfig



SDK settings management 

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[HostConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config_1_1_host_config.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-delete)**() |
| | **[BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**([BMXClientType] type, String vsn, String dataDir, String cacheDir, String pushCertName, boolean deliveryAck)<br>Constructor  |
| | **[BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**([BMXClientType] type, String vsn, String dataDir, String cacheDir, String pushCertName) |
| | **[BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**([BMXClientType] type, String vsn, String dataDir, String cacheDir, String pushCertName, String appId, String appSecret, boolean deliveryAck) |
| | **[BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**([BMXClientType] type, String vsn, String dataDir, String cacheDir, String pushCertName, String appId, String appSecret) |
| String | **[getDataDir](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getdatadir)**() |
| String | **[getCacheDir](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getcachedir)**() |
| [BMXClientType] | **[getClientType](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getclienttype)**() |
| String | **[getVsn](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getvsn)**() |
| String | **[getSDKVersion](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getsdkversion)**() |
| String | **[getPushCertName](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getpushcertname)**() |
| void | **[setPushCertName](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setpushcertname)**(String arg0) |
| String | **[getUserAgent](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getuseragent)**() |
| boolean | **[carryUsernameInMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-carryusernameinmessage)**() |
| void | **[setCarryUsernameInMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setcarryusernameinmessage)**(boolean arg0) |
| boolean | **[enableDeliveryAck](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-enabledeliveryack)**() |
| void | **[setEnableDeliveryAck](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setenabledeliveryack)**(boolean arg0) |
| BMXLogLevel | **[getLogLevel](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getloglevel)**() |
| void | **[setLogLevel](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setloglevel)**(BMXLogLevel arg0) |
| boolean | **[getConsoleOutput](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getconsoleoutput)**() |
| void | **[setConsoleOutput](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setconsoleoutput)**(boolean arg0) |
| void | **[setHostConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-sethostconfig)**(BMXSDKConfig.HostConfig config) |
| BMXSDKConfig.HostConfig | **[getHostConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-gethostconfig)**() |
| boolean | **[getLoadAllServerConversations](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getloadallserverconversations)**() |
| void | **[setLoadAllServerConversations](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations)**(boolean enable) |
| void | **[setLoadAllServerConversations](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setloadallserverconversations)**() |
| String | **[getDeviceUuid](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getdeviceuuid)**() |
| void | **[setDeviceUuid](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setdeviceuuid)**(String uuid) |
| String | **[getDBCryptoKey](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getdbcryptokey)**() |
| void | **[setDBCryptoKey](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setdbcryptokey)**(String cryptoKey) |
| boolean | **[getVerifyCertificate](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getverifycertificate)**() |
| void | **[setVerifyCertificate](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate)**(boolean verify) |
| void | **[setVerifyCertificate](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setverifycertificate)**() |
| boolean | **[getEnableDNS](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getenabledns)**() |
| void | **[setEnableDNS](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setenabledns)**(boolean enable) |
| void | **[setEnableDNS](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setenabledns)**() |
| String | **[getUserDNSAddress](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getuserdnsaddress)**() |
| void | **[setUserDNSAddress](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setuserdnsaddress)**(String dns) |
| String | **[getAppID](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getappid)**() |
| void | **[setAppID](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setappid)**(String appID) |
| String | **[getAppSecret](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getappsecret)**() |
| void | **[setAppSecret](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setappsecret)**(String appSecret) |
| [BMXPushProviderType] | **[getPushProviderType](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getpushprovidertype)**() |
| void | **[setPushProviderType](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setpushprovidertype)**([BMXPushProviderType] type) |
| [BMXPushEnvironmentType] | **[getPushEnvironmentType](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getpushenvironmenttype)**() |
| void | **[setEnvironmentType](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setenvironmenttype)**([BMXPushEnvironmentType] type) |
| long | **[getDebugLogReceiverId](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getdebuglogreceiverid)**() |
| void | **[setDebugLogReceiverId](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-setdebuglogreceiverid)**(long uid) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-bmxsdkconfig)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md#function-getcptr)**([BMXSDKConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_s_d_k_config.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function BMXSDKConfig

```java
inline BMXSDKConfig(
    BMXClientType type,
    String vsn,
    String dataDir,
    String cacheDir,
    String pushCertName,
    boolean deliveryAck
)
```

Constructor 

**Parameters**: 

  * **type** Client type 
  * **vsn** Client OS version 
  * **dataDir** Storage path of chat data 
  * **cacheDir** Storage path of cached data 
  * **pushCertName** Push certificate name 
  * **deliveryAck** Whether to send message delivery receipt 


### function BMXSDKConfig

```java
inline BMXSDKConfig(
    BMXClientType type,
    String vsn,
    String dataDir,
    String cacheDir,
    String pushCertName
)
```


### function BMXSDKConfig

```java
inline BMXSDKConfig(
    BMXClientType type,
    String vsn,
    String dataDir,
    String cacheDir,
    String pushCertName,
    String appId,
    String appSecret,
    boolean deliveryAck
)
```


### function BMXSDKConfig

```java
inline BMXSDKConfig(
    BMXClientType type,
    String vsn,
    String dataDir,
    String cacheDir,
    String pushCertName,
    String appId,
    String appSecret
)
```


### function getDataDir

```java
inline String getDataDir()
```


### function getCacheDir

```java
inline String getCacheDir()
```


### function getClientType

```java
inline BMXClientType getClientType()
```


### function getVsn

```java
inline String getVsn()
```


### function getSDKVersion

```java
inline String getSDKVersion()
```


### function getPushCertName

```java
inline String getPushCertName()
```


### function setPushCertName

```java
inline void setPushCertName(
    String arg0
)
```


### function getUserAgent

```java
inline String getUserAgent()
```


### function carryUsernameInMessage

```java
inline boolean carryUsernameInMessage()
```


### function setCarryUsernameInMessage

```java
inline void setCarryUsernameInMessage(
    boolean arg0
)
```


### function enableDeliveryAck

```java
inline boolean enableDeliveryAck()
```


### function setEnableDeliveryAck

```java
inline void setEnableDeliveryAck(
    boolean arg0
)
```


### function getLogLevel

```java
inline BMXLogLevel getLogLevel()
```


### function setLogLevel

```java
inline void setLogLevel(
    BMXLogLevel arg0
)
```


### function getConsoleOutput

```java
inline boolean getConsoleOutput()
```


### function setConsoleOutput

```java
inline void setConsoleOutput(
    boolean arg0
)
```


### function setHostConfig

```java
inline void setHostConfig(
    BMXSDKConfig.HostConfig config
)
```


### function getHostConfig

```java
inline BMXSDKConfig.HostConfig getHostConfig()
```


### function getLoadAllServerConversations

```java
inline boolean getLoadAllServerConversations()
```


### function setLoadAllServerConversations

```java
inline void setLoadAllServerConversations(
    boolean enable
)
```


### function setLoadAllServerConversations

```java
inline void setLoadAllServerConversations()
```


### function getDeviceUuid

```java
inline String getDeviceUuid()
```


### function setDeviceUuid

```java
inline void setDeviceUuid(
    String uuid
)
```


### function getDBCryptoKey

```java
inline String getDBCryptoKey()
```


### function setDBCryptoKey

```java
inline void setDBCryptoKey(
    String cryptoKey
)
```


### function getVerifyCertificate

```java
inline boolean getVerifyCertificate()
```


### function setVerifyCertificate

```java
inline void setVerifyCertificate(
    boolean verify
)
```


### function setVerifyCertificate

```java
inline void setVerifyCertificate()
```


### function getEnableDNS

```java
inline boolean getEnableDNS()
```


### function setEnableDNS

```java
inline void setEnableDNS(
    boolean enable
)
```


### function setEnableDNS

```java
inline void setEnableDNS()
```


### function getUserDNSAddress

```java
inline String getUserDNSAddress()
```


### function setUserDNSAddress

```java
inline void setUserDNSAddress(
    String dns
)
```


### function getAppID

```java
inline String getAppID()
```


### function setAppID

```java
inline void setAppID(
    String appID
)
```


### function getAppSecret

```java
inline String getAppSecret()
```


### function setAppSecret

```java
inline void setAppSecret(
    String appSecret
)
```


### function getPushProviderType

```java
inline BMXPushProviderType getPushProviderType()
```


### function setPushProviderType

```java
inline void setPushProviderType(
    BMXPushProviderType type
)
```


### function getPushEnvironmentType

```java
inline BMXPushEnvironmentType getPushEnvironmentType()
```


### function setEnvironmentType

```java
inline void setEnvironmentType(
    BMXPushEnvironmentType type
)
```


### function getDebugLogReceiverId

```java
inline long getDebugLogReceiverId()
```


### function setDebugLogReceiverId

```java
inline void setDebugLogReceiverId(
    long uid
)
```


## Protected Functions Documentation

### function BMXSDKConfig

```java
inline BMXSDKConfig(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function getCPtr

```java
static inline long getCPtr(
    BMXSDKConfig obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800