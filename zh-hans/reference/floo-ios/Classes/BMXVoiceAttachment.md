# BMXVoiceAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 音频消息附件

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

消息附件强制转换为语音附件

`+ (BMXVoiceAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   附件  

#### Return Value
BMXVoiceAttachment

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

克隆函数

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

语音时长

`- (int)duration`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithPath:duration:" title="initWithPath:duration:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="duration" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration*`

<a name="//api/name/initWithPath:duration:displayName:" title="initWithPath:duration:displayName:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:duration:" %}{% endlanying_code_snippet %}
```
### initWithPath:duration:displayName:

构造函数，构建发送音频消息附件

`- (id)initWithPath:(NSString *)*path* duration:(int)*duration* displayName:(NSString *)*displayName*`

#### Parameters

*path*  
   文件的本地路径  

*duration*  
   音频时长  

*displayName*  
   文件展示名  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithRatelUrl:duration:displayName:fileLength:" title="initWithRatelUrl:duration:displayName:fileLength:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithPath:duration:displayName:" %}{% endlanying_code_snippet %}
```
### initWithRatelUrl:duration:displayName:fileLength:

构造函数，构建接收音频消息附件

`- (id)initWithRatelUrl:(NSString *)*ratelUrl* duration:(int)*duration* displayName:(NSString *)*displayName* fileLength:(long long)*fileLength*`

#### Parameters

*ratelUrl*  
   ratel文件服务器地址  

*duration*  
   音频时长  

*displayName*  
   文件展示名  

*fileLength*  
   文件大小  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithRatelUrl:duration:displayName:fileLength:" %}{% endlanying_code_snippet %}
```
### type

返回文件类型

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="type" %}{% endlanying_code_snippet %}
```
