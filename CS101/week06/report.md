# CS101 Week06 学习报告

**学习者**: Amos  
**日期**: 2026年5月2日  
**课程主题**: 字典——有名字的数据

---

## 一、本周课程核心知识点（Week 06）

### 1. 字典的概念与创建

**什么是字典？**
字典是一种存储**键值对（key-value）**的数据结构，就像一本真正的词典。

```python
# 创建字典
student = {
    "name": "小明",
    "age": 16,
    "grade": "高一",
    "score": 95
}

# 空字典
empty_dict = {}

# 访问字典
print(student["name"])  # 小明
print(student["age"])   # 16
```

**字典 vs 列表：**
- 列表：通过**索引**（数字）访问 `list[0]`
- 字典：通过**键**（名字）访问 `dict["name"]`

---

### 2. 字典的增删改操作

**修改值：**
```python
student = {"name": "小明", "score": 95}
student["score"] = 98  # 修改分数
print(student)  # {'name': '小明', 'score': 98}
```

**添加新键值对：**
```python
student["age"] = 16  # 添加年龄
student["grade"] = "高一"  # 添加年级
```

**删除键值对：**
```python
# del 删除
del student["age"]

# pop 删除并返回值
score = student.pop("score")

# clear 清空字典
student.clear()
```

---

### 3. 字典常用方法

```python
student = {"name": "小明", "age": 16, "score": 95}

# 获取所有键
print(student.keys())    # dict_keys(['name', 'age', 'score'])

# 获取所有值
print(student.values())  # dict_values(['小明', 16, 95])

# 获取所有键值对
print(student.items())   # dict_items([('name', '小明'), ('age', 16), ('score', 95)])

# 检查键是否存在
print("name" in student)    # True
print("grade" in student)   # False

# 安全获取值（键不存在时返回默认值）
print(student.get("grade", "未知"))  # 未知
```

---

### 4. 遍历字典

**遍历键：**
```python
for key in student:
    print(key)
# 等价于
for key in student.keys():
    print(key)
```

**遍历值：**
```python
for value in student.values():
    print(value)
```

**遍历键值对（推荐）：**
```python
for key, value in student.items():
    print(f"{key}: {value}")

# 输出：
# name: 小明
# age: 16
# score: 95
```

---

### 5. 嵌套数据结构

**字典嵌套字典：**
```python
students = {
    "001": {"name": "小明", "score": 95},
    "002": {"name": "小红", "score": 88},
    "003": {"name": "小刚", "score": 92}
}

# 访问嵌套数据
print(students["001"]["name"])  # 小明
```

**列表嵌套字典：**
```python
students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 92}
]

# 遍历
for student in students:
    print(f"{student['name']}: {student['score']}")
```

---

### 6. 字典推导式

```python
# 创建数字平方字典
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 过滤字典
scores = {"小明": 95, "小红": 88, "小刚": 92}
excellent = {name: score for name, score in scores.items() if score >= 90}
print(excellent)  # {'小明': 95, '小刚': 92}
```

---

## 二、游戏开发扩展知识

> 以下知识超出了本周学习范畴，但在实际项目中使用了基础知识

### 1. Pygame Zero 游戏引擎进阶

**Pygame Zero 是什么？**
- 基于 Pygame 的简化游戏框架
- 不需要复杂的初始化代码
- 内置游戏循环和事件处理
- 适合快速原型开发

**核心概念：**
```python
import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "我的游戏"

def draw():
    screen.clear()
    # 绘制游戏画面

def update():
    # 更新游戏逻辑
    pass

pgzrun.go()
```

---

### 2. 坐标系统与相机

**世界坐标 vs 屏幕坐标：**
- **世界坐标**：游戏世界中的绝对位置
- **屏幕坐标**：玩家看到的屏幕上的位置
- **相机偏移**：`screen_y = world_y - camera_y`

**相机跟随实现：**
```python
# 相机跟随玩家
camera_y = player['y'] - HEIGHT / 2
camera_y = max(0, min(camera_y, world_height - HEIGHT))

# 绘制时应用相机偏移
draw_y = object_y - camera_y
```

---

### 3. 碰撞检测系统

**矩形碰撞检测（AABB）：**
```python
# Pygame Rect 碰撞检测
player_rect = Rect(player_x, player_y, width, height)
gear_rect = Rect(gear_x, gear_y, 50, 50)

if player_rect.colliderect(gear_rect):
    # 发生碰撞
    player['hp'] -= 20
```

**无敌时间系统：**
```python
# 受伤后无敌时间
if player['invincible'] > 0:
    player['invincible'] -= delta_time
else:
    # 可以受到伤害
    if collision_detected:
        player['hp'] -= damage
        player['invincible'] = 1.0  # 1秒无敌
```

---

### 4. 动画系统

**帧动画原理：**
```python
# 动画状态机
player = {
    'state': 'idle',      # 当前状态
    'anim_frame': 1,      # 当前帧
    'anim_timer': 0,      # 计时器
    'idle_speed': 0.2     # 帧间隔
}

# 更新动画
player['anim_timer'] += delta_time
if player['anim_timer'] >= player['idle_speed']:
    player['anim_timer'] = 0
    player['anim_frame'] = (player['anim_frame'] % 4) + 1
```

**NEAREST 插值（像素风格）：**
```python
# 保持像素风格锐利
gear_img = pygame.transform.rotozoom(gear_img, 0, scale_factor)
# rotozoom 使用 NEAREST 算法，不会模糊
```

---

### 5. 变速移动算法

**正弦函数变速：**
```python
import math

# 计算相对位置 (0.0 ~ 1.0)
position_ratio = (current_x - start_x) / (end_x - start_x)

# 正弦曲线：两端慢，中间快
speed_multiplier = 0.15 + 0.85 * math.sin(position_ratio * math.pi)

# 应用速度
x += base_speed * direction * speed_multiplier
```

**速度分布：**
- 两端（0%, 100%）：0.15x（急刹效果）
- 1/4处（25%）：0.75x
- 中间（50%）：1.0x（最快）
- 3/4处（75%）：0.75x

---

## 三、关键知识点总结

### 基础知识与项目应用的对应关系

| 基础知识 | 在 Pygame Zero 项目中的应用 | 实际场景 |
|---------|---------------------------|----------|
| **字典** | 玩家状态、齿轮配置 | `player = {'hp': 100, ...}` |
| **键值对** | 游戏对象属性 | `gear['x']`, `gear['y']` |
| **嵌套字典** | 复杂对象配置 | `gears = [{'x': ..., ...}, ...]` |
| **字典遍历** | 批量更新游戏对象 | `for gear in gears:` |
| **字典方法** | 安全访问属性 | `player.get('state', 'idle')` |
| **列表+字典** | 游戏对象集合 | `platforms = [Rect(...), ...]` |

---

## 四、实践项目应用

### 项目：《恶魔试炼》- Pygame Zero 完整版

**项目信息：**
- **游戏类型**：垂直平台跳跃游戏
- **开发引擎**：Pygame Zero
- **当前状态**：可玩版本完成

---

### 1. 玩家系统设计

**使用字典管理玩家状态：**
```python
player = {
    'x': 270,
    'y': 607,
    'width': 60,
    'height': 72,
    'speed': 5,
    'vy': 0,
    'jump_force': -15,
    'gravity': 0.8,
    'is_jumping': False,
    'facing': 'right',
    # 动画状态
    'state': 'idle',
    'anim_frame': 1,
    'anim_timer': 0,
    # 生命系统
    'hp': 100,
    'max_hp': 100,
    'invincible': 0,
}
```

**基础知识对应：**
- 键值对存储玩家属性
- 嵌套字典组织相关数据
- 字典访问：`player['hp']`

---

### 2. 齿轮系统设计

**齿轮配置（列表+字典）：**
```python
gears = [
    {'x': 100, 'y': 520 - 50, 'frame': 0, 'timer': 0, 'speed': 0.1,
     'move_x': 100, 'move_speed': 3, 'move_direction': 1, 'move_range': 120,
     'platform_idx': 1},
    {'x': 150, 'y': 360 - 50, 'frame': 0, 'timer': 0, 'speed': 0.1,
     'move_x': 150, 'move_speed': 3, 'move_direction': 1, 'move_range': 120,
     'platform_idx': 3},
]
```

**遍历更新齿轮：**
```python
for gear in gears:
    # 动画更新
    gear['timer'] += delta_time
    if gear['timer'] >= gear['speed']:
        gear['timer'] = 0
        gear['frame'] = (gear['frame'] + 1) % 3
    
    # 移动更新
    gear['x'] += gear['move_speed'] * gear['move_direction']
```

**基础知识对应：**
- 列表存储多个齿轮
- 字典存储单个齿轮属性
- for 循环遍历更新

---

### 3. 碰撞检测系统

**齿轮碰撞（使用字典属性）：**
```python
if player['invincible'] > 0:
    player['invincible'] -= delta_time
else:
    player_rect = Rect(player['x'], player['y'], 
                       player['width'], player['height'])
    
    for gear in gears:
        gear_rect = Rect(gear['x'], gear['y'], 50, 50)
        if player_rect.colliderect(gear_rect):
            player['hp'] -= 20
            player['invincible'] = 1.0
```

**基础知识对应：**
- 字典属性访问
- 条件判断
- 嵌套循环

---

### 4. 坐标系统处理

**相机跟随（世界坐标→屏幕坐标）：**
```python
# 相机偏移
camera_y = player['y'] - HEIGHT / 2

# 绘制平台（应用相机）
screen_platform = Rect(
    platform.left, 
    platform.top - camera_y, 
    platform.width, 
    platform.height
)

# 绘制齿轮（应用相机）
draw_y = gear['y'] - camera_y
```

**基础知识对应：**
- 字典存储相机状态
- 数值计算
- 坐标系转换

---

### 5. 变速移动系统

**正弦函数变速（使用 math 模块）：**
```python
import math

# 计算相对位置
position_ratio = (gear['x'] - platform_left) / (platform_right - platform_left)

# 正弦曲线变速
speed_multiplier = 0.15 + 0.85 * math.sin(position_ratio * math.pi)
gear['x'] += gear['move_speed'] * gear['move_direction'] * speed_multiplier
```

**基础知识对应：**
- 数学计算
- 字典属性更新
- 边界检测

---

### 6. 项目文件结构

```
CS101/week06/
├── 恶魔试炼/
│   ├── game_v2.py              # 主游戏文件（754行）
│   ├── 齿轮1.png               # 齿轮动画帧1
│   ├── 齿轮2.png               # 齿轮动画帧2
│   ├── 齿轮3.png               # 齿轮动画帧3
│   ├── demo墙砖.png            # 平台纹理
│   └── sounds/                 # 音效文件夹
│       ├── jump.wav
│       ├── land.wav
│       ├── fail.wav
│       ├── win.wav
│       ├── menu.wav
│       └── bgm.wav
│
── 场景测试/
│   ├── test_full_animation.py  # 场景测试文件（524行）
│   ├── 齿轮1.png
│   ├── 齿轮2.png
│   ├── 齿轮3.png
│   └── demo墙砖.png
│
├── lessons/
│   └── week06.md               # 第6周课程：字典
│
└── report.md                   # 学习报告 ← 本文件
```

**代码统计：**
- 主游戏文件：754 行
- 场景测试文件：524 行
- **总计：1278 行代码**

---

## 五、学习反思

### 通过本周学习，我理解了：

1. **字典是组织数据的核心工具**
   - 游戏中的所有对象都用字典管理属性
   - 键值对让代码更易读、更易维护
   - 嵌套字典可以组织复杂的数据结构

2. **坐标系统的重要性**
   - 世界坐标和屏幕坐标的区别
   - 相机系统的实现原理
   - 绘制和碰撞检测的坐标一致性

3. **游戏开发的工程思维**
   - 从原型（场景测试）到完整版（恶魔试炼）
   - 模块化设计（玩家、齿轮、平台分离）
   - 调试和修复问题（齿轮位置、相机偏移）

4. **数学在游戏中的应用**
   - 正弦函数实现变速移动
   - 坐标系转换
   - 碰撞检测算法

---

### 思考题

1. **字典 vs 列表的选择**
   - 什么时候用字典？（有名字的数据）
   - 什么时候用列表？（有序集合）
   - 游戏中如何结合使用？

2. **坐标系统的设计**
   - 为什么需要相机系统？
   - 如何保持绘制和碰撞的坐标一致？
   - 多图层游戏如何处理相机？

3. **游戏对象的管理**
   - 如何用字典+列表管理多个游戏对象？
   - 如何高效更新和渲染？
   - 如何处理对象的生命周期？

---

## 六、下次学习预告

下周我们将学习：
- **函数（Functions）** - 组织代码的利器
- **参数和返回值** - 让函数更灵活
- **模块化编程** - 把代码分成小块

**提前思考：**
- 如果把所有代码写在一个文件里会怎样？
- 如何让代码更容易复用？
- 函数和字典如何结合使用？

---

## 七、今日代码文件

```
CS101/
├── lessons/
│   └── week06.md              # 第6周课程：字典
│
├── week06/
│   ├── 恶魔试炼/
│   │   ├── game_v2.py        # 754 行（主游戏）
│   │   ├── 齿轮1.png
│   │   ├── 齿轮2.png
│   │   ├── 齿轮3.png
│   │   ├── demo墙砖.png
│   │   ── sounds/
│   │
│   └── 场景测试/
│       ├── test_full_animation.py  # 524 行（测试）
│       ├── 齿轮1.png
│       ├── 齿轮2.png
│       ├── 齿轮3.png
│       └── demo墙砖.png
│
└── week06/
    └── report.md             # 学习报告 ← 本文件
```

---

**总结**: 本周学习了字典和嵌套数据结构，这是组织复杂数据的核心工具。完成了《恶魔试炼》游戏的开发，实现了完整的平台跳跃系统、齿轮动画系统、碰撞检测系统和相机跟随系统。通过场景测试到正式版本的迭代，理解了游戏开发的工程化流程。字典在游戏中无处不在：玩家状态、齿轮配置、平台属性等。结合列表，可以高效管理多个游戏对象！

**明日目标**: 继续学习函数的定义和使用，将游戏代码模块化，提高代码的可维护性。

---

*"字典让数据有了名字，结构让游戏有了灵魂，代码让梦想成为现实。"*
