---
title: floo::BMXRosterServiceListener
summary: Friend change listener 

---

# floo::BMXRosterServiceListener



Friend change listener 


`#include <bmx_roster_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**()<br>Constructor  |
| virtual | **[~BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md#function-~bmxrosterservicelistener)**()<br>Destructor  |
| virtual void | **[onFriendAdded](classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendadded)**(int64_t sponsorId, int64_t recipientId)<br>Add friend  |
| virtual void | **[onFriendRemoved](classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved)**(int64_t sponsorId, int64_t recipientId)<br>Delete friend  |
| virtual void | **[onApplied](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplied)**(int64_t sponsorId, int64_t recipientId, const std::string & message)<br>Request of adding friend received  |
| virtual void | **[onApplicationAccepted](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted)**(int64_t sponsorId, int64_t recipientId)<br>Request of adding friend approved  |
| virtual void | **[onApplicationDeclined](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined)**(int64_t sponsorId, int64_t recipientId, const std::string & reason)<br>Request of adding friend rejected  |
| virtual void | **[onBlockListAdded](classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded)**(int64_t sponsorId, int64_t recipientId)<br>Add to blacklist  |
| virtual void | **[onBlockListRemoved](classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved)**(int64_t sponsorId, int64_t recipientId)<br>Delete blacklist  |
| virtual void | **[onRosterInfoUpdate](classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate)**(BMXRosterItemPtr item)<br>Update user information  |
| virtual void | **[onRosterListUpdate](classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate)**()<br>Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information  |
| void | **[registerRosterService](classfloo_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)**([BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) * service)<br>**to-be-translate**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) * | **[mService](classfloo_1_1_b_m_x_roster_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXRosterServiceListener

```cpp
inline BMXRosterServiceListener()
```

Constructor 

### function ~BMXRosterServiceListener

```cpp
inline virtual ~BMXRosterServiceListener()
```

Destructor 

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


### function onRosterInfoUpdate

```cpp
inline virtual void onRosterInfoUpdate(
    BMXRosterItemPtr item
)
```

Update user information 

**Parameters**: 

  * **item** Updated friend information 


### function onRosterListUpdate

```cpp
inline virtual void onRosterListUpdate()
```

Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information 

### function registerRosterService

```cpp
inline void registerRosterService(
    BMXRosterService * service
)
```

**to-be-translate** 

**Parameters**: 

  * **service** [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXRosterService * mService;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800