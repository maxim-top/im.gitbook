# BMXGroupMember Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 群成员

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

<a name="//api/name/getMAvatar" title="getMAvatar"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="dealloc" %}{% endlanying_code_snippet %}
```
### getMAvatar

获取群成员头像

`- (NSString *)getMAvatar`

<a name="//api/name/getMCreateTime" title="getMCreateTime"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMAvatar" %}{% endlanying_code_snippet %}
```
### getMCreateTime

`- (long long)getMCreateTime`

<a name="//api/name/getMGroupNickname" title="getMGroupNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMCreateTime" %}{% endlanying_code_snippet %}
```
### getMGroupNickname

`- (NSString *)getMGroupNickname`

<a name="//api/name/getMNickname" title="getMNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMGroupNickname" %}{% endlanying_code_snippet %}
```
### getMNickname

获取群成员昵称

`- (NSString *)getMNickname`

<a name="//api/name/getMUid" title="getMUid"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMNickname" %}{% endlanying_code_snippet %}
```
### getMUid

`- (long long)getMUid`

<a name="//api/name/getMUsername" title="getMUsername"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMUid" %}{% endlanying_code_snippet %}
```
### getMUsername

获取群成员用户名

`- (NSString *)getMUsername`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="getMUsername" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/initWithUid:nickname:createTime:" title="initWithUid:nickname:createTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### initWithUid:nickname:createTime:

`- (id)initWithUid:(long long)*uid* nickname:(NSString *)*nickname* createTime:(long long)*createTime*`

<a name="//api/name/setMAvatar:" title="setMAvatar:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="initWithUid:nickname:createTime:" %}{% endlanying_code_snippet %}
```
### setMAvatar:

设置群成员头像

`- (void)setMAvatar:(NSString *)*value*`

<a name="//api/name/setMCreateTime:" title="setMCreateTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMAvatar:" %}{% endlanying_code_snippet %}
```
### setMCreateTime:

`- (void)setMCreateTime:(long long)*value*`

<a name="//api/name/setMGroupNickname:" title="setMGroupNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMCreateTime:" %}{% endlanying_code_snippet %}
```
### setMGroupNickname:

`- (void)setMGroupNickname:(NSString *)*value*`

<a name="//api/name/setMNickname:" title="setMNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMGroupNickname:" %}{% endlanying_code_snippet %}
```
### setMNickname:

设置群成员昵称

`- (void)setMNickname:(NSString *)*value*`

<a name="//api/name/setMUid:" title="setMUid:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMNickname:" %}{% endlanying_code_snippet %}
```
### setMUid:

`- (void)setMUid:(long long)*value*`

<a name="//api/name/setMUsername:" title="setMUsername:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMUid:" %}{% endlanying_code_snippet %}
```
### setMUsername:

设置群成员用户名

`- (void)setMUsername:(NSString *)*value*`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXGroupMember",function="setMUsername:" %}{% endlanying_code_snippet %}
```
