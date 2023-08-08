---
title: im::floo::floolib::BMXMessageAttachment
summary: Message attachment
---

# im::floo::floolib::BMXMessageAttachment

Message attachment

Inherits from BMXBaseObject

Inherited by [im.floo.floolib.BMXFileAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md), [im.floo.floolib.BMXLocationAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md)

## Public Functions

|                                                                                               | Name                                                                                                                                       |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                                             | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-delete)()                                      |
| BMXMessageAttachment.Type                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type"><strong>type</strong></a>()<br>Attachment type</p>   |
| [BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone"><strong>clone</strong></a>()<br>Copy attachment</p> |

## Protected Functions

|      | Name                                                                                                                                                                                                     |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXMessageAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-finalize)()                                                                                                |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-getcptr)([BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-delete), [im::floo::floolib::BMXImageAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_image\_attachment.md#function-delete), [im::floo::floolib::BMXLocationAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-delete), [im::floo::floolib::BMXVideoAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-delete), [im::floo::floolib::BMXVoiceAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_voice\_attachment.md#function-delete)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```

### function type

```java
inline BMXMessageAttachment.Type type()
```

Attachment type

**Return**: \[Type]

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-type), [im::floo::floolib::BMXImageAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_image\_attachment.md#function-type), [im::floo::floolib::BMXLocationAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-type), [im::floo::floolib::BMXVideoAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-type), [im::floo::floolib::BMXVoiceAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_voice\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```

### function clone

```java
inline BMXMessageAttachment clone()
```

Copy attachment

**Return**: BMXMessageAttachmentPtr

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-clone), [im::floo::floolib::BMXImageAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_image\_attachment.md#function-clone), [im::floo::floolib::BMXLocationAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-clone), [im::floo::floolib::BMXVideoAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-clone), [im::floo::floolib::BMXVoiceAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_voice\_attachment.md#function-clone)

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```

### function BMXMessageAttachment

```java
inline BMXMessageAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```

### function finalize

```java
inline void finalize()
```

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-finalize), [im::floo::floolib::BMXImageAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_image\_attachment.md#function-finalize), [im::floo::floolib::BMXLocationAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-finalize), [im::floo::floolib::BMXVideoAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-finalize), [im::floo::floolib::BMXVoiceAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_voice\_attachment.md#function-finalize)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXMessageAttachment obj
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageAttachment'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
