# BMXVoiceAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Voice message attachment

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

Type casting

`+ (BMXVoiceAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   The attachment

#### Return Value
BMXVoiceAttachment

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/clone" title="clone"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="dynamicCastWithAttachment:" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/duration" title="duration"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="dealloc" %}{% endlanying_code_snippet %}
```
### duration

Duration of the voice

`- (int)duration`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithPath:duration:" title="initWithPath:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="duration" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration*`

<a name="//api/name/initWithPath:duration:displayName:" title="initWithPath:duration:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="initWithPath:duration:" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:displayName:

Constructor

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   Local file path

*duration*  
   Duration of the voice file

*displayName*  
   Attachment name displayed in UI pages

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:duration:displayName:fileLength:" title="initWithRatelUrl:duration:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="initWithPath:duration:displayName:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:duration:displayName:fileLength:

Constructor

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*ratelUrl*  
   The file URL on REST server

*duration*  
   Duration of the voice file

*displayName*  
   Attachment name displayed in UI pages

*fileLength*  
   File length 

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="initWithRatelUrl:duration:displayName:fileLength:" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVoiceAttachment",function="type" %}{% endlanying_code_snippet %}
```
