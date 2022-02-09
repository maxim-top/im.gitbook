# BMXUserServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXUserServiceProtocol.h  

## Instance Methods

<a name="//api/name/connectStatusDidChanged:" title="connectStatusDidChanged:"></a>
### connectStatusDidChanged:

Channel state changed

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

*status*  
   Network status  

#### Discussion
Channel state changed

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userInfoDidUpdated:" title="userInfoDidUpdated:"></a>
### userInfoDidUpdated:

Synchronize user information updates (when user information changes in other devices)

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion
Synchronize user information updates (when user information changes in other devices)

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignIn:" title="userOtherDeviceDidSignIn:"></a>
### userOtherDeviceDidSignIn:

User login on another device

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion
User login on another device

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignOut:" title="userOtherDeviceDidSignOut:"></a>
### userOtherDeviceDidSignOut:

User logout on another device

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion
User logout on another device

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignIn:" title="userSignIn:"></a>
### userSignIn:

User login

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

*userProflie*  
   User information  

#### Discussion
User login

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignOut:userId:" title="userSignOut:userId:"></a>
### userSignOut:userId:

User logout

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

*error*  
   Error code  

#### Discussion
User logout

#### Declared In
* `BMXUserServiceProtocol.h`

