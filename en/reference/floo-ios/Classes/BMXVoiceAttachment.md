# BMXVoiceAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Voice message attachment

## Class Methods

### dynamicCastWithAttachment:

Type casting

`+ (BMXVoiceAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
The attachment

#### Return Value

BMXVoiceAttachment

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### clone

`- (BMXMessageAttachment *)clone`

#### Return Value

[BMXMessageAttachment](BMXMessageAttachment.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### duration

Duration of the voice

`- (int)duration`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### initWithPath:duration:

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### initWithPath:duration:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
Local file path

_duration_\
Duration of the voice file

_displayName_\
Attachment name displayed in UI pages

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### initWithRatelUrl:duration:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
The file URL on REST server

_duration_\
Duration of the voice file

_displayName_\
Attachment name displayed in UI pages

_fileLength_\
File length

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>
```
