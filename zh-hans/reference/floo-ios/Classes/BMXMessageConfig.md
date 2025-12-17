# BMXMessageConfig Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 消息配置

## Class Methods

### createMessageConfigWithMentionAll:

`+ (BMXMessageConfig *)createMessageConfigWithMentionAll:(BOOL)*mentionAll*`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### addGroupMemberWithMemberId:

添加群已读消息的群成员id列表成员

`- (void)addGroupMemberWithMemberId:(long long)*memberId*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### clearGroupMemberList

清空群已读消息的群成员id列表

`- (void)clearGroupMemberList`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getAndroidConfig

获取Android系统配置信息

`- (NSString *)getAndroidConfig`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getBadgeCount:

获取当前的推送消息中badge计数

`- (int)getBadgeCount:(int)*count*`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getBadgeCountType

获取当前的推送消息中badge计数

`- (BMXMessageConfig_BadgeCountType)getBadgeCountType`

#### Return Value

BadgeCountType

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getGroupMemberList

获取需要群已读消息的群成员id列表

`- (ListOfLongLong *)getGroupMemberList`

#### Return Value

[ListOfLongLong](ListOfLongLong.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getIOSConfig

获取IOS系统配置信息

`- (NSString *)getIOSConfig`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getMentionAll

获取是否@全员

`- (BOOL)getMentionAll`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getMentionList

获取@成员列表

`- (ListOfLongLong *)getMentionList`

#### Return Value

[ListOfLongLong](ListOfLongLong.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getMentionedMessage

获取@消息

`- (NSString *)getMentionedMessage`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getPushMessage

获取推送消息

`- (NSString *)getPushMessage`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getPushShowBeginTime

获取推送显示开始时间

`- (int)getPushShowBeginTime`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getPushShowEndTime

获取推送显示结束时间

`- (int)getPushShowEndTime`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getPushTitle

获取推送标题

`- (NSString *)getPushTitle`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCAction

获得RTC相关操作类型信息（呼叫、接通、挂断等）。

`- (NSString *)getRTCAction`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCCallId

获得RTC相关callId信息。

`- (NSString *)getRTCCallId`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCCallType

获得RTC相关通话类型（音频通话、视频通话类型）。

`- (BMXMessageConfig_RTCCallType)getRTCCallType`

#### Return Value

RTCCallType

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCInitiator

获得RTC相关发起者id信息。

`- (long long)getRTCInitiator`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCPin

获得RTC相关pin码信息。

`- (NSString *)getRTCPin`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCRoomId

获得RTC相关房间id信息。

`- (long long)getRTCRoomId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getRTCRoomType

获得RTC相关房间类型信息。

`- (BMXMessageConfig_RTCRoomType)getRTCRoomType`

#### Return Value

[BMXMessageConfig\_RTCRoomType](../Constants/BMXMessageConfig_RTCRoomType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getSenderNickname

获取发送者昵称

`- (NSString *)getSenderNickname`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### getUsername

获得用户名

`- (NSString *)getUsername`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### isSilence

获取当前的推送消息是否是静默消息

`- (BOOL)isSilence`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### removeGroupMemberWithMemberId:

清除需要群已读消息的群成员id列表成员

`- (void)removeGroupMemberWithMemberId:(long long)*memberId*`

#### Return Value

[ListOfLongLong](ListOfLongLong.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### serialize

序列化操作

`- (NSString *)serialize`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setAndroidConfig:

设置Android系统配置信息 @param androidConfig

`- (void)setAndroidConfig:(NSString *)*androidConfig*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setGroupMemberList:

设置需要群已读消息的群成员id列表 @param groupMemberList

`- (void)setGroupMemberList:(ListOfLongLong *)*groupMemberList*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setIOSConfig:

设置IOS系统配置信息 @param iosConfig

`- (void)setIOSConfig:(NSString *)*iosConfig*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionAll:

设置是否@全员 @param mentionAll

`- (void)setMentionAll:(BOOL)*mentionAll*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionList:

设置通知成员id列表 @param mentionList

`- (void)setMentionList:(ListOfLongLong *)*mentionList*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionedMessage:

设置@消息 @param mentionedMessage

`- (void)setMentionedMessage:(NSString *)*mentionedMessage*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushMessage:

设置推送消息 @param pushMessage

`- (void)setPushMessage:(NSString *)*pushMessage*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushShowBeginTime:

设置推送显示开始时间 @param beginTime

`- (void)setPushShowBeginTime:(int)*beginTime*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushShowEndTime:

设置推送显示结束时间 @param endTime

`- (void)setPushShowEndTime:(int)*endTime*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushTitle:

设置推送标题 @param pushTitle

`- (void)setPushTitle:(NSString *)*pushTitle*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCCallInfo:roomId:initiator:roomType:pin:

设置呼叫消息信息

`- (void)setRTCCallInfo:(BMXMessageConfig_RTCCallType)*calltype* roomId:(long long)*roomId* initiator:(long long)*initiator* roomType:(BMXMessageConfig_RTCRoomType)*roomType* pin:(NSString *)*pin*`

#### Parameters

_calltype_\
通话类型（语音电话、视频电话）

_roomId_\
房间id

_initiator_\
发起者id

_roomType_\
房间类型（会议模式，直播模式）

_pin_\
加入房间的pin码

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCHangupInfo:

设置挂断消息信息

`- (void)setRTCHangupInfo:(NSString *)*callId*`

#### Parameters

_callId_\
通话id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCPickupInfo:

设置接通消息信息

`- (void)setRTCPickupInfo:(NSString *)*callId*`

#### Parameters

_callId_\
通话id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setSenderNickname:

设置发送者昵称 @param senderNickname

`- (void)setSenderNickname:(NSString *)*senderNickname*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setUsername:

设置用户名 @param username

`- (void)setUsername:(NSString *)*username*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>
```
