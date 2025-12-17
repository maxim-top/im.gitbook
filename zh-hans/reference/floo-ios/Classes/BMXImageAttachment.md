# BMXImageAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 图片消息附件

## Class Methods

### dynamicCastWithAttachment:

消息附件强制转换为图像附件

`+ (BMXImageAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
附件

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

克隆函数

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

构造函数，构建发送图片消息附件

`- (id)initWithPath:(NSString *)*path* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
本地路径

_size_\
图片的大小，宽度和高度

_displayName_\
展示名

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### initWithRatelUrl:size:displayName:fileLength:

构造函数，构建接收图片消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_size_\
图片的大小，宽度和高度

_displayName_\
展示名

_fileLength_\
文件大小

_url_\
图片ratel服务器地址

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### setThumbnail:

设置发送图片消息缩略图

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

_path_\
本地路径

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>

```

### size

图片大小

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

缩略图下载状态

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

缩略图本地路径

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

远程使用缩略图URL

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

返回图片附件类型

`- (BMXMessageAttachment_Type)type`

#### Return Value

[BMXMessageAttachment\_Type](../Constants/BMXMessageAttachment_Type.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXImageAttachment'></div>
```
