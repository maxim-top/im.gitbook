# BMXGroupServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXGroupServiceProtocol.h  

## Instance Methods

<a name="//api/name/groupAdminsAddedGroup:members:" title="groupAdminsAddedGroup:members:"></a>
### groupAdminsAddedGroup:members:

New Admin added

`- (void)groupAdminsAddedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members*`

#### Discussion
New Admin added

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAdminsRemovedFromGroup:members:reason:" title="groupAdminsRemovedFromGroup:members:reason:"></a>
### groupAdminsRemovedFromGroup:members:reason:

Admin removed

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion
Admin removed

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
### groupAnnouncementUpdate:announcement:

Group announcement updated

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnounment *)*announcement*`

#### Discussion
Group announcement updated

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
### groupApplicationAccepted:approver:

Join group accepted

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion
Join group accepted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
### groupApplicationDeclined:approver:reason:

Join group rejected

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion
Join group rejected

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
### groupDidCreated:

Create a group

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion
Create a group

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
### groupDidRecieveApplied:applicantId:message:

Group membership application received

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion
Group membership application received

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
### groupDidRecieveInviter:groupId:message:

Group invitation received

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion
Group invitation received

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
### groupInfoDidUpdate:updateInfoType:

Group information changes

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroupUpdateInfoType)*type*`

#### Discussion
Group information changes

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
### groupInvitationAccepted:inviteeId:

Group invitation accepted

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion
Group invitation accepted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
### groupInvitationDeclined:inviteeId:reason:

Join group rejected

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion
Join group rejected

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
### groupLeft:reason:

Quit a group

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion
Quit a group

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
### groupMemberDidChangeNickName:memberId:nickName:

Member nickname changed

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion
Member nickname changed

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
### groupMemberJoined:memberId:inviter:

New member added

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion
New member added

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
### groupMemberLeft:memberId:reason:

Member quit

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion
Member quit

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
### groupMembersMutedGroup:members:duration:

Member banned

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion
Member banned

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
### groupMembersUnMutedGroup:Unmuted:

Member unbanned

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion
Member unbanned

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
### groupOwnerAssigned:

Become group Owner

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion
Become group Owner

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
### groupShareFileDidUpdated:sharedFile:

Name of shared file updated

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Name of shared file updated

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
### groupSharedFileDeleted:sharedFile:

Shared file deleted

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Shared file deleted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
### groupSharedFileUploaded:sharedFile:

Shared file received

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Shared file received

#### Declared In
* `BMXGroupServiceProtocol.h`

