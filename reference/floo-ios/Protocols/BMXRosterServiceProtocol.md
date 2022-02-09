# BMXRosterServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXRosterServiceProtocol.h  

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

#### Discussion
添加好友

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendAddedtoBlockListSponsorId:recipientId:" title="friendAddedtoBlockListSponsorId:recipientId:"></a>
### friendAddedtoBlockListSponsorId:recipientId:

<ul>
<li>添加黑名单</li>
</ul>

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Discussion
<ul>
<li>添加黑名单</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidApplicationAcceptedFromSponsorId:recipientId:" title="friendDidApplicationAcceptedFromSponsorId:recipientId:"></a>
### friendDidApplicationAcceptedFromSponsorId:recipientId:

<ul>
<li>加好友申请被通过了</li>
<li>用户B同意用户A的加好友请求后，用户A会收到这个回调</li>
</ul>

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Discussion
<ul>
<li>加好友申请被通过了</li>
<li>用户B同意用户A的加好友请求后，用户A会收到这个回调</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidApplicationDeclinedFromSponsorId:recipientId:reson:" title="friendDidApplicationDeclinedFromSponsorId:recipientId:reson:"></a>
### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

<ul>
<li>加好友申请被拒绝了</li>
<li>用户B拒绝用户A的加好友请求后，用户A会收到这个回调</li>
</ul>

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

*reason*  
   拒绝理由  

#### Discussion
<ul>
<li>加好友申请被拒绝了</li>
<li>用户B拒绝用户A的加好友请求后，用户A会收到这个回调</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidRecivedAppliedSponsorId:recipientId:message:" title="friendDidRecivedAppliedSponsorId:recipientId:message:"></a>
### friendDidRecivedAppliedSponsorId:recipientId:message:

<ul>
<li>收到加好友申请</li>
<li>用户B申请加A为好友后，用户A会收到这个回调</li>
</ul>

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

*message*  
   好友邀请信息  

#### Discussion
<ul>
<li>收到加好友申请</li>
<li>用户B申请加A为好友后，用户A会收到这个回调</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendRemovedFromBlockListSponsorId:recipientId:" title="friendRemovedFromBlockListSponsorId:recipientId:"></a>
### friendRemovedFromBlockListSponsorId:recipientId:

<ul>
<li>删除黑名单</li>
</ul>

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Discussion
<ul>
<li>删除黑名单</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendRemovedSponsorId:recipientId:" title="friendRemovedSponsorId:recipientId:"></a>
### friendRemovedSponsorId:recipientId:

<pre><code>删除好友
</code></pre>

<ul>
<li>用户B删除与用户A的好友关系后，用户A会收到这个回调</li>
</ul>

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   发起方  

*recipientId*  
   接受方  

#### Discussion
<pre><code>删除好友
</code></pre>

<ul>
<li>用户B删除与用户A的好友关系后，用户A会收到这个回调</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/rosterInfoDidUpdate:" title="rosterInfoDidUpdate:"></a>
### rosterInfoDidUpdate:

用户信息更新

`- (void)rosterInfoDidUpdate:(BMXRoster *)*roster*`

#### Discussion
用户信息更新

#### Declared In
* `BMXRosterServiceProtocol.h`

