# BMXRosterServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol 好友服务监听者

## Instance Methods

### friendAddedSponsorId:recipientId:

添加好友

`- (void)friendAddedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendAddedtoBlockListSponsorId:recipientId:

添加黑名单

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidApplicationAcceptedFromSponsorId:recipientId:

加好友申请被通过了 用户B同意用户A的加好友请求后，用户A会收到这个回调

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

加好友申请被拒绝了 用户B拒绝用户A的加好友请求后，用户A会收到这个回调

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

_reason_\
拒绝理由

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidRecivedAppliedSponsorId:recipientId:message:

收到加好友申请 用户B申请加A为好友后，用户A会收到这个回调

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

_message_\
好友邀请信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendRemovedFromBlockListSponsorId:recipientId:

删除黑名单

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendRemovedSponsorId:recipientId:

删除好友 用户B删除与用户A的好友关系后，用户A会收到这个回调

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_\
发起方

_recipientId_\
接受方

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### rosterInfoDidUpdate:

用户信息更新

`- (void)rosterInfoDidUpdate:(BMXRosterItem *)*roster*`

#### Discussion

用户信息更新

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>
```
