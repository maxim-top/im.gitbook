# BMXPushUserProfile Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Push用户Profile

## Instance Methods

<a name="//api/name/dealloc" title="dealloc"></a>
### dealloc

`- (void)dealloc`

<a name="//api/name/messagePushSetting" title="messagePushSetting"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushUserProfile",function="dealloc" %}{% endlanying_code_snippet %}
```
### messagePushSetting

推送用户消息设定

`- (BMXPushUserProfileMessagePushSetting *)messagePushSetting`

#### Return Value
<a href="../Classes/BMXPushUserProfileMessagePushSetting.md">BMXPushUserProfileMessagePushSetting</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushAlias" title="pushAlias"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushUserProfile",function="messagePushSetting" %}{% endlanying_code_snippet %}
```
### pushAlias

推送用户别名

`- (NSString *)pushAlias`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushToken" title="pushToken"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushUserProfile",function="pushAlias" %}{% endlanying_code_snippet %}
```
### pushToken

推送用户token

`- (NSString *)pushToken`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/userId" title="userId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushUserProfile",function="pushToken" %}{% endlanying_code_snippet %}
```
### userId

用户ID（唯一）

`- (long long)userId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushUserProfile",function="userId" %}{% endlanying_code_snippet %}
```
