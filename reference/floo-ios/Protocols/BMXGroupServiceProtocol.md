# BMXGroupServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXGroupServiceProtocol.h  

## Instance Methods

<a name="//api/name/groupAdminsAddedGroup:members:" title="groupAdminsAddedGroup:members:"></a>
### groupAdminsAddedGroup:members:

添加了新管理员

`- (void)groupAdminsAddedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members*`

#### Discussion
添加了新管理员

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAdminsRemovedFromGroup:members:reason:" title="groupAdminsRemovedFromGroup:members:reason:"></a>
### groupAdminsRemovedFromGroup:members:reason:

移除了管理员

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion
移除了管理员

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
### groupAnnouncementUpdate:announcement:

收到群公告

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnounment *)*announcement*`

#### Discussion
收到群公告

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
### groupApplicationAccepted:approver:

入群申请被接受

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion
入群申请被接受

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
### groupApplicationDeclined:approver:reason:

入群申请被拒绝

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion
入群申请被拒绝

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
### groupDidCreated:

多设备同步创建群组

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion
多设备同步创建群组

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
### groupDidRecieveApplied:applicantId:message:

收到入群申请

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion
收到入群申请

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
### groupDidRecieveInviter:groupId:message:

收到入群邀请

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion
收到入群邀请

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
### groupInfoDidUpdate:updateInfoType:

群组信息变更

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroupUpdateInfoType)*type*`

#### Discussion
群组信息变更

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
### groupInvitationAccepted:inviteeId:

入群邀请被接受

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion
入群邀请被接受

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
### groupInvitationDeclined:inviteeId:reason:

入群申请被拒绝

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion
入群申请被拒绝

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
### groupLeft:reason:

退出了某群

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion
退出了某群

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
### groupMemberDidChangeNickName:memberId:nickName:

群成员更改群内昵称

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion
群成员更改群内昵称

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
### groupMemberJoined:memberId:inviter:

加入新成员

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion
加入新成员

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
### groupMemberLeft:memberId:reason:

群成员退出

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion
群成员退出

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
### groupMembersMutedGroup:members:duration:

群成员被禁言

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion
群成员被禁言

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
### groupMembersUnMutedGroup:Unmuted:

群成员被解除禁言

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion
群成员被解除禁言

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
### groupOwnerAssigned:

成为群主

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion
成为群主

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
### groupShareFileDidUpdated:sharedFile:

共享文件更新文件名

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
共享文件更新文件名

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
### groupSharedFileDeleted:sharedFile:

删除了共享文件

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
删除了共享文件

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
### groupSharedFileUploaded:sharedFile:

收到共享文件

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
收到共享文件

#### Declared In
* `BMXGroupServiceProtocol.h`

