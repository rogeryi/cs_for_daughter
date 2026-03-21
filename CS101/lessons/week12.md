# 第 12 周：方法与交互

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块四：面向对象 |
| **课时** | 1.5 小时 |
| **关键词** | 实例方法、对象交互、战斗系统 |

---

## 学习目标

完成本节课后，学生将能够：

1. 定义和使用各种实例方法
2. 实现对象之间的交互
3. 设计简单的战斗系统

---

## 教学内容

### 第一部分：实例方法详解（30 分钟）

#### 1.1 方法的类型

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    # 获取信息的方法（getter）
    def get_hp(self):
        return self.hp
    
    # 修改状态的方法（setter）
    def set_hp(self, new_hp):
        self.hp = max(0, new_hp)
    
    # 执行动作的方法
    def attack(self, target):
        damage = 10
        target.take_damage(damage)
    
    # 返回布尔值的方法
    def is_alive(self):
        return self.hp > 0
    
    # 返回字符串描述的方法
    def __str__(self):
        return f"{self.name}（HP: {self.hp}）"
```

#### 1.2 __str__ 魔术方法

`__str__` 方法定义对象被转换为字符串时的表示。

```python
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"[{self.species}] {self.name}"

cat = Pet("咪咪", "猫")
print(cat)  # [猫] 咪咪
```

---

### 第二部分：对象之间的交互（30 分钟）

#### 2.1 对象作为参数

```python
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self, target):
        """攻击另一个角色"""
        damage = self.attack_power
        print(f"{self.name} 攻击 {target.name}，造成 {damage} 点伤害！")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        """受到伤害"""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} 被击败了！")
        else:
            print(f"{self.name} 剩余 HP: {self.hp}")

# 两个角色交互
hero = Character("勇者", 100, 25)
slime = Character("史莱姆", 30, 5)

hero.attack(slime)   # 勇者 攻击 史莱姆，造成 25 点伤害！
slime.attack(hero)   # 史莱姆 攻击 勇者，造成 5 点伤害！
```

#### 2.2 完整的角色类

```python
class GameCharacter:
    """游戏角色类"""
    
    def __init__(self, name, max_hp, attack, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.hp > 0
    
    def attack_target(self, target):
        """攻击目标"""
        # 计算实际伤害（攻击力 - 防御力，最少1点）
        damage = max(1, self.attack - target.defense)
        print(f"\n{self.name} 攻击 {target.name}！")
        target.take_damage(damage)
        return damage
    
    def take_damage(self, damage):
        """受到伤害"""
        self.hp = max(0, self.hp - damage)
        print(f"{self.name} 受到 {damage} 点伤害！HP: {self.hp}/{self.max_hp}")
    
    def heal(self, amount):
        """恢复生命"""
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        actual = self.hp - old_hp
        print(f"{self.name} 恢复了 {actual} 点生命！HP: {self.hp}/{self.max_hp}")
    
    def show_status(self):
        """显示状态"""
        status = "存活" if self.is_alive() else "死亡"
        print(f"{self.name} | HP: {self.hp}/{self.max_hp} | 攻击: {self.attack} | 防御: {self.defense} | {status}")
```

---

### 第三部分：战斗系统雏形（30 分钟）

#### 3.1 简单回合制战斗

```python
import random

class Fighter:
    """战斗角色"""
    
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.hp > 0
    
    def do_attack(self, target):
        """执行攻击"""
        # 基础伤害
        base_damage = self.attack - target.defense
        # 添加随机浮动（±20%）
        variance = random.uniform(0.8, 1.2)
        damage = max(1, int(base_damage * variance))
        
        target.hp = max(0, target.hp - damage)
        return damage
    
    def __str__(self):
        return f"{self.name} HP:{self.hp}/{self.max_hp}"

def battle(fighter1, fighter2):
    """回合制战斗"""
    print("=" * 40)
    print("        战斗开始！")
    print("=" * 40)
    print(f"{fighter1.name} VS {fighter2.name}")
    print()
    
    turn = 1
    while fighter1.is_alive() and fighter2.is_alive():
        print(f"--- 回合 {turn} ---")
        
        # 角色1攻击
        if fighter1.is_alive():
            damage = fighter1.do_attack(fighter2)
            print(f"{fighter1.name} 攻击 {fighter2.name}，造成 {damage} 点伤害！")
            print(f"  {fighter2}")
        
        # 角色2攻击
        if fighter2.is_alive():
            damage = fighter2.do_attack(fighter1)
            print(f"{fighter2.name} 攻击 {fighter1.name}，造成 {damage} 点伤害！")
            print(f"  {fighter1}")
        
        print()
        turn += 1
    
    # 判定胜负
    print("=" * 40)
    if fighter1.is_alive():
        print(f"🏆 {fighter1.name} 获胜！")
    else:
        print(f"🏆 {fighter2.name} 获胜！")
    print("=" * 40)

# 测试战斗
hero = Fighter("勇者", 100, 25, 10)
boss = Fighter("魔王", 150, 20, 15)
battle(hero, boss)
```

---

### 第四部分：课堂练习（30 分钟）

#### 练习：完善战斗系统

添加以下功能：
- 防御动作（本回合减少受到的伤害）
- 技能攻击（消耗MP，造成更高伤害）

```python
class BattleCharacter:
    """战斗角色（增强版）"""
    
    def __init__(self, name, hp, mp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.is_defending = False
    
    def normal_attack(self, target):
        """普通攻击"""
        defense = target.defense * 2 if target.is_defending else target.defense
        damage = max(1, self.attack - defense)
        target.hp = max(0, target.hp - damage)
        target.is_defending = False
        print(f"{self.name} 普通攻击 {target.name}，造成 {damage} 点伤害！")
    
    def skill_attack(self, target, skill_name, mp_cost, multiplier):
        """技能攻击"""
        if self.mp < mp_cost:
            print(f"{self.name} MP不足，无法使用 {skill_name}！")
            return False
        
        self.mp -= mp_cost
        defense = target.defense * 2 if target.is_defending else target.defense
        damage = max(1, int(self.attack * multiplier) - defense)
        target.hp = max(0, target.hp - damage)
        target.is_defending = False
        print(f"{self.name} 使用 {skill_name}，造成 {damage} 点伤害！")
        return True
    
    def defend(self):
        """防御"""
        self.is_defending = True
        print(f"{self.name} 进入防御姿态！")
    
    def show_status(self):
        print(f"{self.name} | HP:{self.hp}/{self.max_hp} | MP:{self.mp}/{self.max_mp}")
```

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 实例方法 | 操作对象数据的函数 |
| __str__ | 定义对象的字符串表示 |
| 对象交互 | 一个对象调用另一个对象的方法 |
| 战斗系统 | 对象交互的实际应用 |

---

## 参考资料

### 官方文档
- [Python 类和方法](https://docs.python.org/zh-cn/3/tutorial/classes.html)

### 视频教程
- [Python 面向对象编程 - B站](https://www.bilibili.com/video/BV1ex411x7Em)

### 游戏开发
- [回合制战斗系统设计](https://www.gamedesigning.org/learn/turn-based-combat/)
