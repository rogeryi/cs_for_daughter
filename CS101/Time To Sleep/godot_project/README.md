# 🎮 Time To Sleep - Godot 项目

> **引擎：** Godot 4.6.2  
> **类型：** 类银河恶魔城 2D 横版动作游戏  
> **状态：** 原型开发中  

---

## 📁 项目结构

```
godot_project/
├── project.godot              # Godot 项目配置
├── icon.svg                   # 项目图标
├── README.md                  # 本文件
├── 导入指南.md                 # 精灵表导入详细教程
│
├── scenes/                    # 场景文件
│   ├── player.tscn           # 玩家场景
│   └── test_level.tscn       # 测试关卡
│
├── scripts/                   # 脚本文件
│   └── player.gd             # 玩家控制脚本
│
└── assets/                    # 资源文件
    ├── sprites/              # 精灵表（需要您添加）
    │   ├── player_idle.png   ← 待机动画精灵表
    │   ├── player_run.png    ← 移动动画精灵表
    │   └── player_jump.png   ← 跳跃动画精灵表
    └── animations/           # 动画资源
```

---

## 🚀 快速开始

### 1. 安装 Godot

```bash
# macOS（已安装）
godot --version
# 应显示：4.6.2.stable
```

### 2. 打开项目

```bash
cd "/Users/roger/cs/CS101/Time To Sleep/godot_project"
godot
```

或在 Godot 编辑器中：
- 点击 **Import**
- 选择 `project.godot` 文件
- 点击 **Import & Edit**

### 3. 导入精灵表

**请按照 [`导入指南.md`](导入指南.md) 的详细说明操作**

简要步骤：
1. 从 Pixel Studio 导出 3 个精灵表（idle/run/jump）
2. 放入 `assets/sprites/` 文件夹
3. 在 Godot 中配置 SpriteFrames
4. 测试运行

### 4. 运行游戏

**在编辑器中：**
- 打开 `scenes/test_level.tscn`
- 按 **F5** 运行

**从命令行：**
```bash
godot scenes/test_level.tscn
```

---

## 🎮 操作说明

| 按键 | 功能 |
|------|------|
| **A / D** 或 **← / →** | 左右移动 |
| **Space** | 跳跃 |
| **ESC** | 暂停（待实现） |

---

## 🎨 当前功能

### ✅ 已实现
- [x] 玩家移动（左右）
- [x] 跳跃系统（带重力）
- [x] 碰撞检测
- [x] 摄像机跟随
- [x] 测试关卡（地面 + 平台）
- [x] 动画系统框架

### 🔄 待实现
- [ ] 导入精灵表动画（需要您的素材）
- [ ] 攻击系统
- [ ] 冲刺系统
- [ ] 敌人 AI
- [ ] Boss 战
- [ ] 装备系统
- [ ] 完整关卡设计

---

## 📝 动画配置

### 需要的精灵表

从 Pixel Studio 导出以下文件：

#### 1. player_idle.png（待机动画）
- **帧数：** 4-8 帧
- **每帧尺寸：** 32x32 或 64x64
- **布局：** 水平排列（一行）
- **示例：** [帧1][帧2][帧3][帧4]

#### 2. player_run.png（移动动画）
- **帧数：** 8-12 帧
- **每帧尺寸：** 32x32 或 64x64
- **布局：** 水平排列
- **示例：** [帧1][帧2]...[帧12]

#### 3. player_jump.png（跳跃动画）
- **帧数：** 4-8 帧
- **每帧尺寸：** 32x32 或 64x64
- **布局：** 水平排列
- **示例：** [帧1][帧2][帧3][帧4]

### 导出设置（Pixel Studio）
- **格式：** PNG
- **背景：** 透明
- **缩放：** 1x（不要放大）
- **滤镜：** Nearest Neighbor

---

## 🔧 代码说明

### player.gd 核心逻辑

```gdscript
extends CharacterBody2D

# 移动参数
@export var speed: int = 200          # 移动速度
@export var jump_force: int = -400    # 跳跃力度
@export var gravity: int = 800        # 重力

func _physics_process(delta):
    # 1. 重力
    if not is_on_floor():
        velocity.y += gravity * delta
    
    # 2. 跳跃
    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = jump_force
    
    # 3. 移动
    var direction = Input.get_axis("move_left", "move_right")
    velocity.x = direction * speed
    
    # 4. 执行移动
    move_and_slide()
```

---

## 🎯 开发计划

### 阶段 1：基础动画（当前）
- [ ] 导入待机/移动/跳跃动画
- [ ] 测试动画切换
- [ ] 调整动画速度和朝向

### 阶段 2：战斗系统
- [ ] 攻击动画
- [ ] 攻击判定
- [ ] 敌人受击反馈

### 阶段 3：关卡设计
- [ ] 完整测试关卡
- [ ] 敌人放置
- [ ] 收集品

### 阶段 4：完整功能
- [ ] 装备系统
- [ ] UI 界面
- [ ] 音效/BGM

---

## 📚 学习资源

### Godot 官方
- **文档：** https://docs.godotengine.org/
- **教程：** https://docs.godotengine.org/en/stable/getting_started/
- **社区：** https://godotengine.org/community/

### 动画相关
- **SpriteFrames 教程：** https://docs.godotengine.org/en/stable/tutorials/animation/2d_sprite_animation.html
- **2D 游戏教程：** https://docs.godotengine.org/en/stable/tutorials/2d/index.html

### Pixel Studio
- **官方文档：** https://github.com/vico-re/pixel-studio
- **精灵表导出：** 参见 `导入指南.md`

---

## 🐛 常见问题

### Q: 游戏运行但看不到角色？
**A:** 需要导入精灵表！请参考 `导入指南.md`

### Q: 动画播放但很慢/很快？
**A:** 调整 SpriteFrames 中的 Speed 参数：
- 待机：5-8 FPS
- 移动：10-12 FPS
- 跳跃：15-20 FPS

### Q: 角色移动太快/太慢？
**A:** 在 Godot 编辑器中：
1. 选中 Player 节点
2. 修改 Script Variables 中的 `speed` 值

### Q: 跳跃高度不对？
**A:** 调整 `jump_force` 值（负数=向上）：
- 低跳：-300
- 中跳：-400（默认）
- 高跳：-500

---

## 🤝 贡献

这是一个学习项目，欢迎：
- 🎨 贡献像素艺术
- 💡 提出建议
- 🐛 报告问题

---

**项目启动：** 2026-04-25  
**最后更新：** 2026-04-25  
**状态：** 等待精灵表导入 🎨

---

## 📞 需要帮助？

如果您的精灵表已经准备好了，告诉我：
1. 文件位置
2. 每帧尺寸（32x32 或 64x64）
3. 每个动画的帧数

我可以帮您自动配置！🚀
