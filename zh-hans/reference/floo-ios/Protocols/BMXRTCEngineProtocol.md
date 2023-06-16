# BMXRTCEngineProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol RTC Engine监听者

## Instance Methods

<a name="//api/name/onErrorWithInfo:error:" title="onErrorWithInfo:error:"></a>
### onErrorWithInfo:error:

错误信息回调

`- (void)onErrorWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onJoinRoomWithInfo:roomId:error:" title="onJoinRoomWithInfo:roomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onErrorWithInfo:error:" %}{% endlanying_code_snippet %}
```
### onJoinRoomWithInfo:roomId:error:

用户加入房间回调

`- (void)onJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*info*  
   通知信息  

*roomId*  
   房间Id  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onKickoffWithInfo:error:" title="onKickoffWithInfo:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onJoinRoomWithInfo:roomId:error:" %}{% endlanying_code_snippet %}
```
### onKickoffWithInfo:error:

被踢信息回调

`- (void)onKickoffWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLeaveRoomWithInfo:roomId:error:reason:" title="onLeaveRoomWithInfo:roomId:error:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onKickoffWithInfo:error:" %}{% endlanying_code_snippet %}
```
### onLeaveRoomWithInfo:roomId:error:reason:

用户离开房间回调

`- (void)onLeaveRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error* reason:(NSString *)*reason*`

#### Parameters

*info*  
   通知信息  

*roomId*  
   房间Id  

*error*  
   错误码信息  

*reason*  
   离开原因  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalAudioLevelWithVolume:" title="onLocalAudioLevelWithVolume:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLeaveRoomWithInfo:roomId:error:reason:" %}{% endlanying_code_snippet %}
```
### onLocalAudioLevelWithVolume:

本地音量调节回调

`- (void)onLocalAudioLevelWithVolume:(int)*volume*`

#### Parameters

*volume*  
   音量信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalPublishWithStream:info:error:" title="onLocalPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalAudioLevelWithVolume:" %}{% endlanying_code_snippet %}
```
### onLocalPublishWithStream:info:error:

本地流发布回调

`- (void)onLocalPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalStreamMuteRspWithStream:trackType:mute:info:error:" title="onLocalStreamMuteRspWithStream:trackType:mute:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onLocalStreamMuteRspWithStream:trackType:mute:info:error:

本地音频或视频启用禁用通知回调

`- (void)onLocalStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*trackType*  
   音轨或者视频轨类型  

*mute*  
   启用或禁用  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onLocalUnPublishWithStream:info:error:" title="onLocalUnPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalStreamMuteRspWithStream:trackType:mute:info:error:" %}{% endlanying_code_snippet %}
```
### onLocalUnPublishWithStream:info:error:

本地流停止发布回调

`- (void)onLocalUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onMemberExitedWithRoomId:usedId:reason:" title="onMemberExitedWithRoomId:usedId:reason:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onLocalUnPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onMemberExitedWithRoomId:usedId:reason:

其他用户离开房间回调

`- (void)onMemberExitedWithRoomId:(long long)*roomId* usedId:(long long)*usedId* reason:(NSString *)*reason*`

#### Parameters

*roomId*  
   房间Id  

*reason*  
   离开原因  

*userId*  
   用户Id  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onMemberJoinedWithRoomId:usedId:" title="onMemberJoinedWithRoomId:usedId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onMemberExitedWithRoomId:usedId:reason:" %}{% endlanying_code_snippet %}
```
### onMemberJoinedWithRoomId:usedId:

其他用户加入房间回调

`- (void)onMemberJoinedWithRoomId:(long long)*roomId* usedId:(long long)*usedId*`

#### Parameters

*roomId*  
   房间Id  

*usedId*  
   用户id  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onNetworkQualityWithStream:info:error:" title="onNetworkQualityWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onMemberJoinedWithRoomId:usedId:" %}{% endlanying_code_snippet %}
```
### onNetworkQualityWithStream:info:error:

网络质量回调

`- (void)onNetworkQualityWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onReJoinRoomWithInfo:roomId:error:" title="onReJoinRoomWithInfo:roomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onNetworkQualityWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onReJoinRoomWithInfo:roomId:error:

重新加入房间完成回调

`- (void)onReJoinRoomWithInfo:(NSString *)*info* roomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*info*  
   通知信息  

*roomId*  
   房间Id  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRejoiningWithRoomId:error:" title="onRejoiningWithRoomId:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onReJoinRoomWithInfo:roomId:error:" %}{% endlanying_code_snippet %}
```
### onRejoiningWithRoomId:error:

@brief断线重新加入房间回调

`- (void)onRejoiningWithRoomId:(long long)*roomId* error:(BMXErrorCode)*error*`

#### Parameters

*roomId*  
   房间Id  

*error*  
   错误码信息  

#### Discussion
@brief断线重新加入房间回调

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteAudioLevelWithUserId:volume:" title="onRemoteAudioLevelWithUserId:volume:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRejoiningWithRoomId:error:" %}{% endlanying_code_snippet %}
```
### onRemoteAudioLevelWithUserId:volume:

远端音量调节回调

`- (void)onRemoteAudioLevelWithUserId:(long long)*userId* volume:(int)*volume*`

#### Parameters

*userId*  
   用户id  

*volume*  
   音量信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemotePublishWithStream:info:error:" title="onRemotePublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteAudioLevelWithUserId:volume:" %}{% endlanying_code_snippet %}
```
### onRemotePublishWithStream:info:error:

远程流发布回调

`- (void)onRemotePublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteRTCStatsWithStreamStats:info:error:" title="onRemoteRTCStatsWithStreamStats:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemotePublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteRTCStatsWithStreamStats:info:error:

远端统计信息回调

`- (void)onRemoteRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*streamStats*  
   远端流统计信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteStreamMuteRspWithStream:trackType:mute:info:error:" title="onRemoteStreamMuteRspWithStream:trackType:mute:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteRTCStatsWithStreamStats:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteStreamMuteRspWithStream:trackType:mute:info:error:

远端音频或视频启用禁用通知回调

`- (void)onRemoteStreamMuteRspWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* mute:(BOOL)*mute* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*trackType*  
   音轨或者视频轨类型  

*mute*  
   启用或禁用  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteTrackNotifyWithStream:trackType:info:error:" title="onRemoteTrackNotifyWithStream:trackType:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteStreamMuteRspWithStream:trackType:mute:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteTrackNotifyWithStream:trackType:info:error:

远端流信息变更通知

`- (void)onRemoteTrackNotifyWithStream:(BMXStream *)*stream* trackType:(BMXTrackType)*trackType* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*trackType*  
   音轨或者视频轨类型  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRemoteUnPublishWithStream:info:error:" title="onRemoteUnPublishWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteTrackNotifyWithStream:trackType:info:error:" %}{% endlanying_code_snippet %}
```
### onRemoteUnPublishWithStream:info:error:

远程流停止发布回调

`- (void)onRemoteUnPublishWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onSendRTCStatsWithStreamStats:info:error:" title="onSendRTCStatsWithStreamStats:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onRemoteUnPublishWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onSendRTCStatsWithStreamStats:info:error:

发送端统计信息回调

`- (void)onSendRTCStatsWithStreamStats:(BMXStreamStats *)*streamStats* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*streamStats*  
   本地流统计信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onSubscribeWithStream:info:error:" title="onSubscribeWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onSendRTCStatsWithStreamStats:info:error:" %}{% endlanying_code_snippet %}
```
### onSubscribeWithStream:info:error:

订阅流回调

`- (void)onSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onUnSubscribeWithStream:info:error:" title="onUnSubscribeWithStream:info:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onSubscribeWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onUnSubscribeWithStream:info:error:

停止订阅流回调

`- (void)onUnSubscribeWithStream:(BMXStream *)*stream* info:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*stream*  
   流信息  

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onWarningWithInfo:error:" title="onWarningWithInfo:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onUnSubscribeWithStream:info:error:" %}{% endlanying_code_snippet %}
```
### onWarningWithInfo:error:

警告信息回调

`- (void)onWarningWithInfo:(NSString *)*info* error:(BMXErrorCode)*error*`

#### Parameters

*info*  
   通知信息  

*error*  
   错误码信息  

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngineProtocol",function="onWarningWithInfo:error:" %}{% endlanying_code_snippet %}
```
