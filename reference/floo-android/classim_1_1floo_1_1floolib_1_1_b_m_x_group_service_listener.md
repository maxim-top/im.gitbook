---
title: im::floo::floolib::BMXGroupServiceListener
summary: Group change listener 

---

# im::floo::floolib::BMXGroupServiceListener



Group change listener 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-swigtakeownership)**() |
| void | **[onGroupCreate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupcreate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Create a group cross-device synchronously  |
| void | **[onGroupListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**(BMXGroupList list)<br>Group list updated  |
| void | **[onGroupJoined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupjoined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Join a group  |
| void | **[onGroupLeft](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupleft)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String reason)<br>Quit a group  |
| void | **[onInvitated](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitated)**(long groupId, long inviter, String message)<br>Group invitation received  |
| void | **[onInvitationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviteeId)<br>Group invitation accepted  |
| void | **[onInvitationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviteeId, String reason)<br>Join group rejected  |
| void | **[onApplied](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplied)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId, String message)<br>Group membership application received  |
| void | **[onApplicationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long approver)<br>Join group accepted  |
| void | **[onApplicationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long approver, String reason)<br>Join group rejected  |
| void | **[onMembersBanned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersbanned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration)<br>Member banned  |
| void | **[onMembersUnbanned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Member unbanned  |
| void | **[onMemberJoined](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberjoined)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, long inviter)<br>New member added  |
| void | **[onMemberLeft](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberleft)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, String reason)<br>Member quit  |
| void | **[onAdminsAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsadded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>New Admin added  |
| void | **[onAdminsRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsremoved)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String reason)<br>Admin removed  |
| void | **[onOwnerAssigned](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onownerassigned)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Become group Owner  |
| void | **[onGroupInfoUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.UpdateInfoType type)<br>Group information changes  |
| void | **[onMemberChangeNickName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long memberId, String nickName)<br>Member nickname changed  |
| void | **[onAnnouncementUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.Announcement announcement)<br>Group announcement received  |
| void | **[onSharedFileUploaded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>Share file received  |
| void | **[onSharedFileDeleted](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>Shared file deleted  |
| void | **[onSharedFileUpdated](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>Name of shared file updated  |
| void | **[onBlockListAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistadded)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Add to blacklist  |
| void | **[onBlockListRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Delete blacklist  |
| void | **[onGroupListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**()<br>Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information  |
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

Create a group cross-device synchronously 

**Parameters**: 

  * **group** Newly created group 


### function onGroupListUpdate

```java
inline void onGroupListUpdate(
    BMXGroupList list
)
```

Group list updated 

**Parameters**: 

  * **list** Updated group list 


### function onGroupJoined

```java
inline void onGroupJoined(
    BMXGroup group
)
```

Join a group 

**Parameters**: 

  * **group** Group to join 


### function onGroupLeft

```java
inline void onGroupLeft(
    BMXGroup group,
    String reason
)
```

Quit a group 

**Parameters**: 

  * **group** Group to quit 
  * **reason** Quit reason 


### function onInvitated

```java
inline void onInvitated(
    long groupId,
    long inviter,
    String message
)
```

Group invitation received 

**Parameters**: 

  * **groupId** Group id invited to 
  * **inviter** Inviter id 
  * **message** Invitation reason 


### function onInvitationAccepted

```java
inline void onInvitationAccepted(
    BMXGroup group,
    long inviteeId
)
```

Group invitation accepted 

**Parameters**: 

  * **group** A group in which invitation approved 
  * **inviteeId** Invitee id 


### function onInvitationDeclined

```java
inline void onInvitationDeclined(
    BMXGroup group,
    long inviteeId,
    String reason
)
```

Join group rejected 

**Parameters**: 

  * **group** A group in which invitation rejected 
  * **inviteeId** Invitee id 
  * **reason** Rejection reason 


### function onApplied

```java
inline void onApplied(
    BMXGroup group,
    long applicantId,
    String message
)
```

Group membership application received 

**Parameters**: 

  * **group** A group in which received membership application 
  * **applicantId** Applicant id 
  * **message** Application reason 


### function onApplicationAccepted

```java
inline void onApplicationAccepted(
    BMXGroup group,
    long approver
)
```

Join group accepted 

**Parameters**: 

  * **group** Group where membership application was accepted 
  * **approver** Approver of the application 


### function onApplicationDeclined

```java
inline void onApplicationDeclined(
    BMXGroup group,
    long approver,
    String reason
)
```

Join group rejected 

**Parameters**: 

  * **group** Group where membership application was rejected 
  * **approver** Approver of the application 
  * **reason** Reason for rejection 


### function onMembersBanned

```java
inline void onMembersBanned(
    BMXGroup group,
    ListOfLongLong members,
    long duration
)
```

Member banned 

**Parameters**: 

  * **group** Group with member banned 
  * **members** List of banned member ids 
  * **duration** Duration of banned 


### function onMembersUnbanned

```java
inline void onMembersUnbanned(
    BMXGroup group,
    ListOfLongLong members
)
```

Member unbanned 

**Parameters**: 

  * **group** Group with member unbanned 
  * **members** List of unbanned group member ids 


### function onMemberJoined

```java
inline void onMemberJoined(
    BMXGroup group,
    long memberId,
    long inviter
)
```

New member added 

**Parameters**: 

  * **group** Group with new member added 
  * **memberId** ID of added member 
  * **inviter** Inviter id 


### function onMemberLeft

```java
inline void onMemberLeft(
    BMXGroup group,
    long memberId,
    String reason
)
```

Member quit 

**Parameters**: 

  * **group** Group with member quitting 
  * **memberId** ID of quitted member 
  * **reason** Reason for quitting 


### function onAdminsAdded

```java
inline void onAdminsAdded(
    BMXGroup group,
    ListOfLongLong members
)
```

New Admin added 

**Parameters**: 

  * **group** Group where addition of new Admin occurred 
  * **members** List of members promoted to Admins 


### function onAdminsRemoved

```java
inline void onAdminsRemoved(
    BMXGroup group,
    ListOfLongLong members,
    String reason
)
```

Admin removed 

**Parameters**: 

  * **group** Group where Admin removal occurred 
  * **members** List of members degraded from Admins 
  * **reason** Reason for removal 


### function onOwnerAssigned

```java
inline void onOwnerAssigned(
    BMXGroup group
)
```

Become group Owner 

**Parameters**: 

  * **group** A group in which group Owner transferred 


### function onGroupInfoUpdate

```java
inline void onGroupInfoUpdate(
    BMXGroup group,
    BMXGroup.UpdateInfoType type
)
```

Group information changes 

**Parameters**: 

  * **group** Group with group information changed 
  * **type** Type of group information that changed 


### function onMemberChangeNickName

```java
inline void onMemberChangeNickName(
    BMXGroup group,
    long memberId,
    String nickName
)
```

Member nickname changed 

**Parameters**: 

  * **group** A group in which member nickname changed 
  * **memberId** Group member id that changed group nickname 
  * **nickName** Changed group nickname 


### function onAnnouncementUpdate

```java
inline void onAnnouncementUpdate(
    BMXGroup group,
    BMXGroup.Announcement announcement
)
```

Group announcement received 

**Parameters**: 

  * **group** Group where announcement update occurred 
  * **announcement** Latest group announcement after changed 


### function onSharedFileUploaded

```java
inline void onSharedFileUploaded(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

Share file received 

**Parameters**: 

  * **group** A group in which shared file uploading occurred 
  * **sharedFile** Newly uploaded group shared file 


### function onSharedFileDeleted

```java
inline void onSharedFileDeleted(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

Shared file deleted 

**Parameters**: 

  * **group** A group in which shared file deleted 
  * **sharedFile** Deleted group shared file 


### function onSharedFileUpdated

```java
inline void onSharedFileUpdated(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

Name of shared file updated 

**Parameters**: 

  * **group** A group in which share file updated 
  * **sharedFile** Updated group shared file 


### function onBlockListAdded

```java
inline void onBlockListAdded(
    BMXGroup group,
    ListOfLongLong members
)
```

Add to blacklist 

**Parameters**: 

  * **group** Group with blacklist added 
  * **members** List of blacklisted members 


### function onBlockListRemoved

```java
inline void onBlockListRemoved(
    BMXGroup group,
    ListOfLongLong members
)
```

Delete blacklist 

**Parameters**: 

  * **group** Group with blacklist removed 
  * **members** List of unblacklisted members 


### function onGroupListUpdate

```java
inline void onGroupListUpdate()
```

Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information 

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