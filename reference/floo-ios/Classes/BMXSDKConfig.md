# BMXSDKConfig Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXSDKConfig.h  

## Properties

<a name="//api/name/appID" title="appID"></a>
### appID

获取用户的appId, 设置用户的appId。

`@property (nonatomic, copy) NSString *appID`

#### Discussion
获取用户的appId, 设置用户的appId。

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/appSecret" title="appSecret"></a>
### appSecret

`@property (nonatomic, strong) NSString *appSecret`

<a name="//api/name/cacheDir" title="cacheDir"></a>
### cacheDir

`@property (nonatomic, copy, readonly) NSString *cacheDir`

<a name="//api/name/carryUsernameInMessage" title="carryUsernameInMessage"></a>
### carryUsernameInMessage

获取和设置是否在消息config字段里携带username功能（方便在未获取到对方user info时展示其用户名），默认是关闭的。

`@property (nonatomic, assign) BOOL carryUsernameInMessage`

#### Discussion
获取和设置是否在消息config字段里携带username功能（方便在未获取到对方user info时展示其用户名），默认是关闭的。

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/consoleOutput" title="consoleOutput"></a>
### consoleOutput

`@property (nonatomic, assign) BOOL consoleOutput`

<a name="//api/name/dataDir" title="dataDir"></a>
### dataDir

`@property (nonatomic, copy, readonly) NSString *dataDir`

<a name="//api/name/debugLogRecevierID" title="debugLogRecevierID"></a>
### debugLogRecevierID

设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)

`@property (nonatomic, copy) NSString *debugLogRecevierID`

#### Discussion
设置调试log接收账号(仅用于SDK调试，接收客户端log日志使用)

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/deviceUUID" title="deviceUUID"></a>
### deviceUUID

获取设备的唯一识别码,如果使用数据库

`@property (nonatomic, copy) NSString *deviceUUID`

#### Discussion
获取设备的唯一识别码,如果使用数据库

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/enableDNS" title="enableDNS"></a>
### enableDNS

获取是否启用dns功能,设置是否启用dns功能，默认是开启的。

`@property (nonatomic, assign) BOOL enableDNS`

#### Discussion
获取是否启用dns功能,设置是否启用dns功能，默认是开启的。

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/enableDeliveryAck" title="enableDeliveryAck"></a>
### enableDeliveryAck

`@property (nonatomic, assign) BOOL enableDeliveryAck`

<a name="//api/name/hostConfig" title="hostConfig"></a>
### hostConfig

`@property (nonatomic, strong) BMXHostConfig *hostConfig`

<a name="//api/name/loadAllServerConversations" title="loadAllServerConversations"></a>
### loadAllServerConversations

`@property (nonatomic, assign) BOOL loadAllServerConversations`

<a name="//api/name/logoLevelType" title="logoLevelType"></a>
### logoLevelType

`@property (nonatomic, assign, readonly) BMXLogLevel logoLevelType`

<a name="//api/name/pushCertName" title="pushCertName"></a>
### pushCertName

`@property (nonatomic, copy) NSString *pushCertName`

<a name="//api/name/sdkVersion" title="sdkVersion"></a>
### sdkVersion

`@property (nonatomic, copy, readonly) NSString *sdkVersion`

<a name="//api/name/userAgent" title="userAgent"></a>
### userAgent

`@property (nonatomic, copy, readonly) NSString *userAgent`

<a name="//api/name/userDNSAddress" title="userDNSAddress"></a>
### userDNSAddress

获取用户自定义dns服务器地址,设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。

`@property (nonatomic, copy) NSString *userDNSAddress`

#### Discussion
获取用户自定义dns服务器地址,设置用户自定义dns服务器地址，在用户设置了dns服务器的情况下优先使用用户dns。

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/verifyCertificate" title="verifyCertificate"></a>
### verifyCertificate

`@property (nonatomic, assign) BOOL verifyCertificate`

<a name="//api/name/vsn" title="vsn"></a>
### vsn

`@property (nonatomic, copy, readonly) NSString *vsn`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initConfigWithDataDir:cacheDir:pushCertName:userAgent:" title="initConfigWithDataDir:cacheDir:pushCertName:userAgent:"></a>
### initConfigWithDataDir:cacheDir:pushCertName:userAgent:

`- (instancetype)initConfigWithDataDir:(NSString *)*dataDir* cacheDir:(NSString *)*cacheDir* pushCertName:(NSString *)*pushCertName* userAgent:(NSString *)*userAgent*`

