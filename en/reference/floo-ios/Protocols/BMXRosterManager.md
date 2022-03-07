# BMXRosterManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXRosterManager.h  

## Instance Methods

<a name="//api/name/acceptRosterById:withCompletion:" title="acceptRosterById:withCompletion:"></a>
### acceptRosterById:withCompletion:

Accept adding friend request

`- (void)acceptRosterById:(NSInteger)*rosterId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Accept adding friend request

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXRosterServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addRosterListener:" title="addRosterListener:"></a>
### addRosterListener:

Add friend change listener

`- (void)addRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Discussion
Add friend change listener

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/addToBlockList:withCompletion:" title="addToBlockList:withCompletion:"></a>
### addToBlockList:withCompletion:

Add to blacklist

`- (void)addToBlockList:(long long)*rosterId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Add to blacklist

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/applyAddRoster:reason:completion:" title="applyAddRoster:reason:completion:"></a>
### applyAddRoster:reason:completion:

Request to add friend

`- (void)applyAddRoster:(long long)*roster* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
Request to add friend

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/declineRosterById:withReason:completion:" title="declineRosterById:withReason:completion:"></a>
### declineRosterById:withReason:completion:

Reject adding friend request

`- (void)declineRosterById:(NSInteger)*rosterId* withReason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Reject adding friend request

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/downloadAvatarWithRoster:progress:completion:" title="downloadAvatarWithRoster:progress:completion:"></a>
### downloadAvatarWithRoster:progress:completion:

Download avatar

`- (void)downloadAvatarWithRoster:(BMXRoster *)*roster* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletion*`

#### Discussion
Download avatar

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getApplicationListWithCursor:pageSize:completion:" title="getApplicationListWithCursor:pageSize:completion:"></a>
### getApplicationListWithCursor:pageSize:completion:

Get list of adding friend requests

`- (void)getApplicationListWithCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *applicationList , NSString *cursor , int offset , BMXError *error ))*aCompletionBlock*`

#### Discussion
Get list of adding friend requests

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getBlockListforceRefresh:completion:" title="getBlockListforceRefresh:completion:"></a>
### getBlockListforceRefresh:completion:

<ul>
<li>Get blacklist</li>
</ul>

`- (void)getBlockListforceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *blockList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   If forceRefresh == true, force pull from server-side  

*aCompletionBlock*  
   BlockList ,Error  

#### Discussion
<ul>
<li>Get blacklist</li>
</ul>

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getRosterListforceRefresh:completion:" title="getRosterListforceRefresh:completion:"></a>
### getRosterListforceRefresh:completion:

<ul>
<li>Get friend list</li>
</ul>

`- (void)getRosterListforceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *rostIdList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   If forceRefresh == true, force pull from server-side  

*aCompletionBlock*  
   List of friends  

#### Discussion
<ul>
<li>Get friend list</li>
</ul>

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/muteNotificationByRoster:muteNotificationStatus:completion:" title="muteNotificationByRoster:muteNotificationStatus:completion:"></a>
### muteNotificationByRoster:muteNotificationStatus:completion:

Set whether to reject user message

`- (void)muteNotificationByRoster:(BMXRoster *)*roster* muteNotificationStatus:(BOOL)*muteNotificationStatus* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
Set whether to reject user message

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

<a name="//api/name/removeRosterById:withCompletion:" title="removeRosterById:withCompletion:"></a>
### removeRosterById:withCompletion:

Delete friend

`- (void)removeRosterById:(long long)*rostId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Delete friend

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeRosterFromBlockList:withCompletion:" title="removeRosterFromBlockList:withCompletion:"></a>
### removeRosterFromBlockList:withCompletion:

Remove from blacklist

`- (void)removeRosterFromBlockList:(NSInteger)*rostId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Remove from blacklist

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeRosterListener:" title="removeRosterListener:"></a>
### removeRosterListener:

Remove friend change listener

`- (void)removeRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Discussion
Remove friend change listener

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchByRoserName:forceRefresh:completion:" title="searchByRoserName:forceRefresh:completion:"></a>
### searchByRoserName:forceRefresh:completion:

Search by friend Name

`- (void)searchByRoserName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Parameters

*name*  
   Friend name  

*aCompletionBlock*  
   Friend  

#### Discussion
Search by friend Name

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchByRosterId:forceRefresh:completion:" title="searchByRosterId:forceRefresh:completion:"></a>
### searchByRosterId:forceRefresh:completion:

Search by friend ID

`- (void)searchByRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
   Friend ID  

*aCompletionBlock*  
   Friend  

#### Discussion
Search by friend ID

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchRostersByRosterIdList:forceRefresh:completion:" title="searchRostersByRosterIdList:forceRefresh:completion:"></a>
### searchRostersByRosterIdList:forceRefresh:completion:

Batch search for users

`- (void)searchRostersByRosterIdList:(NSArray<NSNumber*> *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXRoster*> *rosterList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterIdList*  
   id  

*forceRefresh*  
   If forceRefresh == true, force pull from server-side  

*aCompletionBlock*  
   rosterList,error  

#### Discussion
Batch search for users

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemAliasByRoster:aliasJson:completion:" title="updateItemAliasByRoster:aliasJson:completion:"></a>
### updateItemAliasByRoster:aliasJson:completion:

Update friend's alias

`- (void)updateItemAliasByRoster:(BMXRoster *)*roster* aliasJson:(NSString *)*aliasJson* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
Update friend's alias

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemExtensionByRoster:extensionJson:completion:" title="updateItemExtensionByRoster:extensionJson:completion:"></a>
### updateItemExtensionByRoster:extensionJson:completion:

Update friend extension information

`- (void)updateItemExtensionByRoster:(BMXRoster *)*roster* extensionJson:(NSString *)*extensionJson* completion:(void ( ^ ) ( BMXRoster *roster , NSString *extensionJson ))*aCompletionBlock*`

#### Discussion
Update friend extension information

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemLocalExtensionByRoster:localExtensionJson:completion:" title="updateItemLocalExtensionByRoster:localExtensionJson:completion:"></a>
### updateItemLocalExtensionByRoster:localExtensionJson:completion:

Update friend's local extension information

`- (void)updateItemLocalExtensionByRoster:(BMXRoster *)*roster* localExtensionJson:(NSString *)*localExtensionJson* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
Update friend's local extension information

#### Declared In
* `BMXRosterManager.h`

