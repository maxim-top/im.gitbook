# BMXLocationAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXLocationAttachment.h  

## Properties

<a name="//api/name/address" title="address"></a>
### address

Address

`@property (nonatomic, copy) NSString *address`

#### Discussion
Address

#### Declared In
* `BMXLocationAttachment.h`

<a name="//api/name/latitude" title="latitude"></a>
### latitude

`@property (nonatomic) double latitude`

<a name="//api/name/longitude" title="longitude"></a>
### longitude

`@property (nonatomic) double longitude`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithLatitude:longitude:address:" title="initWithLatitude:longitude:address:"></a>
### initWithLatitude:longitude:address:

Initialize BMXLocationAttachment

`- (instancetype)initWithLatitude:(double)*aLatitude* longitude:(double)*aLongitude* address:(NSString *)*aAddress*`

#### Parameters

*aLatitude*  
   Latitude  

*aLongitude*  
   Longitude  

*aAddress*  
   Address  

#### Return Value
BMXLocationAttachment

#### Discussion
Initialize BMXLocationAttachment

#### Declared In
* `BMXLocationAttachment.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXLocationAttachment",function="initWithLatitude:longitude:address:" %}{% endlanying_code_snippet %}
```
