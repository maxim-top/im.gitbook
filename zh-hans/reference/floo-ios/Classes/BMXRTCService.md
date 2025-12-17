# BMXRTCService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface RTC服务

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### addDelegate:

添加RTCService回调监听

`- (void)addDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
RTCService监听器

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

添加RTCService回调监听

`- (void)addRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

_listener_\
RTCService监听器

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

获取BMXRTCSignalService的信令服务service（只有BMXRTCEngine需要使用该信令service，第三方RTCEngine对象不需要）

`- (BMXRTCSignalService *)getBMXRTCSignalService`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### getRTCEngine

获取存储的engine对象实例

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

移除RTCService回调监听

`- (void)removeDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
RTCService监听器

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### removeRTCListener:

移除RTCService回调监听

`- (void)removeRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

_listener_\
RTCService监听器

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### sendRTCMessageWithMsg:

发送消息，用来RTCService层进行交互信令发送的操作。

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
发送的信息消息，消息的类型仅为信令消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### sendRTCMessageWithMsg:completion:

发送消息，用来RTCService层进行交互信令发送的操作。

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
发送的信息消息，消息的类型仅为信令消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>

```

### setupRTCEngine:

初始化并存储engine对象实例

`- (void)setupRTCEngine:(BMXRTCEngine *)*engine*`

#### Parameters

_engine_\
BMXRTCEngine对象实例指针

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRTCService'></div>
```
