# BMXRosterServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol Roster service listener

## Instance Methods

<a name="//api/name/friendAddedSponsorId:recipientId:" title="friendAddedSponsorId:recipientId:"></a>
### friendAddedSponsorId:recipientId:

Friend added

`- (void)friendAddedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  

*recipientId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendAddedtoBlockListSponsorId:recipientId:" title="friendAddedtoBlockListSponsorId:recipientId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendAddedSponsorId:recipientId:" %}{% endlanying_code_snippet %}
```
### friendAddedtoBlockListSponsorId:recipientId:

Blocked a user

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  

*recipientId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidApplicationAcceptedFromSponsorId:recipientId:" title="friendDidApplicationAcceptedFromSponsorId:recipientId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendAddedtoBlockListSponsorId:recipientId:" %}{% endlanying_code_snippet %}
```
### friendDidApplicationAcceptedFromSponsorId:recipientId:

Friend request accepted

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  

*recipientId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidApplicationDeclinedFromSponsorId:recipientId:reson:" title="friendDidApplicationDeclinedFromSponsorId:recipientId:reson:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendDidApplicationAcceptedFromSponsorId:recipientId:" %}{% endlanying_code_snippet %}
```
### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

Friend request declined

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

*sponsorId*  

*recipientId*  

*reason*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidRecivedAppliedSponsorId:recipientId:message:" title="friendDidRecivedAppliedSponsorId:recipientId:message:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendDidApplicationDeclinedFromSponsorId:recipientId:reson:" %}{% endlanying_code_snippet %}
```
### friendDidRecivedAppliedSponsorId:recipientId:message:

Received a friend request

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

*sponsorId*  

*recipientId*  

*message*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendRemovedFromBlockListSponsorId:recipientId:" title="friendRemovedFromBlockListSponsorId:recipientId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendDidRecivedAppliedSponsorId:recipientId:message:" %}{% endlanying_code_snippet %}
```
### friendRemovedFromBlockListSponsorId:recipientId:

Unblocked a user

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  

*recipientId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendRemovedSponsorId:recipientId:" title="friendRemovedSponsorId:recipientId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendRemovedFromBlockListSponsorId:recipientId:" %}{% endlanying_code_snippet %}
```
### friendRemovedSponsorId:recipientId:

A friend removed

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  

*recipientId*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/rosterInfoDidUpdate:" title="rosterInfoDidUpdate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="friendRemovedSponsorId:recipientId:" %}{% endlanying_code_snippet %}
```
### rosterInfoDidUpdate:

Roster item information updated

`- (void)rosterInfoDidUpdate:(BMXRosterItem *)*roster*`

#### Discussion

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXRosterServiceProtocol",function="rosterInfoDidUpdate:" %}{% endlanying_code_snippet %}
```
