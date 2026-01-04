# BMXDevice Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Device information

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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="dealloc" %}{% endlanying_code_snippet %}
```
### deviceSN

Device serial number

`- (int)deviceSN`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="deviceSN" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/isCurrentDevice" title="isCurrentDevice"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### isCurrentDevice

Is the current device

`- (BOOL)isCurrentDevice`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/platform" title="platform"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="isCurrentDevice" %}{% endlanying_code_snippet %}
```
### platform

Client platform

`- (int)platform`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setUserAgent:" title="setUserAgent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="platform" %}{% endlanying_code_snippet %}
```
### setUserAgent:

Set user agent

`- (void)setUserAgent:(NSString *)*userAgent*`

#### Parameters

*userAgent*  
   The user agent  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userAgent" title="userAgent"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="setUserAgent:" %}{% endlanying_code_snippet %}
```
### userAgent

User agent

`- (NSString *)userAgent`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userId" title="userId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="userAgent" %}{% endlanying_code_snippet %}
```
### userId

User ID

`- (long long)userId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXDevice",function="userId" %}{% endlanying_code_snippet %}
```
