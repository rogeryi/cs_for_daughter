# CS101 Week04 学习报告

**学习者**: Amos  
**日期**: 2026年4月19日

---

## 今日学习内容

### 一、本周课程核心知识点（Week 04）

#### 1. while 循环

**为什么需要循环？**
- 避免重复代码（打印1-1000不需要写1000行）
- 让计算机重复执行任务

**while 循环语法：**
```python
while 条件:
    # 条件为 True 时重复执行
    # 需要缩进
```

**执行流程：**
```
检查条件 → True → 执行代码 → 回到检查条件
         → False → 结束循环
```

**关键示例：**
```python
# 倒计时
count = 5
while count > 0:
    print(count)
    count = count - 1
print("发射！🚀")

# 计算 1 到 100 的和
total = 0
num = 1
while num <= 100:
    total = total + num
    num = num + 1
print(f"1到100的和是：{total}")  # 5050
```

**重要规则：** 循环变量必须在循环体内被修改，否则会造成无限循环！

---

#### 2. 简写运算符

```python
count = 1

# 等价写法
count = count + 1
count += 1  # 简写

# 其他简写
count -= 1   # count = count - 1
count *= 2   # count = count * 2
count /= 2   # count = count / 2
```

---

#### 3. break：立即退出循环

`break` 会立即终止整个循环，跳到循环后面的代码。

```python
# 找到第一个能被7整除的数就停止
num = 1
while num <= 100:
    if num % 7 == 0:
        print(f"找到了：{num}")
        break  # 立即退出循环
    num += 1
```

**实际应用：用户登录**
```python
correct_password = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("请输入密码：")
    attempts += 1
    
    if password == correct_password:
        print("✅ 登录成功！")
        break  # 密码正确，退出循环
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ 密码错误，还剩 {remaining} 次机会")
```

---

#### 4. continue：跳过本次迭代

`continue` 跳过当前这一次循环的剩余代码，直接进入下一次循环。

```python
# 打印 1-10 中的奇数
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 如果是偶数
        continue       # 跳过，不打印
    print(num)
# 输出：1, 3, 5, 7, 9
```

**break vs continue 对比：**
```
break：    "我不玩了，直接退出"
continue： "这一次跳过，继续下一次"
```

```python
# 使用 break（遇到3就退出）
num = 0
while num < 5:
    num += 1
    if num == 3:
        break
    print(num)
# 输出：1, 2

# 使用 continue（跳过3）
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
# 输出：1, 2, 4, 5
```

---

#### 5. while-else 结构

Python 的 while 循环可以有 else 子句，当循环**正常结束**（不是被 break 终止）时执行。

```python
target = 7
num = 1

while num <= 10:
    if num == target:
        print(f"找到了 {target}！")
        break
    num += 1
else:
    # 只有循环正常结束（没有 break）才执行
    print(f"没找到 {target}")
```

---

#### 6. 用户控制的循环

```python
# 用户决定何时退出
answer = "y"
while answer == "y":
    name = input("请输入名字：")
    print(f"你好，{name}！")
    answer = input("继续吗？(y/n)：")

print("程序结束")
```

---

#### 7. 无限循环的处理

**错误示例（会无限循环）：**
```python
count = 1
while count <= 10:
    print(count)
    # 忘记更新 count 了！count 永远是 1
```

**正确示例：**
```python
count = 1
while count <= 10:
    print(count)
    count += 1  # 每次循环后 count 增加 1
```

**遇到无限循环怎么办？** 按 `Ctrl+C` 强制停止程序

---

### 二、游戏开发扩展知识

> 以下知识超出了本周学习范畴，但在实际项目中使用了基础知识

#### 1. Pygame Zero 游戏引擎

**什么是游戏引擎？**
游戏引擎是制作游戏的工具，帮我们处理图形、声音、输入等复杂工作。

**为什么选择 Pygame Zero？**
- 简单易用，适合初学者
- 使用 Python 语言
- 自动处理游戏循环
- 内置精灵系统和碰撞检测

**安装（macOS）：**
```bash
# 需要虚拟环境（PEP 668 限制）
python3 -m venv .venv
source .venv/bin/activate
pip3 install pgzero
```

**最简单的游戏：**
```python
import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill((135, 206, 235))  # 天蓝色背景

pgzrun.go()
```

---

#### 2. 游戏循环（Game Loop）

**概念：** 游戏就是一个巨大的循环，每秒执行 60 次

```python
# Pygame Zero 自动处理
def draw():
    """绘制画面 - 每秒60次"""
    screen.fill((135, 206, 235))
    # 绘制所有物体

def update():
    """更新逻辑 - 每秒60次"""
    # 更新位置、检测碰撞等
```

**循环流程：**
```
开始 → update() → draw() → update() → draw() → ...
       (逻辑更新)  (画面渲染)  (持续循环)
```

**这就是 `while True` 的实际应用！**

---

#### 3. 精灵（Sprite）

**定义：** 游戏中的角色、敌人、道具等可视元素

```python
# Pygame Zero 的 Actor 系统
player = Actor('player_image', (400, 300))
#             ↑图片名      ↑位置(x, y)

def draw():
    player.draw()  # 自动绘制
```

---

#### 4. 碰撞检测

```python
# 矩形碰撞检测
if player.colliderect(enemy):
    print("碰撞了！")
```

---

#### 5. 面向对象编程（Class）

**为什么需要类？**
- 封装：把相关数据和功能放在一起
- 复用：可以创建多个玩家/敌人
- 组织：代码更清晰

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
        
    def update(self):
        """更新玩家状态"""
        # 移动、跳跃逻辑
        
    def draw(self):
        """绘制玩家"""
        # 绘制角色
```

---

#### 6. 物理系统 - 重力和跳跃

**基础物理公式：**
```python
# 速度 = 速度 + 加速度
velocity_y += gravity

# 位置 = 位置 + 速度
y += velocity_y
```

**跳跃实现：**
```python
# 起跳
if keyboard.up and on_ground:
    velocity_y = -11  # 向上的初速度

# 重力（非对称）
if velocity_y < 0:  # 上升
    gravity = 0.7
else:               # 下落
    gravity = 1.2

velocity_y += gravity
y += velocity_y

# 地面碰撞
if y >= GROUND_Y - height:
    y = GROUND_Y - height
    velocity_y = 0
    on_ground = True
```

---

#### 7. AI 设计 - 敌人巡逻

```python
class Enemy:
    def update(self):
        # 移动
        self.x += self.direction * self.speed
        
        # 到达边界转身（if 判断）
        if self.x > self.platform_right:
            self.direction = -1
        elif self.x < self.platform_left:
            self.direction = 1
```

---

#### 8. 粒子系统

**什么是粒子？**
小的视觉元素，用于特效（爆炸、跳跃、魔法等）

```python
class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
```

---

#### 9. 中文字体支持

**问题：** Pygame Zero 默认字体不支持中文

**解决方案：**
```python
import pygame

# 加载系统中文字体
font = pygame.font.Font('/System/Library/Fonts/PingFang.ttc', 20)

# 自定义绘制函数
def draw_chinese_text(text, pos, fontsize=20, color=(255, 255, 255)):
    if CHINESE_FONT:
        font = pygame.font.Font(CHINESE_FONT, fontsize)
        text_surface = font.render(text, True, color)
        screen.surface.blit(text_surface, pos)
```

---

### 三、关键知识点总结

| 基础知识 | 游戏中的实际应用 |
|---------|-----------------|
| `while True` | 游戏主循环 |
| `break` | 找到平台后退出、Boss死亡 |
| `continue` | 跳过死亡粒子更新 |
| `if-elif-else` | Boss阶段切换、武器选择 |
| `for` 循环 | 遍历敌人、粒子、平台 |
| `and/or` | 碰撞检测、条件判断 |
| 变量更新 `+=` | 位置移动、血量变化 |
| 比较运算符 | 边界判断、血量检查 |

---

### 四、实践项目应用

### 1. 游戏引擎初探 - Pygame Zero

**核心概念**: 游戏引擎是制作游戏的工具，帮我们处理图形、声音、输入等复杂工作

#### 为什么选择 Pygame Zero？

| 特性 | 说明 |
|------|------|
| 简单易用 | 比 Pygame 更简洁，适合初学者 |
| Python 编写 | 使用熟悉的 Python 语言 |
| 2D 游戏 | 专注于 2D 游戏开发 |
| 内置功能 | 自动处理游戏循环、精灵、碰撞等 |

#### 安装和使用

```bash
# macOS 需要虚拟环境（PEP 668 限制）
python3 -m venv .venv
source .venv/bin/activate
pip3 install pgzero
```

```python
# 最简单的 Pygame Zero 游戏
import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill((135, 206, 235))  # 天蓝色背景

pgzrun.go()
```

---

### 2. 游戏开发基础概念

#### 游戏循环 (Game Loop)

```python
# Pygame Zero 自动处理游戏循环
def draw():
    """绘制画面 - 每秒60次"""
    screen.fill((135, 206, 235))
    # 绘制所有物体

def update():
    """更新逻辑 - 每秒60次"""
    # 更新位置、检测碰撞等
```

**循环流程**:
```
开始 → update() → draw() → update() → draw() → ...
       (逻辑更新)  (画面渲染)  (持续循环)
```

#### 精灵 (Sprite)

**定义**: 游戏中的角色、敌人、道具等可视元素

```python
# Pygame Zero 的 Actor 系统
player = Actor('player_image', (400, 300))
#             ↑图片名      ↑位置(x, y)

def draw():
    player.draw()  # 自动绘制
```

**精灵的属性**:
- `x`, `y` - 位置
- `width`, `height` - 大小
- `angle` - 旋转角度
- 自定义属性 - 可以添加任何属性

---

### 3. 碰撞检测

```python
# 矩形碰撞检测
if player.colliderect(enemy):
    print("碰撞了！")

# 距离检测
import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
if distance < 50:
    print("够近了！")
```

---

### 4. 键盘和鼠标输入

```python
# 持续按键检测
def update():
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

# 按键事件（只触发一次）
def on_key_down(key):
    if key == keys.SPACE:
        player.jump()
    if key == keys.X:
        player.attack()
```

---

### 5. 面向对象编程实战

#### 玩家类设计

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 50
        self.hp = 100
        self.max_hp = 100
        self.speed = 5
        
    def update(self):
        """更新玩家状态"""
        # 移动、跳跃、战斗逻辑
        
    def draw(self):
        """绘制玩家"""
        # 绘制角色、血条等
```

**类的优势**:
- ✅ 封装 - 把所有相关数据和功能放在一起
- ✅ 复用 - 可以创建多个玩家/敌人
- ✅ 组织 - 代码更清晰

---

### 6. 物理系统 - 重力和跳跃

#### 基础物理公式

```python
# 速度 = 速度 + 加速度
velocity_y += gravity

# 位置 = 位置 + 速度
y += velocity_y
```

#### 跳跃实现

```python
# 起跳
if keyboard.up and on_ground:
    velocity_y = -11  # 向上的初速度

# 重力
if velocity_y < 0:  # 上升中
    gravity = 0.7
else:               # 下落中
    gravity = 1.2

velocity_y += gravity
y += velocity_y

# 地面碰撞
if y >= GROUND_Y - height:
    y = GROUND_Y - height
    velocity_y = 0
    on_ground = True
```

#### Coyote Time（土狼时间）

```python
# 离开平台后仍可短暂跳跃（更友好）
if on_ground:
    coyote_timer = 8  # 8帧缓冲
else:
    coyote_timer -= 1

if keyboard.up and (on_ground or coyote_timer > 0):
    velocity_y = -11
```

---

### 7. 平台碰撞系统

```python
# 检测是否在平台上方
for platform in platforms:
    if (player.x + width > platform.x and 
        player.x < platform.x + platform.width and
        player.y + height >= platform.y and 
        velocity_y >= 0):
        
        player.y = platform.y - height
        velocity_y = 0
        on_ground = True
```

**关键逻辑**:
1. 水平方向重叠
2. 垂直方向接触
3. 正在下落（velocity_y >= 0）

---

### 8. AI 设计 - 敌人巡逻

#### 简单巡逻

```python
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.start_x = x
        self.patrol_distance = 100
        self.direction = 1
        self.speed = 2
    
    def update(self):
        # 移动
        self.x += self.direction * self.speed
        
        # 到达边界转身
        if self.x > self.start_x + self.patrol_distance:
            self.direction = -1
        elif self.x < self.start_x - self.patrol_distance:
            self.direction = 1
```

#### 智能平台巡逻

```python
# 检测所在平台
for plat in platforms:
    if 敌人在平台上:
        # 设置巡逻边界为平台边缘
        platform_left = plat.x + 5
        platform_right = plat.x + plat.width - 宽度 - 5
        
        # 使用平台边界巡逻
        if self.x > platform_right:
            self.direction = -1
        elif self.x < platform_left:
            self.direction = 1
```

---

### 9. 粒子系统

#### 粒子类

```python
class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime, size=3):
        self.x = x
        self.y = y
        self.vx = vx  # x方向速度
        self.vy = vy  # y方向速度
        self.color = color
        self.lifetime = lifetime  # 存活帧数
        self.max_lifetime = lifetime
        self.size = size
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # 轻微重力
        self.lifetime -= 1
    
    def draw(self, camera_x):
        alpha = self.lifetime / self.max_lifetime
        screen.draw.filled_circle(
            (self.x - camera_x, self.y),
            self.size * alpha,
            color
        )
```

#### 创建二段跳特效

```python
def create_double_jump_effect(x, y):
    # 环形粒子
    for i in range(12):
        angle = (i / 12) * 3.14159 * 2
        vx = math.cos(angle) * 3
        vy = math.sin(angle) * 3
        particles.append(Particle(x, y, vx, vy, 颜色, 20))
```

---

### 10. 中文字体支持

#### 问题
Pygame Zero 默认字体不支持中文，显示为方框 `[]`

#### 解决方案

```python
import os
import platform

def get_chinese_font():
    """根据操作系统选择字体"""
    if platform.system() == 'Darwin':  # macOS
        font_paths = [
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/STHeiti Light.ttc',
        ]
    elif platform.system() == 'Windows':
        font_paths = ['C:/Windows/Fonts/msyh.ttc']
    
    for path in font_paths:
        if os.path.exists(path):
            return path
    return None

# 自定义绘制函数
def draw_chinese_text(text, pos, fontsize=20, color=(255, 255, 255)):
    if CHINESE_FONT:
        font = pygame.font.Font(CHINESE_FONT, fontsize)
        text_surface = font.render(text, True, color)
        screen.surface.blit(text_surface, pos)
```

---

## 实践项目

### 项目1: 猜数字游戏 (guess_number.py)

**功能**:
- ✅ 随机生成 1-100 的数字
- ✅ 玩家猜测
- ✅ 提示"太大"或"太小"
- ✅ 记录猜测次数
- ✅ 最优策略教学（二分查找）

**运行**:
```bash
python3 /Users/roger/cs/CS101/week04/guess_number.py
```

---

### 项目2: 接苹果游戏 (catch_apple.py)

**功能**:
- ✅ Pygame Zero 入门示例
- ✅ 鼠标控制篮子移动
- ✅ 苹果从上方掉落
- ✅ 碰撞检测
- ✅ 分数系统
- ✅ 难度递增

**核心代码**:
```python
basket = Actor('basket', (300, 370))
apple = Actor('apple', (300, 0))

def update():
    basket.x = mouse_x
    apple.y += apple.speed
    
    if basket.colliderect(apple):
        score += 1
```

**运行**:
```bash
python3 /Users/roger/cs/CS101/week04/catch_apple.py
```

---

### 项目3: 像素勇士 - 武器与Boss (horizontal_game_with_boss.py)

**完整功能**:

#### 玩家系统
- ✅ 左右移动
- ✅ 跳跃（物理重力）
- ✅ 二段跳（粒子特效）
- ✅ 快速下落
- ✅ 3种武器切换

#### 武器系统
| 武器 | 伤害 | 范围 | 特点 |
|------|------|------|------|
| 🔵 剑 | 20 | 60 | 平衡型 |
| 🟠 斧 | 35 | 50 | 高伤害 |
| 🟢 矛 | 15 | 90 | 远距离 |

#### 敌人系统
- ✅ 3种敌人类型（普通/快速/坦克）
- ✅ 智能巡逻（不会掉落平台）
- ✅ 血条显示
- ✅ 受击击退

#### Boss系统
- ✅ 三阶段战斗
- ✅ 多种攻击模式
- ✅ AI状态机

#### 关卡设计
- ✅ 6个悬浮平台
- ✅ 横向卷轴相机
- ✅ 任务提示系统

#### 特效系统
- ✅ 二段跳粒子特效
- ✅ 受击闪烁
- ✅ 攻击范围显示

**运行**:
```bash
python3 /Users/roger/cs/CS101/week04/horizontal_game_with_boss.py
```

**操作说明**:
```
← → : 移动
↑   : 跳跃（空中再按=二段跳）
↓   : 快速下落
X   : 攻击
1/2/3 : 切换武器
```

---

## 新学英文词汇

| 中文 | 英文 | 缩写/简称 |
|------|------|-----------|
| 游戏引擎 | Game Engine | Engine |
| 精灵 | Sprite | - |
| 碰撞 | Collision | - |
| 物理 | Physics | - |
| 重力 | Gravity | g |
| 速度 | Velocity | v |
| 加速度 | Acceleration | a |
| 粒子 | Particle | - |
| 渲染 | Render | - |
| 帧率 | Frame Rate | FPS |
| 循环 | Loop | - |
| 事件 | Event | - |
| 状态机 | State Machine | FSM |
| 人工智能 | Artificial Intelligence | AI |

---

## 重要发现

### 1. macOS 的 PEP 668 限制

**问题**: Python 3.13+ 不允许直接安装第三方包

```bash
# ❌ 错误
pip3 install pgzero
# error: externally-managed-environment

# ✅ 正确
python3 -m venv .venv
source .venv/bin/activate
pip3 install pgzero
```

---

### 2. Pygame Zero 按键常量

**常见错误**:
```python
# ❌ 错误
if key == keys.KEY_1:  # AttributeError

# ✅ 正确
if key == keys.K_1:
```

---

### 3. draw 函数中的全局变量

**问题**: 修改全局变量需要声明

```python
# ❌ 错误
def draw():
    score += 1  # UnboundLocalError

# ✅ 正确
def draw():
    global score
    score += 1
```

---

### 4. 物理参数调优

**跳跃手感的关键参数**:

| 参数 | 值 | 影响 |
|------|-----|------|
| 跳跃力 | -11 | 起跳高度 |
| 上升重力 | 0.7 | 上升速度 |
| 下落重力 | 1.2 | 下落速度 |
| Coyote时间 | 8帧 | 跳跃宽容度 |
| 最大速度 | 20 | 下落上限 |

**经验**: 
- 上升重力 < 下落重力 = 更自然
- Coyote Time = 6-10帧最佳
- 需要反复测试调整

---

### 5. 平台碰撞的边界问题

**Bug**: 平台上的敌人会掉下去

**原因**: 没有检测平台边界

**解决**: 
```python
# 记录所在平台
if 敌人在平台上:
    platform_left = 平台左边界
    platform_right = 平台右边界
    
    # 使用平台边界巡逻
    if x > platform_right:
        direction = -1
```

---

## 游戏开发设计总结

### 已完成的设计决策

✅ **非对称重力** - 上升慢、下落快，更真实  
✅ **Coyote Time** - 提升跳跃手感  
✅ **按键去抖** - 防止连续触发  
✅ **二段跳特效** - 视觉反馈  
✅ **平台巡逻边界** - 敌人智能行为  
✅ **中文字体加载** - 跨平台兼容  

### 待完善的设计

🔲 **像素美术** - 替换色块为精美素材  
🔲 **音效系统** - BGM + 音效  
🔲 **多关卡** - 不同主题的场景  
🔲 **更多敌人** - 远程、飞行、精英  
🔲 **角色成长** - 经验值、技能树  
🔲 **存档系统** - 保存进度  

---

## 下次学习预告

- 学习绘制像素美术（Aseprite 或 Pyxel Edit）
- 添加音效系统（背景音乐 + 游戏音效）
- 设计第二关卡（不同主题）
- 学习使用 Git 管理游戏项目
- 优化代码架构（模块化、数据驱动）

---

## 今日代码文件

```
CS101/
├── week04/
│   ├── guess_number.py              # 猜数字游戏
│   ├── catch_apple.py               # 接苹果游戏
│   ├── horizontal_game_with_boss.py # 像素勇士（主项目）
│   ├── game_development_report.md   # 游戏开发报告
│   ├── images/                      # 游戏素材
│   │   ├── player.png
│   │   ├── enemy.png
│   │   ├── basket.png
│   │   └── apple.png
│   └── report.md                    # 学习报告 ← 本文件
│
└── .venv/                           # 虚拟环境
    └── lib/
        └── python3.13/
            └── site-packages/
                └── pgzero/          # Pygame Zero
```

---

## 代码统计

| 项目 | 数量 |
|------|------|
| **总代码行数** | ~1200行 |
| **类数量** | 5个 |
| **函数数量** | ~30个 |
| **游戏系统** | 8个核心系统 |

---

**总结**: 本周学习了 while 循环、break、continue 等基础知识，并通过 Pygame Zero 从零开始制作了一个完整的横版动作游戏。在游戏开发中，反复使用了循环（游戏循环、敌人巡逻、粒子更新）、条件判断（Boss阶段、碰撞检测）、break（找到平台后退出）等基础知识，深刻理解了这些概念在实际项目中的应用。这是从命令行游戏到图形游戏的重要跨越！

**明日目标**: 继续优化游戏手感，学习像素美术制作，为游戏添加精美的视觉素材和音效。

---

## 基础知识在本周项目中的运用

### 1. while 循环 → 游戏主循环

**学习时：**
```python
while count <= 10:
    print(count)
    count += 1
```

**游戏中：**
```python
# Pygame Zero 的游戏循环（本质就是 while True）
def update():
    player.update()      # 每秒执行60次
    for enemy in enemies:
        enemy.update()
```

**理解深化：** 游戏循环就是一个无限循环，持续更新和绘制！

---

### 2. break → 优化性能

**学习时：**
```python
while num <= 100:
    if num % 7 == 0:
        print(f"找到了：{num}")
        break  # 找到就退出
```

**游戏中：**
```python
# 碰撞检测
for plat in platforms:
    if 玩家在平台上:
        玩家站在平台上()
        break  # 找到一个就够了，退出循环
```

**理解深化：** break 不仅用于退出循环，还能优化性能！

---

### 3. if-elif-else → Boss 多阶段

**学习时：**
```python
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("及格")
```

**游戏中：**
```python
# Boss 阶段切换
if self.hp < self.max_hp * 0.3:
    self.phase = 3  # 狂暴
elif self.hp < self.max_hp * 0.6:
    self.phase = 2  # 增强
else:
    self.phase = 1  # 普通
```

**理解深化：** 多分支判断可以控制游戏状态！

---

### 4. for 循环 → 批量处理

**学习时：**
```python
for stat in stat_names:
    print(f"{stat}: {value}")
```

**游戏中：**
```python
# 更新所有敌人
for enemy in enemies:
    enemy.update()

# 更新所有粒子
for p in particles:
    p.update()
```

**理解深化：** 游戏需要处理大量对象，for 循环是必备工具！

---

### 5. and/or → 复杂条件

**学习时：**
```python
if age >= 18 and has_ticket:
    print("可以入场")
```

**游戏中：**
```python
# 平台碰撞检测
if (x + width > plat_x and 
    x < plat_x + plat_w and
    y + height >= plat_y and 
    velocity_y >= 0):
    # 站在平台上
```

**理解深化：** 游戏逻辑往往需要多个条件同时判断！

---

### 6. 变量更新 → 游戏物理

**学习时：**
```python
count = count + 1  # 或 count += 1
```

**游戏中：**
```python
# 位置更新
self.x += self.speed      # 移动
self.velocity_y += gravity # 重力
self.y += self.velocity_y  # 位置变化
```

**理解深化：** 游戏中的运动，本质就是变量不断更新！

---

*"从循环打印数字，到循环更新游戏；从条件判断成绩，到条件控制Boss阶段。基础知识是一样的，只是应用更丰富了。"*

---

## 实践项目：从循环到游戏开发

### 项目引导

本周我们学习了 **while 循环**、**break** 和 **continue**。在下面的游戏项目中，你会看到这些基础知识如何在实际游戏开发中被大量使用。

**学习目标：**
- 理解循环在游戏中的应用（游戏循环）
- 看到 break 在游戏中的实际使用（退出条件）
- 理解 continue 的作用（跳过某些逻辑）
- 体验从简单循环到复杂项目的演变

---

### 实践项目 1：猜数字游戏进阶版

**基础知识运用：**
- ✅ `while True` - 游戏主循环
- ✅ `break` - 猜对时退出循环
- ✅ `if-elif-else` - 判断大小
- ✅ `input()` - 用户输入

**运行：**
```bash
python3 /Users/roger/cs/CS101/week04/guess_number.py
```

**代码中的基础知识：**
```python
# while True 创建无限循环
while True:
    guess = int(input("请输入你的猜测："))
    guess_count += 1
    
    if guess == secret:        # if 条件判断
        print("🎉 恭喜你猜对了！")
        break                   # break 退出循环
    elif guess < secret:       # elif 多分支
        print("📈 太小了！")
    else:                      # else 默认分支
        print("📉 太大了！")
```

---

### 实践项目 2：像素勇士 - 横版动作游戏

这是一个完整的游戏项目，使用了本周学习的基础知识，还引入了游戏开发的高级概念。

**运行：**
```bash
python3 /Users/roger/cs/CS101/week04/horizontal_game_with_boss.py
```

#### 🎮 游戏中的循环应用

**1. 游戏主循环（while 循环的终极应用）**

```python
# Pygame Zero 自动处理的游戏循环
def update():
    """这个函数每秒被调用60次，就是一个 while True 循环"""
    player.update()      # 更新玩家
    
    for enemy in enemies:  # for 循环遍历敌人
        enemy.update()
    
    if boss:
        boss.update()
```

**基础知识的实际应用：**
- `while True` → 游戏循环持续运行
- `for enemy in enemies` → 遍历列表处理每个敌人
- `if boss:` → 条件判断

---

**2. 敌人巡逻（while 循环 + 边界判断）**

```python
class Enemy:
    def update(self):
        # 巡逻移动
        self.x += self.direction * self.speed
        
        # 到达边界转身（if 判断）
        if self.x > self.platform_right:
            self.direction = -1  # 向左走
        elif self.x < self.platform_left:
            self.direction = 1   # 向右走
```

**基础知识的实际应用：**
- `if-elif` → 判断巡逻边界
- `while` 循环 → 每次 update() 都在重复执行
- 变量更新 → `self.x += speed` 就是循环变量更新

---

**3. Boss 多阶段战斗（break 的实际应用）**

```python
def update(self):
    # 根据血量切换阶段
    if self.hp < self.max_hp * 0.3:
        self.phase = 3
        self.is_angry = True
    elif self.hp < self.max_hp * 0.6:
        self.phase = 2
    
    # Boss 死亡检查（break 的变体）
    if not self.alive:
        return  # 相当于 continue，跳过后续代码
```

**基础知识的实际应用：**
- `if-elif-else` → 多阶段判断
- `return` → 类似 break，提前退出函数
- 循环控制 → 控制游戏流程

---

**4. 粒子系统（for 循环 + continue）**

```python
def update_particles():
    global particles
    
    # 更新所有粒子
    for p in particles:
        p.update()
    
    # 移除死亡粒子（列表过滤）
    particles = [p for p in particles if p.lifetime > 0]
```

**基础知识的实际应用：**
- `for p in particles` → 遍历粒子列表
- `if p.lifetime > 0` → 条件过滤
- 列表推导式 → for + if 的组合应用

---

**5. 平台碰撞检测（循环 + 多重条件）**

```python
# 玩家平台碰撞
for plat in platforms:
    plat_x, plat_y, plat_w, plat_h = plat
    
    # 多重条件判断（and 运算符）
    if (self.x + self.width > plat_x and 
        self.x < plat_x + plat_w and
        self.y + self.height >= plat_y and 
        self.velocity_y >= 0):
        
        self.y = plat_y - self.height
        self.velocity_y = 0
        self.on_ground = True
        break  # 找到一个平台就够了，退出循环
```

**基础知识的实际应用：**
- `for` 循环 → 遍历所有平台
- `and` 运算符 → 多个条件同时满足
- `break` → 找到后退出循环（优化性能）

---

### 知识映射表

| 基础知识 | 在游戏中的实际应用 | 代码位置 |
|---------|-------------------|----------|
| `while True` | 游戏主循环 | `update()` 函数 |
| `break` | 找到平台后退出、Boss死亡 | 碰撞检测、Boss更新 |
| `if-elif-else` | Boss阶段切换、武器选择 | Boss类、玩家类 |
| `for` 循环 | 遍历敌人、粒子、平台 | 多处 |
| `and/or` | 碰撞检测、条件判断 | 碰撞系统 |
| 变量更新 | 位置移动、血量变化 | 所有 `update()` |
| 比较运算符 | 边界判断、血量检查 | 多处 |

---

### 学习反思

通过这个游戏项目，你可以看到：

1. **循环无处不在** - 游戏本质上就是一个巨大的循环
2. **条件判断是核心** - 每个游戏逻辑都需要判断
3. **break 和 continue 很重要** - 控制流程的关键工具
4. **基础知识是基石** - 即使是最复杂的游戏，也是由这些简单概念组成

**思考题：**
- 游戏循环和你学的 `while True` 有什么相似之处？
- 敌人巡逻的逻辑中，哪里用到了循环变量的更新？
- Boss 的阶段切换，用了哪种条件语句？

---

*"循环让计算机重复劳动，条件让程序智能决策。这就是编程的核心力量。"*

---

*"从文字到图像，从逻辑到艺术，游戏开发是技术与创意的完美结合。"*
