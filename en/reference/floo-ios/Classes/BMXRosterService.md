# BMXRosterService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Roster Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### acceptWithRosterId:

Accept a friend request

`- (BMXErrorCode)acceptWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
Friend user ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### acceptWithRosterId:completion:

Accept a friend request

`- (void)acceptWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
Friend user ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### addDelegate:

Add a roster sevice listener

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

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

Add a roster sevice listener

`- (void)addRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

_listener_

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

Apply to add a friend

`- (BMXErrorCode)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer*`

#### Parameters

_rosterId_\
Friend user ID

_message_\
The message attached

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### applyWithRosterId:message:authAnswer:completion:

Apply to add a friend

`- (void)applyWithRosterId:(long long)*rosterId* message:(NSString *)*message* authAnswer:(NSString *)*authAnswer* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
Friend user ID

_message_\
The message attached

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

Block a user

`- (BMXErrorCode)blockWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
User ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### blockWithRosterId:completion:

Block a user

`- (void)blockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
User ID

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

Decline a friend request

`- (BMXErrorCode)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason*`

#### Parameters

_rosterId_\
User ID

_reason_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### declineWithRosterId:reason:completion:

Decline a friend request

`- (void)declineWithRosterId:(long long)*rosterId* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
User ID

_reason_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### downloadAvatarWithItem:thumbnail:callback:

Download friend's avatar

`- (BMXErrorCode)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_item_\
Roster item

_thumbnail_\
Is it a thumbnail

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### downloadAvatarWithItem:thumbnail:callback:completion:

Download friend's avatar

`- (void)downloadAvatarWithItem:(BMXRosterItem *)*item* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_\
Roster item

_thumbnail_\
Is it a thumbnail

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByIdWithRosterId:forceRefresh:completion:

Get a roster item

`- (void)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
User ID

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByIdWithRosterId:forceRefresh:item:

Get a roster item

`- (BMXErrorCode)fetchRosterByIdWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_rosterId_\
User ID

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByNameWithName:forceRefresh:completion:

Get a roster item

`- (void)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_name_\
Username

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRosterByNameWithName:forceRefresh:item:

Get a roster item

`- (BMXErrorCode)fetchRosterByNameWithName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_name_\
Username

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRostersByIdListWithRosterIdList:forceRefresh:completion:

Get roster items

`- (void)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItemList *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterIdList_\
User ID list of roster items

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### fetchRostersByIdListWithRosterIdList:list:forceRefresh:

Get roster items

`- (BMXErrorCode)fetchRostersByIdListWithRosterIdList:(ListOfLongLong *)*rosterIdList* list:(BMXRosterItemList *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_rosterIdList_\
User ID list of roster items

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### get:completion:

Get all roster items

`- (void)get:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### get:forceRefresh:

Get all roster items

`- (BMXErrorCode)get:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_forceRefresh_\
From server

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

Get friend request list

`- (BMXErrorCode)getApplicationList:(BMXRosterApplicationResultPage *)*result* cursor:(NSString *)*cursor* pageSize:(int)*pageSize*`

#### Parameters

_cursor_

_pageSize_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getApplicationList:pageSize:completion:

Get friend request list

`- (void)getApplicationList:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( BMXRosterApplicationResultPage *res , BMXError *error ))*aCompletionBlock*`

#### Parameters

_cursor_

_pageSize_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getBlockList:completion:

Get the ID list of user blocked

`- (void)getBlockList:(BOOL)*forceRefresh* completion:(void ( ^ ) ( ListOfLongLong *list , BMXError *error ))*aCompletionBlock*`

#### Parameters

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### getBlockList:forceRefresh:

Get the ID list of user blocked

`- (BMXErrorCode)getBlockList:(ListOfLongLong *)*list* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_forceRefresh_\
From server

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

Remove a roster sevice listener

`- (void)removeDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeRosterListener:

Remove a roster sevice listener

`- (void)removeRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeWithRosterId:

Remove a roster item

`- (BMXErrorCode)removeWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_\
User ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### removeWithRosterId:completion:

Remove a roster item

`- (void)removeWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
User ID

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

Search a roster item

`- (void)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRosterItem *item , BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_\
User ID

_forceRefresh_\
From server

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

Search a roster item

`- (BMXErrorCode)searchWithRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* item:(BMXRosterItem *)*item*`

#### Parameters

_rosterId_\
User ID

_forceRefresh_\
From server

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

Set friend’s alias

`- (BMXErrorCode)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias*`

#### Parameters

_item_

_alias_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemAlias:alias:completion:

Set friend’s alias

`- (void)setItemAlias:(BMXRosterItem *)*item* alias:(NSString *)*alias* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_

_alias_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemExtension:extension:

Set extension information for the roster item(on server)

`- (BMXErrorCode)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

_item_

_extension_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemExtension:extension:completion:

Set extension information for the roster item(on server)

`- (void)setItemExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_

_extension_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemLocalExtension:extension:

Set extension information for the roster item(on local db)

`- (BMXErrorCode)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension*`

#### Parameters

_item_

_extension_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemLocalExtension:extension:completion:

Set extension information for the roster item(on local db)

`- (void)setItemLocalExtension:(BMXRosterItem *)*item* extension:(NSString *)*extension* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_

_extension_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemMuteNotification:status:

Set whether to mute user messages notification

`- (BMXErrorCode)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status*`

#### Parameters

_item_

_status_\
true for mute

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### setItemMuteNotification:status:completion:

Set whether to mute user messages notification

`- (void)setItemMuteNotification:(BMXRosterItem *)*item* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_item_

_status_\
true for mute

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### unblockWithRosterId:

Unblock a roster item

`- (BMXErrorCode)unblockWithRosterId:(long long)*rosterId*`

#### Parameters

_rosterId_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>

```

### unblockWithRosterId:completion:

Unblock a roster item

`- (void)unblockWithRosterId:(long long)*rosterId* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

_rosterId_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterService'></div>
```
