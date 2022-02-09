# BMXVoiceAttachment Class Reference

&nbsp;&nbsp;**Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
&nbsp;&nbsp;**Declared in** BMXVoiceAttachment.h  

## Properties

<a name="//api/name/duration" title="duration"></a>
### duration

时长

`@property (nonatomic, assign) int duration`

#### Discussion
时长

#### Declared In
* `BMXVoiceAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:displayName:fileLength:duration:conversationId:" title="initWithData:displayName:fileLength:duration:conversationId:"></a>
### initWithData:displayName:fileLength:duration:conversationId:

初始化<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

`- (instancetype)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* fileLength:(NSInteger)*fileLength* duration:(NSInteger)*duration* conversationId:(NSString *)*conversationId*`

#### Parameters

*aData*  
&nbsp;&nbsp;&nbsp;音频Data  

*displayName*  
&nbsp;&nbsp;&nbsp;显示名称  

*duration*  
&nbsp;&nbsp;&nbsp;时长  

*conversationId*  
&nbsp;&nbsp;&nbsp;会话Id  

#### Discussion
初始化<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Declared In
* `BMXVoiceAttachment.h`

<a name="//api/name/initWithPath:displayName:duration:conversationId:" title="initWithPath:displayName:duration:conversationId:"></a>
### initWithPath:displayName:duration:conversationId:

初始化<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

`- (instancetype)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName* duration:(NSInteger)*duration* conversationId:(NSString *)*conversationId*`

#### Parameters

*path*  
&nbsp;&nbsp;&nbsp;音频路径  

*displayName*  
&nbsp;&nbsp;&nbsp;显示  

*duration*  
&nbsp;&nbsp;&nbsp;时长  

#### Return Value
<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Discussion
初始化<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Declared In
* `BMXVoiceAttachment.h`

