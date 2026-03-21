# 第 14 周：项目架构设计

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块五：综合应用 |
| **课时** | 1.5 小时 |
| **关键词** | 软件设计、游戏架构、游戏循环、模块化 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解软件设计的基本思想
2. 分析游戏的基本架构
3. 理解游戏循环的概念
4. 设计自己游戏的基本框架

---

## 教学内容

### 第一部分：软件设计基本思想（20 分钟）

#### 1.1 分而治之

把复杂问题分解成小问题，每个小问题对应一个模块。

```
RPG游戏
├── 角色系统
│   ├── 玩家角色
│   └── 敌人角色
├── 战斗系统
│   ├── 攻击逻辑
│   └── 伤害计算
├── 物品系统
│   ├── 道具
│   └── 装备
├── 存档系统
│   ├── 保存
│   └── 加载
└── 用户界面
    ├── 主菜单
    └── 游戏界面
```

#### 1.2 高内聚低耦合

- **高内聚**：相关功能放在一起
- **低耦合**：模块之间的依赖尽量少

```python
# ✅ 好的设计：每个类负责一件事
class Character:      # 负责角色数据
    pass

class Battle:         # 负责战斗逻辑
    pass

class Inventory:      # 负责物品管理
    pass

# ❌ 不好的设计：一个类做所有事
class Game:
    def create_character(self): ...
    def battle(self): ...
    def manage_items(self): ...
    def save_game(self): ...
```

---

### 第二部分：RPG 游戏架构分析（40 分钟）

#### 2.1 游戏的核心组件

```
┌─────────────────────────────────────────────┐
│                  游戏主控制器                 │
│                  (Game)                      │
├─────────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │ 角色系统 │ │ 战斗系统 │ │ 物品系统 │       │
│  └─────────┘ └─────────┘ └─────────┘       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │ 商店系统 │ │ 存档系统 │ │ UI系统  │       │
│  └─────────┘ └─────────┘ └─────────┘       │
└─────────────────────────────────────────────┘
```

#### 2.2 文件结构设计

```
game/
├── main.py           # 程序入口
├── game.py           # 游戏主控制器
├── character.py      # 角色类
├── battle.py         # 战斗系统
├── items.py          # 物品系统
├── shop.py           # 商店系统
├── save_load.py      # 存档系统
├── ui.py             # 用户界面
├── data/
│   ├── monsters.json # 怪物数据
│   └── items.json    # 物品数据
└── saves/
    └── save.json     # 存档文件
```

#### 2.3 核心类设计

```python
# character.py
class Character:
    """角色基类"""
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        actual = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

class Hero(Character):
    """玩家角色"""
    def __init__(self, name):
        super().__init__(name, hp=100, attack=15, defense=5)
        self.level = 1
        self.exp = 0
        self.gold = 100
        self.inventory = []

class Monster(Character):
    """怪物"""
    def __init__(self, name, hp, attack, defense, exp_reward, gold_reward):
        super().__init__(name, hp, attack, defense)
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
```

---

### 第三部分：游戏循环概念（20 分钟）

#### 3.1 什么是游戏循环？

游戏循环是游戏持续运行的核心结构：

```
┌─────────────────────────────────────┐
│             游戏循环                 │
│  ┌─────────┐                       │
│  │ 显示状态 │ ←────────────┐       │
│  └────┬────┘              │       │
│       ↓                   │       │
│  ┌─────────┐              │       │
│  │ 获取输入 │              │       │
│  └────┬────┘              │       │
│       ↓                   │       │
│  ┌─────────┐              │       │
│  │ 处理逻辑 │              │       │
│  └────┬────┘              │       │
│       ↓                   │       │
│  ┌─────────┐              │       │
│  │ 更新状态 │ ─────────────┘       │
│  └─────────┘                       │
└─────────────────────────────────────┘
```

#### 3.2 游戏循环代码示例

```python
class Game:
    def __init__(self):
        self.running = True
        self.hero = None
    
    def main_menu(self):
        """主菜单"""
        while True:
            print("\n" + "=" * 40)
            print("       《勇者传说》")
            print("=" * 40)
            print("1. 新游戏")
            print("2. 继续游戏")
            print("3. 退出")
            
            choice = input("请选择：")
            if choice == "1":
                self.new_game()
                self.game_loop()
            elif choice == "2":
                if self.load_game():
                    self.game_loop()
            elif choice == "3":
                print("再见！")
                break
    
    def game_loop(self):
        """主游戏循环"""
        while self.running and self.hero.is_alive():
            self.show_status()
            action = self.get_player_action()
            self.process_action(action)
    
    def show_status(self):
        """显示当前状态"""
        print(f"\n{self.hero.name} | HP:{self.hero.hp} | 金币:{self.hero.gold}")
    
    def get_player_action(self):
        """获取玩家输入"""
        print("\n1.探险 2.商店 3.状态 4.存档 5.退出")
        return input("选择操作：")
    
    def process_action(self, action):
        """处理玩家操作"""
        if action == "1":
            self.explore()
        elif action == "2":
            self.visit_shop()
        elif action == "3":
            self.show_full_status()
        elif action == "4":
            self.save_game()
        elif action == "5":
            self.running = False
```

---

### 第四部分：讨论与规划（10 分钟）

#### 4.1 你想做什么样的游戏？

思考以下问题：
- 游戏的主题和背景是什么？
- 主角是谁？有什么特点？
- 有哪些敌人？
- 有哪些道具和装备？
- 有什么特殊玩法？

#### 4.2 绘制游戏设计草图

```
我的游戏设计：

游戏名称：________________

主角：
- 名字：________________
- 职业：________________
- 初始属性：HP___ 攻击___ 防御___

敌人类型：
1. ________________
2. ________________
3. ________________

道具类型：
1. ________________
2. ________________

特殊玩法：
________________
```

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 分而治之 | 把大问题分解成小问题 |
| 模块化 | 相关功能放在一起 |
| 游戏循环 | 显示→输入→处理→更新 |
| 文件组织 | 每个模块一个文件 |

---

## 参考资料

### 游戏开发
- [游戏设计入门](https://www.gamedesigning.org/learn/)
- [Python 游戏开发](https://realpython.com/pygame-a-primer/)

### 软件设计
- [软件设计原则](https://en.wikipedia.org/wiki/SOLID)
- [代码整洁之道](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
