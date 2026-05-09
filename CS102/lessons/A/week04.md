# Week 04: 值、引用、`const` 和函数接口

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属部分** | CS102A：现代 C++ 编程与内存模型 |
| **课时** | 2 小时，一对一现场授课 |
| **主环境** | Xcode IDE 工程 |
| **关键词** | 值传递、引用传递、`const`、函数接口、修改权限 |
| **系统连接** | 参数传递决定是否复制对象、是否能修改原对象 |

---

## 教师导读

Week04 是 C++ 思维真正开始和 Python 拉开差距的一节。学生会第一次系统地遇到：函数拿到的到底是“副本”，还是“原来的对象”。

这节课要避免一开始就陷入“引用底层是什么”。先用游戏角色生命值做直观实验：

- 按值传递：函数拿到副本，原角色没变
- 引用传递：函数拿到别名，原角色会变
- `const` 引用：函数能读取，但不能修改

核心目标是让学生开始理解函数接口不是随便写的，它表达了数据流向和修改权限。

---

## 本节课目标

完成本节课后，学生应该能够：

1. 解释按值传递会复制数据
2. 使用引用参数修改外部变量
3. 使用 `const` 表达只读意图
4. 区分 `T`、`T&`、`const T&`
5. 设计简单函数接口：读、写、查询
6. 在 Xcode 中观察函数内外变量地址和变化

---

## 课前准备

创建本周目录和工程：

```text
CS102/
└── week04/
    └── Week04References/
        └── Week04References.xcodeproj
```

本周仍使用单个 `main.cpp`，重点是调试观察函数参数。

---

## 2 小时课堂流程

| 时间 | 环节 | 内容 |
|------|------|------|
| 0:00-0:10 | 复习 | 函数、参数、调用栈 |
| 0:10-0:30 | 值传递 | 治疗函数为什么没生效 |
| 0:30-0:50 | 引用传递 | 用 `int&` 修改原变量 |
| 0:50-1:10 | `const` | 只读参数和修改权限 |
| 1:10-1:30 | 接口设计 | `damage`、`heal`、`print_status` |
| 1:30-1:45 | Xcode 调试 | 地址、变量变化、调用栈 |
| 1:45-1:55 | 学生扩展 | 角色状态函数组 |
| 1:55-2:00 | 复盘 | 函数接口表达意图 |

---

## 一、问题引入：治疗函数为什么没生效？

### 教师示范：按值传递

```cpp
#include <iostream>

void heal(int hp) {
    hp = hp + 20;
    std::cout << "函数内部 hp: " << hp << std::endl;
}

int main() {
    int heroHp {50};

    std::cout << "治疗前 heroHp: " << heroHp << std::endl;
    heal(heroHp);
    std::cout << "治疗后 heroHp: " << heroHp << std::endl;

    return 0;
}
```

运行结果会类似：

```text
治疗前 heroHp: 50
函数内部 hp: 70
治疗后 heroHp: 50
```

让学生先猜，再运行。

讲解：

```text
heal(int hp)
```

这里的 `hp` 是 `heroHp` 的副本。函数内部改的是副本，不是原来的变量。

现场追问：

- “函数内部 hp 变了吗？”
- “main 里的 heroHp 变了吗？”
- “如果函数拿到的是副本，修改副本会影响原件吗？”

---

## 二、引用：给原对象起别名

### 修正版：引用传递

```cpp
#include <iostream>

void heal(int& hp) {
    hp = hp + 20;
    std::cout << "函数内部 hp: " << hp << std::endl;
}

int main() {
    int heroHp {50};

    std::cout << "治疗前 heroHp: " << heroHp << std::endl;
    heal(heroHp);
    std::cout << "治疗后 heroHp: " << heroHp << std::endl;

    return 0;
}
```

运行结果：

```text
治疗前 heroHp: 50
函数内部 hp: 70
治疗后 heroHp: 70
```

讲解：

```cpp
int& hp
```

可以理解为：

```text
hp 是传入变量的另一个名字。
```

函数内部修改 `hp`，就是修改外面的 `heroHp`。

---

## 三、Xcode 调试观察：值和引用的地址

### 观察按值传递

在按值版本里加入：

```cpp
std::cout << "函数内部 hp 地址: " << &hp << std::endl;
```

在 `main` 中加入：

```cpp
std::cout << "main 中 heroHp 地址: " << &heroHp << std::endl;
```

完整观察代码：

```cpp
#include <iostream>

void heal(int hp) {
    std::cout << "函数内部 hp 地址: " << &hp << std::endl;
    hp = hp + 20;
}

int main() {
    int heroHp {50};

    std::cout << "main 中 heroHp 地址: " << &heroHp << std::endl;
    heal(heroHp);

    return 0;
}
```

学生会看到两个地址通常不同。

### 观察引用传递

把函数改为：

```cpp
void heal(int& hp)
```

再运行，通常会看到函数内部地址和外部地址相同。

讲解要谨慎：

- 地址相同帮助理解“引用是别名”
- 不需要把引用解释成“完全等于指针”
- 指针下一周再讲

---

## 四、`const`：明确说“我不会改”

### 只读输出函数

```cpp
#include <iostream>
#include <string>

void print_status(const std::string& name, int hp) {
    std::cout << name << " HP: " << hp << std::endl;
}

int main() {
    std::string heroName {"Mira"};
    int heroHp {80};

    print_status(heroName, heroHp);
    return 0;
}
```

为什么 `name` 用 `const std::string&`？

- `std::string` 可能比 `int` 大，复制有成本
- 函数只是读取名字，不应该修改
- `const` 把“不修改”写进接口

如果在函数中尝试：

```cpp
name = "Changed";
```

编译器会报错。

讲解：

> `const` 像一个承诺：这个函数只看，不改。

---

## 五、三种参数方式对比

| 写法 | 含义 | 是否复制 | 是否能修改外部对象 | 常见用途 |
|------|------|----------|--------------------|----------|
| `int x` | 按值传递 | 是 | 否 | 小对象、需要副本 |
| `int& x` | 引用传递 | 否 | 是 | 需要修改外部对象 |
| `const std::string& x` | 只读引用 | 否 | 否 | 读取较大对象 |

### 本课程初期经验法则

- 小的基础类型：`int`、`double`、`bool` 通常按值传递
- 需要修改外部对象：用 `T&`
- 较大的只读对象：用 `const T&`

以后会学 `std::string_view`、智能指针、移动语义，这些会让接口设计更细致。

---

## 六、项目实践：角色状态函数组

### 教师示范

```cpp
#include <iostream>
#include <string>

void print_status(const std::string& name, int hp, int maxHp) {
    std::cout << name << " HP: " << hp << "/" << maxHp << std::endl;
}

void take_damage(int& hp, int damage) {
    hp = hp - damage;
    if (hp < 0) {
        hp = 0;
    }
}

void heal(int& hp, int amount, int maxHp) {
    hp = hp + amount;
    if (hp > maxHp) {
        hp = maxHp;
    }
}

bool is_alive(int hp) {
    return hp > 0;
}

int main() {
    std::string heroName {"Mira"};
    int maxHp {100};
    int hp {80};

    print_status(heroName, hp, maxHp);

    take_damage(hp, 35);
    print_status(heroName, hp, maxHp);

    heal(hp, 20, maxHp);
    print_status(heroName, hp, maxHp);

    if (is_alive(hp)) {
        std::cout << heroName << " 仍然可以战斗。" << std::endl;
    }

    return 0;
}
```

### 分析函数接口

```cpp
void print_status(const std::string& name, int hp, int maxHp)
```

只读，不修改角色。

```cpp
void take_damage(int& hp, int damage)
```

会修改生命值，所以 `hp` 是引用。

```cpp
bool is_alive(int hp)
```

只需要读取一个小整数，按值传递即可。

现场追问：

- “哪个函数会修改外部变量？”
- “哪个函数只是查询？”
- “如果 `take_damage` 的参数写成 `int hp` 会发生什么？”

---

## 七、Xcode 调试观察

### 观察目标

让学生看到：

- `take_damage` 进入前后，`hp` 如何变化
- 引用参数和外部变量是同一个对象
- `const` 参数不能被修改

### 操作步骤

1. 在 `take_damage(hp, 35);` 设置断点
2. Run
3. Step Into 进入 `take_damage`
4. 查看调用栈：当前函数是 `take_damage`，下面是 `main`
5. 查看变量面板中的 `hp`
6. Step Over 执行 `hp = hp - damage;`
7. 观察 `main` 中的 `hp` 也变化
8. Step Out 回到 `main`

### 地址观察

在 `take_damage` 中临时加入：

```cpp
std::cout << "take_damage hp address: " << &hp << std::endl;
```

在 `main` 中加入：

```cpp
std::cout << "main hp address: " << &hp << std::endl;
```

用地址相同辅助理解引用。

---

## 八、学生接手练习

让学生添加魔法值：

```cpp
int maxMp {50};
int mp {30};
```

添加函数：

```cpp
void use_spell(int& mp, int cost) {
    if (mp >= cost) {
        mp = mp - cost;
        std::cout << "释放魔法，消耗 " << cost << " MP。" << std::endl;
    } else {
        std::cout << "MP 不足，无法释放魔法。" << std::endl;
    }
}
```

学生需要思考：

- `mp` 为什么是引用？
- `cost` 为什么按值传递？
- 这个函数是否应该返回 `bool` 表示是否释放成功？

改进方向：

```cpp
bool use_spell(int& mp, int cost) {
    if (mp < cost) {
        return false;
    }

    mp = mp - cost;
    return true;
}
```

讲解：返回值可以让调用者决定怎么显示结果，这样函数职责更清楚。

---

## 九、常见错误与讲解

### 1. 以为函数一定能修改外部变量

错误直觉：把变量传进去，函数里改了，外面就改。

解释：C++ 默认是按值传递，函数拿到副本。

### 2. 引用参数忘记 `&`

```cpp
void heal(int hp)  // 不会修改外部 hp
```

应该是：

```cpp
void heal(int& hp)
```

### 3. 不该修改的参数没有 `const`

```cpp
void print_status(std::string& name)
```

如果不修改 `name`，更清楚的写法是：

```cpp
void print_status(const std::string& name)
```

### 4. 所有参数都用引用

讲解：引用不是越多越好。接口要表达真实意图。

---

## 十、系统/设计连接

函数接口是模块设计的雏形。

当你看到一个函数：

```cpp
void take_damage(int& hp, int damage)
```

你可以从参数看出：

- 它会修改 `hp`
- 它不会修改 `damage`
- 它没有返回值

大型源码分析中，读函数签名常常比读函数内部更重要。好的接口让读者先理解“这个函数想做什么”。

---

## 十一、AI 辅助创作任务

让学生把角色状态扩成一个小战斗片段：

- 玩家有 HP 和 MP
- 怪物攻击玩家
- 玩家释放魔法
- 如果 MP 不够，普通攻击

重点不是功能多，而是每个函数接口要清楚：

```cpp
void take_damage(int& hp, int damage);
bool use_spell(int& mp, int cost);
void print_status(const std::string& name, int hp, int mp);
bool is_alive(int hp);
```

---

## 十二、学习报告模板

```markdown
# CS102 Week 04 学习报告

## 1. 本周核心知识

- 按值传递会复制变量
- 引用传递可以修改原变量
- `const` 表示只读承诺
- 函数接口表达读写意图

## 2. 参数传递对比

| 写法 | 是否复制 | 能否修改外部变量 | 适合场景 |
|------|----------|------------------|----------|
| `T x` | 是 | 否 | 小对象 |
| `T& x` | 否 | 是 | 需要修改 |
| `const T& x` | 否 | 否 | 只读大对象 |

## 3. Xcode 调试观察

- 按值传递时地址是否相同：
- 引用传递时地址是否相同：
- 调用栈中看到了哪些函数：

## 4. 本周代码

```cpp
// 粘贴角色状态函数组代码
```

## 5. 我的理解

为什么函数参数写法也是一种设计？
```

---

## 十三、教师检查清单

本节课结束前，确认学生能做到：

- 能解释按值传递为什么不修改原变量
- 能写出一个引用参数函数
- 能解释 `const std::string&` 的意义
- 能看函数签名判断是否可能修改参数
- 能用 Xcode Step Into 观察引用参数变化
- 能通过地址观察辅助解释引用
