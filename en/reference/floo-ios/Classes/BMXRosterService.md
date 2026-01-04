# BMXRosterService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Roster Service

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/acceptWithRosterId:" title="acceptWithRosterId:"></a>
### acceptWithRosterId:

Accept a friend request

`- (BMXErrorCode)acceptWithRosterId:(long long)*rosterId*`

#### Parameters

*rosterId*  
    Friend user ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/acceptWithRosterId:completion:" title="acceptWithRosterId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="acceptWithRosterId:" %}{% endlanying_code_snippet %}
```
### acceptWithRosterId:completion:

Accept a friend request

`- (void)acceptWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    Friend user ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="acceptWithRosterId:completion:" %}{% endlanying_code_snippet %}
```
### addDelegate:

Add a roster sevice listener

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addRosterListener:" title="addRosterListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addRosterListener:

Add a roster sevice listener

`- (void)addRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/applyWithRosterId:message:" title="applyWithRosterId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="addRosterListener:" %}{% endlanying_code_snippet %}
```
### applyWithRosterId:message:

`- (BMXErrorCode)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message*`

<a name="//api/name/applyWithRosterId:message:authAnswer:" title="applyWithRosterId:message:authAnswer:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="applyWithRosterId:message:" %}{% endlanying_code_snippet %}
```
### applyWithRosterId:message:authAnswer:

Apply to add a friend

`- (BMXErrorCode)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer*`

#### Parameters

*rosterId*  
    Friend user ID

*message*  
    The message attached

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/applyWithRosterId:message:authAnswer:completion:" title="applyWithRosterId:message:authAnswer:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="applyWithRosterId:message:authAnswer:" %}{% endlanying_code_snippet %}
```
### applyWithRosterId:message:authAnswer:completion:

Apply to add a friend

`- (void)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    Friend user ID

*message*  
    The message attached

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/applyWithRosterId:message:completion:" title="applyWithRosterId:message:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="applyWithRosterId:message:authAnswer:completion:" %}{% endlanying_code_snippet %}
```
### applyWithRosterId:message:completion:

`- (void)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

<a name="//api/name/blockWithRosterId:" title="blockWithRosterId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="applyWithRosterId:message:completion:" %}{% endlanying_code_snippet %}
```
### blockWithRosterId:

Block a user

`- (BMXErrorCode)blockWithRosterId:(long long)*rosterId*`

#### Parameters

*rosterId*  
    User ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/blockWithRosterId:completion:" title="blockWithRosterId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="blockWithRosterId:" %}{% endlanying_code_snippet %}
```
### blockWithRosterId:completion:

Block a user

`- (void)blockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    User ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="blockWithRosterId:completion:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/declineWithRosterId:reason:" title="declineWithRosterId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="dealloc" %}{% endlanying_code_snippet %}
```
### declineWithRosterId:reason:

Decline a friend request

`- (BMXErrorCode)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason*`

#### Parameters

*rosterId*  
    User ID

*reason*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/declineWithRosterId:reason:completion:" title="declineWithRosterId:reason:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="declineWithRosterId:reason:" %}{% endlanying_code_snippet %}
```
### declineWithRosterId:reason:completion:

Decline a friend request

`- (void)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    User ID

*reason*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithItem:thumbnail:callback:" title="downloadAvatarWithItem:thumbnail:callback:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="declineWithRosterId:reason:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithItem:thumbnail:callback:

Download friend's avatar

`- (BMXErrorCode)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

*item*  
    Roster item

*thumbnail*  
    Is it a thumbnail

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithItem:thumbnail:callback:completion:" title="downloadAvatarWithItem:thumbnail:callback:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="downloadAvatarWithItem:thumbnail:callback:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithItem:thumbnail:callback:completion:

Download friend's avatar

`- (void)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*item*  
    Roster item

*thumbnail*  
    Is it a thumbnail

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRosterByIdWithRosterId:forceRefresh:completion:" title="fetchRosterByIdWithRosterId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="downloadAvatarWithItem:thumbnail:callback:completion:" %}{% endlanying_code_snippet %}
```
### fetchRosterByIdWithRosterId:forceRefresh:completion:

Get a roster item

`- (void)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    User ID

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRosterByIdWithRosterId:forceRefresh:item:" title="fetchRosterByIdWithRosterId:forceRefresh:item:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRosterByIdWithRosterId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchRosterByIdWithRosterId:forceRefresh:item:

Get a roster item

`- (BMXErrorCode)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

*rosterId*  
    User ID

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRosterByNameWithName:forceRefresh:completion:" title="fetchRosterByNameWithName:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRosterByIdWithRosterId:forceRefresh:item:" %}{% endlanying_code_snippet %}
```
### fetchRosterByNameWithName:forceRefresh:completion:

Get a roster item

`- (void)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

*name*  
    Username

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRosterByNameWithName:forceRefresh:item:" title="fetchRosterByNameWithName:forceRefresh:item:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRosterByNameWithName:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchRosterByNameWithName:forceRefresh:item:

Get a roster item

`- (BMXErrorCode)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

*name*  
    Username

*forceRefresh*  
    From server
    
#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRostersByIdListWithRosterIdList:forceRefresh:completion:" title="fetchRostersByIdListWithRosterIdList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRosterByNameWithName:forceRefresh:item:" %}{% endlanying_code_snippet %}
```
### fetchRostersByIdListWithRosterIdList:forceRefresh:completion:

Get roster items

`- (void)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItemList *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterIdList*  
    User ID list of roster items

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fetchRostersByIdListWithRosterIdList:list:forceRefresh:" title="fetchRostersByIdListWithRosterIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRostersByIdListWithRosterIdList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### fetchRostersByIdListWithRosterIdList:list:forceRefresh:

Get roster items

`- (BMXErrorCode)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* list:(BMXRosterItemList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*rosterIdList*  
    User ID list of roster items

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/get:completion:" title="get:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="fetchRostersByIdListWithRosterIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### get:completion:

Get all roster items

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="get:completion:" %}{% endlanying_code_snippet %}
```
### get:forceRefresh:

Get all roster items

`- (BMXErrorCode)get:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:completion:" title="getApplicationList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="get:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getApplicationList:completion:

`- (void)getApplicationList:(NSString *)*cursor* completion:(void ( ^ ) ( BMXRosterApplicationResultPage *res , BMXError *error ))*aCompletionBlock*`

<a name="//api/name/getApplicationList:cursor:" title="getApplicationList:cursor:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getApplicationList:completion:" %}{% endlanying_code_snippet %}
```
### getApplicationList:cursor:

`- (BMXErrorCode)getApplicationList:(BMXRosterApplicationResultPage *)*result* cursor:(NSString *)*cursor*`

<a name="//api/name/getApplicationList:cursor:pageSize:" title="getApplicationList:cursor:pageSize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getApplicationList:cursor:" %}{% endlanying_code_snippet %}
```
### getApplicationList:cursor:pageSize:

Get friend request list

`- (BMXErrorCode)getApplicationList:(BMXRosterApplicationResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

*cursor*  

*pageSize*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getApplicationList:pageSize:completion:" title="getApplicationList:pageSize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getApplicationList:cursor:pageSize:" %}{% endlanying_code_snippet %}
```
### getApplicationList:pageSize:completion:

Get friend request list

`- (void)getApplicationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXRosterApplicationResultPage *res , BMXError *error ))*aCompletionBlock*`

#### Parameters

*cursor*  

*pageSize*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:completion:" title="getBlockList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getApplicationList:pageSize:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:completion:

Get the ID list of user blocked

`- (void)getBlockList:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBlockList:forceRefresh:" title="getBlockList:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getBlockList:completion:" %}{% endlanying_code_snippet %}
```
### getBlockList:forceRefresh:

Get the ID list of user blocked

`- (BMXErrorCode)getBlockList:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="getBlockList:forceRefresh:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

Remove a roster sevice listener

`- (void)removeDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeRosterListener:" title="removeRosterListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeRosterListener:

Remove a roster sevice listener

`- (void)removeRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeWithRosterId:" title="removeWithRosterId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="removeRosterListener:" %}{% endlanying_code_snippet %}
```
### removeWithRosterId:

Remove a roster item

`- (BMXErrorCode)removeWithRosterId:(long long)*rosterId*`

#### Parameters

*rosterId*  
    User ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeWithRosterId:completion:" title="removeWithRosterId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="removeWithRosterId:" %}{% endlanying_code_snippet %}
```
### removeWithRosterId:completion:

Remove a roster item

`- (void)removeWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    User ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchWithName:forceRefresh:completion:" title="searchWithName:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="removeWithRosterId:completion:" %}{% endlanying_code_snippet %}
```
### searchWithName:forceRefresh:completion:

`- (void)searchWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

<a name="//api/name/searchWithName:forceRefresh:item:" title="searchWithName:forceRefresh:item:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithName:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### searchWithName:forceRefresh:item:

`- (BMXErrorCode)searchWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

<a name="//api/name/searchWithRosterId:forceRefresh:completion:" title="searchWithRosterId:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithName:forceRefresh:item:" %}{% endlanying_code_snippet %}
```
### searchWithRosterId:forceRefresh:completion:

Search a roster item

`- (void)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
    User ID

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Discussion
Deprecated. use fetchRosterById instead.

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchWithRosterId:forceRefresh:item:" title="searchWithRosterId:forceRefresh:item:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithRosterId:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### searchWithRosterId:forceRefresh:item:

Search a roster item

`- (BMXErrorCode)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

*rosterId*  
    User ID

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Discussion
Deprecated. use fetchRosterById instead.

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchWithRosterIdList:forceRefresh:completion:" title="searchWithRosterIdList:forceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithRosterId:forceRefresh:item:" %}{% endlanying_code_snippet %}
```
### searchWithRosterIdList:forceRefresh:completion:

`- (void)searchWithRosterIdList:(ListOfLongLong *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItemList *list , BMXError *error ))*aCompletionBlock*`

<a name="//api/name/searchWithRosterIdList:list:forceRefresh:" title="searchWithRosterIdList:list:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithRosterIdList:forceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### searchWithRosterIdList:list:forceRefresh:

`- (BMXErrorCode)searchWithRosterIdList:(ListOfLongLong *)*rosterIdList* list:(BMXRosterItemList *)*list* forceRefresh:(BOOL)*forceRefresh*`

<a name="//api/name/setItemAlias:alias:" title="setItemAlias:alias:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="searchWithRosterIdList:list:forceRefresh:" %}{% endlanying_code_snippet %}
```
### setItemAlias:alias:

Set friend’s alias

`- (BMXErrorCode)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias*`

#### Parameters

*item*  

*alias*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemAlias:alias:completion:" title="setItemAlias:alias:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemAlias:alias:" %}{% endlanying_code_snippet %}
```
### setItemAlias:alias:completion:

Set friend’s alias

`- (void)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*item*  

*alias*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemExtension:extension:" title="setItemExtension:extension:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemAlias:alias:completion:" %}{% endlanying_code_snippet %}
```
### setItemExtension:extension:

Set extension information for the roster item(on server)

`- (BMXErrorCode)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

*item*  

*extension*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemExtension:extension:completion:" title="setItemExtension:extension:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemExtension:extension:" %}{% endlanying_code_snippet %}
```
### setItemExtension:extension:completion:

Set extension information for the roster item(on server)

`- (void)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*item*  

*extension*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemLocalExtension:extension:" title="setItemLocalExtension:extension:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemExtension:extension:completion:" %}{% endlanying_code_snippet %}
```
### setItemLocalExtension:extension:

Set extension information for the roster item(on local db)

`- (BMXErrorCode)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

*item*  

*extension*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemLocalExtension:extension:completion:" title="setItemLocalExtension:extension:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemLocalExtension:extension:" %}{% endlanying_code_snippet %}
```
### setItemLocalExtension:extension:completion:

Set extension information for the roster item(on local db)

`- (void)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*item*  

*extension*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemMuteNotification:status:" title="setItemMuteNotification:status:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemLocalExtension:extension:completion:" %}{% endlanying_code_snippet %}
```
### setItemMuteNotification:status:

Set whether to mute user messages notification

`- (BMXErrorCode)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status*`

#### Parameters

*item*  

*status*  
    true for mute

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setItemMuteNotification:status:completion:" title="setItemMuteNotification:status:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemMuteNotification:status:" %}{% endlanying_code_snippet %}
```
### setItemMuteNotification:status:completion:

Set whether to mute user messages notification

`- (void)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*item*  

*status*  
    true for mute

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockWithRosterId:" title="unblockWithRosterId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="setItemMuteNotification:status:completion:" %}{% endlanying_code_snippet %}
```
### unblockWithRosterId:

Unblock a roster item

`- (BMXErrorCode)unblockWithRosterId:(long long)*rosterId*`

#### Parameters

*rosterId*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unblockWithRosterId:completion:" title="unblockWithRosterId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="unblockWithRosterId:" %}{% endlanying_code_snippet %}
```
### unblockWithRosterId:completion:

Unblock a roster item

`- (void)unblockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterService",function="unblockWithRosterId:completion:" %}{% endlanying_code_snippet %}
```
