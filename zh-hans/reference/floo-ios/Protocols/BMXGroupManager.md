# BMXGroupManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXGroupManager.h  

## Instance Methods

<a name="//api/name/acceptApplicationByGroup:applicantId:completion:" title="acceptApplicationByGroup:applicantId:completion:"></a>
### acceptApplicationByGroup:applicantId:completion:

接受入群申请

`- (void)acceptApplicationByGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
接受入群申请

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/acceptInvitationByGroup:inviter:completion:" title="acceptInvitationByGroup:inviter:completion:"></a>
### acceptInvitationByGroup:inviter:completion:

接受入群邀请

`- (void)acceptInvitationByGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
接受入群邀请

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addAdmins:admins:message:completion:" title="addAdmins:admins:message:completion:"></a>
### addAdmins:admins:message:completion:

  添加管理员

`- (void)addAdmins:(BMXGroup *)*group* admins:(NSArray<NSNumber*> *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*admins*  
   Array：id  

*message*  
   String  

*aCompletionBlock*  
   BMXError  

#### Discussion
  添加管理员

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addGroupListener:" title="addGroupListener:"></a>
### addGroupListener:

添加群组变化监听者

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Discussion
添加群组变化监听者

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addMembersToGroup:memberIdlist:message:completion:" title="addMembersToGroup:memberIdlist:message:completion:"></a>
### addMembersToGroup:memberIdlist:message:completion:

  添加群成员

`- (void)addMembersToGroup:(BMXGroup *)*group* memberIdlist:(NSArray<NSNumber*> *)*memberIdlist* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*memberIdlist*  
   id数组  

*message*  
   添加信息  

*aCompletionBlock*  
   BMXError  

#### Discussion
  添加群成员

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/banGroup:duration:completion:" title="banGroup:duration:completion:"></a>
### banGroup:duration:completion:

全员禁言

`- (void)banGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
全员禁言

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/banMembers:group:reason:duration:completion:" title="banMembers:group:reason:duration:completion:"></a>
### banMembers:group:reason:duration:completion:

禁言

`- (void)banMembers:(NSArray<NSNumber*> *)*members* group:(BMXGroup *)*group* reason:(NSString *)*reason* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
禁言

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/blockMembers:members:completion:" title="blockMembers:members:completion:"></a>
### blockMembers:members:completion:

添加黑名单

`- (void)blockMembers:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
添加黑名单

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/creatGroupWithCreateGroupOption:completion:" title="creatGroupWithCreateGroupOption:completion:"></a>
### creatGroupWithCreateGroupOption:completion:

创建群

`- (void)creatGroupWithCreateGroupOption:(BMXCreatGroupOption *)*option* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*option*  
   <a href="../Classes/BMXCreatGroupOption.md">BMXCreatGroupOption</a>  

*aCompletionBlock*  
   Group info ,Error  

#### Discussion
创建群

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/declineApplicationByGroup:applicantId:completion:" title="declineApplicationByGroup:applicantId:completion:"></a>
### declineApplicationByGroup:applicantId:completion:

拒绝入群申请

`- (void)declineApplicationByGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
拒绝入群申请

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/declineInvitationByGroup:inviter:completion:" title="declineInvitationByGroup:inviter:completion:"></a>
### declineInvitationByGroup:inviter:completion:

拒绝入群邀请

`- (void)declineInvitationByGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
拒绝入群邀请

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:completion:" title="deleteAnnouncementWithGroup:announcementId:completion:"></a>
### deleteAnnouncementWithGroup:announcementId:completion:

删除群公告

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
删除群公告

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/destroyGroup:completion:" title="destroyGroup:completion:"></a>
### destroyGroup:completion:

销毁群(群主权限)

`- (void)destroyGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   Error  

#### Discussion
销毁群(群主权限)

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/downloadAvatarWithGroup:progress:completion:" title="downloadAvatarWithGroup:progress:completion:"></a>
### downloadAvatarWithGroup:progress:completion:

下载群头像

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
下载群头像

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/downloadSharedFileFromGroup:shareFile:progress:completion:" title="downloadSharedFileFromGroup:shareFile:progress:completion:"></a>
### downloadSharedFileFromGroup:shareFile:progress:completion:

下载群共享文件

`- (void)downloadSharedFileFromGroup:(BMXGroup *)*group* shareFile:(BMXGroupSharedFile *)*shareFile* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
下载群共享文件

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/editGroupAnnouncement:title:content:completion:" title="editGroupAnnouncement:title:content:completion:"></a>
### editGroupAnnouncement:title:content:completion:

设置群公告

`- (void)editGroupAnnouncement:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
设置群公告

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getAdmins:forceRefresh:completion:" title="getAdmins:forceRefresh:completion:"></a>
### getAdmins:forceRefresh:completion:

  获取Admins列表，如果设置了forceRefresh则从服务器拉取

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *, BMXError *error ))*aCompletionBlock*`

#### Discussion
  获取Admins列表，如果设置了forceRefresh则从服务器拉取

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getAnnouncementListWithGroup:forceRefresh:completion:" title="getAnnouncementListWithGroup:forceRefresh:completion:"></a>
### getAnnouncementListWithGroup:forceRefresh:completion:

获取群公告列表

`- (void)getAnnouncementListWithGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *annoucmentArray , BMXError *error ))*aCompletionBlock*`

#### Discussion
获取群公告列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getApplicationListByCursor:pageSize:completion:" title="getApplicationListByCursor:pageSize:completion:"></a>
### getApplicationListByCursor:pageSize:completion:

分页获取群组申请列表

`- (void)getApplicationListByCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *applicationList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Discussion
分页获取群组申请列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBannedMembersByGroup:completion:" title="getBannedMembersByGroup:completion:"></a>
### getBannedMembersByGroup:completion:

获取禁言列表

`- (void)getBannedMembersByGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( NSArray<BMXGroupBannedMember*> *bannedMemberList , BMXError *error ))*aCompletionBlock*`

#### Discussion
获取禁言列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBlockList:cursor:pageSize:completion:" title="getBlockList:cursor:pageSize:completion:"></a>
### getBlockList:cursor:pageSize:completion:

  分页获取黑名单

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *memberList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupMember *> *memberList,  

#### Discussion
  分页获取黑名单

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBlockListByGroup:forceRefresh:completion:" title="getBlockListByGroup:forceRefresh:completion:"></a>
### getBlockListByGroup:forceRefresh:completion:

获取黑名单

`- (void)getBlockListByGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *, BMXError *error ))*aCompletionBlock*`

#### Discussion
获取黑名单

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupByName:completion:" title="getGroupByName:completion:"></a>
### getGroupByName:completion:

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

`- (void)getGroupByName:(NSString *)*name* completion:(void ( ^ ) ( NSArray *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*name*  
   查询的群名称关键字  

*aCompletionBlock*  
   搜索结果返回的群列表信息,<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>  

#### Discussion
通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupInfoByGroupId:forceRefresh:completion:" title="getGroupInfoByGroupId:forceRefresh:completion:"></a>
### getGroupInfoByGroupId:forceRefresh:completion:

获取群信息

`- (void)getGroupInfoByGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*groupId*  
   群id  

*forceRefresh*  
   如果设置了forceRefresh则从服务器拉取  

*aCompletionBlock*  
   群  

#### Discussion
获取群信息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupInfoByGroupIdArray:forceRefresh:completion:" title="getGroupInfoByGroupIdArray:forceRefresh:completion:"></a>
### getGroupInfoByGroupIdArray:forceRefresh:completion:

获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取

`- (void)getGroupInfoByGroupIdArray:(NSArray<NSNumber*> *)*groupIdArray* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *aGroups , BMXError *aError ))*aCompletionBlock*`

#### Discussion
获取传入群组id的群组信息列表，如果设置了forceRefresh则从服务器拉取

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupListForceRefresh:completion:" title="getGroupListForceRefresh:completion:"></a>
### getGroupListForceRefresh:completion:

获取群组列表

`- (void)getGroupListForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   如果设置了forceRefresh则从服务器拉取  

*aCompletionBlock*  
   GroupList, Error  

#### Discussion
获取群组列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getInvitationListByCursor:pageSize:completion:" title="getInvitationListByCursor:pageSize:completion:"></a>
### getInvitationListByCursor:pageSize:completion:

分页获取群组邀请列表

`- (void)getInvitationListByCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *invitationList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupInvitation *> *invitationList,  

#### Discussion
分页获取群组邀请列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getLatestAnnouncementWithGroup:forceRefresh:completion:" title="getLatestAnnouncementWithGroup:forceRefresh:completion:"></a>
### getLatestAnnouncementWithGroup:forceRefresh:completion:

获取最新的群公告

`- (void)getLatestAnnouncementWithGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnounment *groupAnnounment , BMXError *error ))*aCompletionBlock*`

#### Discussion
获取最新的群公告

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMemberList:cursor:pageSize:completion:" title="getMemberList:cursor:pageSize:completion:"></a>
### getMemberList:cursor:pageSize:completion:

分页获取群成员列表

`- (void)getMemberList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *memberList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*cursor*  
   String  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupMember *> *memberList,  

#### Discussion
分页获取群成员列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMembers:forceRefresh:completion:" title="getMembers:forceRefresh:completion:"></a>
### getMembers:forceRefresh:completion:

获取群成员列表，

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*forceRefresh*  
   如果设置了forceRefresh则从服务器拉取，最多拉取1000人  

*aCompletionBlock*  
   List:BMXGroupMember ,BMXError  

#### Discussion
获取群成员列表，

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMembersNickName:memberIdlist:completion:" title="getMembersNickName:memberIdlist:completion:"></a>
### getMembersNickName:memberIdlist:completion:

批量获取群组成员昵称

`- (void)getMembersNickName:(BMXGroup *)*group* memberIdlist:(NSArray<NSNumber*> *)*memberIdlist* completion:(void ( ^ ) ( NSArray *aGroupMembers , BMXError *aError ))*aCompletionBlock*`

#### Discussion
批量获取群组成员昵称

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getSharedFilesListByGroup:forceRefresh:completion:" title="getSharedFilesListByGroup:forceRefresh:completion:"></a>
### getSharedFilesListByGroup:forceRefresh:completion:

获取群共享文件列表

`- (void)getSharedFilesListByGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupSharedFile*> *sharedFileList , BMXError *error ))*aCompletionBlock*`

#### Discussion
获取群共享文件列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getbannedMemberListGroup:cursor:pageSize:completion:" title="getbannedMemberListGroup:cursor:pageSize:completion:"></a>
### getbannedMemberListGroup:cursor:pageSize:completion:

分页获取禁言列表

`- (void)getbannedMemberListGroup:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *memberList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupMember *> *memberList  

#### Discussion
分页获取禁言列表

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/joinGroup:message:completion:" title="joinGroup:message:completion:"></a>
### joinGroup:message:completion:

加入一个群，根据群设置可能需要管理员批准

`- (void)joinGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*message*  
   申请信息  

*aCompletionBlock*  
   Error  

#### Discussion
加入一个群，根据群设置可能需要管理员批准

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/leaveGroup:completion:" title="leaveGroup:completion:"></a>
### leaveGroup:completion:

退出群

`- (void)leaveGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   Error  

#### Discussion
退出群

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/loadGroupInfo:completion:" title="loadGroupInfo:completion:"></a>
### loadGroupInfo:completion:

获取群详情，从服务端拉取最新信息

`- (void)loadGroupInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>,BMXError  

#### Discussion
获取群详情，从服务端拉取最新信息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/muteMessageByGroup:msgMuteMode:completion:" title="muteMessageByGroup:msgMuteMode:completion:"></a>
### muteMessageByGroup:msgMuteMode:completion:

屏蔽群消息

`- (void)muteMessageByGroup:(BMXGroup *)*group* msgMuteMode:(BMXGroupMsgMuteMode)*msgMuteMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
屏蔽群消息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeAdmins:admins:reason:completion:" title="removeAdmins:admins:reason:completion:"></a>
### removeAdmins:admins:reason:completion:

删除管理员

`- (void)removeAdmins:(BMXGroup *)*group* admins:(NSArray<NSNumber*> *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*admins*  
   Array：id  

*reason*  
   String  

*aCompletionBlock*  
   BMXError  

#### Discussion
删除管理员

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

<a name="//api/name/removeGroupListener:" title="removeGroupListener:"></a>
### removeGroupListener:

移除群组变化监听者

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Discussion
移除群组变化监听者

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeMembersWithGroup:memberlist:reason:completion:" title="removeMembersWithGroup:memberlist:reason:completion:"></a>
### removeMembersWithGroup:memberlist:reason:completion:

删除群成员

`- (void)removeMembersWithGroup:(BMXGroup *)*group* memberlist:(NSArray<NSNumber*> *)*memberList* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*memberList*  
   memberlist  

*reason*  
   reason  

*aCompletionBlock*  
   BMXError  

#### Discussion
删除群成员

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeSharedFileFromGroup:file:completion:" title="removeSharedFileFromGroup:file:completion:"></a>
### removeSharedFileFromGroup:file:completion:

移除群共享文件

`- (void)removeSharedFileFromGroup:(BMXGroup *)*group* file:(BMXGroupSharedFile *)*file* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
移除群共享文件

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setAllowMemberModifyWithGroup:enable:completion:" title="setAllowMemberModifyWithGroup:enable:completion:"></a>
### setAllowMemberModifyWithGroup:enable:completion:

设置是否允许群成员设置群信息

`- (void)setAllowMemberModifyWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否允许操作  

*aCompletionBlock*  
   BMXError  

#### Discussion
设置是否允许群成员设置群信息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setAvatarWithGroup:avatarData:progress:completion:" title="setAvatarWithGroup:avatarData:progress:completion:"></a>
### setAvatarWithGroup:avatarData:progress:completion:

设置群头像

`- (void)setAvatarWithGroup:(BMXGroup *)*group* avatarData:(NSData *)*avatarData* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
设置群头像

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setEnableReadAckWithGroup:enable:completion:" title="setEnableReadAckWithGroup:enable:completion:"></a>
### setEnableReadAckWithGroup:enable:completion:

设置是否开启群消息已读功能

`- (void)setEnableReadAckWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

*aCompletionBlock*  
   BMXError  

#### Discussion
设置是否开启群消息已读功能

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupDescription:description:completion:" title="setGroupDescription:description:completion:"></a>
### setGroupDescription:description:completion:

设置群描述信息

`- (void)setGroupDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置群描述信息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupExtensionWithGroup:extension:completion:" title="setGroupExtensionWithGroup:extension:completion:"></a>
### setGroupExtensionWithGroup:extension:completion:

设置群扩展信息

`- (void)setGroupExtensionWithGroup:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置群扩展信息

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupName:name:completion:" title="setGroupName:name:completion:"></a>
### setGroupName:name:completion:

设置群名称

`- (void)setGroupName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
设置群名称

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setHistoryVisibleWithGroup:enable:completion:" title="setHistoryVisibleWithGroup:enable:completion:"></a>
### setHistoryVisibleWithGroup:enable:completion:

设置群成员是否开可见群历史聊天记录

`- (void)setHistoryVisibleWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

*aCompletionBlock*  
   BMXError  

#### Discussion
设置群成员是否开可见群历史聊天记录

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setInviteModeWithGroup:mode:completion:" title="setInviteModeWithGroup:mode:completion:"></a>
### setInviteModeWithGroup:mode:completion:

设置邀请模式

`- (void)setInviteModeWithGroup:(BMXGroup *)*group* mode:(BMXGroupInviteMode)*inviteMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置邀请模式

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setJoinAuthModeWithGroup:joinAuthMode:completion:" title="setJoinAuthModeWithGroup:joinAuthMode:completion:"></a>
### setJoinAuthModeWithGroup:joinAuthMode:completion:

设置入群审批模式

`- (void)setJoinAuthModeWithGroup:(BMXGroup *)*group* joinAuthMode:(BMXGroupJoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置入群审批模式

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setMsgPushModeWithGroup:mode:completion:" title="setMsgPushModeWithGroup:mode:completion:"></a>
### setMsgPushModeWithGroup:mode:completion:

设置群消息通知模式

`- (void)setMsgPushModeWithGroup:(BMXGroup *)*group* mode:(BMXGroupMsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置群消息通知模式

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setMyNicknameWithGroup:nickName:completion:" title="setMyNicknameWithGroup:nickName:completion:"></a>
### setMyNicknameWithGroup:nickName:completion:

设置在群里的昵称

`- (void)setMyNicknameWithGroup:(BMXGroup *)*group* nickName:(NSString *)*nickName* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置在群里的昵称

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/transferOwnerByGroup:newOwnerId:completion:" title="transferOwnerByGroup:newOwnerId:completion:"></a>
### transferOwnerByGroup:newOwnerId:completion:

转移群主

`- (void)transferOwnerByGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
转移群主

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unbanGroup:completion:" title="unbanGroup:completion:"></a>
### unbanGroup:completion:

解除全员禁言

`- (void)unbanGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
解除全员禁言

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unbanMembersByGroup:members:reason:completion:" title="unbanMembersByGroup:members:reason:completion:"></a>
### unbanMembersByGroup:members:reason:completion:

解除禁言

`- (void)unbanMembersByGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
解除禁言

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unblockMember:members:completion:" title="unblockMember:members:completion:"></a>
### unblockMember:members:completion:

从黑名单删除

`- (void)unblockMember:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
从黑名单删除

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:" title="uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:"></a>
### uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:

添加群共享文件

`- (void)uploadSharedFileToGroup:(BMXGroup *)*group* filePathStr:(NSString *)*filePathStr* displayName:(NSString *)*displayName* extionName:(NSString *)*extionName* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
添加群共享文件

#### Declared In
* `BMXGroupManager.h`

