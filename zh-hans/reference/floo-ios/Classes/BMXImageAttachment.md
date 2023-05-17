# BMXImageAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 图片消息附件

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

消息附件强制转换为图像附件

`+ (BMXImageAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   附件  

#### Return Value
BMXImageAttachment

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/clone" title="clone"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="dynamicCastWithAttachment:" %}{% endlanying_code_snippet %}
```
### clone

克隆函数

`- (BMXMessageAttachment *)clone`

#### Return Value
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/initWithData:thumbnailData:imageSize:displayName:conversationId:" title="initWithData:thumbnailData:imageSize:displayName:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="dealloc" %}{% endlanying_code_snippet %}
```
### initWithData:thumbnailData:imageSize:displayName:conversationId:

`- (id)initWithData:(NSData *)*aData* thumbnailData:(NSData *)*thumbnailData* imageSize:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* conversationId:(long long)*conversationId*`

<a name="//api/name/initWithPath:size:" title="initWithPath:size:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="initWithData:thumbnailData:imageSize:displayName:conversationId:" %}{% endlanying_code_snippet %}
```
### initWithPath:size:

`- (id)initWithPath:(NSString *)*path* size:(BMXMessageAttachmentSize *)*size*`

<a name="//api/name/initWithPath:size:displayName:" title="initWithPath:size:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="initWithPath:size:" %}{% endlanying_code_snippet %}
```
### initWithPath:size:displayName:

构造函数，构建发送图片消息附件

`- (id)initWithPath:(NSString *)*path* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   本地路径  

*size*  
   图片的大小，宽度和高度  

*displayName*  
   展示名  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:size:displayName:fileLength:" title="initWithRatelUrl:size:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="initWithPath:size:displayName:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:size:displayName:fileLength:

构造函数，构建接收图片消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*size*  
   图片的大小，宽度和高度  

*displayName*  
   展示名  

*fileLength*  
   文件大小  

*url*  
   图片ratel服务器地址  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setThumbnail:" title="setThumbnail:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="initWithRatelUrl:size:displayName:fileLength:" %}{% endlanying_code_snippet %}
```
### setThumbnail:

设置发送图片消息缩略图

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

*path*  
   本地路径  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/size" title="size"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="setThumbnail:" %}{% endlanying_code_snippet %}
```
### size

图片大小

`- (BMXMessageAttachmentSize *)size`

#### Return Value
<a href="../Classes/BMXMessageAttachmentSize.md">BMXMessageAttachmentSize</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailDownloadStatus" title="thumbnailDownloadStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="size" %}{% endlanying_code_snippet %}
```
### thumbnailDownloadStatus

缩略图下载状态

`- (BMXMessageAttachment_DownloadStatus)thumbnailDownloadStatus`

#### Return Value
<a href="../Constants/BMXMessageAttachment_DownloadStatus.md">BMXMessageAttachment_DownloadStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailPath" title="thumbnailPath"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="thumbnailDownloadStatus" %}{% endlanying_code_snippet %}
```
### thumbnailPath

缩略图本地路径

`- (NSString *)thumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailUrl" title="thumbnailUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="thumbnailPath" %}{% endlanying_code_snippet %}
```
### thumbnailUrl

远程使用缩略图URL

`- (NSString *)thumbnailUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="thumbnailUrl" %}{% endlanying_code_snippet %}
```
### type

返回图片附件类型

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXImageAttachment",function="type" %}{% endlanying_code_snippet %}
```
