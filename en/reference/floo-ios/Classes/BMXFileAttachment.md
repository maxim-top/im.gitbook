# BMXFileAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface File attachment of messages

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

Type casting

`+ (BMXFileAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   The attachment

#### Return Value
BMXFileAttachment

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

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clone" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/displayName" title="displayName"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### displayName

Attachment name displayed in UI pages.

`- (NSString *)displayName`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadStatus" title="downloadStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="displayName" %}{% endlanying_code_snippet %}
```
### downloadStatus

Download status

`- (BMXMessageAttachment_DownloadStatus)downloadStatus`

#### Return Value
<a href="../Constants/BMXMessageAttachment_DownloadStatus.md">BMXMessageAttachment_DownloadStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fileLength" title="fileLength"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadStatus" %}{% endlanying_code_snippet %}
```
### fileLength

File length

`- (long long)fileLength`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithData:displayName:conversationId:" title="initWithData:displayName:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fileLength" %}{% endlanying_code_snippet %}
```
### initWithData:displayName:conversationId:

`- (id)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* conversationId:(long long)*conversationId*`

<a name="//api/name/initWithPath:" title="initWithPath:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithData:displayName:conversationId:" %}{% endlanying_code_snippet %}
```
### initWithPath:

`- (id)initWithPath:(NSString *)*path*`

<a name="//api/name/initWithPath:displayName:" title="initWithPath:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:" %}{% endlanying_code_snippet %}
```
### initWithPath:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   Local file path

*displayName*  
   Attachment name displayed in UI pages

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:displayName:fileLength:" title="initWithRatelUrl:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:displayName:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*ratelUrl*  
   The file URL on REST server

*displayName*  
   Attachment name displayed in UI pages 

*fileLength*  
   File length  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/path" title="path"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithRatelUrl:displayName:fileLength:" %}{% endlanying_code_snippet %}
```
### path

Local file path

`- (NSString *)path`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ratelUrl" title="ratelUrl"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="path" %}{% endlanying_code_snippet %}
```
### ratelUrl

The file URL on REST server

`- (NSString *)ratelUrl`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ratelUrl" %}{% endlanying_code_snippet %}
```
### type

Attachment type

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/url" title="url"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="type" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="floo-ios",class="",function="url" %}{% endlanying_code_snippet %}
```
