# BMXGroupServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol Group service listener

## Instance Methods

<a name="//api/name/groupAdminsAddedGroup:members:" title="groupAdminsAddedGroup:members:"></a>
### groupAdminsAddedGroup:members:

New admins added

`- (void)groupAdminsAddedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAdminsRemovedFromGroup:members:reason:" title="groupAdminsRemovedFromGroup:members:reason:"></a>
### groupAdminsRemovedFromGroup:members:reason:

Admins removed

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
### groupAnnouncementUpdate:announcement:

Group announcement updated

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
### groupApplicationAccepted:approver:

Group application accepted

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
### groupApplicationDeclined:approver:reason:

Group application declined

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
### groupDidCreated:

Group created(from othe devices)

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
### groupDidRecieveApplied:applicantId:message:

Receive a group application

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
### groupDidRecieveInviter:groupId:message:

Receive a group invitation

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
### groupInfoDidUpdate:updateInfoType:

Group information updated

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroup_UpdateInfoType)*type*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
### groupInvitationAccepted:inviteeId:

Group invitation accepted

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
### groupInvitationDeclined:inviteeId:reason:

Group invitation declined

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
### groupLeft:reason:

Left a group

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
### groupMemberDidChangeNickName:memberId:nickName:

Group member's nickname changed

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
### groupMemberJoined:memberId:inviter:

A new member joined

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
### groupMemberLeft:memberId:reason:

A group member left

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
### groupMembersMutedGroup:members:duration:

Group members muted

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
### groupMembersUnMutedGroup:Unmuted:

Group members unmuted

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
### groupOwnerAssigned:

Group owner changed

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
### groupShareFileDidUpdated:sharedFile:

Group shared file name updated

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
### groupSharedFileDeleted:sharedFile:

A group shared file deleted

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
### groupSharedFileUploaded:sharedFile:

A group shared file uploaded

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

