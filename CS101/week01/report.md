# CS101 Week01 学习报告

**学习者**: Amos  
**日期**: 2026年3月21日

---

## 今日学习内容

### 1. Python 语言介绍

- **Python** 是一门简洁、易读的编程语言，适合作为第一门语言学习
- 设计哲学：优雅、简单、可读
- 应用领域：游戏开发、人工智能、数据分析、网站开发

### 2. 变量 (Variable)

**核心概念**: 变量就像"贴了标签的盒子"，用来存储数据

```python
name = "Amos"    # 字符串 (str)
age = 16         # 整数 (int)
height = 1.75    # 浮点数 (float)
```

**命名规则**:
- 只能包含字母、数字、下划线
- 不能以数字开头
- 不能使用 Python 保留字（如 `class`, `if`）
- 建议使用有意义的名字

### 3. 数据类型

| 类型 | 英文 | 例子 | 说明 |
|------|------|------|------|
| 字符串 | str | `"Amos"` | 文字，用引号包裹 |
| 整数 | int | `16` | 整数 |
| 浮点数 | float | `1.75` | 小数 |
| 布尔值 | bool | `True/False` | 是/否 |

**重要发现**: 不同类型运算结果不同！

```python
age = 16
age_str = "16"

print(age + 1)      # 17 (整数加法)
print(age_str + "1") # "161" (字符串拼接)
```

### 4. 数据结构入门

**列表 (List)**: 有序集合，用编号访问

```python
hobbies = ["玩游戏", "编程", "画画"]
print(hobbies[0])  # "玩游戏" (编号从 0 开始)
```

**字典 (Dictionary)**: 键值对，用名字访问

```python
hero = {"name": "Amos", "hp": 100}
print(hero["name"])  # "Amos"
```

### 5. 计算机基础

**输入-处理-输出模型 (IPO)**:

```
输入 → 处理 → 输出
(键盘)  (CPU)  (屏幕)
```

**GPU 与图形计算**:
- GPU 擅长并行计算百万像素
- 图形计算 = 算出屏幕每个像素的颜色
- 游戏渲染依赖 GPU 的高性能并行处理

---

## 实践练习

### 创建的文件

| 文件 | 说明 |
|------|------|
| `hello.py` | 第一个 Python 程序，学习 print 和变量 |
| `profile.py` | 个人信息卡片，练习变量和数据类型 |

### 运行命令

```bash
python3 /Users/roger/cs/CS101/week01/hello.py
python3 /Users/roger/cs/CS101/week01/profile.py
```

---

## 新学英文词汇

| 中文 | 英文 |
|------|------|
| 变量 | Variable |
| 变量名 | Variable Name |
| 赋值 | Assign |
| 值 | Value |
| 类型 | Type |
| 字符串 | String |
| 整数 | Integer |
| 列表 | List |
| 字典 | Dictionary |

---

## 下次学习预告

- 条件语句 (`if`/`else`)
- 用户输入 (`input()`)
- 制作一个简单的交互程序

---

**总结**: 今天完成了 Python 入门，理解了变量的概念，学会了使用 `print()` 和 `type()`，动手写了两个小程序。良好的开端！
