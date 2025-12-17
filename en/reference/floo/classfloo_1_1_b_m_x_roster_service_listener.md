---
title: floo::BMXRosterServiceListener
summary: Friend change listener
---

# floo::BMXRosterServiceListener

Friend change listener

`#include <bmx_roster_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener"><strong>BMXRosterServiceListener</strong></a>()<br>Constructor</p>                                                                                                                                                                  |
| virtual      | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-~bmxrosterservicelistener"><strong>~BMXRosterServiceListener</strong></a>()<br>Destructor</p>                                                                                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendadded"><strong>onFriendAdded</strong></a>(int64_t sponsorId, int64_t recipientId)<br>Add friend</p>                                                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved"><strong>onFriendRemoved</strong></a>(int64_t sponsorId, int64_t recipientId)<br>Delete friend</p>                                                                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(int64_t sponsorId, int64_t recipientId, const std::string &#x26; message)<br>Request of adding friend received</p>                                                                                                  |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(int64_t sponsorId, int64_t recipientId)<br>Request of adding friend approved</p>                                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(int64_t sponsorId, int64_t recipientId, const std::string &#x26; reason)<br>Request of adding friend rejected</p>                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(int64_t sponsorId, int64_t recipientId)<br>Add to blacklist</p>                                                                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(int64_t sponsorId, int64_t recipientId)<br>Delete blacklist</p>                                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate"><strong>onRosterInfoUpdate</strong></a>(BMXRosterItemPtr item)<br>Update user information</p>                                                                                                                                             |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate"><strong>onRosterListUpdate</strong></a>()<br>Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information</p>                                |
| void         | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice"><strong>registerRosterService</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service.md">BMXRosterService</a> * service)<br>Register BMXRosterService to which BMXRosterServiceListener is bound (automatic registration in SDK)</p> |

## Protected Attributes

|                                                              | Name                                                                             |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) \* | [**mService**](classfloo_1_1_b_m_x_roster_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXRosterServiceListener

```cpp
inline BMXRosterServiceListener()
```

Constructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function \~BMXRosterServiceListener

```cpp
inline virtual ~BMXRosterServiceListener()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onFriendAdded

```cpp
inline virtual void onFriendAdded(
    int64_t sponsorId,
    int64_t recipientId
)
```

Add friend

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onFriendRemoved

```cpp
inline virtual void onFriendRemoved(
    int64_t sponsorId,
    int64_t recipientId
)
```

Delete friend

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onApplied

```cpp
inline virtual void onApplied(
    int64_t sponsorId,
    int64_t recipientId,
    const std::string & message
)
```

Request of adding friend received

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient
* **message** Friend request message

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onApplicationAccepted

```cpp
inline virtual void onApplicationAccepted(
    int64_t sponsorId,
    int64_t recipientId
)
```

Request of adding friend approved

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onApplicationDeclined

```cpp
inline virtual void onApplicationDeclined(
    int64_t sponsorId,
    int64_t recipientId,
    const std::string & reason
)
```

Request of adding friend rejected

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient
* **reason** Reason for application rejection

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onBlockListAdded

```cpp
inline virtual void onBlockListAdded(
    int64_t sponsorId,
    int64_t recipientId
)
```

Add to blacklist

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onBlockListRemoved

```cpp
inline virtual void onBlockListRemoved(
    int64_t sponsorId,
    int64_t recipientId
)
```

Delete blacklist

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onRosterInfoUpdate

```cpp
inline virtual void onRosterInfoUpdate(
    BMXRosterItemPtr item
)
```

Update user information

**Parameters**:

* **item** Updated friend information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onRosterListUpdate

```cpp
inline virtual void onRosterListUpdate()
```

Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function registerRosterService

```cpp
inline void registerRosterService(
    BMXRosterService * service
)
```

Register BMXRosterService to which BMXRosterServiceListener is bound (automatic registration in SDK)

**Parameters**:

* **service** [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXRosterService * mService;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
