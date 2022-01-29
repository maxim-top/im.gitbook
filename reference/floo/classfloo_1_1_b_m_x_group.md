---
title: floo::BMXGroup
summary: 群组 

---

# floo::BMXGroup



群组 


`#include <bmx_group.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[InvitationStatus](classfloo_1_1_b_m_x_group.md#enum-invitationstatus)** { Pending, Accepted, Declined}<br>群邀请状态  |
| enum class| **[ApplicationStatus](classfloo_1_1_b_m_x_group.md#enum-applicationstatus)** { Pending, Accepted, Declined}<br>群申请状态  |
| enum class| **[MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode)** { All, None, AdminOrAt, Admin, At}<br>消息通知类型  |
| enum class| **[ModifyMode](classfloo_1_1_b_m_x_group.md#enum-modifymode)** { AdminOnly, Open}<br>群信息修改模式  |
| enum class| **[JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode)** { Open, NeedApproval, RejectAll}<br>进群验证方式  |
| enum class| **[InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode)** { AdminOnly, Open}<br>邀请入群模式  |
| enum class| **[UpdateInfoType](classfloo_1_1_b_m_x_group.md#enum-updateinfotype)** { UnKnown, Name, Description, Avatar, Owner, Ext, NickName, ModifyMode, JoinAuthMode, InviteMode, MsgPushMode, MsgMuteMode, ReadAckMode, HistoryVisibleMode, BanExpireTime}<br>群组信息更新类型  |
| enum class| **[GroupStatus](classfloo_1_1_b_m_x_group.md#enum-groupstatus)** { Normal, Destroyed}<br>群组状态  |
| enum class| **[MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode)** { None, MuteNotification, MuteChat}<br>群组消息屏蔽模式  |
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
| virtual | **[~BMXGroup](classfloo_1_1_b_m_x_group.md#function-~bmxgroup)**()<br>析构函数  |
| virtual int64_t | **[groupId](classfloo_1_1_b_m_x_group.md#function-groupid)**() =0<br>群Id  |
| virtual [GroupType](classfloo_1_1_b_m_x_group.md#enum-grouptype) | **[groupType](classfloo_1_1_b_m_x_group.md#function-grouptype)**() =0<br>当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）  |
| virtual const std::string & | **[myNickname](classfloo_1_1_b_m_x_group.md#function-mynickname)**() =0<br>在群里的昵称  |
| virtual const std::string & | **[name](classfloo_1_1_b_m_x_group.md#function-name)**() =0<br>群名称  |
| virtual const std::string & | **[description](classfloo_1_1_b_m_x_group.md#function-description)**() =0<br>群描述  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_group.md#function-avatarratelurl)**() =0<br>群头像Ratel服务器Url  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_group.md#function-avatarurl)**() =0<br>群头像服务器Url  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_group.md#function-avatarpath)**() =0<br>群头像下载后的本地路径  |
| virtual std::string | **[avatarThumbnailUrl](classfloo_1_1_b_m_x_group.md#function-avatarthumbnailurl)**() =0<br>群头像缩略图服务器Url  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_group.md#function-avatarthumbnailpath)**() =0<br>群头像缩略图下载后的本地路径  |
| virtual int64_t | **[createTime](classfloo_1_1_b_m_x_group.md#function-createtime)**() =0<br>群创建时间  |
| virtual const JSON & | **[extension](classfloo_1_1_b_m_x_group.md#function-extension)**() =0<br>群扩展信息  |
| virtual int64_t | **[ownerId](classfloo_1_1_b_m_x_group.md#function-ownerid)**() =0<br>群Owner  |
| virtual int | **[capacity](classfloo_1_1_b_m_x_group.md#function-capacity)**() =0<br>最大人数  |
| virtual int | **[membersCount](classfloo_1_1_b_m_x_group.md#function-memberscount)**() =0<br>群成员数量，包含Owner，admins 和members  |
| virtual int | **[adminsCount](classfloo_1_1_b_m_x_group.md#function-adminscount)**() =0<br>群管理员数量  |
| virtual int | **[blockListSize](classfloo_1_1_b_m_x_group.md#function-blocklistsize)**() =0<br>黑名单数量  |
| virtual int | **[bannedListSize](classfloo_1_1_b_m_x_group.md#function-bannedlistsize)**() =0<br>禁言数量  |
| virtual int | **[sharedFilesCount](classfloo_1_1_b_m_x_group.md#function-sharedfilescount)**() =0<br>群共享文件数量  |
| virtual int64_t | **[latestAnnouncementId](classfloo_1_1_b_m_x_group.md#function-latestannouncementid)**() =0<br>最新群公告id  |
| virtual [MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode) | **[msgPushMode](classfloo_1_1_b_m_x_group.md#function-msgpushmode)**() =0<br>群消息通知类型  |
| virtual [ModifyMode](classfloo_1_1_b_m_x_group.md#enum-modifymode) | **[modifyMode](classfloo_1_1_b_m_x_group.md#function-modifymode)**() =0<br>群信息修改模式  |
| virtual [JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode) | **[joinAuthMode](classfloo_1_1_b_m_x_group.md#function-joinauthmode)**() =0<br>入群审批模式  |
| virtual [InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode) | **[inviteMode](classfloo_1_1_b_m_x_group.md#function-invitemode)**() =0<br>入群邀请模式  |
| virtual [MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode) | **[msgMuteMode](classfloo_1_1_b_m_x_group.md#function-msgmutemode)**() =0<br>群消息屏蔽模式  |
| virtual [GroupStatus](classfloo_1_1_b_m_x_group.md#enum-groupstatus) | **[groupStatus](classfloo_1_1_b_m_x_group.md#function-groupstatus)**() =0<br>当前群组的状态。（Normal 正常， Destroyed 以销毁）  |
| virtual bool | **[isMember](classfloo_1_1_b_m_x_group.md#function-ismember)**() =0<br>Deprecated use roleType instead.  |
| virtual bool | **[enableReadAck](classfloo_1_1_b_m_x_group.md#function-enablereadack)**() =0<br>是否开启群消息已读功能  |
| virtual bool | **[historyVisible](classfloo_1_1_b_m_x_group.md#function-historyvisible)**() =0<br>是否可以加载显示历史聊天记录  |
| virtual [MemberRoleType](classfloo_1_1_b_m_x_group.md#enum-memberroletype) | **[roleType](classfloo_1_1_b_m_x_group.md#function-roletype)**() =0<br>成员在群组内的角色类型  |
| virtual int64_t | **[banExpireTime](classfloo_1_1_b_m_x_group.md#function-banexpiretime)**() =0<br>群组全员禁言到期时间  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroup](classfloo_1_1_b_m_x_group.md#function-bmxgroup)**() |

## Public Types Documentation

### enum InvitationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | 请求待处理   |
| Accepted | | 请求已接受   |
| Declined | | 请求已拒绝   |



群邀请状态 

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | 请求待处理   |
| Accepted | | 请求已接受   |
| Declined | | 请求已拒绝   |



群申请状态 

### enum MsgPushMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| All | | 通知所有群消息   |
| None | | 所有消息都不通知   |
| AdminOrAt | | 只通知管理员或者被@消息   |
| Admin | | 只通知知管理员消息   |
| At | | 只通知被@消息   |



消息通知类型 

### enum ModifyMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AdminOnly | | 只有管理员可以   |
| Open | | 所有群成员都可以修改   |



群信息修改模式 

### enum JoinAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | 无需验证   |
| NeedApproval | | 需要管理员批准   |
| RejectAll | | 拒绝所有申请   |



进群验证方式 

### enum InviteMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AdminOnly | | 只有管理员可以邀请他人进群   |
| Open | | 所有人都可以邀请他人进群   |



邀请入群模式 

### enum UpdateInfoType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| UnKnown | | 默认初始化值   |
| Name | | 修改群名称   |
| Description | | 修改群描述   |
| Avatar | | 修改群头像   |
| Owner | | 修改群主   |
| Ext | | 修改群扩展   |
| NickName | | 群成员修改昵称   |
| ModifyMode | | 修改群信息模式   |
| JoinAuthMode | | 修改进群验证方式   |
| InviteMode | | 修改邀请入群模式   |
| MsgPushMode | | 修改群消息推送类型   |
| MsgMuteMode | | 修改是否提醒消息   |
| ReadAckMode | | 是否开启群消息已读功能   |
| HistoryVisibleMode | | 新群成员是否可见群历史聊天记录   |
| BanExpireTime | | 群组全员禁言到期时间   |



群组信息更新类型 

### enum GroupStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal | | 群组状态正常   |
| Destroyed | | 群组已销毁   |



群组状态 

### enum MsgMuteMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| None | | 不屏蔽   |
| MuteNotification | | 屏蔽本地消息通知   |
| MuteChat | | 屏蔽消息，不接收消息   |



群组消息屏蔽模式 

### enum MemberRoleType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| GroupMember | | 群成员   |
| GroupAdmin | | 群管理员   |
| GroupOwner | | 群主   |
| NotGroupMember | | 非群成员   |




### enum GroupType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Private | | 私有群组   |
| Public | | 公开群组(现在暂时没有开放次类型群组)   |
| Chatroom | | 聊天室   |




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

析构函数 

### function groupId

```cpp
virtual int64_t groupId() =0
```

群Id 

**Return**: int64_t 

### function groupType

```cpp
virtual GroupType groupType() =0
```

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室） 

**Return**: GroupType 

### function myNickname

```cpp
virtual const std::string & myNickname() =0
```

在群里的昵称 

**Return**: std::string 

### function name

```cpp
virtual const std::string & name() =0
```

群名称 

**Return**: std::string 

### function description

```cpp
virtual const std::string & description() =0
```

群描述 

**Return**: std::string 

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

群头像Ratel服务器Url 

**Return**: std::string 

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

群头像服务器Url 

**Return**: std::string 

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

群头像下载后的本地路径 

**Return**: std::string 

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

群头像缩略图服务器Url 

**Return**: std::string 

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

群头像缩略图下载后的本地路径 

**Return**: std::string 

### function createTime

```cpp
virtual int64_t createTime() =0
```

群创建时间 

**Return**: int64_t 

### function extension

```cpp
virtual const JSON & extension() =0
```

群扩展信息 

**Return**: JSON(std::string) 

### function ownerId

```cpp
virtual int64_t ownerId() =0
```

群Owner 

**Return**: int64_t 

### function capacity

```cpp
virtual int capacity() =0
```

最大人数 

**Return**: int 

### function membersCount

```cpp
virtual int membersCount() =0
```

群成员数量，包含Owner，admins 和members 

**Return**: int 

### function adminsCount

```cpp
virtual int adminsCount() =0
```

群管理员数量 

**Return**: int 

### function blockListSize

```cpp
virtual int blockListSize() =0
```

黑名单数量 

**Return**: int 

### function bannedListSize

```cpp
virtual int bannedListSize() =0
```

禁言数量 

**Return**: int 

### function sharedFilesCount

```cpp
virtual int sharedFilesCount() =0
```

群共享文件数量 

**Return**: int 

### function latestAnnouncementId

```cpp
virtual int64_t latestAnnouncementId() =0
```

最新群公告id 

**Return**: int64_t 

### function msgPushMode

```cpp
virtual MsgPushMode msgPushMode() =0
```

群消息通知类型 

**Return**: MsgPushMode 

### function modifyMode

```cpp
virtual ModifyMode modifyMode() =0
```

群信息修改模式 

**Return**: ModifyMode 

### function joinAuthMode

```cpp
virtual JoinAuthMode joinAuthMode() =0
```

入群审批模式 

**Return**: JoinAuthMode 

### function inviteMode

```cpp
virtual InviteMode inviteMode() =0
```

入群邀请模式 

**Return**: InviteMode 

### function msgMuteMode

```cpp
virtual MsgMuteMode msgMuteMode() =0
```

群消息屏蔽模式 

**Return**: MsgMuteMode 

### function groupStatus

```cpp
virtual GroupStatus groupStatus() =0
```

当前群组的状态。（Normal 正常， Destroyed 以销毁） 

**Return**: GroupStatus 

### function isMember

```cpp
virtual bool isMember() =0
```

Deprecated use roleType instead. 

**Return**: bool 

当前用户是否是群成员 


### function enableReadAck

```cpp
virtual bool enableReadAck() =0
```

是否开启群消息已读功能 

**Return**: bool 

### function historyVisible

```cpp
virtual bool historyVisible() =0
```

是否可以加载显示历史聊天记录 

**Return**: bool 

### function roleType

```cpp
virtual MemberRoleType roleType() =0
```

成员在群组内的角色类型 

**Return**: MemberRoleType 

### function banExpireTime

```cpp
virtual int64_t banExpireTime() =0
```

群组全员禁言到期时间 

**Return**: int64_t 

## Protected Functions Documentation

### function BMXGroup

```cpp
inline BMXGroup()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800