# BMXUserProfileMessageSetting Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 用户消息设置
mPushEnabled   当APP未打开时是否允许推送
mPushDetail 是否推送消息详情
mPushNickname 对方收到推送消息时显示的名称
mNotificationSound 收到消息时是否通过声音提醒
mNotificationVibrate 收到消息时是否通过震动提醒
mAutoDownloadAttachment 收到消息时是否自动下载缩略图或者语音
mSilenceStartTime 推送静默起始时间
mSilenceEndTime 推送静默结束时间
mPushStartTime 允许推送起始时间
mPushEndTime 允许推送结束时间

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

<a name="//api/name/getMAutoDownloadAttachment" title="getMAutoDownloadAttachment"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### getMAutoDownloadAttachment

`- (BOOL)getMAutoDownloadAttachment`

<a name="//api/name/getMNotificationSound" title="getMNotificationSound"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMAutoDownloadAttachment" %}{% endlanying_code_snippet %}
```
### getMNotificationSound

`- (BOOL)getMNotificationSound`

<a name="//api/name/getMNotificationVibrate" title="getMNotificationVibrate"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMNotificationSound" %}{% endlanying_code_snippet %}
```
### getMNotificationVibrate

`- (BOOL)getMNotificationVibrate`

<a name="//api/name/getMPushDetail" title="getMPushDetail"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMNotificationVibrate" %}{% endlanying_code_snippet %}
```
### getMPushDetail

`- (BOOL)getMPushDetail`

<a name="//api/name/getMPushEnabled" title="getMPushEnabled"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMPushDetail" %}{% endlanying_code_snippet %}
```
### getMPushEnabled

`- (BOOL)getMPushEnabled`

<a name="//api/name/getMPushEndTime" title="getMPushEndTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMPushEnabled" %}{% endlanying_code_snippet %}
```
### getMPushEndTime

`- (int)getMPushEndTime`

<a name="//api/name/getMPushNickname" title="getMPushNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMPushEndTime" %}{% endlanying_code_snippet %}
```
### getMPushNickname

`- (NSString *)getMPushNickname`

<a name="//api/name/getMPushStartTime" title="getMPushStartTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMPushNickname" %}{% endlanying_code_snippet %}
```
### getMPushStartTime

`- (int)getMPushStartTime`

<a name="//api/name/getMSilenceEndTime" title="getMSilenceEndTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMPushStartTime" %}{% endlanying_code_snippet %}
```
### getMSilenceEndTime

`- (int)getMSilenceEndTime`

<a name="//api/name/getMSilenceStartTime" title="getMSilenceStartTime"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMSilenceEndTime" %}{% endlanying_code_snippet %}
```
### getMSilenceStartTime

`- (int)getMSilenceStartTime`

<a name="//api/name/init" title="init"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMSilenceStartTime" %}{% endlanying_code_snippet %}
```
### init

`- (id)init`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="init" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/setMAutoDownloadAttachment:" title="setMAutoDownloadAttachment:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### setMAutoDownloadAttachment:

`- (void)setMAutoDownloadAttachment:(BOOL)*value*`

<a name="//api/name/setMNotificationSound:" title="setMNotificationSound:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMAutoDownloadAttachment:" %}{% endlanying_code_snippet %}
```
### setMNotificationSound:

`- (void)setMNotificationSound:(BOOL)*value*`

<a name="//api/name/setMNotificationVibrate:" title="setMNotificationVibrate:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMNotificationSound:" %}{% endlanying_code_snippet %}
```
### setMNotificationVibrate:

`- (void)setMNotificationVibrate:(BOOL)*value*`

<a name="//api/name/setMPushDetail:" title="setMPushDetail:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMNotificationVibrate:" %}{% endlanying_code_snippet %}
```
### setMPushDetail:

`- (void)setMPushDetail:(BOOL)*value*`

<a name="//api/name/setMPushEnabled:" title="setMPushEnabled:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMPushDetail:" %}{% endlanying_code_snippet %}
```
### setMPushEnabled:

`- (void)setMPushEnabled:(BOOL)*value*`

<a name="//api/name/setMPushEndTime:" title="setMPushEndTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMPushEnabled:" %}{% endlanying_code_snippet %}
```
### setMPushEndTime:

`- (void)setMPushEndTime:(int)*value*`

<a name="//api/name/setMPushNickname:" title="setMPushNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMPushEndTime:" %}{% endlanying_code_snippet %}
```
### setMPushNickname:

`- (void)setMPushNickname:(NSString *)*value*`

<a name="//api/name/setMPushStartTime:" title="setMPushStartTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMPushNickname:" %}{% endlanying_code_snippet %}
```
### setMPushStartTime:

`- (void)setMPushStartTime:(int)*value*`

<a name="//api/name/setMSilenceEndTime:" title="setMSilenceEndTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMPushStartTime:" %}{% endlanying_code_snippet %}
```
### setMSilenceEndTime:

`- (void)setMSilenceEndTime:(int)*value*`

<a name="//api/name/setMSilenceStartTime:" title="setMSilenceStartTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMSilenceEndTime:" %}{% endlanying_code_snippet %}
```
### setMSilenceStartTime:

`- (void)setMSilenceStartTime:(int)*value*`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMSilenceStartTime:" %}{% endlanying_code_snippet %}
```
