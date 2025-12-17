# BMXPushServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol Push service listener

## Instance Methods

### certRetrieved:

Certificate retrieved

`- (void)certRetrieved:(NSString *)*certification*`

#### Parameters

_certification_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### clearedTags:

Push tags cleared

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

_operationId_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### deleteTagsDidFinished:

Push tags deleted

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### getTagsDidFinished:

Get push tags

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushMessageStatusChanged:error:

Push message status changed

`- (void)pushMessageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Parameters

_message_

_error_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushStartDidFinished:

Push service initialized

`- (void)pushStartDidFinished:(NSString *)*bmxToken*`

#### Parameters

_bmxToken_\
bmxToken

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### pushStartDidStopped

Push service stopped

`- (void)pushStartDidStopped`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### receivedPush:

Received push messages

`- (void)receivedPush:(NSArray<BMXMessage*> *)*messages*`

#### Parameters

_messages_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>

```

### setTagsDidFinished:

Push tags has been set

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

_operationId_

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXPushServiceProtocol'></div>
```
