# BMXVoiceAttachment Class Reference

**Inherits from** [BMXFileAttachment](BMXFileAttachment.md) :\
[BMXMessageAttachment](BMXMessageAttachment.md) :\
[BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 音频消息附件

## Class Methods

### dynamicCastWithAttachment:

消息附件强制转换为语音附件

`+ (BMXVoiceAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_attachment_\
附件

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

克隆函数

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

语音时长

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

构造函数，构建发送音频消息附件

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* displayName:(NSString *)*displayName*`

#### Parameters

_path_\
文件的本地路径

_duration_\
音频时长

_displayName_\
文件展示名

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

```

### initWithRatelUrl:duration:displayName:fileLength:

构造函数，构建接收音频消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

_ratelUrl_\
ratel文件服务器地址

_duration_\
音频时长

_displayName_\
文件展示名

_fileLength_\
文件大小

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXVoiceAttachment'></div>
```
