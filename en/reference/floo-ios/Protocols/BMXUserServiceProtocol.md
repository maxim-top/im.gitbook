# BMXUserServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol User service listener

## Instance Methods

### connectStatusDidChanged:

Connection status changed

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

_status_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userInfoDidUpdated:

User information updated

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userOtherDeviceDidSignIn:

User signed in the other device

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userOtherDeviceDidSignOut:

User signed out the other device

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userSignIn:

User signed in

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

_userProflie_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userSignOut:userId:

User signed out

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>
```
