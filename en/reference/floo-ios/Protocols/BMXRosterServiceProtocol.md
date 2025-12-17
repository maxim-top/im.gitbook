# BMXRosterServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol Roster service listener

## Instance Methods

### friendAddedSponsorId:recipientId:

Friend added

`- (void)friendAddedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_

_recipientId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendAddedtoBlockListSponsorId:recipientId:

Blocked a user

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_

_recipientId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidApplicationAcceptedFromSponsorId:recipientId:

Friend request accepted

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_

_recipientId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

Friend request declined

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

_sponsorId_

_recipientId_

_reason_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendDidRecivedAppliedSponsorId:recipientId:message:

Received a friend request

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

_sponsorId_

_recipientId_

_message_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendRemovedFromBlockListSponsorId:recipientId:

Unblocked a user

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_

_recipientId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### friendRemovedSponsorId:recipientId:

A friend removed

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

_sponsorId_

_recipientId_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>

```

### rosterInfoDidUpdate:

Roster item information updated

`- (void)rosterInfoDidUpdate:(BMXRosterItem *)*roster*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXRosterServiceProtocol'></div>
```
