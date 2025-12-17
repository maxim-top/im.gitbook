# BMXUserServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol 用户服务监听者

## Instance Methods

### connectStatusDidChanged:

链接状态发生变化

`- (void)connectStatusDidChanged:(BMXConnectStatus)*status*`

#### Parameters

_status_\
连接状态

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userInfoDidUpdated:

同步用户信息更新（其他设备操作发生用户信息变更）

`- (void)userInfoDidUpdated:(BMXUserProfile *)*userProflie*`

#### Discussion

同步用户信息更新（其他设备操作发生用户信息变更）

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userOtherDeviceDidSignIn:

用户在其他设备上登陆

`- (void)userOtherDeviceDidSignIn:(NSInteger)*deviceSN*`

#### Discussion

用户在其他设备上登陆

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userOtherDeviceDidSignOut:

用户在其他设备上登出

`- (void)userOtherDeviceDidSignOut:(NSInteger)*deviceSN*`

#### Discussion

用户在其他设备上登出

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userSignIn:

用户登陆

`- (void)userSignIn:(BMXUserProfile *)*userProflie*`

#### Parameters

_userProflie_\
用户信息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>

```

### userSignOut:userId:

用户登出

`- (void)userSignOut:(BMXError *)*error* userId:(long long)*userId*`

#### Parameters

_error_\
错误码

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserServiceProtocol'></div>
```
