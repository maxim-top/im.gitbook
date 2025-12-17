# BMXPushService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Push Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### bindDeviceTokenWithToken:

Bind device token for push service

`- (BMXErrorCode)bindDeviceTokenWithToken:(NSString *)*token*`

#### Parameters

_token_\
Device token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### bindVoipTokenWithToken:

Bind VOIP device token for push service

`- (BMXErrorCode)bindVoipTokenWithToken:(NSString *)*token*`

#### Parameters

_token_\
Device token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearAllNotifications

Clear all notifications on the notification bar

`- (void)clearAllNotifications`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearNotificationWithNotificationId:

Clear a notification by ID

`- (void)clearNotificationWithNotificationId:(long long)*notificationId*`

#### Parameters

_notificationId_\
Notification ID

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearTagsWithOperationId:

Clear tags by operation ID

`- (BMXErrorCode)clearTagsWithOperationId:(NSString *)*operationId*`

#### Parameters

_operationId_\
Operation ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### deleteTagsWithTags:operationId:

Remove tags by operation ID

`- (BMXErrorCode)deleteTagsWithTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_\
tags

_operationId_\
Operation ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getCert

Get the push service certificate

`- (NSString *)getCert`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getPushProfile:forceRefresh:

Get the profile of push user

`- (BMXErrorCode)getPushProfile:(BMXPushUserProfile *)*pushProfile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_forceRefresh_\
From server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getTags:operationId:

Get tags of push user

`- (BMXErrorCode)getTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_\
Tag list

_operationId_\
Operation ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getToken

Get access token

`- (NSString *)getToken`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### loadLocalPushMessagesWithRefMsgId:size:result:

`- (BMXErrorCode)loadLocalPushMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### loadLocalPushMessagesWithRefMsgId:size:result:arg4:

Load push messages in local db

`- (BMXErrorCode)loadLocalPushMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXPushService_PushDirection)*arg4*`

#### Parameters

_refMsgId_\
First Message Id

_size_\
Message list as result

_arg4_\
Search direction, Up for earlier

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-35='4' data-36='4' data-37='4' data-38='4' data-39='4' data-40='4' data-41='4' data-42='4' data-43='4' data-44='4' data-45='4' data-46='4' data-47='4' data-48='4' data-49='4' data-50='4' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### resume

Resume push function

`- (BMXErrorCode)resume`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### sendMessageWithContent:

Send a push message

`- (void)sendMessageWithContent:(NSString *)*content*`

#### Parameters

_content_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setBadge:

Set badge count

`- (BMXErrorCode)setBadge:(int)*count*`

#### Parameters

_count_\
Badge count

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setGeoFenceMode

`- (BMXErrorCode)setGeoFenceMode`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setGeoFenceMode:

`- (BMXErrorCode)setGeoFenceMode:(BOOL)*enable*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setGeoFenceMode:isAllow:

Set geo-fencing mode

`- (BMXErrorCode)setGeoFenceMode:(BOOL)*enable* isAllow:(BOOL)*isAllow*`

#### Parameters

_enable_\
Enable the feature

_isAllow_\
Does the user allow

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setPushMode:

Set whether push is allowed

`- (BMXErrorCode)setPushMode:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setPushTime:endHour:

`- (BMXErrorCode)setPushTime:(int)*startHour* endHour:(int)*endHour*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setRunBackgroundMode

`- (BMXErrorCode)setRunBackgroundMode`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setRunBackgroundMode:

Set whether push is allowed to run in the background

`- (BMXErrorCode)setRunBackgroundMode:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setSilenceTime:endHour:

Set the silence time range for the push service

`- (BMXErrorCode)setSilenceTime:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

_startHour_

_endHour_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setTags:operationId:

Set tags for push service

`- (BMXErrorCode)setTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_

_operationId_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### start

`- (BMXErrorCode)start`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### startWithAlias:

`- (BMXErrorCode)startWithAlias:(NSString *)*alias*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### startWithAlias:bmxToken:

Start push service

`- (BMXErrorCode)startWithAlias:(NSString *)*alias* bmxToken:(NSString *)*bmxToken*`

#### Parameters

_alias_\
User alias for push service

_bmxToken_\
User access token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### status

The status of push SDK

`- (BMXPushService_PushSdkStatus)status`

#### Return Value

[BMXPushService\_PushSdkStatus](../Constants/BMXPushService_PushSdkStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### stop

Stop push service

`- (BMXErrorCode)stop`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### unbindAliasWithAlias:

Unbind user alias

`- (BMXErrorCode)unbindAliasWithAlias:(NSString *)*alias*`

#### Parameters

_alias_\
User alias

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>
```
