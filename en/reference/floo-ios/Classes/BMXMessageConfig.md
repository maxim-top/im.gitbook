# BMXMessageConfig Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Message config

## Class Methods

### createMessageConfigWithMentionAll:

`+ (BMXMessageConfig *)createMessageConfigWithMentionAll:(BOOL)*mentionAll*`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### addGroupMemberWithMemberId:

Add ID list of group members who read the message

`- (void)addGroupMemberWithMemberId:(long long)*memberId*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### clearGroupMemberList

Clear the ID list of group members who read the message

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

Get config for Android

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

Get the badge count in the current push message

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

Get the badge count type in the current push message

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

Get group members of the message

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

Get message config for iOS

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

Get whether to mention all members

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

Get a list of members to be mentioned

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

Get mentioned message

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

Get push message

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

Get push begin time

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

Get push end time

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

Get push title

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

Get RTC action (call, pickup, hang up, etc.)

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

Get RTC call ID

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

Get RTC call type(Audio|Video)

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

Caller ID

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

Get RTC call pin code

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

Get RTC room ID

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

Get RTC room type

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

Get sender nickname

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

Get user name

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

Is the push message silent

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

Remove the ID list of group members who read the message

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

Set message config for android device @param androidConfig

`- (void)setAndroidConfig:(NSString *)*androidConfig*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setGroupMemberList:

Set the ID list of group members who should read the message @param groupMemberList

`- (void)setGroupMemberList:(ListOfLongLong *)*groupMemberList*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setIOSConfig:

Set message config for iOS device @param iosConfig

`- (void)setIOSConfig:(NSString *)*iosConfig*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionAll:

Set whether to mention all members @param mentionAll

`- (void)setMentionAll:(BOOL)*mentionAll*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionList:

Set mentioned member list @param mentionList

`- (void)setMentionList:(ListOfLongLong *)*mentionList*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setMentionedMessage:

Set mentioned message @param mentionedMessage

`- (void)setMentionedMessage:(NSString *)*mentionedMessage*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushMessage:

Set push message @param pushMessage

`- (void)setPushMessage:(NSString *)*pushMessage*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushShowBeginTime:

Set push begin time @param beginTime

`- (void)setPushShowBeginTime:(int)*beginTime*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushShowEndTime:

Set push end time @param endTime

`- (void)setPushShowEndTime:(int)*endTime*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setPushTitle:

Set push title @param pushTitle

`- (void)setPushTitle:(NSString *)*pushTitle*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCCallInfo:roomId:initiator:roomType:pin:

Set RTC call info

`- (void)setRTCCallInfo:(BMXMessageConfig_RTCCallType)*calltype* roomId:(long long)*roomId* initiator:(long long)*initiator* roomType:(BMXMessageConfig_RTCRoomType)*roomType* pin:(NSString *)*pin*`

#### Parameters

_calltype_\
RTC call type

_roomId_

_initiator_

_roomType_\
meeting or streaming

_pin_\
RTC call pin code

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCHangupInfo:

Set RTC call hang up information

`- (void)setRTCHangupInfo:(NSString *)*callId*`

#### Parameters

_callId_\
RTC call ID

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setRTCPickupInfo:

Set RTC pickup information

`- (void)setRTCPickupInfo:(NSString *)*callId*`

#### Parameters

_callId_\
RTC call ID

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setSenderNickname:

Set sender nickname @param senderNickname

`- (void)setSenderNickname:(NSString *)*senderNickname*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>

```

### setUsername:

Set username @param username

`- (void)setUsername:(NSString *)*username*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessageConfig'></div>
```
