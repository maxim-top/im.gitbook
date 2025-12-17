---
title: im::floo::floolib::BMXGroupServiceListener
summary: 群组变化监听者
---

# im::floo::floolib::BMXGroupServiceListener

群组变化监听者

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-delete)()                                                                                                                                                                                       |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigreleaseownership)()                                                                                                                                                           |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigtakeownership)()                                                                                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupcreate"><strong>onGroupCreate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>多设备同步创建群组</p>                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>(BMXGroupList list)<br>群列表更新了</p>                                                                                                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupjoined"><strong>onGroupJoined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>加入了某群</p>                                                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupleft"><strong>onGroupLeft</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String reason)<br>退出了某群</p>                                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitated"><strong>onInvitated</strong></a>(long groupId, long inviter, String message)<br>收到入群邀请</p>                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted"><strong>onInvitationAccepted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviteeId)<br>入群邀请被接受</p>                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined"><strong>onInvitationDeclined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviteeId, String reason)<br>入群申请被拒绝</p>        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId, String message)<br>收到入群申请</p>                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long approver)<br>入群申请被接受</p>                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long approver, String reason)<br>入群申请被拒绝</p>       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersbanned"><strong>onMembersBanned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, long duration)<br>群成员被禁言</p>           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned"><strong>onMembersUnbanned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>群成员被解除禁言</p>                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberjoined"><strong>onMemberJoined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, long inviter)<br>加入新成员</p>                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberleft"><strong>onMemberLeft</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, String reason)<br>群成员退出</p>                           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsadded"><strong>onAdminsAdded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>添加了新管理员</p>                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsremoved"><strong>onAdminsRemoved</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String reason)<br>移除了管理员</p>           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onownerassigned"><strong>onOwnerAssigned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>成为群主</p>                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate"><strong>onGroupInfoUpdate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.UpdateInfoType type)<br>群组信息变更</p>                |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname"><strong>onMemberChangeNickName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, String nickName)<br>群成员更改群内昵称</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate"><strong>onAnnouncementUpdate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.Announcement announcement)<br>收到群公告</p>     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded"><strong>onSharedFileUploaded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>收到共享文件</p>        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted"><strong>onSharedFileDeleted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>删除了共享文件</p>         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated"><strong>onSharedFileUpdated</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>共享文件更新文件名</p>       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>添加黑名单</p>                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>删除黑名单</p>                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>()<br>客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息</p>                                                                            |
|                   | [**BMXGroupServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener)()                                                                                                                                                     |
| void              | [**registerGroupService**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-registergroupservice)([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) service)                                                                           |

## Protected Functions

|      | Name                                                                                                                                                                                          |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener)(long cPtr, boolean cMemoryOwn)                                 |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-finalize)()                                                                                            |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigdirectordisconnect)()                                                                |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-getcptr)([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupCreate

```java
inline void onGroupCreate(
    BMXGroup group
)
```

多设备同步创建群组

**Parameters**:

* **group** 新创建的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```java
inline void onGroupListUpdate(
    BMXGroupList list
)
```

群列表更新了

**Parameters**:

* **list** 更新的群组列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupJoined

```java
inline void onGroupJoined(
    BMXGroup group
)
```

加入了某群

**Parameters**:

* **group** 加入的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupLeft

```java
inline void onGroupLeft(
    BMXGroup group,
    String reason
)
```

退出了某群

**Parameters**:

* **group** 退出的群组
* **reason** 退出原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onInvitated

```java
inline void onInvitated(
    long groupId,
    long inviter,
    String message
)
```

收到入群邀请

**Parameters**:

* **groupId** 邀请进入的群组id
* **inviter** 邀请者id
* **message** 邀请原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationAccepted

```java
inline void onInvitationAccepted(
    BMXGroup group,
    long inviteeId
)
```

入群邀请被接受

**Parameters**:

* **group** 邀请被同意的群组
* **inviteeId** 被邀请者id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationDeclined

```java
inline void onInvitationDeclined(
    BMXGroup group,
    long inviteeId,
    String reason
)
```

入群申请被拒绝

**Parameters**:

* **group** 邀请被拒绝的群组
* **inviteeId** 被邀请者id
* **reason** 拒绝原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onApplied

```java
inline void onApplied(
    BMXGroup group,
    long applicantId,
    String message
)
```

收到入群申请

**Parameters**:

* **group** 收到入群申请的群组
* **applicantId** 申请者id
* **message** 申请原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationAccepted

```java
inline void onApplicationAccepted(
    BMXGroup group,
    long approver
)
```

入群申请被接受

**Parameters**:

* **group** 入群申请被接受的群组
* **approver** 申请的批准者

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationDeclined

```java
inline void onApplicationDeclined(
    BMXGroup group,
    long approver,
    String reason
)
```

入群申请被拒绝

**Parameters**:

* **group** 入群申请被拒绝的群组
* **approver** 申请的批准者
* **reason** 拒绝的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onMembersBanned

```java
inline void onMembersBanned(
    BMXGroup group,
    ListOfLongLong members,
    long duration
)
```

群成员被禁言

**Parameters**:

* **group** 群成员被禁言的群组
* **members** 被禁言的群成员id列表
* **duration** 禁言时长

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onMembersUnbanned

```java
inline void onMembersUnbanned(
    BMXGroup group,
    ListOfLongLong members
)
```

群成员被解除禁言

**Parameters**:

* **group** 群成员被解除禁言的群组
* **members** 被解除禁言的群成员id列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onMemberJoined

```java
inline void onMemberJoined(
    BMXGroup group,
    long memberId,
    long inviter
)
```

加入新成员

**Parameters**:

* **group** 有成员加入的群组
* **memberId** 加入成员的id
* **inviter** 邀请者id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onMemberLeft

```java
inline void onMemberLeft(
    BMXGroup group,
    long memberId,
    String reason
)
```

群成员退出

**Parameters**:

* **group** 有成员退出的群组
* **memberId** 退出的群成员id
* **reason** 退出的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsAdded

```java
inline void onAdminsAdded(
    BMXGroup group,
    ListOfLongLong members
)
```

添加了新管理员

**Parameters**:

* **group** 发生添加新管理员的群组
* **members** 被提升为管理员的成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsRemoved

```java
inline void onAdminsRemoved(
    BMXGroup group,
    ListOfLongLong members,
    String reason
)
```

移除了管理员

**Parameters**:

* **group** 发生移除管理员的群组
* **members** 被移除了管理员的成员列表
* **reason** 被移除的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onOwnerAssigned

```java
inline void onOwnerAssigned(
    BMXGroup group
)
```

成为群主

**Parameters**:

* **group** 被转让为群主的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupInfoUpdate

```java
inline void onGroupInfoUpdate(
    BMXGroup group,
    BMXGroup.UpdateInfoType type
)
```

群组信息变更

**Parameters**:

* **group** 群信息发生变更的群组
* **type** 发生变更的群信息类型

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onMemberChangeNickName

```java
inline void onMemberChangeNickName(
    BMXGroup group,
    long memberId,
    String nickName
)
```

群成员更改群内昵称

**Parameters**:

* **group** 发生群成员变更群昵称的群组
* **memberId** 变更群昵称的群成员id
* **nickName** 变更后的群昵称

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onAnnouncementUpdate

```java
inline void onAnnouncementUpdate(
    BMXGroup group,
    BMXGroup.Announcement announcement
)
```

收到群公告

**Parameters**:

* **group** 发生群公告更新的群组
* **announcement** 变更后的最新的群更高

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUploaded

```java
inline void onSharedFileUploaded(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

收到共享文件

**Parameters**:

* **group** 发生群共享文件上传的群组
* **sharedFile** 新上传的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileDeleted

```java
inline void onSharedFileDeleted(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

删除了共享文件

**Parameters**:

* **group** 发生群共享文件删除的群组
* **sharedFile** 被删除的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUpdated

```java
inline void onSharedFileUpdated(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

共享文件更新文件名

**Parameters**:

* **group** 发生群共享文件更新的群组
* **sharedFile** 更新的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListAdded

```java
inline void onBlockListAdded(
    BMXGroup group,
    ListOfLongLong members
)
```

添加黑名单

**Parameters**:

* **group** 添加黑名单的群组
* **members** 添加的黑名单成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListRemoved

```java
inline void onBlockListRemoved(
    BMXGroup group,
    ListOfLongLong members
)
```

删除黑名单

**Parameters**:

* **group** 删除黑名单的群组
* **members** 删除的黑名单成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```java
inline void onGroupListUpdate()
```

客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function BMXGroupServiceListener

```java
inline BMXGroupServiceListener()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function registerGroupService

```java
inline void registerGroupService(
    BMXGroupService service
)
```

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function BMXGroupServiceListener

```java
inline BMXGroupServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXGroupServiceListener obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
