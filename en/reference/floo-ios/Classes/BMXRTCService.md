# BMXRTCService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface RTC service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### addDelegate:

Add a RTCService listener

`- (void)addDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRTCServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### addRTCListener:

Add a RTCService listener

`- (void)addRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### getBMXRTCSignalService

Get the RTC signal service

`- (BMXRTCSignalService *)getBMXRTCSignalService`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### getRTCEngine

Get RTC engine

`- (BMXRTCEngine *)getRTCEngine`

#### Return Value

BMXRTCEngine\*

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### removeDelegate:

Remove a RTCService listener

`- (void)removeDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### removeRTCListener:

Remove a RTCService listener

`- (void)removeRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### sendRTCMessageWithMsg:

Send a RTC message

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### sendRTCMessageWithMsg:completion:

Send a RTC message

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### setupRTCEngine:

Initialize the RTC engine

`- (void)setupRTCEngine:(BMXRTCEngine *)*engine*`

#### Parameters

_engine_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>
```
