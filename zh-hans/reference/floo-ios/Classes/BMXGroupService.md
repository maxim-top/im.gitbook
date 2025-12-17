# BMXGroupService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 群组Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### acceptApplicationWithGroup:applicantId:

接受入群申请

`- (BMXErrorCode)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

#### Parameters

_group_\
进行操作的群组

_applicantId_\
申请进群的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptApplicationWithGroup:applicantId:completion:

接受入群申请

`- (void)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_applicantId_\
申请进群的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptInvitationWithGroup:inviter:

接受入群邀请

`- (BMXErrorCode)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

#### Parameters

_group_\
进行操作的群组

_inviter_\
邀请者id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptInvitationWithGroup:inviter:completion:

接受入群邀请

`- (void)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_inviter_\
邀请者id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addAdminsWithGroup:admins:message:

添加管理员

`- (BMXErrorCode)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message*`

#### Parameters

_group_\
进行操作的群组

_admins_\
要添加为管理员的成员id列表

_message_\
添加为管理员的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addAdminsWithGroup:admins:message:completion:

添加管理员

`- (void)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_admins_\
要添加为管理员的成员id列表

_message_\
添加为管理员的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addDelegate:

添加群组变化监听者

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
群组变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addGroupListener:

添加群组变化监听者

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

_listener_\
群组变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addMembersWithGroup:members:message:

添加群成员

`- (BMXErrorCode)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message*`

#### Parameters

_group_\
进行操作的群组

_members_\
要添加进群的成员id列表

_message_\
添加成员原因信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addMembersWithGroup:members:message:completion:

添加群成员

`- (void)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
要添加进群的成员id列表

_message_\
添加成员原因信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banGroupWithGroup:duration:

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）

`- (BMXErrorCode)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration*`

#### Parameters

_group_\
进行操作的群组

_duration_\
禁言时长(分钟)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banGroupWithGroup:duration:completion:

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）

`- (void)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_duration_\
禁言时长(分钟)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banMembersWithGroup:members:duration:

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banMembersWithGroup:members:duration:reason:

禁言

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason*`

#### Parameters

_group_\
进行操作的群组

_members_\
被禁言的群成员id列表

_duration_\
禁言时长

_reason_\
禁言原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banMembersWithGroup:members:duration:reason:completion:

禁言

`- (void)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
被禁言的群成员id列表

_duration_\
禁言时长

_reason_\
禁言原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### blockMembersWithGroup:members:

添加黑名单

`- (BMXErrorCode)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
进行操作的群组

_members_\
要加入黑名单的群成员id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### blockMembersWithGroup:members:completion:

添加黑名单

`- (void)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
要加入黑名单的群成员id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelDownloadSharedFileWithGroup:sharedFile:

取消下载群共享文件

`- (BMXErrorCode)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
下载的群共享文件

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelDownloadSharedFileWithGroup:sharedFile:completion:

取消下载群共享文件

`- (void)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
下载的群共享文件

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelUploadSharedFileWithGroup:filePath:

取消上传群共享文件

`- (BMXErrorCode)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath*`

#### Parameters

_group_\
进行操作的群组

_filePath_\
文件的本地路径

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelUploadSharedFileWithGroup:filePath:completion:

取消上传群共享文件

`- (void)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_filePath_\
文件的本地路径

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### changeSharedFileNameWithGroup:sharedFile:name:

修改群共享文件名称

`- (BMXErrorCode)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
进行更改的群共享文件

_name_\
修改的群共享文件名称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### changeSharedFileNameWithGroup:sharedFile:name:completion:

修改群共享文件名称

`- (void)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
进行更改的群共享文件

_name_\
修改的群共享文件名称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### createWithOptions:completion:

创建群

`- (void)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

_options_\
创建群组时传入的参数选项

_group_\
创建返回的结果，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### createWithOptions:group:

创建群

`- (BMXErrorCode)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* group:(BMXGroup *)*group*`

#### Parameters

_options_\
创建群组时传入的参数选项

_group_\
创建返回的结果，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineApplicationWithGroup:applicantId:

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineApplicationWithGroup:applicantId:reason:

拒绝入群申请

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason*`

#### Parameters

_group_\
进行操作的群组

_applicantId_\
申请进群的用户id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineApplicationWithGroup:applicantId:reason:completion:

拒绝入群申请

`- (void)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_applicantId_\
申请进群的用户id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineInvitationWithGroup:inviter:

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineInvitationWithGroup:inviter:reason:

拒绝入群邀请

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason*`

#### Parameters

_group_\
进行操作的群组

_inviter_\
邀请者id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineInvitationWithGroup:inviter:reason:completion:

拒绝入群邀请

`- (void)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_inviter_\
邀请者id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### deleteAnnouncementWithGroup:announcementId:

删除群公告

`- (BMXErrorCode)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId*`

#### Parameters

_group_\
进行操作的群组

_announcementId_\
删除的群公告id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### deleteAnnouncementWithGroup:announcementId:completion:

删除群公告

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_announcementId_\
删除的群公告id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### destroyWithGroup:

销毁群

`- (BMXErrorCode)destroyWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
要销毁的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### destroyWithGroup:completion:

销毁群

`- (void)destroyWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
要销毁的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadAvatarWithGroup:thumbnail:callback:

下载群头像

`- (BMXErrorCode)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_group_\
进行操作的群组

_thumbnail_\
设置为true下载缩略图，false下载原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadAvatarWithGroup:thumbnail:callback:completion:

下载群头像

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_thumbnail_\
设置为true下载缩略图，false下载原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadSharedFileWithGroup:sharedFile:arg3:

下载群共享文件

`- (BMXErrorCode)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
下载的群共享文件

_Callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-26='3' data-27='3' data-28='3' data-29='3' data-30='3' data-31='3' data-32='3' data-33='3' data-34='3' data-35='3' data-36='3' data-37='3' data-38='3' data-39='3' data-40='3' data-41='3' data-42='3' data-43='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadSharedFileWithGroup:sharedFile:arg3:completion:

下载群共享文件

`- (void)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
下载的群共享文件

_Callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-26='3' data-27='3' data-28='3' data-29='3' data-30='3' data-31='3' data-32='3' data-33='3' data-34='3' data-35='3' data-36='3' data-37='3' data-38='3' data-39='3' data-40='3' data-41='3' data-42='3' data-43='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### editAnnouncementWithGroup:title:content:

设置群公告

`- (BMXErrorCode)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content*`

#### Parameters

_group_\
进行操作的群组

_title_\
群公告的标题

_content_\
群公告的内容

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### editAnnouncementWithGroup:title:content:completion:

设置群公告

`- (void)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_title_\
群公告的标题

_content_\
群公告的内容

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupByIdWithGroupId:forceRefresh:completion:

通过群组id获取群信息，如果设置了forceRefresh则从服务器拉取

`- (void)fetchGroupByIdWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

_groupId_\
要搜索的群组id

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_group_\
搜索返回的群组信息，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupByIdWithGroupId:group:forceRefresh:

通过群组id获取群信息，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)fetchGroupByIdWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_groupId_\
要搜索的群组id

_group_\
搜索返回的群组信息，传入指向为空的shared\_ptr对象函数执行后从此获取返回结果

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:

通过传入群组的id列表获取群组信息列表，如果设置了forceRefresh则从服务器拉取

`- (void)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_groupIdList_\
群组id列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupsByIdListWithGroupIdList:list:forceRefresh:

通过传入群组的id列表获取群组信息列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_groupIdList_\
群组id列表

_list_\
群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchLocalGroupsByName:completion:

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

`- (void)fetchLocalGroupsByName:(NSString *)*name* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_name_\
查询的群名称关键字

_list_\
搜索结果返回的群列表信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchLocalGroupsByNameWithList:name:

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

`- (BMXErrorCode)fetchLocalGroupsByNameWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

#### Parameters

_list_\
搜索结果返回的群列表信息

_name_\
查询的群名称关键字

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### get:completion:

获取群组列表，如果设置了forceRefresh则从服务器拉取

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群组id列表，传入空列表函数返回后从此处获取返回的群组id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### get:forceRefresh:

获取群组列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)get:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_list_\
群组id列表，传入空列表函数返回后从此处获取返回的群组id列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAdmins:forceRefresh:completion:

获取Admins列表，如果设置了forceRefresh则从服务器拉取

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群管理员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAdmins:list:forceRefresh:

获取Admins列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)getAdmins:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_list_\
群管理员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAnnouncementList:forceRefresh:completion:

获取群公告列表

`- (void)getAnnouncementList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncementList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群公告列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAnnouncementList:list:forceRefresh:

获取群公告列表

`- (BMXErrorCode)getAnnouncementList:(BMXGroup *)*group* list:(BMXGroupAnnouncementList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_list_\
群公告列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getApplicationList:cursor:pageSize:completion:

分页获取群组申请列表

`- (void)getApplicationList:(BMXGroupList *)*list* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupApplicationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_list_\
需要获取群组申请列表信息的群组id列表

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
分页获取的群组申请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getApplicationList:result:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getApplicationList:result:cursor:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getApplicationList:result:cursor:pageSize:

分页获取群组申请列表

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_list_\
需要获取群组申请列表信息的群组id列表

_result_\
分页获取的群组申请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:completion:

获取禁言列表

`- (void)getBannedMembers:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroupBannedMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_list_\
群禁言列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:cursor:pageSize:completion:

分页获取禁言列表

`- (void)getBannedMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupBannedMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
分页获取的禁言列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:list:

获取禁言列表

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* list:(BMXGroupBannedMemberList *)*list*`

#### Parameters

_group_\
进行操作的群组

_list_\
群禁言列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:result:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:result:cursor:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:result:cursor:pageSize:

分页获取禁言列表

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
进行操作的群组

_result_\
分页获取的禁言列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:cursor:pageSize:completion:

分页获取黑名单

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
分页获取的黑名单列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:forceRefresh:completion:

获取黑名单

`- (void)getBlockList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群黑名单列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:list:forceRefresh:

获取黑名单

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_list_\
群黑名单列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:result:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:result:cursor:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:result:cursor:pageSize:

分页获取黑名单

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
进行操作的群组

_result_\
分页获取的黑名单列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInfo:

获取群详情，从服务端拉取最新信息

`- (BMXErrorCode)getInfo:(BMXGroup *)*group*`

#### Parameters

_group_\
要获取群组最新信息的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInfo:completion:

获取群详情，从服务端拉取最新信息

`- (void)getInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
要获取群组最新信息的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInvitationList:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInvitationList:cursor:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInvitationList:cursor:pageSize:

分页获取群组邀请列表

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_result_\
分页获取的群组邀请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInvitationList:pageSize:completion:

分页获取群组邀请列表

`- (void)getInvitationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupInvitationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
分页获取的群组邀请列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getLatestAnnouncement:announcement:forceRefresh:

获取最新的群公告

`- (BMXErrorCode)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_announcement_\
最新的群组公告，传入指向为空的shared\_ptr对象函数返回后从此处获取最新的群组公告

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getLatestAnnouncement:announcement:forceRefresh:completion:

获取最新的群公告

`- (void)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncement *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_announcement_\
最新的群组公告，传入指向为空的shared\_ptr对象函数返回后从此处获取最新的群组公告

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:cursor:pageSize:completion:

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.

`- (void)getMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
分页获取的群成员列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:forceRefresh:completion:

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群成员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:list:forceRefresh:

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_list_\
群成员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:result:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:result:cursor:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:result:cursor:pageSize:

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
进行操作的群组

_result_\
分页获取的群成员列表，传入指向为空的shared\_ptr对象函数执行后从此处获取结果

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembersNickname:members:completion:

获取群组成员详细信息

`- (void)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
要获取群组成员信息详情的群成员id

_list_\
返回的群成员详细，传入空列表在函数操作后从此处获取群成员详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembersNickname:members:list:

获取群组成员详细信息

`- (BMXErrorCode)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* list:(BMXGroupMemberList *)*list*`

#### Parameters

_group_\
进行操作的群组

_members_\
要获取群组成员信息详情的群成员id

_list_\
返回的群成员详细，传入空列表在函数操作后从此处获取群成员详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getSharedFilesList:forceRefresh:completion:

获取群共享文件列表

`- (void)getSharedFilesList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupSharedFileList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

_list_\
群共享文件列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getSharedFilesList:list:forceRefresh:

获取群共享文件列表

`- (BMXErrorCode)getSharedFilesList:(BMXGroup *)*group* list:(BMXGroupSharedFileList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
进行操作的群组

_list_\
群共享文件列表，传入空列表函数返回后从此处获取返回的群组详细信息列表

_forceRefresh_\
设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### joinWithGroup:message:

加入一个群，根据群设置可能需要管理员批准

`- (BMXErrorCode)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message*`

#### Parameters

_group_\
要加入的群组

_message_\
申请入群的信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### joinWithGroup:message:completion:

加入一个群，根据群设置可能需要管理员批准

`- (void)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
要加入的群组

_message_\
申请入群的信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### leaveWithGroup:

退出群

`- (BMXErrorCode)leaveWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
要退出的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### leaveWithGroup:completion:

退出群

`- (void)leaveWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
要退出的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### muteMessageWithGroup:mode:

设置是否屏蔽群消息

`- (BMXErrorCode)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群屏蔽的模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### muteMessageWithGroup:mode:completion:

设置是否屏蔽群消息

`- (void)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群屏蔽的模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeAdminsWithGroup:admins:reason:

删除管理员

`- (BMXErrorCode)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason*`

#### Parameters

_group_\
进行操作的群组

_admins_\
要从管理员移除的成员id列表

_reason_\
要移除管理员的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeAdminsWithGroup:admins:reason:completion:

删除管理员

`- (void)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_admins_\
要从管理员移除的成员id列表

_reason_\
要移除管理员的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeDelegate:

移除群组变化监听者

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
群组变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeGroupListener:

移除群组变化监听者

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

_listener_\
群组变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeMembersWithGroup:members:reason:

删除群成员

`- (BMXErrorCode)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason*`

#### Parameters

_group_\
进行操作的群组

_members_\
要删除的群组成员id列表

_reason_\
删除的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeMembersWithGroup:members:reason:completion:

删除群成员

`- (void)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
要删除的群组成员id列表

_reason_\
删除的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeSharedFileWithGroup:sharedFile:

移除群共享文件

`- (BMXErrorCode)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
删除的群共享文件

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeSharedFileWithGroup:sharedFile:completion:

移除群共享文件

`- (void)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_sharedFile_\
删除的群共享文件

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### searchWithGroupId:forceRefresh:completion:

`- (void)searchWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### searchWithGroupId:group:forceRefresh:

`- (BMXErrorCode)searchWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### searchWithGroupIdList:list:forceRefresh:

`- (BMXErrorCode)searchWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### searchWithList:forceRefresh:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### searchWithList:name:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAllowMemberModify:enable:

设置是否允许群成员设置群信息

`- (BMXErrorCode)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否允许操作

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAllowMemberModify:enable:completion:

设置是否允许群成员设置群信息

`- (void)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否允许操作

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAvatar:avatarPath:arg3:

设置群头像

`- (BMXErrorCode)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

_group_\
进行操作的群组

_avatarPath_\
群头像文件的本地路径

_Callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAvatar:avatarPath:arg3:completion:

设置群头像

`- (void)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_avatarPath_\
群头像文件的本地路径

_Callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setDescription:description:

设置群描述信息

`- (BMXErrorCode)setDescription:(BMXGroup *)*group* description:(NSString *)*description*`

#### Parameters

_group_\
进行操作的群组

_description_\
群组描述

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setDescription:description:completion:

设置群描述信息

`- (void)setDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_description_\
群组描述

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setEnableReadAck:enable:

设置是否开启群消息已读功能

`- (BMXErrorCode)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否开启

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setEnableReadAck:enable:completion:

设置是否开启群消息已读功能

`- (void)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否开启

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setExtension:extension:

设置群扩展信息

`- (BMXErrorCode)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension*`

#### Parameters

_group_\
进行操作的群组

_extension_\
群组的扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setExtension:extension:completion:

设置群扩展信息

`- (void)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_extension_\
群组的扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setHistoryVisible:enable:

设置群成员是否开可见群历史聊天记录

`- (BMXErrorCode)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否开启

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setHistoryVisible:enable:completion:

设置群成员是否开可见群历史聊天记录

`- (void)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_enable_\
是否开启

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setInviteMode:mode:

设置邀请模式

`- (BMXErrorCode)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群组的邀请模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setInviteMode:mode:completion:

设置邀请模式

`- (void)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群组的邀请模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setJoinAuthMode:mode:

设置入群审批模式

`- (BMXErrorCode)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode*`

#### Parameters

_group_\
进行操作的群组

_mode_\
入群审批模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setJoinAuthMode:mode:completion:

设置入群审批模式

`- (void)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_mode_\
入群审批模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMsgPushMode:mode:

设置群消息通知模式

`- (BMXErrorCode)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群消息通知模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMsgPushMode:mode:completion:

设置群消息通知模式

`- (void)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_mode_\
群消息通知模式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMyNickname:nickname:

设置在群里的昵称

`- (BMXErrorCode)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname*`

#### Parameters

_group_\
进行操作的群组

_nickname_\
用户在群组内的昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMyNickname:nickname:completion:

设置在群里的昵称

`- (void)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_nickname_\
用户在群组内的昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setName:name:

设置群名称

`- (BMXErrorCode)setName:(BMXGroup *)*group* name:(NSString *)*name*`

#### Parameters

_group_\
进行操作的群组

_name_\
群组名称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setName:name:completion:

设置群名称

`- (void)setName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_name_\
群组名称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### transferOwnerWithGroup:newOwnerId:

转移群主

`- (BMXErrorCode)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId*`

#### Parameters

_group_\
进行操作的群组

_newOwnerId_\
转让为新群主的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### transferOwnerWithGroup:newOwnerId:completion:

转移群主

`- (void)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_newOwnerId_\
转让为新群主的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanGroupWithGroup:

全员解除禁言

`- (BMXErrorCode)unbanGroupWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
进行操作的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanGroupWithGroup:completion:

全员解除禁言

`- (void)unbanGroupWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanMembersWithGroup:members:

解除禁言

`- (BMXErrorCode)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
进行操作的群组

_members_\
被解除禁言的群成员id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanMembersWithGroup:members:completion:

解除禁言

`- (void)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
被解除禁言的群成员id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unblockMembersWithGroup:members:

从黑名单删除

`- (BMXErrorCode)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
进行操作的群组

_members_\
从黑名单移除的用户id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unblockMembersWithGroup:members:completion:

从黑名单删除

`- (void)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_members_\
从黑名单移除的用户id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:

添加群共享文件

`- (BMXErrorCode)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5*`

#### Parameters

_group_\
进行操作的群组

_filePath_\
文件的本地路径

_displayName_\
文件的展示名

_extensionName_\
文件的扩展名

_Callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-62='5' data-63='5' data-64='5' data-65='5' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:

添加群共享文件

`- (void)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
进行操作的群组

_filePath_\
文件的本地路径

_displayName_\
文件的展示名

_extensionName_\
文件的扩展名

_Callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-62='5' data-63='5' data-64='5' data-65='5' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>
```
