# BMXGroupService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Group Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### acceptApplicationWithGroup:applicantId:

Accept the group application

`- (BMXErrorCode)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

#### Parameters

_group_\
The group

_applicantId_\
User ID applying to join the group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptApplicationWithGroup:applicantId:completion:

Accept the group application

`- (void)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_applicantId_\
User ID applying to join the group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptInvitationWithGroup:inviter:

Accept the group invitation

`- (BMXErrorCode)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

#### Parameters

_group_\
The group

_inviter_\
User ID of the inviter

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### acceptInvitationWithGroup:inviter:completion:

Accept the group invitation

`- (void)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_inviter_\
User ID of the inviter

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addAdminsWithGroup:admins:message:

Add admins

`- (BMXErrorCode)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message*`

#### Parameters

_group_\
The group

_admins_\
Admin ID list

_message_\
Message to added users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addAdminsWithGroup:admins:message:completion:

Add admins

`- (void)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_admins_\
Admin ID list

_message_\
Message to added users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addDelegate:

Add a group events listener

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
The group events listener

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

Add a group events listener

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

_listener_\
The group events listener

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addMembersWithGroup:members:message:

Add group members

`- (BMXErrorCode)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message*`

#### Parameters

_group_\
The group

_members_\
ID list of the added users

_message_\
Message to added users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### addMembersWithGroup:members:message:completion:

Add group members

`- (void)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
ID list of the added users

_message_\
Message to added users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banGroupWithGroup:duration:

Ban all group members

`- (BMXErrorCode)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration*`

#### Parameters

_group_\
The group

_duration_\
Ban duration (min)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banGroupWithGroup:duration:completion:

Ban all group members

`- (void)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_duration_\
Ban duration (min)

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

Ban group members

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason*`

#### Parameters

_group_\
The group

_members_\
ID list of the banned users

_duration_\
Ban duration (min)

_reason_\
Ban reason

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### banMembersWithGroup:members:duration:reason:completion:

Ban group members

`- (void)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
ID list of the banned users

_duration_\
Ban duration (min)

_reason_\
Ban reason

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### blockMembersWithGroup:members:

Block group members

`- (BMXErrorCode)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
The group

_members_\
ID list of the blocked users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### blockMembersWithGroup:members:completion:

Block group members

`- (void)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
ID list of the blocked users

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelDownloadSharedFileWithGroup:sharedFile:

Cancel downloading the group shared file

`- (BMXErrorCode)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

_group_\
The group

_sharedFile_\
The group shared file to be downloaded

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelDownloadSharedFileWithGroup:sharedFile:completion:

Cancel downloading the group shared file

`- (void)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_sharedFile_\
The group shared file to be downloaded

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelUploadSharedFileWithGroup:filePath:

Cancel uploading the group shared file

`- (BMXErrorCode)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath*`

#### Parameters

_group_\
The group

_filePath_\
Local file path

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### cancelUploadSharedFileWithGroup:filePath:completion:

Cancel uploading the group shared file

`- (void)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_filePath_\
Local file path

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### changeSharedFileNameWithGroup:sharedFile:name:

Change the group shared file name

`- (BMXErrorCode)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name*`

#### Parameters

_group_\
The group

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

Change the group shared file name

`- (void)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_sharedFile_\
The shared file

_name_\
New name of the shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### createWithOptions:completion:

Create a group

`- (void)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

_options_\
Options of group creation

_group_\
Group as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### createWithOptions:group:

Create a group

`- (BMXErrorCode)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* group:(BMXGroup *)*group*`

#### Parameters

_options_\
Options of group creation

_group_\
Group as result

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

Decline group application

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason*`

#### Parameters

_group_\
The group

_applicantId_\
User ID of group application

_reason_\
Decline reason

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineApplicationWithGroup:applicantId:reason:completion:

Decline group application

`- (void)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_applicantId_\
User ID of group application

_reason_\
Decline reason

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

Decline group invitation

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason*`

#### Parameters

_group_\
The group

_inviter_\
The inviter user ID

_reason_\
Decline reason

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### declineInvitationWithGroup:inviter:reason:completion:

Decline group invitation

`- (void)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_inviter_\
The inviter user ID

_reason_\
Decline reason

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### deleteAnnouncementWithGroup:announcementId:

Delete a group announcement

`- (BMXErrorCode)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId*`

#### Parameters

_group_\
The group

_announcementId_\
Group announcement ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### deleteAnnouncementWithGroup:announcementId:completion:

Delete a group announcement

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_announcementId_\
Group announcement ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### destroyWithGroup:

Destroy a group

`- (BMXErrorCode)destroyWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### destroyWithGroup:completion:

Destroy a group

`- (void)destroyWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadAvatarWithGroup:thumbnail:callback:

Downlad the group avatar

`- (BMXErrorCode)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_group_\
The group

_thumbnail_\
Is the file to be downloaded a thumbnail

_callback_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadAvatarWithGroup:thumbnail:callback:completion:

Downlad the group avatar

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_thumbnail_\
Is the file to be downloaded a thumbnail

_callback_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadSharedFileWithGroup:sharedFile:arg3:

Download a group shared file

`- (BMXErrorCode)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

_group_\
The group

_sharedFile_\
The shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-26='3' data-27='3' data-28='3' data-29='3' data-30='3' data-31='3' data-32='3' data-33='3' data-34='3' data-35='3' data-36='3' data-37='3' data-38='3' data-39='3' data-40='3' data-41='3' data-42='3' data-43='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### downloadSharedFileWithGroup:sharedFile:arg3:completion:

Download a group shared file

`- (void)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_sharedFile_\
The shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-26='3' data-27='3' data-28='3' data-29='3' data-30='3' data-31='3' data-32='3' data-33='3' data-34='3' data-35='3' data-36='3' data-37='3' data-38='3' data-39='3' data-40='3' data-41='3' data-42='3' data-43='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### editAnnouncementWithGroup:title:content:

Add a new group anncoucement

`- (BMXErrorCode)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content*`

#### Parameters

_group_\
The group

_title_\
The title of group annoucement

_content_\
The content of group annoucement

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### editAnnouncementWithGroup:title:content:completion:

Add a new group anncoucement

`- (void)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_title_\
The title of group annoucement

_content_\
The content of group annoucement

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupByIdWithGroupId:forceRefresh:completion:

Get group by ID

`- (void)fetchGroupByIdWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

_groupId_\
The group ID

_forceRefresh_\
from server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupByIdWithGroupId:group:forceRefresh:

Get group by ID

`- (BMXErrorCode)fetchGroupByIdWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_groupId_\
The group ID

_forceRefresh_\
from server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:

Get groups by ID list

`- (void)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_groupIdList_\
Group ID list

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchGroupsByIdListWithGroupIdList:list:forceRefresh:

Get groups by ID list

`- (BMXErrorCode)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_groupIdList_\
Group ID list

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchLocalGroupsByName:completion:

Get groups by name from local db

`- (void)fetchLocalGroupsByName:(NSString *)*name* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_name_\
Group name

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### fetchLocalGroupsByNameWithList:name:

Get groups by name from local db

`- (BMXErrorCode)fetchLocalGroupsByNameWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

#### Parameters

_name_\
Group name

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### get:completion:

Get my group list

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### get:forceRefresh:

Get my group list

`- (BMXErrorCode)get:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAdmins:forceRefresh:completion:

Get admins of a group

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAdmins:list:forceRefresh:

Get admins of a group

`- (BMXErrorCode)getAdmins:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAnnouncementList:forceRefresh:completion:

Get announcement list

`- (void)getAnnouncementList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncementList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getAnnouncementList:list:forceRefresh:

Get announcement list

`- (BMXErrorCode)getAnnouncementList:(BMXGroup *)*group* list:(BMXGroupAnnouncementList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getApplicationList:cursor:pageSize:completion:

Get group application list in pages

`- (void)getApplicationList:(BMXGroupList *)*list* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupApplicationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_list_\
Group list

_cursor_\
Start cursor

_pageSize_\
Page size

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

Get group application list in pages

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_list_\
Group list

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:completion:

Get group members banned

`- (void)getBannedMembers:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroupBannedMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:cursor:pageSize:completion:

Get group members banned in pages

`- (void)getBannedMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupBannedMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBannedMembers:list:

Get group members banned

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* list:(BMXGroupBannedMemberList *)*list*`

#### Parameters

_group_\
The group

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

Get group members banned in pages

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:cursor:pageSize:completion:

Get group members blocked in pages

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:forceRefresh:completion:

Get group members blocked

`- (void)getBlockList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getBlockList:list:forceRefresh:

Get group members blocked

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

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

Get group members blocked in pages

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInfo:

Get group detail information from server

`- (BMXErrorCode)getInfo:(BMXGroup *)*group*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInfo:completion:

Get group detail information from server

`- (void)getInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

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

Get group invitation list in pages

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getInvitationList:pageSize:completion:

Get group invitation list in pages

`- (void)getInvitationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupInvitationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getLatestAnnouncement:announcement:forceRefresh:

Get the latest announcement

`- (BMXErrorCode)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getLatestAnnouncement:announcement:forceRefresh:completion:

Get the latest announcement

`- (void)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncement *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:cursor:pageSize:completion:

Get group members in pages

`- (void)getMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:forceRefresh:completion:

Get group members

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembers:list:forceRefresh:

Get group members

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

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

Get group members in pages

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_group_\
The group

_cursor_\
Starting cursor

_pageSize_\
Page size

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembersNickname:members:completion:

Get group member details by member ID list

`- (void)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getMembersNickname:members:list:

Get group member details by member ID list

`- (BMXErrorCode)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* list:(BMXGroupMemberList *)*list*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getSharedFilesList:forceRefresh:completion:

Get shared file list of group

`- (void)getSharedFilesList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupSharedFileList *res , BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### getSharedFilesList:list:forceRefresh:

Get shared file list of group

`- (BMXErrorCode)getSharedFilesList:(BMXGroup *)*group* list:(BMXGroupSharedFileList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_group_\
The group

_forceRefresh_\
From server

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

Apply to join a group

`- (BMXErrorCode)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message*`

#### Parameters

_group_\
The group

_message_\
Message sent to admins

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### joinWithGroup:message:completion:

Apply to join a group

`- (void)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_message_\
Message sent to admins

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### leaveWithGroup:

Leave a group

`- (BMXErrorCode)leaveWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### leaveWithGroup:completion:

Leave a group

`- (void)leaveWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### muteMessageWithGroup:mode:

Mute message notifications from the group

`- (BMXErrorCode)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode*`

#### Parameters

_group_\
The group

_mode_\
Mute mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### muteMessageWithGroup:mode:completion:

Mute message notifications from the group

`- (void)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_mode_\
Mute mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeAdminsWithGroup:admins:reason:

Remove admins from group

`- (BMXErrorCode)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason*`

#### Parameters

_group_\
The group

_admins_\
Admin ID list

_reason_\
Reason for removal

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeAdminsWithGroup:admins:reason:completion:

Remove admins from group

`- (void)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_admins_\
Admin ID list

_reason_\
Reason for removal

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeDelegate:

Remove group service listener

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
The listener

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeGroupListener:

Remove group service listener

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

_listener_\
The listener

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeMembersWithGroup:members:reason:

Remove members from group

`- (BMXErrorCode)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

_reason_\
Reason for removal

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeMembersWithGroup:members:reason:completion:

Remove members from group

`- (void)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

_reason_\
Reason for removal

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeSharedFileWithGroup:sharedFile:

Remove the shared files from the group

`- (BMXErrorCode)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

_group_\
The group

_sharedFile_\
The shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### removeSharedFileWithGroup:sharedFile:completion:

Remove the shared files from the group

`- (void)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_sharedFile_\
The shared file

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

Set whether to allow group members to set group information

`- (BMXErrorCode)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAllowMemberModify:enable:completion:

Set whether to allow group members to set group information

`- (void)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAvatar:avatarPath:arg3:

Set group avatar

`- (BMXErrorCode)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

_group_\
The group

_avatarPath_\
The local file path of avatar

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setAvatar:avatarPath:arg3:completion:

Set group avatar

`- (void)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_avatarPath_\
The local file path of avatar

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='3' data-2='3' data-3='3' data-4='3' data-5='3' data-6='3' data-7='3' data-8='3' data-9='3' data-10='3' data-11='3' data-12='3' data-13='3' data-14='3' data-15='3' data-16='3' data-17='3' data-18='3' data-19='3' data-20='3' data-21='3' data-22='3' data-23='3' data-24='3' data-25='3' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setDescription:description:

Set group description

`- (BMXErrorCode)setDescription:(BMXGroup *)*group* description:(NSString *)*description*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setDescription:description:completion:

Set group description

`- (void)setDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setEnableReadAck:enable:

Set whether to enable the read ACK function of the group

`- (BMXErrorCode)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setEnableReadAck:enable:completion:

Set whether to enable the read ACK function of the group

`- (void)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setExtension:extension:

Set group extension information

`- (BMXErrorCode)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension*`

#### Parameters

_group_\
The group

_extension_\
Extension information of the group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setExtension:extension:completion:

Set group extension information

`- (void)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_extension_\
Extension information of the group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setHistoryVisible:enable:

Set whether group members can see group history messages

`- (BMXErrorCode)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setHistoryVisible:enable:completion:

Set whether group members can see group history messages

`- (void)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setInviteMode:mode:

Set invitation mode

`- (BMXErrorCode)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode*`

#### Parameters

_group_\
The group

_mode_\
Invitation mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setInviteMode:mode:completion:

Set invitation mode

`- (void)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_mode_\
Invitation mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setJoinAuthMode:mode:

Set authorization mode

`- (BMXErrorCode)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode*`

#### Parameters

_group_\
The group

_mode_\
Authorization mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setJoinAuthMode:mode:completion:

Set invitation mode

`- (void)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_mode_\
Authorization mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMsgPushMode:mode:

Set message notification mode

`- (BMXErrorCode)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode*`

#### Parameters

_group_\
The group

_mode_\
Notification mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMsgPushMode:mode:completion:

Set message notification mode

`- (void)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_mode_\
Notification mode

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMyNickname:nickname:

Set my nickname in the group

`- (BMXErrorCode)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname*`

#### Parameters

_group_\
The group

_nickname_\
My nickname

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setMyNickname:nickname:completion:

Set my nickname in the group

`- (void)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_nickname_\
My nickname

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setName:name:

Set group name

`- (BMXErrorCode)setName:(BMXGroup *)*group* name:(NSString *)*name*`

#### Parameters

_group_\
The group

_name_\
Group name

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### setName:name:completion:

Set group name

`- (void)setName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_name_\
Group name

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### transferOwnerWithGroup:newOwnerId:

Transfer the owership of the group

`- (BMXErrorCode)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId*`

#### Parameters

_group_\
The group

_newOwnerId_\
New owner User ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### transferOwnerWithGroup:newOwnerId:completion:

Transfer the owership of the group

`- (void)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_newOwnerId_\
New owner User ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanGroupWithGroup:

Unban all members in the group

`- (BMXErrorCode)unbanGroupWithGroup:(BMXGroup *)*group*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanGroupWithGroup:completion:

Unban all members in the group

`- (void)unbanGroupWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanMembersWithGroup:members:

Unban members in the group

`- (BMXErrorCode)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unbanMembersWithGroup:members:completion:

Unban members in the group

`- (void)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unblockMembersWithGroup:members:

Unblock members in the group

`- (BMXErrorCode)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### unblockMembersWithGroup:members:completion:

Unblock members in the group

`- (void)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_members_\
Group members ID list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:

Upload shared file to group

`- (BMXErrorCode)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5*`

#### Parameters

_group_\
The group

_filePath_\
Local path of the shared file

_displayName_\
Display name

_extensionName_\
Extension name of the shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-62='5' data-63='5' data-64='5' data-65='5' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>

```

### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:

Upload shared file to group

`- (void)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_group_\
The group

_filePath_\
Local path of the shared file

_displayName_\
Display name

_extensionName_\
Extension name of the shared file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-62='5' data-63='5' data-64='5' data-65='5' data-repo='lanying-im-ios' data-class='BMXGroupService'></div>
```
