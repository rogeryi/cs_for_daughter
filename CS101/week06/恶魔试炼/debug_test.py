"""
碰撞调试版本 - 使用 demo移动4
"""
import pgzrun

WIDTH = 600
HEIGHT = 700
TITLE = "调试 - demo移动4"

print("=" * 60)
print("测试：demo移动4 精灵图 + 平台碰撞")
print("=" * 60)

player = {
    'x': 280,           # 屏幕中央 (600-40)//2
    'y': 500,
    'width': 40,        # 精灵图宽度（平台120的1/3）
    'height': 40,       # 精灵图高度
    'vx': 0,
    'vy': 0,
    'speed': 5,
    'jump_force': -12,
    'gravity': 0.6,
    'is_jumping': False
}

platforms = [
    Rect(0, 750, 600, 50),
    Rect(50, 650, 120, 20),
    Rect(250, 550, 120, 20),
    Rect(400, 450, 120, 20),
    Rect(100, 350, 120, 20),
]

def update():
    if keyboard.left or keyboard.a:
        player['x'] -= player['speed']
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
    
    player['x'] = max(0, min(WIDTH - player['width'], player['x']))
    
    if not player['is_jumping']:
        if keyboard.space or keyboard.w or keyboard.up:
            player['vy'] = player['jump_force']
            player['is_jumping'] = True
    
    player['vy'] += player['gravity']
    player['y'] += player['vy']
    
    if player['vy'] > 0:
        player_feet = player['y'] + player['height']
        for platform in platforms:
            if (player_feet >= platform.top and
                player_feet <= platform.bottom and
                player['x'] + player['width'] > platform.left and
                player['x'] < platform.right):
                player['y'] = platform.top - player['height']
                player['vy'] = 0
                player['is_jumping'] = False
                print(f"✓ 站在平台上")

def draw():
    screen.fill((30, 30, 30))
    
    for platform in platforms:
        screen.draw.filled_rect(platform, (180, 50, 50))
        screen.draw.rect(platform, (255, 100, 100))
    
    player_rect = Rect(player['x'], player['y'], player['width'], player['height'])
    screen.draw.filled_rect(player_rect, (50, 100, 255, 100))
    screen.draw.rect(player_rect, (100, 200, 255))
    
    try:
        screen.blit('player', (player['x'], player['y']))
    except:
        pass
    
    feet_y = player['y'] + player['height']
    screen.draw.line((player['x'], feet_y), 
                    (player['x'] + player['width'], feet_y), 
                    (255, 255, 0))
    
    screen.draw.text(f"玩家: ({int(player['x'])}, {int(player['y'])})", 
                    (10, 10), fontsize=16, color="white")
    screen.draw.text("蓝框=碰撞框, 黄线=脚部", 
                    (10, 30), fontsize=16, color="white")

print("\n游戏启动...")
pgzrun.go()