# 第 11 周学习报告：类、对象与 Verity 养成游戏

## 一、本周课程核心知识点

### 1. 类与对象

- **类（class）**是创建对象的模板，规定对象有哪些属性和方法。
- **对象（object）**是根据类创建出来的具体实例。
- 同一个类可以创建多个对象，每个对象拥有自己的属性值。

```python
class Cat:
    def __init__(self, name):
        self.name = name

cat1 = Cat("咪咪")
cat2 = Cat("小黑")
```

这里的 `Cat` 是类，`cat1` 和 `cat2` 是两个不同的对象。

### 2. `__init__` 初始化方法

创建对象时，Python 会自动调用 `__init__`。它通常用来设置对象的初始属性。

```python
class Verity:
    def __init__(self, name):
        self.name = name
        self.mood = 70
        self.fullness = 60
```

执行下面的代码时：

```python
verity = Verity("Verity")
```

Python 创建一个 `Verity` 对象，并把 `"Verity"` 传给 `name` 参数。

### 3. `self` 代表当前对象

在类的方法中，`self` 代表正在使用这个方法的对象。

```python
def feed(self):
    self.mood += 8
    self.fullness += 25
```

调用：

```python
verity.feed()
```

可以理解为让 `verity` 这个对象执行 `feed` 方法，所以修改的是这个对象自己的 `mood` 和 `fullness`。

调用方法时不需要手动传入 `self`，Python 会自动完成参数绑定。

### 4. 属性与方法

**属性**保存对象的状态：

```python
verity.mood
verity.fullness
verity.outfit
verity.state
```

**方法**表示对象能够执行的行为：

```python
verity.feed()
verity.play()
verity.talk()
verity.apologize()
```

使用点号 `.` 可以访问对象的属性或调用对象的方法。

### 5. 对象可以在方法调用后改变状态

对象不是一组固定不变的数据。调用方法后，它的属性可以发生变化。

```python
verity = Verity("Verity")
print(verity.mood)  # 70

verity.play()
print(verity.mood)  # 85
```

这说明 `play()` 方法产生了副作用：它修改了对象内部保存的状态。

### 6. 返回值表示行为是否成功

Verity 的互动方法会返回布尔值：

```python
if not self._can_do_daily_action():
    return False

return self._finish_daily_action("谢谢！这份点心刚刚好。")
```

- 返回 `True`：互动成功执行。
- 返回 `False`：当前状态不允许执行这个互动。

例如，Verity 变成怪物后，普通的喂食和玩耍会被拒绝。

### 7. 控制属性范围

五项属性都必须保持在 `0` 到 `100`：

```python
self.mood = max(0, min(100, self.mood))
```

计算顺序：

1. `min(100, self.mood)` 防止数值超过 `100`。
2. `max(0, ...)` 防止数值低于 `0`。

---

## 二、游戏开发扩展知识

> 以下内容超出了“类与对象”的基础范围，但它们展示了基础知识如何组成一个完整游戏。

### 1. 状态机

Verity 有三个状态：

```python
STATE_NORMAL = "normal"
STATE_MONSTER = "monster"
STATE_RECOVERING = "recovering"
```

状态转换过程：

```text
normal
  -> 心情降到 0
monster
  -> 道歉或示弱
recovering
  -> 经过 1 秒
normal（心情恢复到 30）
```

状态机让程序能够根据当前状态决定：

- Verity 应该显示什么外观。
- 哪些按钮可以使用。
- 点击按钮后应该发生什么。

### 2. 游戏逻辑与图形界面分离

项目把代码分成两个主要文件：

- `verity.py`：管理属性、互动、对白和状态转换。
- `verity_game.py`：管理绘图、按钮和鼠标输入。

这样做的好处是：测试 Verity 的逻辑时不需要打开游戏窗口。

### 3. Pygame Zero 回调函数

图形界面使用三个重要回调：

```python
def draw():
    ...

def update(dt):
    ...

def on_mouse_down(pos):
    ...
```

- `draw()`：反复绘制房间、角色、状态栏和按钮。
- `update(dt)`：根据经过的时间更新恢复过程。
- `on_mouse_down(pos)`：处理玩家点击的位置。

`dt` 表示距离上一帧经过了多少秒。程序不断累加它，达到 `1.0` 秒后完成恢复。

### 4. 数据结构的运用

装扮顺序使用元组：

```python
OUTFITS = ("无", "蝴蝶结", "帽子", "眼镜")
```

装扮与对白的对应关系使用字典：

```python
messages = {
    "蝴蝶结": "蝴蝶结适合我吗？",
    "帽子": "这顶帽子让我像个冒险家！",
    "眼镜": "戴上眼镜，我看起来很聪明吧？",
    "无": "今天先做原来的自己。",
}
```

按钮数据也保存了方法名，界面使用 `getattr()` 找到并调用相应方法：

```python
method = getattr(verity, method_name)
method()
```

### 5. 自动化测试与 TDD

项目使用 `unittest` 编写了 16 个测试。开发过程采用：

```text
先写测试 -> 观察测试失败 -> 编写最小实现 -> 再次运行并通过
```

测试覆盖：

- 初始属性。
- 六种日常互动。
- 数值范围。
- 四种装扮循环。
- 怪物状态。
- 道歉与示弱。
- 一秒恢复。
- 心情对应的嘴型方向。
- 状态栏中的角色名字。

---

## 三、关键知识点总结

| 基础知识 | 在 Verity 项目中的应用 | 代码位置 |
|---|---|---|
| `class` | 定义 Verity 角色模板 | `verity.py` 的 `class Verity` |
| 对象 | 创建唯一的游戏角色 | `verity = Verity("Verity")` |
| `__init__` | 设置名字、五项属性、装扮和初始状态 | `Verity.__init__()` |
| `self` | 访问当前 Verity 对象的数据 | 所有实例方法 |
| 属性 | 保存心情、饱食、清洁、体力和亲密度 | `self.mood` 等 |
| 方法 | 实现喂食、玩耍、聊天等行为 | `feed()`、`play()` 等 |
| 条件判断 | 根据状态允许或拒绝互动 | `_can_do_daily_action()` |
| 函数返回值 | 告诉调用者互动是否成功 | `True` / `False` |
| 列表式数据 | 保存按钮标签、方法名和区域 | `DAILY_BUTTONS` |
| 元组 | 保存固定的装扮顺序 | `OUTFITS` |
| 字典 | 根据装扮查找对应对白 | `messages` |
| 状态机 | 管理正常、怪物和恢复状态 | `_check_state()`、`update_recovery()` |
| 模块 | 分离游戏逻辑与图形界面 | `verity.py` / `verity_game.py` |
| 测试 | 验证对象行为和边界情况 | `test_verity.py` |

---

## 四、实践项目：Verity 互动养成游戏

### 1. 项目功能

Verity 是一个黄色 Emoji 风格小球，可以进行以下互动：

| 行为 | 心情变化 | 其他变化 |
|---|---:|---|
| 喂食 | `+8` | 饱食 `+25`、清洁 `-2`、体力 `+2`、亲密 `+3` |
| 玩耍 | `+15` | 饱食 `-8`、清洁 `-5`、体力 `-15`、亲密 `+10` |
| 洗澡 | `+5` | 清洁 `+30`、体力 `-3`、亲密 `+6` |
| 聊天 | `+10` | 体力 `-1`、亲密 `+12` |
| 装扮 | `+12` | 体力 `-4`、亲密 `+8` |
| 暂时离开 | `-25` | 亲密 `-10` |

装扮按照下面的顺序循环：

```text
无 -> 蝴蝶结 -> 帽子 -> 眼镜 -> 无
```

连续三次选择“暂时离开”后，心情从 `70` 降到 `0`，Verity 会变成紫色怪物。此时只能选择：

- 道歉。
- 示弱。

选择其中一个后，Verity 经过一秒恢复为黄色小球，心情变为 `30`。

### 2. 互动对白

对白是对象状态的一部分，保存在 `verity.message` 中。例如：

```python
def talk(self):
    if not self._can_do_daily_action():
        return False

    self.mood += 10
    self.energy -= 1
    self.bond += 12
    return self._finish_daily_action(
        "我喜欢听你说话，也喜欢你听我说。"
    )
```

图形界面只负责显示：

```python
draw_text(verity.message, bubble.center, 18)
```

这体现了“数据与显示分离”的设计。

### 3. 项目文件

| 文件 | 作用 |
|---|---|
| `verity.py` | Verity 类、属性、互动、对白和状态机 |
| `verity_game.py` | Pygame Zero 图形界面和鼠标输入 |
| `test_verity.py` | 16 个自动化测试 |
| `report.md` | 本周学习总结与项目复盘 |

### 4. 运行游戏

在 PowerShell 中执行：

```powershell
cd D:\Work\cs\CS101\week11
python -X utf8 -m pgzero verity_game.py
```

如果在 `codex/verity-game` 工作树中运行，则先进入对应的 `CS101/week11` 目录。

### 5. 运行测试

```powershell
python -B -m unittest discover -s . -p "test*.py" -v
```

预期结果：

```text
Ran 16 tests
OK
```

---

## 五、学习反思与思考题

### 学习反思

1. **类把数据和行为组织在一起。**  
   Verity 的属性和互动方法都属于同一个对象，比使用许多分散的全局变量更容易理解。

2. **对象会保存变化后的状态。**  
   每次互动后，下一次操作都会基于当前属性继续计算。

3. **基础语法可以组成完整游戏。**  
   类、函数、条件判断、元组、字典和模块组合起来，就能完成角色互动、装扮和状态转换。

4. **测试不仅能找错误，也能明确需求。**  
   测试发现了高心情和低心情嘴型方向相反的问题，并防止它以后再次出现。

5. **“能运行”也需要验证运行环境。**  
   这台 Windows 电脑需要用 UTF-8 模式启动 PgZero，最终把真实可用的命令写回了课程文件。

### 思考题

1. 如果创建两个 `Verity` 对象，它们的心情值会互相影响吗？为什么？
2. 为什么 `feed()` 修改的是 `self.mood`，而不是一个普通的局部变量 `mood`？
3. 为什么怪物状态下应该让普通互动返回 `False`？
4. 如果希望 Verity 每分钟自动变饿，应该把变化放在模型还是绘图函数中？
5. 怎样增加第四种状态，例如“睡觉中”，并限制可用按钮？

---

## 六、Agentic 协作复盘

### 1. 我的需求

- 创建一个名为 Verity 的黄色小球角色。
- 支持喂食、玩耍、洗澡、聊天、装扮和暂时离开。
- 所有行为都影响心情。
- 心情归零时变成怪物。
- 道歉或示弱后经过一秒恢复。
- 使用 Pygame Zero 做成可以点击互动的小游戏。

### 2. AI/Agent 给出的结果

- 先整理设计文档和实施计划。
- 把项目拆分为对象基础、日常互动、状态机、图形界面和最终验证五个任务。
- 分别生成模型代码、界面代码、测试和课程运行说明。
- 每个任务都经过独立的规格与代码质量审查。

### 3. 我的审查

重点检查了：

- 属性变化是否与设计一致。
- 每段互动对白是否符合 Verity 的性格。
- 怪物状态是否只显示道歉和示弱。
- 一秒后是否恢复为正常状态和心情 `30`。
- 装扮是否按照固定顺序循环。
- 中文文字和按钮是否完整显示。

### 4. 调试与验证

这次协作发现并修正了两个有代表性的问题：

1. 高心情与低心情的嘴型方向写反了。  
   通过真实 Pygame 画面重放发现问题，再增加回归测试并修正圆弧角度。

2. 原来的 `pgzrun verity_game.py` 在当前电脑上不能直接运行。  
   验证后改成：

   ```powershell
   python -X utf8 -m pgzero verity_game.py
   ```

最终验证包括：

- 16 个自动化测试。
- 三个 Python 文件的编译检查。
- 六种正常互动。
- 四种装扮。
- 怪物状态。
- 道歉和示弱两条恢复路径。
- 中文界面与非空画面检查。
- 游戏进程启动和关闭检查。

### 5. 我的理解

AI/Agent 可以帮助拆分任务、生成代码、运行测试和发现问题，但下面的判断仍然需要学习者自己完成：

- 游戏规则是否符合最初想法。
- 对白是否适合角色。
- 属性变化是否合理。
- 测试是否真正验证了需求。
- 最终画面和交互是否达到预期。

这正是 Agentic 学习的重点：不是被动接受代码，而是提出目标、阅读结果、发现问题、要求修改，并用测试和实际运行证明结果。
