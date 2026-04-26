# 🎨 Pixel Studio Demo 精灵表导入指南

> **目标：** 将 Pixel Studio 中的 demo 角色动画（待机/移动/跳跃）导入 Godot 并切割成可播放的动画

---

## 📋 第一步：从 Pixel Studio 导出精灵表

### 在 Pixel Studio 中操作：

1. **打开您的 demo 项目**
   - 打开 Pixel Studio
   - 找到带有红色标签的 demo 角色

2. **导出待机动画（Idle）**
   ```
   File → Export → Sprite Sheet
   - 选择 "idle" 动画
   - Format: PNG
   - 勾选 "Transparent Background"
   - 导出为: demo_idle.png
   - 保存到桌面
   ```

3. **导出移动动画（Run）**
   ```
   File → Export → Sprite Sheet
   - 选择 "run" 动画
   - Format: PNG
   - 勾选 "Transparent Background"
   - 导出为: demo_run.png
   - 保存到桌面
   ```

4. **导出跳跃动画（Jump）**
   ```
   File → Export → Sprite Sheet
   - 选择 "jump" 动画
   - Format: PNG
   - 勾选 "Transparent Background"
   - 导出为: demo_jump.png
   - 保存到桌面
   ```

---

## 📁 第二步：将文件复制到 Godot 项目

### 方法 1：手动复制
```bash
# 打开终端，执行：
cp ~/Desktop/demo_idle.png "/Users/roger/cs/CS101/Time To Sleep/godot_project/assets/sprites/"
cp ~/Desktop/demo_run.png "/Users/roger/cs/CS101/Time To Sleep/godot_project/assets/sprites/"
cp ~/Desktop/demo_jump.png "/Users/roger/cs/CS101/Time To Sleep/godot_project/assets/sprites/"
```

### 方法 2：拖拽
1. 打开 Finder
2. 导航到：`/Users/roger/cs/CS101/Time To Sleep/godot_project/assets/sprites/`
3. 将桌面上的 3 个 PNG 文件拖入

---

## 🎮 第三步：在 Godot 中导入和切割精灵表

### 3.1 打开 Godot 项目

```bash
cd "/Users/roger/cs/CS101/Time To Sleep/godot_project"
godot
```

### 3.2 配置精灵导入选项

**对每个精灵表文件（idle/run/jump）：**

1. 在 **FileSystem** 面板中，点击 `assets/sprites/demo_idle.png`
2. 在 **Import** 面板中设置：
   - ✅ **Preset:** 2D Pixel
   - ✅ **Filter:** Nearest（保持像素清晰）
   - ❌ **Mipmaps:** 关闭
   - 点击 **Reimport** 按钮

3. 重复以上步骤处理 `demo_run.png` 和 `demo_jump.png`

### 3.3 打开玩家场景

1. 在 **FileSystem** 中双击 `scenes/player.tscn`
2. 在场景树中选中 `AnimatedSprite2D` 节点

### 3.4 创建 SpriteFrames 资源

1. 在 **Inspector** 面板中找到 **Sprite Frames** 属性
2. 点击下拉菜单 → **New SpriteFrames**
3. 点击 **Sprite Frames** 旁边的 **[点击打开]** 按钮
4. 这会打开 **SpriteFrames 编辑器**

### 3.5 切割待机动画（Idle）

1. **重命名默认动画：**
   - 在左侧动画列表中，双击 `default`
   - 重命名为 `idle`

2. **添加精灵表帧：**
   - 点击底部的 **📁 从精灵表添加帧** 按钮
   - 选择 `res://assets/sprites/demo_idle.png`
   - 在弹出的对话框中设置：
     - **Horizontal:** 输入帧数（例如 8）
     - **Vertical:** 1（如果只有一行）
   - 点击 **OK**

3. **调整动画速度：**
   - 选中 `idle` 动画
   - 设置 **Speed (FPS):** 6-8
   - ✅ 勾选 **Loop**

### 3.6 切割移动动画（Run）

1. **创建新动画：**
   - 点击左侧的 **+** 按钮
   - 命名为 `run`

2. **添加精灵表帧：**
   - 点击 **📁 从精灵表添加帧**
   - 选择 `res://assets/sprites/demo_run.png`
   - 设置：
     - **Horizontal:** 输入帧数（例如 8-12）
     - **Vertical:** 1
   - 点击 **OK**

3. **调整动画速度：**
   - 选中 `run` 动画
   - 设置 **Speed (FPS):** 10-12
   - ✅ 勾选 **Loop**

### 3.7 切割跳跃动画（Jump）

1. **创建新动画：**
   - 点击左侧的 **+** 按钮
   - 命名为 `jump`

2. **添加精灵表帧：**
   - 点击 **📁 从精灵表添加帧**
   - 选择 `res://assets/sprites/demo_jump.png`
   - 设置：
     - **Horizontal:** 输入帧数（例如 4-8）
     - **Vertical:** 1
   - 点击 **OK**

3. **调整动画速度：**
   - 选中 `jump` 动画
   - 设置 **Speed (FPS):** 15-20
   - ❌ 取消勾选 **Loop**（跳跃只播放一次）

---

## 🎯 第四步：测试动画

### 4.1 设置默认动画

1. 在 **Inspector** 中找到 **Autoplay**
2. 设置为 `idle`

### 4.2 运行测试

1. 确保 `player.tscn` 是打开的
2. 按 **F5** 或点击右上角的 **▶️ 播放** 按钮
3. Godot 会提示保存场景，点击 **Save**

### 4.3 测试操作

在游戏窗口中：
- **A / D** 或 **← / →** - 左右移动（应该播放 run 动画）
- **Space** - 跳跃（应该播放 jump 动画）
- 静止不动 - 应该播放 idle 动画

---

## 🔧 常见问题排查

### Q1: 动画不显示或显示为白色方块？
**解决方案：**
1. 检查精灵表是否正确导入
2. 确认 Filter 设置为 **Nearest**
3. 重新导入精灵表（点击 Reimport）

### Q2: 动画播放太快或太慢？
**解决方案：**
1. 打开 SpriteFrames 编辑器
2. 调整对应动画的 **Speed (FPS)** 值
3. 建议值：
   - idle: 6-8 FPS
   - run: 10-12 FPS
   - jump: 15-20 FPS

### Q3: 动画帧切割不正确？
**解决方案：**
1. 打开 SpriteFrames 编辑器
2. 删除错误的帧（选中帧，点击垃圾桶图标）
3. 重新从精灵表添加，确保帧数设置正确

### Q4: 角色翻转后动画方向错误？
**解决方案：**
代码中已处理，检查 `player.gd` 中的：
```gdscript
animated_sprite.flip_h = not facing_right
```

---

## 📝 帧数参考

如果您的动画是标准帧数：

| 动画 | 常见帧数 | 建议 FPS | 循环 |
|------|---------|---------|------|
| idle | 4-8 | 6-8 | ✅ |
| run | 8-12 | 10-12 | ✅ |
| jump | 4-8 | 15-20 | ❌ |

---

## 🎨 Pixel Studio 导出技巧

### 确保正确的导出设置：

1. **画布尺寸一致**
   - 所有动画使用相同的画布大小
   - 例如：32x32 或 64x64

2. **角色对齐**
   - 脚部对齐到画布底部
   - 左右居中对齐

3. **透明背景**
   - 确保背景层是透明的
   - 导出时勾选 "Transparent"

4. **精灵表布局**
   - 水平排列（一行多列）
   - 不要留空帧

---

## ✅ 完成检查清单

- [ ] 从 Pixel Studio 导出 3 个精灵表（idle/run/jump）
- [ ] 将文件复制到 `assets/sprites/` 文件夹
- [ ] 在 Godot 中配置导入选项（Nearest Filter）
- [ ] 打开 SpriteFrames 编辑器
- [ ] 切割 idle 动画并设置速度
- [ ] 切割 run 动画并设置速度
- [ ] 切割 jump 动画并设置速度
- [ ] 设置 Autoplay 为 idle
- [ ] 运行游戏测试动画
- [ ] 测试移动、跳跃、待机动画切换

---

## 📞 需要帮助？

如果您在导出过程中遇到问题：

1. **告诉我精灵表的位置**（在桌面、文档或其他位置）
2. **告诉我每个动画的帧数**
3. **告诉我每帧的尺寸**（32x32 或 64x64）

我可以帮您自动完成导入和切割！🚀
