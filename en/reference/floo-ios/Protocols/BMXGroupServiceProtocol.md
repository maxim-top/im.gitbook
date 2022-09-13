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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsAddedGroup:members:" %}{% endlanying_code_snippet %}
```
### groupAdminsRemovedFromGroup:members:reason:

Admin removed

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion
Admin removed

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsRemovedFromGroup:members:reason:" %}{% endlanying_code_snippet %}
```
### groupAnnouncementUpdate:announcement:

Group announcement updated

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnounment *)*announcement*`

#### Discussion
Group announcement updated

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAnnouncementUpdate:announcement:" %}{% endlanying_code_snippet %}
```
### groupApplicationAccepted:approver:

Join group accepted

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion
Join group accepted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationAccepted:approver:" %}{% endlanying_code_snippet %}
```
### groupApplicationDeclined:approver:reason:

Join group rejected

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion
Join group rejected

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationDeclined:approver:reason:" %}{% endlanying_code_snippet %}
```
### groupDidCreated:

Create a group

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion
Create a group

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidCreated:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveApplied:applicantId:message:

Group membership application received

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion
Group membership application received

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveApplied:applicantId:message:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveInviter:groupId:message:

Group invitation received

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion
Group invitation received

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveInviter:groupId:message:" %}{% endlanying_code_snippet %}
```
### groupInfoDidUpdate:updateInfoType:

Group information changes

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroupUpdateInfoType)*type*`

#### Discussion
Group information changes

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInfoDidUpdate:updateInfoType:" %}{% endlanying_code_snippet %}
```
### groupInvitationAccepted:inviteeId:

Group invitation accepted

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion
Group invitation accepted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationAccepted:inviteeId:" %}{% endlanying_code_snippet %}
```
### groupInvitationDeclined:inviteeId:reason:

Join group rejected

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion
Join group rejected

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationDeclined:inviteeId:reason:" %}{% endlanying_code_snippet %}
```
### groupLeft:reason:

Quit a group

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion
Quit a group

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupLeft:reason:" %}{% endlanying_code_snippet %}
```
### groupMemberDidChangeNickName:memberId:nickName:

Member nickname changed

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion
Member nickname changed

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberDidChangeNickName:memberId:nickName:" %}{% endlanying_code_snippet %}
```
### groupMemberJoined:memberId:inviter:

New member added

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion
New member added

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberJoined:memberId:inviter:" %}{% endlanying_code_snippet %}
```
### groupMemberLeft:memberId:reason:

Member quit

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion
Member quit

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberLeft:memberId:reason:" %}{% endlanying_code_snippet %}
```
### groupMembersMutedGroup:members:duration:

Member banned

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion
Member banned

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersMutedGroup:members:duration:" %}{% endlanying_code_snippet %}
```
### groupMembersUnMutedGroup:Unmuted:

Member unbanned

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion
Member unbanned

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersUnMutedGroup:Unmuted:" %}{% endlanying_code_snippet %}
```
### groupOwnerAssigned:

Become group Owner

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion
Become group Owner

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupOwnerAssigned:" %}{% endlanying_code_snippet %}
```
### groupShareFileDidUpdated:sharedFile:

Name of shared file updated

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Name of shared file updated

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupShareFileDidUpdated:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileDeleted:sharedFile:

Shared file deleted

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Shared file deleted

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileDeleted:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileUploaded:sharedFile:

Shared file received

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
Shared file received

#### Declared In
* `BMXGroupServiceProtocol.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileUploaded:sharedFile:" %}{% endlanying_code_snippet %}
```
