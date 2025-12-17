# BMXImageAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Image message attachment

## Class Methods

### dynamicCastWithAttachment:

Type casting

`+ (BMXImageAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
The attachment

#### Return Value

BMXImageAttachment

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### clone

`- (BMXMessageAttachment *)clone`

#### Return Value

[BMXMessageAttachment](BMXMessageAttachment.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### initWithData:thumbnailData:imageSize:displayName:conversationId:

`- (id)initWithData:(NSData *)*aData* thumbnailData:(NSData *)*thumbnailData* imageSize:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* conversationId:(long long)*conversationId*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### initWithPath:size:

`- (id)initWithPath:(NSString *)*path* size:(BMXMessageAttachmentSize *)*size*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### initWithPath:size:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
Local file path

_size_\
Width and height of the image

_displayName_\
Attachment name displayed in UI pages

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### initWithRatelUrl:size:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_size_\
Width and height of the image

_displayName_\
Attachment name displayed in UI pages

_fileLength_\
File length

_url_\
Http url

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### setThumbnail:

Set the local path of thumbnail

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

_path_\
Local file path

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### size

Width and height of the image

`- (BMXMessageAttachmentSize *)size`

#### Return Value

[BMXMessageAttachmentSize](BMXMessageAttachmentSize.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### thumbnailDownloadStatus

Downlad status of thumbnail

`- (BMXMessageAttachment_DownloadStatus)thumbnailDownloadStatus`

#### Return Value

[BMXMessageAttachment\_DownloadStatus](../Constants/BMXMessageAttachment_DownloadStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### thumbnailPath

Local path of thumbnail

`- (NSString *)thumbnailPath`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### thumbnailUrl

Http URL of thumbnail

`- (NSString *)thumbnailUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>
```
