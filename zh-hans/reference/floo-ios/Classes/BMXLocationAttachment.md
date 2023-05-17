# BMXLocationAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 位置消息附件

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

消息附件强制转换为位置附件

`+ (BMXLocationAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   附件  

#### Return Value
BMXLocationAttachment

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/address" title="address"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="dynamicCastWithAttachment:" %}{% endlanying_code_snippet %}
```
### address

地址

`- (NSString *)address`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clone" title="clone"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="address" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/initWithLatitude:longitude:address:" title="initWithLatitude:longitude:address:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="dealloc" %}{% endlanying_code_snippet %}
```
### initWithLatitude:longitude:address:

构造函数

`- (id)initWithLatitude:(double)*latitude* longitude:(double)*longitude* address:(NSString *)*address*`

#### Parameters

*latitude*  
   纬度  

*longitude*  
   经度  

*address*  
   地址名称  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/latitude" title="latitude"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="initWithLatitude:longitude:address:" %}{% endlanying_code_snippet %}
```
### latitude

纬度

`- (double)latitude`

#### Return Value
double

#### Declared In
* `floo_proxy.h`

<a name="//api/name/longitude" title="longitude"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="latitude" %}{% endlanying_code_snippet %}
```
### longitude

经度

`- (double)longitude`

#### Return Value
double

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="longitude" %}{% endlanying_code_snippet %}
```
### type

返回位置附件类型

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="type" %}{% endlanying_code_snippet %}
```
