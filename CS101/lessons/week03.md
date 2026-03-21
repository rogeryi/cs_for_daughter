# 第 3 周：做出选择

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块一：入门基础 |
| **课时** | 1.5 小时 |
| **关键词** | 布尔值、比较运算、逻辑运算、if-elif-else |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解布尔值（True/False）的概念
2. 使用比较运算符比较数据
3. 使用逻辑运算符组合条件
4. 编写 if-elif-else 条件语句
5. 根据不同条件执行不同的代码

---

## 复习回顾（5 分钟）

上节课我们学习了：
- 三种数据类型：整数、浮点数、字符串
- input() 函数获取用户输入
- 类型转换：int()、float()、str()

**快速提问：**
- 如何把用户输入的内容转换成整数？
- f-string 怎么用？

---

## 教学内容

### 第一部分：布尔值与比较运算（20 分钟）

#### 1.1 什么是布尔值？

布尔值只有两个：`True`（真）和 `False`（假）。

```python
is_student = True
is_adult = False

print(type(is_student))  # <class 'bool'>
```

布尔值是**条件判断**的基础——程序需要根据某个条件是"真"还是"假"来决定下一步做什么。

#### 1.2 比较运算符

比较运算符用于比较两个值，结果是布尔值。

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `==` | 等于 | `5 == 5` | `True` |
| `!=` | 不等于 | `5 != 3` | `True` |
| `>` | 大于 | `5 > 3` | `True` |
| `<` | 小于 | `5 < 3` | `False` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `5 <= 3` | `False` |

```python
age = 16

print(age > 18)   # False
print(age < 18)   # True
print(age == 16)  # True
print(age != 16)  # False
print(age >= 16)  # True

# 字符串也可以比较
name = "小明"
print(name == "小明")  # True
print(name == "小红")  # False
```

**注意：** `=` 是赋值，`==` 是比较！

```python
x = 5      # 赋值：把 5 放进 x
x == 5     # 比较：x 是否等于 5？返回 True
```

#### 1.3 比较的实际应用

```python
score = 85

# 检查是否及格
is_pass = score >= 60
print(f"及格了吗？{is_pass}")  # True

# 检查是否满分
is_perfect = score == 100
print(f"满分吗？{is_perfect}")  # False
```

---

### 第二部分：if-elif-else 条件判断（40 分钟）

#### 2.1 if 语句基础

`if` 语句让程序根据条件决定是否执行某段代码。

```python
age = 16

if age >= 18:
    print("你是成年人")
    print("可以进入")
```

**语法要点：**
- `if` 后面是条件，条件后面有冒号 `:`
- 条件成立时执行的代码需要**缩进**（4个空格）
- 缩进相同的代码属于同一个代码块

```
if 条件:
    ← 这里要缩进（4个空格）
    条件为 True 时执行的代码
    可以有多行
```

#### 2.2 if-else 语句

当条件不成立时，执行另一段代码。

```python
age = 16

if age >= 18:
    print("你是成年人")
else:
    print("你还未成年")
```

```
┌─────────────────────────────────────┐
│            age >= 18?               │
│         ↙          ↘                │
│       True        False             │
│         ↓            ↓              │
│   "你是成年人"   "你还未成年"         │
└─────────────────────────────────────┘
```

#### 2.3 if-elif-else 语句

当有多个条件需要判断时，使用 `elif`（else if 的缩写）。

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

**执行流程：**
1. 先判断 `score >= 90`，如果 True，打印"优秀"，结束
2. 如果 False，判断 `score >= 80`，如果 True，打印"良好"，结束
3. 如果 False，判断 `score >= 60`，如果 True，打印"及格"，结束
4. 如果都是 False，执行 `else`，打印"不及格"

**注意：** 一旦某个条件成立并执行了对应的代码，后面的条件就不会再判断了！

```python
score = 95

# 这样写会打印两次吗？
if score >= 60:
    print("及格")
if score >= 90:
    print("优秀")
# 会打印两次！因为这是两个独立的 if

# 正确做法：用 elif
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
# 只打印一次：优秀
```

#### 2.4 嵌套的条件语句

条件语句可以嵌套使用。

```python
age = 20
has_id = True

if age >= 18:
    print("年龄符合要求")
    if has_id:
        print("可以进入")
    else:
        print("请出示身份证")
else:
    print("未成年人禁止入内")
```

#### 2.5 完整示例：成绩评级系统

```python
# 成绩评级系统
print("=" * 30)
print("      成绩评级系统")
print("=" * 30)

score = int(input("请输入分数（0-100）："))

# 先检查分数是否有效
if score < 0 or score > 100:
    print("❌ 分数无效！请输入 0-100 之间的数字")
else:
    # 评级
    if score >= 90:
        grade = "A（优秀）"
    elif score >= 80:
        grade = "B（良好）"
    elif score >= 70:
        grade = "C（中等）"
    elif score >= 60:
        grade = "D（及格）"
    else:
        grade = "F（不及格）"
    
    print(f"你的分数：{score}")
    print(f"等级评定：{grade}")
```

---

### 第三部分：逻辑运算符（20 分钟）

#### 3.1 三个逻辑运算符

| 运算符 | 含义 | 说明 |
|--------|------|------|
| `and` | 与 | 两边都为 True 结果才是 True |
| `or` | 或 | 只要一边为 True 结果就是 True |
| `not` | 非 | 取反，True 变 False，False 变 True |

```python
# and：两边都要 True
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# or：只要一个 True
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# not：取反
print(not True)   # False
print(not False)  # True
```

#### 3.2 实际应用示例

```python
age = 20
has_ticket = True
is_vip = False

# and 示例：两个条件都要满足
if age >= 18 and has_ticket:
    print("可以入场")
# 20 >= 18 是 True，has_ticket 是 True
# True and True = True，所以可以入场

# or 示例：满足一个就行
if has_ticket or is_vip:
    print("可以进入")
# has_ticket 是 True，is_vip 是 False
# True or False = True，所以可以进入

# not 示例：取反
if not is_vip:
    print("普通用户")
# is_vip 是 False，not False = True
# 所以打印"普通用户"
```

#### 3.3 复合条件

```python
# 游乐设施入场条件
age = 12
height = 140

# 条件：年龄大于10岁 且 身高超过130cm
if age > 10 and height > 130:
    print("✅ 可以乘坐")
else:
    print("❌ 不满足条件")

# 条件：成年人 或 有监护人陪同
is_adult = age >= 18
has_guardian = True

if is_adult or has_guardian:
    print("✅ 可以进入")
```

#### 3.4 优先级

逻辑运算符的优先级：`not` > `and` > `or`

```python
# 相当于：(not True) or False
result = not True or False
print(result)  # False

# 使用括号让意图更清晰
result = (age > 10) and (height > 130)
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：成绩等级判断程序

创建一个程序，根据用户输入的分数判断等级，并显示是否及格。

**要求：**
- 90-100：A（优秀）
- 80-89：B（良好）
- 70-79：C（中等）
- 60-69：D（及格）
- 0-59：F（不及格）
- 显示是否及格
- 检查分数是否在有效范围内

**示例代码框架：**

```python
# 成绩等级判断
print("=" * 30)
print("      成绩等级判断")
print("=" * 30)

score = int(input("请输入分数："))

# 检查分数有效性
if score < 0 or score > 100:
    print("分数无效！")
else:
    # 判断等级
    if score >= 90:
        grade = "A"
        level = "优秀"
    elif score >= 80:
        grade = "B"
        level = "良好"
    elif score >= 70:
        grade = "C"
        level = "中等"
    elif score >= 60:
        grade = "D"
        level = "及格"
    else:
        grade = "F"
        level = "不及格"
    
    # 判断是否及格
    is_pass = score >= 60
    
    # 输出结果
    print(f"\n分数：{score}")
    print(f"等级：{grade}（{level}）")
    if is_pass:
        print("状态：✅ 及格")
    else:
        print("状态：❌ 不及格")
```

**扩展挑战：**
- 添加更多的评价信息
- 给优秀的分数添加特殊祝贺语

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 布尔值 | True 和 False，用于表示真假 |
| 比较运算符 | ==、!=、>、<、>=、<= |
| if 语句 | 根据条件决定是否执行代码 |
| if-else | 条件成立执行一段，不成立执行另一段 |
| if-elif-else | 多个条件依次判断 |
| and | 两边都要 True |
| or | 只要一边 True |
| not | 取反 |

**重要提醒：**
- `if` 后面要有冒号 `:`
- 代码块要缩进（4个空格）
- `=` 是赋值，`==` 是比较

---

## 参考资料

### 官方文档
- [Python 布尔运算](https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python if 语句](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#if-statements)
- [Python 比较运算](https://docs.python.org/zh-cn/3/library/stdtypes.html#comparisons)

### 视频教程
- [Python 条件语句详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python if-else 教程 - 菜鸟教程](https://www.runoob.com/python3/python3-conditional-statements.html)

### 在线练习
- [Python Tutor - 可视化条件执行](https://pythontutor.com/)
- [Codecademy Python 条件语句](https://www.codecademy.com/learn/learn-python-3)
- [LeetCode 简单题练习](https://leetcode.cn/problemset/all/?difficulty=EASY)

### 拓展阅读
- [Python 条件表达式（三元运算符）](https://docs.python.org/zh-cn/3/reference/expressions.html#conditional-expressions)
- [代码缩进的重要性](https://peps.python.org/pep-0008/#indentation)
