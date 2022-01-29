---
title: floo::BMXResultPage
summary: 分页结果 

---

# floo::BMXResultPage



分页结果  [More...](#detailed-description)


`#include <bmx_result_page.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**()<br>构造函数  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const std::vector< T > & result, int64_t offset)<br>构造函数  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const std::vector< T > & result, std::string cursor)<br>构造函数  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & from)<br>构造函数  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**([BMXResultPage](classfloo_1_1_b_m_x_result_page.md) && from)<br>构造函数  |
| [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & | **[operator=](classfloo_1_1_b_m_x_result_page.md#function-operator=)**(const [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & from)<br>赋值函数  |
| virtual | **[~BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-~bmxresultpage)**()<br>析构函数  |
| size_t | **[count](classfloo_1_1_b_m_x_result_page.md#function-count)**() const<br>vector对象数组大小  |
| int64_t | **[offset](classfloo_1_1_b_m_x_result_page.md#function-offset)**() const<br>偏移量  |
| const std::string & | **[cursor](classfloo_1_1_b_m_x_result_page.md#function-cursor)**() const<br>cursor偏移量  |
| const std::vector< T > & | **[result](classfloo_1_1_b_m_x_result_page.md#function-result)**() const<br>vector对象数组  |

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


### function BMXResultPage

```cpp
inline BMXResultPage(
    const BMXResultPage & from
)
```

构造函数 

**Parameters**: 

  * **from** BMXResultPage对象 


### function BMXResultPage

```cpp
inline BMXResultPage(
    BMXResultPage && from
)
```

构造函数 

**Parameters**: 

  * **from** BMXResultPage对象 


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

### function ~BMXResultPage

```cpp
inline virtual ~BMXResultPage()
```

析构函数 

### function count

```cpp
inline size_t count() const
```

vector对象数组大小 

**Return**: size_t 

### function offset

```cpp
inline int64_t offset() const
```

偏移量 

**Return**: int64_t 

### function cursor

```cpp
inline const std::string & cursor() const
```

cursor偏移量 

**Return**: std::string 

### function result

```cpp
inline const std::vector< T > & result() const
```

vector对象数组 

**Return**: std::vector<T> 

-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800