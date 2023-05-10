# BMXGroupService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 群组Service

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

接受入群申请

`- (BMXErrorCode)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

#### Parameters

*group*  
   进行操作的群组  

*applicantId*  
   申请进群的用户id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptApplicationWithGroup:applicantId:completion:" title="acceptApplicationWithGroup:applicantId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="acceptApplicationWithGroup:applicantId:" %}{% endlanying_code_snippet %}
```
### acceptApplicationWithGroup:applicantId:completion:

接受入群申请

`- (void)acceptApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*applicantId*  
   申请进群的用户id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptInvitationWithGroup:inviter:" title="acceptInvitationWithGroup:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="acceptApplicationWithGroup:applicantId:completion:" %}{% endlanying_code_snippet %}
```
### acceptInvitationWithGroup:inviter:

接受入群邀请

`- (BMXErrorCode)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

#### Parameters

*group*  
   进行操作的群组  

*inviter*  
   邀请者id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptInvitationWithGroup:inviter:completion:" title="acceptInvitationWithGroup:inviter:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="acceptInvitationWithGroup:inviter:" %}{% endlanying_code_snippet %}
```
### acceptInvitationWithGroup:inviter:completion:

接受入群邀请

`- (void)acceptInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*inviter*  
   邀请者id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addAdminsWithGroup:admins:message:" title="addAdminsWithGroup:admins:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="acceptInvitationWithGroup:inviter:completion:" %}{% endlanying_code_snippet %}
```
### addAdminsWithGroup:admins:message:

添加管理员

`- (BMXErrorCode)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message*`

#### Parameters

*group*  
   进行操作的群组  

*admins*  
   要添加为管理员的成员id列表  

*message*  
   添加为管理员的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addAdminsWithGroup:admins:message:completion:" title="addAdminsWithGroup:admins:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addAdminsWithGroup:admins:message:" %}{% endlanying_code_snippet %}
```
### addAdminsWithGroup:admins:message:completion:

添加管理员

`- (void)addAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*admins*  
   要添加为管理员的成员id列表  

*message*  
   添加为管理员的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addAdminsWithGroup:admins:message:completion:" %}{% endlanying_code_snippet %}
```
### addDelegate:

添加群组变化监听者

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
   群组变化监听者  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXGroupServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addGroupListener:" title="addGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addGroupListener:

添加群组变化监听者

`- (void)addGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

*listener*  
   群组变化监听者  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addMembersWithGroup:members:message:" title="addMembersWithGroup:members:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addGroupListener:" %}{% endlanying_code_snippet %}
```
### addMembersWithGroup:members:message:

添加群成员

`- (BMXErrorCode)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要添加进群的成员id列表  

*message*  
   添加成员原因信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addMembersWithGroup:members:message:completion:" title="addMembersWithGroup:members:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addMembersWithGroup:members:message:" %}{% endlanying_code_snippet %}
```
### addMembersWithGroup:members:message:completion:

添加群成员

`- (void)addMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要添加进群的成员id列表  

*message*  
   添加成员原因信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banGroupWithGroup:duration:" title="banGroupWithGroup:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addMembersWithGroup:members:message:completion:" %}{% endlanying_code_snippet %}
```
### banGroupWithGroup:duration:

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）

`- (BMXErrorCode)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration*`

#### Parameters

*group*  
   进行操作的群组  

*duration*  
   禁言时长(分钟)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banGroupWithGroup:duration:completion:" title="banGroupWithGroup:duration:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banGroupWithGroup:duration:" %}{% endlanying_code_snippet %}
```
### banGroupWithGroup:duration:completion:

全员禁言，当前服务器时间加上禁言时长后计算出全员禁言到期时间（只有管理和群主可以发言）

`- (void)banGroupWithGroup:(BMXGroup *)*group* duration:(long long)*duration* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*duration*  
   禁言时长(分钟)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banMembersWithGroup:members:duration:" title="banMembersWithGroup:members:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banGroupWithGroup:duration:completion:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration*`

<a name="//api/name/banMembersWithGroup:members:duration:reason:" title="banMembersWithGroup:members:duration:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banMembersWithGroup:members:duration:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:reason:

禁言

`- (BMXErrorCode)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   被禁言的群成员id列表  

*duration*  
   禁言时长  

*reason*  
   禁言原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/banMembersWithGroup:members:duration:reason:completion:" title="banMembersWithGroup:members:duration:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banMembersWithGroup:members:duration:reason:" %}{% endlanying_code_snippet %}
```
### banMembersWithGroup:members:duration:reason:completion:

禁言

`- (void)banMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* duration:(long long)*duration* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   被禁言的群成员id列表  

*duration*  
   禁言时长  

*reason*  
   禁言原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockMembersWithGroup:members:" title="blockMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="banMembersWithGroup:members:duration:reason:completion:" %}{% endlanying_code_snippet %}
```
### blockMembersWithGroup:members:

添加黑名单

`- (BMXErrorCode)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要加入黑名单的群成员id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockMembersWithGroup:members:completion:" title="blockMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="blockMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### blockMembersWithGroup:members:completion:

添加黑名单

`- (void)blockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要加入黑名单的群成员id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadSharedFileWithGroup:sharedFile:" title="cancelDownloadSharedFileWithGroup:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="blockMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### cancelDownloadSharedFileWithGroup:sharedFile:

取消下载群共享文件

`- (BMXErrorCode)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   下载的群共享文件  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadSharedFileWithGroup:sharedFile:completion:" title="cancelDownloadSharedFileWithGroup:sharedFile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelDownloadSharedFileWithGroup:sharedFile:" %}{% endlanying_code_snippet %}
```
### cancelDownloadSharedFileWithGroup:sharedFile:completion:

取消下载群共享文件

`- (void)cancelDownloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   下载的群共享文件  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadSharedFileWithGroup:filePath:" title="cancelUploadSharedFileWithGroup:filePath:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelDownloadSharedFileWithGroup:sharedFile:completion:" %}{% endlanying_code_snippet %}
```
### cancelUploadSharedFileWithGroup:filePath:

取消上传群共享文件

`- (BMXErrorCode)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath*`

#### Parameters

*group*  
   进行操作的群组  

*filePath*  
   文件的本地路径  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadSharedFileWithGroup:filePath:completion:" title="cancelUploadSharedFileWithGroup:filePath:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelUploadSharedFileWithGroup:filePath:" %}{% endlanying_code_snippet %}
```
### cancelUploadSharedFileWithGroup:filePath:completion:

取消上传群共享文件

`- (void)cancelUploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*filePath*  
   文件的本地路径  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeSharedFileNameWithGroup:sharedFile:name:" title="changeSharedFileNameWithGroup:sharedFile:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelUploadSharedFileWithGroup:filePath:completion:" %}{% endlanying_code_snippet %}
```
### changeSharedFileNameWithGroup:sharedFile:name:

修改群共享文件名称

`- (BMXErrorCode)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name*`

#### Parameters

*group*  
   进行操作的群组  

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
{% lanying_code_snippet repo="floo-ios",class="",function="changeSharedFileNameWithGroup:sharedFile:name:" %}{% endlanying_code_snippet %}
```
### changeSharedFileNameWithGroup:sharedFile:name:completion:

修改群共享文件名称

`- (void)changeSharedFileNameWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   进行更改的群共享文件  

*name*  
   修改的群共享文件名称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createWithOptions:completion:" title="createWithOptions:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="changeSharedFileNameWithGroup:sharedFile:name:completion:" %}{% endlanying_code_snippet %}
```
### createWithOptions:completion:

创建群

`- (void)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

*options*  
   创建群组时传入的参数选项  

*group*  
   创建返回的结果，传入指向为空的shared_ptr对象函数执行后从此获取返回结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createWithOptions:group:" title="createWithOptions:group:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createWithOptions:completion:" %}{% endlanying_code_snippet %}
```
### createWithOptions:group:

创建群

`- (BMXErrorCode)createWithOptions:(BMXGroupServiceCreateGroupOptions *)*options* group:(BMXGroup *)*group*`

#### Parameters

*options*  
   创建群组时传入的参数选项  

*group*  
   创建返回的结果，传入指向为空的shared_ptr对象函数执行后从此获取返回结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createWithOptions:group:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/declineApplicationWithGroup:applicantId:" title="declineApplicationWithGroup:applicantId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId*`

<a name="//api/name/declineApplicationWithGroup:applicantId:reason:" title="declineApplicationWithGroup:applicantId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineApplicationWithGroup:applicantId:" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:reason:

拒绝入群申请

`- (BMXErrorCode)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason*`

#### Parameters

*group*  
   进行操作的群组  

*applicantId*  
   申请进群的用户id  

*reason*  
   拒绝的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineApplicationWithGroup:applicantId:reason:completion:" title="declineApplicationWithGroup:applicantId:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineApplicationWithGroup:applicantId:reason:" %}{% endlanying_code_snippet %}
```
### declineApplicationWithGroup:applicantId:reason:completion:

拒绝入群申请

`- (void)declineApplicationWithGroup:(BMXGroup *)*group* applicantId:(long long)*applicantId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*applicantId*  
   申请进群的用户id  

*reason*  
   拒绝的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineInvitationWithGroup:inviter:" title="declineInvitationWithGroup:inviter:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineApplicationWithGroup:applicantId:reason:completion:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter*`

<a name="//api/name/declineInvitationWithGroup:inviter:reason:" title="declineInvitationWithGroup:inviter:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineInvitationWithGroup:inviter:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:reason:

拒绝入群邀请

`- (BMXErrorCode)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason*`

#### Parameters

*group*  
   进行操作的群组  

*inviter*  
   邀请者id  

*reason*  
   拒绝的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineInvitationWithGroup:inviter:reason:completion:" title="declineInvitationWithGroup:inviter:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineInvitationWithGroup:inviter:reason:" %}{% endlanying_code_snippet %}
```
### declineInvitationWithGroup:inviter:reason:completion:

拒绝入群邀请

`- (void)declineInvitationWithGroup:(BMXGroup *)*group* inviter:(long long)*inviter* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*inviter*  
   邀请者id  

*reason*  
   拒绝的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:" title="deleteAnnouncementWithGroup:announcementId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="declineInvitationWithGroup:inviter:reason:completion:" %}{% endlanying_code_snippet %}
```
### deleteAnnouncementWithGroup:announcementId:

删除群公告

`- (BMXErrorCode)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId*`

#### Parameters

*group*  
   进行操作的群组  

*announcementId*  
   删除的群公告id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAnnouncementWithGroup:announcementId:completion:" title="deleteAnnouncementWithGroup:announcementId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteAnnouncementWithGroup:announcementId:" %}{% endlanying_code_snippet %}
```
### deleteAnnouncementWithGroup:announcementId:completion:

删除群公告

`- (void)deleteAnnouncementWithGroup:(BMXGroup *)*group* announcementId:(long long)*announcementId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*announcementId*  
   删除的群公告id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/destroyWithGroup:" title="destroyWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteAnnouncementWithGroup:announcementId:completion:" %}{% endlanying_code_snippet %}
```
### destroyWithGroup:

销毁群

`- (BMXErrorCode)destroyWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
   要销毁的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/destroyWithGroup:completion:" title="destroyWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="destroyWithGroup:" %}{% endlanying_code_snippet %}
```
### destroyWithGroup:completion:

销毁群

`- (void)destroyWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   要销毁的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithGroup:thumbnail:callback:" title="downloadAvatarWithGroup:thumbnail:callback:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="destroyWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithGroup:thumbnail:callback:

下载群头像

`- (BMXErrorCode)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

*group*  
   进行操作的群组  

*thumbnail*  
   设置为true下载缩略图，false下载原图  

*callback*  
   下载回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithGroup:thumbnail:callback:completion:" title="downloadAvatarWithGroup:thumbnail:callback:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAvatarWithGroup:thumbnail:callback:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithGroup:thumbnail:callback:completion:

下载群头像

`- (void)downloadAvatarWithGroup:(BMXGroup *)*group* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*thumbnail*  
   设置为true下载缩略图，false下载原图  

*callback*  
   下载回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadSharedFileWithGroup:sharedFile:arg3:" title="downloadSharedFileWithGroup:sharedFile:arg3:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAvatarWithGroup:thumbnail:callback:completion:" %}{% endlanying_code_snippet %}
```
### downloadSharedFileWithGroup:sharedFile:arg3:

下载群共享文件

`- (BMXErrorCode)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   下载的群共享文件  

*Callback*  
   下载回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadSharedFileWithGroup:sharedFile:arg3:completion:" title="downloadSharedFileWithGroup:sharedFile:arg3:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadSharedFileWithGroup:sharedFile:arg3:" %}{% endlanying_code_snippet %}
```
### downloadSharedFileWithGroup:sharedFile:arg3:completion:

下载群共享文件

`- (void)downloadSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   下载的群共享文件  

*Callback*  
   下载回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/editAnnouncementWithGroup:title:content:" title="editAnnouncementWithGroup:title:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadSharedFileWithGroup:sharedFile:arg3:completion:" %}{% endlanying_code_snippet %}
```
### editAnnouncementWithGroup:title:content:

设置群公告

`- (BMXErrorCode)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content*`

#### Parameters

*group*  
   进行操作的群组  

*title*  
   群公告的标题  

*content*  
   群公告的内容  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/editAnnouncementWithGroup:title:content:completion:" title="editAnnouncementWithGroup:title:content:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="editAnnouncementWithGroup:title:content:" %}{% endlanying_code_snippet %}
```
### editAnnouncementWithGroup:title:content:completion:

设置群公告

`- (void)editAnnouncementWithGroup:(BMXGroup *)*group* title:(NSString *)*title* content:(NSString *)*content* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*title*  
   群公告的标题  

*content*  
   群公告的内容  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupByIdWithGroupId:forceRefresh:completion:" title="fetchGroupByIdWithGroupId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="editAnnouncementWithGroup:title:content:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupByIdWithGroupId:forceRefresh:completion:

通过群组id获取群信息，如果设置了forceRefresh则从服务器拉取

`- (void)fetchGroupByIdWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

#### Parameters

*groupId*  
   要搜索的群组id  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*group*  
   搜索返回的群组信息，传入指向为空的shared_ptr对象函数执行后从此获取返回结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupByIdWithGroupId:group:forceRefresh:" title="fetchGroupByIdWithGroupId:group:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchGroupByIdWithGroupId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupByIdWithGroupId:group:forceRefresh:

通过群组id获取群信息，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)fetchGroupByIdWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*groupId*  
   要搜索的群组id  

*group*  
   搜索返回的群组信息，传入指向为空的shared_ptr对象函数执行后从此获取返回结果  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:" title="fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchGroupByIdWithGroupId:group:forceRefresh:" %}{% endlanying_code_snippet %}
```
### fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:

通过传入群组的id列表获取群组信息列表，如果设置了forceRefresh则从服务器拉取

`- (void)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*groupIdList*  
   群组id列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchGroupsByIdListWithGroupIdList:list:forceRefresh:" title="fetchGroupsByIdListWithGroupIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchGroupsByIdListWithGroupIdList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchGroupsByIdListWithGroupIdList:list:forceRefresh:

通过传入群组的id列表获取群组信息列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)fetchGroupsByIdListWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*groupIdList*  
   群组id列表  

*list*  
   群组详细信息列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchLocalGroupsByName:completion:" title="fetchLocalGroupsByName:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchGroupsByIdListWithGroupIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### fetchLocalGroupsByName:completion:

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

`- (void)fetchLocalGroupsByName:(NSString *)*name* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   查询的群名称关键字  

*list*  
   搜索结果返回的群列表信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchLocalGroupsByNameWithList:name:" title="fetchLocalGroupsByNameWithList:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchLocalGroupsByName:completion:" %}{% endlanying_code_snippet %}
```
### fetchLocalGroupsByNameWithList:name:

通过群名称查询本地群信息，从本地数据库中通过群名称查询获取群组

`- (BMXErrorCode)fetchLocalGroupsByNameWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

#### Parameters

*list*  
   搜索结果返回的群列表信息  

*name*  
   查询的群名称关键字  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/get:completion:" title="get:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fetchLocalGroupsByNameWithList:name:" %}{% endlanying_code_snippet %}
```
### get:completion:

获取群组列表，如果设置了forceRefresh则从服务器拉取

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupList *res , BMXError *aError ))*resBlock*`

#### Parameters

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群组id列表，传入空列表函数返回后从此处获取返回的群组id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/get:forceRefresh:" title="get:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="get:completion:" %}{% endlanying_code_snippet %}
```
### get:forceRefresh:

获取群组列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)get:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*list*  
   群组id列表，传入空列表函数返回后从此处获取返回的群组id列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAdmins:forceRefresh:completion:" title="getAdmins:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="get:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getAdmins:forceRefresh:completion:

获取Admins列表，如果设置了forceRefresh则从服务器拉取

`- (void)getAdmins:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群管理员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAdmins:list:forceRefresh:" title="getAdmins:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAdmins:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getAdmins:list:forceRefresh:

获取Admins列表，如果设置了forceRefresh则从服务器拉取

`- (BMXErrorCode)getAdmins:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群管理员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAnnouncementList:forceRefresh:completion:" title="getAnnouncementList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAdmins:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getAnnouncementList:forceRefresh:completion:

获取群公告列表

`- (void)getAnnouncementList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncementList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群公告列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAnnouncementList:list:forceRefresh:" title="getAnnouncementList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAnnouncementList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getAnnouncementList:list:forceRefresh:

获取群公告列表

`- (BMXErrorCode)getAnnouncementList:(BMXGroup *)*group* list:(BMXGroupAnnouncementList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群公告列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:cursor:pageSize:completion:" title="getApplicationList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAnnouncementList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getApplicationList:cursor:pageSize:completion:

分页获取群组申请列表

`- (void)getApplicationList:(BMXGroupList *)*list* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupApplicationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*list*  
   需要获取群组申请列表信息的群组id列表  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

*result*  
   分页获取的群组申请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:result:" title="getApplicationList:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getApplicationList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result*`

<a name="//api/name/getApplicationList:result:cursor:" title="getApplicationList:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getApplicationList:result:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:cursor:

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getApplicationList:result:cursor:pageSize:" title="getApplicationList:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getApplicationList:result:cursor:" %}{% endlanying_code_snippet %}
```
### getApplicationList:result:cursor:pageSize:

分页获取群组申请列表

`- (BMXErrorCode)getApplicationList:(BMXGroupList *)*list* result:(BMXGroupApplicationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*list*  
   需要获取群组申请列表信息的群组id列表  

*result*  
   分页获取的群组申请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:completion:" title="getBannedMembers:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getApplicationList:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:completion:

获取禁言列表

`- (void)getBannedMembers:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXGroupBannedMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群禁言列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:cursor:pageSize:completion:" title="getBannedMembers:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:completion:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:cursor:pageSize:completion:

分页获取禁言列表

`- (void)getBannedMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupBannedMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

*result*  
   分页获取的禁言列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:list:" title="getBannedMembers:list:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:list:

获取禁言列表

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* list:(BMXGroupBannedMemberList *)*list*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群禁言列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBannedMembers:result:" title="getBannedMembers:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:list:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result*`

<a name="//api/name/getBannedMembers:result:cursor:" title="getBannedMembers:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:result:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:cursor:

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getBannedMembers:result:cursor:pageSize:" title="getBannedMembers:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:result:cursor:" %}{% endlanying_code_snippet %}
```
### getBannedMembers:result:cursor:pageSize:

分页获取禁言列表

`- (BMXErrorCode)getBannedMembers:(BMXGroup *)*group* result:(BMXGroupBannedMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
   进行操作的群组  

*result*  
   分页获取的禁言列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:cursor:pageSize:completion:" title="getBlockList:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBannedMembers:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getBlockList:cursor:pageSize:completion:

分页获取黑名单

`- (void)getBlockList:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

*result*  
   分页获取的黑名单列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:forceRefresh:completion:" title="getBlockList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:forceRefresh:completion:

获取黑名单

`- (void)getBlockList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群黑名单列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:list:forceRefresh:" title="getBlockList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:list:forceRefresh:

获取黑名单

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群黑名单列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:result:" title="getBlockList:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

<a name="//api/name/getBlockList:result:cursor:" title="getBlockList:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:result:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:cursor:

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getBlockList:result:cursor:pageSize:" title="getBlockList:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:result:cursor:" %}{% endlanying_code_snippet %}
```
### getBlockList:result:cursor:pageSize:

分页获取黑名单

`- (BMXErrorCode)getBlockList:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
   进行操作的群组  

*result*  
   分页获取的黑名单列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInfo:" title="getInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getBlockList:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getInfo:

获取群详情，从服务端拉取最新信息

`- (BMXErrorCode)getInfo:(BMXGroup *)*group*`

#### Parameters

*group*  
   要获取群组最新信息的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInfo:completion:" title="getInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInfo:" %}{% endlanying_code_snippet %}
```
### getInfo:completion:

获取群详情，从服务端拉取最新信息

`- (void)getInfo:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   要获取群组最新信息的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInvitationList:" title="getInvitationList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInfo:completion:" %}{% endlanying_code_snippet %}
```
### getInvitationList:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result*`

<a name="//api/name/getInvitationList:cursor:" title="getInvitationList:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInvitationList:" %}{% endlanying_code_snippet %}
```
### getInvitationList:cursor:

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getInvitationList:cursor:pageSize:" title="getInvitationList:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInvitationList:cursor:" %}{% endlanying_code_snippet %}
```
### getInvitationList:cursor:pageSize:

分页获取群组邀请列表

`- (BMXErrorCode)getInvitationList:(BMXGroupInvitationPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*result*  
   分页获取的群组邀请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getInvitationList:pageSize:completion:" title="getInvitationList:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInvitationList:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getInvitationList:pageSize:completion:

分页获取群组邀请列表

`- (void)getInvitationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupInvitationPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

*result*  
   分页获取的群组邀请列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLatestAnnouncement:announcement:forceRefresh:" title="getLatestAnnouncement:announcement:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getInvitationList:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getLatestAnnouncement:announcement:forceRefresh:

获取最新的群公告

`- (BMXErrorCode)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*announcement*  
   最新的群组公告，传入指向为空的shared_ptr对象函数返回后从此处获取最新的群组公告  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getLatestAnnouncement:announcement:forceRefresh:completion:" title="getLatestAnnouncement:announcement:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getLatestAnnouncement:announcement:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getLatestAnnouncement:announcement:forceRefresh:completion:

获取最新的群公告

`- (void)getLatestAnnouncement:(BMXGroup *)*group* announcement:(BMXGroupAnnouncement *)*announcement* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupAnnouncement *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*announcement*  
   最新的群组公告，传入指向为空的shared_ptr对象函数返回后从此处获取最新的群组公告  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:cursor:pageSize:completion:" title="getMembers:cursor:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getLatestAnnouncement:announcement:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:cursor:pageSize:completion:

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.

`- (void)getMembers:(BMXGroup *)*group* cursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXGroupMemberResultPage *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

*result*  
   分页获取的群成员列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:forceRefresh:completion:" title="getMembers:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:cursor:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:forceRefresh:completion:

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

`- (void)getMembers:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群成员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:list:forceRefresh:" title="getMembers:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getMembers:list:forceRefresh:

获取群成员列表，如果设置了forceRefresh则从服务器拉取，最多拉取1000人

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* list:(BMXGroupMemberList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群成员列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembers:result:" title="getMembers:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getMembers:result:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result*`

<a name="//api/name/getMembers:result:cursor:" title="getMembers:result:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:result:" %}{% endlanying_code_snippet %}
```
### getMembers:result:cursor:

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getMembers:result:cursor:pageSize:" title="getMembers:result:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:result:cursor:" %}{% endlanying_code_snippet %}
```
### getMembers:result:cursor:pageSize:

分页获取群成员列表，如果设置了forceRefresh则从服务器拉取，单页最大数量为500.

`- (BMXErrorCode)getMembers:(BMXGroup *)*group* result:(BMXGroupMemberResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*group*  
   进行操作的群组  

*result*  
   分页获取的群成员列表，传入指向为空的shared_ptr对象函数执行后从此处获取结果  

*cursor*  
   分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor  

*pageSize*  
   分页大小  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembersNickname:members:completion:" title="getMembersNickname:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembers:result:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getMembersNickname:members:completion:

获取群组成员详细信息

`- (void)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXGroupMemberList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要获取群组成员信息详情的群成员id  

*list*  
   返回的群成员详细，传入空列表在函数操作后从此处获取群成员详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMembersNickname:members:list:" title="getMembersNickname:members:list:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembersNickname:members:completion:" %}{% endlanying_code_snippet %}
```
### getMembersNickname:members:list:

获取群组成员详细信息

`- (BMXErrorCode)getMembersNickname:(BMXGroup *)*group* members:(ListOfLongLong *)*members* list:(BMXGroupMemberList *)*list*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要获取群组成员信息详情的群成员id  

*list*  
   返回的群成员详细，传入空列表在函数操作后从此处获取群成员详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSharedFilesList:forceRefresh:completion:" title="getSharedFilesList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMembersNickname:members:list:" %}{% endlanying_code_snippet %}
```
### getSharedFilesList:forceRefresh:completion:

获取群共享文件列表

`- (void)getSharedFilesList:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroupSharedFileList *res , BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

*list*  
   群共享文件列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSharedFilesList:list:forceRefresh:" title="getSharedFilesList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getSharedFilesList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### getSharedFilesList:list:forceRefresh:

获取群共享文件列表

`- (BMXErrorCode)getSharedFilesList:(BMXGroup *)*group* list:(BMXGroupSharedFileList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*group*  
   进行操作的群组  

*list*  
   群共享文件列表，传入空列表函数返回后从此处获取返回的群组详细信息列表  

*forceRefresh*  
   设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getSharedFilesList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/joinWithGroup:message:" title="joinWithGroup:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### joinWithGroup:message:

加入一个群，根据群设置可能需要管理员批准

`- (BMXErrorCode)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message*`

#### Parameters

*group*  
   要加入的群组  

*message*  
   申请入群的信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/joinWithGroup:message:completion:" title="joinWithGroup:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="joinWithGroup:message:" %}{% endlanying_code_snippet %}
```
### joinWithGroup:message:completion:

加入一个群，根据群设置可能需要管理员批准

`- (void)joinWithGroup:(BMXGroup *)*group* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   要加入的群组  

*message*  
   申请入群的信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/leaveWithGroup:" title="leaveWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="joinWithGroup:message:completion:" %}{% endlanying_code_snippet %}
```
### leaveWithGroup:

退出群

`- (BMXErrorCode)leaveWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
   要退出的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/leaveWithGroup:completion:" title="leaveWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="leaveWithGroup:" %}{% endlanying_code_snippet %}
```
### leaveWithGroup:completion:

退出群

`- (void)leaveWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   要退出的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteMessageWithGroup:mode:" title="muteMessageWithGroup:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="leaveWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### muteMessageWithGroup:mode:

设置是否屏蔽群消息

`- (BMXErrorCode)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群屏蔽的模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteMessageWithGroup:mode:completion:" title="muteMessageWithGroup:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="muteMessageWithGroup:mode:" %}{% endlanying_code_snippet %}
```
### muteMessageWithGroup:mode:completion:

设置是否屏蔽群消息

`- (void)muteMessageWithGroup:(BMXGroup *)*group* mode:(BMXGroup_MsgMuteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群屏蔽的模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAdminsWithGroup:admins:reason:" title="removeAdminsWithGroup:admins:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="muteMessageWithGroup:mode:completion:" %}{% endlanying_code_snippet %}
```
### removeAdminsWithGroup:admins:reason:

删除管理员

`- (BMXErrorCode)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason*`

#### Parameters

*group*  
   进行操作的群组  

*admins*  
   要从管理员移除的成员id列表  

*reason*  
   要移除管理员的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAdminsWithGroup:admins:reason:completion:" title="removeAdminsWithGroup:admins:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeAdminsWithGroup:admins:reason:" %}{% endlanying_code_snippet %}
```
### removeAdminsWithGroup:admins:reason:completion:

删除管理员

`- (void)removeAdminsWithGroup:(BMXGroup *)*group* admins:(ListOfLongLong *)*admins* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*admins*  
   要从管理员移除的成员id列表  

*reason*  
   要移除管理员的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeAdminsWithGroup:admins:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

移除群组变化监听者

`- (void)removeDelegate:(id<BMXGroupServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
   群组变化监听者  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeGroupListener:" title="removeGroupListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeGroupListener:

移除群组变化监听者

`- (void)removeGroupListener:(id<BMXGroupServiceProtocol>)*listener*`

#### Parameters

*listener*  
   群组变化监听者  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMembersWithGroup:members:reason:" title="removeMembersWithGroup:members:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeGroupListener:" %}{% endlanying_code_snippet %}
```
### removeMembersWithGroup:members:reason:

删除群成员

`- (BMXErrorCode)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要删除的群组成员id列表  

*reason*  
   删除的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMembersWithGroup:members:reason:completion:" title="removeMembersWithGroup:members:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMembersWithGroup:members:reason:" %}{% endlanying_code_snippet %}
```
### removeMembersWithGroup:members:reason:completion:

删除群成员

`- (void)removeMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   要删除的群组成员id列表  

*reason*  
   删除的原因  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeSharedFileWithGroup:sharedFile:" title="removeSharedFileWithGroup:sharedFile:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMembersWithGroup:members:reason:completion:" %}{% endlanying_code_snippet %}
```
### removeSharedFileWithGroup:sharedFile:

移除群共享文件

`- (BMXErrorCode)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   删除的群共享文件  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeSharedFileWithGroup:sharedFile:completion:" title="removeSharedFileWithGroup:sharedFile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeSharedFileWithGroup:sharedFile:" %}{% endlanying_code_snippet %}
```
### removeSharedFileWithGroup:sharedFile:completion:

移除群共享文件

`- (void)removeSharedFileWithGroup:(BMXGroup *)*group* sharedFile:(BMXGroupSharedFile *)*sharedFile* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*sharedFile*  
   删除的群共享文件  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchWithGroupId:forceRefresh:completion:" title="searchWithGroupId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeSharedFileWithGroup:sharedFile:completion:" %}{% endlanying_code_snippet %}
```
### searchWithGroupId:forceRefresh:completion:

`- (void)searchWithGroupId:(long long)*groupId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXGroup *res , BMXError *aError ))*resBlock*`

<a name="//api/name/searchWithGroupId:group:forceRefresh:" title="searchWithGroupId:group:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchWithGroupId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### searchWithGroupId:group:forceRefresh:

`- (BMXErrorCode)searchWithGroupId:(long long)*groupId* group:(BMXGroup *)*group* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithGroupIdList:list:forceRefresh:" title="searchWithGroupIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchWithGroupId:group:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithGroupIdList:list:forceRefresh:

`- (BMXErrorCode)searchWithGroupIdList:(ListOfLongLong *)*groupIdList* list:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithList:forceRefresh:" title="searchWithList:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchWithGroupIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithList:forceRefresh:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/searchWithList:name:" title="searchWithList:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchWithList:forceRefresh:" %}{% endlanying_code_snippet %}
```
### searchWithList:name:

`- (BMXErrorCode)searchWithList:(BMXGroupList *)*list* name:(NSString *)*name*`

<a name="//api/name/setAllowMemberModify:enable:" title="setAllowMemberModify:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchWithList:name:" %}{% endlanying_code_snippet %}
```
### setAllowMemberModify:enable:

设置是否允许群成员设置群信息

`- (BMXErrorCode)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否允许操作  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAllowMemberModify:enable:completion:" title="setAllowMemberModify:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAllowMemberModify:enable:" %}{% endlanying_code_snippet %}
```
### setAllowMemberModify:enable:completion:

设置是否允许群成员设置群信息

`- (void)setAllowMemberModify:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否允许操作  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAvatar:avatarPath:arg3:" title="setAvatar:avatarPath:arg3:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAllowMemberModify:enable:completion:" %}{% endlanying_code_snippet %}
```
### setAvatar:avatarPath:arg3:

设置群头像

`- (BMXErrorCode)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3*`

#### Parameters

*group*  
   进行操作的群组  

*avatarPath*  
   群头像文件的本地路径  

*Callback*  
   上传回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAvatar:avatarPath:arg3:completion:" title="setAvatar:avatarPath:arg3:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAvatar:avatarPath:arg3:" %}{% endlanying_code_snippet %}
```
### setAvatar:avatarPath:arg3:completion:

设置群头像

`- (void)setAvatar:(BMXGroup *)*group* avatarPath:(NSString *)*avatarPath* arg3:(void ( ^ ) ( int progress ))*arg3* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*avatarPath*  
   群头像文件的本地路径  

*Callback*  
   上传回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDescription:description:" title="setDescription:description:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAvatar:avatarPath:arg3:completion:" %}{% endlanying_code_snippet %}
```
### setDescription:description:

设置群描述信息

`- (BMXErrorCode)setDescription:(BMXGroup *)*group* description:(NSString *)*description*`

#### Parameters

*group*  
   进行操作的群组  

*description*  
   群组描述  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDescription:description:completion:" title="setDescription:description:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setDescription:description:" %}{% endlanying_code_snippet %}
```
### setDescription:description:completion:

设置群描述信息

`- (void)setDescription:(BMXGroup *)*group* description:(NSString *)*description* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*description*  
   群组描述  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableReadAck:enable:" title="setEnableReadAck:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setDescription:description:completion:" %}{% endlanying_code_snippet %}
```
### setEnableReadAck:enable:

设置是否开启群消息已读功能

`- (BMXErrorCode)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnableReadAck:enable:completion:" title="setEnableReadAck:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setEnableReadAck:enable:" %}{% endlanying_code_snippet %}
```
### setEnableReadAck:enable:completion:

设置是否开启群消息已读功能

`- (void)setEnableReadAck:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:extension:" title="setExtension:extension:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setEnableReadAck:enable:completion:" %}{% endlanying_code_snippet %}
```
### setExtension:extension:

设置群扩展信息

`- (BMXErrorCode)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension*`

#### Parameters

*group*  
   进行操作的群组  

*extension*  
   群组的扩展信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:extension:completion:" title="setExtension:extension:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setExtension:extension:" %}{% endlanying_code_snippet %}
```
### setExtension:extension:completion:

设置群扩展信息

`- (void)setExtension:(BMXGroup *)*group* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*extension*  
   群组的扩展信息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setHistoryVisible:enable:" title="setHistoryVisible:enable:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setExtension:extension:completion:" %}{% endlanying_code_snippet %}
```
### setHistoryVisible:enable:

设置群成员是否开可见群历史聊天记录

`- (BMXErrorCode)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setHistoryVisible:enable:completion:" title="setHistoryVisible:enable:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setHistoryVisible:enable:" %}{% endlanying_code_snippet %}
```
### setHistoryVisible:enable:completion:

设置群成员是否开可见群历史聊天记录

`- (void)setHistoryVisible:(BMXGroup *)*group* enable:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*enable*  
   是否开启  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setInviteMode:mode:" title="setInviteMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setHistoryVisible:enable:completion:" %}{% endlanying_code_snippet %}
```
### setInviteMode:mode:

设置邀请模式

`- (BMXErrorCode)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群组的邀请模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setInviteMode:mode:completion:" title="setInviteMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setInviteMode:mode:" %}{% endlanying_code_snippet %}
```
### setInviteMode:mode:completion:

设置邀请模式

`- (void)setInviteMode:(BMXGroup *)*group* mode:(BMXGroup_InviteMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群组的邀请模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setJoinAuthMode:mode:" title="setJoinAuthMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setInviteMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setJoinAuthMode:mode:

设置入群审批模式

`- (BMXErrorCode)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   入群审批模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setJoinAuthMode:mode:completion:" title="setJoinAuthMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setJoinAuthMode:mode:" %}{% endlanying_code_snippet %}
```
### setJoinAuthMode:mode:completion:

设置入群审批模式

`- (void)setJoinAuthMode:(BMXGroup *)*group* mode:(BMXGroup_JoinAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   入群审批模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMsgPushMode:mode:" title="setMsgPushMode:mode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setJoinAuthMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setMsgPushMode:mode:

设置群消息通知模式

`- (BMXErrorCode)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群消息通知模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMsgPushMode:mode:completion:" title="setMsgPushMode:mode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMsgPushMode:mode:" %}{% endlanying_code_snippet %}
```
### setMsgPushMode:mode:completion:

设置群消息通知模式

`- (void)setMsgPushMode:(BMXGroup *)*group* mode:(BMXGroup_MsgPushMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*mode*  
   群消息通知模式  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMyNickname:nickname:" title="setMyNickname:nickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMsgPushMode:mode:completion:" %}{% endlanying_code_snippet %}
```
### setMyNickname:nickname:

设置在群里的昵称

`- (BMXErrorCode)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname*`

#### Parameters

*group*  
   进行操作的群组  

*nickname*  
   用户在群组内的昵称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMyNickname:nickname:completion:" title="setMyNickname:nickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMyNickname:nickname:" %}{% endlanying_code_snippet %}
```
### setMyNickname:nickname:completion:

设置在群里的昵称

`- (void)setMyNickname:(BMXGroup *)*group* nickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*nickname*  
   用户在群组内的昵称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setName:name:" title="setName:name:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMyNickname:nickname:completion:" %}{% endlanying_code_snippet %}
```
### setName:name:

设置群名称

`- (BMXErrorCode)setName:(BMXGroup *)*group* name:(NSString *)*name*`

#### Parameters

*group*  
   进行操作的群组  

*name*  
   群组名称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setName:name:completion:" title="setName:name:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setName:name:" %}{% endlanying_code_snippet %}
```
### setName:name:completion:

设置群名称

`- (void)setName:(BMXGroup *)*group* name:(NSString *)*name* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*name*  
   群组名称  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferOwnerWithGroup:newOwnerId:" title="transferOwnerWithGroup:newOwnerId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setName:name:completion:" %}{% endlanying_code_snippet %}
```
### transferOwnerWithGroup:newOwnerId:

转移群主

`- (BMXErrorCode)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId*`

#### Parameters

*group*  
   进行操作的群组  

*newOwnerId*  
   转让为新群主的用户id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferOwnerWithGroup:newOwnerId:completion:" title="transferOwnerWithGroup:newOwnerId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="transferOwnerWithGroup:newOwnerId:" %}{% endlanying_code_snippet %}
```
### transferOwnerWithGroup:newOwnerId:completion:

转移群主

`- (void)transferOwnerWithGroup:(BMXGroup *)*group* newOwnerId:(long long)*newOwnerId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*newOwnerId*  
   转让为新群主的用户id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanGroupWithGroup:" title="unbanGroupWithGroup:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="transferOwnerWithGroup:newOwnerId:completion:" %}{% endlanying_code_snippet %}
```
### unbanGroupWithGroup:

全员解除禁言

`- (BMXErrorCode)unbanGroupWithGroup:(BMXGroup *)*group*`

#### Parameters

*group*  
   进行操作的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanGroupWithGroup:completion:" title="unbanGroupWithGroup:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unbanGroupWithGroup:" %}{% endlanying_code_snippet %}
```
### unbanGroupWithGroup:completion:

全员解除禁言

`- (void)unbanGroupWithGroup:(BMXGroup *)*group* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanMembersWithGroup:members:" title="unbanMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unbanGroupWithGroup:completion:" %}{% endlanying_code_snippet %}
```
### unbanMembersWithGroup:members:

解除禁言

`- (BMXErrorCode)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   被解除禁言的群成员id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbanMembersWithGroup:members:completion:" title="unbanMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unbanMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### unbanMembersWithGroup:members:completion:

解除禁言

`- (void)unbanMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   被解除禁言的群成员id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockMembersWithGroup:members:" title="unblockMembersWithGroup:members:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unbanMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### unblockMembersWithGroup:members:

从黑名单删除

`- (BMXErrorCode)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   从黑名单移除的用户id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockMembersWithGroup:members:completion:" title="unblockMembersWithGroup:members:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unblockMembersWithGroup:members:" %}{% endlanying_code_snippet %}
```
### unblockMembersWithGroup:members:completion:

从黑名单删除

`- (void)unblockMembersWithGroup:(BMXGroup *)*group* members:(ListOfLongLong *)*members* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*members*  
   从黑名单移除的用户id列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:" title="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unblockMembersWithGroup:members:completion:" %}{% endlanying_code_snippet %}
```
### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:

添加群共享文件

`- (BMXErrorCode)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5*`

#### Parameters

*group*  
   进行操作的群组  

*filePath*  
   文件的本地路径  

*displayName*  
   文件的展示名  

*extensionName*  
   文件的扩展名  

*Callback*  
   上传回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:" title="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:" %}{% endlanying_code_snippet %}
```
### uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:

添加群共享文件

`- (void)uploadSharedFileWithGroup:(BMXGroup *)*group* filePath:(NSString *)*filePath* displayName:(NSString *)*displayName* extensionName:(NSString *)*extensionName* arg5:(void ( ^ ) ( int progress ))*arg5* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*group*  
   进行操作的群组  

*filePath*  
   文件的本地路径  

*displayName*  
   文件的展示名  

*extensionName*  
   文件的扩展名  

*Callback*  
   上传回调函数  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="uploadSharedFileWithGroup:filePath:displayName:extensionName:arg5:completion:" %}{% endlanying_code_snippet %}
```
