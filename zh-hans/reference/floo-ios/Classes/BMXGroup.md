# BMXGroup Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 群组

## Instance Methods

### adminsCount

群管理员数量

`- (int)adminsCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### avatarPath

群头像下载后的本地路径

`- (NSString *)avatarPath`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### avatarRatelUrl

群头像Ratel服务器Url

`- (NSString *)avatarRatelUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### avatarThumbnailPath

群头像缩略图下载后的本地路径

`- (NSString *)avatarThumbnailPath`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### avatarThumbnailUrl

群头像缩略图服务器Url

`- (NSString *)avatarThumbnailUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### avatarUrl

群头像服务器Url

`- (NSString *)avatarUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### banExpireTime

群组全员禁言到期时间

`- (long long)banExpireTime`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### bannedListSize

禁言数量

`- (int)bannedListSize`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### blockListSize

黑名单数量

`- (int)blockListSize`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### capacity

最大人数

`- (int)capacity`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### createTime

群创建时间

`- (long long)createTime`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### description

群描述

`- (NSString *)description`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### enableReadAck

是否开启群消息已读功能

`- (BOOL)enableReadAck`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### extension

群扩展信息

`- (NSString *)extension`

#### Return Value

JSON(std::string)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### groupId

群Id

`- (long long)groupId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### groupStatus

当前群组的状态。（Normal 正常， Destroyed 以销毁）

`- (BMXGroup_GroupStatus)groupStatus`

#### Return Value

[BMXGroup\_GroupStatus](../Constants/BMXGroup_GroupStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### groupType

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）

`- (BMXGroup_GroupType)groupType`

#### Return Value

[BMXGroup\_GroupType](../Constants/BMXGroup_GroupType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### historyVisible

是否可以加载显示历史聊天记录

`- (BOOL)historyVisible`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### inviteMode

入群邀请模式

`- (BMXGroup_InviteMode)inviteMode`

#### Return Value

[BMXGroup\_InviteMode](../Constants/BMXGroup_InviteMode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### isMember

当前用户是否是群成员

`- (BOOL)isMember`

#### Return Value

BOOL

#### Discussion

Deprecated use [roleType](BMXGroup.md#//api/name/roleType) instead.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### joinAuthMode

入群审批模式

`- (BMXGroup_JoinAuthMode)joinAuthMode`

#### Return Value

[BMXGroup\_JoinAuthMode](../Constants/BMXGroup_JoinAuthMode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### latestAnnouncementId

最新群公告id

`- (long long)latestAnnouncementId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### membersCount

群成员数量，包含Owner，admins 和members

`- (int)membersCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### modifyMode

群信息修改模式

`- (BMXGroup_ModifyMode)modifyMode`

#### Return Value

[BMXGroup\_ModifyMode](../Constants/BMXGroup_ModifyMode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### msgMuteMode

群消息屏蔽模式

`- (BMXGroup_MsgMuteMode)msgMuteMode`

#### Return Value

[BMXGroup\_MsgMuteMode](../Constants/BMXGroup_MsgMuteMode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### msgPushMode

群消息通知类型

`- (BMXGroup_MsgPushMode)msgPushMode`

#### Return Value

MsgPushMode

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### myNickname

在群里的昵称

`- (NSString *)myNickname`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### name

群名称

`- (NSString *)name`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### ownerId

群Owner

`- (long long)ownerId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

```

### roleType

成员在群组内的角色类型

`- (BMXGroup_MemberRoleType)roleType`

#### Return Value

[BMXGroup\_MemberRoleType](../Constants/BMXGroup_MemberRoleType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>
```
