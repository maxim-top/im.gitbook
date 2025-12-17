# BMXRTCEngineProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol RTC Engine监听者

## Instance Methods

### onErrorWithInfo:error:

错误信息回调

`- (void)onErrorWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onJoinRoomWithInfo:roomId:error:

用户加入房间回调

`- (void)onJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_info_\
通知信息

_roomId_\
房间Id

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onKickoffWithInfo:error:

被踢信息回调

`- (void)onKickoffWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLeaveRoomWithInfo:roomId:error:reason:

用户离开房间回调

`- (void)onLeaveRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error* reason:(NSString *)*reason*`

#### Parameters

_info_\
通知信息

_roomId_\
房间Id

_error_\
错误码信息

_reason_\
离开原因

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalAudioLevelWithVolume:

本地音量调节回调

`- (void)onLocalAudioLevelWithVolume:(int)*volume*`

#### Parameters

_volume_\
音量信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalPublishWithStream:info:error:

本地流发布回调

`- (void)onLocalPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalStreamMuteRspWithStream:trackType:mute:info:error:

本地音频或视频启用禁用通知回调

`- (void)onLocalStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_trackType_\
音轨或者视频轨类型

_mute_\
启用或禁用

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onLocalUnPublishWithStream:info:error:

本地流停止发布回调

`- (void)onLocalUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onMemberExitedWithRoomId:usedId:reason:

其他用户离开房间回调

`- (void)onMemberExitedWithRoomId:(long long)*roomId* usedId:(long long)*usedId* reason:(NSString *)*reason*`

#### Parameters

_roomId_\
房间Id

_reason_\
离开原因

_userId_\
用户Id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onMemberJoinedWithRoomId:usedId:

其他用户加入房间回调

`- (void)onMemberJoinedWithRoomId:(long long)*roomId* usedId:(long long)*usedId*`

#### Parameters

_roomId_\
房间Id

_usedId_\
用户id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onNetworkQualityWithStream:info:error:

网络质量回调

`- (void)onNetworkQualityWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onReJoinRoomWithInfo:roomId:error:

重新加入房间完成回调

`- (void)onReJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_info_\
通知信息

_roomId_\
房间Id

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRejoiningWithRoomId:error:

@brief断线重新加入房间回调

`- (void)onRejoiningWithRoomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

_roomId_\
房间Id

_error_\
错误码信息

#### Discussion

@brief断线重新加入房间回调

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteAudioLevelWithUserId:volume:

远端音量调节回调

`- (void)onRemoteAudioLevelWithUserId:(long long)*userId* volume:(int)*volume*`

#### Parameters

_userId_\
用户id

_volume_\
音量信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemotePublishWithStream:info:error:

远程流发布回调

`- (void)onRemotePublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteRTCStatsWithStreamStats:info:error:

远端统计信息回调

`- (void)onRemoteRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_streamStats_\
远端流统计信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteStreamMuteRspWithStream:trackType:mute:info:error:

远端音频或视频启用禁用通知回调

`- (void)onRemoteStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_trackType_\
音轨或者视频轨类型

_mute_\
启用或禁用

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteTrackNotifyWithStream:trackType:info:error:

远端流信息变更通知

`- (void)onRemoteTrackNotifyWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_trackType_\
音轨或者视频轨类型

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onRemoteUnPublishWithStream:info:error:

远程流停止发布回调

`- (void)onRemoteUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onSendRTCStatsWithStreamStats:info:error:

发送端统计信息回调

`- (void)onSendRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_streamStats_\
本地流统计信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onSubscribeWithStream:info:error:

订阅流回调

`- (void)onSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onUnSubscribeWithStream:info:error:

停止订阅流回调

`- (void)onUnSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_stream_\
流信息

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>

```

### onWarningWithInfo:error:

警告信息回调

`- (void)onWarningWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

_info_\
通知信息

_error_\
错误码信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngineProtocol'></div>
```
