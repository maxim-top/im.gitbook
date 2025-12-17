---
title: im::floo::floolib::BMXGroupManager
summary: 群组管理器
---

# im::floo::floolib::BMXGroupManager

群组管理器

## Public Functions

|      | Name                                                                                                                                                                                                                                                                                                                                                                              |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroupManager**](classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bmxgroupmanager)([BMXGroupService](classim_1_1floo_1_1floolib_1_1_b_m_x_group_service.md) service)                                                                                                                                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupList > callBack)<br>获取群组列表，如果设置了forceRefresh则从服务器拉取</p>                                                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final ListOfLongLong groupIdList, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupList > callBack)<br>获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取</p>                                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getgrouplist"><strong>getGroupList</strong></a>(final long groupId, final boolean forceUpdate, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>获取群信息，如果设置了forceRefresh则从服务器拉取</p>                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinvitationlist"><strong>getInvitationList</strong></a>(final String cursor, final int pageSize, final BMXDataCallBack&#x3C; GroupInvitaionPage > callBack)<br>分页获取群组邀请列表</p>                                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(final BMXGroupList list, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; GroupApplicationPage > callBack)<br>分页获取群组申请列表</p>                                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-create"><strong>create</strong></a>(final BMXGroupService.CreateGroupOptions options, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>创建群</p>                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-destroy"><strong>destroy</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>销毁群</p>                                                                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-join"><strong>join</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String message, final BMXCallBack callBack)<br>加入一个群，根据群设置可能需要管理员批准</p>                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-leave"><strong>leave</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>退出群</p>                                                                                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getinfo"><strong>getInfo</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> > callBack)<br>获取群详情，从服务端拉取最新信息</p>                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers"><strong>getMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupMemberResultPage > callBack)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人</p>              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getmembers"><strong>getMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人</p>                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addmembers"><strong>addMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final String message, final BMXCallBack callBack)<br>添加群成员</p>                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removemembers"><strong>removeMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final String reason, final BMXCallBack callBack)<br>删除群成员</p>                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addadmins"><strong>addAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong admins, final String message, final BMXCallBack callBack)<br>添加管理员</p>                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removeadmins"><strong>removeAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong admins, final String reason, final BMXCallBack callBack)<br>删除管理员</p>                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getadmins"><strong>getAdmins</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>获取Admins列表，如果设置了forceRefresh则从服务器拉取</p>                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-blockmembers"><strong>blockMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>添加黑名单</p>                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unblockmembers"><strong>unblockMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>从黑名单删除</p>                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupMemberResultPage > callBack)<br>获取黑名单</p>                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupMemberList > callBack)<br>获取黑名单</p>                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-banmembers"><strong>banMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final long duration, final String reason, final BMXCallBack callBack)<br>禁言</p>                                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-bangroup"><strong>banGroup</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long duration, final BMXCallBack callBack)<br>全员禁言</p>                                                                                                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbanmembers"><strong>unbanMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final ListOfLongLong members, final BMXCallBack callBack)<br>解除禁言</p>                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-unbangroup"><strong>unbanGroup</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXCallBack callBack)<br>解除全员禁言</p>                                                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String cursor, final int pageSize, final BMXDataCallBack&#x3C; BMXGroupBannedMemberResultPage > callBack)<br>获取禁言列表</p>                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getbannedmembers"><strong>getBannedMembers</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXDataCallBack&#x3C; BMXGroupBannedMemberList > callBack)<br>获取禁言列表</p>                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-mutemessage"><strong>muteMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.MsgMuteMode mode, final BMXCallBack callBack)<br>设置是否屏蔽群消息</p>                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptapplication"><strong>acceptApplication</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long applicantId, final BMXCallBack callBack)<br>接受入群申请</p>                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineapplication"><strong>declineApplication</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long applicantId, final String reason, final BMXCallBack callBack)<br>拒绝入群申请</p>                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-acceptinvitation"><strong>acceptInvitation</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long inviter, final BMXCallBack callBack)<br>接受入群邀请</p>                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-declineinvitation"><strong>declineInvitation</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long inviter, final BMXCallBack callBack)<br>拒绝入群邀请</p>                                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-transferowner"><strong>transferOwner</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long newOwnerId, final BMXCallBack callBack)<br>转移群主</p>                                                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-uploadsharedfile"><strong>uploadSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String filePath, final String displayName, final String extensionName, final FileProgressListener listener, final BMXCallBack callBack)<br>添加群共享文件</p> |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removesharedfile"><strong>removeSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final BMXCallBack callBack)<br>移除群共享文件</p>                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadsharedfile"><strong>downloadSharedFile</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final FileProgressListener listener, final BMXCallBack callBack)<br>下载群共享文件</p>                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getsharedfileslist"><strong>getSharedFilesList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupSharedFileList > callBack)<br>获取群共享文件列表</p>                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-changesharedfilename"><strong>changeSharedFileName</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.SharedFile sharedFile, final String name, final BMXCallBack callBack)<br>修改群共享文件名称</p>                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getlatestannouncement"><strong>getLatestAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroup.Announcement > callBack)<br>获取最新的群公告</p>                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-getannouncementlist"><strong>getAnnouncementList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXGroupAnnouncementList > callBack)<br>获取群公告列表</p>                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-editannouncement"><strong>editAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String title, final String content, final BMXCallBack callBack)<br>设置群公告</p>                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-deleteannouncement"><strong>deleteAnnouncement</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final long announcementId, final BMXCallBack callBack)<br>删除群公告</p>                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setname"><strong>setName</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String name, final BMXCallBack callBack)<br>设置群名称</p>                                                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setdescription"><strong>setDescription</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String description, final BMXCallBack callBack)<br>设置群描述信息</p>                                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setextension"><strong>setExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String extension, final BMXCallBack callBack)<br>设置群扩展信息</p>                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmynickname"><strong>setMyNickname</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String nickname, final BMXCallBack callBack)<br>设置在群里的昵称</p>                                                                                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setmsgpushmode"><strong>setMsgPushMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.MsgPushMode mode, final BMXCallBack callBack)<br>设置群消息通知模式</p>                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setjoinauthmode"><strong>setJoinAuthMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.JoinAuthMode mode, final BMXCallBack callBack)<br>设置入群审批模式</p>                                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setinvitemode"><strong>setInviteMode</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final BMXGroup.InviteMode mode, final BMXCallBack callBack)<br>设置邀请模式</p>                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setavatar"><strong>setAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>设置群头像</p>                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final FileProgressListener listener, final BMXCallBack callBack)<br>下载群头像</p>                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-addgrouplistener"><strong>addGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>添加群组变化监听者</p>                                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-removegrouplistener"><strong>removeGroupListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_service_listener.md">BMXGroupServiceListener</a> listener)<br>移除群组变化监听者</p>                                                                                                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_manager.md#function-setenablereadack"><strong>setEnableReadAck</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md">BMXGroup</a> group, final boolean enable, final BMXCallBack callBack)<br>设置是否开启群消息已读功能</p>                                                                                       |

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

获取群组列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],群组id列表

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

获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupIdList** 群组id列表
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],群组详细信息列表

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

获取群信息，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **groupId** 要搜索的群组id
* **forceUpdate** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],搜索返回的群组信息

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

分页获取群组邀请列表

**Parameters**:

* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode],分页获取的群组邀请列表

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

分页获取群组申请列表

**Parameters**:

* **list** 需要获取群组申请列表信息的群组id列表
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode],分页获取的群组申请列表

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

创建群

**Parameters**:

* **options** 创建群组时传入的参数选项
* **callBack** \[BMXErrorCode],创建好的群

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

销毁群

**Parameters**:

* **callBack** BMXErrorCode，要销毁的群组

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

加入一个群，根据群设置可能需要管理员批准

**Parameters**:

* **group** 要加入的群组
* **message** 申请入群的信息
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

退出群

**Parameters**:

* **group** 要退出的群组
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

获取群详情，从服务端拉取最新信息

**Parameters**:

* **callBack** \[BMXErrorCode],要获取群组最新信息的群组

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

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

**Parameters**:

* **group** 进行操作的群组
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode],群成员列表

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

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],群成员列表

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

添加群成员

**Parameters**:

* **group** 进行操作的群组
* **members** 要添加进群的成员id列表
* **message** 添加成员原因信息
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

删除群成员

**Parameters**:

* **group** 进行操作的群组
* **members** 要删除的群组成员id列表
* **reason** 删除的原因
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

添加管理员

**Parameters**:

* **group** 进行操作的群组
* **admins** 要添加为管理员的成员id列表
* **message** 添加为管理员的原因
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

删除管理员

**Parameters**:

* **group** 进行操作的群组
* **admins** 要从管理员移除的成员id列表
* **reason** 要移除管理员的原因
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

获取Admins列表，如果设置了forceRefresh则从服务器拉取

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],群管理员列表

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

添加黑名单

**Parameters**:

* **group** 进行操作的群组
* **members** 要加入黑名单的群成员id列表
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

从黑名单删除

**Parameters**:

* **group** 进行操作的群组
* **members** 从黑名单移除的用户id列表
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

获取黑名单

**Parameters**:

* **group** 进行操作的群组
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode],群黑名单列表

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

获取黑名单

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode],群黑名单列表

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

禁言

**Parameters**:

* **group** 进行操作的群组
* **members** 被禁言的群成员id列表
* **duration** 禁言时长
* **reason** 禁言原因
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

全员禁言

**Parameters**:

* **group** 进行操作的群组
* **duration** 禁言时长
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

解除禁言

**Parameters**:

* **group** 进行操作的群组
* **members** 被解除禁言的群成员id列表
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

解除全员禁言

**Parameters**:

* **group** 进行操作的群组
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

获取禁言列表

**Parameters**:

* **group** 进行操作的群组
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode] 群禁言列表

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

获取禁言列表

**Parameters**:

* **group** 进行操作的群组
* **callBack** \[BMXErrorCode] 群禁言列表

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

设置是否屏蔽群消息

**Parameters**:

* **group** 进行操作的群组
* **mode** 群屏蔽的模式
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

接受入群申请

**Parameters**:

* **group** 进行操作的群组
* **applicantId** 申请进群的用户id
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

拒绝入群申请

**Parameters**:

* **group** 进行操作的群组
* **applicantId** 申请进群的用户id
* **reason** 拒绝的原因
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

接受入群邀请

**Parameters**:

* **group** 进行操作的群组
* **inviter** 邀请者id
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

拒绝入群邀请

**Parameters**:

* **group** 进行操作的群组
* **inviter** 邀请者id
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

转移群主

**Parameters**:

* **group** 进行操作的群组
* **newOwnerId** 转让为新群主的用户id
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

添加群共享文件

**Parameters**:

* **group** 进行操作的群组
* **filePath** 文件的本地路径
* **displayName** 文件的展示名
* **extensionName** 文件的扩展名
* **listener** 上传回调函数
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

移除群共享文件

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 删除的群共享文件
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

下载群共享文件

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 下载的群共享文件
* **listener** 下载回调函数
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

获取群共享文件列表

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode] 群共享文件列表

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

修改群共享文件名称

**Parameters**:

* **group** 进行操作的群组
* **sharedFile** 进行更改的群共享文件
* **name** 修改的群共享文件名称
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

获取最新的群公告

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode] 最新的群组公告

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

获取群公告列表

**Parameters**:

* **group** 进行操作的群组
* **forceRefresh** 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
* **callBack** \[BMXErrorCode], 群公告列表

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

设置群公告

**Parameters**:

* **group** 进行操作的群组
* **title** 群公告的标题
* **content** 群公告的内容
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

删除群公告

**Parameters**:

* **group** 进行操作的群组
* **announcementId** 删除的群公告id
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

设置群名称

**Parameters**:

* **group** 进行操作的群组
* **name** 群组名称
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

设置群描述信息

**Parameters**:

* **group** 进行操作的群组
* **description** 群组描述
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

设置群扩展信息

**Parameters**:

* **group** 进行操作的群组
* **extension** 群组的扩展信息
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

设置在群里的昵称

**Parameters**:

* **group** 进行操作的群组
* **nickname** 用户在群组内的昵称
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

设置群消息通知模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 群消息通知模式
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

设置入群审批模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 入群审批模式
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

设置邀请模式

**Parameters**:

* **group** 进行操作的群组
* **mode** 群组的邀请模式
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

设置群头像

**Parameters**:

* **group** 进行操作的群组
* **avatarPath** 群头像文件的本地路径
* **listener** 上传回调函数
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

下载群头像

**Parameters**:

* **group** 进行操作的群组
* **listener** 下载回调函数
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

添加群组变化监听者

**Parameters**:

* **listener** 群组变化监听者

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

移除群组变化监听者

**Parameters**:

* **listener** 群组变化监听者

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

设置是否开启群消息已读功能

**Parameters**:

* **group** 进行操作的群组
* **enable** 是否开启
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroupManager'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
