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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsAddedGroup:members:" %}{% endlanying_code_snippet %}
```
### groupAdminsRemovedFromGroup:members:reason:

Admins removed

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsRemovedFromGroup:members:reason:" %}{% endlanying_code_snippet %}
```
### groupAnnouncementUpdate:announcement:

Group announcement updated

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAnnouncementUpdate:announcement:" %}{% endlanying_code_snippet %}
```
### groupApplicationAccepted:approver:

Group application accepted

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationAccepted:approver:" %}{% endlanying_code_snippet %}
```
### groupApplicationDeclined:approver:reason:

Group application declined

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationDeclined:approver:reason:" %}{% endlanying_code_snippet %}
```
### groupDidCreated:

Group created(from othe devices)

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidCreated:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveApplied:applicantId:message:

Receive a group application

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveApplied:applicantId:message:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveInviter:groupId:message:

Receive a group invitation

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveInviter:groupId:message:" %}{% endlanying_code_snippet %}
```
### groupInfoDidUpdate:updateInfoType:

Group information updated

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroup_UpdateInfoType)*type*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInfoDidUpdate:updateInfoType:" %}{% endlanying_code_snippet %}
```
### groupInvitationAccepted:inviteeId:

Group invitation accepted

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationAccepted:inviteeId:" %}{% endlanying_code_snippet %}
```
### groupInvitationDeclined:inviteeId:reason:

Group invitation declined

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationDeclined:inviteeId:reason:" %}{% endlanying_code_snippet %}
```
### groupLeft:reason:

Left a group

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupLeft:reason:" %}{% endlanying_code_snippet %}
```
### groupMemberDidChangeNickName:memberId:nickName:

Group member's nickname changed

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberDidChangeNickName:memberId:nickName:" %}{% endlanying_code_snippet %}
```
### groupMemberJoined:memberId:inviter:

A new member joined

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberJoined:memberId:inviter:" %}{% endlanying_code_snippet %}
```
### groupMemberLeft:memberId:reason:

A group member left

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberLeft:memberId:reason:" %}{% endlanying_code_snippet %}
```
### groupMembersMutedGroup:members:duration:

Group members muted

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersMutedGroup:members:duration:" %}{% endlanying_code_snippet %}
```
### groupMembersUnMutedGroup:Unmuted:

Group members unmuted

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersUnMutedGroup:Unmuted:" %}{% endlanying_code_snippet %}
```
### groupOwnerAssigned:

Group owner changed

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupOwnerAssigned:" %}{% endlanying_code_snippet %}
```
### groupShareFileDidUpdated:sharedFile:

Group shared file name updated

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupShareFileDidUpdated:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileDeleted:sharedFile:

A group shared file deleted

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileDeleted:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileUploaded:sharedFile:

A group shared file uploaded

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileUploaded:sharedFile:" %}{% endlanying_code_snippet %}
```
