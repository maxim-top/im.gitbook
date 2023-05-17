# BMXRTCServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol RTCService listener

## Instance Methods

<a name="//api/name/onRTCCallMessageReceiveWithMsg:" title="onRTCCallMessageReceiveWithMsg:"></a>
### onRTCCallMessageReceiveWithMsg:

Received a RTC call message
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

Received a RTC hangup message
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

A RTC message status changed

`- (void)onRTCMessageStatusChangedWithMsg:(BMXMessage *)*msg* error:(BMXErrorCode)*error*`

#### Parameters

*msg*  

@param error  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCPickupMessageReceiveWithMsg:" title="onRTCPickupMessageReceiveWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCMessageStatusChangedWithMsg:error:" %}{% endlanying_code_snippet %}
```
### onRTCPickupMessageReceiveWithMsg:

Receive a RTC pickup message
@param msg

`- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCServiceProtocol",function="onRTCPickupMessageReceiveWithMsg:" %}{% endlanying_code_snippet %}
```
