# BMXSDKConfig Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface SDK config

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/carryUsernameInMessage" title="carryUsernameInMessage"></a>
### carryUsernameInMessage

Whether to carry the username in the message

`- (BOOL)carryUsernameInMessage`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="carryUsernameInMessage" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/enableDeliveryAck" title="enableDeliveryAck"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="dealloc" %}{% endlanying_code_snippet %}
```
### enableDeliveryAck

Whether to enable the delivery ACK

`- (BOOL)enableDeliveryAck`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAppID" title="getAppID"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="enableDeliveryAck" %}{% endlanying_code_snippet %}
```
### getAppID

Get the app ID

`- (NSString *)getAppID`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAppSecret" title="getAppSecret"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getAppID" %}{% endlanying_code_snippet %}
```
### getAppSecret

Get app secret

`- (NSString *)getAppSecret`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getCacheDir" title="getCacheDir"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getAppSecret" %}{% endlanying_code_snippet %}
```
### getCacheDir

Get cache files directory

`- (NSString *)getCacheDir`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getClientType" title="getClientType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getCacheDir" %}{% endlanying_code_snippet %}
```
### getClientType

Get client device type

`- (BMXClientType)getClientType`

#### Return Value
<a href="../Constants/BMXClientType.md">BMXClientType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getConsoleOutput" title="getConsoleOutput"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getClientType" %}{% endlanying_code_snippet %}
```
### getConsoleOutput

Get the switch of whether to output the log to console

`- (BOOL)getConsoleOutput`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDBCryptoKey" title="getDBCryptoKey"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getConsoleOutput" %}{% endlanying_code_snippet %}
```
### getDBCryptoKey

Get crypto key of local db

`- (NSString *)getDBCryptoKey`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDataDir" title="getDataDir"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getDBCryptoKey" %}{% endlanying_code_snippet %}
```
### getDataDir

Get data files directory

`- (NSString *)getDataDir`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDebugLogReceiverId" title="getDebugLogReceiverId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getDataDir" %}{% endlanying_code_snippet %}
```
### getDebugLogReceiverId

Get debug log files receiver ID

`- (long long)getDebugLogReceiverId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDeviceUuid" title="getDeviceUuid"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getDebugLogReceiverId" %}{% endlanying_code_snippet %}
```
### getDeviceUuid

Get device UUID

`- (NSString *)getDeviceUuid`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getEnableDNS" title="getEnableDNS"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getDeviceUuid" %}{% endlanying_code_snippet %}
```
### getEnableDNS

Get whether to enable DNS on ratel

`- (BOOL)getEnableDNS`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getHostConfig" title="getHostConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getEnableDNS" %}{% endlanying_code_snippet %}
```
### getHostConfig

Get server hosts information

`- (BMXSDKConfigHostConfig *)getHostConfig`

#### Return Value
<a href="../Classes/BMXSDKConfigHostConfig.md">BMXSDKConfigHostConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLoadAllServerConversations" title="getLoadAllServerConversations"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getHostConfig" %}{% endlanying_code_snippet %}
```
### getLoadAllServerConversations

Whether to generate conversation list from server

`- (BOOL)getLoadAllServerConversations`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLogLevel" title="getLogLevel"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### getLogLevel

Get log level

`- (BMXLogLevel)getLogLevel`

#### Return Value
<a href="../Constants/BMXLogLevel.md">BMXLogLevel</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushCertName" title="getPushCertName"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getLogLevel" %}{% endlanying_code_snippet %}
```
### getPushCertName

Get the push certificate name

`- (NSString *)getPushCertName`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushEnvironmentType" title="getPushEnvironmentType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getPushCertName" %}{% endlanying_code_snippet %}
```
### getPushEnvironmentType

Get push environment type(Development|Product)

`- (BMXPushEnvironmentType)getPushEnvironmentType`

#### Return Value
<a href="../Constants/BMXPushEnvironmentType.md">BMXPushEnvironmentType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushProviderType" title="getPushProviderType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getPushEnvironmentType" %}{% endlanying_code_snippet %}
```
### getPushProviderType

Get push service provider type

`- (BMXPushProviderType)getPushProviderType`

#### Return Value
<a href="../Constants/BMXPushProviderType.md">BMXPushProviderType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSDKVersion" title="getSDKVersion"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getPushProviderType" %}{% endlanying_code_snippet %}
```
### getSDKVersion

Get SDK version

`- (NSString *)getSDKVersion`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getUserAgent" title="getUserAgent"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getSDKVersion" %}{% endlanying_code_snippet %}
```
### getUserAgent

Get user agent

`- (NSString *)getUserAgent`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getUserDNSAddress" title="getUserDNSAddress"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getUserAgent" %}{% endlanying_code_snippet %}
```
### getUserDNSAddress

Get custom DNS address

`- (NSString *)getUserDNSAddress`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getVerifyCertificate" title="getVerifyCertificate"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getUserDNSAddress" %}{% endlanying_code_snippet %}
```
### getVerifyCertificate

Get whether to verify HTTP certificate

`- (BOOL)getVerifyCertificate`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getVsn" title="getVsn"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getVerifyCertificate" %}{% endlanying_code_snippet %}
```
### getVsn

Ge app client version

`- (NSString *)getVsn`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="getVsn" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:" title="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent*`

<a name="//api/name/initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:" title="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:" %}{% endlanying_code_snippet %}
```
### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* appId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

<a name="//api/name/initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:deliveryAck:" title="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:deliveryAck:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:" %}{% endlanying_code_snippet %}
```
### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:deliveryAck:

Constructor

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* appId:(NSString *)*appId* appSecret:(NSString *)*appSecret* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

*type*  
   Client type

*vsn*  
   App client version

*dataDir*  
   Data files directory

*cacheDir*  
   Cache files directory

*SDKVersion*  
   SDK version 

*pushCertName*  
   Push certificate name  

*userAgent*  
   User agent

*appId*  
    App ID

*appSecret*  
    App secret

*deliveryAck*  
    Delivery ACK

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:" title="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:deliveryAck:" %}{% endlanying_code_snippet %}
```
### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:

Constructor

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

*type*  
   Client type

*vsn*  
   App client version

*dataDir*  
   Data files directory

*cacheDir*  
   Cache files directory

*SDKVersion*  
   SDK version 

*pushCertName*  
   Push certificate name  

*userAgent*  
   User agent

*deliveryAck*  
    Delivery ACK

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAppID:" title="setAppID:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:" %}{% endlanying_code_snippet %}
```
### setAppID:

Set app ID

`- (void)setAppID:(NSString *)*appID*`

#### Parameters

*appID*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAppSecret:" title="setAppSecret:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setAppID:" %}{% endlanying_code_snippet %}
```
### setAppSecret:

Set app secret

`- (void)setAppSecret:(NSString *)*appSecret*`

#### Parameters

*appSecret*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setCarryUsernameInMessage:" title="setCarryUsernameInMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setAppSecret:" %}{% endlanying_code_snippet %}
```
### setCarryUsernameInMessage:

Set whether to carry the username in the message

`- (void)setCarryUsernameInMessage:(BOOL)*arg1*`

#### Parameters

*bool*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setConsoleOutput:" title="setConsoleOutput:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setCarryUsernameInMessage:" %}{% endlanying_code_snippet %}
```
### setConsoleOutput:

Set the switch of whether to output the log to console

`- (void)setConsoleOutput:(BOOL)*arg1*`

#### Parameters

*bool*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDBCryptoKey:" title="setDBCryptoKey:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setConsoleOutput:" %}{% endlanying_code_snippet %}
```
### setDBCryptoKey:

Set crypto key of local db

`- (void)setDBCryptoKey:(NSString *)*cryptoKey*`

#### Parameters

*cryptoKey*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDebugLogReceiverId:" title="setDebugLogReceiverId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setDBCryptoKey:" %}{% endlanying_code_snippet %}
```
### setDebugLogReceiverId:

Set debug log files receiver ID

`- (void)setDebugLogReceiverId:(long long)*uid*`

#### Parameters

*uid*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDeviceUuid:" title="setDeviceUuid:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setDebugLogReceiverId:" %}{% endlanying_code_snippet %}
```
### setDeviceUuid:

Set device UUID

`- (void)setDeviceUuid:(NSString *)*uuid*`

#### Parameters

*uuid*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableDNS" title="setEnableDNS"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setDeviceUuid:" %}{% endlanying_code_snippet %}
```
### setEnableDNS

`- (void)setEnableDNS`

<a name="//api/name/setEnableDNS:" title="setEnableDNS:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setEnableDNS" %}{% endlanying_code_snippet %}
```
### setEnableDNS:

Set whether to enable the delivery ACK

`- (void)setEnableDNS:(BOOL)*enable*`

#### Parameters

*enable*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableDeliveryAck:" title="setEnableDeliveryAck:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setEnableDNS:" %}{% endlanying_code_snippet %}
```
### setEnableDeliveryAck:

Enable delivery ACK

`- (void)setEnableDeliveryAck:(BOOL)*arg1*`

#### Parameters

*bool*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnvironmentType:" title="setEnvironmentType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setEnableDeliveryAck:" %}{% endlanying_code_snippet %}
```
### setEnvironmentType:

Set push environment type(Development|Product)

`- (void)setEnvironmentType:(BMXPushEnvironmentType)*type*`

#### Parameters

*type*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setHostConfig:" title="setHostConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setEnvironmentType:" %}{% endlanying_code_snippet %}
```
### setHostConfig:

Set server hosts config

`- (void)setHostConfig:(BMXSDKConfigHostConfig *)*config*`

#### Parameters

*config*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setLoadAllServerConversations" title="setLoadAllServerConversations"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setHostConfig:" %}{% endlanying_code_snippet %}
```
### setLoadAllServerConversations

`- (void)setLoadAllServerConversations`

<a name="//api/name/setLoadAllServerConversations:" title="setLoadAllServerConversations:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setLoadAllServerConversations" %}{% endlanying_code_snippet %}
```
### setLoadAllServerConversations:

Set whether to generate conversation list from server

`- (void)setLoadAllServerConversations:(BOOL)*enable*`

#### Parameters

*enable*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setLogLevel:" title="setLogLevel:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setLoadAllServerConversations:" %}{% endlanying_code_snippet %}
```
### setLogLevel:

Set log level

`- (void)setLogLevel:(BMXLogLevel)*arg1*`

#### Parameters

*BMXLogLevel*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushCertName:" title="setPushCertName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setLogLevel:" %}{% endlanying_code_snippet %}
```
### setPushCertName:

Set the push certificate name

`- (void)setPushCertName:(NSString *)*arg1*`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushProviderType:" title="setPushProviderType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setPushCertName:" %}{% endlanying_code_snippet %}
```
### setPushProviderType:

Set push service provider type

`- (void)setPushProviderType:(BMXPushProviderType)*type*`

#### Parameters

*type*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setUserDNSAddress:" title="setUserDNSAddress:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setPushProviderType:" %}{% endlanying_code_snippet %}
```
### setUserDNSAddress:

Set custom DNS address

`- (void)setUserDNSAddress:(NSString *)*dns*`

#### Parameters

*dns*  
    DNS server address

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setVerifyCertificate" title="setVerifyCertificate"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setUserDNSAddress:" %}{% endlanying_code_snippet %}
```
### setVerifyCertificate

`- (void)setVerifyCertificate`

<a name="//api/name/setVerifyCertificate:" title="setVerifyCertificate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setVerifyCertificate" %}{% endlanying_code_snippet %}
```
### setVerifyCertificate:

Set whether to verify HTTP certificate

`- (void)setVerifyCertificate:(BOOL)*verify*`

#### Parameters

*verify*  
    true to verify

#### Discussion
Set whether to verify HTTP certificate

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfig",function="setVerifyCertificate:" %}{% endlanying_code_snippet %}
```
