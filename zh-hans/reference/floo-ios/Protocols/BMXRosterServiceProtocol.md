# BMXRosterServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol 好友服务监听者

## Instance Methods

<a name="//api/name/friendAddedSponsorId:recipientId:" title="friendAddedSponsorId:recipientId:"></a>
### friendAddedSponsorId:recipientId:

添加好友

`- (void)friendAddedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendAddedtoBlockListSponsorId:recipientId:" title="friendAddedtoBlockListSponsorId:recipientId:"></a>
### friendAddedtoBlockListSponsorId:recipientId:

添加黑名单

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidApplicationAcceptedFromSponsorId:recipientId:" title="friendDidApplicationAcceptedFromSponsorId:recipientId:"></a>
### friendDidApplicationAcceptedFromSponsorId:recipientId:

加好友申请被通过了 用户B同意用户A的加好友请求后，用户A会收到这个回调

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidApplicationDeclinedFromSponsorId:recipientId:reson:" title="friendDidApplicationDeclinedFromSponsorId:recipientId:reson:"></a>
### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

加好友申请被拒绝了 用户B拒绝用户A的加好友请求后，用户A会收到这个回调

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

*reason*  
   拒绝理由  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendDidRecivedAppliedSponsorId:recipientId:message:" title="friendDidRecivedAppliedSponsorId:recipientId:message:"></a>
### friendDidRecivedAppliedSponsorId:recipientId:message:

收到加好友申请 用户B申请加A为好友后，用户A会收到这个回调

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

*message*  
   好友邀请信息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendRemovedFromBlockListSponsorId:recipientId:" title="friendRemovedFromBlockListSponsorId:recipientId:"></a>
### friendRemovedFromBlockListSponsorId:recipientId:

删除黑名单

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/friendRemovedSponsorId:recipientId:" title="friendRemovedSponsorId:recipientId:"></a>
### friendRemovedSponsorId:recipientId:

删除好友 用户B删除与用户A的好友关系后，用户A会收到这个回调

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/rosterInfoDidUpdate:" title="rosterInfoDidUpdate:"></a>
### rosterInfoDidUpdate:

用户信息更新

`- (void)rosterInfoDidUpdate:(BMXRosterItem *)*roster*`

#### Discussion
用户信息更新

#### Declared In
* `floo_proxy.h`

