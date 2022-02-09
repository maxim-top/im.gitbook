# BMXVoiceAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXVoiceAttachment.h  

## Properties

<a name="//api/name/duration" title="duration"></a>
### duration

Length

`@property (nonatomic, assign) int duration`

#### Discussion
Length

#### Declared In
* `BMXVoiceAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:displayName:fileLength:duration:conversationId:" title="initWithData:displayName:fileLength:duration:conversationId:"></a>
### initWithData:displayName:fileLength:duration:conversationId:

Initialization<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

`- (instancetype)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* fileLength:(NSInteger)*fileLength* duration:(NSInteger)*duration* conversationId:(NSString *)*conversationId*`

#### Parameters

*aData*  
   Audio Data  

*displayName*  
   Display name  

*duration*  
   Length  

*conversationId*  
   Session Id  

#### Discussion
Initialization<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Declared In
* `BMXVoiceAttachment.h`

<a name="//api/name/initWithPath:displayName:duration:conversationId:" title="initWithPath:displayName:duration:conversationId:"></a>
### initWithPath:displayName:duration:conversationId:

Initialization<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

`- (instancetype)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName* duration:(NSInteger)*duration* conversationId:(NSString *)*conversationId*`

#### Parameters

*path*  
   Audio path  

*displayName*  
   Display  

*duration*  
   Length  

#### Return Value
<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Discussion
Initialization<a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a>

#### Declared In
* `BMXVoiceAttachment.h`

