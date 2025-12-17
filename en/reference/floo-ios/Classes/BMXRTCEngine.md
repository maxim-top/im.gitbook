# BMXRTCEngine Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface RTC Engine

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### addDelegate:

Add a RTC engine listener

`- (void)addDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRTCEngineProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### addRTCEngineListener:

`- (void)addRTCEngineListener:(id<BMXRTCEngineProtocol>)*listener*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### destroy

Destroy the RTC engine

`- (void)destroy`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### getRTCConfig

Get RTC config

`- (BMXRTCConfig *)getRTCConfig`

#### Return Value

[BMXRTCConfig](BMXRTCConfig.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### joinRoomWithAuth:

Join a room

`- (BMXErrorCode)joinRoomWithAuth:(BMXRoomAuth *)*auth*`

#### Parameters

_auth_\
Authorization information

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### leaveRoom

Leave a room

`- (BMXErrorCode)leaveRoom`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteLocalAudioWithMute:

Mute or unmute my audio

`- (BMXErrorCode)muteLocalAudioWithMute:(BOOL)*mute*`

#### Parameters

_mute_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteLocalVideoWithType:mute:

Mute or unmute my video

`- (BMXErrorCode)muteLocalVideoWithType:(BMXVideoMediaType)*type* mute:(BOOL)*mute*`

#### Parameters

_type_\
Video media type

_mute_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteRemoteAudioWithStream:mute:

Mute or unmute remote video

`- (BMXErrorCode)muteRemoteAudioWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

_stream_

_mute_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteRemoteVideoWithStream:mute:

Mute or unmute remote video

`- (BMXErrorCode)muteRemoteVideoWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

_stream_

_mute_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### publishWithType:hasVideo:hasAudio:

Publish my video and audio streams

`- (BMXErrorCode)publishWithType:(BMXVideoMediaType)*type* hasVideo:(BOOL)*hasVideo* hasAudio:(BOOL)*hasAudio*`

#### Parameters

_type_\
Stream type

_hasVideo_

_hasAudio_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### removeDelegate:

Remove a RTC engine listener

`- (void)removeDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### removeRTCEngineListener:

`- (void)removeRTCEngineListener:(id<BMXRTCEngineProtocol>)*listener*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setAudioProfile:

Set audio settings

`- (BMXErrorCode)setAudioProfile:(BMXAudioProfile)*profile*`

#### Parameters

_profile_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setRoomType:

Set the room type

`- (BMXErrorCode)setRoomType:(BMXRoomType)*type*`

#### Parameters

_type_\
Room类型

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setStreamRole:

Set stream operation permissions

`- (BMXErrorCode)setStreamRole:(BMXStreamRole)*role*`

#### Parameters

_role_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setVideoCodec:

Set video codec

`- (BMXErrorCode)setVideoCodec:(BMXVideoCodec)*codec*`

#### Parameters

_codec_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setVideoProfile:

Set video codec

`- (BMXErrorCode)setVideoProfile:(BMXVideoConfig *)*videoConfig*`

#### Parameters

_codec_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### startPreviewWithCanvas:

Start previewing local video

`- (BMXErrorCode)startPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### startRemoteViewWithCanvas:

Start previewing remote video

`- (BMXErrorCode)startRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### stopPreviewWithCanvas:

Stop previewing local video

`- (BMXErrorCode)stopPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### stopRemoteViewWithCanvas:

Stop previewing remote video

`- (BMXErrorCode)stopRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### subscribeWithStream:

Subscribe a stream

`- (BMXErrorCode)subscribeWithStream:(BMXStream *)*stream*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### switchCamera

Switch cameras

`- (BMXErrorCode)switchCamera`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### unPublishWithType:

Unpublish my video and audio streams

`- (BMXErrorCode)unPublishWithType:(BMXVideoMediaType)*type*`

#### Parameters

_type_\
Stream type

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### unSubscribeWithStream:

Unsubscribe a stream

`- (BMXErrorCode)unSubscribeWithStream:(BMXStream *)*stream*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>
```
