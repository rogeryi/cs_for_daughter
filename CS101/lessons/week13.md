# 第 13 周：继承与多态

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块四：面向对象 |
| **课时** | 1.5 小时 |
| **关键词** | 继承、父类、子类、方法重写、super() |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解继承的概念和用途
2. 创建子类并继承父类
3. 重写父类的方法
4. 使用 super() 调用父类方法

---

## 教学内容

### 第一部分：继承的概念与实现（35 分钟）

#### 1.1 为什么需要继承？

```python
# 不使用继承：大量重复代码
class Warrior:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        self.hp -= damage

class Mage:
    def __init__(self, name, hp, attack, mp):
        self.name = name        # 重复
        self.hp = hp            # 重复
        self.attack = attack    # 重复
        self.mp = mp
    
    def take_damage(self, damage):  # 重复
        self.hp -= damage
```

#### 1.2 继承的语法

```python
class 子类(父类):
    def __init__(self, 参数):
        super().__init__(父类参数)  # 调用父类初始化
        self.子类属性 = 值
```

#### 1.3 使用继承重构

```python
# 父类：所有角色的共同特征
class Character:
    """角色基类"""
    
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        """受到伤害"""
        self.hp = max(0, self.hp - damage)
        print(f"{self.name} 受到 {damage} 点伤害，HP: {self.hp}/{self.max_hp}")
    
    def is_alive(self):
        return self.hp > 0
    
    def show_status(self):
        print(f"{self.name} | HP: {self.hp}/{self.max_hp} | 攻击: {self.attack}")

# 子类：战士
class Warrior(Character):
    """战士类"""
    
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack)  # 调用父类初始化
        self.defense = defense              # 战士特有属性
    
    def block(self):
        """格挡（战士特有技能）"""
        print(f"{self.name} 举起盾牌格挡！")

# 子类：法师
class Mage(Character):
    """法师类"""
    
    def __init__(self, name, hp, attack, mp):
        super().__init__(name, hp, attack)
        self.mp = mp
        self.max_mp = mp
    
    def cast_spell(self, target, spell_name, damage, mp_cost):
        """施放法术（法师特有技能）"""
        if self.mp >= mp_cost:
            self.mp -= mp_cost
            print(f"{self.name} 施放 {spell_name}！")
            target.take_damage(damage)
        else:
            print(f"{self.name} MP不足！")

# 使用
warrior = Warrior("亚瑟", 150, 20, 15)
mage = Mage("梅林", 80, 10, 100)

warrior.show_status()  # 继承的方法
warrior.block()        # 战士特有方法

mage.show_status()     # 继承的方法
mage.cast_spell(warrior, "火球术", 30, 20)  # 法师特有方法
```

---

### 第二部分：方法重写（25 分钟）

#### 2.1 什么是方法重写？

子类可以重新定义父类的方法，这叫做**方法重写（Override）**。

```python
class Character:
    def attack(self, target):
        damage = self.attack_power
        print(f"{self.name} 攻击 {target.name}，造成 {damage} 点伤害")
        target.take_damage(damage)

class Warrior(Character):
    # 重写 attack 方法
    def attack(self, target):
        # 战士攻击时有几率暴击
        import random
        is_critical = random.random() < 0.2
        damage = self.attack_power * 2 if is_critical else self.attack_power
        
        if is_critical:
            print(f"💥 暴击！{self.name} 攻击 {target.name}，造成 {damage} 点伤害")
        else:
            print(f"{self.name} 攻击 {target.name}，造成 {damage} 点伤害")
        target.take_damage(damage)
```

#### 2.2 使用 super() 扩展父类方法

```python
class Character:
    def show_status(self):
        print(f"名字: {self.name}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"攻击: {self.attack}")

class Mage(Character):
    def show_status(self):
        super().show_status()  # 先调用父类的方法
        print(f"MP: {self.mp}/{self.max_mp}")  # 再添加法师特有信息
```

---

### 第三部分：课堂练习（20 分钟）

#### 练习：角色职业系统

创建一个包含多个职业的角色系统。

```python
import random

class Character:
    """角色基类"""
    
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage
    
    def is_alive(self):
        return self.hp > 0
    
    def basic_attack(self, target):
        """基础攻击"""
        damage = target.take_damage(self.attack)
        print(f"{self.name} 攻击 {target.name}，造成 {damage} 点伤害")
    
    def show_status(self):
        print(f"[{self.__class__.__name__}] {self.name}")
        print(f"  HP: {self.hp}/{self.max_hp} | 攻击: {self.attack} | 防御: {self.defense}")

class Warrior(Character):
    """战士：高HP高防御"""
    
    def __init__(self, name):
        super().__init__(name, hp=150, attack=20, defense=15)
        self.rage = 0
    
    def basic_attack(self, target):
        super().basic_attack(target)
        self.rage += 10
        print(f"  {self.name} 怒气值: {self.rage}")
    
    def heavy_strike(self, target):
        """重击（消耗怒气）"""
        if self.rage >= 30:
            self.rage -= 30
            damage = target.take_damage(self.attack * 2)
            print(f"⚔️ {self.name} 使用重击，造成 {damage} 点伤害！")
        else:
            print(f"{self.name} 怒气不足！")

class Mage(Character):
    """法师：高攻击有法力"""
    
    def __init__(self, name):
        super().__init__(name, hp=80, attack=15, defense=5)
        self.mp = 100
        self.max_mp = 100
    
    def fireball(self, target):
        """火球术"""
        if self.mp >= 20:
            self.mp -= 20
            damage = target.take_damage(self.attack * 2)
            print(f"🔥 {self.name} 施放火球术，造成 {damage} 点伤害！")
        else:
            print(f"{self.name} MP不足！")
    
    def show_status(self):
        super().show_status()
        print(f"  MP: {self.mp}/{self.max_mp}")

class Archer(Character):
    """弓箭手：高攻击有暴击"""
    
    def __init__(self, name):
        super().__init__(name, hp=100, attack=25, defense=8)
        self.crit_rate = 0.3
    
    def basic_attack(self, target):
        is_crit = random.random() < self.crit_rate
        if is_crit:
            damage = target.take_damage(self.attack * 2)
            print(f"💥 暴击！{self.name} 射中 {target.name}，造成 {damage} 点伤害！")
        else:
            damage = target.take_damage(self.attack)
            print(f"{self.name} 射中 {target.name}，造成 {damage} 点伤害")

# 测试
print("=== 角色创建 ===\n")
warrior = Warrior("亚瑟")
mage = Mage("梅林")
archer = Archer("罗宾汉")

for char in [warrior, mage, archer]:
    char.show_status()
    print()

print("=== 战斗测试 ===\n")
enemy = Character("史莱姆", 50, 10, 5)
warrior.basic_attack(enemy)
mage.fireball(enemy)
archer.basic_attack(enemy)
```

---

### 第四部分：课程总结（10 分钟）

#### 模块四知识回顾

| 周次 | 主题 | 核心概念 |
|------|------|----------|
| 第11周 | 类与对象初识 | class, __init__, self |
| 第12周 | 方法与交互 | 实例方法, 对象交互 |
| 第13周 | 继承与多态 | 继承, super(), 方法重写 |

#### 面向对象三大特性

1. **封装**：把数据和操作数据的方法放在一起
2. **继承**：子类继承父类的属性和方法
3. **多态**：不同子类对同一方法有不同实现

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 继承 | class 子类(父类) |
| super() | 调用父类的方法 |
| 方法重写 | 子类重新定义父类的方法 |
| 父类 | 提供通用功能的基础类 |
| 子类 | 继承并扩展父类的特殊类 |

---

## 参考资料

### 官方文档
- [Python 继承](https://docs.python.org/zh-cn/3/tutorial/classes.html#inheritance)

### 视频教程
- [Python 继承详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)

### 拓展阅读
- [面向对象设计原则](https://en.wikipedia.org/wiki/SOLID)
