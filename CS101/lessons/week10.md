# 第 10 周：模块与文件

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块三：函数与模块 |
| **课时** | 1.5 小时 |
| **关键词** | 模块、import、random、文件读写、JSON |

---

## 学习目标

完成本节课后，学生将能够：

1. 导入和使用 Python 模块
2. 熟练使用 random 模块
3. 读写文本文件
4. 使用 JSON 保存和加载数据

---

## 教学内容

### 第一部分：模块的导入与使用（25 分钟）

#### 1.1 什么是模块？

模块是包含 Python 代码的文件，可以包含函数、类和变量。使用模块可以：
- 复用他人写好的代码
- 组织自己的代码
- 避免命名冲突

#### 1.2 导入模块的方式

```python
# 方式1：导入整个模块
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

# 方式2：导入特定内容
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793

# 方式3：导入所有内容（不推荐）
from math import *
print(sqrt(16))

# 方式4：使用别名
import math as m
print(m.sqrt(16))  # 4.0

from math import sqrt as square_root
print(square_root(16))  # 4.0
```

#### 1.3 常用内置模块

| 模块 | 用途 |
|------|------|
| `math` | 数学函数 |
| `random` | 随机数 |
| `datetime` | 日期时间 |
| `os` | 操作系统交互 |
| `json` | JSON 处理 |

---

### 第二部分：random 模块详解（20 分钟）

#### 2.1 常用函数

```python
import random

# randint(a, b)：返回 [a, b] 范围内的随机整数
print(random.randint(1, 100))  # 1到100的随机整数

# random()：返回 [0, 1) 范围内的随机浮点数
print(random.random())  # 如 0.7234...

# uniform(a, b)：返回 [a, b] 范围内的随机浮点数
print(random.uniform(1.5, 6.5))

# choice(seq)：从序列中随机选择一个元素
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(random.choice(fruits))

# choices(seq, k=n)：随机选择多个元素（可重复）
print(random.choices(fruits, k=3))

# sample(seq, k=n)：随机选择多个元素（不重复）
print(random.sample(fruits, k=3))

# shuffle(seq)：打乱列表顺序（原地修改）
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)
```

#### 2.2 游戏应用示例

```python
import random

# 抽奖系统
def lottery(prizes):
    """从奖品列表中随机抽取一个"""
    return random.choice(prizes)

# 掷骰子
def roll_dice(sides=6):
    """掷一个指定面数的骰子"""
    return random.randint(1, sides)

# 生成随机敌人
def generate_enemy():
    """生成随机敌人"""
    names = ["哥布林", "史莱姆", "骷髅", "蝙蝠"]
    return {
        "name": random.choice(names),
        "hp": random.randint(10, 50),
        "attack": random.randint(5, 15)
    }
```

---

### 第三部分：文件读写基础（35 分钟）

#### 3.1 打开和关闭文件

```python
# 基本方式（需要手动关闭）
file = open("test.txt", "w")
file.write("Hello, World!")
file.close()

# 推荐方式：使用 with 语句（自动关闭）
with open("test.txt", "w") as file:
    file.write("Hello, World!")
# 文件在 with 块结束后自动关闭
```

#### 3.2 文件打开模式

| 模式 | 说明 |
|------|------|
| `"r"` | 读取（默认），文件必须存在 |
| `"w"` | 写入，会覆盖已有内容 |
| `"a"` | 追加，在文件末尾添加内容 |
| `"r+"` | 读写 |

#### 3.3 写入文件

```python
# 写入文本
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("第一行\n")
    file.write("第二行\n")

# 写入多行
lines = ["苹果", "香蕉", "橙子"]
with open("fruits.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

# 追加内容
with open("fruits.txt", "a", encoding="utf-8") as file:
    file.write("葡萄\n")
```

#### 3.4 读取文件

```python
# 读取全部内容
with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 按行读取
with open("fruits.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() 去除换行符

# 读取为列表
with open("fruits.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)  # ['苹果\n', '香蕉\n', ...]
```

#### 3.5 JSON 文件

JSON 是一种通用的数据格式，非常适合保存游戏存档等结构化数据。

```python
import json

# 保存数据到 JSON 文件
player = {
    "name": "勇者",
    "level": 10,
    "hp": 100,
    "inventory": ["剑", "盾", "药水"]
}

with open("save.json", "w", encoding="utf-8") as file:
    json.dump(player, file, ensure_ascii=False, indent=2)

# 从 JSON 文件加载数据
with open("save.json", "r", encoding="utf-8") as file:
    loaded_player = json.load(file)
    print(loaded_player)
    print(f"玩家名：{loaded_player['name']}")
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：存档功能实现

为之前的程序添加保存和加载功能。

```python
import json

def save_game(data, filename="save.json"):
    """保存游戏数据"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print(f"✅ 游戏已保存到 {filename}")

def load_game(filename="save.json"):
    """加载游戏数据"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"✅ 已从 {filename} 加载游戏")
        return data
    except FileNotFoundError:
        print(f"❌ 存档文件 {filename} 不存在")
        return None

# 测试
player = {
    "name": "小明",
    "level": 5,
    "hp": 80,
    "gold": 150,
    "inventory": ["铁剑", "皮甲", "生命药水"]
}

# 保存
save_game(player)

# 加载
loaded = load_game()
if loaded:
    print(f"玩家：{loaded['name']}, 等级：{loaded['level']}")
```

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| import | 导入模块使用其功能 |
| random | 生成随机数和随机选择 |
| open() | 打开文件，配合 with 使用 |
| read/write | 读取和写入文件内容 |
| json | 保存和加载结构化数据 |

---

## 参考资料

### 官方文档
- [Python 模块](https://docs.python.org/zh-cn/3/tutorial/modules.html)
- [random 模块](https://docs.python.org/zh-cn/3/library/random.html)
- [文件读写](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#reading-and-writing-files)
- [json 模块](https://docs.python.org/zh-cn/3/library/json.html)

### 视频教程
- [Python 模块详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 文件操作 - 菜鸟教程](https://www.runoob.com/python3/python3-file-methods.html)

### 拓展阅读
- [JSON 数据格式](https://www.json.org/json-zh.html)
- [Python 文件路径处理](https://docs.python.org/zh-cn/3/library/pathlib.html)
