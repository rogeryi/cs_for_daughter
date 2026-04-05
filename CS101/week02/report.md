# CS101 Week02 学习报告

**学习者**: Amos  
**日期**: 2026年4月5日

---

## 今日学习内容

### 1. 条件语句 (if/elif/else)

**核心概念**: 让程序根据不同情况做出不同反应

```python
identity_choice = input("请输入选项编号 (1/2/3): ")

if identity_choice == "1":
    identity = "战士"
elif identity_choice == "2":
    identity = "法师"
elif identity_choice == "3":
    identity = "刺客"
else:
    print("无效选择")
    identity = "战士"
```

**逻辑流程**:
```
输入 → 判断 → 执行对应分支
```

---

### 2. 循环结构

#### while 循环 - 重复执行

```python
while True:  # 无限循环
    # 分配属性...
    
    redo = input("是否重新分配属性? (yes/no): ")
    if redo.lower() == 'yes':
        continue  # 继续循环
    else:
        break  # 退出循环
```

#### for 循环 - 遍历集合

```python
stat_names = ["生命", "攻击", "防御", "智力", "魅力", "灵巧", "速度"]

for stat in stat_names:
    print(f"当前 {stat}: {final_stats[stat]}")
```

---

### 3. 用户输入 input()

```python
# 获取文字输入
name = input("请输入你的名字: ")

# 获取数字输入（需要转换）
age = int(input("请输入年龄: "))
birth_month = int(input("请输入月份: "))
```

**注意**: `input()` 返回的是字符串，要用 `int()` 转换成数字。

---

### 4. f-string 格式化

#### 基本用法

```python
name = "Amos"
age = 16
print(f"名字: {name}, 年龄: {age}")
```

#### 浮点数格式化

```python
pi = 3.14159265

print(f"保留2位: {pi:.2f}")    # 3.14
print(f"保留4位: {pi:.4f}")    # 3.1416
print(f"百分比: {0.85:.1%}")   # 85.0%
```

#### 对齐和填充

```python
num = 3.14
print(f"右对齐: {num:>10.2f}")  #       3.14
print(f"左对齐: {num:<10.2f}")  # 3.14
print(f"用0填充: {num:010.2f}") # 0000003.14
```

---

### 5. 字典的进阶使用

#### 嵌套字典

```python
character_stats = {
    "战士": {"生命": 6, "攻击": 6, "防御": 6},
    "法师": {"生命": 3, "攻击": 2, "防御": 2},
    "刺客": {"生命": 4, "攻击": 4, "防御": 2}
}

# 获取战士的生命
stats = character_stats["战士"]
hp = stats["生命"]  # 6
```

#### 字典方法

```python
# 复制字典
final_stats = stats.copy()

# 求所有值的和
total = sum(stats.values())

# 遍历键值对
for key, value in stats.items():
    print(f"{key}: {value}")
```

---

### 6. 字符串方法

```python
text = "Yes"

# 转小写
print(text.lower())  # "yes"

# 比较（忽略大小写）
if text.lower() == "yes":
    print("匹配！")
```

---

### 7. Emoji 和 Unicode

Python 支持直接使用 Emoji：

```python
print("❤️ 生命")    # 红心
print("⚔️ 攻击")   # 交叉的剑
print("🛡️ 防御")   # 盾牌
print("✨ 魅力")    # 火花
```

这些是 **Unicode 编码**，可以直接复制粘贴使用。

---

## 实践项目

### 项目1: 游戏角色创建系统 (game_login.py)

**功能**:
- ✅ 玩家输入名字、性别、出生日期
- ✅ 3个职业选择（战士/法师/刺客）
- ✅ 不同职业有不同基础属性
- ✅ 15点可支配属性自由分配
- ✅ 支持无限次重新分配
- ✅ 可视化属性条

**运行**:
```bash
python3 /Users/roger/cs/CS101/week02/game_login.py
```

---

### 项目2: 《蝴蝶冢》恐怖解密 RPG

**游戏设定**:
- 📖 魔幻现实主义叙事（《百年孤独》风格）
- 🎮 超现实解密体验（《锈湖》风格）
- 🦋 核心设定：人死后尸体会飞出蝴蝶
- 📍 背景：雪原森林深处的"蝶栖镇"

**已实现场景**:

| 场景 | NPC | 特色 |
|------|-----|------|
| 归蝶客栈 | 蝶婆婆 | 登记簿密码锁 |
| 蝶梦亭 | 白 | 记忆之酒的秘密 |
| 镇魂碑 | - | 七蝶机关解密 |

**解密元素**:
- 🔐 登记簿密码锁（答案：5）
- 🗺️ 破旧地图揭示井的秘密
- 🔦 蓝色蝶灯看见蝴蝶记忆
- 📜 镇魂碑揭示小镇规则

**运行**:
```bash
python3 /Users/roger/cs/CS101/蝴蝶冢/game.py
```

---

## 新学英文词汇

| 中文 | 英文 |
|------|------|
| 条件语句 | Conditional Statement |
| 循环 | Loop |
| 输入 | Input |
| 格式化 | Formatting |
| 字典 | Dictionary |
| 遍历 | Iterate/Traverse |
| 副本 | Copy |
| 属性 | Attribute/Stat |

---

## 重要发现

### 1. 不同类型的运算
```python
age = 16
age_str = "16"

print(age + 1)      # 17 (整数加法)
print(age_str + "1") # "161" (字符串拼接)
```

### 2. 列表索引从0开始
```python
hobbies = ["游戏", "编程", "画画"]
print(hobbies[0])  # "游戏"（第一个）
print(hobbies[2])  # "画画"（第三个）
```

### 3. 字典查找很快
```python
# 直接用名字找值，不用遍历
stats = character_stats["战士"]  # 瞬间找到
```

---

## 下次学习预告

- 函数定义和调用
- 模块化编程
- 《蝴蝶冢》更多场景和谜题开发
- 文件读写（保存游戏进度）

---

## 今日代码文件

```
CS101/
├── week02/
│   ├── game_login.py    # 角色创建系统
│   └── report.md        # 学习报告 ← 本文件
│
└── 蝴蝶冢/
    ├── README.md        # 项目说明
    └── game.py          # 游戏主程序
```

---

**总结**: 今天学习了条件语句、循环、用户输入和格式化输出，完成了两个完整的项目。特别是《蝴蝶冢》游戏，融合了恐怖、解密和魔幻现实主义元素，是编程和创意的完美结合！

**明日目标**: 继续完善《蝴蝶冢》，添加更多场景和复杂谜题，同时学习函数的使用。

---

*"在雪原上，蝴蝶是唯一的色彩；在代码里，逻辑是唯一的方向。"*
