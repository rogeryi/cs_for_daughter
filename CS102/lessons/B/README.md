# CS102B: 标准库、并发与软件系统设计

CS102B 是 CS102 的下半部分，共 15 节课。目标是让学生理解标准库容器背后的数据结构直觉，掌握基础并发 API，并开始分析复杂软件系统的设计。

本部分继续使用 Xcode IDE。调试器的重点从“观察变量”扩展到“观察调用链、线程状态、线程调用栈、资源表变化和模块之间的数据流”。

---

## 课程主线

```
源码分析方法
  -> 容器选择
  -> 树、哈希表、队列、优先队列
  -> 复杂度和性能直觉
  -> 文件、时间、资源加载
  -> 线程与同步
  -> 模块、接口、依赖方向
  -> Godot 核心设计案例
  -> mini scene tree 期末项目
```

---

## 课程列表

| 课次 | 主题 |
|------|------|
| Week 16 | 如何读源码：入口、模块、接口、调用链 |
| Week 17 | 容器选择：`vector`、`deque`、`list` |
| Week 18 | 有序容器：`map`、`set` 和树结构直觉 |
| Week 19 | 无序容器：哈希表与资源查找 |
| Week 20 | `stack`、`queue`、`priority_queue` 与任务组织 |
| Week 21 | 复杂度、缓存和性能直觉 |
| Week 22 | 文件系统与资源加载 |
| Week 23 | 时间、计时和游戏循环 |
| Week 24 | 进程、线程、`thread` 和 `jthread` |
| Week 25 | `mutex`、`lock_guard`、`condition_variable` |
| Week 26 | 数据竞争、死锁和线程安全队列 |
| Week 27 | 软件架构：模块、接口、依赖方向 |
| Week 28 | Godot 案例：Node、SceneTree、Signal、Resource |
| Week 29 | 期末项目：mini scene tree / 小型 2D 框架 |
| Week 30 | 项目展示、源码分析报告和重构讨论 |
