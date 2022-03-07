# BMXRosterServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXRosterServiceProtocol.h  

## Instance Methods

<a name="//api/name/friendAddedSponsorId:recipientId:" title="friendAddedSponsorId:recipientId:"></a>
### friendAddedSponsorId:recipientId:

Add friend

`- (void)friendAddedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

#### Discussion
Add friend

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendAddedtoBlockListSponsorId:recipientId:" title="friendAddedtoBlockListSponsorId:recipientId:"></a>
### friendAddedtoBlockListSponsorId:recipientId:

<ul>
<li>Add to blacklist</li>
</ul>

`- (void)friendAddedtoBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

#### Discussion
<ul>
<li>Add to blacklist</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidApplicationAcceptedFromSponsorId:recipientId:" title="friendDidApplicationAcceptedFromSponsorId:recipientId:"></a>
### friendDidApplicationAcceptedFromSponsorId:recipientId:

<ul>
<li>Request of adding friend approved</li>
<li>User A will receive this callback after User B agrees to User A's friend request</li>
</ul>

`- (void)friendDidApplicationAcceptedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

#### Discussion
<ul>
<li>Request of adding friend approved</li>
<li>User A will receive this callback after User B agrees to User A's friend request</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidApplicationDeclinedFromSponsorId:recipientId:reson:" title="friendDidApplicationDeclinedFromSponsorId:recipientId:reson:"></a>
### friendDidApplicationDeclinedFromSponsorId:recipientId:reson:

<ul>
<li>Request of adding friend rejected</li>
<li>User A will receive this callback after User B rejects to User A's friend request</li>
</ul>

`- (void)friendDidApplicationDeclinedFromSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* reson:(NSString *)*reason*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

*reason*  
   Reason for rejection  

#### Discussion
<ul>
<li>Request of adding friend rejected</li>
<li>User A will receive this callback after User B rejects to User A's friend request</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendDidRecivedAppliedSponsorId:recipientId:message:" title="friendDidRecivedAppliedSponsorId:recipientId:message:"></a>
### friendDidRecivedAppliedSponsorId:recipientId:message:

<ul>
<li>Request of adding friend received</li>
<li>User A will receive this callback after User B requests a friend relationship with User A</li>
</ul>

`- (void)friendDidRecivedAppliedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId* message:(NSString *)*message*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

*message*  
   Friend request information  

#### Discussion
<ul>
<li>Request of adding friend received</li>
<li>User A will receive this callback after User B requests a friend relationship with User A</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendRemovedFromBlockListSponsorId:recipientId:" title="friendRemovedFromBlockListSponsorId:recipientId:"></a>
### friendRemovedFromBlockListSponsorId:recipientId:

<ul>
<li>Delete blacklist</li>
</ul>

`- (void)friendRemovedFromBlockListSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

#### Discussion
<ul>
<li>Delete blacklist</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/friendRemovedSponsorId:recipientId:" title="friendRemovedSponsorId:recipientId:"></a>
### friendRemovedSponsorId:recipientId:

<pre><code>Delete friend
</code></pre>

<ul>
<li>User A will receive this callback after User B removes a friend relationship with User A</li>
</ul>

`- (void)friendRemovedSponsorId:(long long)*sponsorId* recipientId:(long long)*recipientId*`

#### Parameters

*sponsorId*  
   Initiator  

*recipientId*  
   Recipient  

#### Discussion
<pre><code>Delete friend
</code></pre>

<ul>
<li>User A will receive this callback after User B removes a friend relationship with User A</li>
</ul>

#### Declared In
* `BMXRosterServiceProtocol.h`

<a name="//api/name/rosterInfoDidUpdate:" title="rosterInfoDidUpdate:"></a>
### rosterInfoDidUpdate:

Update user information

`- (void)rosterInfoDidUpdate:(BMXRoster *)*roster*`

#### Discussion
Update user information

#### Declared In
* `BMXRosterServiceProtocol.h`

