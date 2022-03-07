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

Change the appId of SDK, which also update the appId in BMXConfig.

`- (void)changeAppID:(NSString *)*appID* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*appID*  
   Newly changed appId  

#### Discussion
Change the appId of SDK, which also update the appId in BMXConfig.

#### Declared In
* `BMXClient.h`

<a name="//api/name/connectStatus" title="connectStatus"></a>
### connectStatus

Get the current connection state with server

`- (BMXConnectStatus)connectStatus`

#### Discussion
Get the current connection state with server

#### Declared In
* `BMXClient.h`

<a name="//api/name/disConnect" title="disConnect"></a>
### disConnect

Disconnect

`- (void)disConnect`

#### Discussion
Disconnect

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInById:password:completion:" title="fastSignInById:password:completion:"></a>
### fastSignInById:password:completion:

Login automatically by user ID (a successful login before required, faster)

`- (void)fastSignInById:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login automatically by user ID (a successful login before required, faster)

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInByName:password:completion:" title="fastSignInByName:password:completion:"></a>
### fastSignInByName:password:completion:

Login automatically by username (a successful login before required, faster)

`- (void)fastSignInByName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login automatically by username (a successful login before required, faster)

#### Declared In
* `BMXClient.h`

<a name="//api/name/initializeServerConfig:" title="initializeServerConfig:"></a>
### initializeServerConfig:

Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.

`- (void)initializeServerConfig:(BOOL)*isLocal*`

#### Parameters

*isLocal*  
   True to use locally cached DNS configuration, false to get the latest configuration from server.  

#### Discussion
Get the server network configuration of app, which can be called after initializing SDK and before logging in, so as to get the server configuration in advance and speed up logging in.

#### Declared In
* `BMXClient.h`

<a name="//api/name/networkDidChangedType:reconnect:" title="networkDidChangedType:reconnect:"></a>
### networkDidChangedType:reconnect:

Process network changes in messaging

`- (void)networkDidChangedType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

*type*  
   Changed network type  

*reconnect*  
   Network needs to reconnect or not  

#### Discussion
Process network changes in messaging

#### Declared In
* `BMXClient.h`

<a name="//api/name/reconnect" title="reconnect"></a>
### reconnect

Force reconnection

`- (void)reconnect`

#### Discussion
Force reconnection

#### Declared In
* `BMXClient.h`

<a name="//api/name/registerWithSDKConfig:" title="registerWithSDKConfig:"></a>
### registerWithSDKConfig:

`- (void)registerWithSDKConfig:(BMXSDKConfig *)*config*`

<a name="//api/name/signInById:password:completion:" title="signInById:password:completion:"></a>
### signInById:password:completion:

Login by user ID

`- (void)signInById:(long long)*userId* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by user ID

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInById:withToken:completion:" title="signInById:withToken:completion:"></a>
### signInById:withToken:completion:

Login by user ID and token

`- (void)signInById:(long long)*userId* withToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by user ID and token

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInByName:password:completion:" title="signInByName:password:completion:"></a>
### signInByName:password:completion:

Login by username

`- (void)signInByName:(NSString *)*userName* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by username

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInStatus" title="signInStatus"></a>
### signInStatus

Get the current login state

`- (BMXSignInStatus)signInStatus`

#### Discussion
Get the current login state

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutID:ignoreUnbindDevice:completion:" title="signOutID:ignoreUnbindDevice:completion:"></a>
### signOutID:ignoreUnbindDevice:completion:

Log out

`- (void)signOutID:(NSInteger)*userID* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Log out

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutignoreUnbindDevice:completion:" title="signOutignoreUnbindDevice:completion:"></a>
### signOutignoreUnbindDevice:completion:

`- (void)signOutignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

<a name="//api/name/signUpNewUser:password:completion:" title="signUpNewUser:password:completion:"></a>
### signUpNewUser:password:completion:

To register a new user, username and password are required

`- (void)signUpNewUser:(NSString *)*userName* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *error ))*aCompletionBlock*`

#### Parameters

*userName*  
   Username  

*password*  
   Password  

*aCompletionBlock*  
   After successful registration, get the profile of the newly registered user from this function, and initially passed in a pointing-to-empty shared_ptr object.  

#### Discussion
To register a new user, username and password are required

#### Declared In
* `BMXClient.h`

