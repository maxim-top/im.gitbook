---
title: floo::BMXResultPage
summary: 分页结果
---

# floo::BMXResultPage

分页结果 [More...](classfloo_1_1_b_m_x_result_page.md#detailed-description)

`#include <bmx_result_page.h>`

Inherits from BMXBaseObject

## Public Functions

|                                                       | Name                                                                                                                                                                                                    |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>()<br>构造函数</p>                                                                                 |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const std::vector&#x3C; T > &#x26; result, int64_t offset)<br>构造函数</p>                        |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const std::vector&#x3C; T > &#x26; result, std::string cursor)<br>构造函数</p>                    |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(const <a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26; from)<br>构造函数</p> |
|                                                       | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage"><strong>BMXResultPage</strong></a>(<a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26;&#x26; from)<br>构造函数</p> |
| [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-operator="><strong>operator=</strong></a>(const <a href="classfloo_1_1_b_m_x_result_page.md">BMXResultPage</a> &#x26; from)<br>赋值函数</p>         |
| virtual                                               | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-~bmxresultpage"><strong>~BMXResultPage</strong></a>()<br>析构函数</p>                                                                               |
| size\_t                                               | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-count"><strong>count</strong></a>() const<br>vector对象数组大小</p>                                                                                   |
| int64\_t                                              | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-offset"><strong>offset</strong></a>() const<br>偏移量</p>                                                                                          |
| const std::string &                                   | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-cursor"><strong>cursor</strong></a>() const<br>cursor偏移量</p>                                                                                    |
| const std::vector< T > &                              | <p><a href="classfloo_1_1_b_m_x_result_page.md#function-result"><strong>result</strong></a>() const<br>vector对象数组</p>                                                                                   |

## Detailed Description

```cpp
template <typename T >
class floo::BMXResultPage;
```

分页结果

## Public Functions Documentation

### function BMXResultPage

```cpp
inline BMXResultPage()
```

构造函数

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

构造函数

**Parameters**:

* **result** 列表数据
* **offset** 偏移量

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

构造函数

**Parameters**:

* **result** 列表结果
* **cursor** cursor偏移量

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

构造函数

**Parameters**:

* **from** BMXResultPage对象

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

构造函数

**Parameters**:

* **from** BMXResultPage对象

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

赋值函数

**Parameters**:

* **from** BMXResultPage对象

**Return**: [BMXResultPage](classfloo_1_1_b_m_x_result_page.md)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function \~BMXResultPage

```cpp
inline virtual ~BMXResultPage()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function count

```cpp
inline size_t count() const
```

vector对象数组大小

**Return**: size\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function offset

```cpp
inline int64_t offset() const
```

偏移量

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function cursor

```cpp
inline const std::string & cursor() const
```

cursor偏移量

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>

```

### function result

```cpp
inline const std::vector< T > & result() const
```

vector对象数组

**Return**: std::vector

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXResultPage'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
