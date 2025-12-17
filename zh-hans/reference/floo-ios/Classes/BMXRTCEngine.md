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

添加聊天监听者

`- (void)addDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

_listener_\
聊天监听者

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

销毁音视频Engine

`- (void)destroy`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### getRTCConfig

获取RTC设置

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

加入频道

`- (BMXErrorCode)joinRoomWithAuth:(BMXRoomAuth *)*auth*`

#### Parameters

_auth_\
加入频道时的认证信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### leaveRoom

离开频道

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

打开关闭本地音频

`- (BMXErrorCode)muteLocalAudioWithMute:(BOOL)*mute*`

#### Parameters

_mute_\
true为打开，false为关闭

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteLocalVideoWithType:mute:

打开关闭本地视频

`- (BMXErrorCode)muteLocalVideoWithType:(BMXVideoMediaType)*type* mute:(BOOL)*mute*`

#### Parameters

_type_\
视频流类型

_mute_\
true为打开，false为关闭

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteRemoteAudioWithStream:mute:

打开关闭远端音频

`- (BMXErrorCode)muteRemoteAudioWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

_stream_\
远端流

_mute_\
true为打开，false为关闭

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### muteRemoteVideoWithStream:mute:

打开关闭远端视频

`- (BMXErrorCode)muteRemoteVideoWithStream:(BMXStream *)*stream* mute:(BOOL)*mute*`

#### Parameters

_stream_\
远端流

_mute_\
true为打开，false为关闭

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### publishWithType:hasVideo:hasAudio:

发布流信息

`- (BMXErrorCode)publishWithType:(BMXVideoMediaType)*type* hasVideo:(BOOL)*hasVideo* hasAudio:(BOOL)*hasAudio*`

#### Parameters

_type_\
流媒体类型

_hasVideo_\
是否存在视频流

_hasAudio_\
是否存在音频流

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### removeDelegate:

移除聊天监听者

`- (void)removeDelegate:(id<BMXRTCEngineProtocol>)*aDelegate*`

#### Parameters

_listener_\
聊天监听者

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

设置音频编码格式

`- (BMXErrorCode)setAudioProfile:(BMXAudioProfile)*profile*`

#### Parameters

_profile_\
音频编码格式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setRoomType:

设置Room的类型

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

设置流操作权限

`- (BMXErrorCode)setStreamRole:(BMXStreamRole)*role*`

#### Parameters

_role_\
操作权限，推流、拉流、推拉流。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setVideoCodec:

设置视频编码格式类型

`- (BMXErrorCode)setVideoCodec:(BMXVideoCodec)*codec*`

#### Parameters

_codec_\
VP8编码、H264编码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### setVideoProfile:

设置视频编码格式类型

`- (BMXErrorCode)setVideoProfile:(BMXVideoConfig *)*videoConfig*`

#### Parameters

_codec_\
VP8编码、H264编码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### startPreviewWithCanvas:

开启本地渲染

`- (BMXErrorCode)startPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_\
画布属性信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### startRemoteViewWithCanvas:

开启远端渲染

`- (BMXErrorCode)startRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_\
画布属性信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### stopPreviewWithCanvas:

停止本地渲染

`- (BMXErrorCode)stopPreviewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_\
画布属性信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### stopRemoteViewWithCanvas:

停止远端渲染

`- (BMXErrorCode)stopRemoteViewWithCanvas:(BMXVideoCanvas *)*canvas*`

#### Parameters

_canvas_\
画布属性信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### subscribeWithStream:

订阅流信息

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

切换摄像头

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

停止发布流

`- (BMXErrorCode)unPublishWithType:(BMXVideoMediaType)*type*`

#### Parameters

_type_\
流媒体类型

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>

```

### unSubscribeWithStream:

停止订阅流

`- (BMXErrorCode)unSubscribeWithStream:(BMXStream *)*stream*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCEngine'></div>
```
