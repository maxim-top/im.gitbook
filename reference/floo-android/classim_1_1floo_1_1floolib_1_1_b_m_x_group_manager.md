---
title: im::floo::floolib::BMXGroupManager
summary: Group Manager 

---

# im::floo::floolib::BMXGroupManager



Group Manager 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bmxgroupmanager)**([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) service) |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final boolean forceRefresh, final BMXDataCallBack< BMXGroupList > callBack)<br>Get group list, pull from server if forceRefreshed is set  |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final ListOfLongLong groupIdList, final boolean forceRefresh, final BMXDataCallBack< BMXGroupList > callBack)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set  |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final long groupId, final boolean forceUpdate, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>Get group information, pull from server if forceRefreshed is set  |
| void | **[getInvitationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinvitationlist)**(final String cursor, final int pageSize, final BMXDataCallBack< GroupInvitaionPage > callBack)<br>Get group invitation list in pages  |
| void | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getapplicationlist)**(final BMXGroupList list, final String cursor, final int pageSize, final BMXDataCallBack< GroupApplicationPage > callBack)<br>Get a list of group applications in pages  |
| void | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-create)**(final BMXGroupService.CreateGroupOptions options, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>Create group  |
| void | **[destroy](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-destroy)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>Destroy group  |
| void | **[join](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-join)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String message, final BMXCallBack callBack)<br>Join a group, which may require admin approval depending on group settings  |
| void | **[leave](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-leave)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>Quit group  |
| void | **[getInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinfo)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>Get group details, pull the latest information from server  |
| void | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupMemberResultPage > callBack)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000  |
| void | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000  |
| void | **[addMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final String message, final BMXCallBack callBack)<br>Add group member  |
| void | **[removeMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removemembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final String reason, final BMXCallBack callBack)<br>Remove group member  |
| void | **[addAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong admins, final String message, final BMXCallBack callBack)<br>Add Admin  |
| void | **[removeAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removeadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong admins, final String reason, final BMXCallBack callBack)<br>Remove admin  |
| void | **[getAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>Get Admins list, pull from server if forceRefreshed is set  |
| void | **[blockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-blockmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>Add to blacklist  |
| void | **[unblockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unblockmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>Unblacklist  |
| void | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupMemberResultPage > callBack)<br>Get blacklist  |
| void | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>Get blacklist  |
| void | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-banmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final long duration, final String reason, final BMXCallBack callBack)<br>Ban  |
| void | **[banGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bangroup)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long duration, final BMXCallBack callBack)<br>Ban all members  |
| void | **[unbanMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbanmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>Unban  |
| void | **[unbanGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbangroup)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>Unban all members  |
| void | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupBannedMemberResultPage > callBack)<br>Get a list of banned members  |
| void | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXDataCallBack< BMXGroupBannedMemberList > callBack)<br>Get a list of banned members  |
| void | **[muteMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-mutemessage)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.MsgMuteMode mode, final BMXCallBack callBack)<br>Set whether to block group messages  |
| void | **[acceptApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptapplication)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long applicantId, final BMXCallBack callBack)<br>Accept application of membership  |
| void | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineapplication)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long applicantId, final String reason, final BMXCallBack callBack)<br>Reject application of membership  |
| void | **[acceptInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptinvitation)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long inviter, final BMXCallBack callBack)<br>Accept to join group  |
| void | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineinvitation)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long inviter, final BMXCallBack callBack)<br>Reject invitation to join group  |
| void | **[transferOwner](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-transferowner)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long newOwnerId, final BMXCallBack callBack)<br>Transfer of group Owner  |
| void | **[uploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-uploadsharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String filePath, final String displayName, final String extensionName, final FileProgressListener listener, final BMXCallBack callBack)<br>Add shared file in group  |
| void | **[removeSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removesharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final BMXCallBack callBack)<br>Remove shared file in group  |
| void | **[downloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadsharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final FileProgressListener listener, final BMXCallBack callBack)<br>Download share file in group  |
| void | **[getSharedFilesList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getsharedfileslist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupSharedFileList > callBack)<br>Get a list of share files in group  |
| void | **[changeSharedFileName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-changesharedfilename)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final String name, final BMXCallBack callBack)<br>Modify shared file name in group  |
| void | **[getLatestAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getlatestannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroup.Announcement > callBack)<br>Get the latest group announcement  |
| void | **[getAnnouncementList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getannouncementlist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupAnnouncementList > callBack)<br>Get group announcements list  |
| void | **[editAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-editannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String title, final String content, final BMXCallBack callBack)<br>Write group announcement  |
| void | **[deleteAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-deleteannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long announcementId, final BMXCallBack callBack)<br>Delete group announcement  |
| void | **[setName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setname)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String name, final BMXCallBack callBack)<br>Set group name  |
| void | **[setDescription](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setdescription)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String description, final BMXCallBack callBack)<br>Set group description  |
| void | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setextension)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String extension, final BMXCallBack callBack)<br>Set group extension information  |
| void | **[setMyNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmynickname)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String nickname, final BMXCallBack callBack)<br>Set nickname in group  |
| void | **[setMsgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmsgpushmode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.MsgPushMode mode, final BMXCallBack callBack)<br>Set group message notification mode  |
| void | **[setJoinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setjoinauthmode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.JoinAuthMode mode, final BMXCallBack callBack)<br>Set approval mode for joining group  |
| void | **[setInviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setinvitemode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.InviteMode mode, final BMXCallBack callBack)<br>Set invitation mode  |
| void | **[setAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setavatar)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>Set group avatar  |
| void | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadavatar)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final FileProgressListener listener, final BMXCallBack callBack)<br>Download group avatar  |
| void | **[addGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addgrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>Add group change listener  |
| void | **[removeGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removegrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>Remove group change listener  |
| void | **[setEnableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setenablereadack)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean enable, final BMXCallBack callBack)<br>Set whether group message read is enabled  |

## Public Functions Documentation

### function BMXGroupManager

```java
inline BMXGroupManager(
    BMXGroupService service
)
```


### function getGroupList

```java
inline void getGroupList(
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupList > callBack
)
```

Get group list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], group id list 


### function getGroupList

```java
inline void getGroupList(
    final ListOfLongLong groupIdList,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupList > callBack
)
```

Get the list of group information for the incoming group id, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupIdList** List of group ids 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], group details list 


### function getGroupList

```java
inline void getGroupList(
    final long groupId,
    final boolean forceUpdate,
    final BMXDataCallBack< BMXGroup > callBack
)
```

Get group information, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupId** Group id to search 
  * **forceUpdate** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], group details returned by search 


### function getInvitationList

```java
inline void getInvitationList(
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< GroupInvitaionPage > callBack
)
```

Get group invitation list in pages 

**Parameters**: 

  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 
  * **callBack** [BMXErrorCode], paged list of group invitation 


### function getApplicationList

```java
inline void getApplicationList(
    final BMXGroupList list,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< GroupApplicationPage > callBack
)
```

Get a list of group applications in pages 

**Parameters**: 

  * **list** List of group ids for which group application list information needs to be obtained 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 
  * **callBack** [BMXErrorCode], paged list of group application 


### function create

```java
inline void create(
    final BMXGroupService.CreateGroupOptions options,
    final BMXDataCallBack< BMXGroup > callBack
)
```

Create group 

**Parameters**: 

  * **options** Parameters passed in when creating a group 
  * **callBack** [BMXErrorCode], created group 


### function destroy

```java
inline void destroy(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

Destroy group 

**Parameters**: 

  * **callBack** BMXErrorCode,Group to destroy 


### function join

```java
inline void join(
    final BMXGroup group,
    final String message,
    final BMXCallBack callBack
)
```

Join a group, which may require admin approval depending on group settings 

**Parameters**: 

  * **group** Group to join 
  * **message** Information for group membership application 
  * **callBack** [BMXErrorCode]


### function leave

```java
inline void leave(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

Quit group 

**Parameters**: 

  * **group** Group to quit 
  * **callBack** [BMXErrorCode]


### function getInfo

```java
inline void getInfo(
    final BMXGroup group,
    final BMXDataCallBack< BMXGroup > callBack
)
```

Get group details, pull the latest information from server 

**Parameters**: 

  * **callBack** [BMXErrorCode], the group to get its latest information 


### function getMembers

```java
inline void getMembers(
    final BMXGroup group,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< BMXGroupMemberResultPage > callBack
)
```

Get group member list, pull from server if forceRefresh is set, up to 1,000 

**Parameters**: 

  * **group** Group to operate on 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 
  * **callBack** [BMXErrorCode], group member list 


### function getMembers

```java
inline void getMembers(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

Get group member list, pull from server if forceRefresh is set, up to 1,000 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], group member list 


### function addMembers

```java
inline void addMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final String message,
    final BMXCallBack callBack
)
```

Add group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to join group 
  * **message** Reason for membership application 
  * **callBack** [BMXErrorCode]


### function removeMembers

```java
inline void removeMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final String reason,
    final BMXCallBack callBack
)
```

Remove group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of group member ids to delete 
  * **reason** Reason for deletion 
  * **callBack** [BMXErrorCode]


### function addAdmins

```java
inline void addAdmins(
    final BMXGroup group,
    final ListOfLongLong admins,
    final String message,
    final BMXCallBack callBack
)
```

Add Admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to be added as Admins 
  * **message** Reason for adding as Admin 
  * **callBack** [BMXErrorCode]


### function removeAdmins

```java
inline void removeAdmins(
    final BMXGroup group,
    final ListOfLongLong admins,
    final String reason,
    final BMXCallBack callBack
)
```

Remove admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to degrade from Admins 
  * **reason** Reason to degrade from Admin 
  * **callBack** [BMXErrorCode]


### function getAdmins

```java
inline void getAdmins(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

Get Admins list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], list of group Admins 


### function blockMembers

```java
inline void blockMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

Add to blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to be blacklisted 
  * **callBack** [BMXErrorCode]


### function unblockMembers

```java
inline void unblockMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

Unblacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unblacklisted user ids 
  * **callBack** [BMXErrorCode]


### function getBlockList

```java
inline void getBlockList(
    final BMXGroup group,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< BMXGroupMemberResultPage > callBack
)
```

Get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 
  * **callBack** [BMXErrorCode], list of group blacklists 


### function getBlockList

```java
inline void getBlockList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

Get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], list of group blacklists 


### function banMembers

```java
inline void banMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final long duration,
    final String reason,
    final BMXCallBack callBack
)
```

Ban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of banned member ids 
  * **duration** Duration of banned 
  * **reason** Reason for banned 
  * **callBack** [BMXErrorCode]


### function banGroup

```java
inline void banGroup(
    final BMXGroup group,
    final long duration,
    final BMXCallBack callBack
)
```

Ban all members 

**Parameters**: 

  * **group** Group to operate on 
  * **duration** Duration of banned 
  * **callBack** [BMXErrorCode]


### function unbanMembers

```java
inline void unbanMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

Unban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unbanned group member ids 
  * **callBack** [BMXErrorCode]


### function unbanGroup

```java
inline void unbanGroup(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

Unban all members 

**Parameters**: 

  * **group** Group to operate on 
  * **callBack** [BMXErrorCode]


### function getBannedMembers

```java
inline void getBannedMembers(
    final BMXGroup group,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< BMXGroupBannedMemberResultPage > callBack
)
```

Get a list of banned members 

**Parameters**: 

  * **group** Group to operate on 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 
  * **callBack** [BMXErrorCode], list of group bans 


### function getBannedMembers

```java
inline void getBannedMembers(
    final BMXGroup group,
    final BMXDataCallBack< BMXGroupBannedMemberList > callBack
)
```

Get a list of banned members 

**Parameters**: 

  * **group** Group to operate on 
  * **callBack** [BMXErrorCode], list of group bans 


### function muteMessage

```java
inline void muteMessage(
    final BMXGroup group,
    final BMXGroup.MsgMuteMode mode,
    final BMXCallBack callBack
)
```

Set whether to block group messages 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group blocking mode 
  * **callBack** [BMXErrorCode]


### function acceptApplication

```java
inline void acceptApplication(
    final BMXGroup group,
    final long applicantId,
    final BMXCallBack callBack
)
```

Accept application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 
  * **callBack** [BMXErrorCode]


### function declineApplication

```java
inline void declineApplication(
    final BMXGroup group,
    final long applicantId,
    final String reason,
    final BMXCallBack callBack
)
```

Reject application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 
  * **reason** Reason for rejection 
  * **callBack** [BMXErrorCode]


### function acceptInvitation

```java
inline void acceptInvitation(
    final BMXGroup group,
    final long inviter,
    final BMXCallBack callBack
)
```

Accept to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 
  * **callBack** [BMXErrorCode]


### function declineInvitation

```java
inline void declineInvitation(
    final BMXGroup group,
    final long inviter,
    final BMXCallBack callBack
)
```

Reject invitation to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 
  * **callBack** [BMXErrorCode]


### function transferOwner

```java
inline void transferOwner(
    final BMXGroup group,
    final long newOwnerId,
    final BMXCallBack callBack
)
```

Transfer of group Owner 

**Parameters**: 

  * **group** Group to operate on 
  * **newOwnerId** User id that transferred as new group Owner 
  * **callBack** [BMXErrorCode]


### function uploadSharedFile

```java
inline void uploadSharedFile(
    final BMXGroup group,
    final String filePath,
    final String displayName,
    final String extensionName,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Add shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **filePath** Local path of file 
  * **displayName** File display name 
  * **extensionName** File extension name 
  * **listener** Upload callback function 
  * **callBack** [BMXErrorCode]


### function removeSharedFile

```java
inline void removeSharedFile(
    final BMXGroup group,
    final BMXGroup.SharedFile sharedFile,
    final BMXCallBack callBack
)
```

Remove shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Deleted group shared file 
  * **callBack** [BMXErrorCode]


### function downloadSharedFile

```java
inline void downloadSharedFile(
    final BMXGroup group,
    final BMXGroup.SharedFile sharedFile,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Download share file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Downloaded group shared files 
  * **listener** Download callback function 
  * **callBack** [BMXErrorCode]


### function getSharedFilesList

```java
inline void getSharedFilesList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupSharedFileList > callBack
)
```

Get a list of share files in group 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], list of group shared files 


### function changeSharedFileName

```java
inline void changeSharedFileName(
    final BMXGroup group,
    final BMXGroup.SharedFile sharedFile,
    final String name,
    final BMXCallBack callBack
)
```

Modify shared file name in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Group shared file to change 
  * **name** Modified group shared file name 
  * **callBack** [BMXErrorCode]


### function getLatestAnnouncement

```java
inline void getLatestAnnouncement(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroup.Announcement > callBack
)
```

Get the latest group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], latest group announcement 


### function getAnnouncementList

```java
inline void getAnnouncementList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupAnnouncementList > callBack
)
```

Get group announcements list 

**Parameters**: 

  * **group** Group to operate on 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 
  * **callBack** [BMXErrorCode], list of group announcements 


### function editAnnouncement

```java
inline void editAnnouncement(
    final BMXGroup group,
    final String title,
    final String content,
    final BMXCallBack callBack
)
```

Write group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **title** Tittle of group announcement 
  * **content** Content of group announcement 
  * **callBack** [BMXErrorCode]


### function deleteAnnouncement

```java
inline void deleteAnnouncement(
    final BMXGroup group,
    final long announcementId,
    final BMXCallBack callBack
)
```

Delete group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **announcementId** Deleted group announcement id 
  * **callBack** [BMXErrorCode]


### function setName

```java
inline void setName(
    final BMXGroup group,
    final String name,
    final BMXCallBack callBack
)
```

Set group name 

**Parameters**: 

  * **group** Group to operate on 
  * **name** Group name 
  * **callBack** [BMXErrorCode]


### function setDescription

```java
inline void setDescription(
    final BMXGroup group,
    final String description,
    final BMXCallBack callBack
)
```

Set group description 

**Parameters**: 

  * **group** Group to operate on 
  * **description** Group description 
  * **callBack** [BMXErrorCode]


### function setExtension

```java
inline void setExtension(
    final BMXGroup group,
    final String extension,
    final BMXCallBack callBack
)
```

Set group extension information 

**Parameters**: 

  * **group** Group to operate on 
  * **extension** Group extension information 
  * **callBack** [BMXErrorCode]


### function setMyNickname

```java
inline void setMyNickname(
    final BMXGroup group,
    final String nickname,
    final BMXCallBack callBack
)
```

Set nickname in group 

**Parameters**: 

  * **group** Group to operate on 
  * **nickname** User nickname in group 
  * **callBack** [BMXErrorCode]


### function setMsgPushMode

```java
inline void setMsgPushMode(
    final BMXGroup group,
    final BMXGroup.MsgPushMode mode,
    final BMXCallBack callBack
)
```

Set group message notification mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group message notification mode 
  * **callBack** [BMXErrorCode]


### function setJoinAuthMode

```java
inline void setJoinAuthMode(
    final BMXGroup group,
    final BMXGroup.JoinAuthMode mode,
    final BMXCallBack callBack
)
```

Set approval mode for joining group 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Join approval mode 
  * **callBack** [BMXErrorCode]


### function setInviteMode

```java
inline void setInviteMode(
    final BMXGroup group,
    final BMXGroup.InviteMode mode,
    final BMXCallBack callBack
)
```

Set invitation mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group invitation mode 
  * **callBack** [BMXErrorCode]


### function setAvatar

```java
inline void setAvatar(
    final BMXGroup group,
    final String avatarPath,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Set group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **avatarPath** Local path of group avatar file 
  * **listener** Upload callback function 
  * **callBack** [BMXErrorCode]


### function downloadAvatar

```java
inline void downloadAvatar(
    final BMXGroup group,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Download group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **listener** Download callback function 
  * **callBack** [BMXErrorCode]


### function addGroupListener

```java
inline void addGroupListener(
    BMXGroupServiceListener listener
)
```

Add group change listener 

**Parameters**: 

  * **listener** Group change listener 


### function removeGroupListener

```java
inline void removeGroupListener(
    BMXGroupServiceListener listener
)
```

Remove group change listener 

**Parameters**: 

  * **listener** Group change listener 


### function setEnableReadAck

```java
inline void setEnableReadAck(
    final BMXGroup group,
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether group message read is enabled 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Enable or not 
  * **callBack** [BMXErrorCode]


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800