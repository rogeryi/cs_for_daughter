"""
碰撞调试版本 - 使用 demo移动1（只裁剪左右边框）
"""
import pgzrun
import pygame

WIDTH = 600
HEIGHT = 700
TITLE = "调试 - demo移动1"

print("=" * 60)
print("测试：demo移动1（方向翻转）+ 平台碰撞")
print("=" * 60)

player = {
    'x': 270,           # 屏幕中央 (600-60)//2
    'y': 500,
    'width': 60,        # 精灵图宽度（平台120的1/2）
    'height': 72,       # 精灵图高度（按比例）
    'vx': 0,
    'vy': 0,
    'speed': 5,
    'jump_force': -12,
    'gravity': 0.6,
    'is_jumping': False,
    'facing': 'right'   # 朝向：'left' 或 'right'
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
        player['facing'] = 'left'  # 向左移动，面朝左
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
        player['facing'] = 'right'  # 向右移动，面朝右
    
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
        # 根据朝向翻转精灵图
        sprite = pygame.image.load('images/player.png').convert_alpha()
        if player['facing'] == 'right':
            # 面朝右：翻转（因为原始图是面朝左的）
            sprite = pygame.transform.flip(sprite, True, False)
        # 面朝左：不翻转，保持原始方向
        
        screen.blit(sprite, (player['x'], player['y']))
    except Exception as e:
        print(f"精灵图加载失败: {e}")
        pass
    
    feet_y = player['y'] + player['height']
    screen.draw.line((player['x'], feet_y), 
                    (player['x'] + player['width'], feet_y), 
                    (255, 255, 0))
    
    screen.draw.text(f"玩家: ({int(player['x'])}, {int(player['y'])})", 
                    (10, 10), fontsize=16, color="white")
    screen.draw.text(f"碰撞框: {player['width']}x{player['height']}", 
                    (10, 30), fontsize=16, color="yellow")
    screen.draw.text(f"朝向: {player['facing']}", 
                    (10, 50), fontsize=16, color="cyan")
    screen.draw.text("蓝框=碰撞框, 黄线=脚部, A/D移动", 
                    (10, 70), fontsize=16, color="white")

print("\n游戏启动...")
pgzrun.go()
