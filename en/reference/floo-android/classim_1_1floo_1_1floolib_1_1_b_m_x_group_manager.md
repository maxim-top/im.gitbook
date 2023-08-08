---
title: im::floo::floolib::BMXGroupManager
summary: Group Manager
---

# im::floo::floolib::BMXGroupManager

Group Manager

## Public Functions

|      | Name                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupManager**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_manager.md#function-bmxgroupmanager)([BMXGroupService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md) service)                                                                                                                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupList > callBack)<br>Get group list, pull from server if forceRefreshed is set</p>                                                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final ListOfLongLong groupIdList, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupList > callBack)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set</p>                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final long groupId, final boolean forceUpdate, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>Get group information, pull from server if forceRefreshed is set</p>                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinvitationlist"><strong>getInvitationList</strong></a>(final String cursor, final int pageSize, final BMXDataCallBack&#x3C; GroupInvitaionPage > callBack)<br>Get group invitation list in pages</p>                                                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(final BMXGroupList list, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; GroupApplicationPage > callBack)<br>Get a list of group applications in pages</p>                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-create"><strong>create</strong></a>(final BMXGroupService.CreateGroupOptions options, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>Create group</p>                                                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-destroy"><strong>destroy</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>Destroy group</p>                                                                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-join"><strong>join</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String message, final BMXCallBack callBack)<br>Join a group, which may require admin approval depending on group settings</p>                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-leave"><strong>leave</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>Quit group</p>                                                                                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinfo"><strong>getInfo</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>Get group details, pull the latest information from server</p>                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers"><strong>getMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupMemberResultPage > callBack)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000</p> |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers"><strong>getMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000</p>                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addmembers"><strong>addMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final String message, final BMXCallBack callBack)<br>Add group member</p>                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removemembers"><strong>removeMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final String reason, final BMXCallBack callBack)<br>Remove group member</p>                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addadmins"><strong>addAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong admins, final String message, final BMXCallBack callBack)<br>Add Admin</p>                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removeadmins"><strong>removeAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong admins, final String reason, final BMXCallBack callBack)<br>Remove admin</p>                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getadmins"><strong>getAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>Get Admins list, pull from server if forceRefreshed is set</p>                                       |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-blockmembers"><strong>blockMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>Add to blacklist</p>                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unblockmembers"><strong>unblockMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>Unblacklist</p>                                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupMemberResultPage > callBack)<br>Get blacklist</p>                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>Get blacklist</p>                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-banmembers"><strong>banMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final long duration, final String reason, final BMXCallBack callBack)<br>Ban</p>                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bangroup"><strong>banGroup</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long duration, final BMXCallBack callBack)<br>Ban all members</p>                                                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbanmembers"><strong>unbanMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>Unban</p>                                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbangroup"><strong>unbanGroup</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>Unban all members</p>                                                                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupBannedMemberResultPage > callBack)<br>Get a list of banned members</p>                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXDataCallBack&#x3C; BMXGroupBannedMemberList > callBack)<br>Get a list of banned members</p>                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-mutemessage"><strong>muteMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.MsgMuteMode mode, final BMXCallBack callBack)<br>Set whether to block group messages</p>                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptapplication"><strong>acceptApplication</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long applicantId, final BMXCallBack callBack)<br>Accept application of membership</p>                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineapplication"><strong>declineApplication</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long applicantId, final String reason, final BMXCallBack callBack)<br>Reject application of membership</p>                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptinvitation"><strong>acceptInvitation</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long inviter, final BMXCallBack callBack)<br>Accept to join group</p>                                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineinvitation"><strong>declineInvitation</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long inviter, final BMXCallBack callBack)<br>Reject invitation to join group</p>                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-transferowner"><strong>transferOwner</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long newOwnerId, final BMXCallBack callBack)<br>Transfer of group Owner</p>                                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-uploadsharedfile"><strong>uploadSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String filePath, final String displayName, final String extensionName, final FileProgressListener listener, final BMXCallBack callBack)<br>Add shared file in group</p>    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removesharedfile"><strong>removeSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final BMXCallBack callBack)<br>Remove shared file in group</p>                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadsharedfile"><strong>downloadSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final FileProgressListener listener, final BMXCallBack callBack)<br>Download share file in group</p>                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getsharedfileslist"><strong>getSharedFilesList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupSharedFileList > callBack)<br>Get a list of share files in group</p>                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-changesharedfilename"><strong>changeSharedFileName</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final String name, final BMXCallBack callBack)<br>Modify shared file name in group</p>                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getlatestannouncement"><strong>getLatestAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroup.Announcement > callBack)<br>Get the latest group announcement</p>                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getannouncementlist"><strong>getAnnouncementList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupAnnouncementList > callBack)<br>Get group announcements list</p>                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-editannouncement"><strong>editAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String title, final String content, final BMXCallBack callBack)<br>Write group announcement</p>                                                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-deleteannouncement"><strong>deleteAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long announcementId, final BMXCallBack callBack)<br>Delete group announcement</p>                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setname"><strong>setName</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String name, final BMXCallBack callBack)<br>Set group name</p>                                                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setdescription"><strong>setDescription</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String description, final BMXCallBack callBack)<br>Set group description</p>                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setextension"><strong>setExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String extension, final BMXCallBack callBack)<br>Set group extension information</p>                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmynickname"><strong>setMyNickname</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String nickname, final BMXCallBack callBack)<br>Set nickname in group</p>                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmsgpushmode"><strong>setMsgPushMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.MsgPushMode mode, final BMXCallBack callBack)<br>Set group message notification mode</p>                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setjoinauthmode"><strong>setJoinAuthMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.JoinAuthMode mode, final BMXCallBack callBack)<br>Set approval mode for joining group</p>                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setinvitemode"><strong>setInviteMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.InviteMode mode, final BMXCallBack callBack)<br>Set invitation mode</p>                                                                                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setavatar"><strong>setAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>Set group avatar</p>                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final FileProgressListener listener, final BMXCallBack callBack)<br>Download group avatar</p>                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addgrouplistener"><strong>addGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>Add group change listener</p>                                                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removegrouplistener"><strong>removeGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>Remove group change listener</p>                                                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setenablereadack"><strong>setEnableReadAck</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean enable, final BMXCallBack callBack)<br>Set whether group message read acknowledgement is enabled</p>                                                               |

## Public Functions Documentation

### function BMXGroupManager

```java
inline BMXGroupManager(
    BMXGroupService service
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
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
* **callBack** \[BMXErrorCode], group id list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], group details list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], group details returned by search

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], paged list of group invitation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], paged list of group application

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], created group

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

### function getInfo

```java
inline void getInfo(
    final BMXGroup group,
    final BMXDataCallBack< BMXGroup > callBack
)
```

Get group details, pull the latest information from server

**Parameters**:

* **callBack** \[BMXErrorCode], the group to get its latest information

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], group member list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], group member list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group Admins

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group blacklists

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group blacklists

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group bans

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group bans

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group shared files

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], latest group announcement

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode], list of group announcements

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **nickname** My nickname in group
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

### function addGroupListener

```java
inline void addGroupListener(
    BMXGroupServiceListener listener
)
```

Add group change listener

**Parameters**:

* **listener** Group change listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

### function removeGroupListener

```java
inline void removeGroupListener(
    BMXGroupServiceListener listener
)
```

Remove group change listener

**Parameters**:

* **listener** Group change listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

### function setEnableReadAck

```java
inline void setEnableReadAck(
    final BMXGroup group,
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether group message read acknowledgement is enabled

**Parameters**:

* **group** Group to operate on
* **enable** Enable or not
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
