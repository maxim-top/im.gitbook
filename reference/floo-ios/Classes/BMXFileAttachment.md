# BMXFileAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXFileAttachment.h  

## Properties

<a name="//api/name/displayName" title="displayName"></a>
### displayName

Display name

`@property (nonatomic, copy) NSString *displayName`

#### Discussion
Display name

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/downLoadStatus" title="downLoadStatus"></a>
### downLoadStatus

Download state

`@property (nonatomic, assign) BMXAttachmentDownloadStatus downLoadStatus`

#### Discussion
Download state

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/fileLength" title="fileLength"></a>
### fileLength

File size

`@property (nonatomic, assign) long long fileLength`

#### Discussion
File size

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/path" title="path"></a>
### path

Local path

`@property (nonatomic, copy) NSString *path`

#### Discussion
Local path

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/url" title="url"></a>
### url

File url

`@property (nonatomic, copy) NSString *url`

#### Discussion
File url

#### Declared In
* `BMXFileAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:displayName:conversationId:" title="initWithData:displayName:conversationId:"></a>
### initWithData:displayName:conversationId:

Initialize file BMXFileAttachment

`- (instancetype)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

#### Parameters

*aData*  
   File data  

*displayName*  
   File name  

*conversationId*  
   Session id  

#### Return Value
BMXFileAttachment

#### Discussion
Initialize file BMXFileAttachment

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/initWithPath:displayName:conversationId:" title="initWithPath:displayName:conversationId:"></a>
### initWithPath:displayName:conversationId:

Initialize file BMXFileAttachment

`- (instancetype)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

#### Parameters

*path*  
   File path  

*displayName*  
   File name  

*conversationId*  
   Session id  

#### Discussion
Initialize file BMXFileAttachment

#### Declared In
* `BMXFileAttachment.h`

