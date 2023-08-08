---
title: im::floo::floolib::BMXGroupServiceListener
summary: Group change listener
---

# im::floo::floolib::BMXGroupServiceListener

Group change listener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-delete)()                                                                                                                                                                                                   |
| void              | [**swigReleaseOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-swigreleaseownership)()                                                                                                                                                                       |
| void              | [**swigTakeOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-swigtakeownership)()                                                                                                                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupcreate"><strong>onGroupCreate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Create a group</p>                                                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>(BMXGroupList list)<br>Group list updated</p>                                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupjoined"><strong>onGroupJoined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Join a group</p>                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupleft"><strong>onGroupLeft</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String reason)<br>Quit a group</p>                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitated"><strong>onInvitated</strong></a>(long groupId, long inviter, String message)<br>Group invitation received</p>                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted"><strong>onInvitationAccepted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviteeId)<br>Group invitation accepted</p>                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined"><strong>onInvitationDeclined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviteeId, String reason)<br>Join group rejected</p>                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId, String message)<br>Group membership application received</p>                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long approver)<br>Join group accepted</p>                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long approver, String reason)<br>Join group rejected</p>                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersbanned"><strong>onMembersBanned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, long duration)<br>Member banned</p>                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned"><strong>onMembersUnbanned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Member unbanned</p>                                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberjoined"><strong>onMemberJoined</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, long inviter)<br>New member added</p>                                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberleft"><strong>onMemberLeft</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, String reason)<br>Member quit</p>                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsadded"><strong>onAdminsAdded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>New Admin added</p>                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onadminsremoved"><strong>onAdminsRemoved</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String reason)<br>Admin removed</p>                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onownerassigned"><strong>onOwnerAssigned</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Become group Owner</p>                                                              |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate"><strong>onGroupInfoUpdate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.UpdateInfoType type)<br>Group information changes</p>                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname"><strong>onMemberChangeNickName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long memberId, String nickName)<br>Member nickname changed</p>           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate"><strong>onAnnouncementUpdate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.Announcement announcement)<br>Group announcement updated</p>        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded"><strong>onSharedFileUploaded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>Shared file received</p>                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted"><strong>onSharedFileDeleted</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>Shared file deleted</p>                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated"><strong>onSharedFileUpdated</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>Name of shared file updated</p>             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Add to blacklist</p>                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Delete blacklist</p>                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>()<br>Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information</p> |
|                   | [**BMXGroupServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-bmxgroupservicelistener)()                                                                                                                                                                 |
| void              | [**registerGroupService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-registergroupservice)([BMXGroupService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md) service)                                                                            |

## Protected Functions

|      | Name                                                                                                                                                                                                                  |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-bmxgroupservicelistener)(long cPtr, boolean cMemoryOwn)                                             |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-finalize)()                                                                                                        |
| void | [**swigDirectorDisconnect**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-swigdirectordisconnect)()                                                                            |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#function-getcptr)([BMXGroupServiceListener](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service\_listener.md#variable-swigcmemown) |

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

Create a group

**Parameters**:

* **group** Newly created group

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

Group list updated

**Parameters**:

* **list** Updated group list

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

Join a group

**Parameters**:

* **group** Group to join

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

Quit a group

**Parameters**:

* **group** Group to quit
* **reason** Quit reason

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

Group invitation received

**Parameters**:

* **groupId** Group id invited to
* **inviter** Inviter id
* **message** Invitation reason

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

Group invitation accepted

**Parameters**:

* **group** A group in which invitation approved
* **inviteeId** Invitee id

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

Join group rejected

**Parameters**:

* **group** A group in which invitation rejected
* **inviteeId** Invitee id
* **reason** Rejection reason

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

Group membership application received

**Parameters**:

* **group** A group in which received membership application
* **applicantId** Applicant id
* **message** Application reason

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

Join group accepted

**Parameters**:

* **group** Group where membership application was accepted
* **approver** Approver of the application

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

Join group rejected

**Parameters**:

* **group** Group where membership application was rejected
* **approver** Approver of the application
* **reason** Reason for rejection

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

Member banned

**Parameters**:

* **group** Group with member banned
* **members** List of banned member ids
* **duration** Duration of banned

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

Member unbanned

**Parameters**:

* **group** Group with member unbanned
* **members** List of unbanned group member ids

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

New member added

**Parameters**:

* **group** Group with new member added
* **memberId** ID of added member
* **inviter** Inviter id

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

Member quit

**Parameters**:

* **group** Group with member quitting
* **memberId** ID of quitted member
* **reason** Reason for quitting

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

New Admin added

**Parameters**:

* **group** Group where addition of new Admin occurred
* **members** List of members promoted to Admins

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

Admin removed

**Parameters**:

* **group** Group where Admin removal occurred
* **members** List of members degraded from Admins
* **reason** Reason for removal

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

Become group Owner

**Parameters**:

* **group** A group in which group Owner transferred

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

Group information changes

**Parameters**:

* **group** Group with group information changed
* **type** Type of group information that changed

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

Member nickname changed

**Parameters**:

* **group** A group in which member nickname changed
* **memberId** Group member id that changed group nickname
* **nickName** Changed group nickname

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

Group announcement updated

**Parameters**:

* **group** Group where announcement update occurred
* **announcement** Latest group announcement after changed

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

Shared file received

**Parameters**:

* **group** A group in which shared file uploading occurred
* **sharedFile** Newly uploaded group shared file

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

Shared file deleted

**Parameters**:

* **group** A group in which shared file deleted
* **sharedFile** Deleted group shared file

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

Name of shared file updated

**Parameters**:

* **group** A group in which share file updated
* **sharedFile** Updated group shared file

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

Add to blacklist

**Parameters**:

* **group** Group with blacklist added
* **members** List of blacklisted members

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

Delete blacklist

**Parameters**:

* **group** Group with blacklist removed
* **members** List of unblacklisted members

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupServiceListener'></div>
```

### function onGroupListUpdate

```java
inline void onGroupListUpdate()
```

Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information

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



Updated on 2022-01-26 at 17:18:31 +0800
