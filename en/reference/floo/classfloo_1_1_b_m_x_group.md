---
title: floo::BMXGroup
summary: Group
---

# floo::BMXGroup

Group

`#include <bmx_group.h>`

Inherits from BMXBaseObject

## Public Types

|                                             | Name                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-invitationstatus"><strong>InvitationStatus</strong></a> { Pending, Accepted, Declined}<br>Group invitation state</p>                                                                                                                                                 |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-applicationstatus"><strong>ApplicationStatus</strong></a> { Pending, Accepted, Declined}<br>Group application state</p>                                                                                                                                              |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-msgpushmode"><strong>MsgPushMode</strong></a> { All, None, AdminOrAt, Admin, At}<br>Message notification type</p>                                                                                                                                                    |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-modifymode"><strong>ModifyMode</strong></a> { AdminOnly, Open}<br>Group information modification mode</p>                                                                                                                                                            |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-joinauthmode"><strong>JoinAuthMode</strong></a> { Open, NeedApproval, RejectAll}<br>Group joining authentication mode</p>                                                                                                                                            |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-invitemode"><strong>InviteMode</strong></a> { AdminOnly, Open}<br>Group invitation mode</p>                                                                                                                                                                          |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-updateinfotype"><strong>UpdateInfoType</strong></a> { UnKnown, Name, Description, Avatar, Owner, Ext, NickName, ModifyMode, JoinAuthMode, InviteMode, MsgPushMode, MsgMuteMode, ReadAckMode, HistoryVisibleMode, BanExpireTime}<br>Group information update type</p> |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-groupstatus"><strong>GroupStatus</strong></a> { Normal, Destroyed}<br>Grouping state</p>                                                                                                                                                                             |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-msgmutemode"><strong>MsgMuteMode</strong></a> { None, MuteNotification, MuteChat}<br>Group message blocking mode</p>                                                                                                                                                 |
| enum class                                  | [**MemberRoleType**](classfloo\_1\_1\_b\_m\_x\_group.md#enum-memberroletype) { GroupMember, GroupAdmin, GroupOwner, NotGroupMember}                                                                                                                                                                                |
| enum class                                  | [**GroupType**](classfloo\_1\_1\_b\_m\_x\_group.md#enum-grouptype) { Private, Public, Chatroom}                                                                                                                                                                                                                    |
| typedef std::shared\_ptr< \[Member] >       | [**MemberPtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-memberptr)                                                                                                                                                                                                                                              |
| typedef std::vector< MemberPtr >            | [**MemberList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-memberlist)                                                                                                                                                                                                                                            |
| typedef std::shared\_ptr< \[BannedMember] > | [**BannedMemberPtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-bannedmemberptr)                                                                                                                                                                                                                                  |
| typedef std::vector< BannedMemberPtr >      | [**BannedMemberList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-bannedmemberlist)                                                                                                                                                                                                                                |
| typedef std::shared\_ptr< \[SharedFile] >   | [**SharedFilePtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-sharedfileptr)                                                                                                                                                                                                                                      |
| typedef std::vector< SharedFilePtr >        | [**SharedFileList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-sharedfilelist)                                                                                                                                                                                                                                    |
| typedef std::shared\_ptr< \[Announcement] > | [**AnnouncementPtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-announcementptr)                                                                                                                                                                                                                                  |
| typedef std::vector< AnnouncementPtr >      | [**AnnouncementList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-announcementlist)                                                                                                                                                                                                                                |
| typedef std::shared\_ptr< \[Invitation] >   | [**InvitationPtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-invitationptr)                                                                                                                                                                                                                                      |
| typedef std::vector< InvitationPtr >        | [**InvitationList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-invitationlist)                                                                                                                                                                                                                                    |
| typedef std::shared\_ptr< \[Application] >  | [**ApplicationPtr**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-applicationptr)                                                                                                                                                                                                                                    |
| typedef std::vector< ApplicationPtr >       | [**ApplicationList**](classfloo\_1\_1\_b\_m\_x\_group.md#typedef-applicationlist)                                                                                                                                                                                                                                  |

## Public Functions

|                                                                                  | Name                                                                                                                                                                        |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                          | <p><a href="classfloo_1_1_b_m_x_group.md#function-~bmxgroup"><strong>~BMXGroup</strong></a>()<br>Destructor</p>                                                             |
| virtual int64\_t                                                                 | <p><a href="classfloo_1_1_b_m_x_group.md#function-groupid"><strong>groupId</strong></a>() =0<br>Group Id</p>                                                                |
| virtual [GroupType](classfloo\_1\_1\_b\_m\_x\_group.md#enum-grouptype)           | <p><a href="classfloo_1_1_b_m_x_group.md#function-grouptype"><strong>groupType</strong></a>() =0<br>Type of the current group (Private, Public, Chatroom)</p>               |
| virtual const std::string &                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-mynickname"><strong>myNickname</strong></a>() =0<br>Group member nickname of mine</p>                                     |
| virtual const std::string &                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-name"><strong>name</strong></a>() =0<br>Group name</p>                                                                    |
| virtual const std::string &                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-description"><strong>description</strong></a>() =0<br>Group description</p>                                               |
| virtual std::string                                                              | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>Url for group avatar Ratel server</p>                         |
| virtual std::string                                                              | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>Url for group avatar server</p>                                         |
| virtual std::string                                                              | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>Local path of downloaded group avatar</p>                             |
| virtual std::string                                                              | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>() =0<br>Url for group avatar thumbnail server</p>             |
| virtual std::string                                                              | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>Local path of downloaded group avatar thumbnail</p> |
| virtual int64\_t                                                                 | <p><a href="classfloo_1_1_b_m_x_group.md#function-createtime"><strong>createTime</strong></a>() =0<br>Group creation time</p>                                               |
| virtual const JSON &                                                             | <p><a href="classfloo_1_1_b_m_x_group.md#function-extension"><strong>extension</strong></a>() =0<br>Group extension information</p>                                         |
| virtual int64\_t                                                                 | <p><a href="classfloo_1_1_b_m_x_group.md#function-ownerid"><strong>ownerId</strong></a>() =0<br>Group Owner</p>                                                             |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-capacity"><strong>capacity</strong></a>() =0<br>Maximum number of group members</p>                                       |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-memberscount"><strong>membersCount</strong></a>() =0<br>Number of group members, including Owner, Admins and Members</p>  |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-adminscount"><strong>adminsCount</strong></a>() =0<br>Number of group admins</p>                                          |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-blocklistsize"><strong>blockListSize</strong></a>() =0<br>Blacklisted user-number</p>                                     |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-bannedlistsize"><strong>bannedListSize</strong></a>() =0<br>Banned user-number</p>                                        |
| virtual int                                                                      | <p><a href="classfloo_1_1_b_m_x_group.md#function-sharedfilescount"><strong>sharedFilesCount</strong></a>() =0<br>Shared file-number in group</p>                           |
| virtual int64\_t                                                                 | <p><a href="classfloo_1_1_b_m_x_group.md#function-latestannouncementid"><strong>latestAnnouncementId</strong></a>() =0<br>Latest group announcement id</p>                  |
| virtual [MsgPushMode](classfloo\_1\_1\_b\_m\_x\_group.md#enum-msgpushmode)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-msgpushmode"><strong>msgPushMode</strong></a>() =0<br>Group message notification type</p>                                 |
| virtual [ModifyMode](classfloo\_1\_1\_b\_m\_x\_group.md#enum-modifymode)         | <p><a href="classfloo_1_1_b_m_x_group.md#function-modifymode"><strong>modifyMode</strong></a>() =0<br>Group information modification mode</p>                               |
| virtual [JoinAuthMode](classfloo\_1\_1\_b\_m\_x\_group.md#enum-joinauthmode)     | <p><a href="classfloo_1_1_b_m_x_group.md#function-joinauthmode"><strong>joinAuthMode</strong></a>() =0<br>Join approval mode</p>                                            |
| virtual [InviteMode](classfloo\_1\_1\_b\_m\_x\_group.md#enum-invitemode)         | <p><a href="classfloo_1_1_b_m_x_group.md#function-invitemode"><strong>inviteMode</strong></a>() =0<br>Group invitation mode</p>                                             |
| virtual [MsgMuteMode](classfloo\_1\_1\_b\_m\_x\_group.md#enum-msgmutemode)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-msgmutemode"><strong>msgMuteMode</strong></a>() =0<br>Group message blocking mode</p>                                     |
| virtual [GroupStatus](classfloo\_1\_1\_b\_m\_x\_group.md#enum-groupstatus)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-groupstatus"><strong>groupStatus</strong></a>() =0<br>state of the current group. (Normal, Destroyed)</p>                 |
| virtual bool                                                                     | <p><a href="classfloo_1_1_b_m_x_group.md#function-ismember"><strong>isMember</strong></a>() =0<br>Deprecated use roleType instead.</p>                                      |
| virtual bool                                                                     | <p><a href="classfloo_1_1_b_m_x_group.md#function-enablereadack"><strong>enableReadAck</strong></a>() =0<br>Whether group message read acknowledgement feature enabled</p>  |
| virtual bool                                                                     | <p><a href="classfloo_1_1_b_m_x_group.md#function-historyvisible"><strong>historyVisible</strong></a>() =0<br>Whether to load and display the chat history</p>              |
| virtual [MemberRoleType](classfloo\_1\_1\_b\_m\_x\_group.md#enum-memberroletype) | <p><a href="classfloo_1_1_b_m_x_group.md#function-roletype"><strong>roleType</strong></a>() =0<br>Type of a member role in group</p>                                        |
| virtual int64\_t                                                                 | <p><a href="classfloo_1_1_b_m_x_group.md#function-banexpiretime"><strong>banExpireTime</strong></a>() =0<br>Expiration time of banning all group members</p>                |

## Protected Functions

|   | Name                                                                   |
| - | ---------------------------------------------------------------------- |
|   | [**BMXGroup**](classfloo\_1\_1\_b\_m\_x\_group.md#function-bmxgroup)() |

## Public Types Documentation

### enum InvitationStatus

| Enumerator | Value | Description      |
| ---------- | ----- | ---------------- |
| Pending    |       | Request pending  |
| Accepted   |       | Request accepted |
| Declined   |       | Request rejected |

Group invitation state

### enum ApplicationStatus

| Enumerator | Value | Description      |
| ---------- | ----- | ---------------- |
| Pending    |       | Request pending  |
| Accepted   |       | Request accepted |
| Declined   |       | Request rejected |

Group application state

### enum MsgPushMode

| Enumerator | Value | Description                          |
| ---------- | ----- | ------------------------------------ |
| All        |       | Alert all group messages             |
| None       |       | Do not alert any group message       |
| AdminOrAt  |       | Alert Admins only, except @ messages |
| Admin      |       | Alert Admins only                    |
| At         |       | Alert @ messages only                |

Message notification type

### enum ModifyMode

| Enumerator | Value | Description                 |
| ---------- | ----- | --------------------------- |
| AdminOnly  |       | Admin only                  |
| Open       |       | Any group member can modify |

Group information modification mode

### enum JoinAuthMode

| Enumerator   | Value | Description                |
| ------------ | ----- | -------------------------- |
| Open         |       | No authentication required |
| NeedApproval |       | Admin approval required    |
| RejectAll    |       | All requests rejected      |

Group joining authentication mode

### enum InviteMode

| Enumerator | Value | Description                             |
| ---------- | ----- | --------------------------------------- |
| AdminOnly  |       | Only Admins can invite new group member |
| Open       |       | Anyone can invite new group member      |

Group invitation mode

### enum UpdateInfoType

| Enumerator         | Value | Description                                                |
| ------------------ | ----- | ---------------------------------------------------------- |
| UnKnown            |       | Default initialization value                               |
| Name               |       | Modify group name                                          |
| Description        |       | Modify group description                                   |
| Avatar             |       | Modify group avatar                                        |
| Owner              |       | Modify group Owner                                         |
| Ext                |       | Modify group extension                                     |
| NickName           |       | Modify group member nickname                               |
| ModifyMode         |       | Modify group information mode                              |
| JoinAuthMode       |       | Modify group authentication mode                           |
| InviteMode         |       | Modify group invitation mode                               |
| MsgPushMode        |       | Modify group pushed message type                           |
| MsgMuteMode        |       | Modify whether to alert message                            |
| ReadAckMode        |       | Whether group message read acknowledgement feature enabled |
| HistoryVisibleMode |       | Whether group chat history is visible to new members       |
| BanExpireTime      |       | Expiration time of banning all group members               |

Group information update type

### enum GroupStatus

| Enumerator | Value | Description           |
| ---------- | ----- | --------------------- |
| Normal     |       | Group state is normal |
| Destroyed  |       | Group destroyed       |

Grouping state

### enum MsgMuteMode

| Enumerator       | Value | Description                        |
| ---------------- | ----- | ---------------------------------- |
| None             |       | No blocking                        |
| MuteNotification |       | Block local message notification   |
| MuteChat         |       | Block message, no message received |

Group message blocking mode

### enum MemberRoleType

| Enumerator     | Value | Description      |
| -------------- | ----- | ---------------- |
| GroupMember    |       | Group members    |
| GroupAdmin     |       | Group Admin      |
| GroupOwner     |       | Group Owner      |
| NotGroupMember |       | Non-group member |

### enum GroupType

| Enumerator | Value | Description                                               |
| ---------- | ----- | --------------------------------------------------------- |
| Private    |       | Private group                                             |
| Public     |       | Public group (other sub-type groups are not released yet) |
| Chatroom   |       | Chatroom                                                  |

### typedef MemberPtr

```cpp
typedef std::shared_ptr<Member> floo::BMXGroup::MemberPtr;
```

### typedef MemberList

```cpp
typedef std::vector<MemberPtr> floo::BMXGroup::MemberList;
```

### typedef BannedMemberPtr

```cpp
typedef std::shared_ptr<BannedMember> floo::BMXGroup::BannedMemberPtr;
```

### typedef BannedMemberList

```cpp
typedef std::vector<BannedMemberPtr> floo::BMXGroup::BannedMemberList;
```

### typedef SharedFilePtr

```cpp
typedef std::shared_ptr<SharedFile> floo::BMXGroup::SharedFilePtr;
```

### typedef SharedFileList

```cpp
typedef std::vector<SharedFilePtr> floo::BMXGroup::SharedFileList;
```

### typedef AnnouncementPtr

```cpp
typedef std::shared_ptr<Announcement> floo::BMXGroup::AnnouncementPtr;
```

### typedef AnnouncementList

```cpp
typedef std::vector<AnnouncementPtr> floo::BMXGroup::AnnouncementList;
```

### typedef InvitationPtr

```cpp
typedef std::shared_ptr<Invitation> floo::BMXGroup::InvitationPtr;
```

### typedef InvitationList

```cpp
typedef std::vector<InvitationPtr> floo::BMXGroup::InvitationList;
```

### typedef ApplicationPtr

```cpp
typedef std::shared_ptr<Application> floo::BMXGroup::ApplicationPtr;
```

### typedef ApplicationList

```cpp
typedef std::vector<ApplicationPtr> floo::BMXGroup::ApplicationList;
```

## Public Functions Documentation

### function \~BMXGroup

```cpp
inline virtual ~BMXGroup()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function groupId

```cpp
virtual int64_t groupId() =0
```

Group Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function groupType

```cpp
virtual GroupType groupType() =0
```

Type of the current group (Private, Public, Chatroom)

**Return**: GroupType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function myNickname

```cpp
virtual const std::string & myNickname() =0
```

Group member nickname of mine

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function name

```cpp
virtual const std::string & name() =0
```

Group name

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function description

```cpp
virtual const std::string & description() =0
```

Group description

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

Url for group avatar Ratel server

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

Url for group avatar server

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local path of downloaded group avatar

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

Url for group avatar thumbnail server

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local path of downloaded group avatar thumbnail

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function createTime

```cpp
virtual int64_t createTime() =0
```

Group creation time

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function extension

```cpp
virtual const JSON & extension() =0
```

Group extension information

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function ownerId

```cpp
virtual int64_t ownerId() =0
```

Group Owner

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function capacity

```cpp
virtual int capacity() =0
```

Maximum number of group members

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function membersCount

```cpp
virtual int membersCount() =0
```

Number of group members, including Owner, Admins and Members

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function adminsCount

```cpp
virtual int adminsCount() =0
```

Number of group admins

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function blockListSize

```cpp
virtual int blockListSize() =0
```

Blacklisted user-number

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function bannedListSize

```cpp
virtual int bannedListSize() =0
```

Banned user-number

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function sharedFilesCount

```cpp
virtual int sharedFilesCount() =0
```

Shared file-number in group

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function latestAnnouncementId

```cpp
virtual int64_t latestAnnouncementId() =0
```

Latest group announcement id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function msgPushMode

```cpp
virtual MsgPushMode msgPushMode() =0
```

Group message notification type

**Return**: MsgPushMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function modifyMode

```cpp
virtual ModifyMode modifyMode() =0
```

Group information modification mode

**Return**: ModifyMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function joinAuthMode

```cpp
virtual JoinAuthMode joinAuthMode() =0
```

Join approval mode

**Return**: JoinAuthMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function inviteMode

```cpp
virtual InviteMode inviteMode() =0
```

Group invitation mode

**Return**: InviteMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function msgMuteMode

```cpp
virtual MsgMuteMode msgMuteMode() =0
```

Group message blocking mode

**Return**: MsgMuteMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function groupStatus

```cpp
virtual GroupStatus groupStatus() =0
```

state of the current group. (Normal, Destroyed)

**Return**: GroupStatus

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function isMember

```cpp
virtual bool isMember() =0
```

Deprecated use roleType instead.

**Return**: bool

Whether the current user is a group member

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function enableReadAck

```cpp
virtual bool enableReadAck() =0
```

Whether group message read acknowledgement feature enabled

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function historyVisible

```cpp
virtual bool historyVisible() =0
```

Whether to load and display the chat history

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function roleType

```cpp
virtual MemberRoleType roleType() =0
```

Type of a member role in group

**Return**: MemberRoleType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function banExpireTime

```cpp
virtual int64_t banExpireTime() =0
```

Expiration time of banning all group members

**Return**: int64\_t

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

### function BMXGroup

```cpp
inline BMXGroup()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
