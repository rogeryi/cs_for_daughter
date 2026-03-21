# 第 9 周：函数进阶

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块三：函数与模块 |
| **课时** | 1.5 小时 |
| **关键词** | 默认参数、关键字参数、作用域、函数设计 |

---

## 学习目标

完成本节课后，学生将能够：

1. 使用默认参数简化函数调用
2. 使用关键字参数提高代码可读性
3. 理解变量作用域（局部变量和全局变量）
4. 遵循函数设计原则编写高质量代码

---

## 教学内容

### 第一部分：默认参数与关键字参数（25 分钟）

#### 1.1 默认参数

给参数设置默认值，调用时可以省略该参数。

```python
# 带默认参数的函数
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

# 使用默认值
greet("小明")           # 你好，小明！

# 覆盖默认值
greet("小明", "早上好")  # 早上好，小明！
```

**重要规则：** 有默认值的参数必须放在没有默认值的参数后面！

```python
# ✅ 正确
def func(a, b, c=10, d=20):
    pass

# ❌ 错误
# def func(a=10, b):  # SyntaxError
#     pass
```

#### 1.2 关键字参数

调用函数时，可以用参数名指定值，不需要按顺序。

```python
def introduce(name, age, city):
    print(f"我叫{name}，今年{age}岁，来自{city}。")

# 位置参数：按顺序传递
introduce("小明", 16, "北京")

# 关键字参数：用参数名指定
introduce(name="小明", age=16, city="北京")

# 可以打乱顺序
introduce(city="北京", name="小明", age=16)

# 混合使用（位置参数必须在前）
introduce("小明", city="北京", age=16)
```

#### 1.3 实用示例

```python
def create_character(name, hp=100, attack=10, defense=5, level=1):
    """创建游戏角色"""
    return {
        "name": name,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "level": level
    }

# 使用默认值创建普通角色
warrior = create_character("战士")
print(warrior)
# {'name': '战士', 'hp': 100, 'attack': 10, 'defense': 5, 'level': 1}

# 自定义部分属性
mage = create_character("法师", hp=80, attack=15)
print(mage)
# {'name': '法师', 'hp': 80, 'attack': 15, 'defense': 5, 'level': 1}

# 创建高级角色
boss = create_character("魔王", hp=500, attack=50, defense=30, level=10)
print(boss)
```

---

### 第二部分：变量作用域（25 分钟）

#### 2.1 局部变量

在函数内部定义的变量是**局部变量**，只在函数内部有效。

```python
def my_function():
    x = 10  # 局部变量
    print(f"函数内部：x = {x}")

my_function()
# print(x)  # ❌ 错误！x 在函数外部不存在
```

#### 2.2 全局变量

在函数外部定义的变量是**全局变量**，可以在任何地方访问。

```python
y = 20  # 全局变量

def my_function():
    print(f"函数内部可以访问全局变量：y = {y}")

my_function()
print(f"函数外部：y = {y}")
```

#### 2.3 同名变量

函数内部可以有和全局变量同名的局部变量。

```python
x = 100  # 全局变量

def my_function():
    x = 10  # 局部变量，与全局变量同名但不同
    print(f"函数内部：x = {x}")  # 10

my_function()
print(f"函数外部：x = {x}")  # 100（全局变量没变）
```

#### 2.4 global 关键字

如果要在函数内部修改全局变量，需要使用 `global` 关键字。

```python
count = 0  # 全局变量

def increment():
    global count  # 声明使用全局变量
    count += 1

print(f"初始值：{count}")  # 0
increment()
increment()
increment()
print(f"调用后：{count}")  # 3
```

**建议：** 尽量避免使用 global，而是通过参数和返回值传递数据。

```python
# ✅ 推荐的做法
def increment(count):
    return count + 1

count = 0
count = increment(count)
count = increment(count)
print(count)  # 2
```

---

### 第三部分：函数设计原则（20 分钟）

#### 3.1 单一职责原则

每个函数应该只做一件事。

```python
# ❌ 不好：一个函数做了太多事
def process_student(name, scores):
    # 计算平均分
    avg = sum(scores) / len(scores)
    # 判断等级
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    else:
        grade = "C"
    # 打印结果
    print(f"{name}: 平均分{avg}, 等级{grade}")
    # 保存到文件
    with open("students.txt", "a") as f:
        f.write(f"{name},{avg},{grade}\n")

# ✅ 好：每个函数只做一件事
def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    return "C"

def save_to_file(name, avg, grade):
    with open("students.txt", "a") as f:
        f.write(f"{name},{avg},{grade}\n")
```

#### 3.2 命名要有意义

```python
# ❌ 不好
def f(x, y):
    return x * y

# ✅ 好
def calculate_area(width, height):
    return width * height
```

#### 3.3 添加文档字符串

```python
def calculate_bmi(weight, height):
    """
    计算BMI指数
    
    参数：
        weight: 体重（公斤）
        height: 身高（米）
    
    返回：
        BMI值（保留1位小数）
    """
    bmi = weight / (height ** 2)
    return round(bmi, 1)
```

#### 3.4 避免副作用

```python
# ❌ 不好：修改了传入的列表
def add_item(items, item):
    items.append(item)  # 修改了原列表

# ✅ 好：返回新列表
def add_item(items, item):
    return items + [item]  # 不修改原列表
```

---

### 第四部分：课堂练习（20 分钟）

#### 练习：骰子模拟器

创建一个骰子模拟器，包含多种类型的骰子。

```python
import random

def roll_dice(sides=6, count=1):
    """
    投掷骰子
    
    参数：
        sides: 骰子面数（默认6面）
        count: 骰子数量（默认1个）
    
    返回：
        如果count=1，返回单个结果
        如果count>1，返回结果列表
    """
    if count == 1:
        return random.randint(1, sides)
    else:
        return [random.randint(1, sides) for _ in range(count)]

def roll_d6(count=1):
    """投掷6面骰子"""
    return roll_dice(6, count)

def roll_d20(count=1):
    """投掷20面骰子（常用于桌游）"""
    return roll_dice(20, count)

def calculate_total(results):
    """计算骰子结果总和"""
    if isinstance(results, list):
        return sum(results)
    return results

# 测试
print("=== 骰子模拟器 ===\n")

# 投掷1个6面骰子
result = roll_d6()
print(f"投掷1个D6：{result}")

# 投掷3个6面骰子
results = roll_d6(3)
print(f"投掷3个D6：{results}，总计：{calculate_total(results)}")

# 投掷1个20面骰子
result = roll_d20()
print(f"投掷1个D20：{result}")

# 自定义：投掷2个10面骰子
results = roll_dice(sides=10, count=2)
print(f"投掷2个D10：{results}，总计：{calculate_total(results)}")
```

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 默认参数 | 调用时可省略，必须放在最后 |
| 关键字参数 | 用参数名指定值，可打乱顺序 |
| 局部变量 | 函数内部定义，只在函数内有效 |
| 全局变量 | 函数外部定义，任何地方可访问 |
| global | 在函数内修改全局变量（尽量避免） |

**函数设计原则：**
1. 单一职责：每个函数只做一件事
2. 命名清晰：函数名能表达功能
3. 添加文档：说明参数和返回值
4. 避免副作用：不修改传入的参数

---

## 参考资料

### 官方文档
- [Python 函数参数](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python 作用域规则](https://docs.python.org/zh-cn/3/tutorial/classes.html#python-scopes-and-namespaces)

### 视频教程
- [Python 函数进阶 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 变量作用域 - 菜鸟教程](https://www.runoob.com/python3/python3-namespace-scope.html)

### 在线练习
- [Python Tutor - 可视化作用域](https://pythontutor.com/)
- [Exercism Python Track](https://exercism.org/tracks/python)

### 拓展阅读
- [Python 函数式编程](https://docs.python.org/zh-cn/3/howto/functional.html)
- [代码整洁之道](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
