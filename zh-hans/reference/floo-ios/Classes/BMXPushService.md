# BMXPushService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 推送Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### bindDeviceTokenWithToken:

推送绑定设备token。

`- (BMXErrorCode)bindDeviceTokenWithToken:(NSString *)*token*`

#### Parameters

_token_\
设备的推送token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### bindVoipTokenWithToken:

推送绑定设备token。

`- (BMXErrorCode)bindVoipTokenWithToken:(NSString *)*token*`

#### Parameters

_token_\
设备的推送token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearAllNotifications

清空下拉通知栏全部通知。

`- (void)clearAllNotifications`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearNotificationWithNotificationId:

清除指定id的通知。

`- (void)clearNotificationWithNotificationId:(long long)*notificationId*`

#### Parameters

_notificationId_\
通知id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### clearTagsWithOperationId:

清空推送用户的标签。

`- (BMXErrorCode)clearTagsWithOperationId:(NSString *)*operationId*`

#### Parameters

_operationId_\
操作id。在回调通知中对应通知提醒。

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

删除推送用户的标签。

`- (BMXErrorCode)deleteTagsWithTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_\
要删除用户标签

_operationId_\
操作id。在回调通知中对应通知提醒。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getCert

获取登陆后服务器返回的推送证书。

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

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取

`- (BMXErrorCode)getPushProfile:(BMXPushUserProfile *)*pushProfile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_forceRefresh_\
是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

_profile_\
推送用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getTags:operationId:

获取推送用户的标签。

`- (BMXErrorCode)getTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_\
用户标签

_operationId_\
操作id。在回调通知中对应通知提醒。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### getToken

获取登陆后使用的用户token。

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

加载数据库本地存储的推送消息。如果不指定则从最新消息开始

`- (BMXErrorCode)loadLocalPushMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXPushService_PushDirection)*arg4*`

#### Parameters

_refMsgId_\
加载推送消息的起始id

_size_\
最大加载消息条数

_result_\
数据库返回的加载本地推送消息列表

_arg4_\
加载推送消息的方向，默认是加载更早的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-35='4' data-36='4' data-37='4' data-38='4' data-39='4' data-40='4' data-41='4' data-42='4' data-43='4' data-44='4' data-45='4' data-46='4' data-47='4' data-48='4' data-49='4' data-50='4' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### resume

恢复推送功能接口。

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

发送推送上行消息，消息状态变化会通过listener通知

`- (void)sendMessageWithContent:(NSString *)*content*`

#### Parameters

_content_\
发送的上行推送消息内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setBadge:

设置推送用户的未读角标。

`- (BMXErrorCode)setBadge:(int)*count*`

#### Parameters

_count_\
用户未读角标数

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

设置推送的地理围栏功能是否运行。

`- (BMXErrorCode)setGeoFenceMode:(BOOL)*enable* isAllow:(BOOL)*isAllow*`

#### Parameters

_enable_\
地理围栏功能是否运行。

_isAllow_\
用户是否主动弹出用户定位请求。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setPushMode

设置允许推送时间。

`- (BMXErrorCode)setPushMode`

#### Parameters

_startHour_\
静默允许推送的起始时间小时

_endHour_\
静默允许推送的结束时间小时

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setPushMode:

设置推送启用状态。默认为使用推送。

`- (BMXErrorCode)setPushMode:(BOOL)*enable*`

#### Parameters

_enable_\
推送的启用状态

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

设置推送是否可以后台运行。默认是false。

`- (BMXErrorCode)setRunBackgroundMode:(BOOL)*enable*`

#### Parameters

_enable_\
推送后台运行状态。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setSilenceTime:endHour:

设置推送静默的起始结束时间。

`- (BMXErrorCode)setSilenceTime:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

_startHour_\
静默推送的起始时间小时

_endHour_\
静默推送的结束时间小时

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### setTags:operationId:

设置推送用户的标签。

`- (BMXErrorCode)setTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

_tags_\
用户标签

_operationId_\
操作id。在回调通知中对应通知提醒。

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

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

`- (BMXErrorCode)startWithAlias:(NSString *)*alias* bmxToken:(NSString *)*bmxToken*`

#### Parameters

_alias_\
推送初始化使用的当前用户别名

_bmxToken_\
推送初始化的时候App传入的使用的用户的token，无用户的状态下不传入即可。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>

```

### status

推送sdk当前的状态。

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

停止推送功能接口。

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

解除用户别名绑定。

`- (BMXErrorCode)unbindAliasWithAlias:(NSString *)*alias*`

#### Parameters

_alias_\
需要解除绑定的用户别名。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushService'></div>
```
