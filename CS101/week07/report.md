# CS101 Week07 学习报告

**学习者**: Amos  
**日期**: 2026年5月9日  
**课程主题**: 综合练习——列表与字典的嵌套

---

## 一、本周课程核心知识点（Week 07）

### 1. 列表中的列表（二维列表）

列表的元素可以是另一个列表，形成"列表中的列表"。

```python
# 二维列表：表示一个 3x3 的棋盘
board = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["O", "X", "O"]
]

# 访问元素：board[行][列]
print(board[0][0])  # O（第1行第1列）
print(board[1][2])  # X（第2行第3列）
print(board[2][1])  # X（第3行第2列）
```

**棋盘结构示意图：**
```
       列0    列1    列2
      ┌─────┬─────┬─────┐
行0   │  O  │  X  │  O  │  board[0]
      ├─────┼──────────┤
行1   │  X  │  O  │  X  │  board[1]
      ├─────┼─────┼─────┤
行2   │  O  │  X  │  O  │  board[2]
      └─────┴─────┴─────┘
```

**遍历二维列表：**
```python
# 打印棋盘
for row in board:
    for cell in row:
        print(cell, end=" ")
    print()  # 换行

# 或者使用索引
for i in range(len(board)):
    for j in range(len(board[i])):
        print(f"board[{i}][{j}] = {board[i][j]}")
```

---

### 2. 字典中的字典

字典的值也可以是另一个字典。

```python
# 嵌套字典：存储多个学生的详细信息
students = {
    "小明": {
        "age": 16,
        "grade": "高一",
        "scores": {"语文": 90, "数学": 95, "英语": 88}
    },
    "小红": {
        "age": 17,
        "grade": "高二",
        "scores": {"语文": 92, "数学": 88, "英语": 95}
    }
}

# 访问嵌套数据
print(students["小明"]["age"])           # 16
print(students["小明"]["scores"]["数学"]) # 95
print(students["小红"]["grade"])         # 高二
```

**遍历嵌套字典：**
```python
for name, info in students.items():
    print(f"\n学生：{name}")
    print(f"  年龄：{info['age']}")
    print(f"  年级：{info['grade']}")
    print("  成绩：")
    for subject, score in info["scores"].items():
        print(f"    {subject}：{score}")
```

---

### 3. 列表中的字典

列表的元素可以是字典，常用于存储多条记录。

```python
# 列表中的字典：学生列表
students = [
    {"name": "小明", "age": 16, "score": 95},
    {"name": "小红", "age": 17, "score": 88},
    {"name": "小刚", "age": 16, "score": 92}
]

# 访问数据
print(students[0]["name"])  # 小明
print(students[1]["score"]) # 88

# 遍历
for student in students:
    print(f"{student['name']}: {student['score']}分")

# 添加新学生
students.append({"name": "小美", "age": 16, "score": 96})
```

---

### 4. 字典中的列表

字典的值可以是列表。

```python
# 字典中的列表：每个学生的多次考试成绩
scores = {
    "小明": [95, 88, 92, 90],
    "小红": [88, 92, 95, 91],
    "小刚": [76, 82, 85, 88]
}

# 访问数据
print(scores["小明"][0])  # 95（小明的第一次成绩）
print(scores["小红"][-1]) # 91（小红的最后一次成绩）

# 计算平均分
for name, score_list in scores.items():
    avg = sum(score_list) / len(score_list)
    print(f"{name}的平均分：{avg:.1f}")
```

---

### 5. 复杂数据结构设计

#### 5.1 设计数据结构的思路

在设计数据结构时，思考以下问题：
1. 要存储什么信息？
2. 信息之间有什么关系？
3. 需要进行什么操作？（查找、遍历、添加、删除）

#### 5.2 游戏角色系统示例

```python
# 游戏角色数据结构
character = {
    "name": "勇者",
    "level": 10,
    "hp": 100,
    "max_hp": 100,
    "attack": 25,
    "defense": 15,
    "skills": ["火球术", "治疗术", "闪避"],
    "inventory": [
        {"name": "生命药水", "type": "consumable", "effect": 50, "count": 3},
        {"name": "铁剑", "type": "weapon", "attack": 10, "count": 1}
    ],
    "equipment": {
        "weapon": "铁剑",
        "armor": "皮甲",
        "accessory": None
    }
}
```

#### 5.3 商品库存系统示例

```python
# 商品库存
inventory = {
    "水果": [
        {"name": "苹果", "price": 5.0, "stock": 100},
        {"name": "香蕉", "price": 3.0, "stock": 150},
        {"name": "橙子", "price": 4.5, "stock": 80}
    ],
    "饮料": [
        {"name": "可乐", "price": 3.5, "stock": 200},
        {"name": "雪碧", "price": 3.5, "stock": 180},
        {"name": "矿泉水", "price": 2.0, "stock": 300}
    ]
}

# 显示所有商品
for category, products in inventory.items():
    print(f"\n【{category}】")
    for product in products:
        print(f"  {product['name']}: ¥{product['price']}, 库存{product['stock']}")
```

---

## 二、游戏开发扩展知识

> 以下知识超出了本周学习范畴，但在实际项目中使用了基础知识

### 1. 复杂数据结构在游戏中的应用

**游戏世界数据模型：**
```python
# 游戏世界数据结构
game_world = {
    "level": 1,
    "player": {
        "name": "西蒙",
        "hp": 100,
        "position": {"x": 270, "y": 607}
    },
    "platforms": [
        {"x": 0, "y": 680, "width": 600, "type": "ground"},
        {"x": 50, "y": 560, "width": 120, "type": "platform"},
        {"x": 250, "y": 430, "width": 120, "type": "platform"}
    ],
    "gears": [
        {"x": 100, "y": 470, "platform_idx": 1, "speed": 3},
        {"x": 150, "y": 310, "platform_idx": 2, "speed": 3}
    ],
    "camera": {
        "y": 0,
        "target_y": 0
    }
}
```

---

### 2. 嵌套数据结构的优势

**组织复杂游戏数据：**
- ✅ **清晰的结构** - 数据分类明确
- ✅ **易于访问** - 通过键名直接访问
- ✅ **灵活扩展** - 可以轻松添加新属性
- ✅ **批量处理** - 用 for 循环遍历

**对比简单数据结构：**
```python
# ❌ 不好的方式：分散的变量
player_name = "西蒙"
player_hp = 100
player_x = 270
player_y = 607

# ✅ 好的方式：嵌套字典
player = {
    "name": "西蒙",
    "hp": 100,
    "position": {"x": 270, "y": 607}
}
```

---

### 3. 数据结构设计模式

**列表+字典组合：**
```python
# 管理多个游戏对象
enemies = [
    {"name": "哥布林", "hp": 50, "position": {"x": 100, "y": 200}},
    {"name": "骷髅兵", "hp": 80, "position": {"x": 300, "y": 400}}
]

# 遍历并更新
for enemy in enemies:
    enemy["hp"] -= 10
    enemy["position"]["x"] += 1
```

**字典嵌套字典：**
```python
# 装备系统
equipment = {
    "weapon": {"name": "铁剑", "attack": 10},
    "armor": {"name": "皮甲", "defense": 5},
    "accessory": None
}

# 装备新武器
equipment["weapon"] = {"name": "钢剑", "attack": 20}
```

---

### 4. Pygame Zero 中的数据组织

**平台系统：**
```python
# 使用列表存储多个平台
platforms = [
    Rect(0, 680, 600, 20),      # 地面
    Rect(100, 520, 120, 20),    # 平台1
    Rect(250, 430, 120, 20),    # 平台2
    Rect(150, 360, 120, 20),    # 平台3
]

# 遍历平台进行碰撞检测
for platform in platforms:
    if player_rect.colliderect(platform):
        # 处理碰撞
        pass
```

**齿轮系统：**
```python
# 使用列表存储多个齿轮
gears = [
    {
        "x": 100, "y": 470,
        "frame": 0, "timer": 0, "speed": 0.1,
        "move_x": 100, "move_speed": 3,
        "move_direction": 1, "move_range": 120,
        "platform_idx": 1
    },
    # ... 更多齿轮
]

# 遍历并更新齿轮
for gear in gears:
    gear["timer"] += delta_time
    gear["x"] += gear["move_speed"] * gear["move_direction"]
```

---

## 三、关键知识点总结

### 基础知识与项目应用的对应关系

| 基础知识 | 在 Pygame Zero 项目中的应用 | 实际场景 |
|---------|---------------------------|----------|
| **二维列表** | 游戏地图网格 | `board[row][col]` |
| **字典嵌套** | 玩家属性组织 | `player["position"]["x"]` |
| **列表中的字典** | 多个游戏对象 | `platforms = [Rect(...), ...]` |
| **字典中的列表** | 一对多关系 | `gear["animations"] = [...]` |
| **嵌套遍历** | 批量更新游戏对象 | `for gear in gears: ...` |
| **数据结构设计** | 游戏系统架构 | 角色、物品、关卡系统 |

---

## 四、实践项目应用

### 项目：《恶魔试炼》- 数据结构应用

**项目信息：**
- **游戏类型**：垂直平台跳跃游戏
- **开发引擎**：Pygame Zero
- **数据结构应用**：嵌套字典+列表管理游戏对象

---

### 1. 玩家系统设计

**使用嵌套字典管理玩家状态：**
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
    # 动画状态（嵌套字典）
    'animation': {
        'state': 'idle',
        'frame': 1,
        'timer': 0,
        'speeds': {
            'idle': 0.2,
            'move': 0.15
        }
    },
    # 生命系统
    'hp': 100,
    'max_hp': 100,
    'invincible': 0,
}

# 访问嵌套数据
current_state = player['animation']['state']
idle_speed = player['animation']['speeds']['idle']
```

**基础知识对应：**
- 字典嵌套字典组织相关数据
- 多层访问：`player['animation']['state']`
- 字典中的字典存储配置参数

---

### 2. 齿轮系统设计

**齿轮配置（列表中的字典）：**
```python
gears = [
    {
        'x': 100, 
        'y': 470, 
        'frame': 0, 
        'timer': 0, 
        'speed': 0.1,
        'move_x': 100, 
        'move_speed': 3, 
        'move_direction': 1, 
        'move_range': 120,
        'platform_idx': 1
    },
    {
        'x': 150, 
        'y': 310, 
        'frame': 0, 
        'timer': 0, 
        'speed': 0.1,
        'move_x': 150, 
        'move_speed': 3, 
        'move_direction': 1, 
        'move_range': 120,
        'platform_idx': 3
    },
]

# 遍历更新所有齿轮
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
- 列表存储多个齿轮对象
- 字典存储单个齿轮的所有属性
- for 循环遍历更新

---

### 3. 平台系统设计

**平台列表（列表中的Rect对象）：**
```python
platforms = [
    Rect(0, 680, 600, 20),      # 地面
    Rect(100, 520, 120, 20),    # 平台1
    Rect(250, 430, 120, 20),    # 平台2
    Rect(150, 360, 120, 20),    # 平台3
    Rect(200, 200, 120, 20),    # 平台4
]

# 遍历平台进行碰撞检测
for platform in platforms:
    if player_rect.colliderect(platform):
        player['y'] = platform.top - player['height']
        player['vy'] = 0
        player['is_jumping'] = False
```

**基础知识对应：**
- 列表存储多个平台
- 遍历列表检查碰撞
- Rect对象作为列表元素

---

### 4. 相机系统设计

**相机状态（字典）：**
```python
camera = {
    'y': 0,
    'target_y': 0,
    'smooth_speed': 0.1
}

# 更新相机位置
camera['target_y'] = player['y'] - HEIGHT / 2
camera['y'] += (camera['target_y'] - camera['y']) * camera['smooth_speed']

# 绘制时应用相机偏移
draw_y = object_y - camera['y']
```

**基础知识对应：**
- 字典存储相机状态
- 平滑跟随算法
- 坐标系统转换

---

### 5. 碰撞检测系统

**使用嵌套数据管理碰撞：**
```python
# 碰撞检测配置
collision_config = {
    'player': {
        'width': 60,
        'height': 72,
        'offset': {'x': 0, 'y': 0}
    },
    'gear': {
        'width': 50,
        'height': 50,
        'damage': 20
    }
}

# 碰撞检测
def check_gear_collision(player, gear):
    player_rect = Rect(
        player['x'] + collision_config['player']['offset']['x'],
        player['y'],
        collision_config['player']['width'],
        collision_config['player']['height']
    )
    
    gear_rect = Rect(gear['x'], gear['y'], 
                     collision_config['gear']['width'],
                     collision_config['gear']['height'])
    
    if player_rect.colliderect(gear_rect):
        return collision_config['gear']['damage']
    return 0
```

**基础知识对应：**
- 嵌套字典存储配置
- 多层访问配置参数
- 函数封装碰撞逻辑

---

### 6. 项目文件结构

```
CS101/week06/
├── 恶魔试炼/
│   ├── game_v2.py              # 主游戏文件（754行）
│   │   ├── player 字典          # 玩家状态（多层嵌套）
│   │   ├── gears 列表           # 齿轮列表（字典元素）
│   │   ├── platforms 列表       # 平台列表（Rect元素）
│   │   └── camera 字典          # 相机状态
│   └── sounds/                 # 音效文件夹
│
└── 场景测试/
    └── test_full_animation.py  # 场景测试文件（524行）
```

**数据结构统计：**
- 玩家字典：18个键（3层嵌套）
- 齿轮列表：3个字典元素
- 平台列表：8个Rect元素
- 相机字典：3个键

---

## 五、学习反思

### 通过本周学习，我理解了：

1. **嵌套数据结构是组织复杂信息的关键**
   - 游戏开发中大量使用嵌套字典和列表
   - 合理的数据结构让代码更清晰、更易维护
   - 设计数据结构要考虑数据的访问模式

2. **数据结构设计的核心原则**
   - 明确存储什么信息
   - 分析信息之间的关系
   - 考虑需要进行的操作
   - 选择合适的数据结构

3. **列表+字典的强大组合**
   - 列表管理多个对象
   - 字典描述单个对象
   - 嵌套组织复杂数据
   - 这是游戏开发的标准模式

4. **从简单到复杂的渐进**
   - 简单变量 → 列表/字典 → 嵌套结构
   - 每层嵌套都增加表达能力
   - 但要避免过度复杂化

---

### 思考题

1. **数据结构选择**
   - 什么时候用列表？（有序集合、批量处理）
   - 什么时候用字典？（键值对、快速查找）
   - 什么时候用嵌套？（复杂关系、分层组织）

2. **嵌套深度**
   - 嵌套多少层合适？
   - 过深的嵌套会带来什么问题？
   - 如何平衡结构的清晰度和复杂度？

3. **数据访问效率**
   - 如何快速访问深层嵌套数据？
   - 是否需要中间变量？
   - 如何避免重复访问？

4. **数据结构扩展**
   - 如何添加新的游戏对象类型？
   - 如何修改数据结构而不破坏现有代码？
   - 如何保证数据结构的一致性？

---

## 六、下次学习预告

下周我们将学习：
- **函数（Functions）** - 组织代码的利器
- **参数和返回值** - 让函数更灵活
- **模块化编程** - 把代码分成小块
- **代码复用** - 避免重复劳动

**提前思考：**
- 现在游戏代码都在一个文件里，有什么问题？
- 如何把碰撞检测、动画更新等功能封装成函数？
- 函数和数据结构的结合会带来什么好处？

---

## 七、今日代码文件

```
CS101/
├── lessons/
│   └── week07.md              # 第7周课程：综合练习
│
├── week06/
│   ├── 恶魔试炼/
│   │   ├── game_v2.py        # 754 行（主游戏）
│   │   │   ├── player 字典    # 嵌套字典管理玩家
│   │   │   ├── gears 列表     # 列表中的字典
│   │   │   └── platforms 列表 # 列表中的Rect
│   │   └── sounds/           # 音效
│   │
│   └── 场景测试/
│       └── test_full_animation.py  # 524 行
│
└── week07/
    └── report.md             # 学习报告 ← 本文件
```

---

**总结**: 本周学习了列表与字典的嵌套，这是组织复杂数据结构的核心技能。通过分析《恶魔试炼》项目的代码，理解了嵌套数据结构在游戏中的实际应用：玩家状态用嵌套字典管理，多个齿轮用列表中的字典存储，平台用列表管理。嵌套数据结构让游戏对象的管理更清晰、更高效，是游戏开发的标准模式！

**明日目标**: 学习函数的定义和使用，将游戏代码模块化，提高代码的可维护性和复用性。

---

*"嵌套让数据有了层次，结构让复杂变得清晰，设计让代码拥有灵魂。"*
