---
title: im::floo::floolib::BMXRosterServiceListener
summary: Friend change listener
---

# im::floo::floolib::BMXRosterServiceListener

Friend change listener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-delete)()                                                                                                                                                                                                                     |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigreleaseownership)()                                                                                                                                                                                         |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigtakeownership)()                                                                                                                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendadded"><strong>onFriendAdded</strong></a>(long sponsorId, long recipientId)<br>Add friend</p>                                                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved"><strong>onFriendRemoved</strong></a>(long sponsorId, long recipientId)<br>Delete friend</p>                                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(long sponsorId, long recipientId, String message)<br>Request of adding friend received</p>                                                                                           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(long sponsorId, long recipientId)<br>Request of adding friend approved</p>                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(long sponsorId, long recipientId, String reason)<br>Request of adding friend rejected</p>                                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(long sponsorId, long recipientId)<br>Add to blacklist</p>                                                                                                              |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(long sponsorId, long recipientId)<br>Delete blacklist</p>                                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate"><strong>onRosterInfoUpdate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>Update user information</p>                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate"><strong>onRosterListUpdate</strong></a>()<br>Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information</p> |
|                   | [**BMXRosterServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)()                                                                                                                                                                                 |
| void              | [**registerRosterService**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service)                                                                                                     |

## Protected Functions

|      | Name                                                                                                                                                                                             |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXRosterServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)(long cPtr, boolean cMemoryOwn)                                 |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-finalize)()                                                                                              |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigdirectordisconnect)()                                                                  |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-getcptr)([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onFriendAdded

```java
inline void onFriendAdded(
    long sponsorId,
    long recipientId
)
```

Add friend

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onFriendRemoved

```java
inline void onFriendRemoved(
    long sponsorId,
    long recipientId
)
```

Delete friend

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onApplied

```java
inline void onApplied(
    long sponsorId,
    long recipientId,
    String message
)
```

Request of adding friend received

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient
* **message** Friend request message

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onApplicationAccepted

```java
inline void onApplicationAccepted(
    long sponsorId,
    long recipientId
)
```

Request of adding friend approved

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onApplicationDeclined

```java
inline void onApplicationDeclined(
    long sponsorId,
    long recipientId,
    String reason
)
```

Request of adding friend rejected

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient
* **reason** Reason for application rejection

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onBlockListAdded

```java
inline void onBlockListAdded(
    long sponsorId,
    long recipientId
)
```

Add to blacklist

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onBlockListRemoved

```java
inline void onBlockListRemoved(
    long sponsorId,
    long recipientId
)
```

Delete blacklist

**Parameters**:

* **sponsorId** Operation initiator
* **recipientId** Operation recipient

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onRosterInfoUpdate

```java
inline void onRosterInfoUpdate(
    BMXRosterItem item
)
```

Update user information

**Parameters**:

* **item** Updated friend information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function onRosterListUpdate

```java
inline void onRosterListUpdate()
```

Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function registerRosterService

```java
inline void registerRosterService(
    BMXRosterService service
)
```

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXRosterServiceListener obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
