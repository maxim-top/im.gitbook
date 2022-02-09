# BMXLocationAttachment Class Reference

  **Inherits from** <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a> :   
NSObject  
  **Declared in** BMXLocationAttachment.h  

## Properties

<a name="//api/name/address" title="address"></a>
### address

地址

`@property (nonatomic, copy) NSString *address`

#### Discussion
地址

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

初始化BMXLocationAttachment

`- (instancetype)initWithLatitude:(double)*aLatitude* longitude:(double)*aLongitude* address:(NSString *)*aAddress*`

#### Parameters

*aLatitude*  
   纬度  

*aLongitude*  
   经度  

*aAddress*  
   地址  

#### Return Value
BMXLocationAttachment

#### Discussion
初始化BMXLocationAttachment

#### Declared In
* `BMXLocationAttachment.h`

