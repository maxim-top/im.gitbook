# BMXMessageConfig Class Reference

&nbsp;&nbsp;**Inherits from** NSObject  
&nbsp;&nbsp;**Declared in** BMXMessageConfig.h  

## Properties

<a name="//api/name/groupMemberList" title="groupMemberList"></a>
### groupMemberList

`@property (nonatomic, strong) NSArray&lt;NSString*&gt; *groupMemberList`

<a name="//api/name/mentionAll" title="mentionAll"></a>
### mentionAll

`@property (nonatomic, assign) BOOL mentionAll`

<a name="//api/name/mentionList" title="mentionList"></a>
### mentionList

`@property (nonatomic, strong) NSArray&lt;NSString*&gt; *mentionList`

<a name="//api/name/mentionMessage" title="mentionMessage"></a>
### mentionMessage

`@property (nonatomic, copy) NSString *mentionMessage`

<a name="//api/name/pushMessage" title="pushMessage"></a>
### pushMessage

`@property (nonatomic, copy) NSString *pushMessage`

<a name="//api/name/senderName" title="senderName"></a>
### senderName

`@property (nonatomic, copy) NSString *senderName`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/addGroupMember:" title="addGroupMember:"></a>
### addGroupMember:

`- (void)addGroupMember:(NSString *)*rosterId*`

<a name="//api/name/clealerGroupMemberList" title="clealerGroupMemberList"></a>
### clealerGroupMemberList

`- (void)clealerGroupMemberList`

<a name="//api/name/initConfigWithMentionAll:" title="initConfigWithMentionAll:"></a>
### initConfigWithMentionAll:

`- (instancetype)initConfigWithMentionAll:(BOOL)*isMentionAll*`

<a name="//api/name/removeGroupMember:" title="removeGroupMember:"></a>
### removeGroupMember:

`- (void)removeGroupMember:(NSString *)*rosterId*`

<a name="//api/name/username" title="username"></a>
### username

`- (NSString *)username`

