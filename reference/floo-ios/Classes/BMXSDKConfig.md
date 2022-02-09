# BMXSDKConfig Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXSDKConfig.h  

## Properties

<a name="//api/name/appID" title="appID"></a>
### appID

Get user's appId, set user's appId.

`@property (nonatomic, copy) NSString *appID`

#### Discussion
Get user's appId, set user's appId.

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

Get and set whether to carry the username function in the message config field (which is convenient to display the opposite username when the user info is not obtained), default off.

`@property (nonatomic, assign) BOOL carryUsernameInMessage`

#### Discussion
Get and set whether to carry the username function in the message config field (which is convenient to display the opposite username when the user info is not obtained), default off.

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

Set debug log receiving account (for SDK debugging only, used for receiving client log)

`@property (nonatomic, copy) NSString *debugLogRecevierID`

#### Discussion
Set debug log receiving account (for SDK debugging only, used for receiving client log)

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/deviceUUID" title="deviceUUID"></a>
### deviceUUID

Get the unique identifier of device, is using a database

`@property (nonatomic, copy) NSString *deviceUUID`

#### Discussion
Get the unique identifier of device, is using a database

#### Declared In
* `BMXSDKConfig.h`

<a name="//api/name/enableDNS" title="enableDNS"></a>
### enableDNS

Get whether dns function enabled, set whether to enable dns function, default enabled.

`@property (nonatomic, assign) BOOL enableDNS`

#### Discussion
Get whether dns function enabled, set whether to enable dns function, default enabled.

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

Get user-defined dns server address, set user-defined server address, use the user-defined dns first when the dns server set.

`@property (nonatomic, copy) NSString *userDNSAddress`

#### Discussion
Get user-defined dns server address, set user-defined server address, use the user-defined dns first when the dns server set.

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

