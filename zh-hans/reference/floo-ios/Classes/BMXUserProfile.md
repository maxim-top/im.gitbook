# BMXUserProfile Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 用户Profile

## Instance Methods

<a name="//api/name/addFriendAuthMode" title="addFriendAuthMode"></a>
### addFriendAuthMode

加好友校验方式

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

添加好友时的验证问题

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

用户头像本地存储路径

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

用户ratel服务器头像url

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

用户头像缩略图本地存储路径

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

用户头像url

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

用户策略

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

用户邮箱

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

收到群组邀请进群时是否自动同意进群

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

用户消息设定

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

用户手机

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

用户昵称

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

用户私有扩展信息，好友不可见

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

用户公开扩展信息，好友可见

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

用户ID（唯一）

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

用户名（唯一）

`- (NSString *)username`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="username" %}{% endlanying_code_snippet %}
```
