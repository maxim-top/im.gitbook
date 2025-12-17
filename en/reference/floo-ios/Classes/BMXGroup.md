# BMXGroup Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Group

## Instance Methods

### adminsCount

The number of administrators

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

The local file path of group avatar

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

The group avatar URL on REST server

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

The local file path of group avatar thumbnail

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

The group avatar thumbnail URL on HTTP server

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

The group avatar URL on HTTP server

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

The expiration time of all group members banned

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

The number of group members banned

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

The number of group members blocked

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

Maximum number of group members

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

The created time of group

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

Group discription

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

Enable read ACK of group message

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

Group extension information

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

Group ID

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

Group status(Normal|Destroyed)

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

Group type(Private|Public|Chatroom)

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

Dispaly the history messages

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

Invitation mode

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

I am the group member

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

Authorization mode

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

Latest group announcement ID

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

The number of all group member

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

Modification mode of group information

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

Mute mode of group messages

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

Group message push mode

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

My nick name in this group

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

Group name

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

Group owner ID

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

The role type of group member

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

The number of file shared in the group

`- (int)sharedFilesCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroup'></div>
```
