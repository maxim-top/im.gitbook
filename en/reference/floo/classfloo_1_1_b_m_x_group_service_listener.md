---
title: floo::BMXGroupServiceListener
summary: Group change listener
---

# floo::BMXGroupServiceListener

Group change listener

`#include <bmx_group_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                                                       |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener"><strong>BMXGroupServiceListener</strong></a>()<br>Constructor</p>                                                                                                                                                              |
| virtual      | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-~bmxgroupservicelistener"><strong>~BMXGroupServiceListener</strong></a>()<br>Destructor</p>                                                                                                                                                             |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupcreate"><strong>onGroupCreate</strong></a>(BMXGroupPtr group)<br>Create a group</p>                                                                                                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>(const BMXGroupList &#x26; list)<br>Group list updated</p>                                                                                                                                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupjoined"><strong>onGroupJoined</strong></a>(BMXGroupPtr group)<br>Join a group</p>                                                                                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupleft"><strong>onGroupLeft</strong></a>(BMXGroupPtr group, const std::string &#x26; reason)<br>Quit a group</p>                                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitated"><strong>onInvitated</strong></a>(int64_t groupId, int64_t inviter, const std::string &#x26; message)<br>Group invitation received</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted"><strong>onInvitationAccepted</strong></a>(BMXGroupPtr group, int64_t inviteeId)<br>Group invitation accepted</p>                                                                                                                  |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined"><strong>onInvitationDeclined</strong></a>(BMXGroupPtr group, int64_t inviteeId, const std::string &#x26; reason)<br>Join group rejected</p>                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(BMXGroupPtr group, int64_t applicantId, const std::string &#x26; message)<br>Group membership application received</p>                                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(BMXGroupPtr group, int64_t approver)<br>Join group accepted</p>                                                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(BMXGroupPtr group, int64_t approver, const std::string &#x26; reason)<br>Join group rejected</p>                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersbanned"><strong>onMembersBanned</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members, int64_t duration)<br>Member banned</p>                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned"><strong>onMembersUnbanned</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>Member unbanned</p>                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberjoined"><strong>onMemberJoined</strong></a>(BMXGroupPtr group, int64_t memberId, int64_t inviter)<br>New member added</p>                                                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberleft"><strong>onMemberLeft</strong></a>(BMXGroupPtr group, int64_t memberId, const std::string &#x26; reason)<br>Member quit</p>                                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsadded"><strong>onAdminsAdded</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>New Admin added</p>                                                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsremoved"><strong>onAdminsRemoved</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members, const std::string &#x26; reason)<br>Admin removed</p>                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onownerassigned"><strong>onOwnerAssigned</strong></a>(BMXGroupPtr group)<br>Become group Owner</p>                                                                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate"><strong>onGroupInfoUpdate</strong></a>(BMXGroupPtr group, <a href="classfloo_1_1_b_m_x_group.md#enum-updateinfotype">BMXGroup::UpdateInfoType</a> type)<br>Group information changes</p>                                             |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname"><strong>onMemberChangeNickName</strong></a>(BMXGroupPtr group, int64_t memberId, const std::string &#x26; nickName)<br>Member nickname changed</p>                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate"><strong>onAnnouncementUpdate</strong></a>(BMXGroupPtr group, BMXGroup::AnnouncementPtr announcement)<br>Group announcement updated</p>                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded"><strong>onSharedFileUploaded</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Shared file received</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted"><strong>onSharedFileDeleted</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Shared file deleted</p>                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated"><strong>onSharedFileUpdated</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Name of shared file updated</p>                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>Add to blacklist</p>                                                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>Delete blacklist</p>                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>()<br>Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information</p>                                |
| void         | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-registergroupservice"><strong>registerGroupService</strong></a>(<a href="classfloo_1_1_b_m_x_group_service.md">BMXGroupService</a> * service)<br>Register BMXGroupService to which BMXGroupServiceListener is bound (automatic registration in SDK)</p> |

## Protected Attributes

|                                                            | Name                                                                            |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) \* | [**mService**](classfloo_1_1_b_m_x_group_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXGroupServiceListener

```cpp
inline BMXGroupServiceListener()
```

Constructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function \~BMXGroupServiceListener

```cpp
inline virtual ~BMXGroupServiceListener()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupCreate

```cpp
inline virtual void onGroupCreate(
    BMXGroupPtr group
)
```

Create a group

**Parameters**:

* **group** Newly created group

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```cpp
inline virtual void onGroupListUpdate(
    const BMXGroupList & list
)
```

Group list updated

**Parameters**:

* **list** Updated group list

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupJoined

```cpp
inline virtual void onGroupJoined(
    BMXGroupPtr group
)
```

Join a group

**Parameters**:

* **group** Group to join

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupLeft

```cpp
inline virtual void onGroupLeft(
    BMXGroupPtr group,
    const std::string & reason
)
```

Quit a group

**Parameters**:

* **group** Group to quit
* **reason** Quit reason

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitated

```cpp
inline virtual void onInvitated(
    int64_t groupId,
    int64_t inviter,
    const std::string & message
)
```

Group invitation received

**Parameters**:

* **groupId** Group id invited to
* **inviter** Inviter id
* **message** Invitation reason

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationAccepted

```cpp
inline virtual void onInvitationAccepted(
    BMXGroupPtr group,
    int64_t inviteeId
)
```

Group invitation accepted

**Parameters**:

* **group** A group in which invitation approved
* **inviteeId** Invitee id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationDeclined

```cpp
inline virtual void onInvitationDeclined(
    BMXGroupPtr group,
    int64_t inviteeId,
    const std::string & reason
)
```

Join group rejected

**Parameters**:

* **group** A group in which invitation rejected
* **inviteeId** Invitee id
* **reason** Rejection reason

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplied

```cpp
inline virtual void onApplied(
    BMXGroupPtr group,
    int64_t applicantId,
    const std::string & message
)
```

Group membership application received

**Parameters**:

* **group** A group in which received membership application
* **applicantId** Applicant id
* **message** Application reason

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationAccepted

```cpp
inline virtual void onApplicationAccepted(
    BMXGroupPtr group,
    int64_t approver
)
```

Join group accepted

**Parameters**:

* **group** Group where membership application was accepted
* **approver** Approver of the application

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationDeclined

```cpp
inline virtual void onApplicationDeclined(
    BMXGroupPtr group,
    int64_t approver,
    const std::string & reason
)
```

Join group rejected

**Parameters**:

* **group** Group where membership application was rejected
* **approver** Approver of the application
* **reason** Reason for rejection

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMembersBanned

```cpp
inline virtual void onMembersBanned(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    int64_t duration
)
```

Member banned

**Parameters**:

* **group** Group with member banned
* **members** List of banned member ids
* **duration** Duration of banned

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMembersUnbanned

```cpp
inline virtual void onMembersUnbanned(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

Member unbanned

**Parameters**:

* **group** Group with member unbanned
* **members** List of unbanned group member ids

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberJoined

```cpp
inline virtual void onMemberJoined(
    BMXGroupPtr group,
    int64_t memberId,
    int64_t inviter
)
```

New member added

**Parameters**:

* **group** Group with new member added
* **memberId** ID of added member
* **inviter** Inviter id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberLeft

```cpp
inline virtual void onMemberLeft(
    BMXGroupPtr group,
    int64_t memberId,
    const std::string & reason
)
```

Member quit

**Parameters**:

* **group** Group with member quitting
* **memberId** ID of quitted member
* **reason** Reason for quitting

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsAdded

```cpp
inline virtual void onAdminsAdded(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

New Admin added

**Parameters**:

* **group** Group where addition of new Admin occurred
* **members** List of members promoted to Admins

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsRemoved

```cpp
inline virtual void onAdminsRemoved(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    const std::string & reason
)
```

Admin removed

**Parameters**:

* **group** Group where Admin removal occurred
* **members** List of members degraded from Admins
* **reason** Reason for removal

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onOwnerAssigned

```cpp
inline virtual void onOwnerAssigned(
    BMXGroupPtr group
)
```

Become group Owner

**Parameters**:

* **group** A group in which group Owner transferred

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupInfoUpdate

```cpp
inline virtual void onGroupInfoUpdate(
    BMXGroupPtr group,
    BMXGroup::UpdateInfoType type
)
```

Group information changes

**Parameters**:

* **group** Group with group information changed
* **type** Type of group information that changed

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberChangeNickName

```cpp
inline virtual void onMemberChangeNickName(
    BMXGroupPtr group,
    int64_t memberId,
    const std::string & nickName
)
```

Member nickname changed

**Parameters**:

* **group** A group in which member nickname changed
* **memberId** Group member id that changed group nickname
* **nickName** Changed group nickname

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAnnouncementUpdate

```cpp
inline virtual void onAnnouncementUpdate(
    BMXGroupPtr group,
    BMXGroup::AnnouncementPtr announcement
)
```

Group announcement updated

**Parameters**:

* **group** Group where announcement update occurred
* **announcement** Latest group announcement after changed

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUploaded

```cpp
inline virtual void onSharedFileUploaded(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

Shared file received

**Parameters**:

* **group** A group in which shared file uploading occurred
* **sharedFile** Newly uploaded group shared file

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileDeleted

```cpp
inline virtual void onSharedFileDeleted(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

Shared file deleted

**Parameters**:

* **group** A group in which shared file deleted
* **sharedFile** Deleted group shared file

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUpdated

```cpp
inline virtual void onSharedFileUpdated(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

Name of shared file updated

**Parameters**:

* **group** A group in which share file updated
* **sharedFile** Updated group shared file

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListAdded

```cpp
inline virtual void onBlockListAdded(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

Add to blacklist

**Parameters**:

* **group** Group with blacklist added
* **members** List of blacklisted members

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListRemoved

```cpp
inline virtual void onBlockListRemoved(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

Delete blacklist

**Parameters**:

* **group** Group with blacklist removed
* **members** List of unblacklisted members

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```cpp
inline virtual void onGroupListUpdate()
```

Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function registerGroupService

```cpp
inline void registerGroupService(
    BMXGroupService * service
)
```

Register BMXGroupService to which BMXGroupServiceListener is bound (automatic registration in SDK)

**Parameters**:

* **service** [BMXGroupService](classfloo_1_1_b_m_x_group_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXGroupService * mService;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
