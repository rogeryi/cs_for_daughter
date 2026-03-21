# 第 2 周：数据的类型

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块一：入门基础 |
| **课时** | 1.5 小时 |
| **关键词** | 整数、浮点数、字符串、类型转换、input |

---

## 学习目标

完成本节课后，学生将能够：

1. 区分 Python 中的三种基本数据类型：整数、浮点数、字符串
2. 进行基本的数学运算
3. 使用 `input()` 函数获取用户输入
4. 理解并使用类型转换函数
5. 掌握字符串的基本操作

---

## 复习回顾（5 分钟）

上节课我们学习了：
- 什么是编程和 Python
- 如何使用 `print()` 输出信息
- 什么是变量以及如何创建变量

**快速提问：**
- 如何创建一个存储你名字的变量？
- `print("Hello")` 和 `print(Hello)` 有什么区别？

---

## 教学内容

### 第一部分：整数、浮点数、字符串（30 分钟）

#### 1.1 整数（int）

整数就是没有小数点的数字，可以是正数、负数或零。

```python
# 整数示例
age = 16
score = 100
temperature = -5
count = 0

print(type(age))  # <class 'int'>
```

#### 1.2 浮点数（float）

浮点数是带小数点的数字。

```python
# 浮点数示例
height = 1.75
price = 9.99
pi = 3.14159

print(type(height))  # <class 'float'>

# 注意：整数除法可能产生浮点数
result = 10 / 3
print(result)       # 3.3333...
print(type(result)) # <class 'float'>
```

#### 1.3 数学运算

Python 可以像计算器一样进行数学运算：

| 运算符 | 名称 | 示例 | 结果 |
|--------|------|------|------|
| `+` | 加法 | `5 + 3` | `8` |
| `-` | 减法 | `5 - 3` | `2` |
| `*` | 乘法 | `5 * 3` | `15` |
| `/` | 除法 | `5 / 3` | `1.666...` |
| `//` | 整除 | `5 // 3` | `1` |
| `%` | 取余 | `5 % 3` | `2` |
| `**` | 幂运算 | `5 ** 3` | `125` |

```python
# 运算示例
a = 10
b = 3

print("加法:", a + b)    # 13
print("减法:", a - b)    # 7
print("乘法:", a * b)    # 30
print("除法:", a / b)    # 3.333...
print("整除:", a // b)   # 3
print("取余:", a % b)    # 1
print("幂运算:", a ** b) # 1000

# 复合运算
result = (a + b) * 2 - 5
print("复合运算:", result)  # 21
```

#### 1.4 字符串（str）

字符串是由字符组成的文本，用引号包围。

```python
# 字符串可以用单引号或双引号
name = "小明"
greeting = '你好'

# 多行字符串用三引号
poem = """
静夜思
床前明月光，
疑是地上霜。
"""

print(type(name))  # <class 'str'>
```

**字符串 vs 数字：**

```python
# 这是数字，可以做数学运算
num1 = 100
num2 = 200
print(num1 + num2)  # 300

# 这是字符串，+ 会拼接
str1 = "100"
str2 = "200"
print(str1 + str2)  # "100200"
```

---

### 第二部分：类型转换与 input() 函数（30 分钟）

#### 2.1 input() 函数

`input()` 用于获取用户从键盘输入的内容。

```python
# 基本用法
name = input("请输入你的名字：")
print("你好,", name)

# input() 总是返回字符串！
age = input("请输入你的年龄：")
print(type(age))  # <class 'str'> 即使输入的是数字
```

**重要提醒：** `input()` 返回的永远是字符串，即使用户输入的是数字！

#### 2.2 类型转换

当需要把一种类型转换成另一种类型时，使用类型转换函数：

| 函数 | 作用 | 示例 |
|------|------|------|
| `int()` | 转换为整数 | `int("16")` → `16` |
| `float()` | 转换为浮点数 | `float("3.14")` → `3.14` |
| `str()` | 转换为字符串 | `str(100)` → `"100"` |

```python
# 字符串转数字
age_str = "16"
age_int = int(age_str)
print(age_int + 1)  # 17

# 数字转字符串
score = 95
message = "你的分数是：" + str(score) + "分"
print(message)

# 浮点数和整数互转
pi = 3.14159
print(int(pi))    # 3（直接截断，不是四舍五入）
print(float(10))  # 10.0
```

#### 2.3 从用户获取数字

```python
# 错误示范
age = input("请输入年龄：")
# next_year = age + 1  # 错误！字符串不能和数字相加

# 正确做法
age = input("请输入年龄：")
age = int(age)  # 转换为整数
next_year = age + 1
print("明年你", next_year, "岁")

# 或者一行搞定
age = int(input("请输入年龄："))
```

#### 2.4 处理用户输入的常见问题

```python
# 获取身高（浮点数）
height = float(input("请输入身高（米）："))
print("你的身高是", height, "米")

# 注意：如果用户输入的不是有效数字，程序会报错
# 例如用户输入 "abc"，int("abc") 会导致 ValueError
# 后面我们会学习如何处理这种情况
```

---

### 第三部分：字符串的基本操作（20 分钟）

#### 3.1 字符串拼接

```python
first_name = "小"
last_name = "明"

# 方法1：用 + 号拼接
full_name = first_name + last_name
print(full_name)  # 小明

# 方法2：用逗号（print 专用，会自动加空格）
print(first_name, last_name)  # 小 明

# 方法3：f-string（推荐！Python 3.6+）
age = 16
message = f"我叫{full_name}，今年{age}岁"
print(message)  # 我叫小明，今年16岁
```

#### 3.2 f-string 格式化（重点）

f-string 是最现代、最方便的字符串格式化方式：

```python
name = "小明"
age = 16
height = 1.75

# 基本用法：f"...{变量}..."
print(f"姓名：{name}")
print(f"年龄：{age}")

# 可以在 {} 中进行计算
print(f"明年年龄：{age + 1}")

# 格式化数字
price = 19.9
print(f"价格：{price:.2f} 元")  # 保留2位小数：19.90

pi = 3.14159265
print(f"圆周率：{pi:.4f}")  # 保留4位小数：3.1416
```

#### 3.3 字符串的其他操作

```python
text = "Hello, Python!"

# 获取长度
print(len(text))  # 14

# 大小写转换
print(text.upper())  # HELLO, PYTHON!
print(text.lower())  # hello, python!

# 字符串重复
print("=" * 20)  # ====================
print("哈" * 3)   # 哈哈哈

# 检查是否包含
print("Python" in text)  # True
print("Java" in text)    # False
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：简单计算器

创建一个程序，让用户输入两个数字，然后显示它们的加、减、乘、除结果。

**示例代码框架：**

```python
# 简单计算器
# 作者：[你的名字]

print("=" * 30)
print("      简单计算器")
print("=" * 30)

# 获取用户输入
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

# 计算并显示结果
print(f"\n计算结果：")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2:.2f}")

print("=" * 30)
```

**扩展挑战：**
- 添加幂运算和取余运算
- 美化输出格式
- 添加整除运算

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 整数 int | 没有小数点的数字 |
| 浮点数 float | 带小数点的数字 |
| 字符串 str | 用引号包围的文本 |
| input() | 获取用户输入（返回字符串） |
| 类型转换 | int()、float()、str() |
| f-string | f"...{变量}..." 格式化字符串 |

**重要提醒：**
- `input()` 返回的永远是字符串
- 不同类型的数据不能直接运算，需要先转换

---

## 参考资料

### 官方文档
- [Python 数据类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)
- [Python 内置函数](https://docs.python.org/zh-cn/3/library/functions.html)
- [格式化字符串字面值 f-string](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#formatted-string-literals)

### 视频教程
- [Python 数据类型详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python input函数 - 菜鸟教程](https://www.runoob.com/python3/python3-func-input.html)

### 在线练习
- [Python Tutor - 可视化代码执行](https://pythontutor.com/)
- [Codecademy Python 数据类型](https://www.codecademy.com/learn/learn-python-3)

### 拓展阅读
- [为什么浮点数不精确？](https://docs.python.org/zh-cn/3/tutorial/floatingpoint.html)
- [Python 字符串方法大全](https://www.runoob.com/python3/python3-string.html)
