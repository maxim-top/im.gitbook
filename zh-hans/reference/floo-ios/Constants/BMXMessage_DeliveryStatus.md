# BMXMessage_DeliveryStatus Constants Reference

  **Declared in** floo_proxy.h  

### BMXMessage_DeliveryStatus

消息投递状态

#### Definition
    typedef NS_ENUM(NSInteger, BMXMessage_DeliveryStatus ) {   
        
        BMXMessage_DeliveryStatus_New,
        
        BMXMessage_DeliveryStatus_Delivering,
        
        BMXMessage_DeliveryStatus_Deliveried,
        
        BMXMessage_DeliveryStatus_Failed,
        
        BMXMessage_DeliveryStatus_Recalled,
        
    };

#### Constants

<a name="" title="BMXMessage_DeliveryStatus_New"></a><code>BMXMessage_DeliveryStatus_New</code>

消息投递状态

   Declared In `floo_proxy.h`.

<a name="" title="BMXMessage_DeliveryStatus_Delivering"></a><code>BMXMessage_DeliveryStatus_Delivering</code>

新创建消息

   Declared In `floo_proxy.h`.

<a name="" title="BMXMessage_DeliveryStatus_Deliveried"></a><code>BMXMessage_DeliveryStatus_Deliveried</code>

消息投递中

   Declared In `floo_proxy.h`.

<a name="" title="BMXMessage_DeliveryStatus_Failed"></a><code>BMXMessage_DeliveryStatus_Failed</code>

消息已投递

   Declared In `floo_proxy.h`.

<a name="" title="BMXMessage_DeliveryStatus_Recalled"></a><code>BMXMessage_DeliveryStatus_Recalled</code>

消息投递失败

   Declared In `floo_proxy.h`.

#### Declared In
`floo_proxy.h`

