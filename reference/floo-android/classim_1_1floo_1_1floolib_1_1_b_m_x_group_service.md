---
title: im::floo::floolib::BMXGroupService
summary: Group Service 

---

# im::floo::floolib::BMXGroupService



Group Service 

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[CreateGroupOptions](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_1_1_create_group_options.md)** <br>Group creation options  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-delete)**() |
| [BMXErrorCode] | **[get](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-get)**(BMXGroupList list, boolean forceRefresh)<br>Get group list, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList list, boolean forceRefresh)<br>Get group list, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[fetchGroupsByIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupsbyidlist)**(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[fetchGroupById](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupbyid)**(long groupId, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean forceRefresh)<br>Get group information, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(long groupId, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean forceUpdate)<br>Get group information, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[fetchLocalGroupsByName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchlocalgroupsbyname)**(BMXGroupList list, String name)<br>Query local group information by group name and retrieve the group from local database by group name query  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList list, String name)<br>Query local group information by group name and retrieve the group from local database by group name query  |
| [BMXErrorCode] | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-create)**(BMXGroupService.CreateGroupOptions options, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Create group  |
| [BMXErrorCode] | **[destroy](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-destroy)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Destroy group  |
| [BMXErrorCode] | **[join](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-join)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String message)<br>Join a group, which may require admin approval depending on group settings  |
| [BMXErrorCode] | **[leave](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-leave)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Quit group  |
| [BMXErrorCode] | **[getInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinfo)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Get group details, pull the latest information from server  |
| [BMXErrorCode] | **[getMembersNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembersnickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, BMXGroupMemberList list)<br>Get group member details  |
| [BMXErrorCode] | **[getInvitationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinvitationlist)**(GroupInvitaionPage result, String cursor, int pageSize)<br>Get group invitation list in pages  |
| [BMXErrorCode] | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getapplicationlist)**(BMXGroupList list, GroupApplicationPage result, String cursor, int pageSize)<br>Get a list of group applications in pages  |
| [BMXErrorCode] | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>Get list of group members in pages, pull from server if forceRefresh is set, up to 500 per page.  |
| [BMXErrorCode] | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000  |
| [BMXErrorCode] | **[addMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String message)<br>Add group member  |
| [BMXErrorCode] | **[removeMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removemembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String reason)<br>Remove group member  |
| [BMXErrorCode] | **[addAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong admins, String message)<br>Add Admin  |
| [BMXErrorCode] | **[removeAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removeadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong admins, String reason)<br>Remove admin  |
| [BMXErrorCode] | **[getAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>Get Admins list, pull from server if forceRefreshed is set  |
| [BMXErrorCode] | **[blockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-blockmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Add to blacklist  |
| [BMXErrorCode] | **[unblockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unblockmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Unblacklist  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>Paged to get blacklist  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>Get blacklist  |
| [BMXErrorCode] | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration, String reason)<br>Ban  |
| [BMXErrorCode] | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration) |
| [BMXErrorCode] | **[banGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bangroup)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long duration)<br>Ban all members, the expiration time is calculated from the current server time plus banning duration (only Admins and group Owner can speak in the duration)  |
| [BMXErrorCode] | **[unbanMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbanmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>Unban  |
| [BMXErrorCode] | **[unbanGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbangroup)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>Unban all members  |
| [BMXErrorCode] | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupBannedMemberResultPage result, String cursor, int pageSize)<br>Paged to get ban list  |
| [BMXErrorCode] | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupBannedMemberList list)<br>Get a list of banned members  |
| [BMXErrorCode] | **[muteMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-mutemessage)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.MsgMuteMode mode)<br>Set whether to block group messages  |
| [BMXErrorCode] | **[acceptApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId)<br>Accept application of membership  |
| [BMXErrorCode] | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId, String reason)<br>Reject application of membership  |
| [BMXErrorCode] | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId) |
| [BMXErrorCode] | **[acceptInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter)<br>Accept to join group  |
| [BMXErrorCode] | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter, String reason)<br>Reject invitation to join group  |
| [BMXErrorCode] | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter) |
| [BMXErrorCode] | **[transferOwner](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-transferowner)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long newOwnerId)<br>Transfer of group Owner  |
| [BMXErrorCode] | **[uploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-uploadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String filePath, String displayName, String extensionName, FileProgressListener arg4)<br>Add shared file in group  |
| [BMXErrorCode] | **[cancelUploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceluploadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String filePath)<br>Cancel uploading group shared files  |
| [BMXErrorCode] | **[removeSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removesharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>Remove shared file in group  |
| [BMXErrorCode] | **[downloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile, FileProgressListener arg2)<br>Download share file in group  |
| [BMXErrorCode] | **[cancelDownloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceldownloadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>Cancel downloading group shared files  |
| [BMXErrorCode] | **[getSharedFilesList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getsharedfileslist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupSharedFileList list, boolean forceRefresh)<br>Get a list of share files in group  |
| [BMXErrorCode] | **[changeSharedFileName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-changesharedfilename)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile, String name)<br>Modify shared file name in group  |
| [BMXErrorCode] | **[getLatestAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getlatestannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.Announcement announcement, boolean forceRefresh)<br>Get the latest group announcement  |
| [BMXErrorCode] | **[getAnnouncementList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getannouncementlist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupAnnouncementList list, boolean forceRefresh)<br>Get group announcements list  |
| [BMXErrorCode] | **[editAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-editannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String title, String content)<br>Write group announcement  |
| [BMXErrorCode] | **[deleteAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-deleteannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long announcementId)<br>Delete group announcement  |
| [BMXErrorCode] | **[setName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String name)<br>Set group name  |
| [BMXErrorCode] | **[setDescription](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setdescription)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String description)<br>Set group description  |
| [BMXErrorCode] | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setextension)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String extension)<br>Set group extension information  |
| [BMXErrorCode] | **[setMyNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmynickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String nickname)<br>Set nickname in group  |
| [BMXErrorCode] | **[setMsgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmsgpushmode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.MsgPushMode mode)<br>Set group message notification mode  |
| [BMXErrorCode] | **[setJoinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setjoinauthmode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.JoinAuthMode mode)<br>Set approval mode for joining group  |
| [BMXErrorCode] | **[setInviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setinvitemode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.InviteMode mode)<br>Set invitation mode  |
| [BMXErrorCode] | **[setAllowMemberModify](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setallowmembermodify)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>Set whether group members are allowed to set group information  |
| [BMXErrorCode] | **[setEnableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setenablereadack)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>Set whether group message read acknowledgement is enabled  |
| [BMXErrorCode] | **[setHistoryVisible](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-sethistoryvisible)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>Set whether group members are allowed to enable visible message history  |
| [BMXErrorCode] | **[setAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setavatar)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String avatarPath, FileProgressListener arg2)<br>Set group avatar  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadavatar)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean thumbnail, FileProgressListener arg2)<br>Download group avatar  |
| void | **[addGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addgrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>Add group change listener  |
| void | **[removeGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removegrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>Remove group change listener  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bmxgroupservice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getcptr)**([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function get

```java
inline BMXErrorCode get(
    BMXGroupList list,
    boolean forceRefresh
)
```

Get group list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **list** List of group ids, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function search

```java
inline BMXErrorCode search(
    BMXGroupList list,
    boolean forceRefresh
)
```

Get group list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **list** List of group ids, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function fetchGroupsByIdList

```java
inline BMXErrorCode fetchGroupsByIdList(
    ListOfLongLong groupIdList,
    BMXGroupList list,
    boolean forceRefresh
)
```

Get the list of group information for the incoming group id, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupIdList** List of group ids 
  * **list** List of group details, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function search

```java
inline BMXErrorCode search(
    ListOfLongLong groupIdList,
    BMXGroupList list,
    boolean forceRefresh
)
```

Get the list of group information for the incoming group id, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupIdList** List of group ids 
  * **list** List of group details, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function fetchGroupById

```java
inline BMXErrorCode fetchGroupById(
    long groupId,
    BMXGroup group,
    boolean forceRefresh
)
```

Get group information, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupId** Group id to search 
  * **group** Group information returned by search, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function search

```java
inline BMXErrorCode search(
    long groupId,
    BMXGroup group,
    boolean forceUpdate
)
```

Get group information, pull from server if forceRefreshed is set 

**Parameters**: 

  * **groupId** Group id to search 
  * **group** Group information returned by search, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **forceUpdate** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function fetchLocalGroupsByName

```java
inline BMXErrorCode fetchLocalGroupsByName(
    BMXGroupList list,
    String name
)
```

Query local group information by group name and retrieve the group from local database by group name query 

**Parameters**: 

  * **list** Group list information returned by search result 
  * **name** Keyword of group name for query 


**Return**: [BMXErrorCode]

### function search

```java
inline BMXErrorCode search(
    BMXGroupList list,
    String name
)
```

Query local group information by group name and retrieve the group from local database by group name query 

**Parameters**: 

  * **list** Group list information returned by search result 
  * **name** Keyword of group name for query 


**Return**: [BMXErrorCode]

### function create

```java
inline BMXErrorCode create(
    BMXGroupService.CreateGroupOptions options,
    BMXGroup group
)
```

Create group 

**Parameters**: 

  * **options** Parameters passed in when creating a group 
  * **group** Created groups, pass in a pointing-to-empty objective function shared_ptr and fetch returned result here 


**Return**: [BMXErrorCode]

### function destroy

```java
inline BMXErrorCode destroy(
    BMXGroup group
)
```

Destroy group 

**Parameters**: 

  * **group** Group to destroy 


**Return**: [BMXErrorCode]

### function join

```java
inline BMXErrorCode join(
    BMXGroup group,
    String message
)
```

Join a group, which may require admin approval depending on group settings 

**Parameters**: 

  * **group** Group to join 
  * **message** Information for group membership application 


**Return**: [BMXErrorCode]

### function leave

```java
inline BMXErrorCode leave(
    BMXGroup group
)
```

Quit group 

**Parameters**: 

  * **group** Group to quit 


**Return**: [BMXErrorCode]

### function getInfo

```java
inline BMXErrorCode getInfo(
    BMXGroup group
)
```

Get group details, pull the latest information from server 

**Parameters**: 

  * **group** Group for which the latest information needs to be obtained 


**Return**: [BMXErrorCode]

### function getMembersNickname

```java
inline BMXErrorCode getMembersNickname(
    BMXGroup group,
    ListOfLongLong members,
    BMXGroupMemberList list
)
```

Get group member details 

**Parameters**: 

  * **group** Group to operate on 
  * **members** Group member id to get group member details 
  * **list** Returned group member details, pass in an empty list function and fetch the returned list of group member details here 


**Return**: [BMXErrorCode]

### function getInvitationList

```java
inline BMXErrorCode getInvitationList(
    GroupInvitaionPage result,
    String cursor,
    int pageSize
)
```

Get group invitation list in pages 

**Parameters**: 

  * **result** Paged list of group invitations, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function getApplicationList

```java
inline BMXErrorCode getApplicationList(
    BMXGroupList list,
    GroupApplicationPage result,
    String cursor,
    int pageSize
)
```

Get a list of group applications in pages 

**Parameters**: 

  * **list** List of group ids for which group application list information needs to be obtained 
  * **result** Paged list of group applications, pass in a pointing-to-emtpy shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function getMembers

```java
inline BMXErrorCode getMembers(
    BMXGroup group,
    BMXGroupMemberResultPage result,
    String cursor,
    int pageSize
)
```

Get list of group members in pages, pull from server if forceRefresh is set, up to 500 per page. 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged list of group members, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function getMembers

```java
inline BMXErrorCode getMembers(
    BMXGroup group,
    BMXGroupMemberList list,
    boolean forceRefresh
)
```

Get group member list, pull from server if forceRefresh is set, up to 1,000 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group members, pass in an empty list function and fetch the returned list of group details 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function addMembers

```java
inline BMXErrorCode addMembers(
    BMXGroup group,
    ListOfLongLong members,
    String message
)
```

Add group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to join group 
  * **message** Reason for membership application 


**Return**: [BMXErrorCode]

### function removeMembers

```java
inline BMXErrorCode removeMembers(
    BMXGroup group,
    ListOfLongLong members,
    String reason
)
```

Remove group member 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of group member ids to delete 
  * **reason** Reason for deletion 


**Return**: [BMXErrorCode]

### function addAdmins

```java
inline BMXErrorCode addAdmins(
    BMXGroup group,
    ListOfLongLong admins,
    String message
)
```

Add Admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to be added as Admins 
  * **message** Reason for adding as Admin 


**Return**: [BMXErrorCode]

### function removeAdmins

```java
inline BMXErrorCode removeAdmins(
    BMXGroup group,
    ListOfLongLong admins,
    String reason
)
```

Remove admin 

**Parameters**: 

  * **group** Group to operate on 
  * **admins** List of member ids to degrade from Admins 
  * **reason** Reason to degrade from Admin 


**Return**: [BMXErrorCode]

### function getAdmins

```java
inline BMXErrorCode getAdmins(
    BMXGroup group,
    BMXGroupMemberList list,
    boolean forceRefresh
)
```

Get Admins list, pull from server if forceRefreshed is set 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group Admins, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function blockMembers

```java
inline BMXErrorCode blockMembers(
    BMXGroup group,
    ListOfLongLong members
)
```

Add to blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of member ids to be blacklisted 


**Return**: [BMXErrorCode]

### function unblockMembers

```java
inline BMXErrorCode unblockMembers(
    BMXGroup group,
    ListOfLongLong members
)
```

Unblacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unblacklisted user ids 


**Return**: [BMXErrorCode]

### function getBlockList

```java
inline BMXErrorCode getBlockList(
    BMXGroup group,
    BMXGroupMemberResultPage result,
    String cursor,
    int pageSize
)
```

Paged to get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged list of blacklists, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function getBlockList

```java
inline BMXErrorCode getBlockList(
    BMXGroup group,
    BMXGroupMemberList list,
    boolean forceRefresh
)
```

Get blacklist 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group blacklists, pass in an empty list function and fetch the returned list of group details here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function banMembers

```java
inline BMXErrorCode banMembers(
    BMXGroup group,
    ListOfLongLong members,
    long duration,
    String reason
)
```

Ban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of banned member ids 
  * **duration** Duration of banned 
  * **reason** Reason for banned 


**Return**: [BMXErrorCode]

### function banMembers

```java
inline BMXErrorCode banMembers(
    BMXGroup group,
    ListOfLongLong members,
    long duration
)
```


### function banGroup

```java
inline BMXErrorCode banGroup(
    BMXGroup group,
    long duration
)
```

Ban all members, the expiration time is calculated from the current server time plus banning duration (only Admins and group Owner can speak in the duration) 

**Parameters**: 

  * **group** Group to operate on 
  * **duration** Banning duration (minute) 


**Return**: [BMXErrorCode]

### function unbanMembers

```java
inline BMXErrorCode unbanMembers(
    BMXGroup group,
    ListOfLongLong members
)
```

Unban 

**Parameters**: 

  * **group** Group to operate on 
  * **members** List of unbanned group member ids 


**Return**: [BMXErrorCode]

### function unbanGroup

```java
inline BMXErrorCode unbanGroup(
    BMXGroup group
)
```

Unban all members 

**Parameters**: 

  * **group** Group to operate on 


**Return**: [BMXErrorCode]

### function getBannedMembers

```java
inline BMXErrorCode getBannedMembers(
    BMXGroup group,
    BMXGroupBannedMemberResultPage result,
    String cursor,
    int pageSize
)
```

Paged to get ban list 

**Parameters**: 

  * **group** Group to operate on 
  * **result** Paged ban list, pass in a pointing-to-empty shared_ptr objective function and fetch the returned result here 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function getBannedMembers

```java
inline BMXErrorCode getBannedMembers(
    BMXGroup group,
    BMXGroupBannedMemberList list
)
```

Get a list of banned members 

**Parameters**: 

  * **group** Group to operate on 
  * **list** Group ban list, pass in an empty list function and fetch the returned list of group details here 


**Return**: [BMXErrorCode]

### function muteMessage

```java
inline BMXErrorCode muteMessage(
    BMXGroup group,
    BMXGroup.MsgMuteMode mode
)
```

Set whether to block group messages 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group blocking mode 


**Return**: [BMXErrorCode]

### function acceptApplication

```java
inline BMXErrorCode acceptApplication(
    BMXGroup group,
    long applicantId
)
```

Accept application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 


**Return**: [BMXErrorCode]

### function declineApplication

```java
inline BMXErrorCode declineApplication(
    BMXGroup group,
    long applicantId,
    String reason
)
```

Reject application of membership 

**Parameters**: 

  * **group** Group to operate on 
  * **applicantId** User id that request to join group 
  * **reason** Reason for rejection 


**Return**: [BMXErrorCode]

### function declineApplication

```java
inline BMXErrorCode declineApplication(
    BMXGroup group,
    long applicantId
)
```


### function acceptInvitation

```java
inline BMXErrorCode acceptInvitation(
    BMXGroup group,
    long inviter
)
```

Accept to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 


**Return**: [BMXErrorCode]

### function declineInvitation

```java
inline BMXErrorCode declineInvitation(
    BMXGroup group,
    long inviter,
    String reason
)
```

Reject invitation to join group 

**Parameters**: 

  * **group** Group to operate on 
  * **inviter** Inviter id 
  * **reason** Reason for rejection 


**Return**: [BMXErrorCode]

### function declineInvitation

```java
inline BMXErrorCode declineInvitation(
    BMXGroup group,
    long inviter
)
```


### function transferOwner

```java
inline BMXErrorCode transferOwner(
    BMXGroup group,
    long newOwnerId
)
```

Transfer of group Owner 

**Parameters**: 

  * **group** Group to operate on 
  * **newOwnerId** User id that transferred as new group Owner 


**Return**: [BMXErrorCode]

### function uploadSharedFile

```java
inline BMXErrorCode uploadSharedFile(
    BMXGroup group,
    String filePath,
    String displayName,
    String extensionName,
    FileProgressListener arg4
)
```

Add shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **filePath** Local path of file 
  * **displayName** File display name 
  * **extensionName** File extension name 
  * **arg4** Upload callback function 


**Return**: [BMXErrorCode]

### function cancelUploadSharedFile

```java
inline BMXErrorCode cancelUploadSharedFile(
    BMXGroup group,
    String filePath
)
```

Cancel uploading group shared files 

**Parameters**: 

  * **group** Group to operate on 
  * **filePath** Local path of file 


**Return**: [BMXErrorCode]

### function removeSharedFile

```java
inline BMXErrorCode removeSharedFile(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

Remove shared file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Deleted group shared file 


**Return**: [BMXErrorCode]

### function downloadSharedFile

```java
inline BMXErrorCode downloadSharedFile(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile,
    FileProgressListener arg2
)
```

Download share file in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Downloaded group shared files 
  * **arg2** Download callback function 


**Return**: [BMXErrorCode]

### function cancelDownloadSharedFile

```java
inline BMXErrorCode cancelDownloadSharedFile(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile
)
```

Cancel downloading group shared files 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Downloaded group shared files 


**Return**: [BMXErrorCode]

### function getSharedFilesList

```java
inline BMXErrorCode getSharedFilesList(
    BMXGroup group,
    BMXGroupSharedFileList list,
    boolean forceRefresh
)
```

Get a list of share files in group 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group shared files, pass in an empty list function and fetch the returned list of group details here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function changeSharedFileName

```java
inline BMXErrorCode changeSharedFileName(
    BMXGroup group,
    BMXGroup.SharedFile sharedFile,
    String name
)
```

Modify shared file name in group 

**Parameters**: 

  * **group** Group to operate on 
  * **sharedFile** Group shared file to change 
  * **name** Modified group shared file name 


**Return**: [BMXErrorCode]

### function getLatestAnnouncement

```java
inline BMXErrorCode getLatestAnnouncement(
    BMXGroup group,
    BMXGroup.Announcement announcement,
    boolean forceRefresh
)
```

Get the latest group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **announcement** Latest group announcement, pass in a pointing-to-empty shared_ptr objective function and fetch the latest group announcement here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function getAnnouncementList

```java
inline BMXErrorCode getAnnouncementList(
    BMXGroup group,
    BMXGroupAnnouncementList list,
    boolean forceRefresh
)
```

Get group announcements list 

**Parameters**: 

  * **group** Group to operate on 
  * **list** List of group announcements, pass in an empty list function and fetch the returned result here 
  * **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function editAnnouncement

```java
inline BMXErrorCode editAnnouncement(
    BMXGroup group,
    String title,
    String content
)
```

Write group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **title** Tittle of group announcement 
  * **content** Content of group announcement 


**Return**: [BMXErrorCode]

### function deleteAnnouncement

```java
inline BMXErrorCode deleteAnnouncement(
    BMXGroup group,
    long announcementId
)
```

Delete group announcement 

**Parameters**: 

  * **group** Group to operate on 
  * **announcementId** Deleted group announcement id 


**Return**: [BMXErrorCode]

### function setName

```java
inline BMXErrorCode setName(
    BMXGroup group,
    String name
)
```

Set group name 

**Parameters**: 

  * **group** Group to operate on 
  * **name** Group name 


**Return**: [BMXErrorCode]

### function setDescription

```java
inline BMXErrorCode setDescription(
    BMXGroup group,
    String description
)
```

Set group description 

**Parameters**: 

  * **group** Group to operate on 
  * **description** Group description 


**Return**: [BMXErrorCode]

### function setExtension

```java
inline BMXErrorCode setExtension(
    BMXGroup group,
    String extension
)
```

Set group extension information 

**Parameters**: 

  * **group** Group to operate on 
  * **extension** Group extension information 


**Return**: [BMXErrorCode]

### function setMyNickname

```java
inline BMXErrorCode setMyNickname(
    BMXGroup group,
    String nickname
)
```

Set nickname in group 

**Parameters**: 

  * **group** Group to operate on 
  * **nickname** My nickname in group 


**Return**: [BMXErrorCode]

### function setMsgPushMode

```java
inline BMXErrorCode setMsgPushMode(
    BMXGroup group,
    BMXGroup.MsgPushMode mode
)
```

Set group message notification mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group message notification mode 


**Return**: [BMXErrorCode]

### function setJoinAuthMode

```java
inline BMXErrorCode setJoinAuthMode(
    BMXGroup group,
    BMXGroup.JoinAuthMode mode
)
```

Set approval mode for joining group 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Join approval mode 


**Return**: [BMXErrorCode]

### function setInviteMode

```java
inline BMXErrorCode setInviteMode(
    BMXGroup group,
    BMXGroup.InviteMode mode
)
```

Set invitation mode 

**Parameters**: 

  * **group** Group to operate on 
  * **mode** Group invitation mode 


**Return**: [BMXErrorCode]

### function setAllowMemberModify

```java
inline BMXErrorCode setAllowMemberModify(
    BMXGroup group,
    boolean enable
)
```

Set whether group members are allowed to set group information 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Whether allowed to operate 


**Return**: [BMXErrorCode]

### function setEnableReadAck

```java
inline BMXErrorCode setEnableReadAck(
    BMXGroup group,
    boolean enable
)
```

Set whether group message read acknowledgement is enabled 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Enable or not 


**Return**: [BMXErrorCode]

### function setHistoryVisible

```java
inline BMXErrorCode setHistoryVisible(
    BMXGroup group,
    boolean enable
)
```

Set whether group members are allowed to enable visible message history 

**Parameters**: 

  * **group** Group to operate on 
  * **enable** Enable or not 


**Return**: [BMXErrorCode]

### function setAvatar

```java
inline BMXErrorCode setAvatar(
    BMXGroup group,
    String avatarPath,
    FileProgressListener arg2
)
```

Set group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **avatarPath** Local path of group avatar file 
  * **arg2** Upload callback function 


**Return**: [BMXErrorCode]

### function downloadAvatar

```java
inline BMXErrorCode downloadAvatar(
    BMXGroup group,
    boolean thumbnail,
    FileProgressListener arg2
)
```

Download group avatar 

**Parameters**: 

  * **group** Group to operate on 
  * **thumbnail** True to download thumbnail, false to download original image 
  * **arg2** Download callback function 


**Return**: [BMXErrorCode]

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


## Protected Functions Documentation

### function BMXGroupService

```java
inline BMXGroupService(
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
    BMXGroupService obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800