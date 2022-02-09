# BMXGroup Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXGroup.h  

## Overview

Chatroom

## Properties

<a name="//api/name/adminsCount" title="adminsCount"></a>
### adminsCount

Group admin-number

`@property (nonatomic, assign, readonly) NSInteger adminsCount`

#### Discussion
Group admin-number

#### Declared In
* `BMXGroup.h`

<a name="//api/name/annountment" title="annountment"></a>
### annountment

`@property (nonatomic, strong) BMXGroupAnnounment *annountment`

<a name="//api/name/avatarPath" title="avatarPath"></a>
### avatarPath

Local path of downloaded group avatar

`@property (nonatomic, copy, readonly) NSString *avatarPath`

#### Discussion
Local path of downloaded group avatar

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarThumbnailPath" title="avatarThumbnailPath"></a>
### avatarThumbnailPath

Local path of downloaded group avatar thumbnail

`@property (nonatomic, copy, readonly) NSString *avatarThumbnailPath`

#### Discussion
Local path of downloaded group avatar thumbnail

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarThumbnailUrl" title="avatarThumbnailUrl"></a>
### avatarThumbnailUrl

Group avatar thumbnail

`@property (nonatomic, copy, readonly) NSString *avatarThumbnailUrl`

#### Discussion
Group avatar thumbnail

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
### avatarUrl

Group avatar

`@property (nonatomic, copy, readonly) NSString *avatarUrl`

#### Discussion
Group avatar

#### Declared In
* `BMXGroup.h`

<a name="//api/name/banExpireTime" title="banExpireTime"></a>
### banExpireTime

Expiration time of banning all members

`@property (nonatomic, assign, readonly) long long banExpireTime`

#### Discussion
Expiration time of banning all members

#### Declared In
* `BMXGroup.h`

<a name="//api/name/capactiy" title="capactiy"></a>
### capactiy

Max member-number

`@property (nonatomic, assign, readonly) NSInteger capactiy`

#### Discussion
Max member-number

#### Declared In
* `BMXGroup.h`

<a name="//api/name/creatTime" title="creatTime"></a>
### creatTime

Group creation time

`@property (nonatomic, readonly) long long creatTime`

#### Discussion
Group creation time

#### Declared In
* `BMXGroup.h`

<a name="//api/name/enableReadAck" title="enableReadAck"></a>
### enableReadAck

Whether group message read feature enabled

`@property (nonatomic, assign) BOOL enableReadAck`

#### Discussion
Whether group message read feature enabled

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupDescription" title="groupDescription"></a>
### groupDescription

Group description

`@property (nonatomic, copy, readonly) NSString *groupDescription`

#### Discussion
Group description

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupId" title="groupId"></a>
### groupId

Group Id

`@property (nonatomic, assign, readonly) long long groupId`

#### Discussion
Group Id

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupStatus" title="groupStatus"></a>
### groupStatus

state of the current group. (Normal, Destroyed)

`@property (nonatomic, assign) BMXGroupStatus groupStatus`

#### Discussion
state of the current group. (Normal, Destroyed)

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupType" title="groupType"></a>
### groupType

`@property (nonatomic, assign, readonly) BMXGroupType groupType`

<a name="//api/name/historyVisible" title="historyVisible"></a>
### historyVisible

Whether to load and display the chat history

`@property (nonatomic, assign) BOOL historyVisible`

#### Discussion
Whether to load and display the chat history

#### Declared In
* `BMXGroup.h`

<a name="//api/name/inviteMode" title="inviteMode"></a>
### inviteMode

Group invitation mode

`@property (nonatomic, assign, readonly) BMXGroupInviteMode inviteMode`

#### Discussion
Group invitation mode

#### Declared In
* `BMXGroup.h`

<a name="//api/name/isMember" title="isMember"></a>
### isMember

`@property (nonatomic, assign, readonly) BOOL isMember`

<a name="//api/name/joinAuthMode" title="joinAuthMode"></a>
### joinAuthMode

Join approval mode

`@property (nonatomic, assign, readonly) BMXGroupJoinAuthMode joinAuthMode`

#### Discussion
Join approval mode

#### Declared In
* `BMXGroup.h`

<a name="//api/name/jsonextension" title="jsonextension"></a>
### jsonextension

Group extension information

`@property (nonatomic, copy, readonly) NSString *jsonextension`

#### Discussion
Group extension information

#### Declared In
* `BMXGroup.h`

<a name="//api/name/membersCount" title="membersCount"></a>
### membersCount

Group member-number, including Owner, Admins and Members

`@property (nonatomic, assign, readonly) NSInteger membersCount`

#### Discussion
Group member-number, including Owner, Admins and Members

#### Declared In
* `BMXGroup.h`

<a name="//api/name/modifyMode" title="modifyMode"></a>
### modifyMode

Group information modification mode

`@property (nonatomic, assign, readonly) BMXGroupModifyMode modifyMode`

#### Discussion
Group information modification mode

#### Declared In
* `BMXGroup.h`

<a name="//api/name/msgMuteMode" title="msgMuteMode"></a>
### msgMuteMode

Group message blocking mode

`@property (nonatomic, assign) BMXGroupMsgMuteMode msgMuteMode`

#### Discussion
Group message blocking mode

#### Declared In
* `BMXGroup.h`

<a name="//api/name/msgPushMode" title="msgPushMode"></a>
### msgPushMode

Group message notification type

`@property (nonatomic, assign, readonly) BMXGroupMsgPushMode msgPushMode`

#### Discussion
Group message notification type

#### Declared In
* `BMXGroup.h`

<a name="//api/name/myNickName" title="myNickName"></a>
### myNickName

Group member nickname

`@property (nonatomic, copy, readonly) NSString *myNickName`

#### Discussion
Group member nickname

#### Declared In
* `BMXGroup.h`

<a name="//api/name/name" title="name"></a>
### name

Group name

`@property (nonatomic, copy, readonly) NSString *name`

#### Discussion
Group name

#### Declared In
* `BMXGroup.h`

<a name="//api/name/ownerId" title="ownerId"></a>
### ownerId

Group members

`@property (nonatomic, assign, readonly) NSInteger ownerId`

#### Discussion
Group members

#### Declared In
* `BMXGroup.h`

<a name="//api/name/roleType" title="roleType"></a>
### roleType

`@property (nonatomic, assign) BMXGroupMemberRoleType roleType`

<a name="//api/name/shareFile" title="shareFile"></a>
### shareFile

`@property (nonatomic, strong, readonly) BMXGroupSharedFile *shareFile`

<a name="//api/name/sharedFilesCount" title="sharedFilesCount"></a>
### sharedFilesCount

Shared file-number in group

`@property (nonatomic, assign, readonly) NSInteger sharedFilesCount`

#### Discussion
Shared file-number in group

#### Declared In
* `BMXGroup.h`

