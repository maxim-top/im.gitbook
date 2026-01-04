# BMXMessageConfig Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 消息配置

## Class Methods

<a name="//api/name/createMessageConfigWithMentionAll:" title="createMessageConfigWithMentionAll:"></a>
### createMessageConfigWithMentionAll:

`+ (BMXMessageConfig *)createMessageConfigWithMentionAll:(BOOL)*mentionAll*`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/addGroupMemberWithMemberId:" title="addGroupMemberWithMemberId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="createMessageConfigWithMentionAll:" %}{% endlanying_code_snippet %}
```
### addGroupMemberWithMemberId:

添加群已读消息的群成员id列表成员

`- (void)addGroupMemberWithMemberId:(long long)*memberId*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearGroupMemberList" title="clearGroupMemberList"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="addGroupMemberWithMemberId:" %}{% endlanying_code_snippet %}
```
### clearGroupMemberList

清空群已读消息的群成员id列表

`- (void)clearGroupMemberList`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="clearGroupMemberList" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/getAndroidConfig" title="getAndroidConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="dealloc" %}{% endlanying_code_snippet %}
```
### getAndroidConfig

获取Android系统配置信息

`- (NSString *)getAndroidConfig`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBadgeCount:" title="getBadgeCount:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getAndroidConfig" %}{% endlanying_code_snippet %}
```
### getBadgeCount:

获取当前的推送消息中badge计数

`- (int)getBadgeCount:(int)*count*`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getBadgeCountType" title="getBadgeCountType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getBadgeCount:" %}{% endlanying_code_snippet %}
```
### getBadgeCountType

获取当前的推送消息中badge计数

`- (BMXMessageConfig_BadgeCountType)getBadgeCountType`

#### Return Value
BadgeCountType

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupMemberList" title="getGroupMemberList"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getBadgeCountType" %}{% endlanying_code_snippet %}
```
### getGroupMemberList

获取需要群已读消息的群成员id列表

`- (ListOfLongLong *)getGroupMemberList`

#### Return Value
<a href="../Classes/ListOfLongLong.md">ListOfLongLong</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getIOSConfig" title="getIOSConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getGroupMemberList" %}{% endlanying_code_snippet %}
```
### getIOSConfig

获取IOS系统配置信息

`- (NSString *)getIOSConfig`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMentionAll" title="getMentionAll"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getIOSConfig" %}{% endlanying_code_snippet %}
```
### getMentionAll

获取是否@全员

`- (BOOL)getMentionAll`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMentionList" title="getMentionList"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getMentionAll" %}{% endlanying_code_snippet %}
```
### getMentionList

获取@成员列表

`- (ListOfLongLong *)getMentionList`

#### Return Value
<a href="../Classes/ListOfLongLong.md">ListOfLongLong</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMentionedMessage" title="getMentionedMessage"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getMentionList" %}{% endlanying_code_snippet %}
```
### getMentionedMessage

获取@消息

`- (NSString *)getMentionedMessage`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushMessage" title="getPushMessage"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getMentionedMessage" %}{% endlanying_code_snippet %}
```
### getPushMessage

获取推送消息

`- (NSString *)getPushMessage`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushShowBeginTime" title="getPushShowBeginTime"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getPushMessage" %}{% endlanying_code_snippet %}
```
### getPushShowBeginTime

获取推送显示开始时间

`- (int)getPushShowBeginTime`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushShowEndTime" title="getPushShowEndTime"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getPushShowBeginTime" %}{% endlanying_code_snippet %}
```
### getPushShowEndTime

获取推送显示结束时间

`- (int)getPushShowEndTime`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getPushTitle" title="getPushTitle"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getPushShowEndTime" %}{% endlanying_code_snippet %}
```
### getPushTitle

获取推送标题

`- (NSString *)getPushTitle`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCAction" title="getRTCAction"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getPushTitle" %}{% endlanying_code_snippet %}
```
### getRTCAction

获得RTC相关操作类型信息（呼叫、接通、挂断等）。

`- (NSString *)getRTCAction`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCCallId" title="getRTCCallId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCAction" %}{% endlanying_code_snippet %}
```
### getRTCCallId

获得RTC相关callId信息。

`- (NSString *)getRTCCallId`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCCallType" title="getRTCCallType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCCallId" %}{% endlanying_code_snippet %}
```
### getRTCCallType

获得RTC相关通话类型（音频通话、视频通话类型）。

`- (BMXMessageConfig_RTCCallType)getRTCCallType`

#### Return Value
RTCCallType

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCInitiator" title="getRTCInitiator"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCCallType" %}{% endlanying_code_snippet %}
```
### getRTCInitiator

获得RTC相关发起者id信息。

`- (long long)getRTCInitiator`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCPin" title="getRTCPin"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCInitiator" %}{% endlanying_code_snippet %}
```
### getRTCPin

获得RTC相关pin码信息。

`- (NSString *)getRTCPin`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCRoomId" title="getRTCRoomId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCPin" %}{% endlanying_code_snippet %}
```
### getRTCRoomId

获得RTC相关房间id信息。

`- (long long)getRTCRoomId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCRoomType" title="getRTCRoomType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCRoomId" %}{% endlanying_code_snippet %}
```
### getRTCRoomType

获得RTC相关房间类型信息。

`- (BMXMessageConfig_RTCRoomType)getRTCRoomType`

#### Return Value
<a href="../Constants/BMXMessageConfig_RTCRoomType.md">BMXMessageConfig_RTCRoomType</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSenderNickname" title="getSenderNickname"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getRTCRoomType" %}{% endlanying_code_snippet %}
```
### getSenderNickname

获取发送者昵称

`- (NSString *)getSenderNickname`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getUsername" title="getUsername"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getSenderNickname" %}{% endlanying_code_snippet %}
```
### getUsername

获得用户名

`- (NSString *)getUsername`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isSilence" title="isSilence"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="getUsername" %}{% endlanying_code_snippet %}
```
### isSilence

获取当前的推送消息是否是静默消息

`- (BOOL)isSilence`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeGroupMemberWithMemberId:" title="removeGroupMemberWithMemberId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="isSilence" %}{% endlanying_code_snippet %}
```
### removeGroupMemberWithMemberId:

清除需要群已读消息的群成员id列表成员

`- (void)removeGroupMemberWithMemberId:(long long)*memberId*`

#### Return Value
<a href="../Classes/ListOfLongLong.md">ListOfLongLong</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/serialize" title="serialize"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="removeGroupMemberWithMemberId:" %}{% endlanying_code_snippet %}
```
### serialize

序列化操作

`- (NSString *)serialize`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAndroidConfig:" title="setAndroidConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="serialize" %}{% endlanying_code_snippet %}
```
### setAndroidConfig:

设置Android系统配置信息
@param androidConfig

`- (void)setAndroidConfig:(NSString *)*androidConfig*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupMemberList:" title="setGroupMemberList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setAndroidConfig:" %}{% endlanying_code_snippet %}
```
### setGroupMemberList:

设置需要群已读消息的群成员id列表
@param groupMemberList

`- (void)setGroupMemberList:(ListOfLongLong *)*groupMemberList*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIOSConfig:" title="setIOSConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setGroupMemberList:" %}{% endlanying_code_snippet %}
```
### setIOSConfig:

设置IOS系统配置信息
@param iosConfig

`- (void)setIOSConfig:(NSString *)*iosConfig*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMentionAll:" title="setMentionAll:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setIOSConfig:" %}{% endlanying_code_snippet %}
```
### setMentionAll:

设置是否@全员
@param mentionAll

`- (void)setMentionAll:(BOOL)*mentionAll*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMentionList:" title="setMentionList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setMentionAll:" %}{% endlanying_code_snippet %}
```
### setMentionList:

设置通知成员id列表
@param mentionList

`- (void)setMentionList:(ListOfLongLong *)*mentionList*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMentionedMessage:" title="setMentionedMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setMentionList:" %}{% endlanying_code_snippet %}
```
### setMentionedMessage:

设置@消息
@param mentionedMessage

`- (void)setMentionedMessage:(NSString *)*mentionedMessage*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushMessage:" title="setPushMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setMentionedMessage:" %}{% endlanying_code_snippet %}
```
### setPushMessage:

设置推送消息
@param pushMessage

`- (void)setPushMessage:(NSString *)*pushMessage*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushShowBeginTime:" title="setPushShowBeginTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setPushMessage:" %}{% endlanying_code_snippet %}
```
### setPushShowBeginTime:

设置推送显示开始时间
@param beginTime

`- (void)setPushShowBeginTime:(int)*beginTime*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushShowEndTime:" title="setPushShowEndTime:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setPushShowBeginTime:" %}{% endlanying_code_snippet %}
```
### setPushShowEndTime:

设置推送显示结束时间
@param endTime

`- (void)setPushShowEndTime:(int)*endTime*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushTitle:" title="setPushTitle:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setPushShowEndTime:" %}{% endlanying_code_snippet %}
```
### setPushTitle:

设置推送标题
@param pushTitle

`- (void)setPushTitle:(NSString *)*pushTitle*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRTCCallInfo:roomId:initiator:roomType:pin:" title="setRTCCallInfo:roomId:initiator:roomType:pin:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setPushTitle:" %}{% endlanying_code_snippet %}
```
### setRTCCallInfo:roomId:initiator:roomType:pin:

设置呼叫消息信息

`- (void)setRTCCallInfo:(BMXMessageConfig_RTCCallType)*calltype* roomId:(long long)*roomId* initiator:(long long)*initiator* roomType:(BMXMessageConfig_RTCRoomType)*roomType* pin:(NSString *)*pin*`

#### Parameters

*calltype*  
   通话类型（语音电话、视频电话）  

*roomId*  
   房间id  

*initiator*  
   发起者id  

*roomType*  
   房间类型（会议模式，直播模式）  

*pin*  
   加入房间的pin码  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRTCHangupInfo:" title="setRTCHangupInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCCallInfo:roomId:initiator:roomType:pin:" %}{% endlanying_code_snippet %}
```
### setRTCHangupInfo:

设置挂断消息信息

`- (void)setRTCHangupInfo:(NSString *)*callId*`

#### Parameters

*callId*  
   通话id  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRTCPickupInfo:" title="setRTCPickupInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCHangupInfo:" %}{% endlanying_code_snippet %}
```
### setRTCPickupInfo:

设置接通消息信息

`- (void)setRTCPickupInfo:(NSString *)*callId*`

#### Parameters

*callId*  
   通话id  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setSenderNickname:" title="setSenderNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCPickupInfo:" %}{% endlanying_code_snippet %}
```
### setSenderNickname:

设置发送者昵称
@param senderNickname

`- (void)setSenderNickname:(NSString *)*senderNickname*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setUsername:" title="setUsername:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setSenderNickname:" %}{% endlanying_code_snippet %}
```
### setUsername:

设置用户名
@param username

`- (void)setUsername:(NSString *)*username*`

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setUsername:" %}{% endlanying_code_snippet %}
```
