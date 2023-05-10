# BMXRosterItem Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 联系人

## Instance Methods

<a name="//api/name/addFriendAuthMode" title="addFriendAuthMode"></a>
### addFriendAuthMode

roster的好友添加验证方式。

`- (BMXRosterItem_AddFriendAuthMode)addFriendAuthMode`

#### Return Value
<a href="../Constants/BMXRosterItem_AddFriendAuthMode.md">BMXRosterItem_AddFriendAuthMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/alias" title="alias"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### alias

用户对好友添加的备注等信息

`- (NSString *)alias`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/authQuestion" title="authQuestion"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="alias" %}{% endlanying_code_snippet %}
```
### authQuestion

roster的好友验证问题。

`- (NSString *)authQuestion`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="authQuestion" %}{% endlanying_code_snippet %}
```
### avatarPath

好友头像本地存储路径

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

好友头像Ratel服务器地址

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

好友头像缩略图本地存储路径

`- (NSString *)avatarThumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailUrl" title="avatarThumbnailUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### avatarThumbnailUrl

好友头像缩略图服务器地址

`- (NSString *)avatarThumbnailUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### avatarUrl

好友头像服务器地址

`- (NSString *)avatarUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/ext" title="ext"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### ext

用户的服务器扩展信息

`- (NSString *)ext`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isMuteNotification" title="isMuteNotification"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ext" %}{% endlanying_code_snippet %}
```
### isMuteNotification

是否提醒用户消息

`- (BOOL)isMuteNotification`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/localExt" title="localExt"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### localExt

用户的本地扩展信息

`- (NSString *)localExt`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/nickname" title="nickname"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="localExt" %}{% endlanying_code_snippet %}
```
### nickname

好友昵称

`- (NSString *)nickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/publicInfo" title="publicInfo"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="nickname" %}{% endlanying_code_snippet %}
```
### publicInfo

扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等

`- (NSString *)publicInfo`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/relation" title="relation"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="publicInfo" %}{% endlanying_code_snippet %}
```
### relation

联系人关系

`- (BMXRosterItem_RosterRelation)relation`

#### Return Value
<a href="../Constants/BMXRosterItem_RosterRelation.md">BMXRosterItem_RosterRelation</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/rosterId" title="rosterId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="relation" %}{% endlanying_code_snippet %}
```
### rosterId

好友Id

`- (long long)rosterId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/username" title="username"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="rosterId" %}{% endlanying_code_snippet %}
```
### username

好友名

`- (NSString *)username`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="username" %}{% endlanying_code_snippet %}
```
