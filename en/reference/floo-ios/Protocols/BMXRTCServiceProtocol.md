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
### onRTCHangupMessageReceiveWithMsg:

Received a RTC hangup message
@param msg

`- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCMessageStatusChangedWithMsg:error:" title="onRTCMessageStatusChangedWithMsg:error:"></a>
### onRTCMessageStatusChangedWithMsg:error:

A RTC message status changed

`- (void)onRTCMessageStatusChangedWithMsg:(BMXMessage *)*msg* error:(BMXErrorCode)*error*`

#### Parameters

*msg*  

@param error  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onRTCPickupMessageReceiveWithMsg:" title="onRTCPickupMessageReceiveWithMsg:"></a>
### onRTCPickupMessageReceiveWithMsg:

Receive a RTC pickup message
@param msg

`- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage *)*msg*`

#### Declared In
* `floo_proxy.h`

