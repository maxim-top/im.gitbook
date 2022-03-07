# BMXClient Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXClient.h  

## Properties

<a name="//api/name/chatService" title="chatService"></a>
### chatService

`@property (nonatomic, strong, readonly) id<BMXChatManager> chatService`

<a name="//api/name/groupService" title="groupService"></a>
### groupService

`@property (nonatomic, strong, readonly) id<BMXGroupManager> groupService`

<a name="//api/name/pushService" title="pushService"></a>
### pushService

`@property (nonatomic, strong, readonly) id<BMXPushManager> pushService`

<a name="//api/name/rosterService" title="rosterService"></a>
### rosterService

`@property (nonatomic, strong, readonly) id<BMXRosterManager> rosterService`

<a name="//api/name/sdkConfig" title="sdkConfig"></a>
### sdkConfig

`@property (nonatomic, strong) BMXSDKConfig *sdkConfig`

<a name="//api/name/userService" title="userService"></a>
### userService

`@property (nonatomic, strong, readonly) id<BMXUserManager> userService`

<a title="Class Methods" name="class_methods"></a>
## Class Methods

<a name="//api/name/getCacheDir" title="getCacheDir"></a>
### getCacheDir

`+ (NSString *)getCacheDir`

<a name="//api/name/sharedClient" title="sharedClient"></a>
### sharedClient

`+ (instancetype)sharedClient`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/changeAppID:completion:" title="changeAppID:completion:"></a>
### changeAppID:completion:

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

`- (void)changeAppID:(NSString *)*appID* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*appID*  
   新变更的appId  

#### Discussion
更改SDK的appId，本操作会同时更新BMXConfig中的appId。

#### Declared In
* `BMXClient.h`

<a name="//api/name/connectStatus" title="connectStatus"></a>
### connectStatus

获取当前和服务器的连接状态

`- (BMXConnectStatus)connectStatus`

#### Discussion
获取当前和服务器的连接状态

#### Declared In
* `BMXClient.h`

<a name="//api/name/disConnect" title="disConnect"></a>
### disConnect

断开网络连接

`- (void)disConnect`

#### Discussion
断开网络连接

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInById:password:completion:" title="fastSignInById:password:completion:"></a>
### fastSignInById:password:completion:

通过用户ID自动登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInById:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
通过用户ID自动登录（要求之前成功登录过，登录速度较快）

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInByName:password:completion:" title="fastSignInByName:password:completion:"></a>
### fastSignInByName:password:completion:

通过用户名自动登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInByName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
通过用户名自动登录（要求之前成功登录过，登录速度较快）

#### Declared In
* `BMXClient.h`

<a name="//api/name/initializeServerConfig:" title="initializeServerConfig:"></a>
### initializeServerConfig:

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

`- (void)initializeServerConfig:(BOOL)*isLocal*`

#### Parameters

*isLocal*  
   为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。  

#### Discussion
获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

#### Declared In
* `BMXClient.h`

<a name="//api/name/networkDidChangedType:reconnect:" title="networkDidChangedType:reconnect:"></a>
### networkDidChangedType:reconnect:

处理网络状态发送变化

`- (void)networkDidChangedType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

*type*  
   变化后的网络类型  

*reconnect*  
   网络是否需要重连  

#### Discussion
处理网络状态发送变化

#### Declared In
* `BMXClient.h`

<a name="//api/name/reconnect" title="reconnect"></a>
### reconnect

强制重新连接

`- (void)reconnect`

#### Discussion
强制重新连接

#### Declared In
* `BMXClient.h`

<a name="//api/name/registerWithSDKConfig:" title="registerWithSDKConfig:"></a>
### registerWithSDKConfig:

`- (void)registerWithSDKConfig:(BMXSDKConfig *)*config*`

<a name="//api/name/signInById:password:completion:" title="signInById:password:completion:"></a>
### signInById:password:completion:

通过用户ID登录

`- (void)signInById:(long long)*userId* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
通过用户ID登录

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInById:withToken:completion:" title="signInById:withToken:completion:"></a>
### signInById:withToken:completion:

通过用户ID和token登录

`- (void)signInById:(long long)*userId* withToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
通过用户ID和token登录

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInByName:password:completion:" title="signInByName:password:completion:"></a>
### signInByName:password:completion:

通过用户名登录

`- (void)signInByName:(NSString *)*userName* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
通过用户名登录

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInStatus" title="signInStatus"></a>
### signInStatus

获取当前的登录状态

`- (BMXSignInStatus)signInStatus`

#### Discussion
获取当前的登录状态

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutID:ignoreUnbindDevice:completion:" title="signOutID:ignoreUnbindDevice:completion:"></a>
### signOutID:ignoreUnbindDevice:completion:

退出登录

`- (void)signOutID:(NSInteger)*userID* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
退出登录

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutignoreUnbindDevice:completion:" title="signOutignoreUnbindDevice:completion:"></a>
### signOutignoreUnbindDevice:completion:

`- (void)signOutignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

<a name="//api/name/signUpNewUser:password:completion:" title="signUpNewUser:password:completion:"></a>
### signUpNewUser:password:completion:

注册新用户，username和password是必填参数

`- (void)signUpNewUser:(NSString *)*userName* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *error ))*aCompletionBlock*`

#### Parameters

*userName*  
   用户名  

*password*  
   密码  

*aCompletionBlock*  
   注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared_ptr对象即可。  

#### Discussion
注册新用户，username和password是必填参数

#### Declared In
* `BMXClient.h`

