# 第 5 周：列表——批量管理数据

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块二：核心语法 |
| **课时** | 1.5 小时 |
| **关键词** | 列表、索引、切片、for 循环、列表方法 |

---

## 学习目标

完成本节课后，学生将能够：

1. 创建和访问列表
2. 使用索引和切片操作列表元素
3. 使用列表的增删改方法
4. 使用 for 循环遍历列表
5. 理解列表在实际编程中的应用

---

## 复习回顾（5 分钟）

上节课我们学习了：
- while 循环重复执行代码
- break 退出循环，continue 跳过本次迭代

**快速提问：**
- 什么情况下会造成无限循环？
- break 和 continue 的区别是什么？

---

## 教学内容

### 第一部分：列表的创建与访问（25 分钟）

#### 1.1 什么是列表？

列表是一种可以存储**多个数据**的容器，就像一排带编号的盒子。

```python
# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
scores = [95, 87, 92, 78, 88]
mixed = [1, "hello", 3.14, True]  # 可以混合不同类型

# 空列表
empty_list = []
```

```
列表 fruits:
┌─────┬─────┬─────┬─────┐
│ 苹果 │ 香蕉 │ 橙子 │ 葡萄 │
└─────┴─────┴─────┴─────┘
  [0]   [1]   [2]   [3]   ← 索引（从0开始）
```

#### 1.2 访问列表元素（索引）

列表中的每个元素都有一个**索引**（编号），从 0 开始。

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 正向索引（从0开始）
print(fruits[0])  # 苹果
print(fruits[1])  # 香蕉
print(fruits[2])  # 橙子
print(fruits[3])  # 葡萄

# 负向索引（从末尾开始，-1是最后一个）
print(fruits[-1])  # 葡萄
print(fruits[-2])  # 橙子
```

```
正向索引:    0      1      2      3
          ┌─────┬─────┬─────┬─────┐
          │ 苹果 │ 香蕉 │ 橙子 │ 葡萄 │
          └─────┴─────┴─────┴─────┘
负向索引:   -4     -3     -2     -1
```

#### 1.3 列表切片

切片可以获取列表的一部分。

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 语法：列表[起始:结束]  （包含起始，不包含结束）
print(fruits[1:3])   # ['香蕉', '橙子']
print(fruits[0:2])   # ['苹果', '香蕉']
print(fruits[:3])    # ['苹果', '香蕉', '橙子']  省略起始=从头开始
print(fruits[2:])    # ['橙子', '葡萄', '西瓜']  省略结束=到末尾
print(fruits[:])     # 整个列表的副本

# 带步长的切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8]  每隔2个取一个
print(numbers[1::2])  # [1, 3, 5, 7, 9]  从索引1开始，每隔2个
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  反转
```

#### 1.4 列表长度和检查元素

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 获取列表长度
print(len(fruits))  # 4

# 检查元素是否在列表中
print("苹果" in fruits)     # True
print("榴莲" in fruits)     # False
print("榴莲" not in fruits) # True
```

---

### 第二部分：列表的增删改操作（30 分钟）

#### 2.1 修改元素

```python
fruits = ["苹果", "香蕉", "橙子"]

# 直接通过索引修改
fruits[1] = "草莓"
print(fruits)  # ['苹果', '草莓', '橙子']
```

#### 2.2 添加元素

```python
fruits = ["苹果", "香蕉"]

# append：在末尾添加一个元素
fruits.append("橙子")
print(fruits)  # ['苹果', '香蕉', '橙子']

# insert：在指定位置插入元素
fruits.insert(1, "草莓")  # 在索引1的位置插入
print(fruits)  # ['苹果', '草莓', '香蕉', '橙子']

# extend：添加多个元素
fruits.extend(["葡萄", "西瓜"])
print(fruits)  # ['苹果', '草莓', '香蕉', '橙子', '葡萄', '西瓜']

# + 号拼接（创建新列表）
new_fruits = fruits + ["芒果", "榴莲"]
print(new_fruits)
```

#### 2.3 删除元素

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "香蕉"]

# remove：删除第一个匹配的元素
fruits.remove("香蕉")
print(fruits)  # ['苹果', '橙子', '葡萄', '香蕉']

# pop：删除并返回指定索引的元素（默认最后一个）
last = fruits.pop()
print(last)    # 香蕉
print(fruits)  # ['苹果', '橙子', '葡萄']

first = fruits.pop(0)
print(first)   # 苹果
print(fruits)  # ['橙子', '葡萄']

# del：删除指定索引的元素
del fruits[0]
print(fruits)  # ['葡萄']

# clear：清空列表
fruits.clear()
print(fruits)  # []
```

#### 2.4 其他常用方法

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 排序（修改原列表）
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # 降序
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# 反转
numbers.reverse()
print(numbers)

# 统计元素出现次数
print(numbers.count(1))  # 2

# 查找元素索引
print(numbers.index(5))  # 返回第一个5的索引
```

---

### 第三部分：for 循环遍历列表（25 分钟）

#### 3.1 for 循环基础

for 循环用于**遍历**可迭代对象（如列表）中的每一个元素。

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 遍历列表
for fruit in fruits:
    print(fruit)
```

输出：
```
苹果
香蕉
橙子
葡萄
```

**执行流程：**
1. 取出列表第一个元素"苹果"，赋值给 fruit
2. 执行循环体（print）
3. 取出下一个元素"香蕉"，赋值给 fruit
4. 执行循环体
5. ...直到所有元素都处理完毕

#### 3.2 for vs while

```python
fruits = ["苹果", "香蕉", "橙子"]

# for 循环（推荐遍历列表时使用）
for fruit in fruits:
    print(fruit)

# 等价的 while 循环
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

**什么时候用哪个？**
- `for`：遍历已知的集合（列表、字符串等）
- `while`：根据条件重复（次数不确定时）

#### 3.3 range() 函数

`range()` 生成一个数字序列，常与 for 循环配合使用。

```python
# range(stop)：从0到stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)：从start到stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)：带步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 倒序
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

#### 3.4 遍历时获取索引

```python
fruits = ["苹果", "香蕉", "橙子"]

# 方法1：使用 range 和 len
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 方法2：使用 enumerate（推荐）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 输出：
# 0: 苹果
# 1: 香蕉
# 2: 橙子
```

#### 3.5 实用示例

```python
# 计算列表元素的总和
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"总和：{total}")  # 150

# 找出最大值
numbers = [23, 45, 12, 67, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"最大值：{max_num}")  # 67
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：待办事项列表

创建一个简单的待办事项管理程序：
- 可以查看所有待办事项
- 可以添加新的待办事项
- 用循环让用户可以重复操作

**示例代码框架：**

```python
# 待办事项列表
print("=" * 40)
print("        待办事项管理")
print("=" * 40)

todos = []

while True:
    print("\n请选择操作：")
    print("1. 查看待办事项")
    print("2. 添加待办事项")
    print("3. 退出")
    
    choice = input("请输入选项：")
    
    if choice == "1":
        if len(todos) == 0:
            print("\n📭 暂无待办事项")
        else:
            print("\n📋 待办事项列表：")
            for i, todo in enumerate(todos, 1):
                print(f"  {i}. {todo}")
    
    elif choice == "2":
        new_todo = input("请输入新的待办事项：")
        todos.append(new_todo)
        print(f"✅ 已添加：{new_todo}")
    
    elif choice == "3":
        print("👋 再见！")
        break
    
    else:
        print("❌ 无效选项，请重新选择")
```

**扩展挑战：**
- 添加删除待办事项的功能
- 添加标记完成的功能
- 显示待办事项的序号

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 列表 | 存储多个数据的有序容器 |
| 索引 | 从0开始，-1是最后一个 |
| 切片 | list[start:end] 获取子列表 |
| append | 在末尾添加元素 |
| remove/pop | 删除元素 |
| for 循环 | 遍历列表中的每个元素 |
| range() | 生成数字序列 |

**重要提醒：**
- 索引从 0 开始，不是 1
- 切片不包含结束索引的元素
- for 循环适合遍历，while 循环适合条件控制

---

## 参考资料

### 官方文档
- [Python 列表](https://docs.python.org/zh-cn/3/tutorial/introduction.html#lists)
- [Python 列表方法](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#more-on-lists)
- [for 语句](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#for-statements)
- [range() 函数](https://docs.python.org/zh-cn/3/library/stdtypes.html#range)

### 视频教程
- [Python 列表详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 列表教程 - 菜鸟教程](https://www.runoob.com/python3/python3-list.html)

### 在线练习
- [Python Tutor - 可视化列表操作](https://pythontutor.com/)
- [Codecademy Python 列表](https://www.codecademy.com/learn/learn-python-3)
- [LeetCode 数组相关题目](https://leetcode.cn/tag/array/)

### 拓展阅读
- [Python 列表推导式](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#list-comprehensions)
- [列表和元组的区别](https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/)
