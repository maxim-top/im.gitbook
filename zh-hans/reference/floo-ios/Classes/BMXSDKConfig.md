# BMXSDKConfig Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface SDK设置管理

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### carryUsernameInMessage

发送消息的config中是否携带

`- (BOOL)carryUsernameInMessage`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### enableDeliveryAck

是否发送消息送达回执

`- (BOOL)enableDeliveryAck`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getAppID

获取用户的appID。

`- (NSString *)getAppID`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getAppSecret

获取用户的appSecret。

`- (NSString *)getAppSecret`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getCacheDir

获取缓存数据存储路径，比如用户头像

`- (NSString *)getCacheDir`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getClientType

客户端类型

`- (BMXClientType)getClientType`

#### Return Value

[BMXClientType](../Constants/BMXClientType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getConsoleOutput

Log是否输出到Console

`- (BOOL)getConsoleOutput`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getDBCryptoKey

获取设备的本地数据库加密密钥。

`- (NSString *)getDBCryptoKey`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getDataDir

获取聊天数据存储路径，包含消息、附件等

`- (NSString *)getDataDir`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getDebugLogReceiverId

获取调试log接收着账号(仅用于SDK调试，接收客户端log日志使用)

`- (long long)getDebugLogReceiverId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getDeviceUuid

获取设备的唯一识别码

`- (NSString *)getDeviceUuid`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getEnableDNS

获取是否启用dns功能。

`- (BOOL)getEnableDNS`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getHostConfig

获取服务器配置

`- (BMXSDKConfigHostConfig *)getHostConfig`

#### Return Value

[BMXSDKConfigHostConfig](BMXSDKConfigHostConfig.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getLoadAllServerConversations

是否根据服务器返回未读列表创建所有会话.

`- (BOOL)getLoadAllServerConversations`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getLogLevel

Log输出等级

`- (BMXLogLevel)getLogLevel`

#### Return Value

[BMXLogLevel](../Constants/BMXLogLevel.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getPushCertName

获取Push证书名字

`- (NSString *)getPushCertName`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getPushEnvironmentType

获取用户的推送环境类型。

`- (BMXPushEnvironmentType)getPushEnvironmentType`

#### Return Value

[BMXPushEnvironmentType](../Constants/BMXPushEnvironmentType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getPushProviderType

获取用户的推送提供商类型。

`- (BMXPushProviderType)getPushProviderType`

#### Return Value

[BMXPushProviderType](../Constants/BMXPushProviderType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getSDKVersion

SDK版本

`- (NSString *)getSDKVersion`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getUserAgent

获取用户代理信息

`- (NSString *)getUserAgent`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getUserDNSAddress

获取用户自定义dns服务器地址。

`- (NSString *)getUserDNSAddress`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getVerifyCertificate

获取https请求是否验证服务器端证书。

`- (BOOL)getVerifyCertificate`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### getVsn

客户端OS版本

`- (NSString *)getVsn`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* appId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:appId:appSecret:deliveryAck:

构造函数

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* appId:(NSString *)*appId* appSecret:(NSString *)*appSecret* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

_type_\
客户端类型

_vsn_\
客户端OS版本

_dataDir_\
聊天数据存储路径

_cacheDir_\
缓存数据存储路径

_SDKVersion_\
SDK版本

_pushCertName_\
Push证书名字

_userAgent_\
用户代理信息

_appId_\
用户的appId

_appSecret_\
用户的appSecret（对于使用推送的用户，必须同时设置appId和appSecret）

_deliveryAck_\
是否发送消息送达回执

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:

构造函数

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

_type_\
客户端类型

_vsn_\
客户端OS版本

_dataDir_\
聊天数据存储路径

_cacheDir_\
缓存数据存储路径

_SDKVersion_\
SDK版本

_pushCertName_\
Push证书名字

_userAgent_\
用户代理信息

_deliveryAck_\
是否发送消息送达回执

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setAppID:

设置用户的appID。

`- (void)setAppID:(NSString *)*appID*`

#### Parameters

_appID_\
用户的appID

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setAppSecret:

设置用户的appSecret。

`- (void)setAppSecret:(NSString *)*appSecret*`

#### Parameters

_appID_\
用户的appSecret

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setCarryUsernameInMessage:

设置发送消息的config中是否携带用户名

`- (void)setCarryUsernameInMessage:(BOOL)*arg1*`

#### Parameters

_bool_\
设置是否在送消息的config中携带用户名

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setConsoleOutput:

设置Log是否输出到Console

`- (void)setConsoleOutput:(BOOL)*arg1*`

#### Parameters

_bool_\
设置Log是否输出到Console

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDBCryptoKey:

设置本地数据库的加密密钥，在app卸载之前应该始终保持一直，app删除后再次安装时可以产生不同的密钥。用于本地数据库加密。

`- (void)setDBCryptoKey:(NSString *)*cryptoKey*`

#### Parameters

_cryptoKey_\
本地数据库的加密密钥。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDebugLogReceiverId:

设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)

`- (void)setDebugLogReceiverId:(long long)*uid*`

#### Parameters

_uid_\
调试log接收者id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDeviceUuid:

设置设备的唯一识别码，在app卸载之前应该始终保持一致，app删除后再次安装时可以产生不同的设备识别码。

`- (void)setDeviceUuid:(NSString *)*uuid*`

#### Parameters

_uuid_\
设备的唯一识别码。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnableDNS

`- (void)setEnableDNS`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnableDNS:

设置是否启用dns功能，默认是开启的。

`- (void)setEnableDNS:(BOOL)*enable*`

#### Parameters

_enable_\
是否启用dns功能

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnableDeliveryAck:

设置是否发送消息送达回执

`- (void)setEnableDeliveryAck:(BOOL)*arg1*`

#### Parameters

_bool_\
是否发送消息送达回执

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnvironmentType:

设置用户的推送环境类型。

`- (void)setEnvironmentType:(BMXPushEnvironmentType)*type*`

#### Parameters

_type_\
用户的推送环境类型

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setHostConfig:

设置服务器配置

`- (void)setHostConfig:(BMXSDKConfigHostConfig *)*config*`

#### Parameters

_config_\
服务器配置

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setLoadAllServerConversations

`- (void)setLoadAllServerConversations`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setLoadAllServerConversations:

是否根据服务器返回未读列表创建所有会话，默认为false，只会创建有未读消息的会话。

`- (void)setLoadAllServerConversations:(BOOL)*enable*`

#### Parameters

_enable_\
是否根据服务器返回未读列表创建所有会话

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setLogLevel:

设置Log输出等级

`- (void)setLogLevel:(BMXLogLevel)*arg1*`

#### Parameters

_BMXLogLevel_\
Log输出等级

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setPushCertName:

设置Push证书名字

`- (void)setPushCertName:(NSString *)*arg1*`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setPushProviderType:

设置用户的推送提供商类型。

`- (void)setPushProviderType:(BMXPushProviderType)*type*`

#### Parameters

_type_\
用户的推送提供商类型

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setUserDNSAddress:

设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。

`- (void)setUserDNSAddress:(NSString *)*dns*`

#### Parameters

_dns_\
用户自定义dns服务器地址

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setVerifyCertificate

`- (void)setVerifyCertificate`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setVerifyCertificate:

设置https请求是否验证服务器端证书。

`- (void)setVerifyCertificate:(BOOL)*verify*`

#### Parameters

_verify_\
https请求是否验证服务器端证书

#### Discussion

设置https请求是否验证服务器端证书。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>
```
