# BMXRTCServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol RTCService listener

## Instance Methods

### onRTCCallMessageReceiveWithMsg:

Received a RTC call message @param msg

`- (void)onRTCCallMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCHangupMessageReceiveWithMsg:

Received a RTC hangup message @param msg

`- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCMessageStatusChangedWithMsg:error:

A RTC message status changed

`- (void)onRTCMessageStatusChangedWithMsg:(BMXMessage *)*msg* error:(BMXErrorCode)*error*`

#### Parameters

_msg_

@param error

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>

```

### onRTCPickupMessageReceiveWithMsg:

Receive a RTC pickup message @param msg

`- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCServiceProtocol'></div>
```
