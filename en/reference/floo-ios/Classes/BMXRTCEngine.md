# BMXRTCEngine Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface RTC Engine

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

Add a RTC engine listener

`- (void)addDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRTCEngineProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addRTCEngineListener:" title="addRTCEngineListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addRTCEngineListener:

`- (void)addRTCEngineListener:(id<BMXRTCEngineProtocol>)*listener*`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="addRTCEngineListener:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/destroy" title="destroy"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="dealloc" %}{% endlanying_code_snippet %}
```
### destroy

Destroy the RTC engine

`- (void)destroy`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCConfig" title="getRTCConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="destroy" %}{% endlanying_code_snippet %}
```
### getRTCConfig

Get RTC config

`- (BMXRTCConfig *)getRTCConfig`

#### Return Value
<a href="../Classes/BMXRTCConfig.md">BMXRTCConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="getRTCConfig" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/joinRoomWithAuth:" title="joinRoomWithAuth:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### joinRoomWithAuth:

Join a room

`- (BMXErrorCode)joinRoomWithAuth:(BMXRoomAuth *)*auth*`

#### Parameters

*auth*  
    Authorization information

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/leaveRoom" title="leaveRoom"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="joinRoomWithAuth:" %}{% endlanying_code_snippet %}
```
### leaveRoom

Leave a room

`- (BMXErrorCode)leaveRoom`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteLocalAudioWithMute:" title="muteLocalAudioWithMute:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="leaveRoom" %}{% endlanying_code_snippet %}
```
### muteLocalAudioWithMute:

Mute or unmute my audio

`- (BMXErrorCode)muteLocalAudioWithMute:(BOOL)*mute*`

#### Parameters

*mute*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteLocalVideoWithType:mute:" title="muteLocalVideoWithType:mute:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="muteLocalAudioWithMute:" %}{% endlanying_code_snippet %}
```
### muteLocalVideoWithType:mute:

Mute or unmute my video

`- (BMXErrorCode)muteLocalVideoWithType:(BMXVideoMediaType)*type* mute:(BOOL)*mute*`

#### Parameters

*type*  
    Video media type

*mute*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteRemoteAudioWithStream:mute:" title="muteRemoteAudioWithStream:mute:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="muteLocalVideoWithType:mute:" %}{% endlanying_code_snippet %}
```
### muteRemoteAudioWithStream:mute:

Mute or unmute remote video

`- (BMXErrorCode)muteRemoteAudioWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

*stream*  

*mute*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/muteRemoteVideoWithStream:mute:" title="muteRemoteVideoWithStream:mute:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="muteRemoteAudioWithStream:mute:" %}{% endlanying_code_snippet %}
```
### muteRemoteVideoWithStream:mute:

Mute or unmute remote video

`- (BMXErrorCode)muteRemoteVideoWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

*stream*  

*mute*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/publishWithType:hasVideo:hasAudio:" title="publishWithType:hasVideo:hasAudio:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="muteRemoteVideoWithStream:mute:" %}{% endlanying_code_snippet %}
```
### publishWithType:hasVideo:hasAudio:

Publish my video and audio streams

`- (BMXErrorCode)publishWithType:(BMXVideoMediaType)*type* hasVideo:(BOOL)*hasVideo* hasAudio:(BOOL)*hasAudio*`

#### Parameters

*type*  
    Stream type

*hasVideo*  

*hasAudio*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="publishWithType:hasVideo:hasAudio:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

Remove a RTC engine listener

`- (void)removeDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeRTCEngineListener:" title="removeRTCEngineListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeRTCEngineListener:

`- (void)removeRTCEngineListener:(id<BMXRTCEngineProtocol>)*listener*`

<a name="//api/name/setAudioProfile:" title="setAudioProfile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="removeRTCEngineListener:" %}{% endlanying_code_snippet %}
```
### setAudioProfile:

Set audio settings

`- (BMXErrorCode)setAudioProfile:(BMXAudioProfile)*profile*`

#### Parameters

*profile*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRoomType:" title="setRoomType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="setAudioProfile:" %}{% endlanying_code_snippet %}
```
### setRoomType:

Set the room type

`- (BMXErrorCode)setRoomType:(BMXRoomType)*type*`

#### Parameters

*type*  
   Room类型  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setStreamRole:" title="setStreamRole:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="setRoomType:" %}{% endlanying_code_snippet %}
```
### setStreamRole:

Set stream operation permissions

`- (BMXErrorCode)setStreamRole:(BMXStreamRole)*role*`

#### Parameters

*role*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setVideoCodec:" title="setVideoCodec:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="setStreamRole:" %}{% endlanying_code_snippet %}
```
### setVideoCodec:

Set video codec

`- (BMXErrorCode)setVideoCodec:(BMXVideoCodec)*codec*`

#### Parameters

*codec*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setVideoProfile:" title="setVideoProfile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="setVideoCodec:" %}{% endlanying_code_snippet %}
```
### setVideoProfile:

Set video codec

`- (BMXErrorCode)setVideoProfile:(BMXVideoConfig *)*videoConfig*`

#### Parameters

*codec*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/startPreviewWithCanvas:" title="startPreviewWithCanvas:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="setVideoProfile:" %}{% endlanying_code_snippet %}
```
### startPreviewWithCanvas:

Start previewing local video

`- (BMXErrorCode)startPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

*canvas*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/startRemoteViewWithCanvas:" title="startRemoteViewWithCanvas:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="startPreviewWithCanvas:" %}{% endlanying_code_snippet %}
```
### startRemoteViewWithCanvas:

Start previewing remote video

`- (BMXErrorCode)startRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

*canvas*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/stopPreviewWithCanvas:" title="stopPreviewWithCanvas:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="startRemoteViewWithCanvas:" %}{% endlanying_code_snippet %}
```
### stopPreviewWithCanvas:

Stop previewing local video

`- (BMXErrorCode)stopPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

*canvas*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/stopRemoteViewWithCanvas:" title="stopRemoteViewWithCanvas:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="stopPreviewWithCanvas:" %}{% endlanying_code_snippet %}
```
### stopRemoteViewWithCanvas:

Stop previewing remote video

`- (BMXErrorCode)stopRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

*canvas*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/subscribeWithStream:" title="subscribeWithStream:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="stopRemoteViewWithCanvas:" %}{% endlanying_code_snippet %}
```
### subscribeWithStream:

Subscribe a stream

`- (BMXErrorCode)subscribeWithStream:(BMXStream *)*stream*`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/switchCamera" title="switchCamera"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="subscribeWithStream:" %}{% endlanying_code_snippet %}
```
### switchCamera

Switch cameras

`- (BMXErrorCode)switchCamera`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unPublishWithType:" title="unPublishWithType:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="switchCamera" %}{% endlanying_code_snippet %}
```
### unPublishWithType:

Unpublish my video and audio streams

`- (BMXErrorCode)unPublishWithType:(BMXVideoMediaType)*type*`

#### Parameters

*type*  
    Stream type

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unSubscribeWithStream:" title="unSubscribeWithStream:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="unPublishWithType:" %}{% endlanying_code_snippet %}
```
### unSubscribeWithStream:

Unsubscribe a stream

`- (BMXErrorCode)unSubscribeWithStream:(BMXStream *)*stream*`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCEngine",function="unSubscribeWithStream:" %}{% endlanying_code_snippet %}
```
