---
title: floo::BMXGroup
summary: Group 

---

# floo::BMXGroup



Group 


`#include <bmx_group.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[InvitationStatus](classfloo_1_1_b_m_x_group.md#enum-invitationstatus)** { Pending, Accepted, Declined}<br>Group invitation state  |
| enum class| **[ApplicationStatus](classfloo_1_1_b_m_x_group.md#enum-applicationstatus)** { Pending, Accepted, Declined}<br>Group application state  |
| enum class| **[MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode)** { All, None, AdminOrAt, Admin, At}<br>Message notification type  |
| enum class| **[ModifyMode](classfloo_1_1_b_m_x_group.md#enum-modifymode)** { AdminOnly, Open}<br>Group information modification mode  |
| enum class| **[JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode)** { Open, NeedApproval, RejectAll}<br>Group joining authentication mode  |
| enum class| **[InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode)** { AdminOnly, Open}<br>Group invitation mode  |
| enum class| **[UpdateInfoType](classfloo_1_1_b_m_x_group.md#enum-updateinfotype)** { UnKnown, Name, Description, Avatar, Owner, Ext, NickName, ModifyMode, JoinAuthMode, InviteMode, MsgPushMode, MsgMuteMode, ReadAckMode, HistoryVisibleMode, BanExpireTime}<br>Group information update type  |
| enum class| **[GroupStatus](classfloo_1_1_b_m_x_group.md#enum-groupstatus)** { Normal, Destroyed}<br>Grouping state  |
| enum class| **[MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode)** { None, MuteNotification, MuteChat}<br>Group message blocking mode  |
| enum class| **[MemberRoleType](classfloo_1_1_b_m_x_group.md#enum-memberroletype)** { GroupMember, GroupAdmin, GroupOwner, NotGroupMember} |
| enum class| **[GroupType](classfloo_1_1_b_m_x_group.md#enum-grouptype)** { Private, Public, Chatroom} |
| typedef std::shared_ptr< [Member] > | **[MemberPtr](classfloo_1_1_b_m_x_group.md#typedef-memberptr)**  |
| typedef std::vector< MemberPtr > | **[MemberList](classfloo_1_1_b_m_x_group.md#typedef-memberlist)**  |
| typedef std::shared_ptr< [BannedMember] > | **[BannedMemberPtr](classfloo_1_1_b_m_x_group.md#typedef-bannedmemberptr)**  |
| typedef std::vector< BannedMemberPtr > | **[BannedMemberList](classfloo_1_1_b_m_x_group.md#typedef-bannedmemberlist)**  |
| typedef std::shared_ptr< [SharedFile] > | **[SharedFilePtr](classfloo_1_1_b_m_x_group.md#typedef-sharedfileptr)**  |
| typedef std::vector< SharedFilePtr > | **[SharedFileList](classfloo_1_1_b_m_x_group.md#typedef-sharedfilelist)**  |
| typedef std::shared_ptr< [Announcement] > | **[AnnouncementPtr](classfloo_1_1_b_m_x_group.md#typedef-announcementptr)**  |
| typedef std::vector< AnnouncementPtr > | **[AnnouncementList](classfloo_1_1_b_m_x_group.md#typedef-announcementlist)**  |
| typedef std::shared_ptr< [Invitation] > | **[InvitationPtr](classfloo_1_1_b_m_x_group.md#typedef-invitationptr)**  |
| typedef std::vector< InvitationPtr > | **[InvitationList](classfloo_1_1_b_m_x_group.md#typedef-invitationlist)**  |
| typedef std::shared_ptr< [Application] > | **[ApplicationPtr](classfloo_1_1_b_m_x_group.md#typedef-applicationptr)**  |
| typedef std::vector< ApplicationPtr > | **[ApplicationList](classfloo_1_1_b_m_x_group.md#typedef-applicationlist)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXGroup](classfloo_1_1_b_m_x_group.md#function-~bmxgroup)**()<br>Destructor  |
| virtual int64_t | **[groupId](classfloo_1_1_b_m_x_group.md#function-groupid)**() =0<br>Group Id  |
| virtual [GroupType](classfloo_1_1_b_m_x_group.md#enum-grouptype) | **[groupType](classfloo_1_1_b_m_x_group.md#function-grouptype)**() =0<br>Type of the current group (Private, Public, Chatroom)  |
| virtual const std::string & | **[myNickname](classfloo_1_1_b_m_x_group.md#function-mynickname)**() =0<br>Group member nickname of mine  |
| virtual const std::string & | **[name](classfloo_1_1_b_m_x_group.md#function-name)**() =0<br>Group name  |
| virtual const std::string & | **[description](classfloo_1_1_b_m_x_group.md#function-description)**() =0<br>Group description  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_group.md#function-avatarratelurl)**() =0<br>Url for group avatar Ratel server  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_group.md#function-avatarurl)**() =0<br>Url for group avatar server  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_group.md#function-avatarpath)**() =0<br>Local path of downloaded group avatar  |
| virtual std::string | **[avatarThumbnailUrl](classfloo_1_1_b_m_x_group.md#function-avatarthumbnailurl)**() =0<br>Url for group avatar thumbnail server  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_group.md#function-avatarthumbnailpath)**() =0<br>Local path of downloaded group avatar thumbnail  |
| virtual int64_t | **[createTime](classfloo_1_1_b_m_x_group.md#function-createtime)**() =0<br>Group creation time  |
| virtual const JSON & | **[extension](classfloo_1_1_b_m_x_group.md#function-extension)**() =0<br>Group extension information  |
| virtual int64_t | **[ownerId](classfloo_1_1_b_m_x_group.md#function-ownerid)**() =0<br>Group Owner  |
| virtual int | **[capacity](classfloo_1_1_b_m_x_group.md#function-capacity)**() =0<br>Maximum number of group members  |
| virtual int | **[membersCount](classfloo_1_1_b_m_x_group.md#function-memberscount)**() =0<br>Number of group members, including Owner, Admins and Members  |
| virtual int | **[adminsCount](classfloo_1_1_b_m_x_group.md#function-adminscount)**() =0<br>Number of group admins  |
| virtual int | **[blockListSize](classfloo_1_1_b_m_x_group.md#function-blocklistsize)**() =0<br>Blacklisted user-number  |
| virtual int | **[bannedListSize](classfloo_1_1_b_m_x_group.md#function-bannedlistsize)**() =0<br>Banned user-number  |
| virtual int | **[sharedFilesCount](classfloo_1_1_b_m_x_group.md#function-sharedfilescount)**() =0<br>Shared file-number in group  |
| virtual int64_t | **[latestAnnouncementId](classfloo_1_1_b_m_x_group.md#function-latestannouncementid)**() =0<br>Latest group announcement id  |
| virtual [MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode) | **[msgPushMode](classfloo_1_1_b_m_x_group.md#function-msgpushmode)**() =0<br>Group message notification type  |
| virtual [ModifyMode](classfloo_1_1_b_m_x_group.md#enum-modifymode) | **[modifyMode](classfloo_1_1_b_m_x_group.md#function-modifymode)**() =0<br>Group information modification mode  |
| virtual [JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode) | **[joinAuthMode](classfloo_1_1_b_m_x_group.md#function-joinauthmode)**() =0<br>Join approval mode  |
| virtual [InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode) | **[inviteMode](classfloo_1_1_b_m_x_group.md#function-invitemode)**() =0<br>Group invitation mode  |
| virtual [MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode) | **[msgMuteMode](classfloo_1_1_b_m_x_group.md#function-msgmutemode)**() =0<br>Group message blocking mode  |
| virtual [GroupStatus](classfloo_1_1_b_m_x_group.md#enum-groupstatus) | **[groupStatus](classfloo_1_1_b_m_x_group.md#function-groupstatus)**() =0<br>state of the current group. (Normal, Destroyed)  |
| virtual bool | **[isMember](classfloo_1_1_b_m_x_group.md#function-ismember)**() =0<br>Deprecated use roleType instead.  |
| virtual bool | **[enableReadAck](classfloo_1_1_b_m_x_group.md#function-enablereadack)**() =0<br>Whether group message read acknowledgement feature enabled  |
| virtual bool | **[historyVisible](classfloo_1_1_b_m_x_group.md#function-historyvisible)**() =0<br>Whether to load and display the chat history  |
| virtual [MemberRoleType](classfloo_1_1_b_m_x_group.md#enum-memberroletype) | **[roleType](classfloo_1_1_b_m_x_group.md#function-roletype)**() =0<br>Type of a member role in group  |
| virtual int64_t | **[banExpireTime](classfloo_1_1_b_m_x_group.md#function-banexpiretime)**() =0<br>Expiration time of banning all group members  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroup](classfloo_1_1_b_m_x_group.md#function-bmxgroup)**() |

## Public Types Documentation

### enum InvitationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | Request pending   |
| Accepted | | Request accepted   |
| Declined | | Request rejected   |



Group invitation state 

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | Request pending   |
| Accepted | | Request accepted   |
| Declined | | Request rejected   |



Group application state 

### enum MsgPushMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| All | | Alert all group messages   |
| None | | Do not alert any group message   |
| AdminOrAt | | Alert Admins only, except @ messages   |
| Admin | | Alert Admins only   |
| At | | Alert @ messages only   |



Message notification type 

### enum ModifyMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AdminOnly | | Admin only   |
| Open | | Any group member can modify   |



Group information modification mode 

### enum JoinAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | No authentication required   |
| NeedApproval | | Admin approval required   |
| RejectAll | | All requests rejected   |



Group joining authentication mode 

### enum InviteMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AdminOnly | | Only Admins can invite new group member   |
| Open | | Anyone can invite new group member   |



Group invitation mode 

### enum UpdateInfoType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| UnKnown | | Default initialization value   |
| Name | | Modify group name   |
| Description | | Modify group description   |
| Avatar | | Modify group avatar   |
| Owner | | Modify group Owner   |
| Ext | | Modify group extension   |
| NickName | | Modify group member nickname   |
| ModifyMode | | Modify group information mode   |
| JoinAuthMode | | Modify group authentication mode   |
| InviteMode | | Modify group invitation mode   |
| MsgPushMode | | Modify group pushed message type   |
| MsgMuteMode | | Modify whether to alert message   |
| ReadAckMode | | Whether group message read acknowledgement feature enabled   |
| HistoryVisibleMode | | Whether group chat history is visible to new members   |
| BanExpireTime | | Expiration time of banning all group members   |



Group information update type 

### enum GroupStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal | | Group state is normal   |
| Destroyed | | Group destroyed   |



Grouping state 

### enum MsgMuteMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| None | | No blocking   |
| MuteNotification | | Block local message notification   |
| MuteChat | | Block message, no message received   |



Group message blocking mode 

### enum MemberRoleType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| GroupMember | | Group members   |
| GroupAdmin | | Group Admin   |
| GroupOwner | | Group Owner   |
| NotGroupMember | | Non-group member   |




### enum GroupType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Private | | Private group   |
| Public | | Public group (other sub-type groups are not released yet)   |
| Chatroom | | Chatroom   |




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

### function ~BMXGroup

```cpp
inline virtual ~BMXGroup()
```

Destructor 

### function groupId

```cpp
virtual int64_t groupId() =0
```

Group Id 

**Return**: int64_t 

### function groupType

```cpp
virtual GroupType groupType() =0
```

Type of the current group (Private, Public, Chatroom) 

**Return**: GroupType 

### function myNickname

```cpp
virtual const std::string & myNickname() =0
```

Group member nickname of mine 

**Return**: std::string 

### function name

```cpp
virtual const std::string & name() =0
```

Group name 

**Return**: std::string 

### function description

```cpp
virtual const std::string & description() =0
```

Group description 

**Return**: std::string 

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

Url for group avatar Ratel server 

**Return**: std::string 

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

Url for group avatar server 

**Return**: std::string 

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local path of downloaded group avatar 

**Return**: std::string 

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

Url for group avatar thumbnail server 

**Return**: std::string 

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local path of downloaded group avatar thumbnail 

**Return**: std::string 

### function createTime

```cpp
virtual int64_t createTime() =0
```

Group creation time 

**Return**: int64_t 

### function extension

```cpp
virtual const JSON & extension() =0
```

Group extension information 

**Return**: JSON(std::string) 

### function ownerId

```cpp
virtual int64_t ownerId() =0
```

Group Owner 

**Return**: int64_t 

### function capacity

```cpp
virtual int capacity() =0
```

Maximum number of group members 

**Return**: int 

### function membersCount

```cpp
virtual int membersCount() =0
```

Number of group members, including Owner, Admins and Members 

**Return**: int 

### function adminsCount

```cpp
virtual int adminsCount() =0
```

Number of group admins 

**Return**: int 

### function blockListSize

```cpp
virtual int blockListSize() =0
```

Blacklisted user-number 

**Return**: int 

### function bannedListSize

```cpp
virtual int bannedListSize() =0
```

Banned user-number 

**Return**: int 

### function sharedFilesCount

```cpp
virtual int sharedFilesCount() =0
```

Shared file-number in group 

**Return**: int 

### function latestAnnouncementId

```cpp
virtual int64_t latestAnnouncementId() =0
```

Latest group announcement id 

**Return**: int64_t 

### function msgPushMode

```cpp
virtual MsgPushMode msgPushMode() =0
```

Group message notification type 

**Return**: MsgPushMode 

### function modifyMode

```cpp
virtual ModifyMode modifyMode() =0
```

Group information modification mode 

**Return**: ModifyMode 

### function joinAuthMode

```cpp
virtual JoinAuthMode joinAuthMode() =0
```

Join approval mode 

**Return**: JoinAuthMode 

### function inviteMode

```cpp
virtual InviteMode inviteMode() =0
```

Group invitation mode 

**Return**: InviteMode 

### function msgMuteMode

```cpp
virtual MsgMuteMode msgMuteMode() =0
```

Group message blocking mode 

**Return**: MsgMuteMode 

### function groupStatus

```cpp
virtual GroupStatus groupStatus() =0
```

state of the current group. (Normal, Destroyed) 

**Return**: GroupStatus 

### function isMember

```cpp
virtual bool isMember() =0
```

Deprecated use roleType instead. 

**Return**: bool 

Whether the current user is a group member 


### function enableReadAck

```cpp
virtual bool enableReadAck() =0
```

Whether group message read acknowledgement feature enabled 

**Return**: bool 

### function historyVisible

```cpp
virtual bool historyVisible() =0
```

Whether to load and display the chat history 

**Return**: bool 

### function roleType

```cpp
virtual MemberRoleType roleType() =0
```

Type of a member role in group 

**Return**: MemberRoleType 

### function banExpireTime

```cpp
virtual int64_t banExpireTime() =0
```

Expiration time of banning all group members 

**Return**: int64_t 

## Protected Functions Documentation

### function BMXGroup

```cpp
inline BMXGroup()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800