# BMXRTCServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol RTCService状态监听者

## Instance Methods

### onRTCCallMessageReceiveWithMsg:

接收到通话请求消息 @param msg

`- (void)onRTCCallMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCHangupMessageReceiveWithMsg:

接收到挂断消息 @param msg

`- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCMessageStatusChangedWithMsg:error:

发送信令消息状态变化

`- (void)onRTCMessageStatusChangedWithMsg:(BMXMessage *)*msg* error:(BMXErrorCode)*error*`

#### Parameters

_msg_\
发生变化的信令消息 @param error

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCPickupMessageReceiveWithMsg:

接收到接通消息 @param msg

`- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>
```
