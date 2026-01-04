# BMXGroup Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Group

## Instance Methods

<a name="//api/name/adminsCount" title="adminsCount"></a>
### adminsCount

The number of administrators

`- (int)adminsCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="adminsCount" %}{% endlanying_code_snippet %}
```
### avatarPath

The local file path of group avatar

`- (NSString *)avatarPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarRatelUrl" title="avatarRatelUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="avatarPath" %}{% endlanying_code_snippet %}
```
### avatarRatelUrl

The group avatar URL on REST server

`- (NSString *)avatarRatelUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailPath" title="avatarThumbnailPath"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### avatarThumbnailPath

The local file path of group avatar thumbnail

`- (NSString *)avatarThumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarThumbnailUrl" title="avatarThumbnailUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### avatarThumbnailUrl

The group avatar thumbnail URL on HTTP server

`- (NSString *)avatarThumbnailUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### avatarUrl

The group avatar URL on HTTP server

`- (NSString *)avatarUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banExpireTime" title="banExpireTime"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### banExpireTime

The expiration time of all group members banned

`- (long long)banExpireTime`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/bannedListSize" title="bannedListSize"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="banExpireTime" %}{% endlanying_code_snippet %}
```
### bannedListSize

The number of group members banned

`- (int)bannedListSize`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockListSize" title="blockListSize"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="bannedListSize" %}{% endlanying_code_snippet %}
```
### blockListSize

The number of group members blocked

`- (int)blockListSize`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/capacity" title="capacity"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="blockListSize" %}{% endlanying_code_snippet %}
```
### capacity

Maximum number of group members

`- (int)capacity`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createTime" title="createTime"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="capacity" %}{% endlanying_code_snippet %}
```
### createTime

The created time of group

`- (long long)createTime`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="createTime" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/description" title="description"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="dealloc" %}{% endlanying_code_snippet %}
```
### description

Group discription

`- (NSString *)description`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/enableReadAck" title="enableReadAck"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="description" %}{% endlanying_code_snippet %}
```
### enableReadAck

Enable read ACK of group message

`- (BOOL)enableReadAck`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/extension" title="extension"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="enableReadAck" %}{% endlanying_code_snippet %}
```
### extension

Group extension information

`- (NSString *)extension`

#### Return Value
JSON(std::string)

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupId" title="groupId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="extension" %}{% endlanying_code_snippet %}
```
### groupId

Group ID

`- (long long)groupId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupStatus" title="groupStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="groupId" %}{% endlanying_code_snippet %}
```
### groupStatus

Group status(Normal|Destroyed)

`- (BMXGroup_GroupStatus)groupStatus`

#### Return Value
<a href="../Constants/BMXGroup_GroupStatus.md">BMXGroup_GroupStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupType" title="groupType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="groupStatus" %}{% endlanying_code_snippet %}
```
### groupType

Group type(Private|Public|Chatroom)

`- (BMXGroup_GroupType)groupType`

#### Return Value
<a href="../Constants/BMXGroup_GroupType.md">BMXGroup_GroupType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/historyVisible" title="historyVisible"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="groupType" %}{% endlanying_code_snippet %}
```
### historyVisible

Dispaly the history messages

`- (BOOL)historyVisible`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/inviteMode" title="inviteMode"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="historyVisible" %}{% endlanying_code_snippet %}
```
### inviteMode

Invitation mode

`- (BMXGroup_InviteMode)inviteMode`

#### Return Value
<a href="../Constants/BMXGroup_InviteMode.md">BMXGroup_InviteMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isMember" title="isMember"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="inviteMode" %}{% endlanying_code_snippet %}
```
### isMember

I am the group member

`- (BOOL)isMember`

#### Return Value
BOOL

#### Discussion
Deprecated use <a href="#//api/name/roleType">roleType</a> instead.

#### Declared In
* `floo_proxy.h`

<a name="//api/name/joinAuthMode" title="joinAuthMode"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="isMember" %}{% endlanying_code_snippet %}
```
### joinAuthMode

Authorization mode

`- (BMXGroup_JoinAuthMode)joinAuthMode`

#### Return Value
<a href="../Constants/BMXGroup_JoinAuthMode.md">BMXGroup_JoinAuthMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/latestAnnouncementId" title="latestAnnouncementId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="joinAuthMode" %}{% endlanying_code_snippet %}
```
### latestAnnouncementId

Latest group announcement ID

`- (long long)latestAnnouncementId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/membersCount" title="membersCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="latestAnnouncementId" %}{% endlanying_code_snippet %}
```
### membersCount

The number of all group member

`- (int)membersCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/modifyMode" title="modifyMode"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="membersCount" %}{% endlanying_code_snippet %}
```
### modifyMode

Modification mode of group information

`- (BMXGroup_ModifyMode)modifyMode`

#### Return Value
<a href="../Constants/BMXGroup_ModifyMode.md">BMXGroup_ModifyMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgMuteMode" title="msgMuteMode"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="modifyMode" %}{% endlanying_code_snippet %}
```
### msgMuteMode

Mute mode of group messages

`- (BMXGroup_MsgMuteMode)msgMuteMode`

#### Return Value
<a href="../Constants/BMXGroup_MsgMuteMode.md">BMXGroup_MsgMuteMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgPushMode" title="msgPushMode"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="msgMuteMode" %}{% endlanying_code_snippet %}
```
### msgPushMode

Group message push mode

`- (BMXGroup_MsgPushMode)msgPushMode`

#### Return Value
MsgPushMode

#### Declared In
* `floo_proxy.h`

<a name="//api/name/myNickname" title="myNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="msgPushMode" %}{% endlanying_code_snippet %}
```
### myNickname

My nick name in this group

`- (NSString *)myNickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/name" title="name"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="myNickname" %}{% endlanying_code_snippet %}
```
### name

Group name

`- (NSString *)name`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ownerId" title="ownerId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="name" %}{% endlanying_code_snippet %}
```
### ownerId

Group owner ID

`- (long long)ownerId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/roleType" title="roleType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="ownerId" %}{% endlanying_code_snippet %}
```
### roleType

The role type of group member

`- (BMXGroup_MemberRoleType)roleType`

#### Return Value
<a href="../Constants/BMXGroup_MemberRoleType.md">BMXGroup_MemberRoleType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sharedFilesCount" title="sharedFilesCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="roleType" %}{% endlanying_code_snippet %}
```
### sharedFilesCount

The number of file shared in the group

`- (int)sharedFilesCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroup",function="sharedFilesCount" %}{% endlanying_code_snippet %}
```
