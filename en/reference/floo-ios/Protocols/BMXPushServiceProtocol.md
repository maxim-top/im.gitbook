# BMXPushServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol Push service listener

## Instance Methods

<a name="//api/name/certRetrieved:" title="certRetrieved:"></a>
### certRetrieved:

Certificate retrieved

`- (void)certRetrieved:(NSString *)*certification*`

#### Parameters

*certification*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clearedTags:" title="clearedTags:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="certRetrieved:" %}{% endlanying_code_snippet %}
```
### clearedTags:

Push tags cleared

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteTagsDidFinished:" title="deleteTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="clearedTags:" %}{% endlanying_code_snippet %}
```
### deleteTagsDidFinished:

Push tags deleted

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getTagsDidFinished:" title="getTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="deleteTagsDidFinished:" %}{% endlanying_code_snippet %}
```
### getTagsDidFinished:

Get push tags

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushMessageStatusChanged:error:" title="pushMessageStatusChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="getTagsDidFinished:" %}{% endlanying_code_snippet %}
```
### pushMessageStatusChanged:error:

Push message status changed

`- (void)pushMessageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Parameters

*message*  

*error*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushStartDidFinished:" title="pushStartDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushMessageStatusChanged:error:" %}{% endlanying_code_snippet %}
```
### pushStartDidFinished:

Push service initialized

`- (void)pushStartDidFinished:(NSString *)*bmxToken*`

#### Parameters

*bmxToken*  
   bmxToken  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushStartDidStopped" title="pushStartDidStopped"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushStartDidFinished:" %}{% endlanying_code_snippet %}
```
### pushStartDidStopped

Push service stopped

`- (void)pushStartDidStopped`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedPush:" title="receivedPush:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="pushStartDidStopped" %}{% endlanying_code_snippet %}
```
### receivedPush:

Received push messages

`- (void)receivedPush:(NSArray<BMXMessage*> *)*messages*`

#### Parameters

*messages*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setTagsDidFinished:" title="setTagsDidFinished:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="receivedPush:" %}{% endlanying_code_snippet %}
```
### setTagsDidFinished:

Push tags has been set

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXPushServiceProtocol",function="setTagsDidFinished:" %}{% endlanying_code_snippet %}
```
