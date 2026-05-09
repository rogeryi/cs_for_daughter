# Week 28: Godot 案例：Node、SceneTree、Signal、Resource

## 课程信息

| 项目 | 内容 |
|------|------|
| **所属部分** | CS102B：标准库、并发与软件系统设计 |
| **关键词** | Godot、Node、SceneTree、Signal、Resource、源码分析 |
| **系统连接** | 游戏引擎如何组织对象、事件和资源 |

## 学习目标

1. 理解 Godot 的 Node 和 SceneTree 设计直觉
2. 理解 Signal 作为事件解耦机制
3. 理解 Resource 作为可复用资源概念
4. 从文档和少量源码片段中提取核心设计

## 核心概念

- Node 是游戏对象和功能节点的基础抽象
- SceneTree 通过父子关系组织场景
- Signal 让对象不用直接知道彼此也能通信
- Resource 让数据和资源可以复用、保存和加载

## 课堂实践

- 画出一个简单平台跳跃游戏的节点树
- 用 C++ 伪代码实现简化 signal 机制
- 讨论 Resource 和普通对象的区别

## 系统/设计连接

Godot 是观察复杂软件设计的好案例。学习重点不是记住源码细节，而是理解大型系统如何用少数核心抽象管理复杂度。

## 学习报告提示

- SceneTree 为什么适合描述游戏场景？
- Signal 解决了什么耦合问题？
- Resource 和 Node 的职责有什么不同？
