# BMXGroup Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXGroup.h  

## Overview

群

## Properties

<a name="//api/name/adminsCount" title="adminsCount"></a>
### adminsCount

群管理员数量

`@property (nonatomic, assign, readonly) NSInteger adminsCount`

#### Discussion
群管理员数量

#### Declared In
* `BMXGroup.h`

<a name="//api/name/annountment" title="annountment"></a>
### annountment

`@property (nonatomic, strong) BMXGroupAnnounment *annountment`

<a name="//api/name/avatarPath" title="avatarPath"></a>
### avatarPath

群头像下载后的本地路径

`@property (nonatomic, copy, readonly) NSString *avatarPath`

#### Discussion
群头像下载后的本地路径

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarThumbnailPath" title="avatarThumbnailPath"></a>
### avatarThumbnailPath

群头像缩略图下载后的本地路径

`@property (nonatomic, copy, readonly) NSString *avatarThumbnailPath`

#### Discussion
群头像缩略图下载后的本地路径

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarThumbnailUrl" title="avatarThumbnailUrl"></a>
### avatarThumbnailUrl

群头像缩略图

`@property (nonatomic, copy, readonly) NSString *avatarThumbnailUrl`

#### Discussion
群头像缩略图

#### Declared In
* `BMXGroup.h`

<a name="//api/name/avatarUrl" title="avatarUrl"></a>
### avatarUrl

群头像

`@property (nonatomic, copy, readonly) NSString *avatarUrl`

#### Discussion
群头像

#### Declared In
* `BMXGroup.h`

<a name="//api/name/banExpireTime" title="banExpireTime"></a>
### banExpireTime

全群禁言到期时间

`@property (nonatomic, assign, readonly) long long banExpireTime`

#### Discussion
全群禁言到期时间

#### Declared In
* `BMXGroup.h`

<a name="//api/name/capactiy" title="capactiy"></a>
### capactiy

最大人数

`@property (nonatomic, assign, readonly) NSInteger capactiy`

#### Discussion
最大人数

#### Declared In
* `BMXGroup.h`

<a name="//api/name/creatTime" title="creatTime"></a>
### creatTime

群创建时间

`@property (nonatomic, readonly) long long creatTime`

#### Discussion
群创建时间

#### Declared In
* `BMXGroup.h`

<a name="//api/name/enableReadAck" title="enableReadAck"></a>
### enableReadAck

是否开启群消息已读功能

`@property (nonatomic, assign) BOOL enableReadAck`

#### Discussion
是否开启群消息已读功能

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupDescription" title="groupDescription"></a>
### groupDescription

群描述

`@property (nonatomic, copy, readonly) NSString *groupDescription`

#### Discussion
群描述

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupId" title="groupId"></a>
### groupId

群Id

`@property (nonatomic, assign, readonly) long long groupId`

#### Discussion
群Id

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupStatus" title="groupStatus"></a>
### groupStatus

当前群组的状态。（Normal 正常， Destroyed 以销毁）

`@property (nonatomic, assign) BMXGroupStatus groupStatus`

#### Discussion
当前群组的状态。（Normal 正常， Destroyed 以销毁）

#### Declared In
* `BMXGroup.h`

<a name="//api/name/groupType" title="groupType"></a>
### groupType

`@property (nonatomic, assign, readonly) BMXGroupType groupType`

<a name="//api/name/historyVisible" title="historyVisible"></a>
### historyVisible

是否可以加载显示历史聊天记录

`@property (nonatomic, assign) BOOL historyVisible`

#### Discussion
是否可以加载显示历史聊天记录

#### Declared In
* `BMXGroup.h`

<a name="//api/name/inviteMode" title="inviteMode"></a>
### inviteMode

入群邀请模式

`@property (nonatomic, assign, readonly) BMXGroupInviteMode inviteMode`

#### Discussion
入群邀请模式

#### Declared In
* `BMXGroup.h`

<a name="//api/name/isMember" title="isMember"></a>
### isMember

`@property (nonatomic, assign, readonly) BOOL isMember`

<a name="//api/name/joinAuthMode" title="joinAuthMode"></a>
### joinAuthMode

入群审批模式

`@property (nonatomic, assign, readonly) BMXGroupJoinAuthMode joinAuthMode`

#### Discussion
入群审批模式

#### Declared In
* `BMXGroup.h`

<a name="//api/name/jsonextension" title="jsonextension"></a>
### jsonextension

群扩展信息

`@property (nonatomic, copy, readonly) NSString *jsonextension`

#### Discussion
群扩展信息

#### Declared In
* `BMXGroup.h`

<a name="//api/name/membersCount" title="membersCount"></a>
### membersCount

群成员数量，包含Owner，admins 和members

`@property (nonatomic, assign, readonly) NSInteger membersCount`

#### Discussion
群成员数量，包含Owner，admins 和members

#### Declared In
* `BMXGroup.h`

<a name="//api/name/modifyMode" title="modifyMode"></a>
### modifyMode

群信息修改模式

`@property (nonatomic, assign, readonly) BMXGroupModifyMode modifyMode`

#### Discussion
群信息修改模式

#### Declared In
* `BMXGroup.h`

<a name="//api/name/msgMuteMode" title="msgMuteMode"></a>
### msgMuteMode

群消息屏蔽模式

`@property (nonatomic, assign) BMXGroupMsgMuteMode msgMuteMode`

#### Discussion
群消息屏蔽模式

#### Declared In
* `BMXGroup.h`

<a name="//api/name/msgPushMode" title="msgPushMode"></a>
### msgPushMode

群消息通知类型

`@property (nonatomic, assign, readonly) BMXGroupMsgPushMode msgPushMode`

#### Discussion
群消息通知类型

#### Declared In
* `BMXGroup.h`

<a name="//api/name/myNickName" title="myNickName"></a>
### myNickName

在群里的昵称

`@property (nonatomic, copy, readonly) NSString *myNickName`

#### Discussion
在群里的昵称

#### Declared In
* `BMXGroup.h`

<a name="//api/name/name" title="name"></a>
### name

群名称

`@property (nonatomic, copy, readonly) NSString *name`

#### Discussion
群名称

#### Declared In
* `BMXGroup.h`

<a name="//api/name/ownerId" title="ownerId"></a>
### ownerId

群成员

`@property (nonatomic, assign, readonly) NSInteger ownerId`

#### Discussion
群成员

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

群共享文件数量

`@property (nonatomic, assign, readonly) NSInteger sharedFilesCount`

#### Discussion
群共享文件数量

#### Declared In
* `BMXGroup.h`

