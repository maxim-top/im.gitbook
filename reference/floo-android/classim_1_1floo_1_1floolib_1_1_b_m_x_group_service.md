---
title: im::floo::floolib::BMXGroupService
summary: 群组Service 

---

# im::floo::floolib::BMXGroupService



群组Service 

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[CreateGroupOptions](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_1_1_create_group_options.md)** <br>创建群组选项  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-delete)**() |
| [BMXErrorCode] | **[get](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-get)**(BMXGroupList list, boolean forceRefresh)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList list, boolean forceRefresh)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[fetchGroupsByIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupsbyidlist)**(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(ListOfLongLong groupIdList, BMXGroupList list, boolean forceRefresh)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[fetchGroupById](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchgroupbyid)**(long groupId, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean forceRefresh)<br>获取群信息，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(long groupId, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean forceUpdate)<br>获取群信息，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[fetchLocalGroupsByName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-fetchlocalgroupsbyname)**(BMXGroupList list, String name)<br>通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-search)**(BMXGroupList list, String name)<br>通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组  |
| [BMXErrorCode] | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-create)**(BMXGroupService.CreateGroupOptions options, [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>创建群  |
| [BMXErrorCode] | **[destroy](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-destroy)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>销毁群  |
| [BMXErrorCode] | **[join](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-join)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String message)<br>加入一个群，根据群设置可能需要管理员批准  |
| [BMXErrorCode] | **[leave](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-leave)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>退出群  |
| [BMXErrorCode] | **[getInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinfo)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>获取群详情，从服务端拉取最新信息  |
| [BMXErrorCode] | **[getMembersNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembersnickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, BMXGroupMemberList list)<br>获取群组成员详细信息  |
| [BMXErrorCode] | **[getInvitationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getinvitationlist)**(GroupInvitaionPage result, String cursor, int pageSize)<br>分页获取群组邀请列表  |
| [BMXErrorCode] | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getapplicationlist)**(BMXGroupList list, GroupApplicationPage result, String cursor, int pageSize)<br>分页获取群组申请列表  |
| [BMXErrorCode] | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.  |
| [BMXErrorCode] | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人  |
| [BMXErrorCode] | **[addMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String message)<br>添加群成员  |
| [BMXErrorCode] | **[removeMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removemembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, String reason)<br>删除群成员  |
| [BMXErrorCode] | **[addAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong admins, String message)<br>添加管理员  |
| [BMXErrorCode] | **[removeAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removeadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong admins, String reason)<br>删除管理员  |
| [BMXErrorCode] | **[getAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getadmins)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>获取Admins列表，如果设置了forceRefresh则从服务器拉取  |
| [BMXErrorCode] | **[blockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-blockmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>添加黑名单  |
| [BMXErrorCode] | **[unblockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unblockmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>从黑名单删除  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberResultPage result, String cursor, int pageSize)<br>分页获取黑名单  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getblocklist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupMemberList list, boolean forceRefresh)<br>获取黑名单  |
| [BMXErrorCode] | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration, String reason)<br>禁言  |
| [BMXErrorCode] | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-banmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members, long duration) |
| [BMXErrorCode] | **[banGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-bangroup)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long duration)<br>全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）  |
| [BMXErrorCode] | **[unbanMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbanmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, ListOfLongLong members)<br>解除禁言  |
| [BMXErrorCode] | **[unbanGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-unbangroup)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group)<br>全员解除禁言  |
| [BMXErrorCode] | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupBannedMemberResultPage result, String cursor, int pageSize)<br>分页获取禁言列表  |
| [BMXErrorCode] | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getbannedmembers)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupBannedMemberList list)<br>获取禁言列表  |
| [BMXErrorCode] | **[muteMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-mutemessage)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.MsgMuteMode mode)<br>设置是否屏蔽群消息  |
| [BMXErrorCode] | **[acceptApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId)<br>接受入群申请  |
| [BMXErrorCode] | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId, String reason)<br>拒绝入群申请  |
| [BMXErrorCode] | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineapplication)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long applicantId) |
| [BMXErrorCode] | **[acceptInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-acceptinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter)<br>接受入群邀请  |
| [BMXErrorCode] | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter, String reason)<br>拒绝入群邀请  |
| [BMXErrorCode] | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-declineinvitation)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long inviter) |
| [BMXErrorCode] | **[transferOwner](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-transferowner)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long newOwnerId)<br>转移群主  |
| [BMXErrorCode] | **[uploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-uploadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String filePath, String displayName, String extensionName, FileProgressListener arg4)<br>添加群共享文件  |
| [BMXErrorCode] | **[cancelUploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceluploadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String filePath)<br>取消上传群共享文件  |
| [BMXErrorCode] | **[removeSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removesharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>移除群共享文件  |
| [BMXErrorCode] | **[downloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile, FileProgressListener arg2)<br>下载群共享文件  |
| [BMXErrorCode] | **[cancelDownloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-canceldownloadsharedfile)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile)<br>取消下载群共享文件  |
| [BMXErrorCode] | **[getSharedFilesList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getsharedfileslist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupSharedFileList list, boolean forceRefresh)<br>获取群共享文件列表  |
| [BMXErrorCode] | **[changeSharedFileName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-changesharedfilename)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.SharedFile sharedFile, String name)<br>修改群共享文件名称  |
| [BMXErrorCode] | **[getLatestAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getlatestannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.Announcement announcement, boolean forceRefresh)<br>获取最新的群公告  |
| [BMXErrorCode] | **[getAnnouncementList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-getannouncementlist)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroupAnnouncementList list, boolean forceRefresh)<br>获取群公告列表  |
| [BMXErrorCode] | **[editAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-editannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String title, String content)<br>设置群公告  |
| [BMXErrorCode] | **[deleteAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-deleteannouncement)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, long announcementId)<br>删除群公告  |
| [BMXErrorCode] | **[setName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String name)<br>设置群名称  |
| [BMXErrorCode] | **[setDescription](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setdescription)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String description)<br>设置群描述信息  |
| [BMXErrorCode] | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setextension)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String extension)<br>设置群扩展信息  |
| [BMXErrorCode] | **[setMyNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmynickname)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String nickname)<br>设置在群里的昵称  |
| [BMXErrorCode] | **[setMsgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setmsgpushmode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.MsgPushMode mode)<br>设置群消息通知模式  |
| [BMXErrorCode] | **[setJoinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setjoinauthmode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.JoinAuthMode mode)<br>设置入群审批模式  |
| [BMXErrorCode] | **[setInviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setinvitemode)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, BMXGroup.InviteMode mode)<br>设置邀请模式  |
| [BMXErrorCode] | **[setAllowMemberModify](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setallowmembermodify)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>设置是否允许群成员设置群信息  |
| [BMXErrorCode] | **[setEnableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setenablereadack)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>设置是否开启群消息已读功能  |
| [BMXErrorCode] | **[setHistoryVisible](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-sethistoryvisible)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean enable)<br>设置群成员是否开可见群历史聊天记录  |
| [BMXErrorCode] | **[setAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-setavatar)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, String avatarPath, FileProgressListener arg2)<br>设置群头像  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-downloadavatar)**([BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, boolean thumbnail, FileProgressListener arg2)<br>下载群头像  |
| void | **[addGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-addgrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>添加群组变化监听者  |
| void | **[removeGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md#function-removegrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>移除群组变化监听者  |

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

获取群组列表，如果设置了forceRefresh则从服务器拉取 

**Parameters**: 

  * **list** 群组id列表，传入空列表函数返回后从此处获取返回的群组id列表 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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
  * **group** 搜索返回的群组信息，传入指向为空的shared_ptr对象函数执行后从此获取返回结果 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 


**Return**: [BMXErrorCode]

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
  * **group** 搜索返回的群组信息，传入指向为空的shared_ptr对象函数执行后从此获取返回结果 
  * **forceUpdate** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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
  * **group** 创建好的群，传入指向为空的shared_ptr对象函数执行后从此获取返回结果 


**Return**: [BMXErrorCode]

### function destroy

```java
inline BMXErrorCode destroy(
    BMXGroup group
)
```

销毁群 

**Parameters**: 

  * **group** 要销毁的群组 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function leave

```java
inline BMXErrorCode leave(
    BMXGroup group
)
```

退出群 

**Parameters**: 

  * **group** 要退出的群组 


**Return**: [BMXErrorCode]

### function getInfo

```java
inline BMXErrorCode getInfo(
    BMXGroup group
)
```

获取群详情，从服务端拉取最新信息 

**Parameters**: 

  * **group** 要获取群组最新信息的群组 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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

  * **result** 分页获取的群组邀请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


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

分页获取群组申请列表 

**Parameters**: 

  * **list** 需要获取群组申请列表信息的群组id列表 
  * **result** 分页获取的群组申请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


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

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500. 

**Parameters**: 

  * **group** 进行操作的群组 
  * **result** 分页获取的群成员列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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

分页获取黑名单 

**Parameters**: 

  * **group** 进行操作的群组 
  * **result** 分页获取的黑名单列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


**Return**: [BMXErrorCode]

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

禁言 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 被禁言的群成员id列表 
  * **duration** 禁言时长 
  * **reason** 禁言原因 


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

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言） 

**Parameters**: 

  * **group** 进行操作的群组 
  * **duration** 禁言时长(分钟) 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function unbanGroup

```java
inline BMXErrorCode unbanGroup(
    BMXGroup group
)
```

全员解除禁言 

**Parameters**: 

  * **group** 进行操作的群组 


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

分页获取禁言列表 

**Parameters**: 

  * **group** 进行操作的群组 
  * **result** 分页获取的禁言列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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

接受入群邀请 

**Parameters**: 

  * **group** 进行操作的群组 
  * **inviter** 邀请者id 


**Return**: [BMXErrorCode]

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

转移群主 

**Parameters**: 

  * **group** 进行操作的群组 
  * **newOwnerId** 转让为新群主的用户id 


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

添加群共享文件 

**Parameters**: 

  * **group** 进行操作的群组 
  * **filePath** 文件的本地路径 
  * **displayName** 文件的展示名 
  * **extensionName** 文件的扩展名 
  * **arg4** 上传回调函数 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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
  * **announcement** 最新的群组公告，传入指向为空的shared_ptr对象函数返回后从此处获取最新的群组公告 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function addGroupListener

```java
inline void addGroupListener(
    BMXGroupServiceListener listener
)
```

添加群组变化监听者 

**Parameters**: 

  * **listener** 群组变化监听者 


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