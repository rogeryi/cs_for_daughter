"""
精灵图测试 - 试验如何导入和显示图片
"""
import pgzrun

# 游戏设置
WIDTH = 800
HEIGHT = 600
TITLE = "精灵图测试"
FPS = 60

# 玩家属性
player = {
    'x': 400,  # 屏幕中央
    'y': 300,
    'speed': 5
}

print("=" * 50)
print("精灵图测试程序启动")
print("=" * 50)
print(f"图片应该放在: images/ 文件夹")
print(f"图片名称: demo移动1.png")
print("=" * 50)

def draw():
    """绘制画面"""
    # 清空屏幕（白色背景）
    screen.fill((255, 255, 255))
    
    # 方法1：使用 screen.blit() 加载图片
    try:
        # 注意：不需要写 .png 扩展名
        screen.blit('demo移动1', (player['x'], player['y']))
        print(f"✓ 成功显示精灵图 at ({player['x']}, {player['y']})")
    except Exception as e:
        print(f"✗ 精灵图加载失败: {e}")
        # 如果失败，画一个矩形代替
        player_rect = Rect(player['x'], player['y'], 100, 100)
        screen.draw.filled_rect(player_rect, (255, 0, 0))
        screen.draw.text("精灵图加载失败", (player['x'], player['y']), 
                        fontsize=20, color="white")
    
    # 显示操作提示
    screen.draw.text("使用方向键或WASD移动", (10, 10), 
                    fontsize=24, color="black")
    screen.draw.text(f"玩家位置: x={player['x']}, y={player['y']}", 
                    (10, 40), fontsize=20, color="black")

def update():
    """更新游戏逻辑"""
    # 上下左右移动
    if keyboard.left or keyboard.a:
        player['x'] -= player['speed']
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
    if keyboard.up or keyboard.w:
        player['y'] -= player['speed']
    if keyboard.down or keyboard.s:
        player['y'] += player['speed']
    
    # 边界限制
    player['x'] = max(0, min(WIDTH - 100, player['x']))
    player['y'] = max(0, min(HEIGHT - 100, player['y']))

# 启动游戏
print("\n游戏启动中...")
pgzrun.go()
