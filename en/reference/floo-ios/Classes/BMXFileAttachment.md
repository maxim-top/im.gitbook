# BMXFileAttachment Class Reference

**Inherits from** [BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface File attachment of messages

## Class Methods

### dynamicCastWithAttachment:

Type casting

`+ (BMXFileAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
The attachment

#### Return Value

BMXFileAttachment

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### clone

`- (BMXMessageAttachment *)clone`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### displayName

Attachment name displayed in UI pages.

`- (NSString *)displayName`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### downloadStatus

Download status

`- (BMXMessageAttachment_DownloadStatus)downloadStatus`

#### Return Value

[BMXMessageAttachment\_DownloadStatus](../Constants/BMXMessageAttachment_DownloadStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### fileLength

File length

`- (long long)fileLength`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### initWithData:displayName:conversationId:

`- (id)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* conversationId:(long long)*conversationId*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### initWithPath:

`- (id)initWithPath:(NSString *)*path*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### initWithPath:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
Local file path

_displayName_\
Attachment name displayed in UI pages

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### initWithRatelUrl:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
The file URL on REST server

_displayName_\
Attachment name displayed in UI pages

_fileLength_\
File length

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### path

Local file path

`- (NSString *)path`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### ratelUrl

The file URL on REST server

`- (NSString *)ratelUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### type

Attachment type

`- (BMXMessageAttachment_Type)type`

#### Return Value

[BMXMessageAttachment\_Type](../Constants/BMXMessageAttachment_Type.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### url

Http url

`- (NSString *)url`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>
```
