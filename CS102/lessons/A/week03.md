# Week 03: 表达式、控制流和函数

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属部分** | CS102A：现代 C++ 编程与内存模型 |
| **课时** | 2 小时，一对一现场授课 |
| **主环境** | Xcode IDE 工程 |
| **关键词** | 表达式、`if`、`while`、`for`、函数、调用栈 |
| **系统连接** | 控制流决定程序执行路径，函数调用形成调用栈 |

---

## 教师导读

Week03 开始，学生会从“变量和输入输出”进入“程序逻辑”。这节课的主线是一个小型猜数字/战斗判断程序，用条件和循环表达游戏规则，再用函数把程序拆成更清楚的小块。

本节不要急着讲复杂算法。重点是让学生建立三个直觉：

1. 表达式会产生值
2. 控制流决定下一步执行哪一段代码
3. 函数调用会让程序暂时进入另一个小任务，完成后再回来

Xcode 里最重要的观察点是调用栈。学生应该第一次看到：程序停在函数内部时，调用栈能告诉我们“是谁调用了这个函数”。

---

## 本节课目标

完成本节课后，学生应该能够：

1. 使用比较表达式产生 `bool` 结果
2. 使用 `if` / `else if` / `else` 表达分支逻辑
3. 使用 `while` 表达重复直到条件不满足
4. 使用 `for` 表达固定次数重复
5. 定义和调用简单函数
6. 把较长程序拆成多个职责清楚的函数
7. 在 Xcode 中观察函数调用栈

---

## 课前准备

创建本周目录和工程：

```text
CS102/
└── week03/
    └── Week03FlowFunctions/
        └── Week03FlowFunctions.xcodeproj
```

本周工程只需要 `main.cpp`。如果学生想把函数拆到其他文件，可以作为扩展，不在本节强制。

---

## 2 小时课堂流程

| 时间 | 环节 | 内容 |
|------|------|------|
| 0:00-0:10 | 复习 | 类型、变量、输入输出 |
| 0:10-0:30 | 表达式和条件 | 比较、`bool`、`if` |
| 0:30-0:50 | 教师示范 | 战斗伤害判断 |
| 0:50-1:10 | 循环 | 猜数字主循环 |
| 1:10-1:30 | 函数 | 拆出 `print_hint`、`is_correct` |
| 1:30-1:45 | Xcode 调试 | Step Into、调用栈 |
| 1:45-1:55 | 学生扩展 | 限制次数、胜负提示 |
| 1:55-2:00 | 复盘 | 控制流和函数的意义 |

---

## 一、表达式：会产生值的代码片段

先从学生熟悉的判断开始：

```cpp
int hp {80};
bool isAlive {hp > 0};
```

`hp > 0` 是一个表达式，它的结果是 `true` 或 `false`。

常见比较：

```cpp
level >= 5
hp == 0
gold < price
name != "Boss"
```

注意讲清楚：

- `=` 是赋值
- `==` 是比较是否相等

现场追问：

- “`hp = 0` 和 `hp == 0` 有什么区别？”
- “`gold < price` 的结果是什么类型？”
- “如果 `hp` 是 0，`hp > 0` 的结果是什么？”

---

## 二、条件判断：让程序做选择

### 教师示范：生命值状态

```cpp
#include <iostream>

int main() {
    int hp {35};

    if (hp <= 0) {
        std::cout << "角色已经倒下。" << std::endl;
    } else if (hp < 30) {
        std::cout << "角色生命值很低。" << std::endl;
    } else {
        std::cout << "角色还能继续战斗。" << std::endl;
    }

    return 0;
}
```

讲解顺序：

1. `if` 后面的条件必须能判断真假
2. 满足第一个条件就执行对应代码块
3. `else if` 是继续检查另一个条件
4. `else` 是前面都不满足时执行

学生接手：

- 修改 `hp` 为 `100`
- 修改 `hp` 为 `20`
- 修改 `hp` 为 `0`
- 每次运行前先猜输出结果

---

## 三、循环：重复做一件事

### `while`：条件满足就继续

```cpp
#include <iostream>

int main() {
    int count {3};

    while (count > 0) {
        std::cout << "倒计时：" << count << std::endl;
        count = count - 1;
    }

    std::cout << "开始！" << std::endl;
    return 0;
}
```

讲解要点：

- 先判断条件
- 条件为真，执行循环体
- 执行完再回到条件
- 如果变量不更新，可能无限循环

### `for`：固定次数循环

```cpp
for (int i {1}; i <= 5; ++i) {
    std::cout << "第 " << i << " 次训练" << std::endl;
}
```

暂时把 `++i` 解释为 “让 i 增加 1”。深入差异以后再讲。

现场追问：

- “`while` 适合什么情况？”
- “`for` 适合什么情况？”
- “如果忘记 `count = count - 1` 会怎样？”

---

## 四、项目实践：猜数字游戏 v1

### 第一版：全部写在 `main`

```cpp
#include <iostream>

int main() {
    int secret {7};
    int guess {};

    std::cout << "猜一个 1 到 10 的数字: ";

    while (true) {
        std::cin >> guess;

        if (guess == secret) {
            std::cout << "猜对了！" << std::endl;
            break;
        } else if (guess < secret) {
            std::cout << "太小了，再猜: ";
        } else {
            std::cout << "太大了，再猜: ";
        }
    }

    return 0;
}
```

讲解：

- `while (true)` 表示一直循环
- `break` 表示提前退出循环
- 每次输入后进行一次判断

这段代码足够展示控制流，但 `main` 开始变长。接下来引入函数。

---

## 五、函数：给一段逻辑起名字

### 拆出提示函数

```cpp
#include <iostream>

void print_hint(int guess, int secret) {
    if (guess < secret) {
        std::cout << "太小了，再猜: ";
    } else {
        std::cout << "太大了，再猜: ";
    }
}

int main() {
    int secret {7};
    int guess {};

    std::cout << "猜一个 1 到 10 的数字: ";

    while (true) {
        std::cin >> guess;

        if (guess == secret) {
            std::cout << "猜对了！" << std::endl;
            break;
        }

        print_hint(guess, secret);
    }

    return 0;
}
```

### 解释函数结构

```cpp
void print_hint(int guess, int secret)
```

- `void`：这个函数不返回结果
- `print_hint`：函数名
- `int guess, int secret`：参数

函数的价值：

- 给一段逻辑起名字
- 让 `main` 更像流程目录
- 让代码更容易调试和修改

---

## 六、进一步拆分：判断是否猜对

```cpp
#include <iostream>

bool is_correct(int guess, int secret) {
    return guess == secret;
}

void print_hint(int guess, int secret) {
    if (guess < secret) {
        std::cout << "太小了，再猜: ";
    } else {
        std::cout << "太大了，再猜: ";
    }
}

int main() {
    int secret {7};
    int guess {};

    std::cout << "猜一个 1 到 10 的数字: ";

    while (true) {
        std::cin >> guess;

        if (is_correct(guess, secret)) {
            std::cout << "猜对了！" << std::endl;
            break;
        }

        print_hint(guess, secret);
    }

    return 0;
}
```

讲解：

- `is_correct` 返回 `bool`
- 函数名像一个问题
- `if (is_correct(...))` 读起来接近自然语言

现场追问：

- “哪个函数负责判断？”
- “哪个函数负责输出提示？”
- “`main` 现在更清楚了吗？为什么？”

---

## 七、Xcode 调试观察：Step Into 和调用栈

### 观察目标

让学生看到函数调用不是“跳走消失”，而是调用栈里多了一层。

### 操作步骤

1. 在 `if (is_correct(guess, secret))` 设置断点
2. Run，输入一个数字
3. 程序停在断点
4. 使用 Step Into 进入 `is_correct`
5. 查看调用栈：
   - 当前在 `is_correct`
   - 下面能看到 `main`
6. Step Out 回到 `main`
7. 对 `print_hint` 重复一次

### 讲解调用栈

调用栈可以理解为：

```text
程序正在做的小任务列表。
最上面是当前正在执行的函数。
下面是它从哪里被叫来的。
```

现场追问：

- “现在调用栈最上面是什么函数？”
- “`is_correct` 是谁调用的？”
- “Step Into 和 Step Over 有什么区别？”

---

## 八、学生扩展任务

让学生添加“最多猜 3 次”：

```cpp
#include <iostream>

bool is_correct(int guess, int secret) {
    return guess == secret;
}

void print_hint(int guess, int secret) {
    if (guess < secret) {
        std::cout << "太小了。" << std::endl;
    } else {
        std::cout << "太大了。" << std::endl;
    }
}

int main() {
    int secret {7};
    int guess {};
    int attempts {0};
    int maxAttempts {3};

    while (attempts < maxAttempts) {
        std::cout << "请输入你的猜测: ";
        std::cin >> guess;
        attempts = attempts + 1;

        if (is_correct(guess, secret)) {
            std::cout << "猜对了！你用了 " << attempts << " 次。" << std::endl;
            return 0;
        }

        print_hint(guess, secret);
    }

    std::cout << "次数用完了，答案是 " << secret << "。" << std::endl;
    return 0;
}
```

教师引导：

- 这是第一个比较完整的 C++ 小游戏循环
- 它有状态：`attempts`
- 它有规则：最多 3 次
- 它有函数：判断和提示

---

## 九、常见错误与讲解

### 1. 把 `=` 当成 `==`

```cpp
if (guess = secret) {
}
```

解释：这是赋值，不是比较。C++ 可能允许某些赋值表达式出现在条件里，所以尤其危险。

### 2. 无限循环

```cpp
while (attempts < maxAttempts) {
    std::cin >> guess;
    // 忘记 attempts = attempts + 1;
}
```

解释：循环条件永远不变，就可能一直循环。

### 3. 函数先使用后定义

如果把 `is_correct` 放在 `main` 后面，暂时会报错。以后可以用函数声明解决。

### 4. 函数职责不清

一个函数既判断、又输入、又输出、又修改状态，会变得难读。先让函数做一件清楚的事。

---

## 十、系统/设计连接

控制流是程序的“路线图”，函数是程序的“路标”。

在游戏里：

- `if` 用于判断胜负、碰撞、血量、状态
- `while` 用于游戏主循环
- `for` 用于遍历敌人、道具、地图格子
- 函数用于把复杂游戏逻辑拆成小块

这节课为之后的“模块”和“源码分析”打基础。以后读大型项目时，不会逐行从头看到尾，而是先看函数和模块如何组织。

---

## 十一、AI 辅助创作任务

让学生选一个小扩展：

- 加入难度选择：简单答案范围 1-10，困难 1-100
- 加入生命值：猜错扣血
- 加入评分：猜得越少分越高

示例方向：生命值版本。

```cpp
int hp {3};

while (hp > 0) {
    std::cout << "HP: " << hp << ", guess: ";
    std::cin >> guess;

    if (is_correct(guess, secret)) {
        std::cout << "胜利！" << std::endl;
        return 0;
    }

    hp = hp - 1;
    print_hint(guess, secret);
}

std::cout << "失败，答案是 " << secret << "。" << std::endl;
```

---

## 十二、学习报告模板

```markdown
# CS102 Week 03 学习报告

## 1. 本周核心知识

- 表达式会产生值
- `if` 用于分支判断
- `while` 和 `for` 用于循环
- 函数可以把程序拆成小块
- 调用栈可以显示函数调用关系

## 2. 控制流总结

| 结构 | 用途 | 本周例子 |
|------|------|----------|
| `if` | 选择路径 | 判断猜大/猜小 |
| `while` | 不确定次数循环 | 一直猜到结束 |
| `for` | 固定次数循环 | 训练 5 次 |
| 函数 | 命名一段逻辑 | `is_correct` |

## 3. Xcode 调试观察

- 我 Step Into 进入了哪个函数：
- 调用栈显示了什么：
- Step Over 和 Step Into 的区别：

## 4. 本周代码

```cpp
// 粘贴猜数字游戏代码
```

## 5. 我的理解

为什么函数能让程序更容易读？
```

---

## 十三、教师检查清单

本节课结束前，确认学生能做到：

- 能解释 `=` 和 `==` 的区别
- 能写出一个 `if-else`
- 能写出一个 `while` 循环
- 能解释为什么会发生无限循环
- 能定义一个返回 `bool` 的函数
- 能在 Xcode 中 Step Into 一个函数
- 能在调用栈中指出当前函数和调用者
