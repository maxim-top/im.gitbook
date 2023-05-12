# BMXUserProfile Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface User Profile

## Instance Methods

<a name="//api/name/addFriendAuthMode" title="addFriendAuthMode"></a>
### addFriendAuthMode

Friend authorization mode

`- (BMXUserProfile_AddFriendAuthMode)addFriendAuthMode`

#### Return Value
<a href="../Constants/BMXUserProfile_AddFriendAuthMode.md">BMXUserProfile_AddFriendAuthMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/authQuestion" title="authQuestion"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### authQuestion

Authorization question

`- (BMXUserProfileAuthQuestion *)authQuestion`

#### Return Value
AuthQuestion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="authQuestion" %}{% endlanying_code_snippet %}
```
### avatarPath

Local path of my avatar

`- (NSString *)avatarPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarRatelUrl" title="avatarRatelUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarPath" %}{% endlanying_code_snippet %}
```
### avatarRatelUrl

The avatar file URL on REST server

`- (NSString *)avatarRatelUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailPath" title="avatarThumbnailPath"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### avatarThumbnailPath

The avatar thumbnail file URL on HTTP server

`- (NSString *)avatarThumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### avatarUrl

The avatar file URL on HTTP server

`- (NSString *)avatarUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/category" title="category"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### category

User grade(Normal|Advanced)

`- (BMXUserProfile_UserCategory)category`

#### Return Value
<a href="../Constants/BMXUserProfile_UserCategory.md">BMXUserProfile_UserCategory</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="category" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/email" title="email"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### email

Email

`- (NSString *)email`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isAutoAcceptGroupInvite" title="isAutoAcceptGroupInvite"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="email" %}{% endlanying_code_snippet %}
```
### isAutoAcceptGroupInvite

Whether to accept group invitation automatically

`- (BOOL)isAutoAcceptGroupInvite`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageSetting" title="messageSetting"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isAutoAcceptGroupInvite" %}{% endlanying_code_snippet %}
```
### messageSetting

Message settings

`- (BMXUserProfileMessageSetting *)messageSetting`

#### Return Value
<a href="../Classes/BMXUserProfileMessageSetting.md">BMXUserProfileMessageSetting</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/mobilePhone" title="mobilePhone"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="messageSetting" %}{% endlanying_code_snippet %}
```
### mobilePhone

User phone number

`- (NSString *)mobilePhone`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/nickname" title="nickname"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="mobilePhone" %}{% endlanying_code_snippet %}
```
### nickname

User nickname

`- (NSString *)nickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/privateInfo" title="privateInfo"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="nickname" %}{% endlanying_code_snippet %}
```
### privateInfo

Extension information for user(Not visible to friends)

`- (NSString *)privateInfo`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/publicInfo" title="publicInfo"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="privateInfo" %}{% endlanying_code_snippet %}
```
### publicInfo

Extension information for user(Visible to friends)

`- (NSString *)publicInfo`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userId" title="userId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="publicInfo" %}{% endlanying_code_snippet %}
```
### userId

`- (long long)userId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/username" title="username"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="userId" %}{% endlanying_code_snippet %}
```
### username

`- (NSString *)username`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="username" %}{% endlanying_code_snippet %}
```
