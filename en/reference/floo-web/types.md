# types
## types {#module_types}

* [types](#module_types)
    * ["flooNotice" (res)](#event_floonotice)
    * ["flooError" (res)](#event_flooerror)
    * ["loginFail" (desc)](#event_loginfail)
    * ["loginSuccess" (res)](#event_loginsuccess)
    * ["onGroupListUpdate" (meta)](#event_ongrouplistupdate)
    * ["onGroupMemberChanged" (groupId)](#event_ongroupmemberchanged)
    * ["onGroupMessage" (meta)](#event_ongroupmessage)
    * ["onInputStatusMessage" (res)](#event_oninputstatusmessage)
    * ["onMentionMessage" (meta)](#event_onmentionmessage)
    * ["onMessageCanceled" (res)](#event_onmessagecanceled)
    * ["onMessageDeleted" (res)](#event_onmessagedeleted)
    * ["onMessageRecalled" (res)](#event_onmessagerecalled)
    * ["onMessageStatusChanged" (res)](#event_onmessagestatuschanged)
    * ["onReceiveHistoryMsg" (res)](#event_onreceivehistorymsg)
    * ["onRosterInfoUpdate" (res)](#event_onrosterinfoupdate)
    * ["onRosterListUpdate" (meta)](#event_onrosterlistupdate)
    * ["onRosterMessage" (meta)](#event_onrostermessage)
    * ["onSendingMessageStatusChanged" (res)](#event_onsendingmessagestatuschanged)
    * ["onUnreadChange" (cid)](#event_onunreadchange)
    * ["recentlistUpdate"](#event_recentlistupdate)
    * ["onGroupCreated" (meta)](#event_ongroupcreated)
    * ["onGroupDestoryed" (meta)](#event_ongroupdestoryed)
    * ["onGroupJoined" (meta)](#event_ongroupjoined)
    * ["onGroupApplyAccepted" (meta)](#event_ongroupapplyaccepted)
    * ["onGroupApplyDeclined" (meta)](#event_ongroupapplydeclined)
    * ["onGroupBaned" (meta)](#event_ongroupbaned)
    * ["onGroupUnbaned" (meta)](#event_ongroupunbaned)
    * [~RosterItem](#module_types__rosteritem) : <code>object</code>
    * [~UserSettings](#module_types__usersettings) : <code>object</code>
    * [~UserProfile](#module_types__userprofile) : <code>object</code>
    * [~Meta](#module_types__meta) : <code>object</code>
    * [~RosterApplication](#module_types__rosterapplication) : <code>object</code>
    * [~GroupInfoAndSettings](#module_types__groupinfoandsettings) : <code>object</code>
    * [~BriefGroupInfoAndSettings](#module_types__briefgroupinfoandsettings) : <code>object</code>
    * [~GroupMember](#module_types__groupmember) : <code>object</code>
    * [~GroupMemberBanned](#module_types__groupmemberbanned) : <code>object</code>
    * [~GroupUserRelationResponse](#module_types__groupuserrelationresponse) : <code>object</code>
    * [~GroupAnnouncement](#module_types__groupannouncement) : <code>object</code>
    * [~GroupInfoRequest](#module_types__groupinforequest) : <code>object</code>
    * [~GroupBannedMemberRequest](#module_types__groupbannedmemberrequest) : <code>object</code>
    * [~GroupBlockedListItem](#module_types__groupblockedlistitem) : <code>object</code>
    * [~GroupInvitation](#module_types__groupinvitation) : <code>object</code>
    * [~GroupApplication](#module_types__groupapplication) : <code>object</code>
    * [~GroupSharedFile](#module_types__groupsharedfile) : <code>object</code>
    * [~GroupSharedFileResponse](#module_types__groupsharedfileresponse) : <code>object</code>
    * [~GroupBanAllResponse](#module_types__groupbanallresponse) : <code>object</code>
    * [~FileUpload](#module_types__fileupload) : <code>object</code>
    * [~FileUploadResult](#module_types__fileuploadresult) : <code>object</code>
    * [~fileUploadProgress](#module_types__fileuploadprogress) : <code>function</code>
    * [~ConversationItem](#module_types__conversationitem) : <code>object</code>
    * [~UserProfile](#module_types__userprofile) : <code>object</code>
    * [~UserSettings](#module_types__usersettings) : <code>object</code>
    * [~Event](#module_types__event) : <code>string</code>
    * [~EventCallback](#module_types__eventcallback) : <code>function</code>

### "flooNotice" (res) {#event_floonotice}
Floo notification

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | Results |
| res.category | <code>string</code> | Types |
| res.desc | <code>string</code> | Description |

**Example**  
```js
{category: 'loginMessage',desc: 'socket connecting...'} // Start connecting
{category: 'loginMessage',desc: 'socket connect success...'} // Connected
{category: 'loginMessage',desc: 'logining socket service...'} // Start logging in
{category: 'loginMessage',desc: 'login socket failure ......'} // Login failed
{category: 'loginMessage',desc: 'login socket success.....'} // Login succeeded
{category: 'loginMessage', desc: 'getting token...' } //Get token
{category: 'loginMessage',desc: 'token sucecc, getting roster lists..'} // Getting token succeeded, start to fetch friend list
{category: 'loginMessage',desc: 'get roster list failure:' + ex.message} // Friend list fetching failed
{category: 'action', desc: 'relogin' } // Need to automatically login
{category: 'action', desc: 'relogin_manually' }  // Need to manually login
{category: 'conversation_deleted',desc: { id, source:'user_operation' }} // Session deleted. ID:session ID, source: source
{category: 'userNotice', desc:'PASSWORD_CHANGED'} // User password changed
{category: 'userNotice', desc:'FROZEN'} // User account frozen
{category: 'userNotice', desc:'REMOVED'} // User removed
{category: 'userNotice', desc:'KICK_BY_SAME_DEVICE'} // Current device is kicked off the line by the same device
{category: 'userNotice', desc:'KICKED_BY_OTHER_DEVICE'} // Current device is kicked off the line by other device
{category: 'userNotice', desc:'INFO_UPDATED'} // User information changed:profile or setting
{category: 'userNotice', desc:'DEVICE_LOGIN'} // User's other device logged-in
{category: 'userNotice', desc:'DEVICE_LOGOUT'} // User's other device logged-out
{category: 'userNotice', desc:'DEVICE_ADDED'} // New device notified
{category: 'userNotice', desc:'DEVICE_REMOVED'} // Device removal notified
{category: 'userNotice', desc:'CLUSTER_CHANGED'} // User's group changed, please re-login
```
### "flooError" (res) {#event_flooerror}
FlooError

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.category | <code>string</code> | Types |
| res.desc | <code>string</code> | Description |

**Example**  
```js
{category: 'USER_BANNED', desc:'User is banned'}
{category: 'USER_FROZEN', desc:'User is frozen, please contact App Admin.'}
{category: 'APP_FROZEN', desc:'APP is frozen, please login Maximtop Console for more details.'}
{category: 'LICENSE', desc:'Invalid LICENSE, please make sure service is paid on time.'}
{category: 'LICENSE', desc:'LICENSE user limit reached, please purchase higher service package.'}
{category: 'DNS_FAILED', desc: dnsServer } // DNS error: unaccessible
```
### "loginFail" (desc) {#event_loginfail}
Login failed

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| desc | <code>string</code> | Cause of failure |

### "loginSuccess" (res) {#event_loginsuccess}
Login successful

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | Empty object |

### "onGroupListUpdate" (meta) {#event_ongrouplistupdate}
Group list updated

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) ¦ <code>undefined</code> | Notification message content |

### "onGroupMemberChanged" (groupId) {#event_ongroupmemberchanged}
Group member list updated

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| groupId | <code>number</code> | GroupID |

### "onGroupMessage" (meta) {#event_ongroupmessage}
Group message received

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content |

### "onInputStatusMessage" (res) {#event_oninputstatusmessage}
The other party is typing

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.ext | <code>string</code> | Extension field |
| res.from | <code>string</code> | Sender's user ID |
| res.to | <code>string</code> | Receiver's user ID |

### "onMentionMessage" (meta) {#event_onmentionmessage}
Group @message received

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content |

### "onMessageCanceled" (res) {#event_onmessagecanceled}
Message is re-unread

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | SessionID |
| res.mid | <code>string</code> | MessageID |

### "onMessageDeleted" (res) {#event_onmessagedeleted}
MessageDeleted

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | SessionID |
| res.mid | <code>string</code> | MessageID |

### "onMessageRecalled" (res) {#event_onmessagerecalled}
Message is withdrawn

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | SessionID |
| res.mid | <code>string</code> | MessageID |

### "onMessageStatusChanged" (res) {#event_onmessagestatuschanged}
Message status changed: withdrawn/deleted/read

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | SessionID |
| res.mid | <code>string</code> | MessageID |

### "onReceiveHistoryMsg" (res) {#event_onreceivehistorymsg}
Message history received

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.next | <code>number</code> | The key to get message history next time |

### "onRosterInfoUpdate" (res) {#event_onrosterinfoupdate}
Friend info changed

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.rosterIds | <code>Array.&lt;number&gt;</code> | Friend's user ID list |

### "onRosterListUpdate" (meta) {#event_onrosterlistupdate}
Friend list changed

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of friend's notification |

### "onRosterMessage" (meta) {#event_onrostermessage}
Single chat message received

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content |

### "onSendingMessageStatusChanged" (res) {#event_onsendingmessagestatuschanged}
Message sending status changed

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.status: | <code>number</code> | Sending status, can be valued as sending|failed|sent |
| res.mid: | <code>number</code> | client_mid generated by client |

### "onUnreadChange" (cid) {#event_onunreadchange}
Unread count changed

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| cid | <code>number</code> | SessionID |

### "recentlistUpdate" {#event_recentlistupdate}
Latest conversation updated

**Kind**: event emitted by [<code>types</code>](#module_types)  
### "onGroupCreated" (meta) {#event_ongroupcreated}
Group creation notification

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupDestoryed" (meta) {#event_ongroupdestoryed}
Group dismissal notification

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupJoined" (meta) {#event_ongroupjoined}
Member joining application notification

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupApplyAccepted" (meta) {#event_ongroupapplyaccepted}
Group joining application approved

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupApplyDeclined" (meta) {#event_ongroupapplydeclined}
Group joining application rejected

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupBaned" (meta) {#event_ongroupbaned}
Banned in group

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### "onGroupUnbaned" (meta) {#event_ongroupunbaned}
Unbanned in group

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types__meta) | Message content of group notification |

### types~RosterItem : <code>object</code> {#module_types__rosteritem}
Friend info

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| alias | <code>string</code> | Alias |
| auth_mode | <code>number</code> | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests,int32 |
| auth_question | <code>string</code> | Verification question |
| avatar | <code>string</code> | Avatar |
| description | <code>string</code> | Description |
| ext | <code>string</code> | Extension information |
| mute_notification | <code>boolean</code> | Whether to receive message alert |
| nick_name | <code>string</code> | Nickname or name |
| public_info | <code>string</code> | Public information, visible to both friends and strangers |
| relation | <code>number</code> | Relationships: 0 - Friend, 1 - Deleted, 2 - Stranger, int32 |
| user_id | <code>number</code> | Friend user ID,int64 |
| username | <code>string</code> | Username |

### types~UserSettings : <code>object</code> {#module_types__usersettings}
User settings information

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| auth_answer | <code>string</code> | Answer of verification question |
| auth_mode | <code>number</code> | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests,int32 |
| auth_question | <code>string</code> | Verification question |
| auto_download | <code>boolean</code> | Whether to download automatically |
| group_confirm | <code>boolean</code> | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
| id | <code>number</code> | User ID, int64 |
| no_push | <code>boolean</code> | Whether to turn off push |
| no_push_detail | <code>boolean</code> | Whether to push details |
| no_push_end_hour | <code>number</code> | Start of push no-disturb time,int32 |
| no_push_start_hour | <code>number</code> | End of push no-disturb time,int32 |
| no_sounds | <code>boolean</code> | Whether to mute when message received |
| push_nick_name | <code>string</code> | Push nickname |
| push_token | <code>string</code> | Push token |
| silence_end_time | <code>number</code> | End of push no-reminder time,int32 |
| silence_start_time | <code>number</code> | Start of push no-reminder time,int32 |
| user_id | <code>number</code> | User ID,int64 |
| vibratory | <code>boolean</code> | Whether to vibrate when message received |

### types~UserProfile : <code>object</code> {#module_types__userprofile}
User information

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | Avatar url |
| description | <code>string</code> | Description |
| email | <code>string</code> | Email |
| mobile | <code>string</code> | Mobile number |
| nick_name | <code>string</code> | Nickname |
| private_info | <code>string</code> | Private information, visible only to yourself |
| public_info | <code>string</code> | Public information, visible to both friends and strangers |
| user_id | <code>number</code> | User ID,int64 |
| username | <code>string</code> | Username |

### types~Meta : <code>object</code> {#module_types__meta}
Message body

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>string</code> | MessageID |
| from | <code>string</code> | Sender |
| to | <code>string</code> | Receiver |
| content | <code>string</code> | Message content |
| type | <code>string</code> | Message types: text, image, audio, video, file, location, command, forward |
| ext | <code>string</code> ¦ <code>object</code> | Extension field |
| config | <code>string</code> ¦ <code>object</code> | SDKExtension field |
| attach | <code>string</code> ¦ <code>object</code> | Attachment info |
| status | <code>number</code> | Message status: 0 - Unread, 1 - Delivered, 2 - Read |
| timestamp | <code>string</code> | Message delivery timestamp (milliseconds) |
| toType | <code>string</code> | Receiver types: roster - friend, group - group |

### types~RosterApplication : <code>object</code> {#module_types__rosterapplication}
List entries of adding friend request

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| expired_time | <code>number</code> | Expiration time,int64 |
| reason | <code>string</code> | Request description |
| status | <code>number</code> | Status: 0 - Awaiting confirmation, 1 - Approved, 2 - Rejected int32 |
| user_id | <code>number</code> | User ID that initiate adding friend,int64 |

### types~GroupInfoAndSettings : <code>object</code> {#module_types__groupinfoandsettings}
Group info

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| apply_approval | <code>number</code> | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
| avatar | <code>string</code> | Group avatar |
| ban_expire_time | <code>number</code> | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently |
| created_at | <code>number</code> | Creation time |
| description | <code>string</code> | Group description |
| ext | <code>string</code> | Group extension information |
| group_id | <code>number</code> | Group id,int64 |
| history_visible | <code>boolean</code> | History chat visibility settings for new members |
| member_invite | <code>boolean</code> | Group member invite settings: false - do not allow invitations, true - allow invitations (default) |
| member_modify | <code>boolean</code> | Group members modify group info settings: false - group members can't modify group info (default), true - group members can modify group info |
| msg_mute_mode | <code>number</code> | Group message blocking mode: 0 - no blocking, 1 - blocking local message notifications, 2 - blocking all, means not receiving messages |
| msg_push_mode | <code>number</code> | Group message push mode: 0 - receive all pushes, 1 - block all pushes, 2 - receive admin and @message pushes, 3 - receive admin message pushes only, 4 - receive @message pushes only |
| name | <code>string</code> | Group name |
| owner_id | <code>number</code> | Group Owner id,int64 |
| read_ack | <code>boolean</code> | Group message read function settings |
| status | <code>number</code> | Group state, 0: normal, 1: dissolved |
| type | <code>number</code> | Group types: 1 - public group, 0 - private group, 2 - chatroom |
| updated_at | <code>number</code> | Update time,int64 |
| count | <code>number</code> | Number of group members |
| capacity | <code>number</code> | GroupCapacity |

### types~BriefGroupInfoAndSettings : <code>object</code> {#module_types__briefgroupinfoandsettings}
Group profile and user settings

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| apply_approval | <code>number</code> | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
| avatar | <code>string</code> | Group avatar |
| capacity | <code>number</code> | GroupCapacity |
| count | <code>number</code> | Number of group members |
| group_id | <code>number</code> | Group id,int64 |
| msg_mute_mode | <code>number</code> | Group message blocking mode: 0 - no blocking, 1 - blocking local message notifications, 2 - blocking all, means not receiving messages |
| msg_push_mode | <code>number</code> | Group message push mode: 0 - receive all pushes, 1 - block all pushes, 2 - receive admin and @message pushes, 3 - receive admin message pushes only, 4 - receive @message pushes only |
| name | <code>string</code> | Group name |
| owner | <code>number</code> | Group Owner id,int64 |
| status | <code>number</code> | Group state, 0: normal, 1: dissolved,int32 |
| type | <code>number</code> | Group types: 1 - public group, 0 - private group, 2 - chatroom.int32 |

### types~GroupMember : <code>object</code> {#module_types__groupmember}
Group member format

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| display_name | <code>string</code> | Group member profile |
| join_time | <code>number</code> | Member join time,int64 |
| user_id | <code>number</code> | User id,int64 |
| avatar | <code>string</code> | AvatarAddress |

### types~GroupMemberBanned : <code>object</code> {#module_types__groupmemberbanned}
Banned members

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| display_name | <code>string</code> | Group member profile |
| join_time | <code>number</code> | Member join time,int64 |
| user_id | <code>number</code> | User id,int64 |
| avatar | <code>string</code> | AvatarAddress |
| expired_time | <code>number</code> | BanExpiration time |

### types~GroupUserRelationResponse : <code>object</code> {#module_types__groupuserrelationresponse}
Group user's request result

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| reason | <code>string</code> | Reason |
| result | <code>string</code> | Results |
| user_id | <code>number</code> | User ID,int64 |

### types~GroupAnnouncement : <code>object</code> {#module_types__groupannouncement}
GroupAnnouncement content

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| author | <code>number</code> | Announcement publisher,int64 |
| content | <code>string</code> | Announcement content |
| created_at | <code>number</code> | Announcement publish time,int64 |
| group_id | <code>number</code> | Group id,int64 |
| id | <code>number</code> | Announcement id,int64 |
| title | <code>string</code> | Announcement tittle |

### types~GroupInfoRequest : <code>object</code> {#module_types__groupinforequest}
Create group

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | Group avatar |
| description | <code>string</code> | Group description |
| name | <code>string</code> | Group name |
| type | <code>number</code> | Group type: 1 for public group, 0 for private group, 2 for chatroom,int32 |
| user_list | <code>Array.&lt;number&gt;</code> | List of user ids invited to join group |

### types~GroupBannedMemberRequest : <code>object</code> {#module_types__groupbannedmemberrequest}
Ban request

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| duration | <code>number</code> | Duration of banned in minutes,int64 |
| group_id | <code>number</code> | Group id,int64 |
| user_list | <code>Array.&lt;number&gt;</code> | User id list |

### types~GroupBlockedListItem : <code>object</code> {#module_types__groupblockedlistitem}
Group blacklist

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| user_id | <code>number</code> | User id,int64 |
| group_id | <code>number</code> | Group id,int64 |
| create_at | <code>string</code> | Creation time |

### types~GroupInvitation : <code>object</code> {#module_types__groupinvitation}
Group invitation info

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |
| inviter_id | <code>number</code> | Inviter ID |
| invitee_id | <code>number</code> | Invitee ID |
| reason | <code>string</code> | Reason |
| status | <code>number</code> | Status: 0 - Pending, 1 - User agreed, 2 - User rejected |
| expire_time | <code>number</code> | Expiration time |
| create_at | <code>string</code> | Creation time |

### types~GroupApplication : <code>object</code> {#module_types__groupapplication}
GroupMembership application information

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |
| applicant_id | <code>number</code> | Applicant ID |
| reason | <code>string</code> | Reason |
| expire_time | <code>number</code> | Expiration time |
| status | <code>number</code> | Status: 0 - Pending, 1 - Agreed, 2 - Rejected |

### types~GroupSharedFile : <code>object</code> {#module_types__groupsharedfile}
Returned format of group shared files

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| created_at | <code>number</code> | int64 |
| file_id | <code>number</code> | Shared file id,int64 |
| group_id | <code>number</code> | Group id,int64 |
| name | <code>string</code> | Shared file name |
| size | <code>number</code> | Shared file size,int64 |
| type | <code>string</code> | Shared file type |
| updated_at | <code>number</code> | int64 |
| uploader | <code>number</code> | Shared file uploader,int64 |
| url | <code>string</code> | Shared file url |

### types~GroupSharedFileResponse : <code>object</code> {#module_types__groupsharedfileresponse}
Result of group shared files deletion

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| file_id | <code>number</code> | FileID |
| reason | <code>string</code> | Reason |
| result | <code>string</code> | Results |

### types~GroupBanAllResponse : <code>object</code> {#module_types__groupbanallresponse}
Result of banning all members

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| ban_expire_time | <code>number</code> | Expiration time of banning all members,int64 |

### types~FileUpload : <code>object</code> {#module_types__fileupload}
File uploading info

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| download_url | <code>string</code> | Download address |
| oss_body_param | <code>object.&lt;string, string&gt;</code> | Additional parameters |
| upload_url | <code>string</code> | Upload address |

### types~FileUploadResult : <code>object</code> {#module_types__fileuploadresult}
File uploading result

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | Download address |

### types~fileUploadProgress : <code>function</code> {#module_types__fileuploadprogress}
FileUpload progressCallback

**Kind**: inner typedef of [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | Progress |
| res.loaded | <code>number</code> | Downloaded bytes |
| res.total | <code>number</code> | Total bytes |

### types~ConversationItem : <code>object</code> {#module_types__conversationitem}
Conversation info

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>number</code> | SessionID |
| content | <code>string</code> | Message content |
| timestamp | <code>string</code> | Message delivery timestamp (milliseconds) |
| type | <code>string</code> | Session type: roster - Single chat, group - Group chat |

### types~UserProfile : <code>object</code> {#module_types__userprofile}
User information

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | Avatar url |
| description | <code>string</code> | Description |
| email | <code>string</code> | Email |
| mobile | <code>string</code> | Mobile number |
| nick_name | <code>string</code> | Nickname |
| private_info | <code>string</code> | Private information, visible only to yourself |
| public_info | <code>string</code> | Public information, visible to both friends and strangers |
| user_id | <code>number</code> | User ID,int64 |
| username | <code>string</code> | Username |

### types~UserSettings : <code>object</code> {#module_types__usersettings}
User settings information

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| auth_answer | <code>string</code> | Answer of verification question |
| auth_mode | <code>number</code> | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests,int32 |
| auth_question | <code>string</code> | Verification question |
| auto_download | <code>boolean</code> | Whether to download automatically |
| group_confirm | <code>boolean</code> | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
| id | <code>number</code> | Set ID |
| no_push | <code>boolean</code> | Whether to turn off push |
| no_push_detail | <code>boolean</code> | Whether to push details |
| no_push_end_hour | <code>number</code> | Start of push no-disturb time,int32 |
| no_push_start_hour | <code>number</code> | End of push no-disturb time,int32 |
| no_sounds | <code>boolean</code> | Whether to mute when message received |
| push_nick_name | <code>string</code> | Push nickname |
| push_token | <code>string</code> | Push token |
| silence_end_time | <code>number</code> | End of push no-reminder time,int32 |
| silence_start_time | <code>number</code> | Start of push no-reminder time,int32 |
| user_id | <code>number</code> | User ID,int64 |
| vibratory | <code>boolean</code> | Whether to vibrate when message received |

### types~Event : <code>string</code> {#module_types__event}
Listening event name

**Kind**: inner typedef of [<code>types</code>](#module_types)  
### types~EventCallback : <code>function</code> {#module_types__eventcallback}
Listening event callback

**Kind**: inner typedef of [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | [<code>flooNotice</code>](#event_floonotice) ¦ [<code>flooError</code>](#event_flooerror) ¦ [<code>loginFail</code>](#event_loginfail) ¦ [<code>loginSuccess</code>](#event_loginsuccess) ¦ [<code>onGroupListUpdate</code>](#event_ongrouplistupdate) ¦ [<code>onGroupMemberChanged</code>](#event_ongroupmemberchanged) ¦ [<code>onGroupMessage</code>](#event_ongroupmessage) ¦ [<code>onInputStatusMessage</code>](#event_oninputstatusmessage) ¦ [<code>onMentionMessage</code>](#event_onmentionmessage) ¦ [<code>onMessageCanceled</code>](#event_onmessagecanceled) ¦ [<code>onMessageDeleted</code>](#event_onmessagedeleted) ¦ [<code>onMessageRecalled</code>](#event_onmessagerecalled) ¦ [<code>onMessageStatusChanged</code>](#event_onmessagestatuschanged) ¦ [<code>onReceiveHistoryMsg</code>](#event_onreceivehistorymsg) ¦ [<code>onRosterInfoUpdate</code>](#event_onrosterinfoupdate) ¦ [<code>onRosterListUpdate</code>](#event_onrosterlistupdate) ¦ [<code>onRosterMessage</code>](#event_onrostermessage) ¦ [<code>onSendingMessageStatusChanged</code>](#event_onsendingmessagestatuschanged) ¦ [<code>onUnreadChange</code>](#event_onunreadchange) ¦ [<code>recentlistUpdate</code>](#event_recentlistupdate) ¦ [<code>onGroupCreated</code>](#event_ongroupcreated) ¦ [<code>onGroupDestoryed</code>](#event_ongroupdestoryed) ¦ [<code>onGroupJoined</code>](#event_ongroupjoined) ¦ [<code>onGroupApplyAccepted</code>](#event_ongroupapplyaccepted) ¦ [<code>onGroupApplyDeclined</code>](#event_ongroupapplydeclined) ¦ [<code>onGroupBaned</code>](#event_ongroupbaned) ¦ [<code>onGroupUnbaned</code>](#event_ongroupunbaned) | Event result |
