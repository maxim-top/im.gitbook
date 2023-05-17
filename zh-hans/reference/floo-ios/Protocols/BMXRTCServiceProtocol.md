# BMXRTCServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol RTCService状态监听者

## Instance Methods

<a name="//api/name/onRTCCallMessageReceiveWithMsg:" title="onRTCCallMessageReceiveWithMsg:"></a>
### onRTCCallMessageReceiveWithMsg:

接收到通话请求消息
@param msg

`- (void)onRTCCallMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCHangupMessageReceiveWithMsg:" title="onRTCHangupMessageReceiveWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCCallMessageReceiveWithMsg:" %}{% endlanying_code_snippet %}
```
### onRTCHangupMessageReceiveWithMsg:

接收到挂断消息
@param msg

`- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCMessageStatusChangedWithMsg:error:" title="onRTCMessageStatusChangedWithMsg:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCHangupMessageReceiveWithMsg:" %}{% endlanying_code_snippet %}
```
### onRTCMessageStatusChangedWithMsg:error:

发送信令消息状态变化

`- (void)onRTCMessageStatusChangedWithMsg:(BMXMessage *)*msg* error:(BMXErrorCode)*error*`

#### Parameters

*msg*  
   发生变化的信令消息
@param error  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCPickupMessageReceiveWithMsg:" title="onRTCPickupMessageReceiveWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCMessageStatusChangedWithMsg:error:" %}{% endlanying_code_snippet %}
```
### onRTCPickupMessageReceiveWithMsg:

接收到接通消息
@param msg

`- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCPickupMessageReceiveWithMsg:" %}{% endlanying_code_snippet %}
```
