# BMXVideoAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXFileAttachment.md">BMXFileAttachment</a> :   
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXVideoAttachment.h  

## Properties

<a name="//api/name/duration" title="duration"></a>
### duration

Length

`@property (nonatomic, assign) int duration`

#### Discussion
Length

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailFileLength" title="thumbnailFileLength"></a>
### thumbnailFileLength

thumbnail file size

`@property (nonatomic) long long thumbnailFileLength`

#### Discussion
thumbnail file size

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailPath" title="thumbnailPath"></a>
### thumbnailPath

Thumbnail path

`@property (nonatomic, copy) NSString *thumbnailPath`

#### Discussion
Thumbnail path

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnailUrl" title="thumbnailUrl"></a>
### thumbnailUrl

Thumbnail url

`@property (nonatomic, copy) NSString *thumbnailUrl`

#### Discussion
Thumbnail url

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/thumbnaildownLoadStatus" title="thumbnaildownLoadStatus"></a>
### thumbnaildownLoadStatus

Video download status

`@property (nonatomic, assign) BMXAttachmentDownloadStatus thumbnaildownLoadStatus`

#### Discussion
Video download status

#### Declared In
* `BMXVideoAttachment.h`

<a name="//api/name/videoSize" title="videoSize"></a>
### videoSize

video size

`@property (nonatomic) CGSize videoSize`

#### Discussion
video size

#### Declared In
* `BMXVideoAttachment.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithData:duration:videoSize:displayName:conversationId:" title="initWithData:duration:videoSize:displayName:conversationId:"></a>
### initWithData:duration:videoSize:displayName:conversationId:

`- (instancetype)initWithData:(NSData *)*aData* duration:(int)*duration* videoSize:(CGSize)*videoSize* displayName:(NSString *)*displayName* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithData:duration:videoSize:displayName:thumbnailData:conversationId:" title="initWithData:duration:videoSize:displayName:thumbnailData:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVideoAttachment",function="initWithData:duration:videoSize:displayName:conversationId:" %}{% endlanying_code_snippet %}
```
### initWithData:duration:videoSize:displayName:thumbnailData:conversationId:

`- (instancetype)initWithData:(NSData *)*aData* duration:(int)*duration* videoSize:(CGSize)*videoSize* displayName:(NSString *)*displayName* thumbnailData:(NSData *)*thumbnailData* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithLocalPath:duration:size:displayName:conversationId:" title="initWithLocalPath:duration:size:displayName:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVideoAttachment",function="initWithData:duration:videoSize:displayName:thumbnailData:conversationId:" %}{% endlanying_code_snippet %}
```
### initWithLocalPath:duration:size:displayName:conversationId:

`- (instancetype)initWithLocalPath:(NSString *)*aLocalPath* duration:(int)*duration* size:(CGSize)*size* displayName:(NSString *)*aDisplayName* conversationId:(NSString *)*conversationId*`

<a name="//api/name/initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:" title="initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVideoAttachment",function="initWithLocalPath:duration:size:displayName:conversationId:" %}{% endlanying_code_snippet %}
```
### initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:

`- (instancetype)initWithLocalPath:(NSString *)*aLocalPath* duration:(int)*duration* size:(CGSize)*size* thumbnailPath:(NSString *)*thumbnailPath* displayName:(NSString *)*aDisplayName* conversationId:(NSString *)*conversationId*`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXVideoAttachment",function="initWithLocalPath:duration:size:thumbnailPath:displayName:conversationId:" %}{% endlanying_code_snippet %}
```
