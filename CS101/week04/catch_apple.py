# 接苹果游戏 - Pygame Zero 示例
# 控制篮子接住掉落的苹果

import pgzrun
import random

# 窗口设置
WIDTH = 600
HEIGHT = 400
TITLE = "接苹果游戏 🍎"

# 创建精灵
basket = Actor('basket', (300, 370))  # 篮子
apple = Actor('apple', (300, 0))      # 苹果
apple.speed = 3  # 自定义属性：下落速度

# 游戏变量
score = 0
game_over = False

def draw():
    # 清屏（浅蓝色背景）
    screen.fill((135, 206, 235))
    
    # 绘制精灵
    basket.draw()
    apple.draw()
    
    # 显示分数
    screen.draw.text(f"分数: {score}", (10, 10), fontsize=30, color="white")
    
    # 游戏结束提示
    if game_over:
        screen.draw.text("游戏结束！", center=(300, 200), 
                        fontsize=50, color="red")
        screen.draw.text(f"最终分数: {score}", center=(300, 250), 
                        fontsize=30, color="white")
        screen.draw.text("按空格键重新开始", center=(300, 300), 
                        fontsize=20, color="yellow")

def update():
    global score, game_over
    
    if game_over:
        return
    
    # 篮子跟随鼠标
    basket.x = mouse_x
    
    # 苹果下落
    apple.y += apple.speed
    
    # 检查苹果是否掉出屏幕
    if apple.y > HEIGHT:
        game_over = True
        return
    
    # 检查碰撞（接到苹果）
    if basket.colliderect(apple):
        score += 1
        # 重置苹果位置到顶部
        apple.y = 0
        apple.x = random.randint(50, WIDTH - 50)
        # 增加难度
        apple.speed += 0.2

def on_mouse_move(pos):
    """鼠标移动事件"""
    global mouse_x
    mouse_x = pos[0]  # 获取鼠标的 x 坐标

def on_key_down(key):
    """按键事件"""
    global game_over, score, apple
    if key == keys.SPACE and game_over:
        # 重新开始
        game_over = False
        score = 0
        apple.y = 0
        apple.x = random.randint(50, WIDTH - 50)
        apple.speed = 3

# 初始化鼠标位置
mouse_x = 300

# 启动游戏
pgzrun.go()
