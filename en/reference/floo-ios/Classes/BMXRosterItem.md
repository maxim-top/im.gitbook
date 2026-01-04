# BMXRosterItem Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Roster item

## Instance Methods

<a name="//api/name/addFriendAuthMode" title="addFriendAuthMode"></a>
### addFriendAuthMode

Friend authorization mode

`- (BMXRosterItem_AddFriendAuthMode)addFriendAuthMode`

#### Return Value
<a href="../Constants/BMXRosterItem_AddFriendAuthMode.md">BMXRosterItem_AddFriendAuthMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/alias" title="alias"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### alias

Alias for friend

`- (NSString *)alias`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/authQuestion" title="authQuestion"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="alias" %}{% endlanying_code_snippet %}
```
### authQuestion

Authorization question

`- (NSString *)authQuestion`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="authQuestion" %}{% endlanying_code_snippet %}
```
### avatarPath

Local path of friends avatar

`- (NSString *)avatarPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarRatelUrl" title="avatarRatelUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="avatarPath" %}{% endlanying_code_snippet %}
```
### avatarRatelUrl

The friend's avatar URL on REST server

`- (NSString *)avatarRatelUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailPath" title="avatarThumbnailPath"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### avatarThumbnailPath

Local path of friends avatar thumbnail

`- (NSString *)avatarThumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailUrl" title="avatarThumbnailUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### avatarThumbnailUrl

The friend's avatar thumbnail URL on HTTP server

`- (NSString *)avatarThumbnailUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### avatarUrl

The friend's avatar URL on HTTP server

`- (NSString *)avatarUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/ext" title="ext"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="dealloc" %}{% endlanying_code_snippet %}
```
### ext

Extension information of the friend(on server)

`- (NSString *)ext`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isMuteNotification" title="isMuteNotification"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="ext" %}{% endlanying_code_snippet %}
```
### isMuteNotification

Whether to mute the user's push message notification

`- (BOOL)isMuteNotification`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/localExt" title="localExt"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### localExt

Extension information of the friend (local db only)

`- (NSString *)localExt`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/nickname" title="nickname"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="localExt" %}{% endlanying_code_snippet %}
```
### nickname

`- (NSString *)nickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/publicInfo" title="publicInfo"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="nickname" %}{% endlanying_code_snippet %}
```
### publicInfo

Extension information visible to friends

`- (NSString *)publicInfo`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/relation" title="relation"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="publicInfo" %}{% endlanying_code_snippet %}
```
### relation

My relationship to the friend

`- (BMXRosterItem_RosterRelation)relation`

#### Return Value
<a href="../Constants/BMXRosterItem_RosterRelation.md">BMXRosterItem_RosterRelation</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/rosterId" title="rosterId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="relation" %}{% endlanying_code_snippet %}
```
### rosterId

Friend ID

`- (long long)rosterId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/username" title="username"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="rosterId" %}{% endlanying_code_snippet %}
```
### username

Friend's username

`- (NSString *)username`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterItem",function="username" %}{% endlanying_code_snippet %}
```
