# CS101 Week03 学习报告

**学习者**: Amos  
**日期**: 2026年4月18日

---

## 今日学习内容

### 1. 布尔值 (Boolean)

**核心概念**: 布尔值只有两个：`True`（真）和 `False`（假），是条件判断的基础

```python
is_student = True
is_adult = False

print(type(is_student))  # <class 'bool'>
```

**实际应用**:
```python
score = 85
is_pass = score >= 60  # True
is_perfect = score == 100  # False
```

---

### 2. 比较运算符

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `==` | 等于 | `5 == 5` | `True` |
| `!=` | 不等于 | `5 != 3` | `True` |
| `>` | 大于 | `5 > 3` | `True` |
| `<` | 小于 | `5 < 3` | `False` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `5 <= 3` | `False` |

**重要区别**:
```python
x = 5      # 赋值：把 5 放进 x
x == 5     # 比较：x 是否等于 5？返回 True
```

---

### 3. 条件语句 (if/elif/else)

#### 基础 if 语句
```python
age = 16

if age >= 18:
    print("你是成年人")
```

#### if-else 语句
```python
if age >= 18:
    print("你是成年人")
else:
    print("你还未成年")
```

#### if-elif-else 多分支
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

**执行流程**: 从上到下依次判断，一旦某个条件成立，执行对应代码后**立即结束**，不再判断后续条件。

---

### 4. 逻辑运算符

| 运算符 | 含义 | 说明 |
|--------|------|------|
| `and` | 与 | 两边都为 True 结果才是 True |
| `or` | 或 | 只要一边为 True 结果就是 True |
| `not` | 非 | 取反，True 变 False |

**实际应用**:
```python
# and：两个条件都要满足
if age >= 18 and has_ticket:
    print("可以入场")

# or：满足一个就行
if has_ticket or is_vip:
    print("可以进入")

# not：取反
if not is_vip:
    print("普通用户")
```

**优先级**: `not` > `and` > `or`

---

### 5. 嵌套条件语句

条件语句可以嵌套使用：

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

---

### 6. 面向对象编程入门 (OOP)

**类 (Class)**: 对象的模板，定义属性和方法

```python
class Character:
    """角色类"""
    def __init__(self, name, hp, attack):
        self.name = name          # 属性
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.alive = True
    
    def take_damage(self, damage):
        """方法：受到伤害"""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
```

**对象 (Object)**: 类的实例

```python
# 创建角色对象
hero = Character("救世主", 100, 20)
monster = Character("岩壳甲虫", 50, 10)

# 调用方法
hero.take_damage(10)
print(hero.hp)  # 90
```

---

### 7. 游戏开发中的状态管理

**角色状态追踪**:
```python
self.shield = 0              # 护盾
self.buff_attack = 0         # 攻击增益
self.debuff_defense = 0      # 防御削弱
self.is_frozen = False       # 是否被冻结
self.energy = 50             # 能量值
self.resurrection_used = False  # 复活是否已使用
```

**战斗流程控制**:
```python
while player.alive and enemy.alive:
    # 玩家回合
    player.attack(enemy)
    
    # 敌人回合
    enemy.attack(player)
```

---

## 实践项目

### 项目：《天哪，是五彩缤纷的天降救世主😱》

**项目类型**: 回合制对战 RPG 游戏  
**代码量**: 1119 行  
**文件**: `color_savior.py`

---

#### 📖 游戏背景

源彩大陆原本是一个五彩缤纷的世界，居民热爱艺术、色彩和设计。直到有一天，黑白影子出现，夺走了所有色彩。一个五彩的人突然出现，承诺为大家夺回应有的颜色。

---

#### 🎮 游戏特色

**核心玩法**:
- ✅ 回合制战斗系统
- ✅ 三原色元素克制（红→黄→蓝→红）
- ✅ 3 个关卡 + 最终决战
- ✅ 4 位可招募伙伴
- ✅ 技能能量系统
- ✅ 状态效果（护盾、冻结、增益/减益）
- ✅ Boss 多阶段战斗
- ✅ 成就系统

**三原色克制关系**:
```
🔴 红色 克制 🟡 黄色
🟡 黄色 克制 🔵 蓝色
🔵 蓝色 克制 🔴 红色
```

---

#### 🎯 游戏流程

```
新手教程（3回合）
    ↓
休息时刻 → 招募芙丽雅（治疗）
    ↓
第一关：大地的回响（5回合，黄色主题）
    ↓
休息时刻 → 招募阿卡列（输出）
    ↓
第二关：火焰的怒嚎（6回合，红色主题）
    ↓
休息时刻 → 招募厄希斯（防御）
    ↓
第三关：大海的咆哮（7回合，蓝色主题）
    ↓
决战前夕 → 招募莱因克雷德（辅助）
    ↓
最终决战（无限回合，三阶段 Boss）
```

---

#### 👥 角色设计

| 角色 | 性别 | 定位 | 技能特色 |
|------|------|------|----------|
| 芙丽雅 | 女 | 治疗 | 神圣祷言、圣愈之光、复活恩典 |
| 阿卡列 | 男 | 输出 | 断钢斩、血偿、战鬼觉醒 |
| 厄希斯 | 女 | 防御 | 霜骨壁垒、命运纺线、终焉之茧 |
| 莱因克雷德 | 男 | 辅助 | 解析之眼、活性秘药、知识共鸣 |

---

#### 🐉 Boss 设计

**第一关 Boss**：「亘古岩心」戈尔姆
- 地裂崩碎（黄）- 全体重击
- 晶化护甲（黄）- 提升防御
- 岩浆喷涌（红）- 跨界攻击
- 核心共鸣（蓝）- 恢复生命

**第二关 Boss**：「焚世者」伊格尼图斯
- 末日烈焰（红）- 火焰群攻
- 不灭之躯（红）- 濒死恢复
- 熔岩护甲（黄）- 反伤
- 爆炎新星（蓝）- 爆发攻击

**第三关 Boss**：「深渊之主」塔拉萨
- 海啸吞没（蓝）- 水压群攻
- 深海再生（蓝）- 持续恢复
- 漩涡牵引（蓝）- 攻击三人
- 绝对零度（黄）- 冻结目标

**最终 Boss**：黑白之主（三阶段）

---

#### 🏆 成就系统

| 成就 | 条件 |
|------|------|
| 天哪，是五彩缤纷的天降救世主😱 | 通关 |
| 殒落的五彩之星 | 未通关 |
| 我是一头绚烂的孤狼 | 无伙伴通关 |
| 叽里咕噜说什么呢，和我的羁绊说去吧 | 全伙伴通关 |
| 我说艺术就是创造，你耳朵聋吗 | 最终战 20 回合内结束 |

---

#### 💻 技术亮点

**面向对象设计**:
```python
class Character:
    """角色基类"""
    def __init__(self, name, hp, attack, defense, element, role="输出"):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        # ... 更多属性
    
    def take_damage(self, damage, attack_element=None):
        """受到伤害（包含元素克制、护盾、弱点标记）"""
        # 元素克制计算
        # 防御计算
        # 护盾吸收
        # ...
```

**元素克制系统**:
```python
def get_element_multiplier(attacker, defender):
    """计算元素克制倍率"""
    # 红克黄、黄克蓝、蓝克红
    if (attacker == "红" and defender == "黄") or \
       (attacker == "黄" and defender == "蓝") or \
       (attacker == "蓝" and defender == "红"):
        return 1.5  # 克制伤害 ×1.5
    return 1.0  # 正常伤害
```

**技能能量系统**:
```python
def use_skill(self, energy_cost):
    """尝试使用技能"""
    if self.energy >= energy_cost:
        self.energy -= energy_cost
        return True
    return False
```

**状态管理**:
```python
# 护盾系统
if self.shield > 0:
    if self.shield >= actual_damage:
        self.shield -= actual_damage
        actual_damage = 0
    else:
        actual_damage -= self.shield
        self.shield = 0

# 冻结效果
if self.is_frozen:
    self.is_frozen = False
    print(f"❄️ {self.name} 被冻结，无法行动！")
```

---

#### 📊 游戏规模

| 指标 | 数量 |
|------|------|
| 总代码行数 | 1119 行 |
| 可玩角色 | 5 个（主角 + 4 伙伴）|
| 普通敌人 | 9 种 |
| Boss | 4 个（含三阶段最终 Boss）|
| 技能数量 | 20+ 个 |
| 成就 | 5 个 |
| 关卡 | 3 + 1 最终战 |

---

## 新学英文词汇

| 中文 | 英文 |
|------|------|
| 布尔值 | Boolean |
| 比较运算符 | Comparison Operator |
| 条件语句 | Conditional Statement |
| 逻辑运算 | Logical Operation |
| 类 | Class |
| 对象 | Object |
| 属性 | Attribute/Property |
| 方法 | Method |
| 初始化 | Initialize |
| 实例 | Instance |
| 继承 | Inheritance |
| 封装 | Encapsulation |
| 元素克制 | Element Counter |
| 护盾 | Shield |
| 增益 | Buff |
| 减益 | Debuff |
| 冻结 | Freeze |
| 能量 | Energy |
| 回合制 | Turn-based |
| 成就 | Achievement |

---

## 重要发现

### 1. 条件语句的执行顺序
```python
score = 95

# 错误写法（会打印两次）
if score >= 60:
    print("及格")
if score >= 90:
    print("优秀")

# 正确写法（只打印一次）
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
```
**关键**: `elif` 确保一旦某个条件成立，后续条件不再判断。

### 2. `=` 和 `==` 的区别
```python
x = 5      # 赋值：把 5 放进变量 x
x == 5     # 比较：x 等于 5 吗？返回 True
```
这是初学者最容易犯的错误！

### 3. 面向对象的威力
使用类可以将数据和操作封装在一起：
```python
# 不使用类：数据和操作分离
hero_hp = 100
hero_attack = 20
# 需要手动管理...

# 使用类：数据和操作封装
hero = Character("救世主", 100, 20)
hero.take_damage(10)  # 自动处理
```

### 4. 游戏状态管理
复杂游戏需要追踪大量状态：
- 生命值、护盾、能量
- 增益/减益效果
- 特殊状态（冻结、眩晕等）
- 技能使用次数限制

合理的数据结构让代码更清晰！

### 5. 元素克制系统
三原色克制形成了策略深度：
```
玩家需要根据敌人属性选择攻击元素
→ 增加了游戏的策略性
→ 让战斗更有趣
```

---

## 与前两周的对比

| 周次 | 代码量 | 项目复杂度 | 核心概念 |
|------|--------|-----------|----------|
| Week 01 | ~60 行 | 简单程序 | 变量、print、数据类型 |
| Week 02 | ~146 行 | 交互程序 | input、条件、循环、字典 |
| Week 03 | **1119 行** | **完整游戏** | **OOP、状态管理、游戏系统** |

**进步巨大！** 从简单的信息卡片到完整的回合制 RPG 游戏！

---

## 下次学习预告

- 函数参数和返回值深入
- 模块化和代码组织
- 文件读写（保存游戏进度）
- 错误处理（try-except）
- 《色彩救世主》功能完善和 BUG 修复

---

## 今日代码文件

```
CS101/
├── week03/
│   ├── color_savior.py    # 色彩救世主游戏（1119行）
│   ├── aa.py              # 辅助函数练习
│   ├── plan.md            # 游戏设计文档
│   └── report.md          # 学习报告 ← 本文件
```

---

**总结**: 今天是突破性的一周！学习了布尔值、比较运算、条件语句和逻辑运算，更重要的是开始使用面向对象编程开发了一个完整的回合制 RPG 游戏。《色彩救世主》有 1119 行代码，包含完整的战斗系统、元素克制、角色招募、成就系统。这是一个真正的游戏项目！

**明日目标**: 继续完善游戏，修复可能的 BUG，添加更多细节和动画效果，同时深入学习函数的高级用法。

---

*"在源彩大陆，色彩是生命的力量；在代码世界，逻辑是创造的灵魂。"*
