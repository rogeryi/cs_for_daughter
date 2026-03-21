# 第 11 周：类与对象初识

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块四：面向对象 |
| **课时** | 1.5 小时 |
| **关键词** | 类、对象、属性、__init__、self |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解面向对象编程的基本概念
2. 定义简单的类
3. 创建和使用对象
4. 理解 `__init__` 方法和 `self` 参数

---

## 教学内容

### 第一部分：从现实世界理解对象（20 分钟）

#### 1.1 什么是对象？

在现实世界中，**对象**是具体的事物。每个对象都有：
- **属性**：描述对象的特征（是什么样的）
- **行为**：对象能做的事情（能做什么）

```
例子：一只猫

属性（特征）：
- 名字：咪咪
- 颜色：橘色
- 年龄：2岁

行为（动作）：
- 吃东西
- 睡觉
- 喵喵叫
```

#### 1.2 类和对象的关系

- **类（Class）**：是对象的"蓝图"或"模板"
- **对象（Object）**：是根据类创建的具体实例

```
类 "猫" 是一个模板，定义了猫应该有什么属性和行为

对象是具体的猫：
- 咪咪（橘猫，2岁）
- 小黑（黑猫，3岁）
- 花花（花猫，1岁）
```

---

### 第二部分：定义第一个类（30 分钟）

#### 2.1 类的定义语法

```python
class 类名:
    """类的文档字符串"""
    
    def __init__(self, 参数1, 参数2):
        """初始化方法"""
        self.属性1 = 参数1
        self.属性2 = 参数2
    
    def 方法名(self):
        """方法（对象的行为）"""
        # 方法体
```

#### 2.2 第一个类：猫

```python
class Cat:
    """猫类"""
    
    def __init__(self, name, color, age):
        """初始化猫的属性"""
        self.name = name
        self.color = color
        self.age = age
    
    def meow(self):
        """喵喵叫"""
        print(f"{self.name}：喵喵喵~")
    
    def introduce(self):
        """自我介绍"""
        print(f"我是{self.color}色的猫，名叫{self.name}，今年{self.age}岁。")

# 创建对象（实例化）
cat1 = Cat("咪咪", "橘", 2)
cat2 = Cat("小黑", "黑", 3)

# 访问属性
print(cat1.name)   # 咪咪
print(cat2.age)    # 3

# 调用方法
cat1.meow()        # 咪咪：喵喵喵~
cat2.introduce()   # 我是黑色的猫，名叫小黑，今年3岁。
```

#### 2.3 理解 __init__ 和 self

**`__init__` 方法：**
- 初始化方法，创建对象时自动调用
- 用于设置对象的初始属性
- 双下划线开头和结尾，称为"魔术方法"

**`self` 参数：**
- 代表对象自身
- 在类的方法中访问对象的属性和其他方法
- 调用方法时不需要传入 self，Python 自动处理

```python
cat1 = Cat("咪咪", "橘", 2)

# 实际发生的事情：
# 1. Python 创建一个新对象
# 2. 调用 __init__(self, "咪咪", "橘", 2)
#    其中 self 就是新创建的对象
# 3. self.name = "咪咪" 给这个对象设置 name 属性
```

---

### 第三部分：更多示例（30 分钟）

#### 3.1 游戏角色类

```python
class Character:
    """游戏角色类"""
    
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.is_alive = True
    
    def take_damage(self, damage):
        """受到伤害"""
        self.hp -= damage
        print(f"{self.name} 受到 {damage} 点伤害！")
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} 被击败了！")
    
    def heal(self, amount):
        """恢复生命"""
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.name} 恢复了 {amount} 点生命，当前HP：{self.hp}")
    
    def show_status(self):
        """显示状态"""
        print(f"{self.name} - HP: {self.hp}/{self.max_hp}, 攻击: {self.attack}")

# 创建角色
hero = Character("勇者", 100, 20)
monster = Character("史莱姆", 30, 5)

# 使用角色
hero.show_status()        # 勇者 - HP: 100/100, 攻击: 20
monster.show_status()     # 史莱姆 - HP: 30/30, 攻击: 5

hero.take_damage(15)      # 勇者 受到 15 点伤害！
hero.heal(10)             # 勇者 恢复了 10 点生命，当前HP：95
```

#### 3.2 银行账户类

```python
class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            print(f"存入 {amount} 元，余额：{self.balance} 元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款"""
        if amount > self.balance:
            print(f"余额不足！当前余额：{self.balance} 元")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            self.balance -= amount
            print(f"取出 {amount} 元，余额：{self.balance} 元")
    
    def get_balance(self):
        """查询余额"""
        return self.balance

# 使用
account = BankAccount("小明", 1000)
account.deposit(500)      # 存入 500 元，余额：1500 元
account.withdraw(200)     # 取出 200 元，余额：1300 元
account.withdraw(2000)    # 余额不足！当前余额：1300 元
```

---

### 第四部分：课堂练习（10 分钟）

#### 练习：宠物类

创建一个宠物类，包含基本属性和行为。

```python
class Pet:
    """宠物类"""
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species  # 种类
        self.age = age
        self.hunger = 50        # 饥饿度 0-100
        self.happiness = 50     # 快乐度 0-100
    
    def feed(self):
        """喂食"""
        self.hunger = max(0, self.hunger - 30)
        print(f"喂了{self.name}食物，饥饿度：{self.hunger}")
    
    def play(self):
        """玩耍"""
        self.happiness = min(100, self.happiness + 20)
        self.hunger = min(100, self.hunger + 10)
        print(f"和{self.name}玩耍，快乐度：{self.happiness}")
    
    def show_status(self):
        """显示状态"""
        print(f"\n=== {self.name} ===")
        print(f"种类：{self.species}")
        print(f"年龄：{self.age}岁")
        print(f"饥饿度：{self.hunger}/100")
        print(f"快乐度：{self.happiness}/100")

# 测试
my_pet = Pet("小白", "狗", 2)
my_pet.show_status()
my_pet.feed()
my_pet.play()
my_pet.show_status()
```

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 类 | 对象的模板/蓝图 |
| 对象 | 类的具体实例 |
| 属性 | 对象的数据/特征 |
| 方法 | 对象的行为/功能 |
| __init__ | 初始化方法，创建对象时自动调用 |
| self | 代表对象自身 |

---

## 参考资料

### 官方文档
- [Python 类](https://docs.python.org/zh-cn/3/tutorial/classes.html)

### 视频教程
- [Python 面向对象 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 类和对象 - 菜鸟教程](https://www.runoob.com/python3/python3-class.html)

### 拓展阅读
- [面向对象编程简介](https://realpython.com/python3-object-oriented-programming/)
