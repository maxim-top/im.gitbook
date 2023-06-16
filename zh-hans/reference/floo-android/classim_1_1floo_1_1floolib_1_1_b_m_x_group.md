---
title: im::floo::floolib::BMXGroup
summary: 群组 

---

# im::floo::floolib::BMXGroup



群组 

Inherits from BMXBaseObject

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Announcement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_announcement.md)** <br>群公告  |
| class | **[Application](classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_application.md)** <br>群申请  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bmxgroup)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-delete)**() |
| long | **[groupId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupid)**()<br>群Id  |
| BMXGroup.GroupType | **[groupType](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-grouptype)**()<br>当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）  |
| String | **[myNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-mynickname)**()<br>在群里的昵称  |
| String | **[name](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-name)**()<br>群名称  |
| String | **[description](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-description)**()<br>群描述  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarratelurl)**()<br>群头像ratel地址  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarurl)**()<br>群头像  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarpath)**()<br>群头像下载后的本地路径  |
| String | **[avatarThumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailurl)**()<br>群头像缩略图地址  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailpath)**()<br>群头像缩略图下载后的本地路径  |
| long | **[createTime](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-createtime)**()<br>群创建时间  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-extension)**()<br>群扩展信息  |
| long | **[ownerId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ownerid)**()<br>群Owner  |
| int | **[capacity](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-capacity)**()<br>最大人数  |
| int | **[membersCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-memberscount)**()<br>群成员数量，包含Owner，admins 和members  |
| int | **[adminsCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-adminscount)**()<br>群管理员数量  |
| int | **[blockListSize](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-blocklistsize)**()<br>黑名单数量  |
| int | **[bannedListSize](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bannedlistsize)**()<br>禁言数量  |
| int | **[sharedFilesCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-sharedfilescount)**()<br>群共享文件数量  |
| long | **[latestAnnouncementId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-latestannouncementid)**()<br>最新群公告id  |
| BMXGroup.MsgPushMode | **[msgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgpushmode)**()<br>群消息通知类型  |
| BMXGroup.ModifyMode | **[modifyMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-modifymode)**()<br>群信息修改模式  |
| BMXGroup.JoinAuthMode | **[joinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-joinauthmode)**()<br>入群审批模式  |
| BMXGroup.InviteMode | **[inviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-invitemode)**()<br>入群邀请模式  |
| BMXGroup.MsgMuteMode | **[msgMuteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgmutemode)**()<br>群消息屏蔽模式  |
| BMXGroup.GroupStatus | **[groupStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupstatus)**()<br>当前群组的状态。（Normal 正常， Destroyed 以销毁）  |
| boolean | **[isMember](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ismember)**()<br>Deprecated use roleType instead.  |
| boolean | **[enableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-enablereadack)**()<br>是否开启群消息已读功能  |
| boolean | **[historyVisible](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-historyvisible)**()<br>是否可以加载显示历史聊天记录  |
| BMXGroup.MemberRoleType | **[roleType](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-roletype)**()<br>成员在群组内的角色类型  |
| long | **[banExpireTime](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-banexpiretime)**()<br>群组全员禁言到期时间  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bmxgroup)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-getcptr)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) obj) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| transient long | **[swigCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#variable-swigcptr)**  |

## Public Functions Documentation

### function BMXGroup

```java
inline BMXGroup()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="BMXGroup" %}{% endlanying_code_snippet %}
```
### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="delete" %}{% endlanying_code_snippet %}
```
### function groupId

```java
inline long groupId()
```

群Id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="groupId" %}{% endlanying_code_snippet %}
```
### function groupType

```java
inline BMXGroup.GroupType groupType()
```

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室） 

**Return**: [GroupType]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="groupType" %}{% endlanying_code_snippet %}
```
### function myNickname

```java
inline String myNickname()
```

在群里的昵称 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="myNickname" %}{% endlanying_code_snippet %}
```
### function name

```java
inline String name()
```

群名称 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="name" %}{% endlanying_code_snippet %}
```
### function description

```java
inline String description()
```

群描述 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="description" %}{% endlanying_code_snippet %}
```
### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

群头像ratel地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### function avatarUrl

```java
inline String avatarUrl()
```

群头像 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### function avatarPath

```java
inline String avatarPath()
```

群头像下载后的本地路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="avatarPath" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

群头像缩略图地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

群头像缩略图下载后的本地路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### function createTime

```java
inline long createTime()
```

群创建时间 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="createTime" %}{% endlanying_code_snippet %}
```
### function extension

```java
inline String extension()
```

群扩展信息 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="extension" %}{% endlanying_code_snippet %}
```
### function ownerId

```java
inline long ownerId()
```

群Owner 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="ownerId" %}{% endlanying_code_snippet %}
```
### function capacity

```java
inline int capacity()
```

最大人数 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="capacity" %}{% endlanying_code_snippet %}
```
### function membersCount

```java
inline int membersCount()
```

群成员数量，包含Owner，admins 和members 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="membersCount" %}{% endlanying_code_snippet %}
```
### function adminsCount

```java
inline int adminsCount()
```

群管理员数量 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="adminsCount" %}{% endlanying_code_snippet %}
```
### function blockListSize

```java
inline int blockListSize()
```

黑名单数量 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="blockListSize" %}{% endlanying_code_snippet %}
```
### function bannedListSize

```java
inline int bannedListSize()
```

禁言数量 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="bannedListSize" %}{% endlanying_code_snippet %}
```
### function sharedFilesCount

```java
inline int sharedFilesCount()
```

群共享文件数量 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="sharedFilesCount" %}{% endlanying_code_snippet %}
```
### function latestAnnouncementId

```java
inline long latestAnnouncementId()
```

最新群公告id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="latestAnnouncementId" %}{% endlanying_code_snippet %}
```
### function msgPushMode

```java
inline BMXGroup.MsgPushMode msgPushMode()
```

群消息通知类型 

**Return**: [MsgPushMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="msgPushMode" %}{% endlanying_code_snippet %}
```
### function modifyMode

```java
inline BMXGroup.ModifyMode modifyMode()
```

群信息修改模式 

**Return**: [ModifyMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="modifyMode" %}{% endlanying_code_snippet %}
```
### function joinAuthMode

```java
inline BMXGroup.JoinAuthMode joinAuthMode()
```

入群审批模式 

**Return**: [JoinAuthMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="joinAuthMode" %}{% endlanying_code_snippet %}
```
### function inviteMode

```java
inline BMXGroup.InviteMode inviteMode()
```

入群邀请模式 

**Return**: [InviteMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="inviteMode" %}{% endlanying_code_snippet %}
```
### function msgMuteMode

```java
inline BMXGroup.MsgMuteMode msgMuteMode()
```

群消息屏蔽模式 

**Return**: [MsgMuteMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="msgMuteMode" %}{% endlanying_code_snippet %}
```
### function groupStatus

```java
inline BMXGroup.GroupStatus groupStatus()
```

当前群组的状态。（Normal 正常， Destroyed 以销毁） 

**Return**: [GroupStatus]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="groupStatus" %}{% endlanying_code_snippet %}
```
### function isMember

```java
inline boolean isMember()
```

Deprecated use roleType instead. 

**Return**: bool 

当前用户是否是群成员 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="isMember" %}{% endlanying_code_snippet %}
```
### function enableReadAck

```java
inline boolean enableReadAck()
```

是否开启群消息已读功能 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="enableReadAck" %}{% endlanying_code_snippet %}
```
### function historyVisible

```java
inline boolean historyVisible()
```

是否可以加载显示历史聊天记录 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="historyVisible" %}{% endlanying_code_snippet %}
```
### function roleType

```java
inline BMXGroup.MemberRoleType roleType()
```

成员在群组内的角色类型 

**Return**: [MemberRoleType]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="roleType" %}{% endlanying_code_snippet %}
```
### function banExpireTime

```java
inline long banExpireTime()
```

群组全员禁言到期时间 

## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="banExpireTime" %}{% endlanying_code_snippet %}
```
### function BMXGroup

```java
inline BMXGroup(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="BMXGroup" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXGroup obj
)
```


## Public Attributes Documentation

### variable swigCPtr

```java
transient long swigCPtr;
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXGroup",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800