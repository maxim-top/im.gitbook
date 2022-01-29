---
title: im::floo::floolib::BMXGroupServiceListener
summary: 群组变化监听者 

---

# im::floo::floolib::BMXGroupServiceListener



群组变化监听者 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigtakeownership)**() |
| void | **[onGroupCreate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupcreate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>多设备同步创建群组  |
| void | **[onGroupListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**(BMXGroupList list)<br>群列表更新了  |
| void | **[onGroupJoined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupjoined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>加入了某群  |
| void | **[onGroupLeft](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupleft)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String reason)<br>退出了某群  |
| void | **[onInvitated](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitated)**(long groupId, long inviter, String message)<br>收到入群邀请  |
| void | **[onInvitationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviteeId)<br>入群邀请被接受  |
| void | **[onInvitationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviteeId, String reason)<br>入群申请被拒绝  |
| void | **[onApplied](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplied)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId, String message)<br>收到入群申请  |
| void | **[onApplicationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long approver)<br>入群申请被接受  |
| void | **[onApplicationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long approver, String reason)<br>入群申请被拒绝  |
| void | **[onMembersBanned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersbanned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration)<br>群成员被禁言  |
| void | **[onMembersUnbanned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>群成员被解除禁言  |
| void | **[onMemberJoined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberjoined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, long inviter)<br>加入新成员  |
| void | **[onMemberLeft](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberleft)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, String reason)<br>群成员退出  |
| void | **[onAdminsAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsadded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>添加了新管理员  |
| void | **[onAdminsRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsremoved)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String reason)<br>移除了管理员  |
| void | **[onOwnerAssigned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onownerassigned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>成为群主  |
| void | **[onGroupInfoUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.UpdateInfoType type)<br>群组信息变更  |
| void | **[onMemberChangeNickName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, String nickName)<br>群成员更改群内昵称  |
| void | **[onAnnouncementUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.Announcement announcement)<br>收到群公告  |
| void | **[onSharedFileUploaded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>收到共享文件  |
| void | **[onSharedFileDeleted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>删除了共享文件  |
| void | **[onSharedFileUpdated](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>共享文件更新文件名  |
| void | **[onBlockListAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistadded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>添加黑名单  |
| void | **[onBlockListRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>删除黑名单  |
| void | **[onGroupListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**()<br>客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息  |
| | **[BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener)**() |
| void | **[registerGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-registergroupservice)**([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-getcptr)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
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


### function onGroupListUpdate

```java
inline void onGroupListUpdate(
    BMXGroupList list
)
```

群列表更新了 

**Parameters**: 

  * **list** 更新的群组列表 


### function onGroupJoined

```java
inline void onGroupJoined(
    BMXGroup group
)
```

加入了某群 

**Parameters**: 

  * **group** 加入的群组 


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


### function onOwnerAssigned

```java
inline void onOwnerAssigned(
    BMXGroup group
)
```

成为群主 

**Parameters**: 

  * **group** 被转让为群主的群组 


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


### function onGroupListUpdate

```java
inline void onGroupListUpdate()
```

客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息 

### function BMXGroupServiceListener

```java
inline BMXGroupServiceListener()
```


### function registerGroupService

```java
inline void registerGroupService(
    BMXGroupService service
)
```


## Protected Functions Documentation

### function BMXGroupServiceListener

```java
inline BMXGroupServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800