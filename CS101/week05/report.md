# CS101 Week05 学习报告

**学习者**: Amos  
**日期**: 2026年4月25日  
**课程主题**: 列表——批量管理数据

---

## 一、本周课程核心知识点（Week 05）

### 1. 列表的创建与访问

**什么是列表？**
列表是一种可以存储**多个数据**的容器，就像一排带编号的盒子。

```python
# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
scores = [95, 87, 92, 78, 88]
mixed = [1, "hello", 3.14, True]  # 可以混合不同类型

# 空列表
empty_list = []
```

**列表结构示意图：**
```
列表 fruits:
┌─────┬─────┬─────┬─────┐
│ 苹果 │ 香蕉 │ 橙子 │ 葡萄 │
└─────┴─────┴─────┴─────┘
  [0]   [1]   [2]   [3]   ← 索引（从0开始）
```

**访问列表元素（索引）：**
```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 正向索引（从0开始）
print(fruits[0])  # 苹果
print(fruits[1])  # 香蕉
print(fruits[2])  # 橙子
print(fruits[3])  # 葡萄

# 负向索引（从末尾开始，-1是最后一个）
print(fruits[-1])  # 葡萄
print(fruits[-2])  # 橙子
```

---

### 2. 列表切片

切片可以获取列表的一部分。

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 语法：列表[起始:结束]  （包含起始，不包含结束）
print(fruits[1:3])   # ['香蕉', '橙子']
print(fruits[0:2])   # ['苹果', '香蕉']
print(fruits[:3])    # ['苹果', '香蕉', '橙子']  省略起始=从头开始
print(fruits[2:])    # ['橙子', '葡萄', '西瓜']  省略结束=到末尾
print(fruits[:])     # 整个列表的副本

# 带步长的切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8]  每隔2个取一个
print(numbers[1::2])  # [1, 3, 5, 7, 9]  从索引1开始，每隔2个
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  反转
```

---

### 3. 列表的增删改操作

**修改元素：**
```python
fruits = ["苹果", "香蕉", "橙子"]
fruits[1] = "草莓"
print(fruits)  # ['苹果', '草莓', '橙子']
```

**添加元素：**
```python
fruits = ["苹果", "香蕉"]

# append：在末尾添加一个元素
fruits.append("橙子")
print(fruits)  # ['苹果', '香蕉', '橙子']

# insert：在指定位置插入元素
fruits.insert(1, "草莓")  # 在索引1的位置插入
print(fruits)  # ['苹果', '草莓', '香蕉', '橙子']

# extend：添加多个元素
fruits.extend(["葡萄", "西瓜"])
print(fruits)  # ['苹果', '草莓', '香蕉', '橙子', '葡萄', '西瓜']
```

**删除元素：**
```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# remove：删除第一个匹配的元素
fruits.remove("香蕉")

# pop：删除并返回指定索引的元素（默认最后一个）
last = fruits.pop()
print(last)    # 葡萄

# del：删除指定索引的元素
del fruits[0]

# clear：清空列表
fruits.clear()
```

---

### 4. 列表常用方法

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 排序（修改原列表）
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # 降序
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# 反转
numbers.reverse()

# 统计元素出现次数
print(numbers.count(1))  # 2

# 查找元素索引
print(numbers.index(5))  # 返回第一个5的索引

# 获取列表长度
print(len(numbers))  # 8

# 检查元素是否在列表中
print(5 in numbers)     # True
print(10 in numbers)    # False
```

---

### 5. for 循环遍历列表

**for 循环基础：**
```python
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 遍历列表
for fruit in fruits:
    print(fruit)
```

**执行流程：**
1. 取出列表第一个元素"苹果"，赋值给 fruit
2. 执行循环体（print）
3. 取出下一个元素"香蕉"，赋值给 fruit
4. 执行循环体
5. ...直到所有元素都处理完毕

**for vs while：**
```python
fruits = ["苹果", "香蕉", "橙子"]

# for 循环（推荐遍历列表时使用）
for fruit in fruits:
    print(fruit)

# 等价的 while 循环
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

**什么时候用哪个？**
- `for`：遍历已知的集合（列表、字符串等）
- `while`：根据条件重复（次数不确定时）

---

### 6. range() 函数

`range()` 生成一个数字序列，常与 for 循环配合使用。

```python
# range(stop)：从0到stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)：从start到stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)：带步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 倒序
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

---

### 7. 遍历时获取索引

```python
fruits = ["苹果", "香蕉", "橙子"]

# 方法1：使用 range 和 len
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 方法2：使用 enumerate（推荐）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 输出：
# 0: 苹果
# 1: 香蕉
# 2: 橙子
```

---

## 二、游戏开发扩展知识

> 以下知识超出了本周学习范畴，但在实际项目中使用了基础知识

### 1. Godot 游戏引擎

**什么是 Godot？**
Godot 是一个免费、开源的现代游戏引擎，支持 2D 和 3D 游戏开发。

**为什么选择 Godot？**
- 完全免费，开源
- 轻量级（编辑器只有 ~100MB）
- 强大的 2D 引擎（像素级精确）
- 使用 GDScript（类似 Python，容易学习）
- 节点系统（清晰的项目组织）
- 跨平台导出（Windows/Mac/Linux/Android/iOS）

**Godot vs Pygame Zero：**
| 特性 | Pygame Zero | Godot |
|------|-------------|-------|
| 学习难度 | ⭐ 简单 | ⭐⭐ 中等 |
| 功能完整度 | ⭐⭐ 基础 | ⭐⭐⭐⭐⭐ 完整 |
| 可视化编辑 | ❌ 无 | ✅ 有 |
| 性能 | ⭐⭐ 一般 | ⭐⭐⭐⭐ 优秀 |
| 适合场景 | 快速原型 | 完整游戏 |

---

### 2. Godot 项目结构

**节点系统（Node）：**
Godot 使用节点树来组织游戏对象。

```
场景（Scene）
├── 玩家节点（CharacterBody2D）
│   ├── 精灵节点（AnimatedSprite2D）
│   ├── 碰撞体节点（CollisionShape2D）
│   └── 摄像机节点（Camera2D）
├── 地图节点（TileMap）
└── UI节点（Control）
```

**场景系统：**
- 每个游戏对象都是一个场景
- 场景可以互相嵌套
- 场景可以实例化多次

---

### 3. GDScript 基础

GDScript 是 Godot 的脚本语言，语法类似 Python。

```gdscript
# Godot 4.x GDScript
extends CharacterBody2D  # 继承节点类型

# 变量声明
@export var speed: float = 300.0
@export var jump_force: float = -600.0
var gravity: float = 1200.0

# 物理更新函数（类似 Pygame Zero 的 update）
func _physics_process(delta):
    # 应用重力
    velocity.y += gravity * delta
    
    # 水平移动
    var direction = Input.get_axis("move_left", "move_right")
    velocity.x = direction * speed
    
    # 跳跃
    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = jump_force
    
    # 移动角色
    move_and_slide()
```

---

### 4. 精灵表（Sprite Sheet）

**什么是精灵表？**
将多个动画帧合并到一张图片中，提高性能。

**导入流程：**
1. 从 Pixel Studio 导出精灵表
2. 在 Godot 中创建 SpriteFrames 资源
3. 配置每一帧的切割参数
4. 设置动画名称和帧率

**切割示例：**
```
精灵表：player_idle.png
┌────┬────┬────┬────┐
│ F0 │ F1 │ F2 │ F3 │  ← 4个帧
└────┴────┴────┴────┘
每个帧：64x64 像素
```

---

### 5. 动画系统

**AnimatedSprite2D 节点：**
- 管理多个动画
- 每个动画有多个帧
- 可以控制播放速度和循环

```gdscript
# 播放动画
$AnimatedSprite2D.play("idle")
$AnimatedSprite2D.play("run")
$AnimatedSprite2D.play("jump")

# 根据状态切换动画
if is_on_floor():
    if velocity.x != 0:
        $AnimatedSprite2D.play("run")
    else:
        $AnimatedSprite2D.play("idle")
else:
    $AnimatedSprite2D.play("jump")
```

---

## 三、关键知识点总结

### 基础知识与项目应用的对应关系

| 基础知识 | 在 Godot 项目中的应用 | 实际场景 |
|---------|---------------------|----------|
| **列表** | 存储多个动画帧 | SpriteFrames 的帧列表 |
| **索引** | 访问特定帧 | `frames[0]`, `frames[1]` |
| **for 循环** | 遍历所有敌人/平台 | 更新游戏对象 |
| **append** | 动态添加敌人/道具 | 关卡生成 |
| **range** | 生成敌人波次 | `for i in range(5)` |
| **枚举** | 游戏状态管理 | `enum {IDLE, RUN, JUMP}` |
| **排序** | 排行榜/得分排序 | `scores.sort()` |
| **切片** | 获取部分数据 | `top_scores = scores[:5]` |

---

## 四、实践项目应用

### 项目：《Time To Sleep》- Godot 原型

**项目信息：**
- **游戏类型**：类银河恶魔城 2D 横版动作游戏
- **开发引擎**：Godot 4.6.2
- **当前状态**：原型开发中

---

### 1. Godot 环境搭建

**安装 Godot（macOS）：**
```bash
# 使用 Homebrew 安装
brew install --cask godot

# 验证安装
which godot
godot --version
# 输出：4.6.2.stable
```

**创建项目：**
1. 打开 Godot 编辑器
2. 点击 "New Project"
3. 设置项目路径和渲染器
4. 点击 "Create & Edit"

---

### 2. 项目结构

```
godot_project/
├── project.godot              # Godot 项目配置
├── scenes/                    # 场景文件
│   ├── player.tscn           # 玩家场景
│   └── test_level.tscn       # 测试关卡
├── scripts/                   # 脚本文件
│   └── player.gd             # 玩家控制脚本
└── assets/                    # 资源文件
    ├── sprites/              # 精灵表
    │   ├── player_idle.png   # 待机动画
    │   ├── player_run.png    # 移动动画
    │   └── player_jump.png   # 跳跃动画
    └── animations/           # 动画资源
```

---

### 3. 玩家系统实现

**使用的基础知识：**

#### ✅ **列表的应用 - 动画帧管理**
```gdscript
# SpriteFrames 内部使用列表存储帧
# 每一帧都是列表中的一个元素
# 帧列表：[frame_0, frame_1, frame_2, frame_3]
```

**基础知识对应：**
- `frames[0]` → 列表索引访问
- `len(frames)` → 列表长度
- `for frame in frames` → for 循环遍历

---

#### ✅ **for 循环 - 批量处理**
```gdscript
# 遍历所有敌人（概念示例）
for enemy in enemies:
    enemy.update()
    if enemy.hp <= 0:
        enemies.remove(enemy)
```

**基础知识对应：**
- `for enemy in enemies` → for 循环遍历列表
- 列表的增删改操作

---

#### ✅ **range() - 生成敌人波次**
```gdscript
# 生成一波敌人
func spawn_wave(enemy_count):
    for i in range(enemy_count):
        var enemy = Enemy.new()
        enemy.position.x = 500 + i * 100
        add_child(enemy)
```

**基础知识对应：**
- `range(enemy_count)` → 生成数字序列
- for 循环重复执行

---

#### ✅ **枚举 - 游戏状态管理**
```gdscript
# 玩家状态（类似列表的有序集合）
enum PlayerState {
    IDLE,    # 0
    RUN,     # 1
    JUMP,    # 2
    ATTACK   # 3
}

var current_state = PlayerState.IDLE
```

**基础知识对应：**
- 枚举是特殊的有序集合
- 可以通过索引访问

---

### 4. 精灵表切割

**切割参数示例：**
```
待机动画 (player_idle.png):
- 帧数：4 帧
- 每帧大小：64x64 像素
- 总大小：256x64 像素
- 帧索引：[0, 1, 2, 3]

移动动画 (player_run.png):
- 帧数：8 帧
- 每帧大小：64x64 像素
- 总大小：512x64 像素
- 帧索引：[0, 1, 2, 3, 4, 5, 6, 7]

跳跃动画 (player_jump.png):
- 帧数：6 帧
- 每帧大小：64x64 像素
- 总大小：384x64 像素
- 帧索引：[0, 1, 2, 3, 4, 5]
```

**基础知识应用：**
- 帧索引 → 列表索引
- 帧列表 → 数组概念
- 切割参数 → 数值计算

---

### 5. 已完成的文档

| 文档 | 内容 | 行数 |
|------|------|------|
| README.md | Godot 项目说明 | 262 |
| 导入指南.md | 精灵表导入详细教程 | ~200 |
| 精灵表切割步骤详细版.md | 切割流程说明 | ~300 |
| 快速参考-精灵表切割.md | 快速查询表 | ~80 |
| 最终版-精灵表切割指南.md | 完整版指南 | ~280 |
| 精灵表精确切割参数.md | 详细参数 | ~200 |
| Pixel_Studio_导入步骤.md | Pixel Studio 教程 | ~250 |

**总计：约 1572 行文档**

---

## 五、学习反思

### 通过本周学习，我理解了：

1. **列表是数据管理的基础**
   - 游戏中的所有集合（敌人、道具、粒子）都用列表管理
   - 列表操作（增删改查）是游戏开发的核心技能

2. **for 循环是批量处理的利器**
   - 遍历所有游戏对象
   - 更新状态、检测碰撞、渲染画面
   - 比 while 循环更简洁安全

3. **从 Python 到 GDScript 的过渡**
   - 语法相似，容易学习
   - Godot 的节点系统让代码组织更清晰
   - 可视化编辑器提高开发效率

4. **游戏引擎的选择**
   - Pygame Zero：适合快速原型和学习
   - Godot：适合完整游戏开发
   - 两者都是很好的学习工具

---

### 思考题

1. **列表在游戏中的应用**
   - 敌人列表：如何管理所有敌人？
   - 道具列表：如何添加和删除道具？
   - 粒子列表：如何批量更新粒子？

2. **for 循环 vs while 循环**
   - 什么时候用 for 循环？（遍历已知集合）
   - 什么时候用 while 循环？（条件不确定）
   - 游戏主循环应该用哪个？

3. **列表方法的实际应用**
   - `append()`：添加新敌人
   - `remove()`：删除死亡敌人
   - `sort()`：排行榜排序
   - `len()`：检查剩余敌人数量

---

## 六、下次学习预告

下周我们将学习：
- **函数（Functions）** - 组织代码的利器
- **参数和返回值** - 让函数更灵活
- **模块化编程** - 把代码分成小块

**提前思考：**
- Godot 中的 `_physics_process(delta)` 是什么？（答案：函数！）
- 如果把所有代码写在一个函数里会怎样？
- 如何让代码更容易复用？

---

## 七、今日代码文件

```
CS101/
├── lessons/
│   └── week05.md              # 第5周课程：列表
│
├── Time To Sleep/
│   ├── game/                  # Pygame Zero 原型
│   │   └── game.py           # 568 行
│   │
│   └── godot_project/         # Godot 项目
│       ├── project.godot     # 项目配置
│       ├── scenes/           # 场景文件
│       │   ├── player.tscn
│       │   └── test_level.tscn
│       ├── scripts/          # 脚本文件
│       │   └── player.gd
│       ├── assets/           # 资源文件
│       │   └── sprites/      # 精灵表
│       └── *.md              # 7 个文档文件
│
└── week05/
    └── report.md             # 学习报告 ← 本文件
```

---

**总结**: 本周学习了列表和 for 循环，这是批量管理数据的核心工具。同时开始了 Godot 引擎的学习，创建了《Time To Sleep》的 Godot 项目原型。列表在游戏中无处不在：敌人列表、道具列表、动画帧列表等。通过 Godot 的可视化编辑器，可以更直观地理解游戏对象的组织方式。从 Pygame Zero 到 Godot，是从小型原型到完整游戏引擎的重要跨越！

**明日目标**: 继续学习 Godot 的节点系统，实现玩家的基本移动和动画，学习函数的定义和使用。

---

*"列表让数据井然有序，循环让处理批量完成，引擎让游戏从梦想走向现实。"*
