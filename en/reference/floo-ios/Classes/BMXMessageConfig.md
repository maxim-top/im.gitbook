# BMXMessageConfig Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Message config

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

Add ID list of group members who read the message

`- (void)addGroupMemberWithMemberId:(long long)*memberId*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearGroupMemberList" title="clearGroupMemberList"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="addGroupMemberWithMemberId:" %}{% endlanying_code_snippet %}
```
### clearGroupMemberList

Clear the ID list of group members who read the message

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

Get config for Android

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

Get the badge count in the current push message

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

Get the badge count type in the current push message

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

Get group members of the message

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

Get message config for iOS

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

Get whether to mention all members

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

Get a list of members to be mentioned 

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

Get mentioned message

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

Get push message

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

Get push begin time

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

Get push end time

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

Get push title

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

Get RTC action (call, pickup, hang up, etc.)

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

Get RTC call ID

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

Get RTC call type(Audio|Video)

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

Caller ID

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

Get RTC call pin code

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

Get RTC room ID

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

Get RTC room type

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

Get sender nickname

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

Get user name

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

Is the push message silent

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

Remove the ID list of group members who read the message

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

Set message config for android device
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

Set the ID list of group members who should read the message
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

Set message config for iOS device
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

Set whether to mention all members
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

Set mentioned member list
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

Set mentioned message
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

Set push message
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

Set push begin time
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

Set push end time
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

Set push title
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

Set RTC call info

`- (void)setRTCCallInfo:(BMXMessageConfig_RTCCallType)*calltype* roomId:(long long)*roomId* initiator:(long long)*initiator* roomType:(BMXMessageConfig_RTCRoomType)*roomType* pin:(NSString *)*pin*`

#### Parameters

*calltype*  
    RTC call type

*roomId*  

*initiator*  

*roomType*  
    meeting or streaming

*pin*  
    RTC call pin code

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRTCHangupInfo:" title="setRTCHangupInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCCallInfo:roomId:initiator:roomType:pin:" %}{% endlanying_code_snippet %}
```
### setRTCHangupInfo:

Set RTC call hang up information

`- (void)setRTCHangupInfo:(NSString *)*callId*`

#### Parameters

*callId*  
    RTC call ID

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setRTCPickupInfo:" title="setRTCPickupInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCHangupInfo:" %}{% endlanying_code_snippet %}
```
### setRTCPickupInfo:

Set RTC pickup information

`- (void)setRTCPickupInfo:(NSString *)*callId*`

#### Parameters

*callId*  
    RTC call ID

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setSenderNickname:" title="setSenderNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setRTCPickupInfo:" %}{% endlanying_code_snippet %}
```
### setSenderNickname:

Set sender nickname
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

Set username
@param username

`- (void)setUsername:(NSString *)*username*`

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessageConfig",function="setUsername:" %}{% endlanying_code_snippet %}
```
