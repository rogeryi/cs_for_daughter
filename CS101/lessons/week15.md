# 第 15 周：项目启动准备

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块五：综合应用 |
| **课时** | 1.5 小时 |
| **关键词** | 代码组织、项目框架、假期项目准备 |

---

## 学习目标

完成本节课后，学生将能够：

1. 组织多文件的 Python 项目
2. 搭建游戏的基本框架
3. 理解假期项目的要求和安排
4. 完成游戏设计文档初稿

---

## 教学内容

### 第一部分：代码组织与文件结构（25 分钟）

#### 1.1 创建项目目录

```bash
# 创建项目文件夹
mkdir rpg_game
cd rpg_game

# 创建子目录
mkdir data saves
```

最终结构：
```
rpg_game/
├── main.py           # 程序入口
├── game.py           # 游戏主控制器
├── character.py      # 角色类
├── battle.py         # 战斗系统
├── items.py          # 物品系统
├── shop.py           # 商店系统
├── utils.py          # 工具函数
├── data/
│   └── config.json   # 游戏配置
└── saves/
    └── (存档文件)
```

#### 1.2 模块导入

```python
# main.py
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()

# game.py
from character import Hero, Monster
from battle import Battle
from shop import Shop

class Game:
    def __init__(self):
        self.hero = None
        # ...
```

#### 1.3 __name__ == "__main__" 的作用

```python
# utils.py
def clear_screen():
    print("\n" * 50)

def pause():
    input("按回车继续...")

# 测试代码只在直接运行此文件时执行
if __name__ == "__main__":
    print("测试工具函数")
    clear_screen()
    pause()
```

---

### 第二部分：游戏核心框架搭建（40 分钟）

#### 2.1 character.py - 角色模块

```python
"""角色模块"""

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
    
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
    
    def __str__(self):
        return f"{self.name} HP:{self.hp}/{self.max_hp}"


class Hero(Character):
    """玩家角色"""
    
    def __init__(self, name):
        super().__init__(name, hp=100, attack=15, defense=5)
        self.level = 1
        self.exp = 0
        self.exp_to_next = 100
        self.gold = 100
        self.inventory = []
    
    def gain_exp(self, amount):
        """获得经验值"""
        self.exp += amount
        print(f"获得 {amount} 经验值！")
        while self.exp >= self.exp_to_next:
            self.level_up()
    
    def level_up(self):
        """升级"""
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = int(self.exp_to_next * 1.5)
        
        # 属性提升
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 2
        
        print(f"\n🎉 升级了！当前等级：{self.level}")
    
    def to_dict(self):
        """转换为字典（用于存档）"""
        return {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "exp": self.exp,
            "gold": self.gold,
            "inventory": self.inventory
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建（用于读档）"""
        hero = cls(data["name"])
        hero.level = data["level"]
        hero.hp = data["hp"]
        hero.max_hp = data["max_hp"]
        hero.attack = data["attack"]
        hero.defense = data["defense"]
        hero.exp = data["exp"]
        hero.gold = data["gold"]
        hero.inventory = data["inventory"]
        return hero


class Monster(Character):
    """怪物"""
    
    def __init__(self, name, hp, attack, defense, exp_reward, gold_reward):
        super().__init__(name, hp, attack, defense)
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
```

#### 2.2 game.py - 游戏主控制器

```python
"""游戏主控制器"""
import json
import random
from character import Hero, Monster

class Game:
    """游戏主类"""
    
    def __init__(self):
        self.hero = None
        self.running = True
    
    def run(self):
        """运行游戏"""
        self.main_menu()
    
    def main_menu(self):
        """主菜单"""
        while True:
            print("\n" + "=" * 40)
            print("         《勇者传说》")
            print("=" * 40)
            print("1. 新游戏")
            print("2. 继续游戏")
            print("3. 退出")
            print("=" * 40)
            
            choice = input("请选择：")
            
            if choice == "1":
                self.new_game()
            elif choice == "2":
                self.load_game()
            elif choice == "3":
                print("\n感谢游玩，再见！")
                break
    
    def new_game(self):
        """开始新游戏"""
        print("\n=== 创建角色 ===")
        name = input("请输入角色名字：")
        self.hero = Hero(name)
        print(f"\n欢迎，{name}！你的冒险开始了！")
        self.game_loop()
    
    def game_loop(self):
        """主游戏循环"""
        self.running = True
        
        while self.running and self.hero.is_alive():
            print(f"\n--- {self.hero.name} | Lv.{self.hero.level} | "
                  f"HP:{self.hero.hp}/{self.hero.max_hp} | 金币:{self.hero.gold} ---")
            print("1.探险 2.商店 3.状态 4.存档 5.返回主菜单")
            
            choice = input("选择操作：")
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.visit_shop()
            elif choice == "3":
                self.show_status()
            elif choice == "4":
                self.save_game()
            elif choice == "5":
                self.running = False
        
        if not self.hero.is_alive():
            print("\n游戏结束...")
    
    def explore(self):
        """探险（遇到怪物）"""
        monsters = [
            Monster("史莱姆", 30, 8, 2, 20, 10),
            Monster("哥布林", 40, 12, 3, 30, 15),
            Monster("骷髅兵", 50, 15, 5, 50, 25),
        ]
        monster = random.choice(monsters)
        print(f"\n⚔️ 遭遇了 {monster.name}！")
        
        # 简单战斗逻辑
        while self.hero.is_alive() and monster.is_alive():
            print(f"\n你的HP: {self.hero.hp} | {monster.name}的HP: {monster.hp}")
            print("1.攻击 2.逃跑")
            action = input("选择：")
            
            if action == "1":
                # 玩家攻击
                damage = monster.take_damage(self.hero.attack)
                print(f"你对{monster.name}造成了{damage}点伤害！")
                
                # 怪物反击
                if monster.is_alive():
                    damage = self.hero.take_damage(monster.attack)
                    print(f"{monster.name}对你造成了{damage}点伤害！")
            elif action == "2":
                if random.random() < 0.5:
                    print("逃跑成功！")
                    return
                else:
                    print("逃跑失败！")
                    damage = self.hero.take_damage(monster.attack)
                    print(f"{monster.name}对你造成了{damage}点伤害！")
        
        if self.hero.is_alive():
            print(f"\n🎉 战斗胜利！")
            self.hero.gain_exp(monster.exp_reward)
            self.hero.gold += monster.gold_reward
            print(f"获得 {monster.gold_reward} 金币！")
    
    def visit_shop(self):
        """访问商店"""
        print("\n=== 商店 ===")
        print("1. 生命药水 (50金币) - 恢复50HP")
        print("2. 返回")
        
        choice = input("选择：")
        if choice == "1":
            if self.hero.gold >= 50:
                self.hero.gold -= 50
                self.hero.inventory.append("生命药水")
                print("购买成功！")
            else:
                print("金币不足！")
    
    def show_status(self):
        """显示详细状态"""
        print(f"\n=== {self.hero.name} 的状态 ===")
        print(f"等级: {self.hero.level}")
        print(f"HP: {self.hero.hp}/{self.hero.max_hp}")
        print(f"攻击: {self.hero.attack}")
        print(f"防御: {self.hero.defense}")
        print(f"经验: {self.hero.exp}/{self.hero.exp_to_next}")
        print(f"金币: {self.hero.gold}")
        print(f"背包: {self.hero.inventory}")
    
    def save_game(self):
        """保存游戏"""
        data = self.hero.to_dict()
        with open("saves/save.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✅ 游戏已保存！")
    
    def load_game(self):
        """加载游戏"""
        try:
            with open("saves/save.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.hero = Hero.from_dict(data)
            print(f"✅ 已加载存档：{self.hero.name}")
            self.game_loop()
        except FileNotFoundError:
            print("❌ 没有找到存档文件！")
```

#### 2.3 main.py - 程序入口

```python
"""游戏入口"""
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
```

---

### 第三部分：假期项目说明与答疑（25 分钟）

#### 3.1 假期项目概述

**项目名称**：命令行 RPG 游戏《勇者传说》

**项目目标**：
- 综合运用本学期所学知识
- 独立完成一个完整的游戏项目
- 建立软件开发的完整经验

#### 3.2 六周进度安排

| 周次 | 主题 | 交付物 |
|------|------|--------|
| 第1周 | 需求分析与设计 | 游戏设计文档 |
| 第2周 | 角色系统开发 | character.py 完成 |
| 第3周 | 战斗系统开发 | battle.py 完成 |
| 第4周 | 道具与商店系统 | items.py, shop.py 完成 |
| 第5周 | 游戏流程与存档 | game.py 完成 |
| 第6周 | 完善与展示 | 最终版本 + 展示 |

#### 3.3 每周安排

- **周二 19:00-20:30**：课程指导
- **周五 19:00-20:30**：代码审查
- **其他时间**：自主开发

#### 3.4 评估标准

| 项目 | 占比 | 说明 |
|------|------|------|
| 功能完整性 | 40% | 核心功能是否实现 |
| 代码质量 | 30% | 代码结构、命名、注释 |
| 创意加分 | 20% | 独特的功能或玩法 |
| 文档完整性 | 10% | 设计文档、README |

#### 3.5 答疑时间

（在课堂上回答学生的问题）

---

## 课堂小结

### 本节课内容

| 概念 | 要点 |
|------|------|
| 项目结构 | 多文件组织，模块分离 |
| 模块导入 | from module import Class |
| 游戏框架 | 主控制器 + 各功能模块 |
| __main__ | 程序入口判断 |

### 学期总结

恭喜你完成了 CS101 的学期课程！你已经学会了：

- ✅ Python 基础语法
- ✅ 数据类型和数据结构
- ✅ 条件语句和循环
- ✅ 函数和模块
- ✅ 面向对象编程
- ✅ 文件读写和数据持久化

接下来的假期，让我们一起完成这个激动人心的项目！

---

## 参考资料

### 项目开发
- [Python 项目结构最佳实践](https://docs.python-guide.org/writing/structure/)
- [GitHub 项目管理](https://docs.github.com/cn)

### 游戏开发
- [游戏设计文档模板](https://www.gamedesigning.org/learn/game-design-document/)
- [独立游戏开发经验](https://www.indienova.com/)

### 代码规范
- [PEP 8 代码风格指南](https://peps.python.org/pep-0008/)
- [Python 命名规范](https://realpython.com/python-pep8/)
