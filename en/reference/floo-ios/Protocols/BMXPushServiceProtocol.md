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
### clearedTags:

Push tags cleared

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteTagsDidFinished:" title="deleteTagsDidFinished:"></a>
### deleteTagsDidFinished:

Push tags deleted

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getTagsDidFinished:" title="getTagsDidFinished:"></a>
### getTagsDidFinished:

Get push tags

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/pushMessageStatusChanged:error:" title="pushMessageStatusChanged:error:"></a>
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
### pushStartDidStopped

Push service stopped

`- (void)pushStartDidStopped`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedPush:" title="receivedPush:"></a>
### receivedPush:

Received push messages

`- (void)receivedPush:(NSArray<BMXMessage*> *)*messages*`

#### Parameters

*messages*  

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setTagsDidFinished:" title="setTagsDidFinished:"></a>
### setTagsDidFinished:

Push tags has been set

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  

#### Discussion

#### Declared In
* `floo_proxy.h`

