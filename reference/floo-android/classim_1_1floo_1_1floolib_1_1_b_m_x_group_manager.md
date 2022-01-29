---
title: im::floo::floolib::BMXGroupManager
summary: 群组管理器 

---

# im::floo::floolib::BMXGroupManager



群组管理器 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXGroupManager](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bmxgroupmanager)**([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) service) |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final boolean forceRefresh, final BMXDataCallBack< BMXGroupList > callBack)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取  |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final ListOfLongLong groupIdList, final boolean forceRefresh, final BMXDataCallBack< BMXGroupList > callBack)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取  |
| void | **[getGroupList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist)**(final long groupId, final boolean forceUpdate, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>获取群信息，如果设置了forceRefresh则从服务器拉取  |
| void | **[getInvitationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinvitationlist)**(final String cursor, final int pageSize, final BMXDataCallBack< GroupInvitaionPage > callBack)<br>分页获取群组邀请列表  |
| void | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getapplicationlist)**(final BMXGroupList list, final String cursor, final int pageSize, final BMXDataCallBack< GroupApplicationPage > callBack)<br>分页获取群组申请列表  |
| void | **[create](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-create)**(final BMXGroupService.CreateGroupOptions options, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>创建群  |
| void | **[destroy](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-destroy)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>销毁群  |
| void | **[join](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-join)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String message, final BMXCallBack callBack)<br>加入一个群，根据群设置可能需要管理员批准  |
| void | **[leave](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-leave)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>退出群  |
| void | **[getInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinfo)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXDataCallBack< [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) > callBack)<br>获取群详情，从服务端拉取最新信息  |
| void | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupMemberResultPage > callBack)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人  |
| void | **[getMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人  |
| void | **[addMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final String message, final BMXCallBack callBack)<br>添加群成员  |
| void | **[removeMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removemembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final String reason, final BMXCallBack callBack)<br>删除群成员  |
| void | **[addAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong admins, final String message, final BMXCallBack callBack)<br>添加管理员  |
| void | **[removeAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removeadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong admins, final String reason, final BMXCallBack callBack)<br>删除管理员  |
| void | **[getAdmins](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getadmins)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>获取Admins列表，如果设置了forceRefresh则从服务器拉取  |
| void | **[blockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-blockmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>添加黑名单  |
| void | **[unblockMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unblockmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>从黑名单删除  |
| void | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupMemberResultPage > callBack)<br>获取黑名单  |
| void | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupMemberList > callBack)<br>获取黑名单  |
| void | **[banMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-banmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final long duration, final String reason, final BMXCallBack callBack)<br>禁言  |
| void | **[banGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bangroup)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long duration, final BMXCallBack callBack)<br>全员禁言  |
| void | **[unbanMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbanmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final ListOfLongLong members, final BMXCallBack callBack)<br>解除禁言  |
| void | **[unbanGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbangroup)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXCallBack callBack)<br>解除全员禁言  |
| void | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String cursor, final int pageSize, final BMXDataCallBack< BMXGroupBannedMemberResultPage > callBack)<br>获取禁言列表  |
| void | **[getBannedMembers](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXDataCallBack< BMXGroupBannedMemberList > callBack)<br>获取禁言列表  |
| void | **[muteMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-mutemessage)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.MsgMuteMode mode, final BMXCallBack callBack)<br>设置是否屏蔽群消息  |
| void | **[acceptApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptapplication)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long applicantId, final BMXCallBack callBack)<br>接受入群申请  |
| void | **[declineApplication](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineapplication)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long applicantId, final String reason, final BMXCallBack callBack)<br>拒绝入群申请  |
| void | **[acceptInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptinvitation)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long inviter, final BMXCallBack callBack)<br>接受入群邀请  |
| void | **[declineInvitation](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineinvitation)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long inviter, final BMXCallBack callBack)<br>拒绝入群邀请  |
| void | **[transferOwner](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-transferowner)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long newOwnerId, final BMXCallBack callBack)<br>转移群主  |
| void | **[uploadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-uploadsharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String filePath, final String displayName, final String extensionName, final FileProgressListener listener, final BMXCallBack callBack)<br>添加群共享文件  |
| void | **[removeSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removesharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final BMXCallBack callBack)<br>移除群共享文件  |
| void | **[downloadSharedFile](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadsharedfile)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final FileProgressListener listener, final BMXCallBack callBack)<br>下载群共享文件  |
| void | **[getSharedFilesList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getsharedfileslist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupSharedFileList > callBack)<br>获取群共享文件列表  |
| void | **[changeSharedFileName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-changesharedfilename)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.SharedFile sharedFile, final String name, final BMXCallBack callBack)<br>修改群共享文件名称  |
| void | **[getLatestAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getlatestannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroup.Announcement > callBack)<br>获取最新的群公告  |
| void | **[getAnnouncementList](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getannouncementlist)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean forceRefresh, final BMXDataCallBack< BMXGroupAnnouncementList > callBack)<br>获取群公告列表  |
| void | **[editAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-editannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String title, final String content, final BMXCallBack callBack)<br>设置群公告  |
| void | **[deleteAnnouncement](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-deleteannouncement)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final long announcementId, final BMXCallBack callBack)<br>删除群公告  |
| void | **[setName](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setname)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String name, final BMXCallBack callBack)<br>设置群名称  |
| void | **[setDescription](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setdescription)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String description, final BMXCallBack callBack)<br>设置群描述信息  |
| void | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setextension)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String extension, final BMXCallBack callBack)<br>设置群扩展信息  |
| void | **[setMyNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmynickname)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String nickname, final BMXCallBack callBack)<br>设置在群里的昵称  |
| void | **[setMsgPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmsgpushmode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.MsgPushMode mode, final BMXCallBack callBack)<br>设置群消息通知模式  |
| void | **[setJoinAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setjoinauthmode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.JoinAuthMode mode, final BMXCallBack callBack)<br>设置入群审批模式  |
| void | **[setInviteMode](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setinvitemode)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final BMXGroup.InviteMode mode, final BMXCallBack callBack)<br>设置邀请模式  |
| void | **[setAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setavatar)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>设置群头像  |
| void | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadavatar)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final FileProgressListener listener, final BMXCallBack callBack)<br>下载群头像  |
| void | **[addGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addgrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>添加群组变化监听者  |
| void | **[removeGroupListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removegrouplistener)**([BMXGroupServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md) listener)<br>移除群组变化监听者  |
| void | **[setEnableReadAck](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setenablereadack)**(final [BMXGroup](classim_1_1floo_1_1floolib_1_1_b_m_x_group.md) group, final boolean enable, final BMXCallBack callBack)<br>设置是否开启群消息已读功能  |

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

获取群组列表，如果设置了forceRefresh则从服务器拉取 

**Parameters**: 

  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],群组id列表 


### function getGroupList

```java
inline void getGroupList(
    final ListOfLongLong groupIdList,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupList > callBack
)
```

获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取 

**Parameters**: 

  * **groupIdList** 群组id列表 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],群组详细信息列表 


### function getGroupList

```java
inline void getGroupList(
    final long groupId,
    final boolean forceUpdate,
    final BMXDataCallBack< BMXGroup > callBack
)
```

获取群信息，如果设置了forceRefresh则从服务器拉取 

**Parameters**: 

  * **groupId** 要搜索的群组id 
  * **forceUpdate** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],搜索返回的群组信息 


### function getInvitationList

```java
inline void getInvitationList(
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< GroupInvitaionPage > callBack
)
```

分页获取群组邀请列表 

**Parameters**: 

  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 
  * **callBack** [BMXErrorCode],分页获取的群组邀请列表 


### function getApplicationList

```java
inline void getApplicationList(
    final BMXGroupList list,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< GroupApplicationPage > callBack
)
```

分页获取群组申请列表 

**Parameters**: 

  * **list** 需要获取群组申请列表信息的群组id列表 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 
  * **callBack** [BMXErrorCode],分页获取的群组申请列表 


### function create

```java
inline void create(
    final BMXGroupService.CreateGroupOptions options,
    final BMXDataCallBack< BMXGroup > callBack
)
```

创建群 

**Parameters**: 

  * **options** 创建群组时传入的参数选项 
  * **callBack** [BMXErrorCode],创建好的群 


### function destroy

```java
inline void destroy(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

销毁群 

**Parameters**: 

  * **callBack** BMXErrorCode，要销毁的群组 


### function join

```java
inline void join(
    final BMXGroup group,
    final String message,
    final BMXCallBack callBack
)
```

加入一个群，根据群设置可能需要管理员批准 

**Parameters**: 

  * **group** 要加入的群组 
  * **message** 申请入群的信息 
  * **callBack** [BMXErrorCode]


### function leave

```java
inline void leave(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

退出群 

**Parameters**: 

  * **group** 要退出的群组 
  * **callBack** [BMXErrorCode]


### function getInfo

```java
inline void getInfo(
    final BMXGroup group,
    final BMXDataCallBack< BMXGroup > callBack
)
```

获取群详情，从服务端拉取最新信息 

**Parameters**: 

  * **callBack** [BMXErrorCode],要获取群组最新信息的群组 


### function getMembers

```java
inline void getMembers(
    final BMXGroup group,
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< BMXGroupMemberResultPage > callBack
)
```

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人 

**Parameters**: 

  * **group** 进行操作的群组 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 
  * **callBack** [BMXErrorCode],群成员列表 


### function getMembers

```java
inline void getMembers(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],群成员列表 


### function addMembers

```java
inline void addMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final String message,
    final BMXCallBack callBack
)
```

添加群成员 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 要添加进群的成员id列表 
  * **message** 添加成员原因信息 
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

删除群成员 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 要删除的群组成员id列表 
  * **reason** 删除的原因 
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

添加管理员 

**Parameters**: 

  * **group** 进行操作的群组 
  * **admins** 要添加为管理员的成员id列表 
  * **message** 添加为管理员的原因 
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

删除管理员 

**Parameters**: 

  * **group** 进行操作的群组 
  * **admins** 要从管理员移除的成员id列表 
  * **reason** 要移除管理员的原因 
  * **callBack** [BMXErrorCode]


### function getAdmins

```java
inline void getAdmins(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

获取Admins列表，如果设置了forceRefresh则从服务器拉取 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],群管理员列表 


### function blockMembers

```java
inline void blockMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

添加黑名单 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 要加入黑名单的群成员id列表 
  * **callBack** [BMXErrorCode]


### function unblockMembers

```java
inline void unblockMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

从黑名单删除 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 从黑名单移除的用户id列表 
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

获取黑名单 

**Parameters**: 

  * **group** 进行操作的群组 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 
  * **callBack** [BMXErrorCode],群黑名单列表 


### function getBlockList

```java
inline void getBlockList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupMemberList > callBack
)
```

获取黑名单 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode],群黑名单列表 


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

禁言 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 被禁言的群成员id列表 
  * **duration** 禁言时长 
  * **reason** 禁言原因 
  * **callBack** [BMXErrorCode]


### function banGroup

```java
inline void banGroup(
    final BMXGroup group,
    final long duration,
    final BMXCallBack callBack
)
```

全员禁言 

**Parameters**: 

  * **group** 进行操作的群组 
  * **duration** 禁言时长 
  * **callBack** [BMXErrorCode]


### function unbanMembers

```java
inline void unbanMembers(
    final BMXGroup group,
    final ListOfLongLong members,
    final BMXCallBack callBack
)
```

解除禁言 

**Parameters**: 

  * **group** 进行操作的群组 
  * **members** 被解除禁言的群成员id列表 
  * **callBack** [BMXErrorCode]


### function unbanGroup

```java
inline void unbanGroup(
    final BMXGroup group,
    final BMXCallBack callBack
)
```

解除全员禁言 

**Parameters**: 

  * **group** 进行操作的群组 
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

获取禁言列表 

**Parameters**: 

  * **group** 进行操作的群组 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 
  * **callBack** [BMXErrorCode] 群禁言列表 


### function getBannedMembers

```java
inline void getBannedMembers(
    final BMXGroup group,
    final BMXDataCallBack< BMXGroupBannedMemberList > callBack
)
```

获取禁言列表 

**Parameters**: 

  * **group** 进行操作的群组 
  * **callBack** [BMXErrorCode] 群禁言列表 


### function muteMessage

```java
inline void muteMessage(
    final BMXGroup group,
    final BMXGroup.MsgMuteMode mode,
    final BMXCallBack callBack
)
```

设置是否屏蔽群消息 

**Parameters**: 

  * **group** 进行操作的群组 
  * **mode** 群屏蔽的模式 
  * **callBack** [BMXErrorCode]


### function acceptApplication

```java
inline void acceptApplication(
    final BMXGroup group,
    final long applicantId,
    final BMXCallBack callBack
)
```

接受入群申请 

**Parameters**: 

  * **group** 进行操作的群组 
  * **applicantId** 申请进群的用户id 
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

拒绝入群申请 

**Parameters**: 

  * **group** 进行操作的群组 
  * **applicantId** 申请进群的用户id 
  * **reason** 拒绝的原因 
  * **callBack** [BMXErrorCode]


### function acceptInvitation

```java
inline void acceptInvitation(
    final BMXGroup group,
    final long inviter,
    final BMXCallBack callBack
)
```

接受入群邀请 

**Parameters**: 

  * **group** 进行操作的群组 
  * **inviter** 邀请者id 
  * **callBack** [BMXErrorCode]


### function declineInvitation

```java
inline void declineInvitation(
    final BMXGroup group,
    final long inviter,
    final BMXCallBack callBack
)
```

拒绝入群邀请 

**Parameters**: 

  * **group** 进行操作的群组 
  * **inviter** 邀请者id 
  * **callBack** [BMXErrorCode]


### function transferOwner

```java
inline void transferOwner(
    final BMXGroup group,
    final long newOwnerId,
    final BMXCallBack callBack
)
```

转移群主 

**Parameters**: 

  * **group** 进行操作的群组 
  * **newOwnerId** 转让为新群主的用户id 
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

添加群共享文件 

**Parameters**: 

  * **group** 进行操作的群组 
  * **filePath** 文件的本地路径 
  * **displayName** 文件的展示名 
  * **extensionName** 文件的扩展名 
  * **listener** 上传回调函数 
  * **callBack** [BMXErrorCode]


### function removeSharedFile

```java
inline void removeSharedFile(
    final BMXGroup group,
    final BMXGroup.SharedFile sharedFile,
    final BMXCallBack callBack
)
```

移除群共享文件 

**Parameters**: 

  * **group** 进行操作的群组 
  * **sharedFile** 删除的群共享文件 
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

下载群共享文件 

**Parameters**: 

  * **group** 进行操作的群组 
  * **sharedFile** 下载的群共享文件 
  * **listener** 下载回调函数 
  * **callBack** [BMXErrorCode]


### function getSharedFilesList

```java
inline void getSharedFilesList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupSharedFileList > callBack
)
```

获取群共享文件列表 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode] 群共享文件列表 


### function changeSharedFileName

```java
inline void changeSharedFileName(
    final BMXGroup group,
    final BMXGroup.SharedFile sharedFile,
    final String name,
    final BMXCallBack callBack
)
```

修改群共享文件名称 

**Parameters**: 

  * **group** 进行操作的群组 
  * **sharedFile** 进行更改的群共享文件 
  * **name** 修改的群共享文件名称 
  * **callBack** [BMXErrorCode]


### function getLatestAnnouncement

```java
inline void getLatestAnnouncement(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroup.Announcement > callBack
)
```

获取最新的群公告 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode] 最新的群组公告 


### function getAnnouncementList

```java
inline void getAnnouncementList(
    final BMXGroup group,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXGroupAnnouncementList > callBack
)
```

获取群公告列表 

**Parameters**: 

  * **group** 进行操作的群组 
  * **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取 
  * **callBack** [BMXErrorCode], 群公告列表 


### function editAnnouncement

```java
inline void editAnnouncement(
    final BMXGroup group,
    final String title,
    final String content,
    final BMXCallBack callBack
)
```

设置群公告 

**Parameters**: 

  * **group** 进行操作的群组 
  * **title** 群公告的标题 
  * **content** 群公告的内容 
  * **callBack** [BMXErrorCode]


### function deleteAnnouncement

```java
inline void deleteAnnouncement(
    final BMXGroup group,
    final long announcementId,
    final BMXCallBack callBack
)
```

删除群公告 

**Parameters**: 

  * **group** 进行操作的群组 
  * **announcementId** 删除的群公告id 
  * **callBack** [BMXErrorCode]


### function setName

```java
inline void setName(
    final BMXGroup group,
    final String name,
    final BMXCallBack callBack
)
```

设置群名称 

**Parameters**: 

  * **group** 进行操作的群组 
  * **name** 群组名称 
  * **callBack** [BMXErrorCode]


### function setDescription

```java
inline void setDescription(
    final BMXGroup group,
    final String description,
    final BMXCallBack callBack
)
```

设置群描述信息 

**Parameters**: 

  * **group** 进行操作的群组 
  * **description** 群组描述 
  * **callBack** [BMXErrorCode]


### function setExtension

```java
inline void setExtension(
    final BMXGroup group,
    final String extension,
    final BMXCallBack callBack
)
```

设置群扩展信息 

**Parameters**: 

  * **group** 进行操作的群组 
  * **extension** 群组的扩展信息 
  * **callBack** [BMXErrorCode]


### function setMyNickname

```java
inline void setMyNickname(
    final BMXGroup group,
    final String nickname,
    final BMXCallBack callBack
)
```

设置在群里的昵称 

**Parameters**: 

  * **group** 进行操作的群组 
  * **nickname** 用户在群组内的昵称 
  * **callBack** [BMXErrorCode]


### function setMsgPushMode

```java
inline void setMsgPushMode(
    final BMXGroup group,
    final BMXGroup.MsgPushMode mode,
    final BMXCallBack callBack
)
```

设置群消息通知模式 

**Parameters**: 

  * **group** 进行操作的群组 
  * **mode** 群消息通知模式 
  * **callBack** [BMXErrorCode]


### function setJoinAuthMode

```java
inline void setJoinAuthMode(
    final BMXGroup group,
    final BMXGroup.JoinAuthMode mode,
    final BMXCallBack callBack
)
```

设置入群审批模式 

**Parameters**: 

  * **group** 进行操作的群组 
  * **mode** 入群审批模式 
  * **callBack** [BMXErrorCode]


### function setInviteMode

```java
inline void setInviteMode(
    final BMXGroup group,
    final BMXGroup.InviteMode mode,
    final BMXCallBack callBack
)
```

设置邀请模式 

**Parameters**: 

  * **group** 进行操作的群组 
  * **mode** 群组的邀请模式 
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

设置群头像 

**Parameters**: 

  * **group** 进行操作的群组 
  * **avatarPath** 群头像文件的本地路径 
  * **listener** 上传回调函数 
  * **callBack** [BMXErrorCode]


### function downloadAvatar

```java
inline void downloadAvatar(
    final BMXGroup group,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

下载群头像 

**Parameters**: 

  * **group** 进行操作的群组 
  * **listener** 下载回调函数 
  * **callBack** [BMXErrorCode]


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


### function setEnableReadAck

```java
inline void setEnableReadAck(
    final BMXGroup group,
    final boolean enable,
    final BMXCallBack callBack
)
```

设置是否开启群消息已读功能 

**Parameters**: 

  * **group** 进行操作的群组 
  * **enable** 是否开启 
  * **callBack** [BMXErrorCode]


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800