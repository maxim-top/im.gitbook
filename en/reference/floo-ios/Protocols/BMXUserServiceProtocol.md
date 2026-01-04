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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="connectStatusDidChanged:" %}{% endlanying_code_snippet %}
```
### userInfoDidUpdated:

User information updated

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userOtherDeviceDidSignIn:" title="userOtherDeviceDidSignIn:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userInfoDidUpdated:" %}{% endlanying_code_snippet %}
```
### userOtherDeviceDidSignIn:

User signed in the other device

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userOtherDeviceDidSignOut:" title="userOtherDeviceDidSignOut:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userOtherDeviceDidSignIn:" %}{% endlanying_code_snippet %}
```
### userOtherDeviceDidSignOut:

User signed out the other device

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userSignIn:" title="userSignIn:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userOtherDeviceDidSignOut:" %}{% endlanying_code_snippet %}
```
### userSignIn:

User signed in

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

*userProflie*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userSignOut:userId:" title="userSignOut:userId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userSignIn:" %}{% endlanying_code_snippet %}
```
### userSignOut:userId:

User signed out

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

*error*  

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userSignOut:userId:" %}{% endlanying_code_snippet %}
```
