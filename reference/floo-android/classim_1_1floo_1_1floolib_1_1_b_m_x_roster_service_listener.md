---
title: im::floo::floolib::BMXRosterServiceListener
summary: Friend change listener 

---

# im::floo::floolib::BMXRosterServiceListener



Friend change listener 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigtakeownership)**() |
| void | **[onFriendAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendadded)**(long sponsorId, long recipientId)<br>Add friend  |
| void | **[onFriendRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved)**(long sponsorId, long recipientId)<br>Delete friend  |
| void | **[onApplied](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplied)**(long sponsorId, long recipientId, String message)<br>Request of adding friend received  |
| void | **[onApplicationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted)**(long sponsorId, long recipientId)<br>Request of adding friend approved  |
| void | **[onApplicationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined)**(long sponsorId, long recipientId, String reason)<br>Request of adding friend rejected  |
| void | **[onBlockListAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded)**(long sponsorId, long recipientId)<br>Add to blacklist  |
| void | **[onBlockListRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved)**(long sponsorId, long recipientId)<br>Delete blacklist  |
| void | **[onRosterInfoUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Update user information  |
| void | **[onRosterListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate)**()<br>Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information  |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**() |
| void | **[registerRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)**([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-getcptr)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
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


### function onRosterInfoUpdate

```java
inline void onRosterInfoUpdate(
    BMXRosterItem item
)
```

Update user information 

**Parameters**: 

  * **item** Updated friend information 


### function onRosterListUpdate

```java
inline void onRosterListUpdate()
```

Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information 

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener()
```


### function registerRosterService

```java
inline void registerRosterService(
    BMXRosterService service
)
```


## Protected Functions Documentation

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800