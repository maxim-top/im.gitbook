# BMXGroupService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Group Service

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/acceptApplicationWithGroup:applicantId:" title="acceptApplicationWithGroup:applicantId:"></a>
### acceptApplicationWithGroup:applicantId:

Accept the group application

`- (BMXErrorCode)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

#### Parameters

*group*  
   The group  

*applicantId*  
   User ID applying to join the group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptApplicationWithGroup:applicantId:completion:" title="acceptApplicationWithGroup:applicantId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="acceptApplicationWithGroup:applicantId:" %}{% endlanying_code_snippet %}
```
### acceptApplicationWithGroup:applicantId:completion:

Accept the group application

`- (void)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group 

*applicantId*  
   User ID applying to join the group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptInvitationWithGroup:inviter:" title="acceptInvitationWithGroup:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="acceptApplicationWithGroup:applicantId:completion:" %}{% endlanying_code_snippet %}
```
### acceptInvitationWithGroup:inviter:

Accept the group invitation

`- (BMXErrorCode)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

#### Parameters

*group*  
   The group

*inviter*  
   User ID of the inviter

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptInvitationWithGroup:inviter:completion:" title="acceptInvitationWithGroup:inviter:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="acceptInvitationWithGroup:inviter:" %}{% endlanying_code_snippet %}
```
### acceptInvitationWithGroup:inviter:completion:

Accept the group invitation

`- (void)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*inviter*  
   User ID of the inviter

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addAdminsWithGroup:admins:message:" title="addAdminsWithGroup:admins:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="acceptInvitationWithGroup:inviter:completion:" %}{% endlanying_code_snippet %}
```
### addAdminsWithGroup:admins:message:

Add admins

`- (BMXErrorCode)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message*`

#### Parameters

*group*  
   The group

*admins*  
   Admin ID list

*message*  
   Message to added users

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addAdminsWithGroup:admins:message:completion:" title="addAdminsWithGroup:admins:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addAdminsWithGroup:admins:message:" %}{% endlanying_code_snippet %}
```
### addAdminsWithGroup:admins:message:completion:

Add admins

`- (void)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*admins*  
   Admin ID list

*message*  
   Message to added users

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addAdminsWithGroup:admins:message:completion:" %}{% endlanying_code_snippet %}
```
### addDelegate:

Add a group events listener

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
   The group events listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addGroupListener:" title="addGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addGroupListener:

Add a group events listener

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

*listener*  
   The group events listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addMembersWithGroup:members:message:" title="addMembersWithGroup:members:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addGroupListener:" %}{% endlanying_code_snippet %}
```
### addMembersWithGroup:members:message:

Add group members

`- (BMXErrorCode)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the added users

*message*  
   Message to added users 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addMembersWithGroup:members:message:completion:" title="addMembersWithGroup:members:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addMembersWithGroup:members:message:" %}{% endlanying_code_snippet %}
```
### addMembersWithGroup:members:message:completion:

Add group members

`- (void)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the added users

*message*  
   Message to added users 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banGroupWithGroup:duration:" title="banGroupWithGroup:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="addMembersWithGroup:members:message:completion:" %}{% endlanying_code_snippet %}
```
### banGroupWithGroup:duration:

Ban all group members

`- (BMXErrorCode)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration*`

#### Parameters

*group*  
   The group

*duration*  
   Ban duration (min)

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banGroupWithGroup:duration:completion:" title="banGroupWithGroup:duration:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="banGroupWithGroup:duration:" %}{% endlanying_code_snippet %}
```
### banGroupWithGroup:duration:completion:

Ban all group members

`- (void)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group  

*duration*  
   Ban duration (min)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banMembersWithGroup:members:duration:" title="banMembersWithGroup:members:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="banGroupWithGroup:duration:completion:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration*`

<a name="//api/name/banMembersWithGroup:members:duration:reason:" title="banMembersWithGroup:members:duration:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="banMembersWithGroup:members:duration:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:reason:

Ban group members

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the banned users

*duration*  
   Ban duration (min)

*reason*  
   Ban reason

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banMembersWithGroup:members:duration:reason:completion:" title="banMembersWithGroup:members:duration:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="banMembersWithGroup:members:duration:reason:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:reason:completion:

Ban group members

`- (void)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the banned users

*duration*  
   Ban duration (min)

*reason*  
   Ban reason  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockMembersWithGroup:members:" title="blockMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="banMembersWithGroup:members:duration:reason:completion:" %}{% endlanying_code_snippet %}
```
### blockMembersWithGroup:members:

Block group members

`- (BMXErrorCode)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the blocked users

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockMembersWithGroup:members:completion:" title="blockMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="blockMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### blockMembersWithGroup:members:completion:

Block group members

`- (void)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*members*  
   ID list of the blocked users

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadSharedFileWithGroup:sharedFile:" title="cancelDownloadSharedFileWithGroup:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="blockMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### cancelDownloadSharedFileWithGroup:sharedFile:

Cancel downloading the group shared file

`- (BMXErrorCode)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

*group*  
   The group

*sharedFile*  
   The group shared file to be downloaded

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadSharedFileWithGroup:sharedFile:completion:" title="cancelDownloadSharedFileWithGroup:sharedFile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="cancelDownloadSharedFileWithGroup:sharedFile:" %}{% endlanying_code_snippet %}
```
### cancelDownloadSharedFileWithGroup:sharedFile:completion:

Cancel downloading the group shared file

`- (void)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*sharedFile*  
   The group shared file to be downloaded

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadSharedFileWithGroup:filePath:" title="cancelUploadSharedFileWithGroup:filePath:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="cancelDownloadSharedFileWithGroup:sharedFile:completion:" %}{% endlanying_code_snippet %}
```
### cancelUploadSharedFileWithGroup:filePath:

Cancel uploading the group shared file

`- (BMXErrorCode)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath*`

#### Parameters

*group*  
   The group

*filePath*  
   Local file path

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadSharedFileWithGroup:filePath:completion:" title="cancelUploadSharedFileWithGroup:filePath:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="cancelUploadSharedFileWithGroup:filePath:" %}{% endlanying_code_snippet %}
```
### cancelUploadSharedFileWithGroup:filePath:completion:

Cancel uploading the group shared file

`- (void)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*filePath*  
   Local file path

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeSharedFileNameWithGroup:sharedFile:name:" title="changeSharedFileNameWithGroup:sharedFile:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="cancelUploadSharedFileWithGroup:filePath:completion:" %}{% endlanying_code_snippet %}
```
### changeSharedFileNameWithGroup:sharedFile:name:

Change the group shared file name

`- (BMXErrorCode)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name*`

#### Parameters

*group*  
   The group

*sharedFile*  
   进行更改的群共享文件  

*name*  
   修改的群共享文件名称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeSharedFileNameWithGroup:sharedFile:name:completion:" title="changeSharedFileNameWithGroup:sharedFile:name:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="changeSharedFileNameWithGroup:sharedFile:name:" %}{% endlanying_code_snippet %}
```
### changeSharedFileNameWithGroup:sharedFile:name:completion:

Change the group shared file name

`- (void)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*sharedFile*  
   The shared file

*name*  
   New name of the shared file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createWithOptions:completion:" title="createWithOptions:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="changeSharedFileNameWithGroup:sharedFile:name:completion:" %}{% endlanying_code_snippet %}
```
### createWithOptions:completion:

Create a group

`- (void)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

*options*  
   Options of group creation 

*group*  
   Group as result  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createWithOptions:group:" title="createWithOptions:group:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="createWithOptions:completion:" %}{% endlanying_code_snippet %}
```
### createWithOptions:group:

Create a group

`- (BMXErrorCode)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* group:(BMXGroup *)*group*`

#### Parameters

*options*  
   Options of group creation 

*group*  
   Group as result

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="createWithOptions:group:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/declineApplicationWithGroup:applicantId:" title="declineApplicationWithGroup:applicantId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="dealloc" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

<a name="//api/name/declineApplicationWithGroup:applicantId:reason:" title="declineApplicationWithGroup:applicantId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineApplicationWithGroup:applicantId:" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:reason:

Decline group application

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason*`

#### Parameters

*group*  
   The group

*applicantId*  
   User ID of group application

*reason*  
   Decline reason  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineApplicationWithGroup:applicantId:reason:completion:" title="declineApplicationWithGroup:applicantId:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineApplicationWithGroup:applicantId:reason:" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:reason:completion:

Decline group application

`- (void)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*applicantId*  
   User ID of group application

*reason*  
   Decline reason

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineInvitationWithGroup:inviter:" title="declineInvitationWithGroup:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineApplicationWithGroup:applicantId:reason:completion:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

<a name="//api/name/declineInvitationWithGroup:inviter:reason:" title="declineInvitationWithGroup:inviter:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineInvitationWithGroup:inviter:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:reason:

Decline group invitation

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason*`

#### Parameters

*group*  
   The group

*inviter*  
   The inviter user ID

*reason*  
   Decline reason

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineInvitationWithGroup:inviter:reason:completion:" title="declineInvitationWithGroup:inviter:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineInvitationWithGroup:inviter:reason:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:reason:completion:

Decline group invitation

`- (void)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group  

*inviter*  
   The inviter user ID

*reason*  
   Decline reason

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:" title="deleteAnnouncementWithGroup:announcementId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="declineInvitationWithGroup:inviter:reason:completion:" %}{% endlanying_code_snippet %}
```
### deleteAnnouncementWithGroup:announcementId:

Delete a group announcement

`- (BMXErrorCode)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId*`

#### Parameters

*group*  
   The group  

*announcementId*  
   Group announcement ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:completion:" title="deleteAnnouncementWithGroup:announcementId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="deleteAnnouncementWithGroup:announcementId:" %}{% endlanying_code_snippet %}
```
### deleteAnnouncementWithGroup:announcementId:completion:

Delete a group announcement

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*announcementId*  
   Group announcement ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/destroyWithGroup:" title="destroyWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="deleteAnnouncementWithGroup:announcementId:completion:" %}{% endlanying_code_snippet %}
```
### destroyWithGroup:

Destroy a group

`- (BMXErrorCode)destroyWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
   The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/destroyWithGroup:completion:" title="destroyWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="destroyWithGroup:" %}{% endlanying_code_snippet %}
```
### destroyWithGroup:completion:

Destroy a group

`- (void)destroyWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithGroup:thumbnail:callback:" title="downloadAvatarWithGroup:thumbnail:callback:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="destroyWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithGroup:thumbnail:callback:

Downlad the group avatar

`- (BMXErrorCode)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

*group*  
   The group

*thumbnail*  
   Is the file to be downloaded a thumbnail

*callback*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithGroup:thumbnail:callback:completion:" title="downloadAvatarWithGroup:thumbnail:callback:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="downloadAvatarWithGroup:thumbnail:callback:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithGroup:thumbnail:callback:completion:

Downlad the group avatar

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group  

*thumbnail*  
   Is the file to be downloaded a thumbnail

*callback*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadSharedFileWithGroup:sharedFile:arg3:" title="downloadSharedFileWithGroup:sharedFile:arg3:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="downloadAvatarWithGroup:thumbnail:callback:completion:" %}{% endlanying_code_snippet %}
```
### downloadSharedFileWithGroup:sharedFile:arg3:

Download a group shared file

`- (BMXErrorCode)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

*group*  
   The group

*sharedFile*  
   The shared file 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadSharedFileWithGroup:sharedFile:arg3:completion:" title="downloadSharedFileWithGroup:sharedFile:arg3:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="downloadSharedFileWithGroup:sharedFile:arg3:" %}{% endlanying_code_snippet %}
```
### downloadSharedFileWithGroup:sharedFile:arg3:completion:

Download a group shared file

`- (void)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*sharedFile*  
   The shared file 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/editAnnouncementWithGroup:title:content:" title="editAnnouncementWithGroup:title:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="downloadSharedFileWithGroup:sharedFile:arg3:completion:" %}{% endlanying_code_snippet %}
```
### editAnnouncementWithGroup:title:content:

Add a new group anncoucement

`- (BMXErrorCode)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content*`

#### Parameters

*group*  
   The group

*title*  
   The title of group annoucement

*content*  
   The content of group annoucement

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/editAnnouncementWithGroup:title:content:completion:" title="editAnnouncementWithGroup:title:content:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="editAnnouncementWithGroup:title:content:" %}{% endlanying_code_snippet %}
```
### editAnnouncementWithGroup:title:content:completion:

Add a new group anncoucement

`- (void)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*title*  
   The title of group annoucement

*content*  
    The content of group annoucement

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupByIdWithGroupId:forceRefresh:completion:" title="fetchGroupByIdWithGroupId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="editAnnouncementWithGroup:title:content:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupByIdWithGroupId:forceRefresh:completion:

Get group by ID

`- (void)fetchGroupByIdWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

*groupId*  
   The group ID

*forceRefresh*  
   from server  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupByIdWithGroupId:group:forceRefresh:" title="fetchGroupByIdWithGroupId:group:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchGroupByIdWithGroupId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupByIdWithGroupId:group:forceRefresh:

Get group by ID

`- (BMXErrorCode)fetchGroupByIdWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*groupId*  
   The group ID

*forceRefresh*  
   from server  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:" title="fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchGroupByIdWithGroupId:group:forceRefresh:" %}{% endlanying_code_snippet %}
```
### fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:

Get groups by ID list

`- (void)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*groupIdList*  
   Group ID list  

*forceRefresh*  
   From server 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupsByIdListWithGroupIdList:list:forceRefresh:" title="fetchGroupsByIdListWithGroupIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupsByIdListWithGroupIdList:list:forceRefresh:

Get groups by ID list

`- (BMXErrorCode)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*groupIdList*  
   Group ID list
 

*forceRefresh*  
   From server  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchLocalGroupsByName:completion:" title="fetchLocalGroupsByName:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchGroupsByIdListWithGroupIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### fetchLocalGroupsByName:completion:

Get groups by name from local db

`- (void)fetchLocalGroupsByName:(NSString *)*name* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   Group name

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchLocalGroupsByNameWithList:name:" title="fetchLocalGroupsByNameWithList:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchLocalGroupsByName:completion:" %}{% endlanying_code_snippet %}
```
### fetchLocalGroupsByNameWithList:name:

Get groups by name from local db

`- (BMXErrorCode)fetchLocalGroupsByNameWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

#### Parameters

*name*  
   Group name  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/get:completion:" title="get:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="fetchLocalGroupsByNameWithList:name:" %}{% endlanying_code_snippet %}
```
### get:completion:

Get my group list

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*forceRefresh*  
   From server  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/get:forceRefresh:" title="get:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="get:completion:" %}{% endlanying_code_snippet %}
```
### get:forceRefresh:

Get my group list

`- (BMXErrorCode)get:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*forceRefresh*  
   From server  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAdmins:forceRefresh:completion:" title="getAdmins:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="get:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getAdmins:forceRefresh:completion:

Get admins of a group

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group

*forceRefresh*  
   From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAdmins:list:forceRefresh:" title="getAdmins:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getAdmins:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getAdmins:list:forceRefresh:

Get admins of a group

`- (BMXErrorCode)getAdmins:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   The group

*forceRefresh*  
   From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAnnouncementList:forceRefresh:completion:" title="getAnnouncementList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getAdmins:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getAnnouncementList:forceRefresh:completion:

Get announcement list

`- (void)getAnnouncementList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncementList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   The group  

*forceRefresh*  
   From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAnnouncementList:list:forceRefresh:" title="getAnnouncementList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getAnnouncementList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getAnnouncementList:list:forceRefresh:

Get announcement list

`- (BMXErrorCode)getAnnouncementList:(BMXGroup *)*group* list:(BMXGroupAnnouncementList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   The group  

*forceRefresh*  
   From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:cursor:pageSize:completion:" title="getApplicationList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getAnnouncementList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getApplicationList:cursor:pageSize:completion:

Get group application list in pages

`- (void)getApplicationList:(BMXGroupList *)*list* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupApplicationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*list*  
   Group list  

*cursor*  
   Start cursor  

*pageSize*  
   Page size

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:result:" title="getApplicationList:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getApplicationList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result*`

<a name="//api/name/getApplicationList:result:cursor:" title="getApplicationList:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getApplicationList:result:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:cursor:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getApplicationList:result:cursor:pageSize:" title="getApplicationList:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getApplicationList:result:cursor:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:cursor:pageSize:

Get group application list in pages

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*list*  
   Group list

*cursor*  
   Starting cursor

*pageSize*  
   Page size  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:completion:" title="getBannedMembers:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getApplicationList:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:completion:

Get group members banned

`- (void)getBannedMembers:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroupBannedMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:cursor:pageSize:completion:" title="getBannedMembers:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:completion:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:cursor:pageSize:completion:

Get group members banned in pages

`- (void)getBannedMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupBannedMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*cursor*  
   Starting cursor

*pageSize*  
   Page size  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:list:" title="getBannedMembers:list:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:list:

Get group members banned

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* list:(BMXGroupBannedMemberList *)*list*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:result:" title="getBannedMembers:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:list:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result*`

<a name="//api/name/getBannedMembers:result:cursor:" title="getBannedMembers:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:result:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:cursor:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getBannedMembers:result:cursor:pageSize:" title="getBannedMembers:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:result:cursor:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:cursor:pageSize:

Get group members banned in pages

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
    The group

*cursor*  
   Starting cursor

*pageSize*  
   Page size  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:cursor:pageSize:completion:" title="getBlockList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBannedMembers:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getBlockList:cursor:pageSize:completion:

Get group members blocked in pages

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*cursor*  
   Starting cursor

*pageSize*  
   Page size  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:forceRefresh:completion:" title="getBlockList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:forceRefresh:completion:

Get group members blocked 

`- (void)getBlockList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server
    
#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:list:forceRefresh:" title="getBlockList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:list:forceRefresh:

Get group members blocked 

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
    The group
    
*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:result:" title="getBlockList:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

<a name="//api/name/getBlockList:result:cursor:" title="getBlockList:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:result:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:cursor:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getBlockList:result:cursor:pageSize:" title="getBlockList:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:result:cursor:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:cursor:pageSize:

Get group members blocked in pages

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
    The group

*cursor*  
   Starting cursor

*pageSize*  
   Page size  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInfo:" title="getInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getBlockList:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getInfo:

Get group detail information from server

`- (BMXErrorCode)getInfo:(BMXGroup *)*group*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInfo:completion:" title="getInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInfo:" %}{% endlanying_code_snippet %}
```
### getInfo:completion:

Get group detail information from server

`- (void)getInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInvitationList:" title="getInvitationList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInfo:completion:" %}{% endlanying_code_snippet %}
```
### getInvitationList:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result*`

<a name="//api/name/getInvitationList:cursor:" title="getInvitationList:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInvitationList:" %}{% endlanying_code_snippet %}
```
### getInvitationList:cursor:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getInvitationList:cursor:pageSize:" title="getInvitationList:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInvitationList:cursor:" %}{% endlanying_code_snippet %}
```
### getInvitationList:cursor:pageSize:

Get group invitation list in pages

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*cursor*  
    Starting cursor

*pageSize*  
    Page size

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInvitationList:pageSize:completion:" title="getInvitationList:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInvitationList:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getInvitationList:pageSize:completion:

Get group invitation list in pages

`- (void)getInvitationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupInvitationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*cursor*  
    Starting cursor

*pageSize*  
    Page size

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLatestAnnouncement:announcement:forceRefresh:" title="getLatestAnnouncement:announcement:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getInvitationList:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getLatestAnnouncement:announcement:forceRefresh:

Get the latest announcement

`- (BMXErrorCode)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLatestAnnouncement:announcement:forceRefresh:completion:" title="getLatestAnnouncement:announcement:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getLatestAnnouncement:announcement:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getLatestAnnouncement:announcement:forceRefresh:completion:

Get the latest announcement

`- (void)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncement *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:cursor:pageSize:completion:" title="getMembers:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getLatestAnnouncement:announcement:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:cursor:pageSize:completion:

Get group members in pages

`- (void)getMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*cursor*  
    Starting cursor

*pageSize*  
    Page size

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:forceRefresh:completion:" title="getMembers:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:forceRefresh:completion:

Get group members

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:list:forceRefresh:" title="getMembers:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:list:forceRefresh:

Get group members

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:result:" title="getMembers:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getMembers:result:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

<a name="//api/name/getMembers:result:cursor:" title="getMembers:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:result:" %}{% endlanying_code_snippet %}
```
### getMembers:result:cursor:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getMembers:result:cursor:pageSize:" title="getMembers:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:result:cursor:" %}{% endlanying_code_snippet %}
```
### getMembers:result:cursor:pageSize:

Get group members in pages

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
    The group

*cursor*  
    Starting cursor

*pageSize*  
    Page size

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembersNickname:members:completion:" title="getMembersNickname:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembers:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getMembersNickname:members:completion:

Get group member details by member ID list

`- (void)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembersNickname:members:list:" title="getMembersNickname:members:list:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembersNickname:members:completion:" %}{% endlanying_code_snippet %}
```
### getMembersNickname:members:list:

Get group member details by member ID list

`- (BMXErrorCode)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* list:(BMXGroupMemberList *)*list*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSharedFilesList:forceRefresh:completion:" title="getSharedFilesList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getMembersNickname:members:list:" %}{% endlanying_code_snippet %}
```
### getSharedFilesList:forceRefresh:completion:

Get shared file list of group

`- (void)getSharedFilesList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupSharedFileList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSharedFilesList:list:forceRefresh:" title="getSharedFilesList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getSharedFilesList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getSharedFilesList:list:forceRefresh:

Get shared file list of group

`- (BMXErrorCode)getSharedFilesList:(BMXGroup *)*group* list:(BMXGroupSharedFileList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
    The group

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="getSharedFilesList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/joinWithGroup:message:" title="joinWithGroup:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### joinWithGroup:message:

Apply to join a group

`- (BMXErrorCode)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message*`

#### Parameters

*group*  
    The group

*message*  
    Message sent to admins 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/joinWithGroup:message:completion:" title="joinWithGroup:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="joinWithGroup:message:" %}{% endlanying_code_snippet %}
```
### joinWithGroup:message:completion:

Apply to join a group

`- (void)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*message*  
    Message sent to admins 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/leaveWithGroup:" title="leaveWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="joinWithGroup:message:completion:" %}{% endlanying_code_snippet %}
```
### leaveWithGroup:

Leave a group

`- (BMXErrorCode)leaveWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/leaveWithGroup:completion:" title="leaveWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="leaveWithGroup:" %}{% endlanying_code_snippet %}
```
### leaveWithGroup:completion:

Leave a group

`- (void)leaveWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteMessageWithGroup:mode:" title="muteMessageWithGroup:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="leaveWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### muteMessageWithGroup:mode:

Mute message notifications from the group

`- (BMXErrorCode)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode*`

#### Parameters

*group*  
    The group

*mode*  
    Mute mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteMessageWithGroup:mode:completion:" title="muteMessageWithGroup:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="muteMessageWithGroup:mode:" %}{% endlanying_code_snippet %}
```
### muteMessageWithGroup:mode:completion:

Mute message notifications from the group

`- (void)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*mode*  
    Mute mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAdminsWithGroup:admins:reason:" title="removeAdminsWithGroup:admins:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="muteMessageWithGroup:mode:completion:" %}{% endlanying_code_snippet %}
```
### removeAdminsWithGroup:admins:reason:

Remove admins from group

`- (BMXErrorCode)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason*`

#### Parameters

*group*  
    The group

*admins*  
    Admin ID list

*reason*  
    Reason for removal

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAdminsWithGroup:admins:reason:completion:" title="removeAdminsWithGroup:admins:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeAdminsWithGroup:admins:reason:" %}{% endlanying_code_snippet %}
```
### removeAdminsWithGroup:admins:reason:completion:

Remove admins from group

`- (void)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*admins*  
    Admin ID list

*reason*  
    Reason for removal

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeAdminsWithGroup:admins:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

Remove group service listener

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
    The listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeGroupListener:" title="removeGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeGroupListener:

Remove group service listener

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

*listener*  
    The listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMembersWithGroup:members:reason:" title="removeMembersWithGroup:members:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeGroupListener:" %}{% endlanying_code_snippet %}
```
### removeMembersWithGroup:members:reason:

Remove members from group

`- (BMXErrorCode)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

*reason*  
    Reason for removal

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMembersWithGroup:members:reason:completion:" title="removeMembersWithGroup:members:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeMembersWithGroup:members:reason:" %}{% endlanying_code_snippet %}
```
### removeMembersWithGroup:members:reason:completion:

Remove members from group

`- (void)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

*reason*  
    Reason for removal

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeSharedFileWithGroup:sharedFile:" title="removeSharedFileWithGroup:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeMembersWithGroup:members:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeSharedFileWithGroup:sharedFile:

Remove the shared files from the group

`- (BMXErrorCode)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

*group*  
    The group

*sharedFile*  
    The shared file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeSharedFileWithGroup:sharedFile:completion:" title="removeSharedFileWithGroup:sharedFile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeSharedFileWithGroup:sharedFile:" %}{% endlanying_code_snippet %}
```
### removeSharedFileWithGroup:sharedFile:completion:

Remove the shared files from the group

`- (void)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*sharedFile*  
    The shared file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchWithGroupId:forceRefresh:completion:" title="searchWithGroupId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="removeSharedFileWithGroup:sharedFile:completion:" %}{% endlanying_code_snippet %}
```
### searchWithGroupId:forceRefresh:completion:

`- (void)searchWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

<a name="//api/name/searchWithGroupId:group:forceRefresh:" title="searchWithGroupId:group:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="searchWithGroupId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### searchWithGroupId:group:forceRefresh:

`- (BMXErrorCode)searchWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithGroupIdList:list:forceRefresh:" title="searchWithGroupIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="searchWithGroupId:group:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithGroupIdList:list:forceRefresh:

`- (BMXErrorCode)searchWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithList:forceRefresh:" title="searchWithList:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="searchWithGroupIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithList:forceRefresh:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithList:name:" title="searchWithList:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="searchWithList:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithList:name:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

<a name="//api/name/setAllowMemberModify:enable:" title="setAllowMemberModify:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="searchWithList:name:" %}{% endlanying_code_snippet %}
```
### setAllowMemberModify:enable:

Set whether to allow group members to set group information

`- (BMXErrorCode)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAllowMemberModify:enable:completion:" title="setAllowMemberModify:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setAllowMemberModify:enable:" %}{% endlanying_code_snippet %}
```
### setAllowMemberModify:enable:completion:

Set whether to allow group members to set group information

`- (void)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAvatar:avatarPath:arg3:" title="setAvatar:avatarPath:arg3:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setAllowMemberModify:enable:completion:" %}{% endlanying_code_snippet %}
```
### setAvatar:avatarPath:arg3:

Set group avatar

`- (BMXErrorCode)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

*group*  
    The group

*avatarPath*  
    The local file path of avatar

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAvatar:avatarPath:arg3:completion:" title="setAvatar:avatarPath:arg3:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setAvatar:avatarPath:arg3:" %}{% endlanying_code_snippet %}
```
### setAvatar:avatarPath:arg3:completion:

Set group avatar

`- (void)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*avatarPath*  
    The local file path of avatar

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDescription:description:" title="setDescription:description:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setAvatar:avatarPath:arg3:completion:" %}{% endlanying_code_snippet %}
```
### setDescription:description:

Set group description

`- (BMXErrorCode)setDescription:(BMXGroup *)*group* description:(NSString *)*description*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDescription:description:completion:" title="setDescription:description:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setDescription:description:" %}{% endlanying_code_snippet %}
```
### setDescription:description:completion:

Set group description

`- (void)setDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableReadAck:enable:" title="setEnableReadAck:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setDescription:description:completion:" %}{% endlanying_code_snippet %}
```
### setEnableReadAck:enable:

Set whether to enable the read ACK function of the group

`- (BMXErrorCode)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableReadAck:enable:completion:" title="setEnableReadAck:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setEnableReadAck:enable:" %}{% endlanying_code_snippet %}
```
### setEnableReadAck:enable:completion:

Set whether to enable the read ACK function of the group

`- (void)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:extension:" title="setExtension:extension:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setEnableReadAck:enable:completion:" %}{% endlanying_code_snippet %}
```
### setExtension:extension:

Set group extension information

`- (BMXErrorCode)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension*`

#### Parameters

*group*  
    The group

*extension*  
    Extension information of the group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:extension:completion:" title="setExtension:extension:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setExtension:extension:" %}{% endlanying_code_snippet %}
```
### setExtension:extension:completion:

Set group extension information

`- (void)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*extension*  
    Extension information of the group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setHistoryVisible:enable:" title="setHistoryVisible:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setExtension:extension:completion:" %}{% endlanying_code_snippet %}
```
### setHistoryVisible:enable:

Set whether group members can see group history messages

`- (BMXErrorCode)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setHistoryVisible:enable:completion:" title="setHistoryVisible:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setHistoryVisible:enable:" %}{% endlanying_code_snippet %}
```
### setHistoryVisible:enable:completion:

Set whether group members can see group history messages

`- (void)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setInviteMode:mode:" title="setInviteMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setHistoryVisible:enable:completion:" %}{% endlanying_code_snippet %}
```
### setInviteMode:mode:

Set invitation mode

`- (BMXErrorCode)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode*`

#### Parameters

*group*  
    The group

*mode*  
    Invitation mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setInviteMode:mode:completion:" title="setInviteMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setInviteMode:mode:" %}{% endlanying_code_snippet %}
```
### setInviteMode:mode:completion:

Set invitation mode

`- (void)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*mode*  
    Invitation mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setJoinAuthMode:mode:" title="setJoinAuthMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setInviteMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setJoinAuthMode:mode:

Set authorization mode

`- (BMXErrorCode)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode*`

#### Parameters

*group*  
    The group

*mode*  
    Authorization mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setJoinAuthMode:mode:completion:" title="setJoinAuthMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setJoinAuthMode:mode:" %}{% endlanying_code_snippet %}
```
### setJoinAuthMode:mode:completion:

Set invitation mode

`- (void)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*mode*  
    Authorization mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMsgPushMode:mode:" title="setMsgPushMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setJoinAuthMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setMsgPushMode:mode:

Set message notification mode

`- (BMXErrorCode)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode*`

#### Parameters

*group*  
    The group

*mode*  
    Notification mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMsgPushMode:mode:completion:" title="setMsgPushMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setMsgPushMode:mode:" %}{% endlanying_code_snippet %}
```
### setMsgPushMode:mode:completion:

Set message notification mode

`- (void)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*mode*  
    Notification mode

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMyNickname:nickname:" title="setMyNickname:nickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setMsgPushMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setMyNickname:nickname:

Set my nickname in the group

`- (BMXErrorCode)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname*`

#### Parameters

*group*  
    The group

*nickname*  
    My nickname

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMyNickname:nickname:completion:" title="setMyNickname:nickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setMyNickname:nickname:" %}{% endlanying_code_snippet %}
```
### setMyNickname:nickname:completion:

Set my nickname in the group

`- (void)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*nickname*  
    My nickname

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setName:name:" title="setName:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setMyNickname:nickname:completion:" %}{% endlanying_code_snippet %}
```
### setName:name:

Set group name

`- (BMXErrorCode)setName:(BMXGroup *)*group* name:(NSString *)*name*`

#### Parameters

*group*  
    The group

*name*  
    Group name

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setName:name:completion:" title="setName:name:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setName:name:" %}{% endlanying_code_snippet %}
```
### setName:name:completion:

Set group name

`- (void)setName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*name*  
    Group name

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferOwnerWithGroup:newOwnerId:" title="transferOwnerWithGroup:newOwnerId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="setName:name:completion:" %}{% endlanying_code_snippet %}
```
### transferOwnerWithGroup:newOwnerId:

Transfer the owership of the group

`- (BMXErrorCode)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId*`

#### Parameters

*group*  
    The group

*newOwnerId*  
    New owner User ID  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferOwnerWithGroup:newOwnerId:completion:" title="transferOwnerWithGroup:newOwnerId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="transferOwnerWithGroup:newOwnerId:" %}{% endlanying_code_snippet %}
```
### transferOwnerWithGroup:newOwnerId:completion:

Transfer the owership of the group

`- (void)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*newOwnerId*  
    New owner User ID  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanGroupWithGroup:" title="unbanGroupWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="transferOwnerWithGroup:newOwnerId:completion:" %}{% endlanying_code_snippet %}
```
### unbanGroupWithGroup:

Unban all members in the group

`- (BMXErrorCode)unbanGroupWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanGroupWithGroup:completion:" title="unbanGroupWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unbanGroupWithGroup:" %}{% endlanying_code_snippet %}
```
### unbanGroupWithGroup:completion:

Unban all members in the group

`- (void)unbanGroupWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanMembersWithGroup:members:" title="unbanMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unbanGroupWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### unbanMembersWithGroup:members:

Unban members in the group

`- (BMXErrorCode)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanMembersWithGroup:members:completion:" title="unbanMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unbanMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### unbanMembersWithGroup:members:completion:

Unban members in the group

`- (void)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockMembersWithGroup:members:" title="unblockMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unbanMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### unblockMembersWithGroup:members:

Unblock members in the group

`- (BMXErrorCode)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockMembersWithGroup:members:completion:" title="unblockMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unblockMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### unblockMembersWithGroup:members:completion:

Unblock members in the group

`- (void)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*members*  
    Group members ID list

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:" title="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="unblockMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:

Upload shared file to group

`- (BMXErrorCode)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5*`

#### Parameters

*group*  
    The group

*filePath*  
    Local path of the shared file

*displayName*  
    Display name

*extensionName*  
    Extension name of the shared file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:" title="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:" %}{% endlanying_code_snippet %}
```
### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:

Upload shared file to group

`- (void)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
    The group

*filePath*  
    Local path of the shared file

*displayName*  
    Display name

*extensionName*  
    Extension name of the shared file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupService",function="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:" %}{% endlanying_code_snippet %}
```
