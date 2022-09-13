# BMXGroupManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXGroupManager.h  

## Instance Methods

<a name="//api/name/acceptApplicationByGroup:applicantId:completion:" title="acceptApplicationByGroup:applicantId:completion:"></a>
### acceptApplicationByGroup:applicantId:completion:

Accept application of membership

`- (void)acceptApplicationByGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Accept application of membership

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/acceptInvitationByGroup:inviter:completion:" title="acceptInvitationByGroup:inviter:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="acceptApplicationByGroup:applicantId:completion:" %}{% endlanying_code_snippet %}
```
### acceptInvitationByGroup:inviter:completion:

Accept to join group

`- (void)acceptInvitationByGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Accept to join group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addAdmins:admins:message:completion:" title="addAdmins:admins:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="acceptInvitationByGroup:inviter:completion:" %}{% endlanying_code_snippet %}
```
### addAdmins:admins:message:completion:

  Add Admin

`- (void)addAdmins:(BMXGroup *)*group* admins:(NSArray<NSNumber*> *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*admins*  
   Array:id  

*message*  
   String  

*aCompletionBlock*  
   BMXError  

#### Discussion
  Add Admin

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="addAdmins:admins:message:completion:" %}{% endlanying_code_snippet %}
```
### addDelegate:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addGroupListener:" title="addGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addGroupListener:

Add group change listener

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Discussion
Add group change listener

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/addMembersToGroup:memberIdlist:message:completion:" title="addMembersToGroup:memberIdlist:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="addGroupListener:" %}{% endlanying_code_snippet %}
```
### addMembersToGroup:memberIdlist:message:completion:

  Add group member

`- (void)addMembersToGroup:(BMXGroup *)*group* memberIdlist:(NSArray<NSNumber*> *)*memberIdlist* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*memberIdlist*  
   id array  

*message*  
   Adding information  

*aCompletionBlock*  
   BMXError  

#### Discussion
  Add group member

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/banGroup:duration:completion:" title="banGroup:duration:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="addMembersToGroup:memberIdlist:message:completion:" %}{% endlanying_code_snippet %}
```
### banGroup:duration:completion:

Ban all members

`- (void)banGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Ban all members

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/banMembers:group:reason:duration:completion:" title="banMembers:group:reason:duration:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="banGroup:duration:completion:" %}{% endlanying_code_snippet %}
```
### banMembers:group:reason:duration:completion:

Ban

`- (void)banMembers:(NSArray<NSNumber*> *)*members* group:(BMXGroup *)*group* reason:(NSString *)*reason* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Ban

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/blockMembers:members:completion:" title="blockMembers:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="banMembers:group:reason:duration:completion:" %}{% endlanying_code_snippet %}
```
### blockMembers:members:completion:

Add to blacklist

`- (void)blockMembers:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Add to blacklist

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/creatGroupWithCreateGroupOption:completion:" title="creatGroupWithCreateGroupOption:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="blockMembers:members:completion:" %}{% endlanying_code_snippet %}
```
### creatGroupWithCreateGroupOption:completion:

Create group

`- (void)creatGroupWithCreateGroupOption:(BMXCreatGroupOption *)*option* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*option*  
   <a href="../Classes/BMXCreatGroupOption.md">BMXCreatGroupOption</a>  

*aCompletionBlock*  
   Group info ,Error  

#### Discussion
Create group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/declineApplicationByGroup:applicantId:completion:" title="declineApplicationByGroup:applicantId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="creatGroupWithCreateGroupOption:completion:" %}{% endlanying_code_snippet %}
```
### declineApplicationByGroup:applicantId:completion:

Reject application of membership

`- (void)declineApplicationByGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Reject application of membership

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/declineInvitationByGroup:inviter:completion:" title="declineInvitationByGroup:inviter:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="declineApplicationByGroup:applicantId:completion:" %}{% endlanying_code_snippet %}
```
### declineInvitationByGroup:inviter:completion:

Reject invitation to join group

`- (void)declineInvitationByGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Reject invitation to join group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:completion:" title="deleteAnnouncementWithGroup:announcementId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="declineInvitationByGroup:inviter:completion:" %}{% endlanying_code_snippet %}
```
### deleteAnnouncementWithGroup:announcementId:completion:

Delete group announcement

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
Delete group announcement

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/destroyGroup:completion:" title="destroyGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="deleteAnnouncementWithGroup:announcementId:completion:" %}{% endlanying_code_snippet %}
```
### destroyGroup:completion:

Destroy group (valid only for group Owner)

`- (void)destroyGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   Error  

#### Discussion
Destroy group (valid only for group Owner)

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/downloadAvatarWithGroup:progress:completion:" title="downloadAvatarWithGroup:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="destroyGroup:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithGroup:progress:completion:

Download group avatar

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
Download group avatar

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/downloadSharedFileFromGroup:shareFile:progress:completion:" title="downloadSharedFileFromGroup:shareFile:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="downloadAvatarWithGroup:progress:completion:" %}{% endlanying_code_snippet %}
```
### downloadSharedFileFromGroup:shareFile:progress:completion:

Download share file in group

`- (void)downloadSharedFileFromGroup:(BMXGroup *)*group* shareFile:(BMXGroupSharedFile *)*shareFile* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
Download share file in group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/editGroupAnnouncement:title:content:completion:" title="editGroupAnnouncement:title:content:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="downloadSharedFileFromGroup:shareFile:progress:completion:" %}{% endlanying_code_snippet %}
```
### editGroupAnnouncement:title:content:completion:

Write group announcement

`- (void)editGroupAnnouncement:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
Write group announcement

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getAdmins:forceRefresh:completion:" title="getAdmins:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="editGroupAnnouncement:title:content:completion:" %}{% endlanying_code_snippet %}
```
### getAdmins:forceRefresh:completion:

  Get Admins list, pull from server if forceRefreshed is set

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *, BMXError *error ))*aCompletionBlock*`

#### Discussion
  Get Admins list, pull from server if forceRefreshed is set

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getAnnouncementListWithGroup:forceRefresh:completion:" title="getAnnouncementListWithGroup:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getAdmins:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getAnnouncementListWithGroup:forceRefresh:completion:

Get group announcements list

`- (void)getAnnouncementListWithGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *annoucmentArray , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get group announcements list

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getApplicationListByCursor:pageSize:completion:" title="getApplicationListByCursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getAnnouncementListWithGroup:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getApplicationListByCursor:pageSize:completion:

Get a list of group applications in pages

`- (void)getApplicationListByCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *applicationList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get a list of group applications in pages

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBannedMembersByGroup:completion:" title="getBannedMembersByGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getApplicationListByCursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBannedMembersByGroup:completion:

Get a list of banned members

`- (void)getBannedMembersByGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( NSArray<BMXGroupBannedMember*> *bannedMemberList , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get a list of banned members

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBlockList:cursor:pageSize:completion:" title="getBlockList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getBannedMembersByGroup:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:cursor:pageSize:completion:

  Paged to get blacklist

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *memberList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupMember *> *memberList,  

#### Discussion
  Paged to get blacklist

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getBlockListByGroup:forceRefresh:completion:" title="getBlockListByGroup:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getBlockList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBlockListByGroup:forceRefresh:completion:

Get blacklist

`- (void)getBlockListByGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *, BMXError *error ))*aCompletionBlock*`

#### Discussion
Get blacklist

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupByName:completion:" title="getGroupByName:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getBlockListByGroup:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getGroupByName:completion:

Query local group information by group name and retrieve the group from local database by group name query

`- (void)getGroupByName:(NSString *)*name* completion:(void ( ^ ) ( NSArray *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*name*  
   Keyword of group name for query  

*aCompletionBlock*  
   Group list information returned by search result,<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>  

#### Discussion
Query local group information by group name and retrieve the group from local database by group name query

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupInfoByGroupId:forceRefresh:completion:" title="getGroupInfoByGroupId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getGroupByName:completion:" %}{% endlanying_code_snippet %}
```
### getGroupInfoByGroupId:forceRefresh:completion:

Get group information

`- (void)getGroupInfoByGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*groupId*  
   Group id  

*forceRefresh*  
   Pull from server if forceRefresh is set  

*aCompletionBlock*  
   Group  

#### Discussion
Get group information

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupInfoByGroupIdArray:forceRefresh:completion:" title="getGroupInfoByGroupIdArray:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getGroupInfoByGroupId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getGroupInfoByGroupIdArray:forceRefresh:completion:

Get the list of group information for the incoming group id, pull from server if forceRefreshed is set

`- (void)getGroupInfoByGroupIdArray:(NSArray<NSNumber*> *)*groupIdArray* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *aGroups , BMXError *aError ))*aCompletionBlock*`

#### Discussion
Get the list of group information for the incoming group id, pull from server if forceRefreshed is set

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getGroupListForceRefresh:completion:" title="getGroupListForceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getGroupInfoByGroupIdArray:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getGroupListForceRefresh:completion:

Get group list

`- (void)getGroupListForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   Pull from server if forceRefresh is set  

*aCompletionBlock*  
   GroupList, Error  

#### Discussion
Get group list

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getInvitationListByCursor:pageSize:completion:" title="getInvitationListByCursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getGroupListForceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getInvitationListByCursor:pageSize:completion:

Get group invitation list in pages

`- (void)getInvitationListByCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *invitationList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupInvitation *> *invitationList,  

#### Discussion
Get group invitation list in pages

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getLatestAnnouncementWithGroup:forceRefresh:completion:" title="getLatestAnnouncementWithGroup:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getInvitationListByCursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getLatestAnnouncementWithGroup:forceRefresh:completion:

Get the latest group announcement

`- (void)getLatestAnnouncementWithGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnounment *groupAnnounment , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get the latest group announcement

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMemberList:cursor:pageSize:completion:" title="getMemberList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getLatestAnnouncementWithGroup:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMemberList:cursor:pageSize:completion:

Get group member list in pages

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
Get group member list in pages

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMembers:forceRefresh:completion:" title="getMembers:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getMemberList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:forceRefresh:completion:

Get group member list,

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupMember*> *groupList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*forceRefresh*  
   Pull from server if forceRefresh is set, max. 1,000 members  

*aCompletionBlock*  
   List:BMXGroupMember ,BMXError  

#### Discussion
Get group member list,

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getMembersNickName:memberIdlist:completion:" title="getMembersNickName:memberIdlist:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getMembers:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMembersNickName:memberIdlist:completion:

Get group member nicknames in batch

`- (void)getMembersNickName:(BMXGroup *)*group* memberIdlist:(NSArray<NSNumber*> *)*memberIdlist* completion:(void ( ^ ) ( NSArray *aGroupMembers , BMXError *aError ))*aCompletionBlock*`

#### Discussion
Get group member nicknames in batch

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getSharedFilesListByGroup:forceRefresh:completion:" title="getSharedFilesListByGroup:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getMembersNickName:memberIdlist:completion:" %}{% endlanying_code_snippet %}
```
### getSharedFilesListByGroup:forceRefresh:completion:

Get a list of share files in group

`- (void)getSharedFilesListByGroup:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXGroupSharedFile*> *sharedFileList , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get a list of share files in group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/getbannedMemberListGroup:cursor:pageSize:completion:" title="getbannedMemberListGroup:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getSharedFilesListByGroup:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getbannedMemberListGroup:cursor:pageSize:completion:

Paged to get ban list

`- (void)getbannedMemberListGroup:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *memberList , NSString *cursor , long long offset , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  
   string  

*pageSize*  
   int  

*aCompletionBlock*  
   NSArray<BMXGroupMember *> *memberList  

#### Discussion
Paged to get ban list

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/joinGroup:message:completion:" title="joinGroup:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="getbannedMemberListGroup:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### joinGroup:message:completion:

Join a group, which may require admin approval depending on group settings

`- (void)joinGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*message*  
   Membership application information  

*aCompletionBlock*  
   Error  

#### Discussion
Join a group, which may require admin approval depending on group settings

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/leaveGroup:completion:" title="leaveGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="joinGroup:message:completion:" %}{% endlanying_code_snippet %}
```
### leaveGroup:completion:

Quit group

`- (void)leaveGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   Error  

#### Discussion
Quit group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/loadGroupInfo:completion:" title="loadGroupInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="leaveGroup:completion:" %}{% endlanying_code_snippet %}
```
### loadGroupInfo:completion:

Get group details, pull the latest information from server

`- (void)loadGroupInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*aCompletionBlock*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>,BMXError  

#### Discussion
Get group details, pull the latest information from server

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/muteMessageByGroup:msgMuteMode:completion:" title="muteMessageByGroup:msgMuteMode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="loadGroupInfo:completion:" %}{% endlanying_code_snippet %}
```
### muteMessageByGroup:msgMuteMode:completion:

Block group message

`- (void)muteMessageByGroup:(BMXGroup *)*group* msgMuteMode:(BMXGroupMsgMuteMode)*msgMuteMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Block group message

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeAdmins:admins:reason:completion:" title="removeAdmins:admins:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="muteMessageByGroup:msgMuteMode:completion:" %}{% endlanying_code_snippet %}
```
### removeAdmins:admins:reason:completion:

Remove admin

`- (void)removeAdmins:(BMXGroup *)*group* admins:(NSArray<NSNumber*> *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   <a href="../Classes/BMXGroup.md">BMXGroup</a>  

*admins*  
   Array:id  

*reason*  
   String  

*aCompletionBlock*  
   BMXError  

#### Discussion
Remove admin

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="removeAdmins:admins:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

<a name="//api/name/removeGroupListener:" title="removeGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeGroupListener:

Remove group change listener

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Discussion
Remove group change listener

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeMembersWithGroup:memberlist:reason:completion:" title="removeMembersWithGroup:memberlist:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="removeGroupListener:" %}{% endlanying_code_snippet %}
```
### removeMembersWithGroup:memberlist:reason:completion:

Remove group member

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
Remove group member

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/removeSharedFileFromGroup:file:completion:" title="removeSharedFileFromGroup:file:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="removeMembersWithGroup:memberlist:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeSharedFileFromGroup:file:completion:

Remove shared file in group

`- (void)removeSharedFileFromGroup:(BMXGroup *)*group* file:(BMXGroupSharedFile *)*file* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Remove shared file in group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setAllowMemberModifyWithGroup:enable:completion:" title="setAllowMemberModifyWithGroup:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="removeSharedFileFromGroup:file:completion:" %}{% endlanying_code_snippet %}
```
### setAllowMemberModifyWithGroup:enable:completion:

Set whether group members are allowed to set group information

`- (void)setAllowMemberModifyWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   Group to operate on  

*enable*  
   Whether allowed to operate  

*aCompletionBlock*  
   BMXError  

#### Discussion
Set whether group members are allowed to set group information

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setAvatarWithGroup:avatarData:progress:completion:" title="setAvatarWithGroup:avatarData:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setAllowMemberModifyWithGroup:enable:completion:" %}{% endlanying_code_snippet %}
```
### setAvatarWithGroup:avatarData:progress:completion:

Set group avatar

`- (void)setAvatarWithGroup:(BMXGroup *)*group* avatarData:(NSData *)*avatarData* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
Set group avatar

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setEnableReadAckWithGroup:enable:completion:" title="setEnableReadAckWithGroup:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setAvatarWithGroup:avatarData:progress:completion:" %}{% endlanying_code_snippet %}
```
### setEnableReadAckWithGroup:enable:completion:

Set whether group message read acknowledgement is enabled

`- (void)setEnableReadAckWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   Group to operate on  

*enable*  
   Enable or not  

*aCompletionBlock*  
   BMXError  

#### Discussion
Set whether group message read acknowledgement is enabled

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupDescription:description:completion:" title="setGroupDescription:description:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setEnableReadAckWithGroup:enable:completion:" %}{% endlanying_code_snippet %}
```
### setGroupDescription:description:completion:

Set group description

`- (void)setGroupDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set group description

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupExtensionWithGroup:extension:completion:" title="setGroupExtensionWithGroup:extension:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setGroupDescription:description:completion:" %}{% endlanying_code_snippet %}
```
### setGroupExtensionWithGroup:extension:completion:

Set group extension information

`- (void)setGroupExtensionWithGroup:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set group extension information

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setGroupName:name:completion:" title="setGroupName:name:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setGroupExtensionWithGroup:extension:completion:" %}{% endlanying_code_snippet %}
```
### setGroupName:name:completion:

Set group name

`- (void)setGroupName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXGroup *group , BMXError *error ))*aCompletionBlock*`

#### Discussion
Set group name

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setHistoryVisibleWithGroup:enable:completion:" title="setHistoryVisibleWithGroup:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setGroupName:name:completion:" %}{% endlanying_code_snippet %}
```
### setHistoryVisibleWithGroup:enable:completion:

Set whether group members are allowed to enable visible message history

`- (void)setHistoryVisibleWithGroup:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*group*  
   Group to operate on  

*enable*  
   Enable or not  

*aCompletionBlock*  
   BMXError  

#### Discussion
Set whether group members are allowed to enable visible message history

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setInviteModeWithGroup:mode:completion:" title="setInviteModeWithGroup:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setHistoryVisibleWithGroup:enable:completion:" %}{% endlanying_code_snippet %}
```
### setInviteModeWithGroup:mode:completion:

Set invitation mode

`- (void)setInviteModeWithGroup:(BMXGroup *)*group* mode:(BMXGroupInviteMode)*inviteMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set invitation mode

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setJoinAuthModeWithGroup:joinAuthMode:completion:" title="setJoinAuthModeWithGroup:joinAuthMode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setInviteModeWithGroup:mode:completion:" %}{% endlanying_code_snippet %}
```
### setJoinAuthModeWithGroup:joinAuthMode:completion:

Set approval mode for joining group

`- (void)setJoinAuthModeWithGroup:(BMXGroup *)*group* joinAuthMode:(BMXGroupJoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set approval mode for joining group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setMsgPushModeWithGroup:mode:completion:" title="setMsgPushModeWithGroup:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setJoinAuthModeWithGroup:joinAuthMode:completion:" %}{% endlanying_code_snippet %}
```
### setMsgPushModeWithGroup:mode:completion:

Set group message notification mode

`- (void)setMsgPushModeWithGroup:(BMXGroup *)*group* mode:(BMXGroupMsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set group message notification mode

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/setMyNicknameWithGroup:nickName:completion:" title="setMyNicknameWithGroup:nickName:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setMsgPushModeWithGroup:mode:completion:" %}{% endlanying_code_snippet %}
```
### setMyNicknameWithGroup:nickName:completion:

Set nickname in group

`- (void)setMyNicknameWithGroup:(BMXGroup *)*group* nickName:(NSString *)*nickName* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set nickname in group

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/transferOwnerByGroup:newOwnerId:completion:" title="transferOwnerByGroup:newOwnerId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="setMyNicknameWithGroup:nickName:completion:" %}{% endlanying_code_snippet %}
```
### transferOwnerByGroup:newOwnerId:completion:

Transfer of group Owner

`- (void)transferOwnerByGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Transfer of group Owner

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unbanGroup:completion:" title="unbanGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="transferOwnerByGroup:newOwnerId:completion:" %}{% endlanying_code_snippet %}
```
### unbanGroup:completion:

Unban all members

`- (void)unbanGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Unban all members

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unbanMembersByGroup:members:reason:completion:" title="unbanMembersByGroup:members:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="unbanGroup:completion:" %}{% endlanying_code_snippet %}
```
### unbanMembersByGroup:members:reason:completion:

Unban

`- (void)unbanMembersByGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Unban

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/unblockMember:members:completion:" title="unblockMember:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="unbanMembersByGroup:members:reason:completion:" %}{% endlanying_code_snippet %}
```
### unblockMember:members:completion:

Unblacklist

`- (void)unblockMember:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Unblacklist

#### Declared In
* `BMXGroupManager.h`

<a name="//api/name/uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:" title="uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="unblockMember:members:completion:" %}{% endlanying_code_snippet %}
```
### uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:

Add shared file in group

`- (void)uploadSharedFileToGroup:(BMXGroup *)*group* filePathStr:(NSString *)*filePathStr* displayName:(NSString *)*displayName* extionName:(NSString *)*extionName* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXGroup *resultGroup , BMXError *error ))*aCompletion*`

#### Discussion
Add shared file in group

#### Declared In
* `BMXGroupManager.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupManager",function="uploadSharedFileToGroup:filePathStr:displayName:extionName:progress:completion:" %}{% endlanying_code_snippet %}
```
