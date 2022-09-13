# BMXPushServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXPushServiceProtocol.h  

## Instance Methods

<a name="//api/name/certRetrieved:" title="certRetrieved:"></a>
### certRetrieved:

Push初始化完成后获取推送证书。

`- (void)certRetrieved:(NSString *)*certification*`

#### Parameters

*certification*  
   推送证书  

#### Discussion
Push初始化完成后获取推送证书。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/clearedTags:" title="clearedTags:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="certRetrieved:" %}{% endlanying_code_snippet %}
```
### clearedTags:

清空用户推送成功回调。

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

*operationId*  
   操作id  

#### Discussion
清空用户推送成功回调。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/deleteTagsDidFinished:" title="deleteTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="clearedTags:" %}{% endlanying_code_snippet %}
```
### deleteTagsDidFinished:

删除用户推送标签成功回调

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   操作id  

#### Discussion
删除用户推送标签成功回调

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/getTagsDidFinished:" title="getTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="deleteTagsDidFinished:" %}{% endlanying_code_snippet %}
```
### getTagsDidFinished:

获取用户推送标签成功回调。

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   操作id  

#### Discussion
获取用户推送标签成功回调。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushMessageStatusChanged:error:" title="pushMessageStatusChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="getTagsDidFinished:" %}{% endlanying_code_snippet %}
```
### pushMessageStatusChanged:error:

发送Push上行消息状态变化通知。

`- (void)pushMessageStatusChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Parameters

*message*  
   发生状态变化的上行消息  

*error*  
   状态错误码  

#### Discussion
发送Push上行消息状态变化通知。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushStartDidFinished:" title="pushStartDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushMessageStatusChanged:error:" %}{% endlanying_code_snippet %}
```
### pushStartDidFinished:

Push初始化完成通知。

`- (void)pushStartDidFinished:(NSString *)*bmxToken*`

#### Parameters

*bmxToken*  
   bmxToken  

#### Discussion
Push初始化完成通知。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushStartDidStopped" title="pushStartDidStopped"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushStartDidFinished:" %}{% endlanying_code_snippet %}
```
### pushStartDidStopped

Push功能停止通知。

`- (void)pushStartDidStopped`

#### Discussion
Push功能停止通知。

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/receivedPush:" title="receivedPush:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushStartDidStopped" %}{% endlanying_code_snippet %}
```
### receivedPush:

接收到新的Push通知

`- (void)receivedPush:(NSArray<BMXMessageObject*> *)*messages*`

#### Parameters

*messages*  
   Push通知列表  

#### Discussion
接收到新的Push通知

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/setTagsDidFinished:" title="setTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="receivedPush:" %}{% endlanying_code_snippet %}
```
### setTagsDidFinished:

设置用户推送标签成功回调。

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   操作id  

#### Discussion
设置用户推送标签成功回调。

#### Declared In
* `BMXPushServiceProtocol.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="setTagsDidFinished:" %}{% endlanying_code_snippet %}
```
