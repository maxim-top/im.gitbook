# BMXVideoAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Video message attachment

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

Type casting

`+ (BMXVideoAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   The attachment

#### Return Value
BMXVideoAttachment

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/clone" title="clone"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dynamicCastWithAttachment:" %}{% endlanying_code_snippet %}
```
### clone


`- (BMXMessageAttachment *)clone`

#### Return Value
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clone" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/duration" title="duration"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### duration

Duration of the video

`- (int)duration`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithPath:duration:size:" title="initWithPath:duration:size:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="duration" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:size:

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size*`

<a name="//api/name/initWithPath:duration:size:displayName:" title="initWithPath:duration:size:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:duration:size:" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:size:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   Local file path

*duration*  
   Duration of the video

*size*  
   Width and height of the video

*displayName*  
   Attachment name displayed in UI pages

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithPath:thumbnailPath:duration:size:" title="initWithPath:thumbnailPath:duration:size:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:duration:size:displayName:" %}{% endlanying_code_snippet %}
```
### initWithPath:thumbnailPath:duration:size:

`- (id)initWithPath:(NSString *)*path* thumbnailPath:(NSString *)*thumbnailPath* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size*`

<a name="//api/name/initWithPath:thumbnailPath:duration:size:displayName:" title="initWithPath:thumbnailPath:duration:size:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:thumbnailPath:duration:size:" %}{% endlanying_code_snippet %}
```
### initWithPath:thumbnailPath:duration:size:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* thumbnailPath:(NSString *)*thumbnailPath* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   Local file path

*thumbnailPath*  
   Local file path of thumbnail

*duration*  
   Duration of the video

*size*  
   Width and height of the video 

*displayName*  
   Attachment name displayed in UI pages

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:duration:size:displayName:fileLength:" title="initWithRatelUrl:duration:size:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:thumbnailPath:duration:size:displayName:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:duration:size:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*ratelUrl*  
   The file URL on REST server

*duration*  
   Duration of the video

*size*  
   Width and height of the video

*displayName*  
   Attachment name displayed in UI pages

*fileLength*  
   File length

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:" title="initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithRatelUrl:duration:size:displayName:fileLength:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* thumbnailRatelUrl:(NSString *)*thumbnailRatelUrl* duration:(int)*duration* size:(BMXMessageAttachmentSize *)*size* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*ratelUrl*  
   The file URL on REST server

*thumbnailRatelUrl*  
   The thumbnail URL on REST server

*duration*  
   Duration of the video

*size*  
   Width and height of the video

*displayName*  
   Attachment name displayed in UI pages

*fileLength*  
   File length

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setThumbnail:" title="setThumbnail:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithRatelUrl:thumbnailRatelUrl:duration:size:displayName:fileLength:" %}{% endlanying_code_snippet %}
```
### setThumbnail:

Set thumbnail of video

`- (void)setThumbnail:(NSString *)*path*`

#### Parameters

*path*  
   Local file path 

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setThumbnailRatelUrl:" title="setThumbnailRatelUrl:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setThumbnail:" %}{% endlanying_code_snippet %}
```
### setThumbnailRatelUrl:

Set the thumbnail URL on REST server

`- (void)setThumbnailRatelUrl:(NSString *)*thumbnailRatelUrl*`

#### Parameters

*thumbnailRatelUrl*  
   The thumbnail URL on REST server

#### Declared In
* `floo_proxy.h`

<a name="//api/name/size" title="size"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setThumbnailRatelUrl:" %}{% endlanying_code_snippet %}
```
### size

Width and height of the video

`- (BMXMessageAttachmentSize *)size`

#### Return Value
<a href="../Classes/BMXMessageAttachmentSize.md">BMXMessageAttachmentSize</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailDownloadStatus" title="thumbnailDownloadStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="size" %}{% endlanying_code_snippet %}
```
### thumbnailDownloadStatus

Download status of thumbnail

`- (BMXMessageAttachment_DownloadStatus)thumbnailDownloadStatus`

#### Return Value
DownloadStatus

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailPath" title="thumbnailPath"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="thumbnailDownloadStatus" %}{% endlanying_code_snippet %}
```
### thumbnailPath

Local file path of thumbnail

`- (NSString *)thumbnailPath`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailRatelUrl" title="thumbnailRatelUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="thumbnailPath" %}{% endlanying_code_snippet %}
```
### thumbnailRatelUrl

The thumbnail URL on REST server

`- (NSString *)thumbnailRatelUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/thumbnailUrl" title="thumbnailUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="thumbnailRatelUrl" %}{% endlanying_code_snippet %}
```
### thumbnailUrl

The thumbnail URL on HTTP server

`- (NSString *)thumbnailUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="thumbnailUrl" %}{% endlanying_code_snippet %}
```
### type

Attachment type

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="type" %}{% endlanying_code_snippet %}
```
