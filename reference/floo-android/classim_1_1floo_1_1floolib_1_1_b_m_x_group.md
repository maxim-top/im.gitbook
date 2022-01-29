---
title: im::floo::floolib::BMXGroup
summary: Group 

---

# im::floo::floolib::BMXGroup



Group 

Inherits from BMXBaseObject

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Announcement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_announcement.md)** <br>Group announcement  |
| class | **[Application](classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_application.md)** <br>Group application  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bmxgroup)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-delete)**() |
| long | **[groupId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupid)**()<br>Group Id  |
| BMXGroup.GroupType | **[groupType](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-grouptype)**()<br>Type of the current group (Private, Public, Chatroom)  |
| String | **[myNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-mynickname)**()<br>Group member nickname  |
| String | **[name](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-name)**()<br>Group name  |
| String | **[description](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-description)**()<br>Group description  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarratelurl)**()<br>Ratel address of group avatar  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarurl)**()<br>Group avatar  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarpath)**()<br>Local path of downloaded group avatar  |
| String | **[avatarThumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailurl)**()<br>Group avatar thumbnail address  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailpath)**()<br>Local path of downloaded group avatar thumbnail  |
| long | **[createTime](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-createtime)**()<br>Group creation time  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-extension)**()<br>Group extension information  |
| long | **[ownerId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ownerid)**()<br>Group Owner  |
| int | **[capacity](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-capacity)**()<br>Max member-number  |
| int | **[membersCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-memberscount)**()<br>Group member-number, including Owner, Admins and Members  |
| int | **[adminsCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-adminscount)**()<br>Group admin-number  |
| int | **[blockListSize](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-blocklistsize)**()<br>Blacklisted user-number  |
| int | **[bannedListSize](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bannedlistsize)**()<br>Banned user-number  |
| int | **[sharedFilesCount](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-sharedfilescount)**()<br>Shared file-number in group  |
| long | **[latestAnnouncementId](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-latestannouncementid)**()<br>Latest group announcement id  |
| BMXGroup.MsgPushMode | **[msgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgpushmode)**()<br>Group message notification type  |
| BMXGroup.ModifyMode | **[modifyMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-modifymode)**()<br>Group information modification mode  |
| BMXGroup.JoinAuthMode | **[joinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-joinauthmode)**()<br>Join approval mode  |
| BMXGroup.InviteMode | **[inviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-invitemode)**()<br>Group invitation mode  |
| BMXGroup.MsgMuteMode | **[msgMuteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgmutemode)**()<br>Group message blocking mode  |
| BMXGroup.GroupStatus | **[groupStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupstatus)**()<br>state of the current group. (Normal, Destroyed)  |
| boolean | **[isMember](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ismember)**()<br>Deprecated use roleType instead.  |
| boolean | **[enableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-enablereadack)**()<br>Whether group message read feature enabled  |
| boolean | **[historyVisible](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-historyvisible)**()<br>Whether to load and display the chat history  |
| BMXGroup.MemberRoleType | **[roleType](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-roletype)**()<br>Type of a member role in group  |
| long | **[banExpireTime](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-banexpiretime)**()<br>**to-be-translate**  |

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


### function delete

```java
inline synchronized void delete()
```


### function groupId

```java
inline long groupId()
```

Group Id 

**Return**: int64_t 

### function groupType

```java
inline BMXGroup.GroupType groupType()
```

Type of the current group (Private, Public, Chatroom) 

**Return**: [GroupType]

### function myNickname

```java
inline String myNickname()
```

Group member nickname 

**Return**: std::string 

### function name

```java
inline String name()
```

Group name 

**Return**: std::string 

### function description

```java
inline String description()
```

Group description 

**Return**: std::string 

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel address of group avatar 

**Return**: std::string 

### function avatarUrl

```java
inline String avatarUrl()
```

Group avatar 

**Return**: std::string 

### function avatarPath

```java
inline String avatarPath()
```

Local path of downloaded group avatar 

**Return**: std::string 

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

Group avatar thumbnail address 

**Return**: std::string 

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local path of downloaded group avatar thumbnail 

**Return**: std::string 

### function createTime

```java
inline long createTime()
```

Group creation time 

**Return**: int64_t 

### function extension

```java
inline String extension()
```

Group extension information 

**Return**: JSON(std::string) 

### function ownerId

```java
inline long ownerId()
```

Group Owner 

**Return**: int64_t 

### function capacity

```java
inline int capacity()
```

Max member-number 

**Return**: int 

### function membersCount

```java
inline int membersCount()
```

Group member-number, including Owner, Admins and Members 

**Return**: int 

### function adminsCount

```java
inline int adminsCount()
```

Group admin-number 

**Return**: int 

### function blockListSize

```java
inline int blockListSize()
```

Blacklisted user-number 

**Return**: int 

### function bannedListSize

```java
inline int bannedListSize()
```

Banned user-number 

**Return**: int 

### function sharedFilesCount

```java
inline int sharedFilesCount()
```

Shared file-number in group 

**Return**: int 

### function latestAnnouncementId

```java
inline long latestAnnouncementId()
```

Latest group announcement id 

**Return**: int64_t 

### function msgPushMode

```java
inline BMXGroup.MsgPushMode msgPushMode()
```

Group message notification type 

**Return**: [MsgPushMode]

### function modifyMode

```java
inline BMXGroup.ModifyMode modifyMode()
```

Group information modification mode 

**Return**: [ModifyMode]

### function joinAuthMode

```java
inline BMXGroup.JoinAuthMode joinAuthMode()
```

Join approval mode 

**Return**: [JoinAuthMode]

### function inviteMode

```java
inline BMXGroup.InviteMode inviteMode()
```

Group invitation mode 

**Return**: [InviteMode]

### function msgMuteMode

```java
inline BMXGroup.MsgMuteMode msgMuteMode()
```

Group message blocking mode 

**Return**: [MsgMuteMode]

### function groupStatus

```java
inline BMXGroup.GroupStatus groupStatus()
```

state of the current group. (Normal, Destroyed) 

**Return**: [GroupStatus]

### function isMember

```java
inline boolean isMember()
```

Deprecated use roleType instead. 

**Return**: bool 

Whether the current user is a group member 


### function enableReadAck

```java
inline boolean enableReadAck()
```

Whether group message read feature enabled 

**Return**: bool 

### function historyVisible

```java
inline boolean historyVisible()
```

Whether to load and display the chat history 

**Return**: bool 

### function roleType

```java
inline BMXGroup.MemberRoleType roleType()
```

Type of a member role in group 

**Return**: [MemberRoleType]

### function banExpireTime

```java
inline long banExpireTime()
```

**to-be-translate** 

## Protected Functions Documentation

### function BMXGroup

```java
inline BMXGroup(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800