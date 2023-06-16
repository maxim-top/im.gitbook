---
title: floo::BMXGroupServiceListener
summary: Group change listener 

---

# floo::BMXGroupServiceListener



Group change listener 


`#include <bmx_group_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupServiceListener](classfloo_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener)**()<br>Constructor  |
| virtual | **[~BMXGroupServiceListener](classfloo_1_1_b_m_x_group_service_listener.md#function-~bmxgroupservicelistener)**()<br>Destructor  |
| virtual void | **[onGroupCreate](classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupcreate)**(BMXGroupPtr group)<br>Create a group  |
| virtual void | **[onGroupListUpdate](classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**(const BMXGroupList & list)<br>Group list updated  |
| virtual void | **[onGroupJoined](classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupjoined)**(BMXGroupPtr group)<br>Join a group  |
| virtual void | **[onGroupLeft](classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupleft)**(BMXGroupPtr group, const std::string & reason)<br>Quit a group  |
| virtual void | **[onInvitated](classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitated)**(int64_t groupId, int64_t inviter, const std::string & message)<br>Group invitation received  |
| virtual void | **[onInvitationAccepted](classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted)**(BMXGroupPtr group, int64_t inviteeId)<br>Group invitation accepted  |
| virtual void | **[onInvitationDeclined](classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined)**(BMXGroupPtr group, int64_t inviteeId, const std::string & reason)<br>Join group rejected  |
| virtual void | **[onApplied](classfloo_1_1_b_m_x_group_service_listener.md#function-onapplied)**(BMXGroupPtr group, int64_t applicantId, const std::string & message)<br>Group membership application received  |
| virtual void | **[onApplicationAccepted](classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted)**(BMXGroupPtr group, int64_t approver)<br>Join group accepted  |
| virtual void | **[onApplicationDeclined](classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined)**(BMXGroupPtr group, int64_t approver, const std::string & reason)<br>Join group rejected  |
| virtual void | **[onMembersBanned](classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersbanned)**(BMXGroupPtr group, const std::vector< int64_t > & members, int64_t duration)<br>Member banned  |
| virtual void | **[onMembersUnbanned](classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned)**(BMXGroupPtr group, const std::vector< int64_t > & members)<br>Member unbanned  |
| virtual void | **[onMemberJoined](classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberjoined)**(BMXGroupPtr group, int64_t memberId, int64_t inviter)<br>New member added  |
| virtual void | **[onMemberLeft](classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberleft)**(BMXGroupPtr group, int64_t memberId, const std::string & reason)<br>Member quit  |
| virtual void | **[onAdminsAdded](classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsadded)**(BMXGroupPtr group, const std::vector< int64_t > & members)<br>New Admin added  |
| virtual void | **[onAdminsRemoved](classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsremoved)**(BMXGroupPtr group, const std::vector< int64_t > & members, const std::string & reason)<br>Admin removed  |
| virtual void | **[onOwnerAssigned](classfloo_1_1_b_m_x_group_service_listener.md#function-onownerassigned)**(BMXGroupPtr group)<br>Become group Owner  |
| virtual void | **[onGroupInfoUpdate](classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate)**(BMXGroupPtr group, [BMXGroup::UpdateInfoType](classfloo_1_1_b_m_x_group.md#enum-updateinfotype) type)<br>Group information changes  |
| virtual void | **[onMemberChangeNickName](classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname)**(BMXGroupPtr group, int64_t memberId, const std::string & nickName)<br>Member nickname changed  |
| virtual void | **[onAnnouncementUpdate](classfloo_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate)**(BMXGroupPtr group, BMXGroup::AnnouncementPtr announcement)<br>Group announcement updated  |
| virtual void | **[onSharedFileUploaded](classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Shared file received  |
| virtual void | **[onSharedFileDeleted](classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Shared file deleted  |
| virtual void | **[onSharedFileUpdated](classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>Name of shared file updated  |
| virtual void | **[onBlockListAdded](classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistadded)**(BMXGroupPtr group, const std::vector< int64_t > & members)<br>Add to blacklist  |
| virtual void | **[onBlockListRemoved](classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved)**(BMXGroupPtr group, const std::vector< int64_t > & members)<br>Delete blacklist  |
| virtual void | **[onGroupListUpdate](classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate)**()<br>Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information  |
| void | **[registerGroupService](classfloo_1_1_b_m_x_group_service_listener.md#function-registergroupservice)**([BMXGroupService](classfloo_1_1_b_m_x_group_service.md) * service)<br>Register BMXGroupService to which BMXGroupServiceListener is bound (automatic registration in SDK)  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) * | **[mService](classfloo_1_1_b_m_x_group_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXGroupServiceListener

```cpp
inline BMXGroupServiceListener()
```

Constructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="BMXGroupServiceListener" %}{% endlanying_code_snippet %}
```
### function ~BMXGroupServiceListener

```cpp
inline virtual ~BMXGroupServiceListener()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="~BMXGroupServiceListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupCreate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupListUpdate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupJoined" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupLeft" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onInvitated" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onInvitationAccepted" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onInvitationDeclined" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onApplied" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onApplicationAccepted" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onApplicationDeclined" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onMembersBanned" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onMembersUnbanned" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onMemberJoined" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onMemberLeft" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onAdminsAdded" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onAdminsRemoved" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onOwnerAssigned" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupInfoUpdate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onMemberChangeNickName" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onAnnouncementUpdate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onSharedFileUploaded" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onSharedFileDeleted" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onSharedFileUpdated" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onBlockListAdded" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onBlockListRemoved" %}{% endlanying_code_snippet %}
```
### function onGroupListUpdate

```cpp
inline virtual void onGroupListUpdate()
```

Triggered when client pulls a new group from server, used to update user group list, and call local fetching group via SDK for all member information 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="onGroupListUpdate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXGroupServiceListener",function="registerGroupService" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800