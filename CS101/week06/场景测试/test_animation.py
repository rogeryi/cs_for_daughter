"""
动画测试版本 - 4帧行走动画 + 4帧待机动画
"""
import pgzrun
import pygame
import time

WIDTH = 600
HEIGHT = 700
TITLE = "动画测试 - 行走+待机"

print("=" * 60)
print("测试：4帧行走动画 + 4帧待机动画 + 方向翻转")
print("=" * 60)

# 预加载所有精灵图
pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载行走帧
move_sprites = {}
for i in range(1, 5):
    path = f"images/move{i}.png"
    move_sprites[i] = pygame.image.load(path).convert_alpha()
    print(f"✓ 加载 move{i}.png: {move_sprites[i].get_size()}")

# 加载待机帧
idle_sprites = {}
for i in range(1, 5):
    path = f"images/idle{i}.png"
    idle_sprites[i] = pygame.image.load(path).convert_alpha()
    print(f"✓ 加载 idle{i}.png: {idle_sprites[i].get_size()}")

player = {
    'x': 270,
    'y': 600,  # 调整初始位置
    'width': 60,
    'height': 75,  # 使用最大高度
    'speed': 5,
    'vy': 0,
    'jump_force': -12,
    'gravity': 0.6,
    'is_jumping': False,
    'facing': 'right',
    'is_moving': False,
    'anim_type': 'idle',      # 当前动画类型：'idle' 或 'move'
    'anim_frame': 1,          # 当前帧 (1-4)
    'anim_timer': 0,          # 动画计时器
    'idle_speed': 0.2,        # 待机动画速度（秒/帧）
    'move_speed': 0.15        # 移动动画速度（秒/帧）
}

platforms = [
    Rect(0, 680, 600, 20),   # 底部铺满的平台
    Rect(50, 580, 120, 20),  # 原有平台位置上调
    Rect(250, 480, 120, 20),
    Rect(400, 380, 120, 20),
    Rect(100, 280, 120, 20),
]

last_time = time.time()

def update():
    global last_time
    
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    
    # 检测移动
    player['is_moving'] = False
    
    if keyboard.left or keyboard.a:
        player['x'] -= player['speed']
        player['facing'] = 'left'
        player['is_moving'] = True
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
        player['facing'] = 'right'
        player['is_moving'] = True
    
    player['x'] = max(0, min(WIDTH - player['width'], player['x']))
    
    # 跳跃
    if not player['is_jumping']:
        if keyboard.space or keyboard.w or keyboard.up:
            player['vy'] = player['jump_force']
            player['is_jumping'] = True
    
    # 重力
    player['vy'] += player['gravity']
    player['y'] += player['vy']
    
    # 碰撞检测
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
    
    # 动画更新
    if player['is_moving']:
        player['anim_type'] = 'move'
        player['anim_timer'] += delta_time
        if player['anim_timer'] >= player['move_speed']:
            player['anim_timer'] = 0
            player['anim_frame'] = (player['anim_frame'] % 4) + 1  # 1→2→3→4→1
    else:
        # 静止时播放待机动画
        player['anim_type'] = 'idle'
        player['anim_timer'] += delta_time
        if player['anim_timer'] >= player['idle_speed']:
            player['anim_timer'] = 0
            player['anim_frame'] = (player['anim_frame'] % 4) + 1  # 1→2→3→4→1

def draw():
    screen.fill((30, 30, 30))
    
    # 绘制平台
    for platform in platforms:
        screen.draw.filled_rect(platform, (180, 50, 50))
        screen.draw.rect(platform, (255, 100, 100))
    
    # 绘制碰撞框
    player_rect = Rect(player['x'], player['y'], player['width'], player['height'])
    screen.draw.filled_rect(player_rect, (50, 100, 255, 100))
    screen.draw.rect(player_rect, (100, 200, 255))
    
    # 绘制精灵图（带方向和动画）
    try:
        # 根据动画类型获取精灵图
        if player['anim_type'] == 'move':
            sprite = move_sprites[player['anim_frame']]
        else:
            sprite = idle_sprites[player['anim_frame']]
        
        # 计算偏移：使脚底紧贴平台
        # 移动帧：高度72的向下偏移1像素，75的不偏移
        # 待机帧：统一高度72，向下偏移1像素
        y_offset = 0
        sprite_height = sprite.get_height()
        
        if player['anim_type'] == 'move':
            if sprite_height == 72:
                y_offset = 1
        else:  # idle - 统一高度72
            y_offset = 1
        
        # 根据朝向翻转
        if player['facing'] == 'right':
            sprite = pygame.transform.flip(sprite, True, False)
        
        screen.blit(sprite, (player['x'], player['y'] + y_offset))
    except Exception as e:
        print(f"精灵图错误: {e}")
    
    # 调试信息
    screen.draw.text(f"玩家: ({int(player['x'])}, {int(player['y'])})", 
                    (10, 10), fontsize=16, color="white")
    screen.draw.text(f"朝向: {player['facing']}", 
                    (10, 30), fontsize=16, color="cyan")
    screen.draw.text(f"动画: {player['anim_type']} 帧{player['anim_frame']}/4", 
                    (10, 50), fontsize=16, color="yellow")
    screen.draw.text(f"移动: {player['is_moving']}", 
                    (10, 70), fontsize=16, color="green")
    screen.draw.text("A/D移动, SPACE跳跃", 
                    (10, 90), fontsize=16, color="white")

print("\n游戏启动...")
pgzrun.go()
