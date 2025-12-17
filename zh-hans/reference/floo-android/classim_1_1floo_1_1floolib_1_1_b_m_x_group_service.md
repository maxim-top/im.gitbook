---
title: im::floo::floolib::BMXGroupService
summary: 群组Service
---

# im::floo::floolib::BMXGroupService

群组Service

## Public Classes

|       | Name                                                                                                                                              |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_1_1_create_group_options.md"><strong>CreateGroupOptions</strong></a><br>创建群组选项</p> |

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-delete)()                                                                                                                                                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-get"><strong>get</strong></a>(BMXGroupList list, boolean forceRefresh)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取</p>                                                                                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(BMXGroupList list, boolean forceRefresh)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取</p>                                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupsbyidlist"><strong>fetchGroupsByIdList</strong></a>(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取</p>                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取</p>                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupbyid"><strong>fetchGroupById</strong></a>(long groupId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean forceRefresh)<br>获取群信息，如果设置了forceRefresh则从服务器拉取</p>                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(long groupId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean forceUpdate)<br>获取群信息，如果设置了forceRefresh则从服务器拉取</p>                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchlocalgroupsbyname"><strong>fetchLocalGroupsByName</strong></a>(BMXGroupList list, String name)<br>通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组</p>                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search"><strong>search</strong></a>(BMXGroupList list, String name)<br>通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组</p>                                                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-create"><strong>create</strong></a>(BMXGroupService.CreateGroupOptions options, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>创建群</p>                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-destroy"><strong>destroy</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>销毁群</p>                                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-join"><strong>join</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String message)<br>加入一个群，根据群设置可能需要管理员批准</p>                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-leave"><strong>leave</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>退出群</p>                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinfo"><strong>getInfo</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>获取群详情，从服务端拉取最新信息</p>                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembersnickname"><strong>getMembersNickname</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, BMXGroupMemberList list)<br>获取群组成员详细信息</p>                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinvitationlist"><strong>getInvitationList</strong></a>(GroupInvitaionPage result, String cursor, int pageSize)<br>分页获取群组邀请列表</p>                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(BMXGroupList list, GroupApplicationPage result, String cursor, int pageSize)<br>分页获取群组申请列表</p>                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers"><strong>getMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.</p> |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers"><strong>getMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人</p>                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addmembers"><strong>addMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String message)<br>添加群成员</p>                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removemembers"><strong>removeMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, String reason)<br>删除群成员</p>                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addadmins"><strong>addAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong admins, String message)<br>添加管理员</p>                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removeadmins"><strong>removeAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong admins, String reason)<br>删除管理员</p>                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getadmins"><strong>getAdmins</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>获取Admins列表，如果设置了forceRefresh则从服务器拉取</p>                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-blockmembers"><strong>blockMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>添加黑名单</p>                                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unblockmembers"><strong>unblockMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>从黑名单删除</p>                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist"><strong>getBlockList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>分页获取黑名单</p>                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist"><strong>getBlockList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupMemberList list, boolean forceRefresh)<br>获取黑名单</p>                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers"><strong>banMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members, long duration, String reason)<br>禁言</p>                                                     |
| \[BMXErrorCode]   | [**banMembers**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers)([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration)                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bangroup"><strong>banGroup</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long duration)<br>全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）</p>                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbanmembers"><strong>unbanMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, ListOfLongLong members)<br>解除禁言</p>                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbangroup"><strong>unbanGroup</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group)<br>全员解除禁言</p>                                                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupBannedMemberResultPage result, String cursor, int pageSize)<br>分页获取禁言列表</p>                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupBannedMemberList list)<br>获取禁言列表</p>                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-mutemessage"><strong>muteMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.MsgMuteMode mode)<br>设置是否屏蔽群消息</p>                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptapplication"><strong>acceptApplication</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId)<br>接受入群申请</p>                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication"><strong>declineApplication</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long applicantId, String reason)<br>拒绝入群申请</p>                                                      |
| \[BMXErrorCode]   | [**declineApplication**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication)([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId)                                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptinvitation"><strong>acceptInvitation</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviter)<br>接受入群邀请</p>                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation"><strong>declineInvitation</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long inviter, String reason)<br>拒绝入群邀请</p>                                                            |
| \[BMXErrorCode]   | [**declineInvitation**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation)([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter)                                                                                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-transferowner"><strong>transferOwner</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long newOwnerId)<br>转移群主</p>                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-uploadsharedfile"><strong>uploadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String filePath, String displayName, String extensionName, FileProgressListener arg4)<br>添加群共享文件</p>    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceluploadsharedfile"><strong>cancelUploadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String filePath)<br>取消上传群共享文件</p>                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removesharedfile"><strong>removeSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>移除群共享文件</p>                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadsharedfile"><strong>downloadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile, FileProgressListener arg2)<br>下载群共享文件</p>                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceldownloadsharedfile"><strong>cancelDownloadSharedFile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile)<br>取消下载群共享文件</p>                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getsharedfileslist"><strong>getSharedFilesList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupSharedFileList list, boolean forceRefresh)<br>获取群共享文件列表</p>                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-changesharedfilename"><strong>changeSharedFileName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.SharedFile sharedFile, String name)<br>修改群共享文件名称</p>                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getlatestannouncement"><strong>getLatestAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.Announcement announcement, boolean forceRefresh)<br>获取最新的群公告</p>                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getannouncementlist"><strong>getAnnouncementList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroupAnnouncementList list, boolean forceRefresh)<br>获取群公告列表</p>                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-editannouncement"><strong>editAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String title, String content)<br>设置群公告</p>                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-deleteannouncement"><strong>deleteAnnouncement</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, long announcementId)<br>删除群公告</p>                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setname"><strong>setName</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String name)<br>设置群名称</p>                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setdescription"><strong>setDescription</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String description)<br>设置群描述信息</p>                                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setextension"><strong>setExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String extension)<br>设置群扩展信息</p>                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmynickname"><strong>setMyNickname</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String nickname)<br>设置在群里的昵称</p>                                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmsgpushmode"><strong>setMsgPushMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.MsgPushMode mode)<br>设置群消息通知模式</p>                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setjoinauthmode"><strong>setJoinAuthMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.JoinAuthMode mode)<br>设置入群审批模式</p>                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setinvitemode"><strong>setInviteMode</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, BMXGroup.InviteMode mode)<br>设置邀请模式</p>                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setallowmembermodify"><strong>setAllowMemberModify</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>设置是否允许群成员设置群信息</p>                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setenablereadack"><strong>setEnableReadAck</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>设置是否开启群消息已读功能</p>                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-sethistoryvisible"><strong>setHistoryVisible</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean enable)<br>设置群成员是否开可见群历史聊天记录</p>                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setavatar"><strong>setAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, String avatarPath, FileProgressListener arg2)<br>设置群头像</p>                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, boolean thumbnail, FileProgressListener arg2)<br>下载群头像</p>                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addgrouplistener"><strong>addGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>添加群组变化监听者</p>                                                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removegrouplistener"><strong>removeGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>移除群组变化监听者</p>                                               |

## Protected Functions

|      | Name                                                                                                                                                                |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupService**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bmxgroupservice)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-finalize)()                                                                           |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getcptr)([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                          |
| ----------------- | --------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#variable-swigcmemown) |

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

获取群组列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **list** 群组id列表，传入空列表函数返回后从此处获取返回的群组id列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取群组列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **list** 群组id列表，传入空列表函数返回后从此处获取返回的群组id列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupIdList** 群组id列表
* **list** 群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupIdList** 群组id列表
* **list** 群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取群信息，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupId** 要搜索的群组id
* **group** 搜索返回的群组信息，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取群信息，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupId** 要搜索的群组id
* **group** 搜索返回的群组信息，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果
* **forceUpdate** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

**Parameters**:

* **list** 搜索结果返回的群列表信息
* **name** 查询的群名称关键字

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

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

**Parameters**:

* **list** 搜索结果返回的群列表信息
* **name** 查询的群名称关键字

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

创建群

**Parameters**:

* **options** 创建群组时传入的参数选项
* **group** 创建好的群，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果

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

销毁群

**Parameters**:

* **group** 要销毁的群组

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

加入一个群，根据群设置可能需要管理员批准

**Parameters**:

* **group** 要加入的群组
* **message** 申请入群的信息

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

退出群

**Parameters**:

* **group** 要退出的群组

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

获取群详情，从服务端拉取最新信息

**Parameters**:

* **group** 要获取群组最新信息的群组

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

获取群组成员详细信息

**Parameters**:

* **group** 进行操作的群组
* **members** 要获取群组成员信息详情的群成员id
* **list** 返回的群成员详细，传入空列表在函数操作后从此处获取群成员详细信息列表

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

分页获取群组邀请列表

**Parameters**:

* **result** 分页获取的群组邀请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

分页获取群组申请列表

**Parameters**:

* **list** 需要获取群组申请列表信息的群组id列表
* **result** 分页获取的群组申请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.

**Parameters**:

* **group** 进行操作的群组
* **result** 分页获取的群成员列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

**Parameters**:

* **group** 进行操作的群组
* **list** 群成员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

添加群成员

**Parameters**:

* **group** 进行操作的群组
* **members** 要添加进群的成员id列表
* **message** 添加成员原因信息

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

删除群成员

**Parameters**:

* **group** 进行操作的群组
* **members** 要删除的群组成员id列表
* **reason** 删除的原因

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

添加管理员

**Parameters**:

* **group** 进行操作的群组
* **admins** 要添加为管理员的成员id列表
* **message** 添加为管理员的原因

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

删除管理员

**Parameters**:

* **group** 进行操作的群组
* **admins** 要从管理员移除的成员id列表
* **reason** 要移除管理员的原因

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

获取Admins列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **group** 进行操作的群组
* **list** 群管理员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

添加黑名单

**Parameters**:

* **group** 进行操作的群组
* **members** 要加入黑名单的群成员id列表

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

从黑名单删除

**Parameters**:

* **group** 进行操作的群组
* **members** 从黑名单移除的用户id列表

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

分页获取黑名单

**Parameters**:

* **group** 进行操作的群组
* **result** 分页获取的黑名单列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

获取黑名单

**Parameters**:

* **group** 进行操作的群组
* **list** 群黑名单列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

禁言

**Parameters**:

* **group** 进行操作的群组
* **members** 被禁言的群成员id列表
* **duration** 禁言时长
* **reason** 禁言原因

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

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）

**Parameters**:

* **group** 进行操作的群组
* **duration** 禁言时长(分钟)

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

解除禁言

**Parameters**:

* **group** 进行操作的群组
* **members** 被解除禁言的群成员id列表

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

全员解除禁言

**Parameters**:

* **group** 进行操作的群组

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

分页获取禁言列表

**Parameters**:

* **group** 进行操作的群组
* **result** 分页获取的禁言列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

获取禁言列表

**Parameters**:

* **group** 进行操作的群组
* **list** 群禁言列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

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

设置是否屏蔽群消息

**Parameters**:

* **group** 进行操作的群组
* **mode** 群屏蔽的模式

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

接受入群申请

**Parameters**:

* **group** 进行操作的群组
* **applicantId** 申请进群的用户id

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

拒绝入群申请

**Parameters**:

* **group** 进行操作的群组
* **applicantId** 申请进群的用户id
* **reason** 拒绝的原因

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

接受入群邀请

**Parameters**:

* **group** 进行操作的群组
* **inviter** 邀请者id

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

拒绝入群邀请

**Parameters**:

* **group** 进行操作的群组
* **inviter** 邀请者id
* **reason** 拒绝的原因

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

转移群主

**Parameters**:

* **group** 进行操作的群组
* **newOwnerId** 转让为新群主的用户id

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

添加群共享文件

**Parameters**:

* **group** 进行操作的群组
* **filePath** 文件的本地路径
* **displayName** 文件的展示名
* **extensionName** 文件的扩展名
* **arg4** 上传回调函数

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

取消上传群共享文件

**Parameters**:

* **group** 进行操作的群组
* **filePath** 文件的本地路径

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

移除群共享文件

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 删除的群共享文件

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

下载群共享文件

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 下载的群共享文件
* **arg2** 下载回调函数

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

取消下载群共享文件

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 下载的群共享文件

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

获取群共享文件列表

**Parameters**:

* **group** 进行操作的群组
* **list** 群共享文件列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

修改群共享文件名称

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 进行更改的群共享文件
* **name** 修改的群共享文件名称

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

获取最新的群公告

**Parameters**:

* **group** 进行操作的群组
* **announcement** 最新的群组公告，传入指向为空的shared\_ptr对象函数返回后从此处获取最新的群组公告
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

获取群公告列表

**Parameters**:

* **group** 进行操作的群组
* **list** 群公告列表，传入空列表函数返回后从此处获取返回的群组详细信息列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

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

设置群公告

**Parameters**:

* **group** 进行操作的群组
* **title** 群公告的标题
* **content** 群公告的内容

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

删除群公告

**Parameters**:

* **group** 进行操作的群组
* **announcementId** 删除的群公告id

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

设置群名称

**Parameters**:

* **group** 进行操作的群组
* **name** 群组名称

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

设置群描述信息

**Parameters**:

* **group** 进行操作的群组
* **description** 群组描述

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

设置群扩展信息

**Parameters**:

* **group** 进行操作的群组
* **extension** 群组的扩展信息

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

设置在群里的昵称

**Parameters**:

* **group** 进行操作的群组
* **nickname** 用户在群组内的昵称

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

设置群消息通知模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 群消息通知模式

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

设置入群审批模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 入群审批模式

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

设置邀请模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 群组的邀请模式

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

设置是否允许群成员设置群信息

**Parameters**:

* **group** 进行操作的群组
* **enable** 是否允许操作

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

设置是否开启群消息已读功能

**Parameters**:

* **group** 进行操作的群组
* **enable** 是否开启

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

设置群成员是否开可见群历史聊天记录

**Parameters**:

* **group** 进行操作的群组
* **enable** 是否开启

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

设置群头像

**Parameters**:

* **group** 进行操作的群组
* **avatarPath** 群头像文件的本地路径
* **arg2** 上传回调函数

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

下载群头像

**Parameters**:

* **group** 进行操作的群组
* **thumbnail** 设置为true下载缩略图，false下载原图
* **arg2** 下载回调函数

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

添加群组变化监听者

**Parameters**:

* **listener** 群组变化监听者

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

移除群组变化监听者

**Parameters**:

* **listener** 群组变化监听者

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

***

Updated on 2022-01-26 at 17:18:31 +0800
