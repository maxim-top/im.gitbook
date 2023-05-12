# BMXUserServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol User service listener

## Instance Methods

<a name="//api/name/connectStatusDidChanged:" title="connectStatusDidChanged:"></a>
### connectStatusDidChanged:

Connection status changed

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

*status*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userInfoDidUpdated:" title="userInfoDidUpdated:"></a>
### userInfoDidUpdated:

User information updated

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userOtherDeviceDidSignIn:" title="userOtherDeviceDidSignIn:"></a>
### userOtherDeviceDidSignIn:

User signed in the other device

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userOtherDeviceDidSignOut:" title="userOtherDeviceDidSignOut:"></a>
### userOtherDeviceDidSignOut:

User signed out the other device

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userSignIn:" title="userSignIn:"></a>
### userSignIn:

User signed in

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

*userProflie*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userSignOut:userId:" title="userSignOut:userId:"></a>
### userSignOut:userId:

User signed out

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

*error*  

#### Declared In
* `floo_proxy.h`

