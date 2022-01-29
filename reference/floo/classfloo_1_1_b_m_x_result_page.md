---
title: floo::BMXResultPage
summary: Paged result 

---

# floo::BMXResultPage



Paged result  [More...](#detailed-description)


`#include <bmx_result_page.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**()<br>Constructor  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const std::vector< T > & result, int64_t offset)<br>Constructor  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const std::vector< T > & result, std::string cursor)<br>Constructor  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**(const [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & from)<br>Constructor  |
| | **[BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-bmxresultpage)**([BMXResultPage](classfloo_1_1_b_m_x_result_page.md) && from)<br>Constructor  |
| [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & | **[operator=](classfloo_1_1_b_m_x_result_page.md#function-operator=)**(const [BMXResultPage](classfloo_1_1_b_m_x_result_page.md) & from)<br>Assignment function  |
| virtual | **[~BMXResultPage](classfloo_1_1_b_m_x_result_page.md#function-~bmxresultpage)**()<br>Destructor  |
| size_t | **[count](classfloo_1_1_b_m_x_result_page.md#function-count)**() const<br>Size of vector object-array  |
| int64_t | **[offset](classfloo_1_1_b_m_x_result_page.md#function-offset)**() const<br>Offset  |
| const std::string & | **[cursor](classfloo_1_1_b_m_x_result_page.md#function-cursor)**() const<br>cursor offset  |
| const std::vector< T > & | **[result](classfloo_1_1_b_m_x_result_page.md#function-result)**() const<br>vector object-array  |

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


### function BMXResultPage

```cpp
inline BMXResultPage(
    const BMXResultPage & from
)
```

Constructor 

**Parameters**: 

  * **from** BMXResultPage object 


### function BMXResultPage

```cpp
inline BMXResultPage(
    BMXResultPage && from
)
```

Constructor 

**Parameters**: 

  * **from** BMXResultPage object 


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

### function ~BMXResultPage

```cpp
inline virtual ~BMXResultPage()
```

Destructor 

### function count

```cpp
inline size_t count() const
```

Size of vector object-array 

**Return**: size_t 

### function offset

```cpp
inline int64_t offset() const
```

Offset 

**Return**: int64_t 

### function cursor

```cpp
inline const std::string & cursor() const
```

cursor offset 

**Return**: std::string 

### function result

```cpp
inline const std::vector< T > & result() const
```

vector object-array 

**Return**: std::vector<T> 

-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800