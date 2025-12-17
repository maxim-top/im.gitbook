# BMXRosterService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 好友Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### acceptWithRosterId:

接受加好友申请

`- (BMXErrorCode)acceptWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
申请加为好友的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### acceptWithRosterId:completion:

接受加好友申请

`- (void)acceptWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
申请加为好友的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### addDelegate:

添加好友变化监听者

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
好友变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### addRosterListener:

添加好友变化监听者

`- (void)addRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

_listener_\
好友变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### applyWithRosterId:message:

`- (BMXErrorCode)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### applyWithRosterId:message:authAnswer:

申请添加好友

`- (BMXErrorCode)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer*`

#### Parameters

_rosterId_\
申请添加的用户id

_message_\
好友申请信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### applyWithRosterId:message:authAnswer:completion:

申请添加好友

`- (void)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
申请添加的用户id

_message_\
好友申请信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### applyWithRosterId:message:completion:

`- (void)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### blockWithRosterId:

加入黑名单

`- (BMXErrorCode)blockWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
加入黑名单的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### blockWithRosterId:completion:

加入黑名单

`- (void)blockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
加入黑名单的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### declineWithRosterId:reason:

拒绝加好友申请

`- (BMXErrorCode)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason*`

#### Parameters

_rosterId_\
申请加为好友的用户id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### declineWithRosterId:reason:completion:

拒绝加好友申请

`- (void)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
申请加为好友的用户id

_reason_\
拒绝的原因

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### downloadAvatarWithItem:thumbnail:callback:

下载头像

`- (BMXErrorCode)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_item_\
用户信息

_thumbnail_\
是否下载缩略图，ture为缩略图，false为原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### downloadAvatarWithItem:thumbnail:callback:completion:

下载头像

`- (void)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
用户信息

_thumbnail_\
是否下载缩略图，ture为缩略图，false为原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByIdWithRosterId:forceRefresh:completion:

通过联系人id搜索用户

`- (void)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
搜索的好友id

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByIdWithRosterId:forceRefresh:item:

通过联系人id搜索用户

`- (BMXErrorCode)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_rosterId_\
搜索的好友id

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByNameWithName:forceRefresh:completion:

通过用户名搜索用户

`- (void)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_name_\
搜索的用户名

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByNameWithName:forceRefresh:item:

通过用户名搜索用户

`- (BMXErrorCode)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_name_\
搜索的用户名

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRostersByIdListWithRosterIdList:forceRefresh:completion:

通过联系人id列表批量搜索用户

`- (void)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItemList *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterIdList_\
需要搜索的用户id列表

_forceRefresh_\
是否强制从服务器获取，为true则强制从服务器获取

_list_\
返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRostersByIdListWithRosterIdList:list:forceRefresh:

通过联系人id列表批量搜索用户

`- (BMXErrorCode)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* list:(BMXRosterItemList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_rosterIdList_\
需要搜索的用户id列表

_list_\
返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表

_forceRefresh_\
是否强制从服务器获取，为true则强制从服务器获取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### get:completion:

获取好友列表，如果forceRefresh == true，则强制从服务端拉取

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_forceRefresh_\
是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

_list_\
好友id列表，传入空列表函数返回后从此处获取返回的好友id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### get:forceRefresh:

获取好友列表，如果forceRefresh == true，则强制从服务端拉取

`- (BMXErrorCode)get:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_list_\
好友id列表，传入空列表函数返回后从此处获取返回的好友id列表

_forceRefresh_\
是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getApplicationList:completion:

`- (void)getApplicationList:(NSString *)*cursor* completion:(void ( ^ ) ( BMXRosterApplicationResultPage *res , BMXError *error ))*aCompletionBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getApplicationList:cursor:

`- (BMXErrorCode)getApplicationList:(BMXRosterApplicationResultPage *)*result* cursor:(NSString *)*cursor*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getApplicationList:cursor:pageSize:

获取申请添加好友列表

`- (BMXErrorCode)getApplicationList:(BMXRosterApplicationResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_result_\
返回的申请好友列表信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getApplicationList:pageSize:completion:

获取申请添加好友列表

`- (void)getApplicationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXRosterApplicationResultPage *res , BMXError *error ))*aCompletionBlock*`

#### Parameters

_cursor_\
分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor

_pageSize_\
分页大小

_result_\
返回的申请好友列表信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getBlockList:completion:

获取黑名单，如果forceRefresh == true，则强制从服务端拉取

`- (void)getBlockList:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_forceRefresh_\
是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

_list_\
好友id列表，传入空列表函数返回后从此处获取返回的黑名单id列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getBlockList:forceRefresh:

获取黑名单，如果forceRefresh == true，则强制从服务端拉取

`- (BMXErrorCode)getBlockList:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_list_\
好友id列表，传入空列表函数返回后从此处获取返回的黑名单id列表

_forceRefresh_\
是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeDelegate:

移除好友变化监听者

`- (void)removeDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
好友变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeRosterListener:

移除好友变化监听者

`- (void)removeRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

_listener_\
好友变化监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeWithRosterId:

删除好友

`- (BMXErrorCode)removeWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
删除的好友id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeWithRosterId:completion:

删除好友

`- (void)removeWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
删除的好友id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithName:forceRefresh:completion:

`- (void)searchWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithName:forceRefresh:item:

`- (BMXErrorCode)searchWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithRosterId:forceRefresh:completion:

搜索用户

`- (void)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
搜索的好友id

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

Deprecated. use fetchRosterById instead.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithRosterId:forceRefresh:item:

搜索用户

`- (BMXErrorCode)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_rosterId_\
搜索的好友id

_forceRefresh_\
为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。

_item_\
查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

Deprecated. use fetchRosterById instead.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithRosterIdList:forceRefresh:completion:

`- (void)searchWithRosterIdList:(ListOfLongLong *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItemList *list , BMXError *error ))*aCompletionBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### searchWithRosterIdList:list:forceRefresh:

`- (BMXErrorCode)searchWithRosterIdList:(ListOfLongLong *)*rosterIdList* list:(BMXRosterItemList *)*list* forceRefresh:(BOOL)*forceRefresh*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemAlias:alias:

更新好友别名

`- (BMXErrorCode)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias*`

#### Parameters

_item_\
用户信息

_alias_\
好友别名

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemAlias:alias:completion:

更新好友别名

`- (void)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
用户信息

_alias_\
好友别名

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemExtension:extension:

更新好友服务器扩展信息

`- (BMXErrorCode)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

_item_\
用户信息

_extension_\
服务器扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemExtension:extension:completion:

更新好友服务器扩展信息

`- (void)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
用户信息

_extension_\
服务器扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemLocalExtension:extension:

更新好友本地扩展信息

`- (BMXErrorCode)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

_item_\
用户信息

_extension_\
本地扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemLocalExtension:extension:completion:

更新好友本地扩展信息

`- (void)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
用户信息

_extension_\
本地扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemMuteNotification:status:

设置是否拒收用户消息

`- (BMXErrorCode)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status*`

#### Parameters

_item_\
用户信息

_status_\
是否拒收用户消息，true拒收，false不拒收

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemMuteNotification:status:completion:

设置是否拒收用户消息

`- (void)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
用户信息

_status_\
是否拒收用户消息，true拒收，false不拒收

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### unblockWithRosterId:

从黑名单移除

`- (BMXErrorCode)unblockWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
从黑名单移除的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### unblockWithRosterId:completion:

从黑名单移除

`- (void)unblockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
从黑名单移除的用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>
```
