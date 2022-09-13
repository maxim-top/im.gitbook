# BMXCreatGroupOption Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXCreatGroupOption.h  

## Properties

<a name="//api/name/announcement" title="announcement"></a>
### announcement

Group announcement

`@property (nonatomic, copy) NSString *announcement`

#### Discussion
Group announcement

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/avatarPath" title="avatarPath"></a>
### avatarPath

Local path of group avatar

`@property (nonatomic, copy) NSString *avatarPath`

#### Discussion
Local path of group avatar

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/extion" title="extion"></a>
### extion

Group extension information

`@property (nonatomic, copy) NSString *extion`

#### Discussion
Group extension information

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/groupDescription" title="groupDescription"></a>
### groupDescription

Group description

`@property (nonatomic, copy) NSString *groupDescription`

#### Discussion
Group description

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/isChatroom" title="isChatroom"></a>
### isChatroom

Chatroom or not

`@property (nonatomic, assign) BOOL isChatroom`

#### Discussion
Chatroom or not

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/members" title="members"></a>
### members

Members added when group created

`@property (nonatomic, strong) NSArray *members`

#### Discussion
Members added when group created

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/message" title="message"></a>
### message

Invitation information received by members when group created

`@property (nonatomic, copy) NSString *message`

#### Discussion
Invitation information received by members when group created

#### Declared In
* `BMXCreatGroupOption.h`

<a name="//api/name/name" title="name"></a>
### name

Group name

`@property (nonatomic, copy) NSString *name`

#### Discussion
Group name

#### Declared In
* `BMXCreatGroupOption.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithGroupName:groupDescription:isPublic:" title="initWithGroupName:groupDescription:isPublic:"></a>
### initWithGroupName:groupDescription:isPublic:

Create group entity

`- (instancetype)initWithGroupName:(NSString *)*name* groupDescription:(NSString *)*groupDescription* isPublic:(BOOL)*isPublic*`

#### Parameters

*name*  
   Required  

*groupDescription*  
   Optional  

#### Return Value
BMXCreatGroupOption

#### Discussion
Create group entity

#### Declared In
* `BMXCreatGroupOption.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXCreatGroupOption",function="initWithGroupName:groupDescription:isPublic:" %}{% endlanying_code_snippet %}
```
