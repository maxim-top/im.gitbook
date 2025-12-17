# BMXRTCEngineProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol RTC Engine listener

## Instance Methods

### onErrorWithInfo:error:

Received an error

`- (void)onErrorWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onJoinRoomWithInfo:roomId:error:

Joined a room

`- (void)onJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_info_

_roomId_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onKickoffWithInfo:error:

Kicked off

`- (void)onKickoffWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLeaveRoomWithInfo:roomId:error:reason:

Left a room

`- (void)onLeaveRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error* reason:(NSString *)*reason*`

#### Parameters

_info_

_roomId_

_error_

_reason_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalAudioLevelWithVolume:

Local audio volume changed

`- (void)onLocalAudioLevelWithVolume:(int)*volume*`

#### Parameters

_volume_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalPublishWithStream:info:error:

Local stream published

`- (void)onLocalPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalStreamMuteRspWithStream:trackType:mute:info:error:

Local stream muted or unmuted

`- (void)onLocalStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_trackType_\
Audio or video

_mute_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalUnPublishWithStream:info:error:

Local stream unpublished

`- (void)onLocalUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onMemberExitedWithRoomId:usedId:reason:

Other member left

`- (void)onMemberExitedWithRoomId:(long long)*roomId* usedId:(long long)*usedId* reason:(NSString *)*reason*`

#### Parameters

_roomId_

_reason_

_userId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onMemberJoinedWithRoomId:usedId:

Other member joined

`- (void)onMemberJoinedWithRoomId:(long long)*roomId* usedId:(long long)*usedId*`

#### Parameters

_roomId_

_usedId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onNetworkQualityWithStream:info:error:

Stream network quality changed

`- (void)onNetworkQualityWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onReJoinRoomWithInfo:roomId:error:

Rejoined a room

`- (void)onReJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_info_

_roomId_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRejoiningWithRoomId:error:

Rejoining a room

`- (void)onRejoiningWithRoomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_roomId_

_error_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteAudioLevelWithUserId:volume:

Remote audio volume changed

`- (void)onRemoteAudioLevelWithUserId:(long long)*userId* volume:(int)*volume*`

#### Parameters

_userId_

_volume_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemotePublishWithStream:info:error:

Remote stream published

`- (void)onRemotePublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteRTCStatsWithStreamStats:info:error:

Remote RTC statistics data received

`- (void)onRemoteRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_streamStats_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteStreamMuteRspWithStream:trackType:mute:info:error:

Remote stream muted or unmuted

`- (void)onRemoteStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_trackType_\
Audio or video

_mute_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteTrackNotifyWithStream:trackType:info:error:

Remote stream track updated

`- (void)onRemoteTrackNotifyWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_trackType_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteUnPublishWithStream:info:error:

Remote stream unpublished

`- (void)onRemoteUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onSendRTCStatsWithStreamStats:info:error:

RTC stream statistics data sent

`- (void)onSendRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_streamStats_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onSubscribeWithStream:info:error:

Stream subscribed

`- (void)onSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onUnSubscribeWithStream:info:error:

Stream unsubscribed

`- (void)onUnSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onWarningWithInfo:error:

Warning info received

`- (void)onWarningWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>
```
