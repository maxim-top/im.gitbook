---
title: floo::BMXResultPage
summary: Paged result
---

# floo::BMXResultPage

Paged result [More...](classfloo_1_1_b_m_x_result_page.md#detailed-description)

`#include <bmx_result_page.h>`

Inherits from BMXBaseObject

## Public Functions

|                                                       | Name                                                                                                                                                                                                           |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>()<br>Constructor</p>                                                                                 |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const std::vector&#x3C; T > &#x26; result, int64_t offset)<br>Constructor</p>                        |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const std::vector&#x3C; T > &#x26; result, std::string cursor)<br>Constructor</p>                    |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const <a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26; from)<br>Constructor</p> |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(<a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26;&#x26; from)<br>Constructor</p> |
| [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-operator="><strong>operator=</strong></a>(const <a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26; from)<br>Assignment function</p> |
| virtual                                               | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-~bmxresultpage"><strong>~BMXResultPage</strong></a>()<br>Destructor</p>                                                                                |
| size\_t                                               | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-count"><strong>count</strong></a>() const<br>Size of vector object-array</p>                                                                           |
| int64\_t                                              | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-offset"><strong>offset</strong></a>() const<br>Offset</p>                                                                                              |
| const std::string &                                   | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-cursor"><strong>cursor</strong></a>() const<br>cursor offset</p>                                                                                       |
| const std::vector< T > &                              | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-result"><strong>result</strong></a>() const<br>vector object-array</p>                                                                                 |

## Detailed Description

```cpp
template <typename T >
class floo::BMXResultPage;
```

Paged result

## Public Functions Documentation

### function BMXResultPage

```cpp
inline BMXResultPage()
```

Constructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function BMXResultPage

```cpp
inline BMXResultPage(
    const std::vector< T > & result,
    int64_t offset
)
```

Constructor

**Parameters**:

* **result** List data
* **offset** Offset

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function BMXResultPage

```cpp
inline BMXResultPage(
    const std::vector< T > & result,
    std::string cursor
)
```

Constructor

**Parameters**:

* **result** List result
* **cursor** cursor offset

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function BMXResultPage

```cpp
inline BMXResultPage(
    const BMXResultPage & from
)
```

Constructor

**Parameters**:

* **from** BMXResultPage object

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function BMXResultPage

```cpp
inline BMXResultPage(
    BMXResultPage && from
)
```

Constructor

**Parameters**:

* **from** BMXResultPage object

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function operator=

```cpp
inline BMXResultPage & operator=(
    const BMXResultPage & from
)
```

Assignment function

**Parameters**:

* **from** BMXResultPage object

**Return**: [BMXResultPage](classfloo_1_1_b_m_x_result_page.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function \~BMXResultPage

```cpp
inline virtual ~BMXResultPage()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function count

```cpp
inline size_t count() const
```

Size of vector object-array

**Return**: size\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function offset

```cpp
inline int64_t offset() const
```

Offset

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function cursor

```cpp
inline const std::string & cursor() const
```

cursor offset

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function result

```cpp
inline const std::vector< T > & result() const
```

vector object-array

**Return**: std::vector

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
