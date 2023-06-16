# BMXRTCService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface RTC服务

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

添加RTCService回调监听

`- (void)addDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
   RTCService监听器  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRTCServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addRTCListener:" title="addRTCListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### addRTCListener:

添加RTCService回调监听

`- (void)addRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

*listener*  
   RTCService监听器  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="addRTCListener:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/getBMXRTCSignalService" title="getBMXRTCSignalService"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="dealloc" %}{% endlanying_code_snippet %}
```
### getBMXRTCSignalService

获取BMXRTCSignalService的信令服务service（只有BMXRTCEngine需要使用该信令service，第三方RTCEngine对象不需要）

`- (BMXRTCSignalService *)getBMXRTCSignalService`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getRTCEngine" title="getRTCEngine"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="getBMXRTCSignalService" %}{% endlanying_code_snippet %}
```
### getRTCEngine

获取存储的engine对象实例

`- (BMXRTCEngine *)getRTCEngine`

#### Return Value
BMXRTCEngine*

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="getRTCEngine" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

移除RTCService回调监听

`- (void)removeDelegate:(id<BMXRTCServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  
   RTCService监听器  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeRTCListener:" title="removeRTCListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeRTCListener:

移除RTCService回调监听

`- (void)removeRTCListener:(id<BMXRTCServiceProtocol>)*listener*`

#### Parameters

*listener*  
   RTCService监听器  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendRTCMessageWithMsg:" title="sendRTCMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="removeRTCListener:" %}{% endlanying_code_snippet %}
```
### sendRTCMessageWithMsg:

发送消息，用来RTCService层进行交互信令发送的操作。

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   发送的信息消息，消息的类型仅为信令消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendRTCMessageWithMsg:completion:" title="sendRTCMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="sendRTCMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### sendRTCMessageWithMsg:completion:

发送消息，用来RTCService层进行交互信令发送的操作。

`- (void)sendRTCMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   发送的信息消息，消息的类型仅为信令消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setupRTCEngine:" title="setupRTCEngine:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="sendRTCMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### setupRTCEngine:

初始化并存储engine对象实例

`- (void)setupRTCEngine:(BMXRTCEngine *)*engine*`

#### Parameters

*engine*  
   BMXRTCEngine对象实例指针  

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRTCService",function="setupRTCEngine:" %}{% endlanying_code_snippet %}
```
