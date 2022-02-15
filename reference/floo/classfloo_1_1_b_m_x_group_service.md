---
title: floo::BMXGroupService
summary: Group Service 

---

# floo::BMXGroupService



Group Service 


`#include <bmx_group_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(int percent)> | **[Callback](classfloo_1_1_b_m_x_group_service.md#typedef-callback)**  |
| typedef std::shared_ptr< [CreateGroupOptions] > | **[CreateGroupOptionsPtr](classfloo_1_1_b_m_x_group_service.md#typedef-creategroupoptionsptr)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXGroupService](classfloo_1_1_b_m_x_group_service.md#function-~bmxgroupservice)**() |
| virtual BMXErrorCode | **[get](classfloo_1_1_b_m_x_group_service.md#function-get)**(BMXGroupList & list, bool forceRefresh) =0<br>Get group list, pull from server if forceRefreshed is set  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList & list, bool forceRefresh) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchGroupsByIdList](classfloo_1_1_b_m_x_group_service.md#function-fetchgroupsbyidlist)**(const std::vector< int64_t > & groupIdList, BMXGroupList & list, bool forceRefresh) =0<br>Get a list of group information from the ID list passed in to group, or pull from server if forceRefresh is set  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_group_service.md#function-search)**(const std::vector< int64_t > & groupIdList, BMXGroupList & list, bool forceRefresh) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchGroupById](classfloo_1_1_b_m_x_group_service.md#function-fetchgroupbyid)**(int64_t groupId, BMXGroupPtr & group, bool forceRefresh) =0<br>Get group information by group id, or pull from server if forceRefresh is set  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_group_service.md#function-search)**(int64_t groupId, BMXGroupPtr & group, bool forceRefresh) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchLocalGroupsByName](classfloo_1_1_b_m_x_group_service.md#function-fetchlocalgroupsbyname)**(BMXGroupList & list, const std::string & name) =0<br>Query local group information by group name and retrieve the group from local database by group name query  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList & list, const std::string & name) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[create](classfloo_1_1_b_m_x_group_service.md#function-create)**(const [CreateGroupOptions] & options, BMXGroupPtr & group) =0<br>Create group  |
| virtual BMXErrorCode | **[destroy](classfloo_1_1_b_m_x_group_service.md#function-destroy)**(BMXGroupPtr group) =0<br>Destroy group  |
| virtual BMXErrorCode | **[join](classfloo_1_1_b_m_x_group_service.md#function-join)**(BMXGroupPtr group, const std::string & message) =0<br>Join a group, which may require admin approval depending on group settings  |
| virtual BMXErrorCode | **[leave](classfloo_1_1_b_m_x_group_service.md#function-leave)**(BMXGroupPtr group) =0<br>Quit group  |
| virtual BMXErrorCode | **[getInfo](classfloo_1_1_b_m_x_group_service.md#function-getinfo)**(BMXGroupPtr group) =0<br>Get group details, pull the latest information from server  |
| virtual BMXErrorCode | **[getMembersNickname](classfloo_1_1_b_m_x_group_service.md#function-getmembersnickname)**(BMXGroupPtr group, const std::vector< int64_t > & members, BMXGroup::MemberList & list) =0<br>Get group member details  |
| virtual BMXErrorCode | **[getInvitationList](classfloo_1_1_b_m_x_group_service.md#function-getinvitationlist)**(BMXGroupInvitationPagePtr & result, const std::string & cursor ="", int pageSize =10) =0<br>Get group invitation list in pages  |
| virtual BMXErrorCode | **[getApplicationList](classfloo_1_1_b_m_x_group_service.md#function-getapplicationlist)**(BMXGroupList list, BMXGroupApplicationPagePtr & result, const std::string & cursor ="", int pageSize =10) =0<br>Get a list of group applications in pages  |
| virtual BMXErrorCode | **[getMembers](classfloo_1_1_b_m_x_group_service.md#function-getmembers)**(BMXGroupPtr group, BMXGroupMemberResultPagePtr & result, const std::string & cursor ="", int pageSize =200) =0<br>Get list of group members in pages, pull from server if forceRefresh is set, up to 500 per page.  |
| virtual BMXErrorCode | **[getMembers](classfloo_1_1_b_m_x_group_service.md#function-getmembers)**(BMXGroupPtr group, BMXGroup::MemberList & list, bool forceRefresh) =0<br>Get group member list, pull from server if forceRefresh is set, up to 1,000  |
| virtual BMXErrorCode | **[addMembers](classfloo_1_1_b_m_x_group_service.md#function-addmembers)**(BMXGroupPtr group, const std::vector< int64_t > & members, const std::string & message) =0<br>Add group member  |
| virtual BMXErrorCode | **[removeMembers](classfloo_1_1_b_m_x_group_service.md#function-removemembers)**(BMXGroupPtr group, const std::vector< int64_t > & members, const std::string & reason) =0<br>Remove group member  |
| virtual BMXErrorCode | **[addAdmins](classfloo_1_1_b_m_x_group_service.md#function-addadmins)**(BMXGroupPtr group, const std::vector< int64_t > & admins, const std::string & message) =0<br>Add Admin  |
| virtual BMXErrorCode | **[removeAdmins](classfloo_1_1_b_m_x_group_service.md#function-removeadmins)**(BMXGroupPtr group, const std::vector< int64_t > & admins, const std::string & reason) =0<br>Remove admin  |
| virtual BMXErrorCode | **[getAdmins](classfloo_1_1_b_m_x_group_service.md#function-getadmins)**(BMXGroupPtr group, BMXGroup::MemberList & list, bool forceRefresh) =0<br>Get Admins list, pull from server if forceRefreshed is set  |
| virtual BMXErrorCode | **[blockMembers](classfloo_1_1_b_m_x_group_service.md#function-blockmembers)**(BMXGroupPtr group, const std::vector< int64_t > & members) =0<br>Add to blacklist  |
| virtual BMXErrorCode | **[unblockMembers](classfloo_1_1_b_m_x_group_service.md#function-unblockmembers)**(BMXGroupPtr group, const std::vector< int64_t > & members) =0<br>Unblacklist  |
| virtual BMXErrorCode | **[getBlockList](classfloo_1_1_b_m_x_group_service.md#function-getblocklist)**(BMXGroupPtr group, BMXGroupMemberResultPagePtr & result, const std::string & cursor ="", int pageSize =200) =0<br>Paged to get blacklist  |
| virtual BMXErrorCode | **[getBlockList](classfloo_1_1_b_m_x_group_service.md#function-getblocklist)**(BMXGroupPtr group, BMXGroup::MemberList & list, bool forceRefresh) =0<br>Get blacklist  |
| virtual BMXErrorCode | **[banMembers](classfloo_1_1_b_m_x_group_service.md#function-banmembers)**(BMXGroupPtr group, const std::vector< int64_t > & members, int64_t duration, const std::string & reason ="") =0<br>Ban  |
| virtual BMXErrorCode | **[banGroup](classfloo_1_1_b_m_x_group_service.md#function-bangroup)**(BMXGroupPtr group, int64_t duration) =0<br>Ban all members, the expiration time is calculated from the current server time plus banning duration (only Admins and group Owner can speak in the duration)  |
| virtual BMXErrorCode | **[unbanMembers](classfloo_1_1_b_m_x_group_service.md#function-unbanmembers)**(BMXGroupPtr group, const std::vector< int64_t > & members) =0<br>Unban  |
| virtual BMXErrorCode | **[unbanGroup](classfloo_1_1_b_m_x_group_service.md#function-unbangroup)**(BMXGroupPtr group) =0<br>Unban all members  |
| virtual BMXErrorCode | **[getBannedMembers](classfloo_1_1_b_m_x_group_service.md#function-getbannedmembers)**(BMXGroupPtr group, BMXGroupBannedMemberResultPagePtr & result, const std::string & cursor ="", int pageSize =200) =0<br>Paged to get ban list  |
| virtual BMXErrorCode | **[getBannedMembers](classfloo_1_1_b_m_x_group_service.md#function-getbannedmembers)**(BMXGroupPtr group, BMXGroup::BannedMemberList & list) =0<br>Get a list of banned members  |
| virtual BMXErrorCode | **[muteMessage](classfloo_1_1_b_m_x_group_service.md#function-mutemessage)**(BMXGroupPtr group, [BMXGroup::MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode) mode) =0<br>Set whether to block group messages  |
| virtual BMXErrorCode | **[acceptApplication](classfloo_1_1_b_m_x_group_service.md#function-acceptapplication)**(BMXGroupPtr group, int64_t applicantId) =0<br>Accept application of membership  |
| virtual BMXErrorCode | **[declineApplication](classfloo_1_1_b_m_x_group_service.md#function-declineapplication)**(BMXGroupPtr group, int64_t applicantId, const std::string & reason ="") =0<br>Reject application of membership  |
| virtual BMXErrorCode | **[acceptInvitation](classfloo_1_1_b_m_x_group_service.md#function-acceptinvitation)**(BMXGroupPtr group, int64_t inviter) =0<br>Accept to join group  |
| virtual BMXErrorCode | **[declineInvitation](classfloo_1_1_b_m_x_group_service.md#function-declineinvitation)**(BMXGroupPtr group, int64_t inviter, const std::string & reason ="") =0<br>Reject invitation to join group  |
| virtual BMXErrorCode | **[transferOwner](classfloo_1_1_b_m_x_group_service.md#function-transferowner)**(BMXGroupPtr group, int64_t newOwnerId) =0<br>Transfer of group Owner  |
| virtual BMXErrorCode | **[uploadSharedFile](classfloo_1_1_b_m_x_group_service.md#function-uploadsharedfile)**(BMXGroupPtr group, const std::string & filePath, const std::string & displayName, const std::string & extensionName, Callback ) =0<br>Add shared file in group  |
| virtual BMXErrorCode | **[cancelUploadSharedFile](classfloo_1_1_b_m_x_group_service.md#function-canceluploadsharedfile)**(BMXGroupPtr group, const std::string & filePath) =0<br>Cancel uploading group shared files  |
| virtual BMXErrorCode | **[removeSharedFile](classfloo_1_1_b_m_x_group_service.md#function-removesharedfile)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile) =0<br>Remove shared file in group  |
| virtual BMXErrorCode | **[downloadSharedFile](classfloo_1_1_b_m_x_group_service.md#function-downloadsharedfile)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile, Callback ) =0<br>Download share file in group  |
| virtual BMXErrorCode | **[cancelDownloadSharedFile](classfloo_1_1_b_m_x_group_service.md#function-canceldownloadsharedfile)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile) =0<br>Cancel downloading group shared files  |
| virtual BMXErrorCode | **[getSharedFilesList](classfloo_1_1_b_m_x_group_service.md#function-getsharedfileslist)**(BMXGroupPtr group, BMXGroup::SharedFileList & list, bool forceRefresh) =0<br>Get a list of share files in group  |
| virtual BMXErrorCode | **[changeSharedFileName](classfloo_1_1_b_m_x_group_service.md#function-changesharedfilename)**(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile, const std::string & name) =0<br>Modify shared file name in group  |
| virtual BMXErrorCode | **[getLatestAnnouncement](classfloo_1_1_b_m_x_group_service.md#function-getlatestannouncement)**(BMXGroupPtr group, BMXGroup::AnnouncementPtr & announcement, bool forceRefresh) =0<br>Get the latest group announcement  |
| virtual BMXErrorCode | **[getAnnouncementList](classfloo_1_1_b_m_x_group_service.md#function-getannouncementlist)**(BMXGroupPtr group, BMXGroup::AnnouncementList & list, bool forceRefresh) =0<br>Get group announcements list  |
| virtual BMXErrorCode | **[editAnnouncement](classfloo_1_1_b_m_x_group_service.md#function-editannouncement)**(BMXGroupPtr group, const std::string & title, const std::string & content) =0<br>Write group announcement  |
| virtual BMXErrorCode | **[deleteAnnouncement](classfloo_1_1_b_m_x_group_service.md#function-deleteannouncement)**(BMXGroupPtr group, int64_t announcementId) =0<br>Delete group announcement  |
| virtual BMXErrorCode | **[setName](classfloo_1_1_b_m_x_group_service.md#function-setname)**(BMXGroupPtr group, const std::string & name) =0<br>Set group name  |
| virtual BMXErrorCode | **[setDescription](classfloo_1_1_b_m_x_group_service.md#function-setdescription)**(BMXGroupPtr group, const std::string & description) =0<br>Set group description  |
| virtual BMXErrorCode | **[setExtension](classfloo_1_1_b_m_x_group_service.md#function-setextension)**(BMXGroupPtr group, const std::string & extension) =0<br>Set group extension information  |
| virtual BMXErrorCode | **[setMyNickname](classfloo_1_1_b_m_x_group_service.md#function-setmynickname)**(BMXGroupPtr group, const std::string & nickname) =0<br>Set nickname in group  |
| virtual BMXErrorCode | **[setMsgPushMode](classfloo_1_1_b_m_x_group_service.md#function-setmsgpushmode)**(BMXGroupPtr group, [BMXGroup::MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode) mode) =0<br>Set group message notification mode  |
| virtual BMXErrorCode | **[setJoinAuthMode](classfloo_1_1_b_m_x_group_service.md#function-setjoinauthmode)**(BMXGroupPtr group, [BMXGroup::JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode) mode) =0<br>Set approval mode for joining group  |
| virtual BMXErrorCode | **[setInviteMode](classfloo_1_1_b_m_x_group_service.md#function-setinvitemode)**(BMXGroupPtr group, [BMXGroup::InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode) mode) =0<br>Set invitation mode  |
| virtual BMXErrorCode | **[setAllowMemberModify](classfloo_1_1_b_m_x_group_service.md#function-setallowmembermodify)**(BMXGroupPtr group, bool enable) =0<br>Set whether group members are allowed to set group information  |
| virtual BMXErrorCode | **[setEnableReadAck](classfloo_1_1_b_m_x_group_service.md#function-setenablereadack)**(BMXGroupPtr group, bool enable) =0<br>Set whether group message read acknowledgement is enabled  |
| virtual BMXErrorCode | **[setHistoryVisible](classfloo_1_1_b_m_x_group_service.md#function-sethistoryvisible)**(BMXGroupPtr group, bool enable) =0<br>Set whether group members are allowed to enable visible message history  |
| virtual BMXErrorCode | **[setAvatar](classfloo_1_1_b_m_x_group_service.md#function-setavatar)**(BMXGroupPtr group, const std::string & avatarPath, Callback ) =0<br>Set group avatar  |
| virtual BMXErrorCode | **[downloadAvatar](classfloo_1_1_b_m_x_group_service.md#function-downloadavatar)**(BMXGroupPtr group, bool thumbnail, Callback callback) =0<br>Download group avatar  |
| virtual void | **[addGroupListener](classfloo_1_1_b_m_x_group_service.md#function-addgrouplistener)**([BMXGroupServiceListener](classfloo_1_1_b_m_x_group_service_listener.md) * listener) =0<br>Add group change listener  |
| virtual void | **[removeGroupListener](classfloo_1_1_b_m_x_group_service.md#function-removegrouplistener)**([BMXGroupServiceListener](classfloo_1_1_b_m_x_group_service_listener.md) * listener) =0<br>Remove group change listener  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupService](classfloo_1_1_b_m_x_group_service.md#function-bmxgroupservice)**() |

## Public Types Documentation

### typedef Callback

```cpp
typedef std::function<void(int percent)> floo::BMXGroupService::Callback;
```


### typedef CreateGroupOptionsPtr

```cpp
typedef std::shared_ptr<CreateGroupOptions> floo::BMXGroupService::CreateGroupOptionsPtr;
```


## Public Functions Documentation

### function ~BMXGroupService

```cpp
inline virtual ~BMXGroupService()
```


### function get

```cpp
virtual BMXErrorCode get(
    BMXGroupList & list,
    bool forceRefresh
) =0
```

Get group list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **list** List of group ids, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function search

```cpp
virtual BMXErrorCode search(
    BMXGroupList & list,
    bool forceRefresh
) =0
```

Deprecated. 

**Parameters**: 

  * **list** List of group ids, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

use get instead.

Get group list, pull from server if forceRefreshed is set 


### function fetchGroupsByIdList

```cpp
virtual BMXErrorCode fetchGroupsByIdList(
    const std::vector< int64_t > & groupIdList,
    BMXGroupList & list,
    bool forceRefresh
) =0
```

Get a list of group information from the ID list passed in to group, or pull from server if forceRefresh is set 

**Parameters**: 

  * **groupIdList** List of group ids 
  * **list** List of group details, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function search

```cpp
virtual BMXErrorCode search(
    const std::vector< int64_t > & groupIdList,
    BMXGroupList & list,
    bool forceRefresh
) =0
```

Deprecated. 

**Parameters**: 

  * **groupIdList** List of group ids 
  * **list** List of group details, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

use fetchGroupsByIdList instead.

Get the list of group information for the incoming group id, pull from server if forceRefreshed is set 


### function fetchGroupById

```cpp
virtual BMXErrorCode fetchGroupById(
    int64_t groupId,
    BMXGroupPtr & group,
    bool forceRefresh
) =0
```

Get group information by group id, or pull from server if forceRefresh is set 

**Parameters**: 

  * **groupId** Group id to search 
  * **group** Group information returned by search, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function search

```cpp
virtual BMXErrorCode search(
    int64_t groupId,
    BMXGroupPtr & group,
    bool forceRefresh
) =0
```

Deprecated. 

**Parameters**: 

  * **groupId** Group id to search 
  * **group** Group information returned by search, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

use fetchGroupById instead.

Get group information, pull from server if forceRefreshed is set 


### function fetchLocalGroupsByName

```cpp
virtual BMXErrorCode fetchLocalGroupsByName(
    BMXGroupList & list,
    const std::string & name
) =0
```

Query local group information by group name and retrieve the group from local database by group name query 

**Parameters**: 

  * **list** Group list information returned by search result 
  * **name** Keyword of group name for query 


**Return**: BMXErrorCode 

### function search

```cpp
virtual BMXErrorCode search(
    BMXGroupList & list,
    const std::string & name
) =0
```

Deprecated. 

**Parameters**: 

  * **list** Group list information returned by search result 
  * **name** Keyword of group name for query 


**Return**: BMXErrorCode 

use fetchLocalGroupsByName instead.

Query local group information by group name and retrieve the group from local database by group name query 


### function create

```cpp
virtual BMXErrorCode create(
    const CreateGroupOptions & options,
    BMXGroupPtr & group
) =0
```

Create group 

**Parameters**: 

  * **options** Parameters passed in when creating a group 
  * **group** Returned result of creation, pass in a pointing-to-empty objective function shared_ptr and fetch the returned result here 


**Return**: BMXErrorCode 

### function destroy

```cpp
virtual BMXErrorCode destroy(
    BMXGroupPtr group
) =0
```

Destroy group 

**Parameters**: 

  * **group** Group to destroy 


**Return**: BMXErrorCode 

### function join

```cpp
virtual BMXErrorCode join(
    BMXGroupPtr group,
    const std::string & message
) =0
```

Join a group, which may require admin approval depending on group settings 

**Parameters**: 

  * **group** Group to join 
  * **message** Information for group membership application 


**Return**: BMXErrorCode 

### function leave

```cpp
virtual BMXErrorCode leave(
    BMXGroupPtr group
) =0
```

Quit group 

**Parameters**: 

  * **group** Group to quit 


**Return**: BMXErrorCode 

### function getInfo

```cpp
virtual BMXErrorCode getInfo(
    BMXGroupPtr group
) =0
```

Get group details, pull the latest information from server 

**Parameters**: 

  * **group** Group for which the latest information needs to be obtained 


**Return**: BMXErrorCode 

### function getMembersNickname

```cpp
virtual BMXErrorCode getMembersNickname(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    BMXGroup::MemberList & list
) =0
```

Get group member details 

**Parameters**: 

  * **group** Group to operate on 
  * **members** Group member id to get group member details 
  * **list** Returned group member details, pass in an empty list function and fetch the returned list of group member details here 


**Return**: BMXErrorCode 

### function getInvitationList

```cpp
virtual BMXErrorCode getInvitationList(
    BMXGroupInvitationPagePtr & result,
    const std::string & cursor ="",
    int pageSize =10
) =0
```

Get group invitation list in pages 

**Parameters**: 

  * **result** Paged list of group invitations, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

### function getApplicationList

```cpp
virtual BMXErrorCode getApplicationList(
    BMXGroupList list,
    BMXGroupApplicationPagePtr & result,
    const std::string & cursor ="",
    int pageSize =10
) =0
```

Get a list of group applications in pages 

**Parameters**: 

  * **list** List of group ids for which group application list information needs to be obtained 
  * **result** Paged list of group applications, pass in a pointing-to-emtpy shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

### function getMembers

```cpp
virtual BMXErrorCode getMembers(
    BMXGroupPtr group,
    BMXGroupMemberResultPagePtr & result,
    const std::string & cursor ="",
    int pageSize =200
) =0
```

Get list of group members in pages, pull from server if forceRefresh is set, up to 500 per page. 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged list of group members, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

### function getMembers

```cpp
virtual BMXErrorCode getMembers(
    BMXGroupPtr group,
    BMXGroup::MemberList & list,
    bool forceRefresh
) =0
```

Get group member list, pull from server if forceRefresh is set, up to 1,000 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group members, pass in an empty list function and fetch the returned list of group details 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function addMembers

```cpp
virtual BMXErrorCode addMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    const std::string & message
) =0
```

Add group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to join group 
  * **message** Reason for membership application 


**Return**: BMXErrorCode 

### function removeMembers

```cpp
virtual BMXErrorCode removeMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    const std::string & reason
) =0
```

Remove group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of group member ids to delete 
  * **reason** Reason for deletion 


**Return**: BMXErrorCode 

### function addAdmins

```cpp
virtual BMXErrorCode addAdmins(
    BMXGroupPtr group,
    const std::vector< int64_t > & admins,
    const std::string & message
) =0
```

Add Admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to be added as Admins 
  * **message** Reason for adding as Admin 


**Return**: BMXErrorCode 

### function removeAdmins

```cpp
virtual BMXErrorCode removeAdmins(
    BMXGroupPtr group,
    const std::vector< int64_t > & admins,
    const std::string & reason
) =0
```

Remove admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to degrade from Admins 
  * **reason** Reason to degrade from Admin 


**Return**: BMXErrorCode 

### function getAdmins

```cpp
virtual BMXErrorCode getAdmins(
    BMXGroupPtr group,
    BMXGroup::MemberList & list,
    bool forceRefresh
) =0
```

Get Admins list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group Admins, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function blockMembers

```cpp
virtual BMXErrorCode blockMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
) =0
```

Add to blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to be blacklisted 


**Return**: BMXErrorCode 

### function unblockMembers

```cpp
virtual BMXErrorCode unblockMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
) =0
```

Unblacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unblacklisted user ids 


**Return**: BMXErrorCode 

### function getBlockList

```cpp
virtual BMXErrorCode getBlockList(
    BMXGroupPtr group,
    BMXGroupMemberResultPagePtr & result,
    const std::string & cursor ="",
    int pageSize =200
) =0
```

Paged to get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged list of blacklists, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

### function getBlockList

```cpp
virtual BMXErrorCode getBlockList(
    BMXGroupPtr group,
    BMXGroup::MemberList & list,
    bool forceRefresh
) =0
```

Get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group blacklists, pass in an empty list function and fetch the returned list of group details here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function banMembers

```cpp
virtual BMXErrorCode banMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    int64_t duration,
    const std::string & reason =""
) =0
```

Ban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of banned member ids 
  * **duration** Duration of banned 
  * **reason** Reason for banned 


**Return**: BMXErrorCode 

### function banGroup

```cpp
virtual BMXErrorCode banGroup(
    BMXGroupPtr group,
    int64_t duration
) =0
```

Ban all members, the expiration time is calculated from the current server time plus banning duration (only Admins and group Owner can speak in the duration) 

**Parameters**: 

  * **group** Group to operate on 
  * **duration** Banning duration (minute) 


**Return**: BMXErrorCode 

### function unbanMembers

```cpp
virtual BMXErrorCode unbanMembers(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
) =0
```

Unban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unbanned group member ids 


**Return**: BMXErrorCode 

### function unbanGroup

```cpp
virtual BMXErrorCode unbanGroup(
    BMXGroupPtr group
) =0
```

Unban all members 

**Parameters**: 

  * **group** Group to operate on 


**Return**: BMXErrorCode 

### function getBannedMembers

```cpp
virtual BMXErrorCode getBannedMembers(
    BMXGroupPtr group,
    BMXGroupBannedMemberResultPagePtr & result,
    const std::string & cursor ="",
    int pageSize =200
) =0
```

Paged to get ban list 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged ban list, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

### function getBannedMembers

```cpp
virtual BMXErrorCode getBannedMembers(
    BMXGroupPtr group,
    BMXGroup::BannedMemberList & list
) =0
```

Get a list of banned members 

**Parameters**: 

  * **group** Group to operate on 
  * **list** Group ban list, pass in an empty list function and fetch the returned list of group details here 


**Return**: BMXErrorCode 

### function muteMessage

```cpp
virtual BMXErrorCode muteMessage(
    BMXGroupPtr group,
    BMXGroup::MsgMuteMode mode
) =0
```

Set whether to block group messages 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group blocking mode 


**Return**: BMXErrorCode 

### function acceptApplication

```cpp
virtual BMXErrorCode acceptApplication(
    BMXGroupPtr group,
    int64_t applicantId
) =0
```

Accept application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 


**Return**: BMXErrorCode 

### function declineApplication

```cpp
virtual BMXErrorCode declineApplication(
    BMXGroupPtr group,
    int64_t applicantId,
    const std::string & reason =""
) =0
```

Reject application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 
  * **reason** Reason for rejection 


**Return**: BMXErrorCode 

### function acceptInvitation

```cpp
virtual BMXErrorCode acceptInvitation(
    BMXGroupPtr group,
    int64_t inviter
) =0
```

Accept to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 


**Return**: BMXErrorCode 

### function declineInvitation

```cpp
virtual BMXErrorCode declineInvitation(
    BMXGroupPtr group,
    int64_t inviter,
    const std::string & reason =""
) =0
```

Reject invitation to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 
  * **reason** Reason for rejection 


**Return**: BMXErrorCode 

### function transferOwner

```cpp
virtual BMXErrorCode transferOwner(
    BMXGroupPtr group,
    int64_t newOwnerId
) =0
```

Transfer of group Owner 

**Parameters**: 

  * **group** Group to operate on 
  * **newOwnerId** User id that transferred as new group Owner 


**Return**: BMXErrorCode 

### function uploadSharedFile

```cpp
virtual BMXErrorCode uploadSharedFile(
    BMXGroupPtr group,
    const std::string & filePath,
    const std::string & displayName,
    const std::string & extensionName,
    Callback 
) =0
```

Add shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **filePath** Local path of file 
  * **displayName** File display name 
  * **extensionName** File extension name 
  * **Callback** Upload callback function 


**Return**: BMXErrorCode 

### function cancelUploadSharedFile

```cpp
virtual BMXErrorCode cancelUploadSharedFile(
    BMXGroupPtr group,
    const std::string & filePath
) =0
```

Cancel uploading group shared files 

**Parameters**: 

  * **group** Group to operate on 
  * **filePath** Local path of file 


**Return**: BMXErrorCode 

### function removeSharedFile

```cpp
virtual BMXErrorCode removeSharedFile(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
) =0
```

Remove shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Deleted group shared file 


**Return**: BMXErrorCode 

### function downloadSharedFile

```cpp
virtual BMXErrorCode downloadSharedFile(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile,
    Callback 
) =0
```

Download share file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Downloaded group shared files 
  * **Callback** Download callback function 


**Return**: BMXErrorCode 

### function cancelDownloadSharedFile

```cpp
virtual BMXErrorCode cancelDownloadSharedFile(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
) =0
```

Cancel downloading group shared files 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Downloaded group shared files 


**Return**: BMXErrorCode 

### function getSharedFilesList

```cpp
virtual BMXErrorCode getSharedFilesList(
    BMXGroupPtr group,
    BMXGroup::SharedFileList & list,
    bool forceRefresh
) =0
```

Get a list of share files in group 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group shared files, pass in an empty list function and fetch the returned list of group details here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function changeSharedFileName

```cpp
virtual BMXErrorCode changeSharedFileName(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile,
    const std::string & name
) =0
```

Modify shared file name in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Group shared file to change 
  * **name** Modified group shared file name 


**Return**: BMXErrorCode 

### function getLatestAnnouncement

```cpp
virtual BMXErrorCode getLatestAnnouncement(
    BMXGroupPtr group,
    BMXGroup::AnnouncementPtr & announcement,
    bool forceRefresh
) =0
```

Get the latest group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **announcement** Latest group announcement, pass in a pointing-to-empty shared_ptr objective function and fetch the latest group announcement here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function getAnnouncementList

```cpp
virtual BMXErrorCode getAnnouncementList(
    BMXGroupPtr group,
    BMXGroup::AnnouncementList & list,
    bool forceRefresh
) =0
```

Get group announcements list 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group announcements, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: BMXErrorCode 

### function editAnnouncement

```cpp
virtual BMXErrorCode editAnnouncement(
    BMXGroupPtr group,
    const std::string & title,
    const std::string & content
) =0
```

Write group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **title** Tittle of group announcement 
  * **content** Content of group announcement 


**Return**: BMXErrorCode 

### function deleteAnnouncement

```cpp
virtual BMXErrorCode deleteAnnouncement(
    BMXGroupPtr group,
    int64_t announcementId
) =0
```

Delete group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **announcementId** Deleted group announcement id 


**Return**: BMXErrorCode 

### function setName

```cpp
virtual BMXErrorCode setName(
    BMXGroupPtr group,
    const std::string & name
) =0
```

Set group name 

**Parameters**: 

  * **group** Group to operate on 
  * **name** Group name 


**Return**: BMXErrorCode 

### function setDescription

```cpp
virtual BMXErrorCode setDescription(
    BMXGroupPtr group,
    const std::string & description
) =0
```

Set group description 

**Parameters**: 

  * **group** Group to operate on 
  * **description** Group description 


**Return**: BMXErrorCode 

### function setExtension

```cpp
virtual BMXErrorCode setExtension(
    BMXGroupPtr group,
    const std::string & extension
) =0
```

Set group extension information 

**Parameters**: 

  * **group** Group to operate on 
  * **extension** Group extension information 


**Return**: BMXErrorCode 

### function setMyNickname

```cpp
virtual BMXErrorCode setMyNickname(
    BMXGroupPtr group,
    const std::string & nickname
) =0
```

Set nickname in group 

**Parameters**: 

  * **group** Group to operate on 
  * **nickname** My nickname in group 


**Return**: BMXErrorCode 

### function setMsgPushMode

```cpp
virtual BMXErrorCode setMsgPushMode(
    BMXGroupPtr group,
    BMXGroup::MsgPushMode mode
) =0
```

Set group message notification mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group message notification mode 


**Return**: BMXErrorCode 

### function setJoinAuthMode

```cpp
virtual BMXErrorCode setJoinAuthMode(
    BMXGroupPtr group,
    BMXGroup::JoinAuthMode mode
) =0
```

Set approval mode for joining group 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Join approval mode 


**Return**: BMXErrorCode 

### function setInviteMode

```cpp
virtual BMXErrorCode setInviteMode(
    BMXGroupPtr group,
    BMXGroup::InviteMode mode
) =0
```

Set invitation mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group invitation mode 


**Return**: BMXErrorCode 

### function setAllowMemberModify

```cpp
virtual BMXErrorCode setAllowMemberModify(
    BMXGroupPtr group,
    bool enable
) =0
```

Set whether group members are allowed to set group information 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Whether allowed to operate 


**Return**: BMXErrorCode 

### function setEnableReadAck

```cpp
virtual BMXErrorCode setEnableReadAck(
    BMXGroupPtr group,
    bool enable
) =0
```

Set whether group message read acknowledgement is enabled 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Enable or not 


**Return**: BMXErrorCode 

### function setHistoryVisible

```cpp
virtual BMXErrorCode setHistoryVisible(
    BMXGroupPtr group,
    bool enable
) =0
```

Set whether group members are allowed to enable visible message history 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Enable or not 


**Return**: BMXErrorCode 

### function setAvatar

```cpp
virtual BMXErrorCode setAvatar(
    BMXGroupPtr group,
    const std::string & avatarPath,
    Callback 
) =0
```

Set group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **avatarPath** Local path of group avatar file 
  * **Callback** Upload callback function 


**Return**: BMXErrorCode 

### function downloadAvatar

```cpp
virtual BMXErrorCode downloadAvatar(
    BMXGroupPtr group,
    bool thumbnail,
    Callback callback
) =0
```

Download group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **thumbnail** True to download thumbnail, false to download original image 
  * **callback** Download callback function 


**Return**: BMXErrorCode 

### function addGroupListener

```cpp
virtual void addGroupListener(
    BMXGroupServiceListener * listener
) =0
```

Add group change listener 

**Parameters**: 

  * **listener** Group change listener 


### function removeGroupListener

```cpp
virtual void removeGroupListener(
    BMXGroupServiceListener * listener
) =0
```

Remove group change listener 

**Parameters**: 

  * **listener** Group change listener 


## Protected Functions Documentation

### function BMXGroupService

```cpp
inline BMXGroupService()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800