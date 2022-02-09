# BMXUserServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXUserServiceProtocol.h  

## Instance Methods

<a name="//api/name/connectStatusDidChanged:" title="connectStatusDidChanged:"></a>
### connectStatusDidChanged:

链接状态发生变化

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

*status*  
   网络状态  

#### Discussion
链接状态发生变化

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userInfoDidUpdated:" title="userInfoDidUpdated:"></a>
### userInfoDidUpdated:

同步用户信息更新（其他设备操作发生用户信息变更）

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion
同步用户信息更新（其他设备操作发生用户信息变更）

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignIn:" title="userOtherDeviceDidSignIn:"></a>
### userOtherDeviceDidSignIn:

用户在其他设备上登陆

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion
用户在其他设备上登陆

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignOut:" title="userOtherDeviceDidSignOut:"></a>
### userOtherDeviceDidSignOut:

用户在其他设备上登出

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion
用户在其他设备上登出

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignIn:" title="userSignIn:"></a>
### userSignIn:

用户登陆

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

*userProflie*  
   用户信息  

#### Discussion
用户登陆

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignOut:userId:" title="userSignOut:userId:"></a>
### userSignOut:userId:

用户登出

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

*error*  
   错误码  

#### Discussion
用户登出

#### Declared In
* `BMXUserServiceProtocol.h`

