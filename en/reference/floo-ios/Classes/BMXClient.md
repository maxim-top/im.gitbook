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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="getCacheDir" %}{% endlanying_code_snippet %}
```
### sharedClient

`+ (instancetype)sharedClient`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/changeAppID:completion:" title="changeAppID:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="sharedClient" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="changeAppID:completion:" %}{% endlanying_code_snippet %}
```
### connectStatus

Get the current connection state with server

`- (BMXConnectStatus)connectStatus`

#### Discussion
Get the current connection state with server

#### Declared In
* `BMXClient.h`

<a name="//api/name/disConnect" title="disConnect"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="connectStatus" %}{% endlanying_code_snippet %}
```
### disConnect

Disconnect

`- (void)disConnect`

#### Discussion
Disconnect

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInById:password:completion:" title="fastSignInById:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="disConnect" %}{% endlanying_code_snippet %}
```
### fastSignInById:password:completion:

Login automatically by user ID (a successful login before required, faster)

`- (void)fastSignInById:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login automatically by user ID (a successful login before required, faster)

#### Declared In
* `BMXClient.h`

<a name="//api/name/fastSignInByName:password:completion:" title="fastSignInByName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInById:password:completion:" %}{% endlanying_code_snippet %}
```
### fastSignInByName:password:completion:

Login automatically by username (a successful login before required, faster)

`- (void)fastSignInByName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login automatically by username (a successful login before required, faster)

#### Declared In
* `BMXClient.h`

<a name="//api/name/initializeServerConfig:" title="initializeServerConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInByName:password:completion:" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="initializeServerConfig:" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="networkDidChangedType:reconnect:" %}{% endlanying_code_snippet %}
```
### reconnect

Force reconnection

`- (void)reconnect`

#### Discussion
Force reconnection

#### Declared In
* `BMXClient.h`

<a name="//api/name/registerWithSDKConfig:" title="registerWithSDKConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="reconnect" %}{% endlanying_code_snippet %}
```
### registerWithSDKConfig:

`- (void)registerWithSDKConfig:(BMXSDKConfig *)*config*`

<a name="//api/name/signInById:password:completion:" title="signInById:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="registerWithSDKConfig:" %}{% endlanying_code_snippet %}
```
### signInById:password:completion:

Login by user ID

`- (void)signInById:(long long)*userId* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by user ID

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInById:withToken:completion:" title="signInById:withToken:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInById:password:completion:" %}{% endlanying_code_snippet %}
```
### signInById:withToken:completion:

Login by user ID and token

`- (void)signInById:(long long)*userId* withToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by user ID and token

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInByName:password:completion:" title="signInByName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInById:withToken:completion:" %}{% endlanying_code_snippet %}
```
### signInByName:password:completion:

Login by username

`- (void)signInByName:(NSString *)*userName* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Login by username

#### Declared In
* `BMXClient.h`

<a name="//api/name/signInStatus" title="signInStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInByName:password:completion:" %}{% endlanying_code_snippet %}
```
### signInStatus

Get the current login state

`- (BMXSignInStatus)signInStatus`

#### Discussion
Get the current login state

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutID:ignoreUnbindDevice:completion:" title="signOutID:ignoreUnbindDevice:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInStatus" %}{% endlanying_code_snippet %}
```
### signOutID:ignoreUnbindDevice:completion:

Log out

`- (void)signOutID:(NSInteger)*userID* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Log out

#### Declared In
* `BMXClient.h`

<a name="//api/name/signOutignoreUnbindDevice:completion:" title="signOutignoreUnbindDevice:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutID:ignoreUnbindDevice:completion:" %}{% endlanying_code_snippet %}
```
### signOutignoreUnbindDevice:completion:

`- (void)signOutignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

<a name="//api/name/signUpNewUser:password:completion:" title="signUpNewUser:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutignoreUnbindDevice:completion:" %}{% endlanying_code_snippet %}
```
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

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signUpNewUser:password:completion:" %}{% endlanying_code_snippet %}
```
