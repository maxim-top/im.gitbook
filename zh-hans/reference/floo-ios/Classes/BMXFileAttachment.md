# BMXFileAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXFileAttachment.h  

## Properties

<a name="//api/name/displayName" title="displayName"></a>
### displayName

显示名称

`@property (nonatomic, copy) NSString *displayName`

#### Discussion
显示名称

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/downLoadStatus" title="downLoadStatus"></a>
### downLoadStatus

下载状态

`@property (nonatomic, assign) BMXAttachmentDownloadStatus downLoadStatus`

#### Discussion
下载状态

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/fileLength" title="fileLength"></a>
### fileLength

文件大小

`@property (nonatomic, assign) long long fileLength`

#### Discussion
文件大小

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/path" title="path"></a>
### path

本地路径

`@property (nonatomic, copy) NSString *path`

#### Discussion
本地路径

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/url" title="url"></a>
### url

文件url

`@property (nonatomic, copy) NSString *url`

#### Discussion
文件url

#### Declared In
* `BMXFileAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:displayName:conversationId:" title="initWithData:displayName:conversationId:"></a>
### initWithData:displayName:conversationId:

初始化文件BMXFileAttachment

`- (instancetype)initWithData:(NSData *)*aData* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

#### Parameters

*aData*  
   文件数据  

*displayName*  
   文件名称  

*conversationId*  
   会话id  

#### Return Value
BMXFileAttachment

#### Discussion
初始化文件BMXFileAttachment

#### Declared In
* `BMXFileAttachment.h`

<a name="//api/name/initWithPath:displayName:conversationId:" title="initWithPath:displayName:conversationId:"></a>
### initWithPath:displayName:conversationId:

初始化文件BMXFileAttachment

`- (instancetype)initWithPath:(NSString *)*path* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

#### Parameters

*path*  
   文件路径  

*displayName*  
   文件名称  

*conversationId*  
   会话id  

#### Discussion
初始化文件BMXFileAttachment

#### Declared In
* `BMXFileAttachment.h`

