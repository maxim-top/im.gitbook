# BMXGroup Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 群组

## Instance Methods

<a name="//api/name/adminsCount" title="adminsCount"></a>
### adminsCount

群管理员数量

`- (int)adminsCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="adminsCount" %}{% endlanying_code_snippet %}
```
### avatarPath

群头像下载后的本地路径

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

群头像Ratel服务器Url

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

群头像缩略图下载后的本地路径

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

群头像缩略图服务器Url

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

群头像服务器Url

`- (NSString *)avatarUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banExpireTime" title="banExpireTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### banExpireTime

群组全员禁言到期时间

`- (long long)banExpireTime`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/bannedListSize" title="bannedListSize"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banExpireTime" %}{% endlanying_code_snippet %}
```
### bannedListSize

禁言数量

`- (int)bannedListSize`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockListSize" title="blockListSize"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="bannedListSize" %}{% endlanying_code_snippet %}
```
### blockListSize

黑名单数量

`- (int)blockListSize`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/capacity" title="capacity"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="blockListSize" %}{% endlanying_code_snippet %}
```
### capacity

最大人数

`- (int)capacity`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createTime" title="createTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="capacity" %}{% endlanying_code_snippet %}
```
### createTime

群创建时间

`- (long long)createTime`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createTime" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/description" title="description"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### description

群描述

`- (NSString *)description`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/enableReadAck" title="enableReadAck"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="description" %}{% endlanying_code_snippet %}
```
### enableReadAck

是否开启群消息已读功能

`- (BOOL)enableReadAck`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/extension" title="extension"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="enableReadAck" %}{% endlanying_code_snippet %}
```
### extension

群扩展信息

`- (NSString *)extension`

#### Return Value
JSON(std::string)

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupId" title="groupId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="extension" %}{% endlanying_code_snippet %}
```
### groupId

群Id

`- (long long)groupId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupStatus" title="groupStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupId" %}{% endlanying_code_snippet %}
```
### groupStatus

当前群组的状态。（Normal 正常， Destroyed 以销毁）

`- (BMXGroup_GroupStatus)groupStatus`

#### Return Value
<a href="../Constants/BMXGroup_GroupStatus.md">BMXGroup_GroupStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupType" title="groupType"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupStatus" %}{% endlanying_code_snippet %}
```
### groupType

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）

`- (BMXGroup_GroupType)groupType`

#### Return Value
<a href="../Constants/BMXGroup_GroupType.md">BMXGroup_GroupType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/historyVisible" title="historyVisible"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupType" %}{% endlanying_code_snippet %}
```
### historyVisible

是否可以加载显示历史聊天记录

`- (BOOL)historyVisible`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/inviteMode" title="inviteMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="historyVisible" %}{% endlanying_code_snippet %}
```
### inviteMode

入群邀请模式

`- (BMXGroup_InviteMode)inviteMode`

#### Return Value
<a href="../Constants/BMXGroup_InviteMode.md">BMXGroup_InviteMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isMember" title="isMember"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="inviteMode" %}{% endlanying_code_snippet %}
```
### isMember

当前用户是否是群成员

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
{% lanying_code_snippet repo="floo-ios",class="",function="isMember" %}{% endlanying_code_snippet %}
```
### joinAuthMode

入群审批模式

`- (BMXGroup_JoinAuthMode)joinAuthMode`

#### Return Value
<a href="../Constants/BMXGroup_JoinAuthMode.md">BMXGroup_JoinAuthMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/latestAnnouncementId" title="latestAnnouncementId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="joinAuthMode" %}{% endlanying_code_snippet %}
```
### latestAnnouncementId

最新群公告id

`- (long long)latestAnnouncementId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/membersCount" title="membersCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="latestAnnouncementId" %}{% endlanying_code_snippet %}
```
### membersCount

群成员数量，包含Owner，admins 和members

`- (int)membersCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/modifyMode" title="modifyMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="membersCount" %}{% endlanying_code_snippet %}
```
### modifyMode

群信息修改模式

`- (BMXGroup_ModifyMode)modifyMode`

#### Return Value
<a href="../Constants/BMXGroup_ModifyMode.md">BMXGroup_ModifyMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgMuteMode" title="msgMuteMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="modifyMode" %}{% endlanying_code_snippet %}
```
### msgMuteMode

群消息屏蔽模式

`- (BMXGroup_MsgMuteMode)msgMuteMode`

#### Return Value
<a href="../Constants/BMXGroup_MsgMuteMode.md">BMXGroup_MsgMuteMode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgPushMode" title="msgPushMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="msgMuteMode" %}{% endlanying_code_snippet %}
```
### msgPushMode

群消息通知类型

`- (BMXGroup_MsgPushMode)msgPushMode`

#### Return Value
MsgPushMode

#### Declared In
* `floo_proxy.h`

<a name="//api/name/myNickname" title="myNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="msgPushMode" %}{% endlanying_code_snippet %}
```
### myNickname

在群里的昵称

`- (NSString *)myNickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/name" title="name"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="myNickname" %}{% endlanying_code_snippet %}
```
### name

群名称

`- (NSString *)name`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ownerId" title="ownerId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="name" %}{% endlanying_code_snippet %}
```
### ownerId

群Owner

`- (long long)ownerId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/roleType" title="roleType"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ownerId" %}{% endlanying_code_snippet %}
```
### roleType

成员在群组内的角色类型

`- (BMXGroup_MemberRoleType)roleType`

#### Return Value
<a href="../Constants/BMXGroup_MemberRoleType.md">BMXGroup_MemberRoleType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sharedFilesCount" title="sharedFilesCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="roleType" %}{% endlanying_code_snippet %}
```
### sharedFilesCount

群共享文件数量

`- (int)sharedFilesCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sharedFilesCount" %}{% endlanying_code_snippet %}
```
