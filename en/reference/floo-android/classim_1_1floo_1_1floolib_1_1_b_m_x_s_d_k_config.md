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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="delete" %}{% endlanying_code_snippet %}
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
  * **deliveryAck** Whether to send message delivery acknowledgement 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
```
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
```
### function getDataDir

```java
inline String getDataDir()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getDataDir" %}{% endlanying_code_snippet %}
```
### function getCacheDir

```java
inline String getCacheDir()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getCacheDir" %}{% endlanying_code_snippet %}
```
### function getClientType

```java
inline BMXClientType getClientType()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getClientType" %}{% endlanying_code_snippet %}
```
### function getVsn

```java
inline String getVsn()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getVsn" %}{% endlanying_code_snippet %}
```
### function getSDKVersion

```java
inline String getSDKVersion()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getSDKVersion" %}{% endlanying_code_snippet %}
```
### function getPushCertName

```java
inline String getPushCertName()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getPushCertName" %}{% endlanying_code_snippet %}
```
### function setPushCertName

```java
inline void setPushCertName(
    String arg0
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setPushCertName" %}{% endlanying_code_snippet %}
```
### function getUserAgent

```java
inline String getUserAgent()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getUserAgent" %}{% endlanying_code_snippet %}
```
### function carryUsernameInMessage

```java
inline boolean carryUsernameInMessage()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="carryUsernameInMessage" %}{% endlanying_code_snippet %}
```
### function setCarryUsernameInMessage

```java
inline void setCarryUsernameInMessage(
    boolean arg0
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setCarryUsernameInMessage" %}{% endlanying_code_snippet %}
```
### function enableDeliveryAck

```java
inline boolean enableDeliveryAck()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="enableDeliveryAck" %}{% endlanying_code_snippet %}
```
### function setEnableDeliveryAck

```java
inline void setEnableDeliveryAck(
    boolean arg0
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setEnableDeliveryAck" %}{% endlanying_code_snippet %}
```
### function getLogLevel

```java
inline BMXLogLevel getLogLevel()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getLogLevel" %}{% endlanying_code_snippet %}
```
### function setLogLevel

```java
inline void setLogLevel(
    BMXLogLevel arg0
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setLogLevel" %}{% endlanying_code_snippet %}
```
### function getConsoleOutput

```java
inline boolean getConsoleOutput()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getConsoleOutput" %}{% endlanying_code_snippet %}
```
### function setConsoleOutput

```java
inline void setConsoleOutput(
    boolean arg0
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setConsoleOutput" %}{% endlanying_code_snippet %}
```
### function setHostConfig

```java
inline void setHostConfig(
    BMXSDKConfig.HostConfig config
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setHostConfig" %}{% endlanying_code_snippet %}
```
### function getHostConfig

```java
inline BMXSDKConfig.HostConfig getHostConfig()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getHostConfig" %}{% endlanying_code_snippet %}
```
### function getLoadAllServerConversations

```java
inline boolean getLoadAllServerConversations()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### function setLoadAllServerConversations

```java
inline void setLoadAllServerConversations(
    boolean enable
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### function setLoadAllServerConversations

```java
inline void setLoadAllServerConversations()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### function getDeviceUuid

```java
inline String getDeviceUuid()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getDeviceUuid" %}{% endlanying_code_snippet %}
```
### function setDeviceUuid

```java
inline void setDeviceUuid(
    String uuid
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setDeviceUuid" %}{% endlanying_code_snippet %}
```
### function getDBCryptoKey

```java
inline String getDBCryptoKey()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getDBCryptoKey" %}{% endlanying_code_snippet %}
```
### function setDBCryptoKey

```java
inline void setDBCryptoKey(
    String cryptoKey
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setDBCryptoKey" %}{% endlanying_code_snippet %}
```
### function getVerifyCertificate

```java
inline boolean getVerifyCertificate()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getVerifyCertificate" %}{% endlanying_code_snippet %}
```
### function setVerifyCertificate

```java
inline void setVerifyCertificate(
    boolean verify
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setVerifyCertificate" %}{% endlanying_code_snippet %}
```
### function setVerifyCertificate

```java
inline void setVerifyCertificate()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setVerifyCertificate" %}{% endlanying_code_snippet %}
```
### function getEnableDNS

```java
inline boolean getEnableDNS()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getEnableDNS" %}{% endlanying_code_snippet %}
```
### function setEnableDNS

```java
inline void setEnableDNS(
    boolean enable
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setEnableDNS" %}{% endlanying_code_snippet %}
```
### function setEnableDNS

```java
inline void setEnableDNS()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setEnableDNS" %}{% endlanying_code_snippet %}
```
### function getUserDNSAddress

```java
inline String getUserDNSAddress()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getUserDNSAddress" %}{% endlanying_code_snippet %}
```
### function setUserDNSAddress

```java
inline void setUserDNSAddress(
    String dns
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setUserDNSAddress" %}{% endlanying_code_snippet %}
```
### function getAppID

```java
inline String getAppID()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getAppID" %}{% endlanying_code_snippet %}
```
### function setAppID

```java
inline void setAppID(
    String appID
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setAppID" %}{% endlanying_code_snippet %}
```
### function getAppSecret

```java
inline String getAppSecret()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getAppSecret" %}{% endlanying_code_snippet %}
```
### function setAppSecret

```java
inline void setAppSecret(
    String appSecret
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setAppSecret" %}{% endlanying_code_snippet %}
```
### function getPushProviderType

```java
inline BMXPushProviderType getPushProviderType()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getPushProviderType" %}{% endlanying_code_snippet %}
```
### function setPushProviderType

```java
inline void setPushProviderType(
    BMXPushProviderType type
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setPushProviderType" %}{% endlanying_code_snippet %}
```
### function getPushEnvironmentType

```java
inline BMXPushEnvironmentType getPushEnvironmentType()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getPushEnvironmentType" %}{% endlanying_code_snippet %}
```
### function setEnvironmentType

```java
inline void setEnvironmentType(
    BMXPushEnvironmentType type
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setEnvironmentType" %}{% endlanying_code_snippet %}
```
### function getDebugLogReceiverId

```java
inline long getDebugLogReceiverId()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getDebugLogReceiverId" %}{% endlanying_code_snippet %}
```
### function setDebugLogReceiverId

```java
inline void setDebugLogReceiverId(
    long uid
)
```


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="setDebugLogReceiverId" %}{% endlanying_code_snippet %}
```
### function BMXSDKConfig

```java
inline BMXSDKConfig(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="BMXSDKConfig" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXSDKConfig obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXSDKConfig",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800