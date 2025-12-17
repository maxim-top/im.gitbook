# BMXSDKConfig Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface SDK config

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### carryUsernameInMessage

Whether to carry the username in the message

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

Whether to enable the delivery ACK

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

Get the app ID

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

Get app secret

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

Get cache files directory

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

Get client device type

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

Get the switch of whether to output the log to console

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

Get crypto key of local db

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

Get data files directory

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

Get debug log files receiver ID

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

Get device UUID

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

Get whether to enable DNS on ratel

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

Get server hosts information

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

Whether to generate conversation list from server

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

Get log level

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

Get the push certificate name

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

Get push environment type(Development|Product)

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

Get push service provider type

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

Get SDK version

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

Get user agent

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

Get custom DNS address

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

Get whether to verify HTTP certificate

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

Ge app client version

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

Constructor

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* appId:(NSString *)*appId* appSecret:(NSString *)*appSecret* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

_type_\
Client type

_vsn_\
App client version

_dataDir_\
Data files directory

_cacheDir_\
Cache files directory

_SDKVersion_\
SDK version

_pushCertName_\
Push certificate name

_userAgent_\
User agent

_appId_\
App ID

_appSecret_\
App secret

_deliveryAck_\
Delivery ACK

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### initWithType:vsn:dataDir:cacheDir:sDKVersion:pushCertName:userAgent:deliveryAck:

Constructor

`- (id)initWithType:(BMXClientType)*type* vsn:(NSString *)*vsn* dataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* sDKVersion:(NSString *)*SDKVersion* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent* deliveryAck:(BOOL)*deliveryAck*`

#### Parameters

_type_\
Client type

_vsn_\
App client version

_dataDir_\
Data files directory

_cacheDir_\
Cache files directory

_SDKVersion_\
SDK version

_pushCertName_\
Push certificate name

_userAgent_\
User agent

_deliveryAck_\
Delivery ACK

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setAppID:

Set app ID

`- (void)setAppID:(NSString *)*appID*`

#### Parameters

_appID_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setAppSecret:

Set app secret

`- (void)setAppSecret:(NSString *)*appSecret*`

#### Parameters

_appSecret_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setCarryUsernameInMessage:

Set whether to carry the username in the message

`- (void)setCarryUsernameInMessage:(BOOL)*arg1*`

#### Parameters

_bool_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setConsoleOutput:

Set the switch of whether to output the log to console

`- (void)setConsoleOutput:(BOOL)*arg1*`

#### Parameters

_bool_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDBCryptoKey:

Set crypto key of local db

`- (void)setDBCryptoKey:(NSString *)*cryptoKey*`

#### Parameters

_cryptoKey_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDebugLogReceiverId:

Set debug log files receiver ID

`- (void)setDebugLogReceiverId:(long long)*uid*`

#### Parameters

_uid_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setDeviceUuid:

Set device UUID

`- (void)setDeviceUuid:(NSString *)*uuid*`

#### Parameters

_uuid_

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

Set whether to enable the delivery ACK

`- (void)setEnableDNS:(BOOL)*enable*`

#### Parameters

_enable_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnableDeliveryAck:

Enable delivery ACK

`- (void)setEnableDeliveryAck:(BOOL)*arg1*`

#### Parameters

_bool_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setEnvironmentType:

Set push environment type(Development|Product)

`- (void)setEnvironmentType:(BMXPushEnvironmentType)*type*`

#### Parameters

_type_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setHostConfig:

Set server hosts config

`- (void)setHostConfig:(BMXSDKConfigHostConfig *)*config*`

#### Parameters

_config_

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

Set whether to generate conversation list from server

`- (void)setLoadAllServerConversations:(BOOL)*enable*`

#### Parameters

_enable_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setLogLevel:

Set log level

`- (void)setLogLevel:(BMXLogLevel)*arg1*`

#### Parameters

_BMXLogLevel_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setPushCertName:

Set the push certificate name

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

Set push service provider type

`- (void)setPushProviderType:(BMXPushProviderType)*type*`

#### Parameters

_type_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>

```

### setUserDNSAddress:

Set custom DNS address

`- (void)setUserDNSAddress:(NSString *)*dns*`

#### Parameters

_dns_\
DNS server address

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

Set whether to verify HTTP certificate

`- (void)setVerifyCertificate:(BOOL)*verify*`

#### Parameters

_verify_\
true to verify

#### Discussion

Set whether to verify HTTP certificate

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXSDKConfig'></div>
```
