# BMXPushService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Push Service

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/bindDeviceTokenWithToken:" title="bindDeviceTokenWithToken:"></a>
### bindDeviceTokenWithToken:

Bind device token for push service

`- (BMXErrorCode)bindDeviceTokenWithToken:(NSString *)*token*`

#### Parameters

*token*  
   Device token  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/bindVoipTokenWithToken:" title="bindVoipTokenWithToken:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="bindDeviceTokenWithToken:" %}{% endlanying_code_snippet %}
```
### bindVoipTokenWithToken:

Bind VOIP device token for push service

`- (BMXErrorCode)bindVoipTokenWithToken:(NSString *)*token*`

#### Parameters

*token*  
   Device token  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearAllNotifications" title="clearAllNotifications"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="bindVoipTokenWithToken:" %}{% endlanying_code_snippet %}
```
### clearAllNotifications

Clear all notifications on the notification bar

`- (void)clearAllNotifications`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearNotificationWithNotificationId:" title="clearNotificationWithNotificationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clearAllNotifications" %}{% endlanying_code_snippet %}
```
### clearNotificationWithNotificationId:

Clear a notification by ID

`- (void)clearNotificationWithNotificationId:(long long)*notificationId*`

#### Parameters

*notificationId*  
   Notification ID

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearTagsWithOperationId:" title="clearTagsWithOperationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clearNotificationWithNotificationId:" %}{% endlanying_code_snippet %}
```
### clearTagsWithOperationId:

Clear tags by operation ID

`- (BMXErrorCode)clearTagsWithOperationId:(NSString *)*operationId*`

#### Parameters

*operationId*  
    Operation ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clearTagsWithOperationId:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteTagsWithTags:operationId:" title="deleteTagsWithTags:operationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteTagsWithTags:operationId:

Remove tags by operation ID

`- (BMXErrorCode)deleteTagsWithTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
    tags

*operationId*  
    Operation ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getCert" title="getCert"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteTagsWithTags:operationId:" %}{% endlanying_code_snippet %}
```
### getCert

Get the push service certificate

`- (NSString *)getCert`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushProfile:forceRefresh:" title="getPushProfile:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getCert" %}{% endlanying_code_snippet %}
```
### getPushProfile:forceRefresh:

Get the profile of push user

`- (BMXErrorCode)getPushProfile:(BMXPushUserProfile *)*pushProfile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getTags:operationId:" title="getTags:operationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getPushProfile:forceRefresh:" %}{% endlanying_code_snippet %}
```
### getTags:operationId:

Get tags of push user

`- (BMXErrorCode)getTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
    Tag list

*operationId*  
    Operation ID

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getToken" title="getToken"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getTags:operationId:" %}{% endlanying_code_snippet %}
```
### getToken

Get access token

`- (NSString *)getToken`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getToken" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/loadLocalPushMessagesWithRefMsgId:size:result:" title="loadLocalPushMessagesWithRefMsgId:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### loadLocalPushMessagesWithRefMsgId:size:result:

`- (BMXErrorCode)loadLocalPushMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

<a name="//api/name/loadLocalPushMessagesWithRefMsgId:size:result:arg4:" title="loadLocalPushMessagesWithRefMsgId:size:result:arg4:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadLocalPushMessagesWithRefMsgId:size:result:" %}{% endlanying_code_snippet %}
```
### loadLocalPushMessagesWithRefMsgId:size:result:arg4:

Load push messages in local db

`- (BMXErrorCode)loadLocalPushMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXPushService_PushDirection)*arg4*`

#### Parameters

*refMsgId*  
   First Message Id

*size*  
   Message list as result

*arg4*  
   Search direction, Up for earlier

#### Declared In
* `floo_proxy.h`

<a name="//api/name/resume" title="resume"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadLocalPushMessagesWithRefMsgId:size:result:arg4:" %}{% endlanying_code_snippet %}
```
### resume

Resume push function

`- (BMXErrorCode)resume`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithContent:" title="sendMessageWithContent:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="resume" %}{% endlanying_code_snippet %}
```
### sendMessageWithContent:

Send a push message

`- (void)sendMessageWithContent:(NSString *)*content*`

#### Parameters

*content*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setBadge:" title="setBadge:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sendMessageWithContent:" %}{% endlanying_code_snippet %}
```
### setBadge:

Set badge count

`- (BMXErrorCode)setBadge:(int)*count*`

#### Parameters

*count*  
    Badge count

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGeoFenceMode" title="setGeoFenceMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setBadge:" %}{% endlanying_code_snippet %}
```
### setGeoFenceMode

`- (BMXErrorCode)setGeoFenceMode`

<a name="//api/name/setGeoFenceMode:" title="setGeoFenceMode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### setGeoFenceMode:

`- (BMXErrorCode)setGeoFenceMode:(BOOL)*enable*`

<a name="//api/name/setGeoFenceMode:isAllow:" title="setGeoFenceMode:isAllow:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGeoFenceMode:" %}{% endlanying_code_snippet %}
```
### setGeoFenceMode:isAllow:

Set geo-fencing mode

`- (BMXErrorCode)setGeoFenceMode:(BOOL)*enable* isAllow:(BOOL)*isAllow*`

#### Parameters

*enable*  
    Enable the feature

*isAllow*  
    Does the user allow

#### Return Value  
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushMode" title="setPushMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGeoFenceMode:isAllow:" %}{% endlanying_code_snippet %}
```

### setPushMode:

Set whether push is allowed

`- (BMXErrorCode)setPushMode:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushTime:endHour:" title="setPushTime:endHour:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setPushMode:" %}{% endlanying_code_snippet %}
```
### setPushTime:endHour:

`- (BMXErrorCode)setPushTime:(int)*startHour* endHour:(int)*endHour*`

<a name="//api/name/setRunBackgroundMode" title="setRunBackgroundMode"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setPushTime:endHour:" %}{% endlanying_code_snippet %}
```
### setRunBackgroundMode

`- (BMXErrorCode)setRunBackgroundMode`

<a name="//api/name/setRunBackgroundMode:" title="setRunBackgroundMode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setRunBackgroundMode" %}{% endlanying_code_snippet %}
```
### setRunBackgroundMode:

Set whether push is allowed to run in the background

`- (BMXErrorCode)setRunBackgroundMode:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setSilenceTime:endHour:" title="setSilenceTime:endHour:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setRunBackgroundMode:" %}{% endlanying_code_snippet %}
```
### setSilenceTime:endHour:

Set the silence time range for the push service

`- (BMXErrorCode)setSilenceTime:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

*startHour*  

*endHour*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setTags:operationId:" title="setTags:operationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setSilenceTime:endHour:" %}{% endlanying_code_snippet %}
```
### setTags:operationId:

Set tags for push service

`- (BMXErrorCode)setTags:(TagList *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  

*operationId*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/start" title="start"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setTags:operationId:" %}{% endlanying_code_snippet %}
```
### start

`- (BMXErrorCode)start`

<a name="//api/name/startWithAlias:" title="startWithAlias:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="start" %}{% endlanying_code_snippet %}
```
### startWithAlias:

`- (BMXErrorCode)startWithAlias:(NSString *)*alias*`

<a name="//api/name/startWithAlias:bmxToken:" title="startWithAlias:bmxToken:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="startWithAlias:" %}{% endlanying_code_snippet %}
```
### startWithAlias:bmxToken:

Start push service

`- (BMXErrorCode)startWithAlias:(NSString *)*alias* bmxToken:(NSString *)*bmxToken*`

#### Parameters

*alias*  
    User alias for push service

*bmxToken*  
    User access token

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/status" title="status"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="startWithAlias:bmxToken:" %}{% endlanying_code_snippet %}
```
### status

The status of push SDK

`- (BMXPushService_PushSdkStatus)status`

#### Return Value
<a href="../Constants/BMXPushService_PushSdkStatus.md">BMXPushService_PushSdkStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/stop" title="stop"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="status" %}{% endlanying_code_snippet %}
```
### stop

Stop push service

`- (BMXErrorCode)stop`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unbindAliasWithAlias:" title="unbindAliasWithAlias:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="stop" %}{% endlanying_code_snippet %}
```
### unbindAliasWithAlias:

Unbind user alias

`- (BMXErrorCode)unbindAliasWithAlias:(NSString *)*alias*`

#### Parameters

*alias*  
    User alias

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unbindAliasWithAlias:" %}{% endlanying_code_snippet %}
```
