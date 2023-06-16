# BMXLocationAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
<a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Location message attachment

## Class Methods

<a name="//api/name/dynamicCastWithAttachment:" title="dynamicCastWithAttachment:"></a>
### dynamicCastWithAttachment:

Type casting

`+ (BMXLocationAttachment *)dynamicCastWithAttachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*attachment*  
   The attachment  

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

The address

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

Constructor

`- (id)initWithLatitude:(double)*latitude* longitude:(double)*longitude* address:(NSString *)*address*`

#### Parameters

*latitude*    

*longitude*  

*address*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/latitude" title="latitude"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="initWithLatitude:longitude:address:" %}{% endlanying_code_snippet %}
```
### latitude

The latitude

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

The longitude

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

Attachment type

`- (BMXMessageAttachment_Type)type`

#### Return Value
<a href="../Constants/BMXMessageAttachment_Type.md">BMXMessageAttachment_Type</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="type" %}{% endlanying_code_snippet %}
```
