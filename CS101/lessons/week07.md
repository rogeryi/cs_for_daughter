# 第 7 周：综合练习课

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属模块** | 模块二：核心语法 |
| **课时** | 1.5 小时 |
| **关键词** | 列表嵌套、字典嵌套、复杂数据结构、综合应用 |

---

## 学习目标

完成本节课后，学生将能够：

1. 理解并使用列表的嵌套（二维列表）
2. 理解并使用字典的嵌套
3. 组合使用列表和字典构建复杂数据结构
4. 设计合适的数据结构来解决实际问题

---

## 复习回顾（5 分钟）

前几周我们学习了：
- 列表：有序的数据集合，用索引访问
- 字典：键值对集合，用键访问
- for 循环：遍历列表和字典

**快速提问：**
- 列表和字典分别用什么访问元素？
- 如何遍历字典的键和值？

---

## 教学内容

### 第一部分：列表与字典的嵌套（30 分钟）

#### 1.1 列表中的列表（二维列表）

列表的元素可以是另一个列表，形成"列表中的列表"。

```python
# 二维列表：表示一个 3x3 的棋盘
board = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["O", "X", "O"]
]

# 访问元素：board[行][列]
print(board[0][0])  # O（第1行第1列）
print(board[1][2])  # X（第2行第3列）
print(board[2][1])  # X（第3行第2列）
```

```
board 的结构：
       列0    列1    列2
      ┌─────┬─────┬─────┐
行0   │  O  │  X  │  O  │  board[0]
      ├─────┼─────┼─────┤
行1   │  X  │  O  │  X  │  board[1]
      ├─────┼─────┼─────┤
行2   │  O  │  X  │  O  │  board[2]
      └─────┴─────┴─────┘
```

**遍历二维列表：**

```python
# 打印棋盘
for row in board:
    for cell in row:
        print(cell, end=" ")
    print()  # 换行

# 或者使用索引
for i in range(len(board)):
    for j in range(len(board[i])):
        print(f"board[{i}][{j}] = {board[i][j]}")
```

#### 1.2 字典中的字典

字典的值也可以是另一个字典。

```python
# 嵌套字典：存储多个学生的详细信息
students = {
    "小明": {
        "age": 16,
        "grade": "高一",
        "scores": {"语文": 90, "数学": 95, "英语": 88}
    },
    "小红": {
        "age": 17,
        "grade": "高二",
        "scores": {"语文": 92, "数学": 88, "英语": 95}
    }
}

# 访问嵌套数据
print(students["小明"]["age"])           # 16
print(students["小明"]["scores"]["数学"]) # 95
print(students["小红"]["grade"])         # 高二
```

**遍历嵌套字典：**

```python
for name, info in students.items():
    print(f"\n学生：{name}")
    print(f"  年龄：{info['age']}")
    print(f"  年级：{info['grade']}")
    print("  成绩：")
    for subject, score in info["scores"].items():
        print(f"    {subject}：{score}")
```

#### 1.3 列表中的字典

列表的元素可以是字典，常用于存储多条记录。

```python
# 列表中的字典：学生列表
students = [
    {"name": "小明", "age": 16, "score": 95},
    {"name": "小红", "age": 17, "score": 88},
    {"name": "小刚", "age": 16, "score": 92}
]

# 访问数据
print(students[0]["name"])  # 小明
print(students[1]["score"]) # 88

# 遍历
for student in students:
    print(f"{student['name']}: {student['score']}分")

# 添加新学生
students.append({"name": "小美", "age": 16, "score": 96})
```

#### 1.4 字典中的列表

字典的值可以是列表。

```python
# 字典中的列表：每个学生的多次考试成绩
scores = {
    "小明": [95, 88, 92, 90],
    "小红": [88, 92, 95, 91],
    "小刚": [76, 82, 85, 88]
}

# 访问数据
print(scores["小明"][0])  # 95（小明的第一次成绩）
print(scores["小红"][-1]) # 91（小红的最后一次成绩）

# 计算平均分
for name, score_list in scores.items():
    avg = sum(score_list) / len(score_list)
    print(f"{name}的平均分：{avg:.1f}")
```

---

### 第二部分：复杂数据结构设计（30 分钟）

#### 2.1 设计数据结构的思路

在设计数据结构时，思考以下问题：
1. 要存储什么信息？
2. 信息之间有什么关系？
3. 需要进行什么操作？（查找、遍历、添加、删除）

#### 2.2 示例：游戏角色系统

```python
# 游戏角色数据结构
character = {
    "name": "勇者",
    "level": 10,
    "hp": 100,
    "max_hp": 100,
    "attack": 25,
    "defense": 15,
    "skills": ["火球术", "治疗术", "闪避"],
    "inventory": [
        {"name": "生命药水", "type": "consumable", "effect": 50, "count": 3},
        {"name": "铁剑", "type": "weapon", "attack": 10, "count": 1}
    ],
    "equipment": {
        "weapon": "铁剑",
        "armor": "皮甲",
        "accessory": None
    }
}

# 显示角色信息
print(f"角色：{character['name']}")
print(f"等级：{character['level']}")
print(f"HP：{character['hp']}/{character['max_hp']}")
print(f"攻击：{character['attack']}")
print(f"防御：{character['defense']}")

print("\n技能列表：")
for skill in character['skills']:
    print(f"  - {skill}")

print("\n背包物品：")
for item in character['inventory']:
    print(f"  - {item['name']} x{item['count']}")
```

#### 2.3 示例：商品库存系统

```python
# 商品库存
inventory = {
    "水果": [
        {"name": "苹果", "price": 5.0, "stock": 100},
        {"name": "香蕉", "price": 3.0, "stock": 150},
        {"name": "橙子", "price": 4.5, "stock": 80}
    ],
    "饮料": [
        {"name": "可乐", "price": 3.5, "stock": 200},
        {"name": "雪碧", "price": 3.5, "stock": 180},
        {"name": "矿泉水", "price": 2.0, "stock": 300}
    ]
}

# 显示所有商品
for category, products in inventory.items():
    print(f"\n【{category}】")
    for product in products:
        print(f"  {product['name']}: ¥{product['price']}, 库存{product['stock']}")

# 查找商品
def find_product(name):
    for category, products in inventory.items():
        for product in products:
            if product['name'] == name:
                return product
    return None

apple = find_product("苹果")
if apple:
    print(f"\n找到商品：{apple['name']}, 价格：¥{apple['price']}")
```

---

### 第三部分：课堂练习（30 分钟）

#### 练习：学生成绩管理系统

创建一个学生成绩管理系统：
- 存储多个学生的信息（姓名、年龄、多科成绩）
- 可以添加新学生
- 可以查看所有学生信息
- 可以计算每个学生的平均分

**示例代码框架：**

```python
# 学生成绩管理系统
print("=" * 50)
print("          学生成绩管理系统")
print("=" * 50)

# 数据结构：列表中的字典
students = []

def add_student():
    """添加新学生"""
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    
    # 输入各科成绩
    scores = {}
    subjects = ["语文", "数学", "英语"]
    for subject in subjects:
        score = float(input(f"请输入{subject}成绩："))
        scores[subject] = score
    
    # 创建学生记录
    student = {
        "name": name,
        "age": age,
        "scores": scores
    }
    students.append(student)
    print(f"✅ 已添加学生：{name}")

def show_all_students():
    """显示所有学生"""
    if not students:
        print("\n📭 暂无学生记录")
        return
    
    print("\n" + "=" * 50)
    print("学生列表：")
    print("-" * 50)
    
    for i, student in enumerate(students, 1):
        # 计算平均分
        scores = student["scores"]
        avg = sum(scores.values()) / len(scores)
        
        print(f"\n{i}. {student['name']} (年龄：{student['age']})")
        print("   成绩：")
        for subject, score in scores.items():
            print(f"     {subject}: {score}")
        print(f"   平均分: {avg:.1f}")
    
    print("=" * 50)

def find_student():
    """查找学生"""
    name = input("请输入要查找的学生姓名：")
    for student in students:
        if student["name"] == name:
            print(f"\n找到学生：{student['name']}")
            print(f"年龄：{student['age']}")
            print("成绩：")
            for subject, score in student["scores"].items():
                print(f"  {subject}: {score}")
            return
    print(f"❌ 未找到学生：{name}")

# 主循环
while True:
    print("\n请选择操作：")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 查找学生")
    print("4. 退出")
    
    choice = input("请输入选项：")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        find_student()
    elif choice == "4":
        print("👋 再见！")
        break
    else:
        print("❌ 无效选项")
```

**扩展挑战：**
- 添加删除学生功能
- 添加修改成绩功能
- 按平均分排序显示
- 统计班级各科平均分

---

## 课堂小结

今天我们学习了：

| 概念 | 要点 |
|------|------|
| 二维列表 | 列表的元素是列表，用 list[i][j] 访问 |
| 嵌套字典 | 字典的值是字典，用 dict[key1][key2] 访问 |
| 列表中的字典 | 常用于存储多条记录 |
| 字典中的列表 | 常用于存储一对多关系 |
| 数据结构设计 | 根据数据关系和操作需求选择合适结构 |

**设计数据结构的原则：**
1. 明确要存储的信息
2. 分析信息之间的关系
3. 考虑要进行的操作
4. 选择合适的数据结构

---

## 参考资料

### 官方文档
- [Python 数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)
- [嵌套列表推导式](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#nested-list-comprehensions)

### 视频教程
- [Python 数据结构详解 - B站](https://www.bilibili.com/video/BV1ex411x7Em)
- [Python 二维列表 - 菜鸟教程](https://www.runoob.com/python3/python3-list.html)

### 在线练习
- [Python Tutor - 可视化嵌套结构](https://pythontutor.com/)
- [LeetCode 数组相关题目](https://leetcode.cn/tag/array/)
- [LeetCode 哈希表题目](https://leetcode.cn/tag/hash-table/)

### 拓展阅读
- [JSON 数据格式](https://www.json.org/json-zh.html) - 与字典非常相似
- [数据结构选择指南](https://realpython.com/python-data-structures/)
