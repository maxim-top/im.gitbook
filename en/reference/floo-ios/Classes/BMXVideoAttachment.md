# BMXVideoAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Video message attachment

## Class Methods

### dynamicCastWithAttachment:

Type casting

`+ (BMXVideoAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
The attachment

#### Return Value

BMXVideoAttachment

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### clone

`- (BMXMessageAttachment *)clone`

#### Return Value

[BMXMessageAttachment](BMXMessageAttachment.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### duration

Duration of the video

`- (int)duration`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithPath:duration:size:

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithPath:duration:size:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
Local file path

_duration_\
Duration of the video

_size_\
Width and height of the video

_displayName_\
Attachment name displayed in UI pages

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithPath:thumbnailPath:duration:size:

`- (id)initWithPath:(NSString *)*path* thumbnailPath:(NSString *)*thumbnailPath* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithPath:thumbnailPath:duration:size:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* thumbnailPath:(NSString *)*thumbnailPath* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
Local file path

_thumbnailPath_\
Local file path of thumbnail

_duration_\
Duration of the video

_size_\
Width and height of the video

_displayName_\
Attachment name displayed in UI pages

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithRatelUrl:duration:size:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
The file URL on REST server

_duration_\
Duration of the video

_size_\
Width and height of the video

_displayName_\
Attachment name displayed in UI pages

_fileLength_\
File length

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* thumbnailRatelUrl:(NSString *)*thumbnailRatelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
The file URL on REST server

_thumbnailRatelUrl_\
The thumbnail URL on REST server

_duration_\
Duration of the video

_size_\
Width and height of the video

_displayName_\
Attachment name displayed in UI pages

_fileLength_\
File length

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### setThumbnail:

Set thumbnail of video

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

_path_\
Local file path

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### setThumbnailRatelUrl:

Set the thumbnail URL on REST server

`- (void)setThumbnailRatelUrl:(NSString *)*thumbnailRatelUrl*`

#### Parameters

_thumbnailRatelUrl_\
The thumbnail URL on REST server

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### size

Width and height of the video

`- (BMXMessageAttachmentSize *)size`

#### Return Value

[BMXMessageAttachmentSize](BMXMessageAttachmentSize.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### thumbnailDownloadStatus

Download status of thumbnail

`- (BMXMessageAttachment_DownloadStatus)thumbnailDownloadStatus`

#### Return Value

DownloadStatus

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### thumbnailPath

Local file path of thumbnail

`- (NSString *)thumbnailPath`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### thumbnailRatelUrl

The thumbnail URL on REST server

`- (NSString *)thumbnailRatelUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### thumbnailUrl

The thumbnail URL on HTTP server

`- (NSString *)thumbnailUrl`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>
```
