# BMXPushServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol 推送服务监听者

## Instance Methods

### certRetrieved:

Push初始化完成后获取推送证书。

`- (void)certRetrieved:(NSString *)*certification*`

#### Parameters

_certification_\
推送证书

#### Discussion

Push初始化完成后获取推送证书。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### clearedTags:

清空用户推送成功回调。

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

_operationId_\
操作id

#### Discussion

清空用户推送成功回调。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### deleteTagsDidFinished:

删除用户推送标签成功回调

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_\
操作id

#### Discussion

删除用户推送标签成功回调

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### getTagsDidFinished:

获取用户推送标签成功回调。

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_\
操作id

#### Discussion

获取用户推送标签成功回调。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushMessageStatusChanged:error:

发送Push上行消息状态变化通知。

`- (void)pushMessageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Parameters

_message_\
发生状态变化的上行消息

_error_\
状态错误码

#### Discussion

发送Push上行消息状态变化通知。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushStartDidFinished:

Push初始化完成通知。

`- (void)pushStartDidFinished:(NSString *)*bmxToken*`

#### Parameters

_bmxToken_\
bmxToken

#### Discussion

Push初始化完成通知。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushStartDidStopped

Push功能停止通知。

`- (void)pushStartDidStopped`

#### Discussion

Push功能停止通知。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### receivedPush:

接收到新的Push通知

`- (void)receivedPush:(NSArray<BMXMessage*> *)*messages*`

#### Parameters

_messages_\
Push通知列表

#### Discussion

接收到新的Push通知

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### setTagsDidFinished:

设置用户推送标签成功回调。

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_\
操作id

#### Discussion

设置用户推送标签成功回调。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>
```
