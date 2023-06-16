# BMXSDKConfigHostConfig Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Server host config

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/dealloc" title="dealloc"></a>
### dealloc

`- (void)dealloc`

<a name="//api/name/getImHost" title="getImHost"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="dealloc" %}{% endlanying_code_snippet %}
```
### getImHost

`- (NSString *)getImHost`

<a name="//api/name/getImPort" title="getImPort"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="getImHost" %}{% endlanying_code_snippet %}
```
### getImPort

`- (int)getImPort`

<a name="//api/name/getRestHost" title="getRestHost"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="getImPort" %}{% endlanying_code_snippet %}
```
### getRestHost

`- (NSString *)getRestHost`

<a name="//api/name/init" title="init"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="getRestHost" %}{% endlanying_code_snippet %}
```
### init

`- (id)init`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="init" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/initWithIm:port:rest:" title="initWithIm:port:rest:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### initWithIm:port:rest:

Constructor

`- (id)initWithIm:(NSString *)*im* port:(int)*port* rest:(NSString *)*rest*`

#### Parameters

*im*  
   Fireplace(IM long link) server IP  

*port*  
   Fireplace server port:w

*rest*  
   Ratel (REST server)base url

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setImHost:" title="setImHost:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="initWithIm:port:rest:" %}{% endlanying_code_snippet %}
```
### setImHost:

`- (void)setImHost:(NSString *)*value*`

<a name="//api/name/setImPort:" title="setImPort:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="setImHost:" %}{% endlanying_code_snippet %}
```
### setImPort:

`- (void)setImPort:(int)*value*`

<a name="//api/name/setRestHost:" title="setRestHost:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="setImPort:" %}{% endlanying_code_snippet %}
```
### setRestHost:

`- (void)setRestHost:(NSString *)*value*`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXSDKConfigHostConfig",function="setRestHost:" %}{% endlanying_code_snippet %}
```
