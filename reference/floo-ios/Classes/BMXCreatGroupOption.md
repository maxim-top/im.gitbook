# BMXCreatGroupOption Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXCreatGroupOption.h  

## Properties

<a name="//api/name/announcement" title="announcement"></a>
### announcement

群公告

`@property (nonatomic, copy) NSString *announcement`

#### Discussion
群公告

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
### avatarPath

群头像本地路径

`@property (nonatomic, copy) NSString *avatarPath`

#### Discussion
群头像本地路径

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/extion" title="extion"></a>
### extion

群扩展信息

`@property (nonatomic, copy) NSString *extion`

#### Discussion
群扩展信息

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/groupDescription" title="groupDescription"></a>
### groupDescription

群描述

`@property (nonatomic, copy) NSString *groupDescription`

#### Discussion
群描述

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/isChatroom" title="isChatroom"></a>
### isChatroom

是否聊天室

`@property (nonatomic, assign) BOOL isChatroom`

#### Discussion
是否聊天室

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/members" title="members"></a>
### members

建群时添加的成员

`@property (nonatomic, strong) NSArray *members`

#### Discussion
建群时添加的成员

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/message" title="message"></a>
### message

建群时成员收到的邀请信息

`@property (nonatomic, copy) NSString *message`

#### Discussion
建群时成员收到的邀请信息

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/name" title="name"></a>
### name

群名称

`@property (nonatomic, copy) NSString *name`

#### Discussion
群名称

#### Declared In
* `BMXCreatGroupOption.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithGroupName:groupDescription:isPublic:" title="initWithGroupName:groupDescription:isPublic:"></a>
### initWithGroupName:groupDescription:isPublic:

创建群实体

`- (instancetype)initWithGroupName:(NSString *)*name* groupDescription:(NSString *)*groupDescription* isPublic:(BOOL)*isPublic*`

#### Parameters

*name*  
   必填  

*groupDescription*  
   非必填  

#### Return Value
BMXCreatGroupOption

#### Discussion
创建群实体

#### Declared In
* `BMXCreatGroupOption.h`

