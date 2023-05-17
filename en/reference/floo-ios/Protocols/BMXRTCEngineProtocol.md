# BMXRTCEngineProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol RTC Engine listener

## Instance Methods

<a name="//api/name/onErrorWithInfo:error:" title="onErrorWithInfo:error:"></a>
### onErrorWithInfo:error:

Received an error

`- (void)onErrorWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onJoinRoomWithInfo:roomId:error:" title="onJoinRoomWithInfo:roomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onErrorWithInfo:error:" %}{% endlanying_code_snippet %}
```
### onJoinRoomWithInfo:roomId:error:

Joined a room

`- (void)onJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*info*  

*roomId*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onKickoffWithInfo:error:" title="onKickoffWithInfo:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onJoinRoomWithInfo:roomId:error:" %}{% endlanying_code_snippet %}
```
### onKickoffWithInfo:error:

Kicked off

`- (void)onKickoffWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLeaveRoomWithInfo:roomId:error:reason:" title="onLeaveRoomWithInfo:roomId:error:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onKickoffWithInfo:error:" %}{% endlanying_code_snippet %}
```
### onLeaveRoomWithInfo:roomId:error:reason:

Left a room

`- (void)onLeaveRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error* reason:(NSString *)*reason*`

#### Parameters

*info*  

*roomId*  

*error*  

*reason*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalAudioLevelWithVolume:" title="onLocalAudioLevelWithVolume:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLeaveRoomWithInfo:roomId:error:reason:" %}{% endlanying_code_snippet %}
```
### onLocalAudioLevelWithVolume:

Local audio volume changed

`- (void)onLocalAudioLevelWithVolume:(int)*volume*`

#### Parameters

*volume*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalPublishWithStream:info:error:" title="onLocalPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalAudioLevelWithVolume:" %}{% endlanying_code_snippet %}
```
### onLocalPublishWithStream:info:error:

Local stream published

`- (void)onLocalPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalStreamMuteRspWithStream:trackType:mute:info:error:" title="onLocalStreamMuteRspWithStream:trackType:mute:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onLocalStreamMuteRspWithStream:trackType:mute:info:error:

Local stream muted or unmuted

`- (void)onLocalStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*trackType*  
    Audio or video

*mute*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalUnPublishWithStream:info:error:" title="onLocalUnPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalStreamMuteRspWithStream:trackType:mute:info:error:" %}{% endlanying_code_snippet %}
```
### onLocalUnPublishWithStream:info:error:

Local stream unpublished

`- (void)onLocalUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onMemberExitedWithRoomId:usedId:reason:" title="onMemberExitedWithRoomId:usedId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalUnPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onMemberExitedWithRoomId:usedId:reason:

Other member left

`- (void)onMemberExitedWithRoomId:(long long)*roomId* usedId:(long long)*usedId* reason:(NSString *)*reason*`

#### Parameters

*roomId*  

*reason*  

*userId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onMemberJoinedWithRoomId:usedId:" title="onMemberJoinedWithRoomId:usedId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onMemberExitedWithRoomId:usedId:reason:" %}{% endlanying_code_snippet %}
```
### onMemberJoinedWithRoomId:usedId:

Other member joined

`- (void)onMemberJoinedWithRoomId:(long long)*roomId* usedId:(long long)*usedId*`

#### Parameters

*roomId*  

*usedId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onNetworkQualityWithStream:info:error:" title="onNetworkQualityWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onMemberJoinedWithRoomId:usedId:" %}{% endlanying_code_snippet %}
```
### onNetworkQualityWithStream:info:error:

Stream network quality changed

`- (void)onNetworkQualityWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onReJoinRoomWithInfo:roomId:error:" title="onReJoinRoomWithInfo:roomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onNetworkQualityWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onReJoinRoomWithInfo:roomId:error:

Rejoined a room

`- (void)onReJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*info*  

*roomId*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRejoiningWithRoomId:error:" title="onRejoiningWithRoomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onReJoinRoomWithInfo:roomId:error:" %}{% endlanying_code_snippet %}
```
### onRejoiningWithRoomId:error:

Rejoining a room

`- (void)onRejoiningWithRoomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*roomId*  

*error*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteAudioLevelWithUserId:volume:" title="onRemoteAudioLevelWithUserId:volume:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRejoiningWithRoomId:error:" %}{% endlanying_code_snippet %}
```
### onRemoteAudioLevelWithUserId:volume:

Remote audio volume changed

`- (void)onRemoteAudioLevelWithUserId:(long long)*userId* volume:(int)*volume*`

#### Parameters

*userId*  

*volume*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemotePublishWithStream:info:error:" title="onRemotePublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteAudioLevelWithUserId:volume:" %}{% endlanying_code_snippet %}
```
### onRemotePublishWithStream:info:error:

Remote stream published

`- (void)onRemotePublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteRTCStatsWithStreamStats:info:error:" title="onRemoteRTCStatsWithStreamStats:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemotePublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteRTCStatsWithStreamStats:info:error:

Remote RTC statistics data received

`- (void)onRemoteRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*streamStats*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteStreamMuteRspWithStream:trackType:mute:info:error:" title="onRemoteStreamMuteRspWithStream:trackType:mute:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteRTCStatsWithStreamStats:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteStreamMuteRspWithStream:trackType:mute:info:error:

Remote stream muted or unmuted

`- (void)onRemoteStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*trackType*  
    Audio or video

*mute*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteTrackNotifyWithStream:trackType:info:error:" title="onRemoteTrackNotifyWithStream:trackType:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteStreamMuteRspWithStream:trackType:mute:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteTrackNotifyWithStream:trackType:info:error:

Remote stream track updated

`- (void)onRemoteTrackNotifyWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*trackType*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteUnPublishWithStream:info:error:" title="onRemoteUnPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteTrackNotifyWithStream:trackType:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteUnPublishWithStream:info:error:

Remote stream unpublished

`- (void)onRemoteUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onSendRTCStatsWithStreamStats:info:error:" title="onSendRTCStatsWithStreamStats:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteUnPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onSendRTCStatsWithStreamStats:info:error:

RTC stream statistics data sent

`- (void)onSendRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*streamStats*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onSubscribeWithStream:info:error:" title="onSubscribeWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onSendRTCStatsWithStreamStats:info:error:" %}{% endlanying_code_snippet %}
```
### onSubscribeWithStream:info:error:

Stream subscribed

`- (void)onSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onUnSubscribeWithStream:info:error:" title="onUnSubscribeWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onSubscribeWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onUnSubscribeWithStream:info:error:

Stream unsubscribed

`- (void)onUnSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onWarningWithInfo:error:" title="onWarningWithInfo:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onUnSubscribeWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onWarningWithInfo:error:

Warning info received

`- (void)onWarningWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  

*error*  

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onWarningWithInfo:error:" %}{% endlanying_code_snippet %}
```
