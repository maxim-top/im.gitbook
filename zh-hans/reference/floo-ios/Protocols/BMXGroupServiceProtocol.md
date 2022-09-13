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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsAddedGroup:members:" %}{% endlanying_code_snippet %}
```
### groupAdminsRemovedFromGroup:members:reason:

移除了管理员

`- (void)groupAdminsRemovedFromGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* reason:(NSString *)*reason*`

#### Discussion
移除了管理员

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupAnnouncementUpdate:announcement:" title="groupAnnouncementUpdate:announcement:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAdminsRemovedFromGroup:members:reason:" %}{% endlanying_code_snippet %}
```
### groupAnnouncementUpdate:announcement:

收到群公告

`- (void)groupAnnouncementUpdate:(BMXGroup *)*group* announcement:(BMXGroupAnnounment *)*announcement*`

#### Discussion
收到群公告

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationAccepted:approver:" title="groupApplicationAccepted:approver:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupAnnouncementUpdate:announcement:" %}{% endlanying_code_snippet %}
```
### groupApplicationAccepted:approver:

入群申请被接受

`- (void)groupApplicationAccepted:(BMXGroup *)*group* approver:(NSInteger)*approver*`

#### Discussion
入群申请被接受

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupApplicationDeclined:approver:reason:" title="groupApplicationDeclined:approver:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationAccepted:approver:" %}{% endlanying_code_snippet %}
```
### groupApplicationDeclined:approver:reason:

入群申请被拒绝

`- (void)groupApplicationDeclined:(BMXGroup *)*group* approver:(NSInteger)*approver* reason:(NSString *)*reason*`

#### Discussion
入群申请被拒绝

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidCreated:" title="groupDidCreated:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupApplicationDeclined:approver:reason:" %}{% endlanying_code_snippet %}
```
### groupDidCreated:

多设备同步创建群组

`- (void)groupDidCreated:(BMXGroup *)*group*`

#### Discussion
多设备同步创建群组

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveApplied:applicantId:message:" title="groupDidRecieveApplied:applicantId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidCreated:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveApplied:applicantId:message:

收到入群申请

`- (void)groupDidRecieveApplied:(BMXGroup *)*group* applicantId:(NSInteger)*applicantId* message:(NSString *)*message*`

#### Discussion
收到入群申请

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupDidRecieveInviter:groupId:message:" title="groupDidRecieveInviter:groupId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveApplied:applicantId:message:" %}{% endlanying_code_snippet %}
```
### groupDidRecieveInviter:groupId:message:

收到入群邀请

`- (void)groupDidRecieveInviter:(NSInteger)*inviter* groupId:(NSInteger)*groupId* message:(NSString *)*message*`

#### Discussion
收到入群邀请

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInfoDidUpdate:updateInfoType:" title="groupInfoDidUpdate:updateInfoType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupDidRecieveInviter:groupId:message:" %}{% endlanying_code_snippet %}
```
### groupInfoDidUpdate:updateInfoType:

群组信息变更

`- (void)groupInfoDidUpdate:(BMXGroup *)*group* updateInfoType:(BMXGroupUpdateInfoType)*type*`

#### Discussion
群组信息变更

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationAccepted:inviteeId:" title="groupInvitationAccepted:inviteeId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInfoDidUpdate:updateInfoType:" %}{% endlanying_code_snippet %}
```
### groupInvitationAccepted:inviteeId:

入群邀请被接受

`- (void)groupInvitationAccepted:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId*`

#### Discussion
入群邀请被接受

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupInvitationDeclined:inviteeId:reason:" title="groupInvitationDeclined:inviteeId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationAccepted:inviteeId:" %}{% endlanying_code_snippet %}
```
### groupInvitationDeclined:inviteeId:reason:

入群申请被拒绝

`- (void)groupInvitationDeclined:(BMXGroup *)*group* inviteeId:(NSInteger)*inviteeId* reason:(NSString *)*reason*`

#### Discussion
入群申请被拒绝

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupLeft:reason:" title="groupLeft:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupInvitationDeclined:inviteeId:reason:" %}{% endlanying_code_snippet %}
```
### groupLeft:reason:

退出了某群

`- (void)groupLeft:(BMXGroup *)*group* reason:(NSString *)*reason*`

#### Discussion
退出了某群

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberDidChangeNickName:memberId:nickName:" title="groupMemberDidChangeNickName:memberId:nickName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupLeft:reason:" %}{% endlanying_code_snippet %}
```
### groupMemberDidChangeNickName:memberId:nickName:

群成员更改群内昵称

`- (void)groupMemberDidChangeNickName:(BMXGroup *)*group* memberId:(long long)*memberId* nickName:(NSString *)*nickName*`

#### Discussion
群成员更改群内昵称

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberJoined:memberId:inviter:" title="groupMemberJoined:memberId:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberDidChangeNickName:memberId:nickName:" %}{% endlanying_code_snippet %}
```
### groupMemberJoined:memberId:inviter:

加入新成员

`- (void)groupMemberJoined:(BMXGroup *)*group* memberId:(NSInteger)*memberId* inviter:(NSInteger)*inviter*`

#### Discussion
加入新成员

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMemberLeft:memberId:reason:" title="groupMemberLeft:memberId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberJoined:memberId:inviter:" %}{% endlanying_code_snippet %}
```
### groupMemberLeft:memberId:reason:

群成员退出

`- (void)groupMemberLeft:(BMXGroup *)*group* memberId:(NSInteger)*memberId* reason:(NSString *)*reason*`

#### Discussion
群成员退出

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersMutedGroup:members:duration:" title="groupMembersMutedGroup:members:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMemberLeft:memberId:reason:" %}{% endlanying_code_snippet %}
```
### groupMembersMutedGroup:members:duration:

群成员被禁言

`- (void)groupMembersMutedGroup:(BMXGroup *)*group* members:(NSArray<NSNumber*> *)*members* duration:(NSInteger)*duration*`

#### Discussion
群成员被禁言

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupMembersUnMutedGroup:Unmuted:" title="groupMembersUnMutedGroup:Unmuted:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersMutedGroup:members:duration:" %}{% endlanying_code_snippet %}
```
### groupMembersUnMutedGroup:Unmuted:

群成员被解除禁言

`- (void)groupMembersUnMutedGroup:(BMXGroup *)*group* Unmuted:(NSArray<NSNumber*> *)*members*`

#### Discussion
群成员被解除禁言

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupOwnerAssigned:" title="groupOwnerAssigned:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupMembersUnMutedGroup:Unmuted:" %}{% endlanying_code_snippet %}
```
### groupOwnerAssigned:

成为群主

`- (void)groupOwnerAssigned:(BMXGroup *)*group*`

#### Discussion
成为群主

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupShareFileDidUpdated:sharedFile:" title="groupShareFileDidUpdated:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupOwnerAssigned:" %}{% endlanying_code_snippet %}
```
### groupShareFileDidUpdated:sharedFile:

共享文件更新文件名

`- (void)groupShareFileDidUpdated:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
共享文件更新文件名

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileDeleted:sharedFile:" title="groupSharedFileDeleted:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupShareFileDidUpdated:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileDeleted:sharedFile:

删除了共享文件

`- (void)groupSharedFileDeleted:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
删除了共享文件

#### Declared In
* `BMXGroupServiceProtocol.h`

<a name="//api/name/groupSharedFileUploaded:sharedFile:" title="groupSharedFileUploaded:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileDeleted:sharedFile:" %}{% endlanying_code_snippet %}
```
### groupSharedFileUploaded:sharedFile:

收到共享文件

`- (void)groupSharedFileUploaded:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Discussion
收到共享文件

#### Declared In
* `BMXGroupServiceProtocol.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupServiceProtocol",function="groupSharedFileUploaded:sharedFile:" %}{% endlanying_code_snippet %}
```
