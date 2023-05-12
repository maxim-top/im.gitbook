# BMXPushUserProfile Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Push User Profile

## Instance Methods

<a name="//api/name/dealloc" title="dealloc"></a>
### dealloc

`- (void)dealloc`

<a name="//api/name/messagePushSetting" title="messagePushSetting"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### messagePushSetting

Push settings for the user

`- (BMXPushUserProfileMessagePushSetting *)messagePushSetting`

#### Return Value
<a href="../Classes/BMXPushUserProfileMessagePushSetting.md">BMXPushUserProfileMessagePushSetting</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushAlias" title="pushAlias"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="messagePushSetting" %}{% endlanying_code_snippet %}
```
### pushAlias

Push user alias

`- (NSString *)pushAlias`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushToken" title="pushToken"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="pushAlias" %}{% endlanying_code_snippet %}
```
### pushToken

Push token

`- (NSString *)pushToken`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userId" title="userId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="pushToken" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="floo-ios",class="",function="userId" %}{% endlanying_code_snippet %}
```
