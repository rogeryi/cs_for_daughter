# 第 6 周：字典——有名字的数据

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块二：核心语法 |
| **课时** | 1.5 小时 |
| **关键词** | 字典、键值对、字典方法、嵌套 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解字典的概念和用途
2. 创建和访问字典
3. 使用字典的增删改方法
4. 遍历字典的键、值和键值对
5. 理解列表和字典的嵌套使用

---

## 复习回顾（5 分钟）

上节课我们学习了：
- 列表的创建、索引、切片
- 列表的增删改操作
- for 循环遍历列表

**快速提问：**
- 如何在列表末尾添加一个元素？
- for 循环和 while 循环的区别是什么？

---

## 教学内容

### 第一部分：字典的概念与创建（25 分钟）

#### 1.1 为什么需要字典？

假设我们要存储一个学生的信息：

```python
# 用列表存储？
student = ["小明", 16, "高一", 95]
# 问题：怎么知道第几个是什么？必须记住顺序

# 用字典存储！
student = {
    "name": "小明",
    "age": 16,
    "grade": "高一",
    "score": 95
}
# 清晰！每个数据都有名字
```

#### 1.2 什么是字典？

字典是一种存储**键值对（key-value）**的数据结构。

```
字典就像一本真正的词典：
┌─────────────────────────────┐
│  词（键）    →    解释（值）  │
├─────────────────────────────┤
│  "name"     →    "小明"      │
│  "age"      →    16         │
│  "grade"    →    "高一"      │
│  "score"    →    95         │
└─────────────────────────────┘
```

#### 1.3 创建字典

```python
# 方式1：直接创建
student = {
    "name": "小明",
    "age": 16,
    "grade": "高一"
}

# 方式2：空字典
empty_dict = {}

# 方式3：使用 dict() 函数
person = dict(name="小红", age=17)
```

**键的要求：**
- 键必须是**不可变类型**（字符串、数字、元组）
- 键必须**唯一**，重复的键会被覆盖

```python
# ✅ 正确
data = {"name": "小明", 1: "one", (1, 2): "tuple key"}

# ❌ 错误：列表不能作为键
# data = {[1, 2]: "list key"}  # TypeError
```

#### 1.4 访问字典元素

```python
student = {"name": "小明", "age": 16, "score": 95}

# 方式1：使用方括号
print(student["name"])   # 小明
print(student["age"])    # 16

# 如果键不存在会报错
# print(student["height"])  # KeyError

# 方式2：使用 get() 方法（推荐）
print(student.get("name"))    # 小明
print(student.get("height"))  # None（键不存在返回 None）
print(student.get("height", 170))  # 170（可以设置默认值）
```

#### 1.5 检查键是否存在

```python
student = {"name": "小明", "age": 16}

# 使用 in 检查
if "name" in student:
    print("有 name 这个键")

if "height" not in student:
    print("没有 height 这个键")
```

---

### 第二部分：字典的操作方法（25 分钟）

#### 2.1 添加和修改元素

```python
student = {"name": "小明", "age": 16}

# 添加新键值对
student["score"] = 95
student["grade"] = "高一"
print(student)
# {'name': '小明', 'age': 16, 'score': 95, 'grade': '高一'}

# 修改已有的值
student["age"] = 17
print(student["age"])  # 17

# 使用 update() 一次添加多个
student.update({"height": 175, "weight": 60})
print(student)
```

#### 2.2 删除元素

```python
student = {"name": "小明", "age": 16, "score": 95, "grade": "高一"}

# pop()：删除指定键并返回其值
age = student.pop("age")
print(age)      # 16
print(student)  # {'name': '小明', 'score': 95, 'grade': '高一'}

# pop() 可以设置默认值，键不存在时返回默认值
height = student.pop("height", "不存在")
print(height)   # 不存在

# del：删除指定键值对
del student["grade"]
print(student)  # {'name': '小明', 'score': 95}

# clear()：清空字典
student.clear()
print(student)  # {}
```

#### 2.3 常用方法

```python
student = {"name": "小明", "age": 16, "score": 95}

# keys()：获取所有键
print(student.keys())    # dict_keys(['name', 'age', 'score'])
print(list(student.keys()))  # ['name', 'age', 'score']

# values()：获取所有值
print(student.values())  # dict_values(['小明', 16, 95])
print(list(student.values()))  # ['小明', 16, 95]

# items()：获取所有键值对
print(student.items())
# dict_items([('name', '小明'), ('age', 16), ('score', 95)])

# len()：获取键值对数量
print(len(student))  # 3
```

---

### 第三部分：遍历字典（20 分钟）

#### 3.1 遍历键

```python
student = {"name": "小明", "age": 16, "score": 95}

# 方式1：直接遍历（默认遍历键）
for key in student:
    print(key)

# 方式2：使用 keys()
for key in student.keys():
    print(key)

# 输出：name, age, score
```

#### 3.2 遍历值

```python
student = {"name": "小明", "age": 16, "score": 95}

for value in student.values():
    print(value)

# 输出：小明, 16, 95
```

#### 3.3 遍历键值对

```python
student = {"name": "小明", "age": 16, "score": 95}

for key, value in student.items():
    print(f"{key}: {value}")

# 输出：
# name: 小明
# age: 16
# score: 95
```

#### 3.4 实用示例

```python
# 统计单词出现次数
text = "apple banana apple orange banana apple"
words = text.split()  # 分割成列表

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'apple': 3, 'banana': 2, 'orange': 1}

# 更简洁的写法：使用 get()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```

---

### 第四部分：课堂练习（20 分钟）

#### 练习：简易通讯录

创建一个通讯录程序：
- 可以添加联系人（姓名、电话）
- 可以查看所有联系人
- 可以根据姓名查找联系人

**示例代码框架：**

```python
# 简易通讯录
print("=" * 40)
print("        简易通讯录")
print("=" * 40)

contacts = {}

while True:
    print("\n请选择操作：")
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 查找联系人")
    print("4. 退出")
    
    choice = input("请输入选项：")
    
    if choice == "1":
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        contacts[name] = phone
        print(f"✅ 已添加联系人：{name}")
    
    elif choice == "2":
        if len(contacts) == 0:
            print("\n📭 通讯录为空")
        else:
            print("\n📋 所有联系人：")
            for name, phone in contacts.items():
                print(f"  {name}: {phone}")
    
    elif choice == "3":
        name = input("请输入要查找的姓名：")
        phone = contacts.get(name)
        if phone:
            print(f"📱 {name} 的电话：{phone}")
        else:
            print(f"❌ 未找到联系人：{name}")
    
    elif choice == "4":
        print("👋 再见！")
        break
    
    else:
        print("❌ 无效选项")
```

**扩展挑战：**
- 添加删除联系人功能
- 添加修改联系人信息功能
- 每个联系人可以存储多个信息（电话、邮箱、地址）

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 字典 | 存储键值对的数据结构 |
| 键 | 必须唯一且不可变（字符串、数字） |
| 值 | 可以是任何类型 |
| 访问 | dict[key] 或 dict.get(key) |
| keys/values/items | 获取键/值/键值对 |
| 遍历 | for key, value in dict.items() |

**字典 vs 列表：**

| 特性 | 列表 | 字典 |
|------|------|------|
| 访问方式 | 索引（数字） | 键（通常是字符串） |
| 顺序 | 有序 | Python 3.7+ 保持插入顺序 |
| 用途 | 存储同类数据的集合 | 存储有关联的信息 |

---

## 参考资料

### 官方文档
- [Python 字典](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#dictionaries)
- [字典类型方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict)

### 视频教程
- [Python 字典详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 字典教程 - 菜鸟教程](https://www.runoob.com/python3/python3-dictionary.html)

### 在线练习
- [Python Tutor - 可视化字典操作](https://pythontutor.com/)
- [Codecademy Python 字典](https://www.codecademy.com/learn/learn-python-3)
- [LeetCode 哈希表题目](https://leetcode.cn/tag/hash-table/)

### 拓展阅读
- [字典推导式](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#dictionaries)
- [defaultdict 和 Counter](https://docs.python.org/zh-cn/3/library/collections.html)
