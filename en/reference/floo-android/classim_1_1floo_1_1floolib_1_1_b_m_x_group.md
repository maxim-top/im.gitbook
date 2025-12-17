---
title: im::floo::floolib::BMXGroup
summary: Group
---

# im::floo::floolib::BMXGroup

Group

Inherits from BMXBaseObject

## Public Classes

|       | Name                                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_announcement.md"><strong>Announcement</strong></a><br>Group announcement</p> |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_application.md"><strong>Application</strong></a><br>Group application</p>    |

## Public Functions

|                         | Name                                                                                                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                         | [**BMXGroup**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bmxgroup)()                                                                                                         |
| synchronized void       | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-delete)()                                                                                                             |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupid"><strong>groupId</strong></a>()<br>Group Id</p>                                                                |
| BMXGroup.GroupType      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-grouptype"><strong>groupType</strong></a>()<br>Type of the current group (Private, Public, Chatroom)</p>               |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-mynickname"><strong>myNickname</strong></a>()<br>Group member nickname of mine</p>                                     |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-name"><strong>name</strong></a>()<br>Group name</p>                                                                    |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-description"><strong>description</strong></a>()<br>Group description</p>                                               |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>Ratel address of group avatar</p>                             |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>Group avatar</p>                                                        |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>Local path of downloaded group avatar</p>                             |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>()<br>Group avatar thumbnail address</p>                    |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>Local path of downloaded group avatar thumbnail</p> |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-createtime"><strong>createTime</strong></a>()<br>Group creation time</p>                                               |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-extension"><strong>extension</strong></a>()<br>Group extension information</p>                                         |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ownerid"><strong>ownerId</strong></a>()<br>Group Owner</p>                                                             |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-capacity"><strong>capacity</strong></a>()<br>Maximum number of group members</p>                                       |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-memberscount"><strong>membersCount</strong></a>()<br>Number of group members, including Owner, Admins and Members</p>  |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-adminscount"><strong>adminsCount</strong></a>()<br>Number of group admins</p>                                          |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-blocklistsize"><strong>blockListSize</strong></a>()<br>Blacklisted user-number</p>                                     |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bannedlistsize"><strong>bannedListSize</strong></a>()<br>Banned user-number</p>                                        |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-sharedfilescount"><strong>sharedFilesCount</strong></a>()<br>Shared file-number in group</p>                           |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-latestannouncementid"><strong>latestAnnouncementId</strong></a>()<br>Latest group announcement id</p>                  |
| BMXGroup.MsgPushMode    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgpushmode"><strong>msgPushMode</strong></a>()<br>Group message notification type</p>                                 |
| BMXGroup.ModifyMode     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-modifymode"><strong>modifyMode</strong></a>()<br>Group information modification mode</p>                               |
| BMXGroup.JoinAuthMode   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-joinauthmode"><strong>joinAuthMode</strong></a>()<br>Join approval mode</p>                                            |
| BMXGroup.InviteMode     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-invitemode"><strong>inviteMode</strong></a>()<br>Group invitation mode</p>                                             |
| BMXGroup.MsgMuteMode    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgmutemode"><strong>msgMuteMode</strong></a>()<br>Group message blocking mode</p>                                     |
| BMXGroup.GroupStatus    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupstatus"><strong>groupStatus</strong></a>()<br>state of the current group. (Normal, Destroyed)</p>                 |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ismember"><strong>isMember</strong></a>()<br>Deprecated use roleType instead.</p>                                      |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-enablereadack"><strong>enableReadAck</strong></a>()<br>Whether group message read acknowledgement feature enabled</p>  |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-historyvisible"><strong>historyVisible</strong></a>()<br>Whether to load and display the chat history</p>              |
| BMXGroup.MemberRoleType | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-roletype"><strong>roleType</strong></a>()<br>Type of a member role in group</p>                                        |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-banexpiretime"><strong>banExpireTime</strong></a>()<br>Expiration time of banning all group members</p>                |

## Protected Functions

|      | Name                                                                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroup**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bmxgroup)(long cPtr, boolean cMemoryOwn)                               |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-finalize)()                                                            |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-getcptr)([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) obj) |

## Public Attributes

|                | Name                                                                            |
| -------------- | ------------------------------------------------------------------------------- |
| transient long | [**swigCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#variable-swigcptr) |

## Public Functions Documentation

### function BMXGroup

```java
inline BMXGroup()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function groupId

```java
inline long groupId()
```

Group Id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function groupType

```java
inline BMXGroup.GroupType groupType()
```

Type of the current group (Private, Public, Chatroom)

**Return**: \[GroupType]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function myNickname

```java
inline String myNickname()
```

Group member nickname of mine

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function name

```java
inline String name()
```

Group name

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function description

```java
inline String description()
```

Group description

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel address of group avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function avatarUrl

```java
inline String avatarUrl()
```

Group avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function avatarPath

```java
inline String avatarPath()
```

Local path of downloaded group avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

Group avatar thumbnail address

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local path of downloaded group avatar thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function createTime

```java
inline long createTime()
```

Group creation time

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function extension

```java
inline String extension()
```

Group extension information

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function ownerId

```java
inline long ownerId()
```

Group Owner

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function capacity

```java
inline int capacity()
```

Maximum number of group members

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function membersCount

```java
inline int membersCount()
```

Number of group members, including Owner, Admins and Members

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function adminsCount

```java
inline int adminsCount()
```

Number of group admins

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function blockListSize

```java
inline int blockListSize()
```

Blacklisted user-number

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function bannedListSize

```java
inline int bannedListSize()
```

Banned user-number

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function sharedFilesCount

```java
inline int sharedFilesCount()
```

Shared file-number in group

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function latestAnnouncementId

```java
inline long latestAnnouncementId()
```

Latest group announcement id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function msgPushMode

```java
inline BMXGroup.MsgPushMode msgPushMode()
```

Group message notification type

**Return**: \[MsgPushMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function modifyMode

```java
inline BMXGroup.ModifyMode modifyMode()
```

Group information modification mode

**Return**: \[ModifyMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function joinAuthMode

```java
inline BMXGroup.JoinAuthMode joinAuthMode()
```

Join approval mode

**Return**: \[JoinAuthMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function inviteMode

```java
inline BMXGroup.InviteMode inviteMode()
```

Group invitation mode

**Return**: \[InviteMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function msgMuteMode

```java
inline BMXGroup.MsgMuteMode msgMuteMode()
```

Group message blocking mode

**Return**: \[MsgMuteMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function groupStatus

```java
inline BMXGroup.GroupStatus groupStatus()
```

state of the current group. (Normal, Destroyed)

**Return**: \[GroupStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function isMember

```java
inline boolean isMember()
```

Deprecated use roleType instead.

**Return**: bool

Whether the current user is a group member

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function enableReadAck

```java
inline boolean enableReadAck()
```

Whether group message read acknowledgement feature enabled

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function historyVisible

```java
inline boolean historyVisible()
```

Whether to load and display the chat history

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function roleType

```java
inline BMXGroup.MemberRoleType roleType()
```

Type of a member role in group

**Return**: \[MemberRoleType]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function banExpireTime

```java
inline long banExpireTime()
```

Expiration time of banning all group members

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
