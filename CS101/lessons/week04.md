# 第 4 周：重复的力量

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块二：核心语法 |
| **课时** | 1.5 小时 |
| **关键词** | while 循环、break、continue、无限循环 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解为什么需要循环
2. 使用 while 循环重复执行代码
3. 使用 break 提前退出循环
4. 使用 continue 跳过当前迭代
5. 避免和处理无限循环

---

## 复习回顾（5 分钟）

上节课我们学习了：
- 布尔值和比较运算符
- if-elif-else 条件语句
- 逻辑运算符 and、or、not

**快速提问：**
- `if` 和 `elif` 有什么区别？
- `and` 和 `or` 的区别是什么？

---

## 教学内容

### 第一部分：为什么需要循环？（10 分钟）

#### 1.1 重复任务的困境

假设我们要打印 1 到 10：

```python
# 不用循环的做法 😫
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

如果要打印 1 到 1000 呢？要写 1000 行代码！

#### 1.2 循环的威力

```python
# 用循环 😎
count = 1
while count <= 10:
    print(count)
    count = count + 1
```

只需要 4 行代码，就能完成重复 10 次、100 次、1000 次的任务！

**循环就是让计算机重复执行某段代码。**

---

### 第二部分：while 循环详解（35 分钟）

#### 2.1 while 循环语法

```python
while 条件:
    # 条件为 True 时重复执行的代码
    # 代码块需要缩进
```

**执行流程：**

```
┌──────────────────────────────┐
│         开始                  │
│           ↓                  │
│     ┌──────────┐             │
│     │ 条件判断  │←──────┐     │
│     └──────────┘      │     │
│      ↙      ↘         │     │
│   True      False     │     │
│    ↓          ↓       │     │
│ 执行代码    结束循环   │     │
│    ↓                  │     │
│    └──────────────────┘     │
└──────────────────────────────┘
```

#### 2.2 基本示例

```python
# 示例1：倒计时
count = 5
while count > 0:
    print(count)
    count = count - 1
print("发射！🚀")
```

输出：
```
5
4
3
2
1
发射！🚀
```

```python
# 示例2：计算 1 到 100 的和
total = 0
num = 1

while num <= 100:
    total = total + num
    num = num + 1

print(f"1到100的和是：{total}")  # 5050
```

#### 2.3 循环变量的更新

**重要：** 循环条件中的变量必须在循环体内被修改，否则会造成无限循环！

```python
# ❌ 错误：无限循环！
count = 1
while count <= 10:
    print(count)
    # 忘记更新 count 了！count 永远是 1，永远 <= 10

# ✅ 正确
count = 1
while count <= 10:
    print(count)
    count = count + 1  # 每次循环后 count 增加 1
```

#### 2.4 简写运算符

```python
count = 1

# 这两种写法是等价的
count = count + 1
count += 1

# 其他简写
count -= 1   # count = count - 1
count *= 2   # count = count * 2
count /= 2   # count = count / 2
```

#### 2.5 用户控制的循环

```python
# 用户决定何时退出
answer = "y"
while answer == "y":
    name = input("请输入名字：")
    print(f"你好，{name}！")
    answer = input("继续吗？(y/n)：")

print("程序结束")
```

---

### 第三部分：循环控制——break 与 continue（25 分钟）

#### 3.1 break：立即退出循环

`break` 会立即终止整个循环，跳到循环后面的代码。

```python
# 找到第一个能被7整除的数就停止
num = 1
while num <= 100:
    if num % 7 == 0:
        print(f"找到了：{num}")
        break  # 立即退出循环
    num += 1

print("循环结束")
```

输出：
```
找到了：7
循环结束
```

**实际应用：用户登录**

```python
# 密码验证（最多尝试3次）
correct_password = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("请输入密码：")
    attempts += 1
    
    if password == correct_password:
        print("✅ 登录成功！")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ 密码错误，还剩 {remaining} 次机会")

if password != correct_password:
    print("❌ 登录失败，账号已锁定")
```

#### 3.2 continue：跳过本次迭代

`continue` 跳过当前这一次循环的剩余代码，直接进入下一次循环。

```python
# 打印 1-10 中的奇数
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # 如果是偶数
        continue       # 跳过，不打印
    print(num)
```

输出：
```
1
3
5
7
9
```

**break vs continue：**

```
break：    "我不玩了，直接退出"
continue： "这一次跳过，继续下一次"
```

```python
# 对比示例
num = 0
print("使用 break：")
while num < 5:
    num += 1
    if num == 3:
        break
    print(num)
# 输出：1, 2

num = 0
print("\n使用 continue：")
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
# 输出：1, 2, 4, 5
```

#### 3.3 while-else 结构

Python 的 while 循环可以有 else 子句，当循环正常结束（不是被 break 终止）时执行。

```python
# 查找数字
target = 7
num = 1

while num <= 10:
    if num == target:
        print(f"找到了 {target}！")
        break
    num += 1
else:
    # 只有循环正常结束（没有 break）才执行
    print(f"没找到 {target}")
```

---

### 第四部分：课堂练习（20 分钟）

#### 练习：猜数字游戏 v1

创建一个猜数字游戏：
- 程序随机生成一个 1-100 的数字
- 用户不断猜测
- 程序提示"太大了"或"太小了"
- 猜对了显示恭喜并告诉用户猜了几次

**示例代码框架：**

```python
import random

# 猜数字游戏 v1
print("=" * 40)
print("        猜数字游戏")
print("=" * 40)
print("我想了一个 1-100 之间的数字，猜猜看！")
print()

# 生成随机数
secret = random.randint(1, 100)
guess_count = 0

# 游戏循环
while True:
    guess = int(input("请输入你的猜测："))
    guess_count += 1
    
    if guess == secret:
        print(f"\n🎉 恭喜你猜对了！")
        print(f"答案是 {secret}")
        print(f"你总共猜了 {guess_count} 次")
        break
    elif guess < secret:
        print("📈 太小了，再大一点！")
    else:
        print("📉 太大了，再小一点！")

print("\n游戏结束，感谢游玩！")
```

**扩展挑战：**
- 限制猜测次数（比如最多 10 次）
- 添加难度选择（不同的数字范围）
- 猜测次数少于5次给予特别表扬

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| while 循环 | 条件为 True 时重复执行代码 |
| 循环变量 | 必须在循环体内更新，否则无限循环 |
| break | 立即退出整个循环 |
| continue | 跳过本次迭代，继续下一次 |
| += | 简写运算符，count += 1 等于 count = count + 1 |

**重要提醒：**
- 循环条件最终必须变成 False，否则无限循环
- 遇到无限循环可以按 Ctrl+C 强制停止程序

---

## 参考资料

### 官方文档
- [Python while 语句](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-while-statement)
- [Python break 和 continue](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [random 模块](https://docs.python.org/zh-cn/3/library/random.html)

### 视频教程
- [Python 循环详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python while 循环 - 菜鸟教程](https://www.runoob.com/python3/python3-while-loop.html)

### 在线练习
- [Python Tutor - 可视化循环执行](https://pythontutor.com/)
- [Codecademy Python 循环](https://www.codecademy.com/learn/learn-python-3)
- [LeetCode 循环相关题目](https://leetcode.cn/tag/simulation/)

### 拓展阅读
- [如何避免无限循环](https://realpython.com/python-while-loop/)
- [Python 循环最佳实践](https://www.geeksforgeeks.org/python-while-loop/)
