# BMXImageAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXImageAttachment.h  

## Properties

<a name="//api/name/pictureSize" title="pictureSize"></a>
### pictureSize

`@property (nonatomic) CGSize pictureSize`

<a name="//api/name/thumbnailDownLoadStatus" title="thumbnailDownLoadStatus"></a>
### thumbnailDownLoadStatus

`@property (nonatomic, assign) BMXAttachmentDownloadStatus thumbnailDownLoadStatus`

<a name="//api/name/thumbnailFileLength" title="thumbnailFileLength"></a>
### thumbnailFileLength

`@property (nonatomic, assign) long long thumbnailFileLength`

<a name="//api/name/thumbnailPath" title="thumbnailPath"></a>
### thumbnailPath

`@property (nonatomic, copy) NSString *thumbnailPath`

<a name="//api/name/thumbnailSize" title="thumbnailSize"></a>
### thumbnailSize

`@property (nonatomic) CGSize thumbnailSize`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:thumbnailData:imageSize:conversationId:" title="initWithData:thumbnailData:imageSize:conversationId:"></a>
### initWithData:thumbnailData:imageSize:conversationId:

`- (instancetype)initWithData:(NSData *)*aData* thumbnailData:(NSData *)*aThumbnailData* imageSize:(CGSize)*imageSize* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithLocalPath:thumbnailPath:size:displayName:conversationId:" title="initWithLocalPath:thumbnailPath:size:displayName:conversationId:"></a>
### initWithLocalPath:thumbnailPath:size:displayName:conversationId:

`- (instancetype)initWithLocalPath:(NSString *)*aLocalPath* thumbnailPath:(NSString *)*aThumbnailPath* size:(CGSize)*size* displayName:(NSString *)*aDisplayName* conversationId:(NSString *)*conversationId*`

<a name="//api/name/setReceiveThumbnailUrl:thumbnailSize:fileLength:" title="setReceiveThumbnailUrl:thumbnailSize:fileLength:"></a>
### setReceiveThumbnailUrl:thumbnailSize:fileLength:

设置接收图片消息缩略图

`- (void)setReceiveThumbnailUrl:(NSString *)*url* thumbnailSize:(CGSize)*thumbnailSize* fileLength:(long long)*fileLength*`

#### Discussion
设置接收图片消息缩略图

#### Declared In
* `BMXImageAttachment.h`

<a name="//api/name/setsendThumbnailPath:" title="setsendThumbnailPath:"></a>
### setsendThumbnailPath:

设置发送图片消息缩略图

`- (void)setsendThumbnailPath:(NSString *)*path*`

#### Discussion
设置发送图片消息缩略图

#### Declared In
* `BMXImageAttachment.h`

