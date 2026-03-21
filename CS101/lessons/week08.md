# 第 8 周：函数入门

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块三：函数与模块 |
| **课时** | 1.5 小时 |
| **关键词** | 函数、def、参数、返回值、代码复用 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解为什么需要函数
2. 定义和调用函数
3. 使用参数传递数据给函数
4. 使用 return 返回函数结果
5. 理解代码复用的重要性

---

## 复习回顾（5 分钟）

前几周我们学习了：
- 列表和字典的嵌套使用
- 复杂数据结构的设计

**快速提问：**
- 如何访问嵌套字典中的数据？
- 列表中的字典通常用来做什么？

---

## 教学内容

### 第一部分：为什么需要函数？（15 分钟）

#### 1.1 重复代码的问题

```python
# 不使用函数：计算多个学生的平均分
# 学生1
scores1 = [90, 85, 88]
total1 = 0
for score in scores1:
    total1 += score
avg1 = total1 / len(scores1)
print(f"学生1平均分：{avg1}")

# 学生2（复制同样的代码）
scores2 = [78, 82, 90]
total2 = 0
for score in scores2:
    total2 += score
avg2 = total2 / len(scores2)
print(f"学生2平均分：{avg2}")

# 学生3（再复制一遍...）
# 如果要修改计算方式，要改多处！
```

**问题：**
- 代码重复，浪费时间
- 难以维护，改一处要改多处
- 容易出错

#### 1.2 函数的优势

```python
# 使用函数：只写一次，多处调用
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

# 调用函数
print(f"学生1平均分：{calculate_average([90, 85, 88])}")
print(f"学生2平均分：{calculate_average([78, 82, 90])}")
print(f"学生3平均分：{calculate_average([95, 92, 88])}")
```

**函数的好处：**
- **代码复用**：写一次，用多次
- **易于维护**：改一处，处处生效
- **代码清晰**：功能独立，结构清晰
- **减少错误**：减少复制粘贴带来的错误

---

### 第二部分：定义与调用函数（30 分钟）

#### 2.1 函数定义语法

```python
def 函数名(参数1, 参数2, ...):
    """文档字符串：描述函数的功能"""
    # 函数体（要缩进）
    代码...
    return 返回值  # 可选
```

#### 2.2 最简单的函数

```python
# 定义一个无参数、无返回值的函数
def say_hello():
    print("Hello, World!")

# 调用函数
say_hello()  # 输出：Hello, World!
say_hello()  # 可以多次调用
```

**注意：**
- `def` 是定义函数的关键字
- 函数名后面有括号和冒号
- 函数体需要缩进
- 定义函数不会执行代码，调用才会执行

#### 2.3 带参数的函数

参数让函数更灵活，可以处理不同的数据。

```python
# 带一个参数
def greet(name):
    print(f"你好，{name}！")

greet("小明")   # 输出：你好，小明！
greet("小红")   # 输出：你好，小红！

# 带多个参数
def introduce(name, age):
    print(f"我叫{name}，今年{age}岁。")

introduce("小明", 16)  # 输出：我叫小明，今年16岁。
introduce("小红", 17)  # 输出：我叫小红，今年17岁。
```

```
函数调用过程：
greet("小明")
    ↓
name = "小明"  （参数赋值）
    ↓
执行函数体
    ↓
print(f"你好，{name}！")
```

#### 2.4 形参和实参

```python
def greet(name):      # name 是「形参」（形式参数）
    print(f"你好，{name}！")

greet("小明")          # "小明" 是「实参」（实际参数）
```

- **形参（Parameter）**：定义函数时的参数，是占位符
- **实参（Argument）**：调用函数时传入的具体值

---

### 第三部分：参数与返回值（35 分钟）

#### 3.1 return 语句

`return` 让函数把结果返回给调用者。

```python
# 没有 return（或 return None）
def greet(name):
    print(f"你好，{name}！")

result = greet("小明")
print(result)  # None

# 有 return
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# return 会立即结束函数
def check_age(age):
    if age < 0:
        return "年龄无效"
    if age >= 18:
        return "成年人"
    return "未成年人"

print(check_age(20))   # 成年人
print(check_age(15))   # 未成年人
print(check_age(-5))   # 年龄无效
```

#### 3.2 返回多个值

Python 函数可以返回多个值（实际上是返回元组）。

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"最小值：{minimum}, 最大值：{maximum}")
# 最小值：1, 最大值：9
```

#### 3.3 实用示例

```python
# 示例1：计算圆的面积
def circle_area(radius):
    """计算圆的面积"""
    pi = 3.14159
    return pi * radius ** 2

area = circle_area(5)
print(f"半径为5的圆面积：{area:.2f}")

# 示例2：判断是否为偶数
def is_even(number):
    """判断数字是否为偶数"""
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# 示例3：生成问候语
def create_greeting(name, time_of_day="早上"):
    """生成问候语"""
    return f"{time_of_day}好，{name}！"

print(create_greeting("小明"))           # 早上好，小明！
print(create_greeting("小明", "下午"))   # 下午好，小明！
```

#### 3.4 函数的执行流程

```python
def calculate(a, b):
    print("开始计算...")
    result = a + b
    print("计算完成！")
    return result

print("程序开始")
answer = calculate(3, 5)
print(f"结果是：{answer}")
print("程序结束")
```

输出：
```
程序开始
开始计算...
计算完成！
结果是：8
程序结束
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：重构猜数字游戏

将之前的猜数字游戏重构为使用函数的版本。

**示例代码框架：**

```python
import random

def generate_secret():
    """生成随机数"""
    return random.randint(1, 100)

def get_guess():
    """获取用户猜测"""
    while True:
        try:
            guess = int(input("请输入你的猜测（1-100）："))
            if 1 <= guess <= 100:
                return guess
            else:
                print("请输入1-100之间的数字！")
        except ValueError:
            print("请输入有效的数字！")

def check_guess(guess, secret):
    """检查猜测结果，返回提示信息"""
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too_low"
    else:
        return "too_high"

def play_game():
    """游戏主函数"""
    print("=" * 40)
    print("        猜数字游戏")
    print("=" * 40)
    print("我想了一个1-100之间的数字，猜猜看！\n")
    
    secret = generate_secret()
    attempts = 0
    
    while True:
        guess = get_guess()
        attempts += 1
        result = check_guess(guess, secret)
        
        if result == "correct":
            print(f"\n🎉 恭喜你猜对了！")
            print(f"答案是 {secret}")
            print(f"你总共猜了 {attempts} 次")
            break
        elif result == "too_low":
            print("📈 太小了，再大一点！")
        else:
            print("📉 太大了，再小一点！")

# 运行游戏
play_game()
```

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 函数 | 可重复使用的代码块 |
| def | 定义函数的关键字 |
| 参数 | 传递给函数的数据 |
| return | 返回函数的结果 |
| 形参/实参 | 定义时的参数/调用时的值 |

**函数的好处：**
- 代码复用
- 易于维护
- 结构清晰
- 减少错误

---

## 参考资料

### 官方文档
- [Python 函数定义](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions)
- [Python 函数参数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#more-on-defining-functions)

### 视频教程
- [Python 函数详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 函数教程 - 菜鸟教程](https://www.runoob.com/python3/python3-function.html)

### 在线练习
- [Python Tutor - 可视化函数调用](https://pythontutor.com/)
- [Codecademy Python 函数](https://www.codecademy.com/learn/learn-python-3)
- [Exercism Python Track](https://exercism.org/tracks/python)

### 拓展阅读
- [Python 函数最佳实践](https://realpython.com/defining-your-own-python-function/)
- [代码复用的重要性](https://en.wikipedia.org/wiki/Code_reuse)
