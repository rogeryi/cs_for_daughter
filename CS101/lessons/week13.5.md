# 第 13.5 周：封装与多态

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块四：面向对象 |
| **课时** | 1.5 小时 |
| **关键词** | 封装、私有属性、getter/setter、多态、鸭子类型 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解封装的概念，知道为什么要保护对象内部数据
2. 使用下划线约定和 `property` 控制属性的访问
3. 理解多态的概念：同一方法，不同表现
4. 利用多态写出"不关心具体类型"的通用代码

---

## 教学内容

### 第一部分：封装——给对象装上保护罩（35 分钟）

#### 1.1 什么是封装？

**封装（Encapsulation）**：把数据（属性）和操作数据的方法绑在一起，同时隐藏内部细节，只暴露安全的接口。

第 11 周我们已经做过一半了——把 `name`、`hp` 和 `take_damage()` 放进同一个类里，这就是"绑在一起"。这一课补上另一半：**隐藏和保护**。

#### 1.2 没有封装会出什么问题？

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

hero = Character("勇者", 100)
hero.hp = 99999      # 外部可以随意改血量！
hero.hp = -50        # 甚至可以改成负数
print(hero.hp)       # -50，游戏逻辑已经坏了
```

问题在于：任何人都能绕过规则直接改数据。就像自动售货机如果敞开后盖，谁都能直接拿饮料，投币检查就没意义了。

**封装的思路**：把数据锁在对象内部，所有修改都必须经过方法——方法里可以写规则。

#### 1.3 私有属性：下划线约定

Python 用下划线前缀表示"这是内部属性，外部不要直接碰"：

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp          # 单下划线：约定俗成的"内部属性"
        self._max_hp = hp

    def take_damage(self, damage):
        """受伤——修改血量的唯一入口，规则在这里"""
        self._hp = max(0, self._hp - damage)   # 保证不会变成负数
        print(f"{self.name} 受到 {damage} 点伤害，HP: {self._hp}/{self._max_hp}")

    def get_hp(self):
        """查询血量"""
        return self._hp

hero = Character("勇者", 100)
hero.take_damage(30)       # 勇者 受到 30 点伤害，HP: 70/100
hero.take_damage(200)      # HP 最低只会到 0，不会是负数
print(hero.get_hp())       # 0
```

> **注意**：Python 不会真的阻止你访问 `_hp`，单下划线是一种**约定**——就像门上贴的"员工通道"，大家都遵守，但没上锁。

双下划线 `__hp` 会触发 Python 的名字改写（变成 `_Character__hp`），更难从外部访问，初学者了解即可，日常用单下划线就够了。

#### 1.4 property：像属性一样访问，像方法一样受控

`get_hp()` 这种写法能用，但调用时带括号不太自然。`property` 让方法看起来像属性：

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """查询余额（只读）"""
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("存款金额必须大于0")
            return
        self._balance += amount
        print(f"存入 {amount} 元，余额：{self._balance} 元")

account = BankAccount("小明", 1000)
print(account.balance)      # 1000，像访问属性一样，不用括号
account.deposit(500)        # 存入 500 元，余额：1500 元
account.balance = 999999    # 报错！没有定义 setter，余额只读
```

#### 1.5 封装小结

| 做法 | 效果 |
|------|------|
| 属性加 `_` 前缀 | 标记为内部属性，外部不直接碰 |
| 修改走方法 | 方法里集中写校验规则 |
| `@property` | 读取像属性，依然受控 |

一句话：**外面的人只需要知道"能做什么"（接口），不需要知道"怎么做到的"（内部实现）。**

---

### 第二部分：多态——同一指令，不同表现（35 分钟）

#### 2.1 什么是多态？

**多态（Polymorphism）**：同一个方法名，不同类型的对象调用时表现出不同的行为。

第 13 周学过方法重写，多态就是方法重写在运行时的效果：

```python
class Character:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name} 发起攻击")

class Warrior(Character):
    def attack(self, target):
        print(f"⚔️ {self.name} 挥剑攻击 {target.name}！")

class Mage(Character):
    def attack(self, target):
        print(f"🔥 {self.name} 施放火球攻击 {target.name}！")

class Archer(Character):
    def attack(self, target):
        print(f"🏹 {self.name} 放箭攻击 {target.name}！")
```

调用方不需要知道对方是哪个子类：

```python
enemy = Character("史莱姆")

def command_attack(char, target):
    """指挥官只喊一声'攻击'，每个职业用自己的方式执行"""
    char.attack(target)

command_attack(Warrior("亚瑟"), enemy)   # ⚔️ 亚瑟 挥剑攻击 史莱姆！
command_attack(Mage("梅林"), enemy)      # 🔥 梅林 施放火球攻击 史莱姆！
command_attack(Archer("罗宾汉"), enemy)  # 🏹 罗宾汉 放箭攻击 史莱姆！
```

`command_attack` 里只写了 `char.attack(target)` 一行——**同样的调用，不同的行为**，这就是多态。

#### 2.2 多态的威力：通用代码

没有多态，就得写一堆 if-else：

```python
# 不用多态：类型判断越写越长
def attack_all(characters, target):
    for char in characters:
        if isinstance(char, Warrior):
            print(f"⚔️ {char.name} 挥剑攻击！")
        elif isinstance(char, Mage):
            print(f"🔥 {char.name} 施放火球！")
        elif isinstance(char, Archer):
            print(f"🏹 {char.name} 放箭！")
        # 新增一个职业，这里就要再加一个 elif……

# 用多态：一行搞定，新增职业不用改这里
def attack_all(characters, target):
    for char in characters:
        char.attack(target)

team = [Warrior("亚瑟"), Mage("梅林"), Archer("罗宾汉")]
attack_all(team, enemy)
```

好处：**新增类型时，写通用代码的地方一行都不用改**，只要新类实现好 `attack` 方法即可。

#### 2.3 鸭子类型：Python 的多态特色

Python 不检查类型，只关心对象"有没有这个方法"：

> 如果它走起来像鸭子、叫起来像鸭子，那它就是鸭子。

```python
class Robot:
    """不是 Character 的子类，但有 attack 方法"""
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"🤖 {self.name} 发射激光攻击 {target.name}！")

command_attack(Robot("高达"), enemy)   # 🤖 高达 发射激光攻击 史莱姆！
```

`Robot` 没有继承 `Character`，但它有 `attack` 方法，照样能传给 `command_attack`。在 Python 里，**行为（有什么方法）比身份（是什么类）更重要**。

#### 2.4 多态小结

| 概念 | 要点 |
|------|------|
| 多态 | 同一方法名，不同对象有不同行为 |
| 实现方式 | 子类重写父类方法 |
| 好处 | 调用方写通用代码，不关心具体类型 |
| 鸭子类型 | 只要有对应方法就能用，不强制继承 |

---

### 第三部分：综合练习（15 分钟）

#### 练习：封装 + 多态的角色系统

要求：
1. 用封装改造第 13 周的角色类：`hp` 改为 `_hp`，血量只能通过 `take_damage` / `heal` 修改，且始终在 `0 ~ max_hp` 之间
2. 给 `Character` 定义 `skill(target)` 方法，每个子类重写出自己的技能
3. 写一个 `battle_round(char_a, char_b)` 函数，让两个角色轮流放技能——只调用 `skill()`，不判断类型

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self._hp = hp
        self._max_hp = hp

    @property
    def hp(self):
        return self._hp

    def is_alive(self):
        return self._hp > 0

    def take_damage(self, damage):
        self._hp = max(0, self._hp - damage)

    def skill(self, target):
        """技能（子类重写）"""
        print(f"{self.name} 发动了普通攻击")

class Warrior(Character):
    def skill(self, target):
        damage = 30
        target.take_damage(damage)
        print(f"⚔️ {self.name} 重击 {target.name}，造成 {damage} 伤害")

class Mage(Character):
    def skill(self, target):
        damage = 45
        target.take_damage(damage)
        print(f"🔥 {self.name} 火球轰击 {target.name}，造成 {damage} 伤害")

def battle_round(char_a, char_b):
    """通用战斗：只靠多态，不关心具体职业"""
    while char_a.is_alive() and char_b.is_alive():
        char_a.skill(char_b)
        if char_b.is_alive():
            char_b.skill(char_a)
    winner = char_a if char_a.is_alive() else char_b
    print(f"🏆 {winner.name} 获胜！")

battle_round(Warrior("亚瑟", 100), Mage("梅林", 90))
```

---

### 第四部分：课程总结（5 分钟）

#### 面向对象三大特性（完整版）

| 特性 | 一句话 | 在哪周学 |
|------|--------|----------|
| 封装 | 数据和方法绑在一起，隐藏内部、保护数据 | 第 11 周 + 本周 |
| 继承 | 子类复用并扩展父类 | 第 13 周 |
| 多态 | 同一方法，不同对象不同行为 | 本周 |

三大特性配合起来：继承搭建类型体系，多态让通用代码灵活扩展，封装保证每个对象内部数据安全。

---

## 课堂小结

| 概念 | 要点 |
|------|------|
| 封装 | 隐藏内部实现，通过方法/接口访问数据 |
| `_属性` | 单下划线前缀，约定为内部属性 |
| getter/setter | 读取/修改属性的受控方法 |
| @property | 让方法像属性一样访问 |
| 多态 | 同一方法名，不同对象不同行为 |
| 鸭子类型 | 有对应方法即可使用，不强制继承 |

---

## 参考资料

### 官方文档
- [Python 类与私有成员](https://docs.python.org/zh-cn/3/tutorial/classes.html#private-variables)
- [property 内置函数](https://docs.python.org/zh-cn/3/library/functions.html#property)

### 视频教程
- [Python 面向对象编程 - B站](https://www.bilibili.com/video/BV1ex411x7Em)

### 拓展阅读
- [Duck typing - Wikipedia](https://en.wikipedia.org/wiki/Duck_typing)
