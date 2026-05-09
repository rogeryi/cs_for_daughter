# Week 05: 地址、指针、数组和地址空间

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属部分** | CS102A：现代 C++ 编程与内存模型 |
| **课时** | 2 小时，一对一现场授课 |
| **主环境** | Xcode IDE 工程 |
| **关键词** | 地址、指针、数组、连续内存、地址空间、C 接口 |
| **系统连接** | 程序中的对象位于进程地址空间中，指针保存对象地址 |

---

## 教师导读

这是 CS102A 的第一节“真正底层”的课。学生会第一次正面看到地址和指针。目标不是让她马上熟练使用指针，而是建立正确心智模型：

1. 变量不仅有值，也有位置
2. 地址描述对象在程序地址空间中的位置
3. 指针是一种保存地址的变量
4. 数组元素通常连续存放
5. 现代 C++ 不把裸指针当作默认所有权工具

这一节要讲得慢。所有抽象概念都尽量用 Xcode 观察来支撑：变量面板、地址打印、Step Over、Memory Graph 的简单观察。不要把指针讲成“很可怕”，而要讲成“强大但需要规则”。

---

## 本节课目标

完成本节课后，学生应该能够：

1. 使用 `&` 取得变量地址
2. 理解地址和值的区别
3. 声明简单指针变量
4. 使用 `*` 通过指针访问对象
5. 观察数组元素的连续地址
6. 理解 C 风格数组和 `std::array` 的基本差异
7. 说明为什么现代 C++ 更偏好容器和智能指针
8. 初步理解 C 接口为什么经常使用指针和数组

---

## 课前准备

创建本周目录和工程：

```text
CS102/
└── week05/
    └── Week05Pointers/
        └── Week05Pointers.xcodeproj
```

本周建议只用 `main.cpp`。如果要观察编译产物或符号，可由教师/AI 使用命令行辅助。

---

## 2 小时课堂流程

| 时间 | 环节 | 内容 |
|------|------|------|
| 0:00-0:10 | 复习 | 引用、地址观察、函数参数 |
| 0:10-0:30 | 地址 | 变量的值和位置 |
| 0:30-0:55 | 指针 | 保存地址、解引用 |
| 0:55-1:15 | Xcode 观察 | 地址、变量面板、Step Over |
| 1:15-1:35 | 数组 | 连续内存、下标访问 |
| 1:35-1:50 | C 接口直觉 | 数组、指针、长度 |
| 1:50-1:58 | 学生扩展 | 小型背包数组观察 |
| 1:58-2:00 | 复盘 | 指针能做什么、不能滥用什么 |

---

## 一、变量有值，也有地址

### 教师示范

```cpp
#include <iostream>

int main() {
    int hp {80};

    std::cout << "hp value  : " << hp << std::endl;
    std::cout << "hp address: " << &hp << std::endl;

    return 0;
}
```

讲解：

- `hp` 表示变量的值
- `&hp` 表示变量的地址

可以用类比：

```text
值：房间里住的人
地址：房间号
变量名：我们给这个房间起的名字
```

但要提醒：类比只是帮助理解，不是内存的完整真相。

现场追问：

- “`hp` 和 `&hp` 输出的是同一种东西吗？”
- “地址看起来为什么像一串十六进制数字？”
- “如果重新运行，地址一定完全一样吗？”

---

## 二、地址空间的直觉

给学生一个简化图：

```text
进程地址空间（简化）

高地址
┌────────────────────┐
│      栈 stack       │  局部变量、函数调用
├────────────────────┤
│      ...           │
├────────────────────┤
│      堆 heap        │  动态分配对象
├────────────────────┤
│      全局数据       │
├────────────────────┤
│      程序代码       │
└────────────────────┘
低地址
```

本节只需要知道：

- 程序运行时像拥有一片自己的地址世界
- 变量和对象存在这片地址空间中
- 地址是程序用来定位对象的方式

不要深入虚拟内存、页表、内核，后续系统概念再慢慢补。

---

## 三、指针：保存地址的变量

### 教师示范

```cpp
#include <iostream>

int main() {
    int hp {80};
    int* hpPointer {&hp};

    std::cout << "hp value       : " << hp << std::endl;
    std::cout << "hp address     : " << &hp << std::endl;
    std::cout << "pointer value  : " << hpPointer << std::endl;
    std::cout << "pointed value  : " << *hpPointer << std::endl;

    return 0;
}
```

逐行讲解：

```cpp
int* hpPointer {&hp};
```

`hpPointer` 是一个指针，它保存 `hp` 的地址。

```cpp
*hpPointer
```

表示“沿着这个地址找到对象，然后访问它的值”。

可以用一句话：

```text
指针保存地址，解引用访问地址指向的对象。
```

---

## 四、通过指针修改对象

```cpp
#include <iostream>

int main() {
    int hp {80};
    int* hpPointer {&hp};

    *hpPointer = 50;

    std::cout << "hp: " << hp << std::endl;

    return 0;
}
```

输出：

```text
hp: 50
```

讲解：

- `hpPointer` 指向 `hp`
- `*hpPointer = 50` 修改的是 `hp` 本身

现场追问：

- “这行改的是指针变量，还是指针指向的对象？”
- “如果我写 `hpPointer = 50` 会是什么意思？会不会通过编译？”
- “引用和指针都能影响外部对象，它们有什么直觉区别？”

暂时回答：

- 引用像别名，使用时更像普通变量
- 指针是明确保存地址的变量，可以改变指向，也可能为空

---

## 五、空指针：没有指向任何对象

```cpp
int* target {nullptr};
```

`nullptr` 表示这个指针现在不指向任何对象。

重要规则：

```cpp
// 不要这样做
// std::cout << *target << std::endl;
```

解引用空指针是严重错误。

本节只讲原则：

> 使用指针前，必须知道它是否指向一个有效对象。

---

## 六、Xcode 调试观察：地址和值

### 观察目标

让学生在 IDE 中看到：

- `hp` 的值
- `&hp` 的地址
- `hpPointer` 保存的地址
- `*hpPointer` 访问到的值

### 操作步骤

1. 在 `int hp {80};` 后设置断点
2. Run
3. Step Over 到 `int* hpPointer {&hp};`
4. 查看变量面板：
   - `hp`
   - `hpPointer`
5. 继续 Step Over 到 `*hpPointer = 50;`
6. 观察 `hp` 变化
7. 在控制台输出地址进行对照

### 观察提示

变量面板有时不会直接显示所有你想看的表达式，可以添加 Watch 表达式：

```text
&hp
*hpPointer
```

如果学生看不清楚，教师可以用输出语句辅助观察。不要让工具细节遮蔽概念。

---

## 七、数组：连续排列的一组元素

### C 风格数组

```cpp
#include <iostream>

int main() {
    int damages[3] {10, 20, 30};

    std::cout << "damages[0]: " << damages[0] << std::endl;
    std::cout << "damages[1]: " << damages[1] << std::endl;
    std::cout << "damages[2]: " << damages[2] << std::endl;

    std::cout << "&damages[0]: " << &damages[0] << std::endl;
    std::cout << "&damages[1]: " << &damages[1] << std::endl;
    std::cout << "&damages[2]: " << &damages[2] << std::endl;

    return 0;
}
```

让学生观察地址差距。

如果 `int` 通常占 4 字节，相邻元素地址通常差 4。

注意表述：

- 具体地址每次运行可能不同
- 但同一个数组内部元素通常连续

---

## 八、`std::array`：现代 C++ 固定数组

```cpp
#include <array>
#include <iostream>

int main() {
    std::array<int, 3> damages {10, 20, 30};

    for (int damage : damages) {
        std::cout << damage << std::endl;
    }

    std::cout << "size: " << damages.size() << std::endl;
    std::cout << "&damages[0]: " << &damages[0] << std::endl;
    std::cout << "&damages[1]: " << &damages[1] << std::endl;

    return 0;
}
```

讲解：

- `std::array<int, 3>` 表示固定长度为 3 的整数数组
- 它比 C 风格数组更像现代 C++ 对象
- 有 `.size()`，更容易和标准库配合

本节不讲 `std::vector`，下一阶段再讲动态数组。

---

## 九、数组和指针的关系：只给直觉

演示：

```cpp
#include <iostream>

void print_first(int* values) {
    std::cout << values[0] << std::endl;
}

int main() {
    int damages[3] {10, 20, 30};
    print_first(damages);

    return 0;
}
```

讲解：

- C 风格接口里经常用指针表示“一段数据的开头”
- 但只有开头地址不够，通常还需要长度

更安全一点：

```cpp
void print_all(int* values, int count) {
    for (int i {0}; i < count; ++i) {
        std::cout << values[i] << std::endl;
    }
}
```

这就是很多 C API 的形状：

```text
数据起点 + 数据长度
```

连接 Godot/游戏引擎：

- 底层库常常需要传递一段内存
- C 接口经常用指针和长度表达数组
- 现代 C++ 会在上层用容器包装这些危险细节

---

## 十、学生接手练习：背包伤害数组

让学生创建一个技能伤害表：

```cpp
#include <array>
#include <iostream>

int main() {
    std::array<int, 4> skillDamages {8, 12, 20, 35};

    for (int i {0}; i < static_cast<int>(skillDamages.size()); ++i) {
        std::cout << "Skill " << i << " damage: "
                  << skillDamages[i] << std::endl;
    }

    std::cout << "Address of skillDamages[0]: " << &skillDamages[0] << std::endl;
    std::cout << "Address of skillDamages[1]: " << &skillDamages[1] << std::endl;

    return 0;
}
```

如果 `static_cast<int>` 暂时显得复杂，可以先告诉学生：

> `.size()` 返回的是无符号大小类型，和 `int` 比较时编译器可能提醒。这里先用转换让类型一致，后面会更系统地讲。

也可以简化成：

```cpp
for (std::size_t i {0}; i < skillDamages.size(); ++i) {
    std::cout << "Skill " << i << " damage: " << skillDamages[i] << std::endl;
}
```

但 `std::size_t` 本节只轻轻带过。

---

## 十一、常见错误与讲解

### 1. 把地址和值混淆

```cpp
int hp {80};
std::cout << hp;   // 值
std::cout << &hp;  // 地址
```

解释：值是对象里面的数据，地址是对象所在的位置。

### 2. 忘记指针类型

```cpp
int hp {80};
int hpPointer {&hp};  // 错
```

应该是：

```cpp
int* hpPointer {&hp};
```

### 3. 解引用空指针

```cpp
int* p {nullptr};
std::cout << *p << std::endl;  // 危险
```

解释：没有指向有效对象，不能访问。

### 4. 数组越界

```cpp
int values[3] {1, 2, 3};
std::cout << values[3] << std::endl;  // 错
```

解释：有效下标是 `0, 1, 2`。C++ 不一定每次都帮你安全拦住越界访问。

### 5. 以为指针就是所有权

解释：指针只是地址，不自动说明“谁负责销毁对象”。所有权问题以后用 RAII 和智能指针讲。

---

## 十二、系统/设计连接

指针和数组是理解底层系统、图形学和游戏引擎的重要基础。

以后会遇到：

- 顶点缓冲区：一大段连续顶点数据
- 纹理数据：一大段像素内存
- 音频数据：一大段采样数据
- C API：传入指针和长度
- 游戏对象容器：用连续内存提升遍历效率

但现代 C++ 的设计原则是：

```text
底层可以理解指针，上层尽量使用安全抽象。
```

也就是：

- 日常数据：优先 `std::array`、`std::vector`
- 所有权：以后优先 RAII、智能指针
- C 接口边界：理解指针，但小心封装

---

## 十三、Xcode 可视化观察任务

本节必须完成以下观察：

1. 设置断点，观察普通变量 `hp`
2. 添加 Watch：`&hp`
3. 创建指针 `hpPointer`
4. 添加 Watch：`hpPointer`
5. 添加 Watch：`*hpPointer`
6. 修改 `*hpPointer`，观察 `hp` 变化
7. 创建数组，观察 `&array[0]`、`&array[1]`、`&array[2]`
8. 解释相邻地址为什么有固定差距

现场追问：

- “`hpPointer` 自己也是变量吗？”
- “`hpPointer` 保存的是什么？”
- “`*hpPointer` 访问的是什么？”
- “数组元素为什么能用下标访问？”
- “为什么只有数组起点地址还不够，还需要长度？”

---

## 十四、命令行观察编译产物（可选）

如果学生好奇底层，可以由教师/AI 使用命令行观察：

- Debug 构建产物位置
- 可执行文件大小
- 是否包含调试符号
- 简单查看符号名

只报告现象，不要求学生掌握命令。

可讲一句：

> Xcode 的调试能力依赖编译时保留的调试信息。没有调试信息，程序仍能运行，但我们更难观察变量和调用栈。

---

## 十五、AI 辅助创作任务

让学生提出小扩展：

- 做一个技能伤害表
- 做一个怪物血量数组
- 做一个三格背包

示例：三格背包编号和地址观察。

```cpp
#include <array>
#include <iostream>
#include <string>

int main() {
    std::array<std::string, 3> inventory {"Potion", "Key", "Map"};

    for (std::size_t i {0}; i < inventory.size(); ++i) {
        std::cout << "Slot " << i << ": " << inventory[i]
                  << " at " << &inventory[i] << std::endl;
    }

    return 0;
}
```

讨论：

- `std::string` 元素也连续放在 `std::array` 中
- 但字符串对象内部可能还管理自己的字符数据
- 这为以后理解对象内存布局埋伏笔

---

## 十六、学习报告模板

```markdown
# CS102 Week 05 学习报告

## 1. 本周核心知识

- 变量有值，也有地址
- `&变量` 可以取得地址
- 指针保存地址
- `*指针` 可以访问指向的对象
- 数组元素通常连续存放

## 2. 地址和值

| 表达式 | 含义 |
|--------|------|
| `hp` | 变量的值 |
| `&hp` | 变量的地址 |
| `hpPointer` | 指针保存的地址 |
| `*hpPointer` | 指针指向对象的值 |

## 3. Xcode 调试观察

- `hp` 的值：
- `&hp` 的地址：
- `hpPointer` 保存的地址：
- `*hpPointer` 看到的值：
- 数组相邻元素地址差距：

## 4. 本周代码

```cpp
// 粘贴指针或数组观察代码
```

## 5. 我的理解

为什么现代 C++ 不建议到处使用裸指针管理对象？
```

---

## 十七、教师检查清单

本节课结束前，确认学生能做到：

- 能区分变量值和变量地址
- 能写出 `&hp`
- 能声明 `int*`
- 能解释 `*pointer` 的含义
- 能说明空指针不能解引用
- 能观察数组元素地址连续
- 能解释 C API 为什么常用“指针 + 长度”
- 能说出现代 C++ 更偏好容器和 RAII 的原因
