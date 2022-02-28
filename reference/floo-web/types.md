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
    * [~RosterItem](#module_types..rosteritem) : <code>object</code>
    * [~UserSettings](#module_types..usersettings) : <code>object</code>
    * [~UserProfile](#module_types..userprofile) : <code>object</code>
    * [~Meta](#module_types..meta) : <code>object</code>
    * [~RosterApplication](#module_types..rosterapplication) : <code>object</code>
    * [~GroupInfoAndSettings](#module_types..groupinfoandsettings) : <code>object</code>
    * [~BriefGroupInfoAndSettings](#module_types..briefgroupinfoandsettings) : <code>object</code>
    * [~GroupMember](#module_types..groupmember) : <code>object</code>
    * [~GroupMemberBanned](#module_types..groupmemberbanned) : <code>object</code>
    * [~GroupUserRelationResponse](#module_types..groupuserrelationresponse) : <code>object</code>
    * [~GroupAnnouncement](#module_types..groupannouncement) : <code>object</code>
    * [~GroupInfoRequest](#module_types..groupinforequest) : <code>object</code>
    * [~GroupBannedMemberRequest](#module_types..groupbannedmemberrequest) : <code>object</code>
    * [~GroupBlockedListItem](#module_types..groupblockedlistitem) : <code>object</code>
    * [~GroupInvitation](#module_types..groupinvitation) : <code>object</code>
    * [~GroupApplication](#module_types..groupapplication) : <code>object</code>
    * [~GroupSharedFile](#module_types..groupsharedfile) : <code>object</code>
    * [~GroupSharedFileResponse](#module_types..groupsharedfileresponse) : <code>object</code>
    * [~GroupBanAllResponse](#module_types..groupbanallresponse) : <code>object</code>
    * [~FileUpload](#module_types..fileupload) : <code>object</code>
    * [~FileUploadResult](#module_types..fileuploadresult) : <code>object</code>
    * [~fileUploadProgress](#module_types..fileuploadprogress) : <code>function</code>
    * [~ConversationItem](#module_types..conversationitem) : <code>object</code>
    * [~UserProfile](#module_types..userprofile) : <code>object</code>
    * [~UserSettings](#module_types..usersettings) : <code>object</code>
    * [~Event](#module_types..event) : <code>string</code>
    * [~EventCallback](#module_types..eventcallback) : <code>function</code>

### "flooNotice" (res) {#event_floonotice}
Floo通知

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | 结果 |
| res.category | <code>string</code> | 类别 |
| res.desc | <code>string</code> | 描述 |

**Example**  
```js
{category: 'loginMessage',desc: 'socket connecting...'} // 开始建连接
{category: 'loginMessage',desc: 'socket connect success...'} // 连接成功
{category: 'loginMessage',desc: 'logining socket service...'} // 开始登录
{category: 'loginMessage',desc: 'login socket failure ......'} // 登录失败
{category: 'loginMessage',desc: 'login socket success.....'} // 登录成功
{category: 'loginMessage', desc: 'getting token...' } //获取token
{category: 'loginMessage',desc: 'token sucecc, getting roster lists..'} // 获取token成功，开始获取好友列表
{category: 'loginMessage',desc: 'get roster list failure:' + ex.message} // 获取好友列表失败
{category: 'action', desc: 'relogin' } // 需要自动登录
{category: 'action', desc: 'relogin_manually' }  // 需要手动登录
{category: 'conversation_deleted',desc: { id, source:'user_operation' }} // 会话被删除。ID：会话ID， source: 来源
{category: 'userNotice', desc:'PASSWORD_CHANGED'} // 用户密码改变
{category: 'userNotice', desc:'FROZEN'} // 用户账户被封禁
{category: 'userNotice', desc:'REMOVED'} // 用户被删除
{category: 'userNotice', desc:'KICK_BY_SAME_DEVICE'} // 当前设备被相同设备踢下线
{category: 'userNotice', desc:'KICKED_BY_OTHER_DEVICE'} // 当前设备被其它设备踢下线
{category: 'userNotice', desc:'INFO_UPDATED'} // 用户信息改变：profile或setting
{category: 'userNotice', desc:'DEVICE_LOGIN'} // 用户其它设备上线
{category: 'userNotice', desc:'DEVICE_LOGOUT'} // 用户其它设备下线
{category: 'userNotice', desc:'DEVICE_ADDED'} // 新设备通知
{category: 'userNotice', desc:'DEVICE_REMOVED'} // 设备被移除的通知
{category: 'userNotice', desc:'CLUSTER_CHANGED'} // 用户所在集群改变 需要重新登录
```
### "flooError" (res) {#event_flooerror}
Floo错误

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.category | <code>string</code> | 类别 |
| res.desc | <code>string</code> | 描述 |

**Example**  
```js
{category: 'USER_BANNED', desc:'用户被禁言'}
{category: 'USER_FROZEN', desc:'用户被冻结，请联系App管理员。'}
{category: 'APP_FROZEN', desc:'APP 被冻结，请登陆美信拓扑控制台查看详情。'}
{category: 'LICENSE', desc:'无效 LICENSE，请确认服务已按时付费。'}
{category: 'LICENSE', desc:'超出 LICENSE 用户数限制，请购买更高规格服务。'}
{category: 'DNS_FAILED', desc: dnsServer } // DNS错误: 无法访问
```
### "loginFail" (desc) {#event_loginfail}
登录失败

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| desc | <code>string</code> | 失败原因 |

### "loginSuccess" (res) {#event_loginsuccess}
登录成功

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | 空对象 |

### "onGroupListUpdate" (meta) {#event_ongrouplistupdate}
群列表更新

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) \| <code>undefined</code> | 通知消息内容 |

### "onGroupMemberChanged" (groupId) {#event_ongroupmemberchanged}
群成员列表更新

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| groupId | <code>number</code> | 群ID |

### "onGroupMessage" (meta) {#event_ongroupmessage}
收到群消息

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 消息内容 |

### "onInputStatusMessage" (res) {#event_oninputstatusmessage}
对方正在输入

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.ext | <code>string</code> | 扩展字段 |
| res.from | <code>string</code> | 发送者用户ID |
| res.to | <code>string</code> | 接收者用户ID |

### "onMentionMessage" (meta) {#event_onmentionmessage}
收到群组&#64;消息

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 消息内容 |

### "onMessageCanceled" (res) {#event_onmessagecanceled}
消息被取消已读

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | 会话ID |
| res.mid | <code>string</code> | 消息ID |

### "onMessageDeleted" (res) {#event_onmessagedeleted}
消息被删除

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | 会话ID |
| res.mid | <code>string</code> | 消息ID |

### "onMessageRecalled" (res) {#event_onmessagerecalled}
消息被撤回

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | 会话ID |
| res.mid | <code>string</code> | 消息ID |

### "onMessageStatusChanged" (res) {#event_onmessagestatuschanged}
消息状态变更：撤回/删除/已读

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.uid | <code>string</code> | 会话ID |
| res.mid | <code>string</code> | 消息ID |

### "onReceiveHistoryMsg" (res) {#event_onreceivehistorymsg}
收到历史消息

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.next | <code>number</code> | 下次取历史消息的key |

### "onRosterInfoUpdate" (res) {#event_onrosterinfoupdate}
好友信息变更

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.rosterIds | <code>Array.&lt;number&gt;</code> | 好友的用户ID列表 |

### "onRosterListUpdate" (meta) {#event_onrosterlistupdate}
好友列表变更

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 好友通知的消息内容 |

### "onRosterMessage" (meta) {#event_onrostermessage}
收到单聊消息

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 消息内容 |

### "onSendingMessageStatusChanged" (res) {#event_onsendingmessagestatuschanged}
消息发送状态变更

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> |  |
| res.status: | <code>number</code> | 发送状态，取值为sending|failed|sent |
| res.mid: | <code>number</code> | 客户端生成的client_mid |

### "onUnreadChange" (cid) {#event_onunreadchange}
未读数改变

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| cid | <code>number</code> | 会话ID |

### "recentlistUpdate" {#event_recentlistupdate}
最近会话更新

**Kind**: event emitted by [<code>types</code>](#module_types)  
### "onGroupCreated" (meta) {#event_ongroupcreated}
群组创建通知

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupDestoryed" (meta) {#event_ongroupdestoryed}
群组解散通知

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupJoined" (meta) {#event_ongroupjoined}
成员入群通知

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupApplyAccepted" (meta) {#event_ongroupapplyaccepted}
群申请被通过

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupApplyDeclined" (meta) {#event_ongroupapplydeclined}
群申请被拒绝

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupBaned" (meta) {#event_ongroupbaned}
被群禁言

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### "onGroupUnbaned" (meta) {#event_ongroupunbaned}
被群取消禁言

**Kind**: event emitted by [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| meta | [<code>Meta</code>](#module_types..meta) | 群通知的消息内容 |

### types~RosterItem : <code>object</code> {#module_types..rosteritem}
好友信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| alias | <code>string</code> | 别名 |
| auth_mode | <code>number</code> | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请,int32 |
| auth_question | <code>string</code> | 验证问题 |
| avatar | <code>string</code> | 头像 |
| description | <code>string</code> | 描述信息 |
| ext | <code>string</code> | 扩展信息 |
| mute_notification | <code>boolean</code> | 是否接收消息提醒 |
| nick_name | <code>string</code> | 昵称或名称 |
| public_info | <code>string</code> | 公开信息，好友和陌生人可见 |
| relation | <code>number</code> | 关系: 0 - 好友，1 - 被删除，2 - 陌生人, int32 |
| user_id | <code>number</code> | 好友用户ID,int64 |
| username | <code>string</code> | 用户名 |

### types~UserSettings : <code>object</code> {#module_types..usersettings}
用户设置信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| auth_answer | <code>string</code> | 验证问题答案 |
| auth_mode | <code>number</code> | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请,int32 |
| auth_question | <code>string</code> | 验证问题 |
| auto_download | <code>boolean</code> | 是否自动下载 |
| group_confirm | <code>boolean</code> | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
| id | <code>number</code> | 用户ID, int64 |
| no_push | <code>boolean</code> | 是否关闭推送消息 |
| no_push_detail | <code>boolean</code> | 是否推送详情 |
| no_push_end_hour | <code>number</code> | 推送免打扰结束时间,int32 |
| no_push_start_hour | <code>number</code> | 推送免打扰开始时间,int32 |
| no_sounds | <code>boolean</code> | 收到消息时是否静音 |
| push_nick_name | <code>string</code> | 推送昵称 |
| push_token | <code>string</code> | 推送token |
| silence_end_time | <code>number</code> | 推送不提醒结束时间,int32 |
| silence_start_time | <code>number</code> | 推送不提醒开始时间,int32 |
| user_id | <code>number</code> | 用户ID,int64 |
| vibratory | <code>boolean</code> | 收到消息时否振动 |

### types~UserProfile : <code>object</code> {#module_types..userprofile}
用户信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | 头像 url |
| description | <code>string</code> | 描述信息 |
| email | <code>string</code> | 邮箱 |
| mobile | <code>string</code> | 手机号码 |
| nick_name | <code>string</code> | 昵称 |
| private_info | <code>string</code> | 私有信息，仅自己可见 |
| public_info | <code>string</code> | 公开信息，好友和陌生人可见 |
| user_id | <code>number</code> | 用户ID,int64 |
| username | <code>string</code> | 用户名 |

### types~Meta : <code>object</code> {#module_types..meta}
消息体

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>string</code> | 消息ID |
| from | <code>string</code> | 发送者 |
| to | <code>string</code> | 接收者 |
| content | <code>string</code> | 消息内容 |
| type | <code>string</code> | 消息类型： text - 文本, image - 图片， audio - 语音, video - 视频，file - 文件, location - 位置， command - 命令, forward - 转发 |
| ext | <code>string</code> \| <code>object</code> | 扩展字段 |
| config | <code>string</code> \| <code>object</code> | SDK扩展字段 |
| attach | <code>string</code> \| <code>object</code> | 附件信息 |
| status | <code>number</code> | 消息状态： 0 - 未读, 1 - 已投递, 2 - 已读 |
| timestamp | <code>string</code> | 消息发送时间戳（毫秒） |
| toType | <code>string</code> | 接收者类型： roster - 好友， group - 群组 |

### types~RosterApplication : <code>object</code> {#module_types..rosterapplication}
加好友申请列表项

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| expired_time | <code>number</code> | 过期时间,int64 |
| reason | <code>string</code> | 申请描述 |
| status | <code>number</code> | 状态： 0 - 等待确认， 1 - 接受， 2 - 拒绝。 int32 |
| user_id | <code>number</code> | 发起加好友申请的用户ID,int64 |

### types~GroupInfoAndSettings : <code>object</code> {#module_types..groupinfoandsettings}
群信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| apply_approval | <code>number</code> | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
| avatar | <code>string</code> | 群头像 |
| ban_expire_time | <code>number</code> | 全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言 |
| created_at | <code>number</code> | 创建时间 |
| description | <code>string</code> | 群描述 |
| ext | <code>string</code> | 群扩展信息 |
| group_id | <code>number</code> | 群id,int64 |
| history_visible | <code>boolean</code> | 新成员可见历史聊天记录设置 |
| member_invite | <code>boolean</code> | 群成员邀请设置: false - 不允许邀请, true - 允许邀请(默认) |
| member_modify | <code>boolean</code> | 群成员修改群信息设置:  false - 群成员不能修改群信息(默认), true - 群成员可以修改群信息 |
| msg_mute_mode | <code>number</code> | 群消息屏蔽模式: 0 - 表示不屏蔽, 1 - 表示屏蔽本地消息通知, 2 - 表示屏蔽消息，不接收消息 |
| msg_push_mode | <code>number</code> | 群消息推送模式：0 - 接收所有推送，1 - 不接受推送，2 - 接收管理员和@消息推送， 3 - 只接收管理员消息推送， 4 - 只接收&#64;消息推送 |
| name | <code>string</code> | 群名称 |
| owner_id | <code>number</code> | 群主id,int64 |
| read_ack | <code>boolean</code> | 群消息已读功能设置 |
| status | <code>number</code> | 群状态, 0：正常, 1：已解散 |
| type | <code>number</code> | 群类型: 1表示公开群，0表示私有群, 2表示聊天室 |
| updated_at | <code>number</code> | 更新时间,int64 |
| count | <code>number</code> | 群成员数 |
| capacity | <code>number</code> | 群容量 |

### types~BriefGroupInfoAndSettings : <code>object</code> {#module_types..briefgroupinfoandsettings}
群简要信息及用户设置

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| apply_approval | <code>number</code> | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
| avatar | <code>string</code> | 群头像 |
| capacity | <code>number</code> | 群容量 |
| count | <code>number</code> | 群成员数 |
| group_id | <code>number</code> | 群id,int64 |
| msg_mute_mode | <code>number</code> | 群消息屏蔽模式: 0 - 表示不屏蔽, 1 - 表示屏蔽本地消息通知, 2 - 表示屏蔽消息，不接收消息 |
| msg_push_mode | <code>number</code> | 群消息推送模式：0 - 接收所有推送，1 - 不接受推送，2 - 接收管理员和@消息推送， 3 - 只接收管理员消息推送， 4 - 只接收&#64;消息推送 |
| name | <code>string</code> | 群名称 |
| owner | <code>number</code> | 群主id,int64 |
| status | <code>number</code> | 群状态, 0：正常, 1：已解散,int32 |
| type | <code>number</code> | 群类型: 1表示公开群，0表示私有群, 2表示聊天室。int32 |

### types~GroupMember : <code>object</code> {#module_types..groupmember}
群成员格式

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| display_name | <code>string</code> | 成员群名片 |
| join_time | <code>number</code> | 成员入群时间,int64 |
| user_id | <code>number</code> | 用户id,int64 |
| avatar | <code>string</code> | 头像地址 |

### types~GroupMemberBanned : <code>object</code> {#module_types..groupmemberbanned}
禁言成员

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| display_name | <code>string</code> | 成员群名片 |
| join_time | <code>number</code> | 成员入群时间,int64 |
| user_id | <code>number</code> | 用户id,int64 |
| avatar | <code>string</code> | 头像地址 |
| expired_time | <code>number</code> | 禁言过期时间 |

### types~GroupUserRelationResponse : <code>object</code> {#module_types..groupuserrelationresponse}
群用户请求结果

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| reason | <code>string</code> | 原因 |
| result | <code>string</code> | 结果 |
| user_id | <code>number</code> | 用户ID，int64 |

### types~GroupAnnouncement : <code>object</code> {#module_types..groupannouncement}
群公告内容

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| author | <code>number</code> | 公告发布者,int64 |
| content | <code>string</code> | 公告内容 |
| created_at | <code>number</code> | 公告发布时间,int64 |
| group_id | <code>number</code> | 群id,int64 |
| id | <code>number</code> | 公告id,int64 |
| title | <code>string</code> | 公告标题 |

### types~GroupInfoRequest : <code>object</code> {#module_types..groupinforequest}
创建群

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | 群头像 |
| description | <code>string</code> | 群描述 |
| name | <code>string</code> | 群名称 |
| type | <code>number</code> | 群类型 1表示公开群，0表示私有群, 2表示聊天室,int32 |
| user_list | <code>Array.&lt;number&gt;</code> | 邀请入群的用户id列表 |

### types~GroupBannedMemberRequest : <code>object</code> {#module_types..groupbannedmemberrequest}
禁言请求

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| duration | <code>number</code> | 禁言时长，单位为分钟,int64 |
| group_id | <code>number</code> | 群id,int64 |
| user_list | <code>Array.&lt;number&gt;</code> | 用户id列表 |

### types~GroupBlockedListItem : <code>object</code> {#module_types..groupblockedlistitem}
群组黑名单

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| user_id | <code>number</code> | 用户id,int64 |
| group_id | <code>number</code> | 群id,int64 |
| create_at | <code>string</code> | 创建时间 |

### types~GroupInvitation : <code>object</code> {#module_types..groupinvitation}
群组邀请信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群ID |
| inviter_id | <code>number</code> | 邀请者ID |
| invitee_id | <code>number</code> | 被邀请者ID |
| reason | <code>string</code> | 原因 |
| status | <code>number</code> | 状态： 0 - 待处理，1 - 用户同意，2 - 用户拒绝 |
| expire_time | <code>number</code> | 过期时间 |
| create_at | <code>string</code> | 创建时间 |

### types~GroupApplication : <code>object</code> {#module_types..groupapplication}
群申请信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群ID |
| applicant_id | <code>number</code> | 申请者ID |
| reason | <code>string</code> | 原因 |
| expire_time | <code>number</code> | 过期时间 |
| status | <code>number</code> | 状态： 0 - 待处理，1 - 同意，2 - 拒绝 |

### types~GroupSharedFile : <code>object</code> {#module_types..groupsharedfile}
群共享文件返回格式

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| created_at | <code>number</code> | int64 |
| file_id | <code>number</code> | 共享文件id,int64 |
| group_id | <code>number</code> | 群id,int64 |
| name | <code>string</code> | 共享文件名称 |
| size | <code>number</code> | 共享文件大小,int64 |
| type | <code>string</code> | 共享文件类型 |
| updated_at | <code>number</code> | int64 |
| uploader | <code>number</code> | 共享文件上传者,int64 |
| url | <code>string</code> | 共享文件url |

### types~GroupSharedFileResponse : <code>object</code> {#module_types..groupsharedfileresponse}
删除群共享文件结果

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| file_id | <code>number</code> | 文件ID |
| reason | <code>string</code> | 原因 |
| result | <code>string</code> | 结果 |

### types~GroupBanAllResponse : <code>object</code> {#module_types..groupbanallresponse}
全员禁言结果

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| ban_expire_time | <code>number</code> | 全员禁言过期时间,int64 |

### types~FileUpload : <code>object</code> {#module_types..fileupload}
文件上传信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| download_url | <code>string</code> | 下载地址 |
| oss_body_param | <code>object.&lt;string, string&gt;</code> | 额外参数 |
| upload_url | <code>string</code> | 上传地址 |

### types~FileUploadResult : <code>object</code> {#module_types..fileuploadresult}
文件上传结果

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | 下载地址 |

### types~fileUploadProgress : <code>function</code> {#module_types..fileuploadprogress}
文件上传进度回调

**Kind**: inner typedef of [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | <code>object</code> | 进度 |
| res.loaded | <code>number</code> | 已下载字节数 |
| res.total | <code>number</code> | 总字节数 |

### types~ConversationItem : <code>object</code> {#module_types..conversationitem}
会话信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>number</code> | 会话ID |
| content | <code>string</code> | 消息内容 |
| timestamp | <code>string</code> | 消息发送时间戳（毫秒） |
| type | <code>string</code> | 会话类型： roster - 单聊， group - 群聊 |

### types~UserProfile : <code>object</code> {#module_types..userprofile}
用户信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| avatar | <code>string</code> | 头像 url |
| description | <code>string</code> | 描述信息 |
| email | <code>string</code> | 邮箱 |
| mobile | <code>string</code> | 手机号码 |
| nick_name | <code>string</code> | 昵称 |
| private_info | <code>string</code> | 私有信息，仅自己可见 |
| public_info | <code>string</code> | 公开信息，好友和陌生人可见 |
| user_id | <code>number</code> | 用户ID,int64 |
| username | <code>string</code> | 用户名 |

### types~UserSettings : <code>object</code> {#module_types..usersettings}
用户设置信息

**Kind**: inner typedef of [<code>types</code>](#module_types)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| auth_answer | <code>string</code> | 验证问题答案 |
| auth_mode | <code>number</code> | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请,int32 |
| auth_question | <code>string</code> | 验证问题 |
| auto_download | <code>boolean</code> | 是否自动下载 |
| group_confirm | <code>boolean</code> | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
| id | <code>number</code> | 设置ID |
| no_push | <code>boolean</code> | 是否关闭推送消息 |
| no_push_detail | <code>boolean</code> | 是否推送详情 |
| no_push_end_hour | <code>number</code> | 推送免打扰结束时间,int32 |
| no_push_start_hour | <code>number</code> | 推送免打扰开始时间,int32 |
| no_sounds | <code>boolean</code> | 收到消息时是否静音 |
| push_nick_name | <code>string</code> | 推送昵称 |
| push_token | <code>string</code> | 推送token |
| silence_end_time | <code>number</code> | 推送不提醒结束时间,int32 |
| silence_start_time | <code>number</code> | 推送不提醒开始时间,int32 |
| user_id | <code>number</code> | 用户ID,int64 |
| vibratory | <code>boolean</code> | 收到消息时否振动 |

### types~Event : <code>string</code> {#module_types..event}
监听事件名称

**Kind**: inner typedef of [<code>types</code>](#module_types)  
### types~EventCallback : <code>function</code> {#module_types..eventcallback}
监听事件回调

**Kind**: inner typedef of [<code>types</code>](#module_types)  

| Param | Type | Description |
| --- | --- | --- |
| res | [<code>flooNotice</code>](#event_floonotice) \| [<code>flooError</code>](#event_flooerror) \| [<code>loginFail</code>](#event_loginfail) \| [<code>loginSuccess</code>](#event_loginsuccess) \| [<code>onGroupListUpdate</code>](#event_ongrouplistupdate) \| [<code>onGroupMemberChanged</code>](#event_ongroupmemberchanged) \| [<code>onGroupMessage</code>](#event_ongroupmessage) \| [<code>onInputStatusMessage</code>](#event_oninputstatusmessage) \| [<code>onMentionMessage</code>](#event_onmentionmessage) \| [<code>onMessageCanceled</code>](#event_onmessagecanceled) \| [<code>onMessageDeleted</code>](#event_onmessagedeleted) \| [<code>onMessageRecalled</code>](#event_onmessagerecalled) \| [<code>onMessageStatusChanged</code>](#event_onmessagestatuschanged) \| [<code>onReceiveHistoryMsg</code>](#event_onreceivehistorymsg) \| [<code>onRosterInfoUpdate</code>](#event_onrosterinfoupdate) \| [<code>onRosterListUpdate</code>](#event_onrosterlistupdate) \| [<code>onRosterMessage</code>](#event_onrostermessage) \| [<code>onSendingMessageStatusChanged</code>](#event_onsendingmessagestatuschanged) \| [<code>onUnreadChange</code>](#event_onunreadchange) \| [<code>recentlistUpdate</code>](#event_recentlistupdate) \| [<code>onGroupCreated</code>](#event_ongroupcreated) \| [<code>onGroupDestoryed</code>](#event_ongroupdestoryed) \| [<code>onGroupJoined</code>](#event_ongroupjoined) \| [<code>onGroupApplyAccepted</code>](#event_ongroupapplyaccepted) \| [<code>onGroupApplyDeclined</code>](#event_ongroupapplydeclined) \| [<code>onGroupBaned</code>](#event_ongroupbaned) \| [<code>onGroupUnbaned</code>](#event_ongroupunbaned) | 事件结果 |
