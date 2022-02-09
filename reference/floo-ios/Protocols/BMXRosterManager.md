# BMXRosterManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXRosterManager.h  

## Instance Methods

<a name="//api/name/acceptRosterById:withCompletion:" title="acceptRosterById:withCompletion:"></a>
### acceptRosterById:withCompletion:

接受加好友申请

`- (void)acceptRosterById:(NSInteger)*rosterId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
接受加好友申请

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

添加好友变化监听者

`- (void)addRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Discussion
添加好友变化监听者

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/addToBlockList:withCompletion:" title="addToBlockList:withCompletion:"></a>
### addToBlockList:withCompletion:

加入黑名单

`- (void)addToBlockList:(long long)*rosterId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
加入黑名单

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/applyAddRoster:reason:completion:" title="applyAddRoster:reason:completion:"></a>
### applyAddRoster:reason:completion:

申请添加好友

`- (void)applyAddRoster:(long long)*roster* reason:(NSString *)*reason* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
申请添加好友

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/declineRosterById:withReason:completion:" title="declineRosterById:withReason:completion:"></a>
### declineRosterById:withReason:completion:

拒绝加好友申请

`- (void)declineRosterById:(NSInteger)*rosterId* withReason:(NSString *)*reason* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
拒绝加好友申请

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/downloadAvatarWithRoster:progress:completion:" title="downloadAvatarWithRoster:progress:completion:"></a>
### downloadAvatarWithRoster:progress:completion:

下载头像

`- (void)downloadAvatarWithRoster:(BMXRoster *)*roster* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletion*`

#### Discussion
下载头像

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getApplicationListWithCursor:pageSize:completion:" title="getApplicationListWithCursor:pageSize:completion:"></a>
### getApplicationListWithCursor:pageSize:completion:

获取申请添加好友列表

`- (void)getApplicationListWithCursor:(NSString *)*cursor* pageSize:(int)*pageSize* completion:(void ( ^ ) ( NSArray *applicationList , NSString *cursor , int offset , BMXError *error ))*aCompletionBlock*`

#### Discussion
获取申请添加好友列表

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getBlockListforceRefresh:completion:" title="getBlockListforceRefresh:completion:"></a>
### getBlockListforceRefresh:completion:

<ul>
<li>获取黑名单</li>
</ul>

`- (void)getBlockListforceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *blockList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   如果forceRefresh == true，则强制从服务端拉取  

*aCompletionBlock*  
   BlockList ,Error  

#### Discussion
<ul>
<li>获取黑名单</li>
</ul>

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/getRosterListforceRefresh:completion:" title="getRosterListforceRefresh:completion:"></a>
### getRosterListforceRefresh:completion:

<ul>
<li>获取好友列表</li>
</ul>

`- (void)getRosterListforceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray *rostIdList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   如果forceRefresh == true，则强制从服务端拉取  

*aCompletionBlock*  
   好友列表  

#### Discussion
<ul>
<li>获取好友列表</li>
</ul>

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/muteNotificationByRoster:muteNotificationStatus:completion:" title="muteNotificationByRoster:muteNotificationStatus:completion:"></a>
### muteNotificationByRoster:muteNotificationStatus:completion:

设置是否拒收用户消息

`- (void)muteNotificationByRoster:(BMXRoster *)*roster* muteNotificationStatus:(BOOL)*muteNotificationStatus* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
设置是否拒收用户消息

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXRosterServiceProtocol>)*aDelegate*`

<a name="//api/name/removeRosterById:withCompletion:" title="removeRosterById:withCompletion:"></a>
### removeRosterById:withCompletion:

删除好友

`- (void)removeRosterById:(long long)*rostId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
删除好友

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeRosterFromBlockList:withCompletion:" title="removeRosterFromBlockList:withCompletion:"></a>
### removeRosterFromBlockList:withCompletion:

从黑名单移除

`- (void)removeRosterFromBlockList:(NSInteger)*rostId* withCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
从黑名单移除

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/removeRosterListener:" title="removeRosterListener:"></a>
### removeRosterListener:

移除好友变化监听者

`- (void)removeRosterListener:(id<BMXRosterServiceProtocol>)*listener*`

#### Discussion
移除好友变化监听者

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchByRoserName:forceRefresh:completion:" title="searchByRoserName:forceRefresh:completion:"></a>
### searchByRoserName:forceRefresh:completion:

通过好友Name搜索

`- (void)searchByRoserName:(NSString *)*name* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Parameters

*name*  
   好友name  

*aCompletionBlock*  
   好友  

#### Discussion
通过好友Name搜索

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchByRosterId:forceRefresh:completion:" title="searchByRosterId:forceRefresh:completion:"></a>
### searchByRosterId:forceRefresh:completion:

通过好友ID搜索

`- (void)searchByRosterId:(long long)*rosterId* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterId*  
   好友ID  

*aCompletionBlock*  
   好友  

#### Discussion
通过好友ID搜索

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/searchRostersByRosterIdList:forceRefresh:completion:" title="searchRostersByRosterIdList:forceRefresh:completion:"></a>
### searchRostersByRosterIdList:forceRefresh:completion:

批量搜索用户

`- (void)searchRostersByRosterIdList:(NSArray<NSNumber*> *)*rosterIdList* forceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( NSArray<BMXRoster*> *rosterList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*rosterIdList*  
   id  

*forceRefresh*  
   如果forceRefresh == true，则强制从服务端拉取  

*aCompletionBlock*  
   rosterList,error  

#### Discussion
批量搜索用户

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemAliasByRoster:aliasJson:completion:" title="updateItemAliasByRoster:aliasJson:completion:"></a>
### updateItemAliasByRoster:aliasJson:completion:

更新好友别名

`- (void)updateItemAliasByRoster:(BMXRoster *)*roster* aliasJson:(NSString *)*aliasJson* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
更新好友别名

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemExtensionByRoster:extensionJson:completion:" title="updateItemExtensionByRoster:extensionJson:completion:"></a>
### updateItemExtensionByRoster:extensionJson:completion:

更新好友扩展信息

`- (void)updateItemExtensionByRoster:(BMXRoster *)*roster* extensionJson:(NSString *)*extensionJson* completion:(void ( ^ ) ( BMXRoster *roster , NSString *extensionJson ))*aCompletionBlock*`

#### Discussion
更新好友扩展信息

#### Declared In
* `BMXRosterManager.h`

<a name="//api/name/updateItemLocalExtensionByRoster:localExtensionJson:completion:" title="updateItemLocalExtensionByRoster:localExtensionJson:completion:"></a>
### updateItemLocalExtensionByRoster:localExtensionJson:completion:

更新好友本地扩展信息

`- (void)updateItemLocalExtensionByRoster:(BMXRoster *)*roster* localExtensionJson:(NSString *)*localExtensionJson* completion:(void ( ^ ) ( BMXRoster *roster , BMXError *error ))*aCompletionBlock*`

#### Discussion
更新好友本地扩展信息

#### Declared In
* `BMXRosterManager.h`

