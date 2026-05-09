# Week 02: 类型、变量、输入输出

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属部分** | CS102A：现代 C++ 编程与内存模型 |
| **课时** | 2 小时，一对一现场授课 |
| **主环境** | Xcode IDE 工程 |
| **关键词** | 类型、变量、初始化、`std::cin`、`std::cout`、输入失败 |
| **系统连接** | 数据在内存中有类型、大小和表示方式 |

---

## 教师导读

这一节要让学生建立 C++ 的第一条重要直觉：**数据不是“随便放在那里”的，数据有类型，类型决定它能做什么、占多大空间、如何被解释。**

从 Python 迁移过来时，学生可能会觉得 C++ “多写了很多类型”。这节课不要把类型讲成负担，而要讲成工具：类型帮助编译器提前发现错误，也帮助人理解程序。

本节课用“游戏角色属性卡”作为主线：名字、等级、生命值、攻击力、是否存活。学生可以很自然地理解为什么不同数据需要不同类型。

---

## 本节课目标

完成本节课后，学生应该能够：

1. 创建并初始化 `int`、`double`、`bool`、`char`、`std::string`
2. 理解 C++ 是静态类型语言
3. 使用 `{}` 进行现代 C++ 初始化
4. 使用 `std::cout` 输出多个变量
5. 使用 `std::cin` 读取输入
6. 在 Xcode 中观察变量值如何变化
7. 初步理解输入失败时程序状态会变得不可靠

---

## 课前准备

创建本周目录和工程：

```text
CS102/
└── week02/
    └── Week02Types/
        └── Week02Types.xcodeproj
```

工程建议：

- Product Name：`Week02Types`
- Language：C++
- 文件：`main.cpp`

本周可以从空工程开始，也可以复制 Week01 的基本结构后清空 `main.cpp`。

---

## 2 小时课堂流程

| 时间 | 环节 | 内容 |
|------|------|------|
| 0:00-0:10 | 复习 | `main()`、`std::cout`、断点 |
| 0:10-0:30 | 类型概念 | Python 动态类型 vs C++ 静态类型 |
| 0:30-0:50 | 教师示范 | 角色属性卡变量 |
| 0:50-1:10 | 学生接手 | 修改属性、添加新变量 |
| 1:10-1:30 | 输入输出 | 用 `std::cin` 创建角色 |
| 1:30-1:45 | 调试观察 | 变量面板、输入前后状态 |
| 1:45-1:55 | 常见错误 | 类型不匹配、输入失败、未初始化 |
| 1:55-2:00 | 复盘 | 类型为什么重要 |

---

## 一、从 Python 变量到 C++ 变量

### Python 中的写法

```python
level = 1
hp = 100
name = "Mira"
is_alive = True
```

Python 不要求我们写类型。解释器会在运行时管理对象类型。

### C++ 中的写法

```cpp
int level {1};
int hp {100};
std::string name {"Mira"};
bool isAlive {true};
```

C++ 要求变量创建时就有明确类型。

讲解重点：

- `int`：整数
- `double`：小数
- `bool`：真假
- `char`：单个字符
- `std::string`：字符串

现场追问：

- “角色等级适合用小数吗？”
- “角色名字能用 `int` 吗？”
- “`isAlive` 为什么适合用 `bool`？”

---

## 二、现代 C++ 初始化

推荐使用花括号初始化：

```cpp
int level {1};
double speed {3.5};
bool hasKey {false};
char rank {'A'};
std::string name {"Mira"};
```

为什么推荐：

- 写法统一
- 可以减少一些意外类型转换
- 一眼能看出变量初始值

不需要第一节就深入所有初始化规则，只要建立风格。

可以简单提一句：

```cpp
int level = 1;   // 也常见
int hp(100);     // 也能用
int mp {50};     // 本课程优先使用
```

---

## 三、教师示范：角色属性卡

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name {"Mira"};
    int level {1};
    int hp {100};
    int attack {12};
    double speed {3.5};
    bool isAlive {true};
    char rank {'C'};

    std::cout << "===== Character Card =====" << std::endl;
    std::cout << "Name  : " << name << std::endl;
    std::cout << "Level : " << level << std::endl;
    std::cout << "HP    : " << hp << std::endl;
    std::cout << "Attack: " << attack << std::endl;
    std::cout << "Speed : " << speed << std::endl;
    std::cout << "Alive : " << isAlive << std::endl;
    std::cout << "Rank  : " << rank << std::endl;

    return 0;
}
```

### 讲解输出结果

`bool` 输出时通常显示：

```text
1
```

而不是：

```text
true
```

如果希望显示 `true/false`：

```cpp
std::cout << std::boolalpha;
```

改进版：

```cpp
std::cout << std::boolalpha;
std::cout << "Alive : " << isAlive << std::endl;
```

---

## 四、学生接手练习

让学生做三步：

1. 修改角色名、等级、生命值
2. 添加一个变量 `gold`
3. 添加一个变量 `hasMagicKey`

目标代码方向：

```cpp
int gold {30};
bool hasMagicKey {false};

std::cout << "Gold  : " << gold << std::endl;
std::cout << "Magic Key: " << std::boolalpha << hasMagicKey << std::endl;
```

现场追问：

- “金币为什么用 `int` 而不是 `double`？”
- “钥匙状态为什么用 `bool`？”
- “如果我把 `name` 改成 `int`，会发生什么？”

---

## 五、输入：让玩家创建角色

### 教师示范代码

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name {};
    int level {};
    int hp {};

    std::cout << "Enter character name: ";
    std::cin >> name;

    std::cout << "Enter level: ";
    std::cin >> level;

    std::cout << "Enter hp: ";
    std::cin >> hp;

    std::cout << std::endl;
    std::cout << "===== Character Card =====" << std::endl;
    std::cout << "Name : " << name << std::endl;
    std::cout << "Level: " << level << std::endl;
    std::cout << "HP   : " << hp << std::endl;

    return 0;
}
```

### 讲解 `std::cin`

`std::cin >> name;` 的直觉：

```text
从控制台读取一个输入，放进 name 变量。
```

注意：这里读取名字时，如果输入 `Mira Chen`，`name` 只会得到 `Mira`。带空格的整行输入以后再讲 `std::getline`。

---

## 六、Xcode 调试观察

### 观察目标

让学生看到变量在输入前后如何变化。

### 操作步骤

1. 在 `std::string name {};` 后设置断点
2. Run
3. 查看变量面板中 `name`、`level`、`hp` 的初始状态
4. Step Over 到 `std::cin >> name;`
5. 在控制台输入名字
6. 再次查看变量面板
7. 对 `level` 和 `hp` 重复观察

### 输入失败观察

让学生在 `Enter level:` 时输入：

```text
abc
```

观察：

- 程序没有得到正常整数
- 后续输入可能也不正常
- `std::cin` 进入失败状态

本节不需要深入清理输入流，只要建立直觉：

> 输入不是永远可信，程序需要处理错误。

---

## 七、常见错误与讲解

### 1. 类型不匹配

```cpp
int level {"one"};
```

解释：`level` 是整数，不能用文字 `"one"` 初始化。

### 2. 字符和字符串混淆

```cpp
char rank {"A"};     // 错
char rank {'A'};     // 对
```

解释：

- `'A'` 是单个字符
- `"A"` 是字符串

### 3. 忘记包含 `<string>`

```cpp
std::string name {"Mira"};
```

需要：

```cpp
#include <string>
```

### 4. 把输入当作永远正确

解释：玩家可能输入任何东西。后面做游戏系统时，输入验证会非常重要。

---

## 八、系统连接：类型是内存解释方式

先给直觉，不深入二进制：

```text
同样是一块内存，解释为 int、double、char，意义会不同。
```

类型告诉编译器：

- 这份数据占多大空间
- 可以做哪些操作
- 如何输出和计算
- 哪些错误可以提前发现

把这个概念埋下，为 Week05 地址和内存布局做准备。

---

## 九、AI 辅助创作任务

让学生提出一个角色卡扩展，例如：

- 添加职业
- 添加是否拥有宠物
- 添加移动速度
- 添加难度等级

可生成代码：

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name {};
    std::string job {};
    int level {};
    int hp {};
    double speed {};
    bool hasPet {};

    std::cout << "Name: ";
    std::cin >> name;

    std::cout << "Job: ";
    std::cin >> job;

    std::cout << "Level: ";
    std::cin >> level;

    std::cout << "HP: ";
    std::cin >> hp;

    std::cout << "Speed: ";
    std::cin >> speed;

    std::cout << "Has pet? Enter 1 for yes, 0 for no: ";
    std::cin >> hasPet;

    std::cout << std::boolalpha;
    std::cout << "\n===== Character Card =====\n";
    std::cout << "Name : " << name << '\n';
    std::cout << "Job  : " << job << '\n';
    std::cout << "Level: " << level << '\n';
    std::cout << "HP   : " << hp << '\n';
    std::cout << "Speed: " << speed << '\n';
    std::cout << "Pet  : " << hasPet << '\n';

    return 0;
}
```

---

## 十、学习报告模板

```markdown
# CS102 Week 02 学习报告

## 1. 本周核心知识

- C++ 变量需要明确类型
- 常见类型：`int`、`double`、`bool`、`char`、`std::string`
- 推荐使用 `{}` 初始化
- `std::cin` 可以读取输入

## 2. 类型对照表

| 数据 | 推荐类型 | 原因 |
|------|----------|------|
| 等级 | `int` | 整数 |
| 速度 | `double` | 可能有小数 |
| 是否存活 | `bool` | 只有真假 |
| 评级 | `char` | 单个字符 |
| 名字 | `std::string` | 文本 |

## 3. Xcode 调试观察

- 输入前变量是什么状态：
- 输入后变量如何变化：
- 输入错误内容时发生了什么：

## 4. 本周代码

```cpp
// 粘贴角色属性卡代码
```

## 5. 我的理解

为什么 C++ 要求变量有明确类型？
```

---

## 十一、教师检查清单

本节课结束前，确认学生能做到：

- 能创建至少 5 种不同类型的变量
- 能解释 `bool` 适合表示真假状态
- 能使用 `std::cout` 输出多个变量
- 能使用 `std::cin` 读取至少 3 个输入
- 能在 Xcode 变量面板中观察变量变化
- 能说出一次输入失败会造成什么问题
