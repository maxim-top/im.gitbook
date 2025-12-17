# BMXFileAttachment Class Reference

**Inherits from** [BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 消息文件附件

## Class Methods

### dynamicCastWithAttachment:

消息附件强制转换为文件附件

`+ (BMXFileAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
附件

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

显示名

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

附件下载状态

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

文件长度

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

构造函数，构建发送文件消息附件

`- (id)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
文件的本地路径

_displayName_\
文件展示名

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### initWithRatelUrl:displayName:fileLength:

构造函数，构建接收文件消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
ratel文件服务器地址

_displayName_\
文件展示名

_fileLength_\
文件大小

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>

```

### path

本地路径

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

远程ratel使用URL

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

返回文件类型

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

远程使用URL

`- (NSString *)url`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXFileAttachment'></div>
```
