# BMXVideoAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 视频消息附件

## Class Methods

### dynamicCastWithAttachment:

消息附件强制转换为视频附件

`+ (BMXVideoAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
附件

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

克隆函数

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

视频片段时长

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

构造函数，构建发送视频消息附件

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
文件的本地路径

_duration_\
视频片段时长

_size_\
视频大小，宽度和高度

_displayName_\
文件展示名

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

构造函数，构建发送视频消息附件

`- (id)initWithPath:(NSString *)*path* thumbnailPath:(NSString *)*thumbnailPath* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
文件的本地路径

_thumbnailPath_\
缩略图文件的本地路径

_duration_\
视频片段时长

_size_\
视频大小，宽度和高度

_displayName_\
文件展示名

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithRatelUrl:duration:size:displayName:fileLength:

构造函数，构建接收视频消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
ratel文件服务器地址

_duration_\
视频片段时长

_size_\
视频大小，宽度和高度

_displayName_\
文件展示名

_fileLength_\
文件大小

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:

构造函数，构建接收视频消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* thumbnailRatelUrl:(NSString *)*thumbnailRatelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
ratel文件服务器地址

_thumbnailRatelUrl_\
缩略图ratel文件服务器地址

_duration_\
视频片段时长

_size_\
视频大小，宽度和高度

_displayName_\
文件展示名

_fileLength_\
文件大小

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### setThumbnail:

设置发送视频片段消息缩略图

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

_path_\
视频片段消息缩略图

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### setThumbnailRatelUrl:

设置发送视频片段消息缩略图ratel服务器路径

`- (void)setThumbnailRatelUrl:(NSString *)*thumbnailRatelUrl*`

#### Parameters

_thumbnailRatelUrl_\
视频片段消息缩略图服务器路径

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>

```

### size

视频大小，宽度和高度

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

缩略图下载状态

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

缩略图本地路径

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

缩略图ratel服务器路径

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

远程缩略图使用URL

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

返回文件类型

`- (BMXMessageAttachment_Type)type`

#### Return Value

[BMXMessageAttachment\_Type](../Constants/BMXMessageAttachment_Type.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVideoAttachment'></div>
```
