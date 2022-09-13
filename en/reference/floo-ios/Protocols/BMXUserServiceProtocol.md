# BMXUserServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXUserServiceProtocol.h  

## Instance Methods

<a name="//api/name/connectStatusDidChanged:" title="connectStatusDidChanged:"></a>
### connectStatusDidChanged:

Channel state changed

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

*status*  
   Network status  

#### Discussion
Channel state changed

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userInfoDidUpdated:" title="userInfoDidUpdated:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="connectStatusDidChanged:" %}{% endlanying_code_snippet %}
```
### userInfoDidUpdated:

Synchronize user information updates (when user information changes in other devices)

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion
Synchronize user information updates (when user information changes in other devices)

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignIn:" title="userOtherDeviceDidSignIn:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userInfoDidUpdated:" %}{% endlanying_code_snippet %}
```
### userOtherDeviceDidSignIn:

User login on another device

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion
User login on another device

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userOtherDeviceDidSignOut:" title="userOtherDeviceDidSignOut:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userOtherDeviceDidSignIn:" %}{% endlanying_code_snippet %}
```
### userOtherDeviceDidSignOut:

User logout on another device

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion
User logout on another device

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignIn:" title="userSignIn:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userOtherDeviceDidSignOut:" %}{% endlanying_code_snippet %}
```
### userSignIn:

User login

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

*userProflie*  
   User information  

#### Discussion
User login

#### Declared In
* `BMXUserServiceProtocol.h`

<a name="//api/name/userSignOut:userId:" title="userSignOut:userId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userSignIn:" %}{% endlanying_code_snippet %}
```
### userSignOut:userId:

User logout

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

*error*  
   Error code  

#### Discussion
User logout

#### Declared In
* `BMXUserServiceProtocol.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserServiceProtocol",function="userSignOut:userId:" %}{% endlanying_code_snippet %}
```
