# BMXDevice Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 设备信息

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

<a name="//api/name/deviceSN" title="deviceSN"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### deviceSN

设备序列号

`- (int)deviceSN`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deviceSN" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/isCurrentDevice" title="isCurrentDevice"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### isCurrentDevice

是否是当前设备

`- (BOOL)isCurrentDevice`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/platform" title="platform"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isCurrentDevice" %}{% endlanying_code_snippet %}
```
### platform

软件平台

`- (int)platform`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setUserAgent:" title="setUserAgent:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="platform" %}{% endlanying_code_snippet %}
```
### setUserAgent:

设置用户代理信息

`- (void)setUserAgent:(NSString *)*userAgent*`

#### Parameters

*userAgent*  
   用户代理信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userAgent" title="userAgent"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setUserAgent:" %}{% endlanying_code_snippet %}
```
### userAgent

用户代理信息

`- (NSString *)userAgent`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userId" title="userId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="userAgent" %}{% endlanying_code_snippet %}
```
### userId

用户id

`- (long long)userId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="userId" %}{% endlanying_code_snippet %}
```
