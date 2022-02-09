# BMXVideoAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXVideoAttachment.h  

## Properties

<a name="//api/name/duration" title="duration"></a>
### duration

时长

`@property (nonatomic, assign) int duration`

#### Discussion
时长

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailFileLength" title="thumbnailFileLength"></a>
### thumbnailFileLength

thumbnail文件大小

`@property (nonatomic) long long thumbnailFileLength`

#### Discussion
thumbnail文件大小

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailPath" title="thumbnailPath"></a>
### thumbnailPath

缩略图路径

`@property (nonatomic, copy) NSString *thumbnailPath`

#### Discussion
缩略图路径

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailUrl" title="thumbnailUrl"></a>
### thumbnailUrl

缩略图url

`@property (nonatomic, copy) NSString *thumbnailUrl`

#### Discussion
缩略图url

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnaildownLoadStatus" title="thumbnaildownLoadStatus"></a>
### thumbnaildownLoadStatus

视频下载状态

`@property (nonatomic, assign) BMXAttachmentDownloadStatus thumbnaildownLoadStatus`

#### Discussion
视频下载状态

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/videoSize" title="videoSize"></a>
### videoSize

video大小

`@property (nonatomic) CGSize videoSize`

#### Discussion
video大小

#### Declared In
* `BMXVideoAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:duration:videoSize:displayName:conversationId:" title="initWithData:duration:videoSize:displayName:conversationId:"></a>
### initWithData:duration:videoSize:displayName:conversationId:

`- (instancetype)initWithData:(NSData *)*aData* duration:(int)*duration* videoSize:(CGSize)*videoSize* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithData:duration:videoSize:displayName:thumbnailData:conversationId:" title="initWithData:duration:videoSize:displayName:thumbnailData:conversationId:"></a>
### initWithData:duration:videoSize:displayName:thumbnailData:conversationId:

`- (instancetype)initWithData:(NSData *)*aData* duration:(int)*duration* videoSize:(CGSize)*videoSize* displayName:(NSString *)*displayName* thumbnailData:(NSData *)*thumbnailData* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithLocalPath:duration:size:displayName:conversationId:" title="initWithLocalPath:duration:size:displayName:conversationId:"></a>
### initWithLocalPath:duration:size:displayName:conversationId:

`- (instancetype)initWithLocalPath:(NSString *)*aLocalPath* duration:(int)*duration* size:(CGSize)*size* displayName:(NSString *)*aDisplayName* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:" title="initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:"></a>
### initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:

`- (instancetype)initWithLocalPath:(NSString *)*aLocalPath* duration:(int)*duration* size:(CGSize)*size* thumbnailPath:(NSString *)*thumbnailPath* displayName:(NSString *)*aDisplayName* conversationId:(NSString *)*conversationId*`

