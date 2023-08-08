---
title: im::floo::floolib::BMXGroupService
summary: Group Service
---

# im::floo::floolib::BMXGroupService

Group Service

## Public Classes

|       | Name                                                                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_1_1_create_group_options.md"><strong>CreateGroupOptions</strong></a><br>Group creation options</p> |

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-delete)()                                                                                                                                                                                                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-get"><strong>get</strong></a>(BMXGroupList list, boolean forceRefresh)<br>Get group list, pull from server if forceRefreshed is set</p>                                                                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(BMXGroupList list, boolean forceRefresh)<br>Get group list, pull from server if forceRefreshed is set</p>                                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupsbyidlist"><strong>fetchGroupsByIdList</strong></a>(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set</p>                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>Get the list of group information for the incoming group id, pull from server if forceRefreshed is set</p>                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupbyid"><strong>fetchGroupById</strong></a>(long groupId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean forceRefresh)<br>Get group information, pull from server if forceRefreshed is set</p>                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(long groupId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean forceUpdate)<br>Get group information, pull from server if forceRefreshed is set</p>                                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchlocalgroupsbyname"><strong>fetchLocalGroupsByName</strong></a>(BMXGroupList list, String name)<br>Query local group information by group name and retrieve the group from local database by group name query</p>                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(BMXGroupList list, String name)<br>Query local group information by group name and retrieve the group from local database by group name query</p>                                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-create"><strong>create</strong></a>(BMXGroupService.CreateGroupOptions options, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Create group</p>                                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-destroy"><strong>destroy</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Destroy group</p>                                                                                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-join"><strong>join</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String message)<br>Join a group, which may require admin approval depending on group settings</p>                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-leave"><strong>leave</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Quit group</p>                                                                                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinfo"><strong>getInfo</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Get group details, pull the latest information from server</p>                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembersnickname"><strong>getMembersNickname</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, BMXGroupMemberList list)<br>Get group member details</p>                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinvitationlist"><strong>getInvitationList</strong></a>(GroupInvitaionPage result, String cursor, int pageSize)<br>Get group invitation list in pages</p>                                                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(BMXGroupList list, GroupApplicationPage result, String cursor, int pageSize)<br>Get a list of group applications in pages</p>                                                                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers"><strong>getMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>Get list of group members in pages, pull from server if forceRefresh is set, up to 500 per page.</p>           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers"><strong>getMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>Get group member list, pull from server if forceRefresh is set, up to 1,000</p>                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addmembers"><strong>addMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String message)<br>Add group member</p>                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removemembers"><strong>removeMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String reason)<br>Remove group member</p>                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addadmins"><strong>addAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong admins, String message)<br>Add Admin</p>                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removeadmins"><strong>removeAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong admins, String reason)<br>Remove admin</p>                                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getadmins"><strong>getAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>Get Admins list, pull from server if forceRefreshed is set</p>                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-blockmembers"><strong>blockMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Add to blacklist</p>                                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unblockmembers"><strong>unblockMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Unblacklist</p>                                                                                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist"><strong>getBlockList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>Paged to get blacklist</p>                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist"><strong>getBlockList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>Get blacklist</p>                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers"><strong>banMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, long duration, String reason)<br>Ban</p>                                                                                                                |
| \[BMXErrorCode]   | [**banMembers**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-banmembers)([BMXGroup](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md) group, ListOfLongLong members, long duration)                                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bangroup"><strong>banGroup</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long duration)<br>Ban all members, the expiration time is calculated from the current server time plus banning duration (only Admins and group Owner can speak in the duration)</p> |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbanmembers"><strong>unbanMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>Unban</p>                                                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbangroup"><strong>unbanGroup</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>Unban all members</p>                                                                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupBannedMemberResultPage result, String cursor, int pageSize)<br>Paged to get ban list</p>                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupBannedMemberList list)<br>Get a list of banned members</p>                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-mutemessage"><strong>muteMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.MsgMuteMode mode)<br>Set whether to block group messages</p>                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptapplication"><strong>acceptApplication</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId)<br>Accept application of membership</p>                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication"><strong>declineApplication</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId, String reason)<br>Reject application of membership</p>                                                                                        |
| \[BMXErrorCode]   | [**declineApplication**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-declineapplication)([BMXGroup](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md) group, long applicantId)                                                                                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptinvitation"><strong>acceptInvitation</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviter)<br>Accept to join group</p>                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation"><strong>declineInvitation</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviter, String reason)<br>Reject invitation to join group</p>                                                                                               |
| \[BMXErrorCode]   | [**declineInvitation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-declineinvitation)([BMXGroup](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md) group, long inviter)                                                                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-transferowner"><strong>transferOwner</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long newOwnerId)<br>Transfer of group Owner</p>                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-uploadsharedfile"><strong>uploadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String filePath, String displayName, String extensionName, FileProgressListener arg4)<br>Add shared file in group</p>                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceluploadsharedfile"><strong>cancelUploadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String filePath)<br>Cancel uploading group shared files</p>                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removesharedfile"><strong>removeSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>Remove shared file in group</p>                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadsharedfile"><strong>downloadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile, FileProgressListener arg2)<br>Download share file in group</p>                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceldownloadsharedfile"><strong>cancelDownloadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>Cancel downloading group shared files</p>                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getsharedfileslist"><strong>getSharedFilesList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupSharedFileList list, boolean forceRefresh)<br>Get a list of share files in group</p>                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-changesharedfilename"><strong>changeSharedFileName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile, String name)<br>Modify shared file name in group</p>                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getlatestannouncement"><strong>getLatestAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.Announcement announcement, boolean forceRefresh)<br>Get the latest group announcement</p>                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getannouncementlist"><strong>getAnnouncementList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupAnnouncementList list, boolean forceRefresh)<br>Get group announcements list</p>                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-editannouncement"><strong>editAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String title, String content)<br>Write group announcement</p>                                                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-deleteannouncement"><strong>deleteAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long announcementId)<br>Delete group announcement</p>                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setname"><strong>setName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String name)<br>Set group name</p>                                                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setdescription"><strong>setDescription</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String description)<br>Set group description</p>                                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setextension"><strong>setExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String extension)<br>Set group extension information</p>                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmynickname"><strong>setMyNickname</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String nickname)<br>Set nickname in group</p>                                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmsgpushmode"><strong>setMsgPushMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.MsgPushMode mode)<br>Set group message notification mode</p>                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setjoinauthmode"><strong>setJoinAuthMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.JoinAuthMode mode)<br>Set approval mode for joining group</p>                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setinvitemode"><strong>setInviteMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.InviteMode mode)<br>Set invitation mode</p>                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setallowmembermodify"><strong>setAllowMemberModify</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>Set whether group members are allowed to set group information</p>                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setenablereadack"><strong>setEnableReadAck</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>Set whether group message read acknowledgement is enabled</p>                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-sethistoryvisible"><strong>setHistoryVisible</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>Set whether group members are allowed to enable visible message history</p>                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setavatar"><strong>setAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String avatarPath, FileProgressListener arg2)<br>Set group avatar</p>                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean thumbnail, FileProgressListener arg2)<br>Download group avatar</p>                                                                                              |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addgrouplistener"><strong>addGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>Add group change listener</p>                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removegrouplistener"><strong>removeGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>Remove group change listener</p>                                                                                        |

## Protected Functions

|      | Name                                                                                                                                                                                      |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-bmxgroupservice)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-finalize)()                                                                                      |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#function-getcptr)([BMXGroupService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group\_service.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **group** Group information returned by search, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **group** Group information returned by search, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **forceUpdate** True to force fetch from server, sdk will fetch from server automatically if local fetch failed

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **group** Created groups, pass in a pointing-to-empty objective function shared\_ptr and fetch returned result here

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function destroy

```java
inline BMXErrorCode destroy(
    BMXGroup group
)
```

Destroy group

**Parameters**:

* **group** Group to destroy

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function leave

```java
inline BMXErrorCode leave(
    BMXGroup group
)
```

Quit group

**Parameters**:

* **group** Group to quit

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function getInfo

```java
inline BMXErrorCode getInfo(
    BMXGroup group
)
```

Get group details, pull the latest information from server

**Parameters**:

* **group** Group for which the latest information needs to be obtained

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

* **result** Paged list of group invitations, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **result** Paged list of group applications, pass in a pointing-to-emtpy shared\_ptr objective function and fetch the returned result here
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **result** Paged list of group members, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **result** Paged list of blacklists, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function banMembers

```java
inline BMXErrorCode banMembers(
    BMXGroup group,
    ListOfLongLong members,
    long duration
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function unbanGroup

```java
inline BMXErrorCode unbanGroup(
    BMXGroup group
)
```

Unban all members

**Parameters**:

* **group** Group to operate on

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **result** Paged ban list, pass in a pointing-to-empty shared\_ptr objective function and fetch the returned result here
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function declineApplication

```java
inline BMXErrorCode declineApplication(
    BMXGroup group,
    long applicantId
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function declineInvitation

```java
inline BMXErrorCode declineInvitation(
    BMXGroup group,
    long inviter
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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
* **announcement** Latest group announcement, pass in a pointing-to-empty shared\_ptr objective function and fetch the latest group announcement here
* **forceRefresh** True to force fetch from server, sdk will fetch from server automatically if local fetch failed

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

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

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function BMXGroupService

```java
inline BMXGroupService(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupService'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
