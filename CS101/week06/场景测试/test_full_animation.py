"""
完整动画状态机测试 - 待机+移动+跳跃
"""
import pgzrun
import pygame
import time
import random

WIDTH = 600
HEIGHT = 700
TITLE = "测试2 - 完整动画状态机"

print("=" * 60)
print("测试：待机 + 移动 + 跳跃 动画状态机 + 粒子特效")
print("=" * 60)

# 预加载所有精灵图
pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载移动帧
move_sprites = {}
for i in range(1, 5):
    move_sprites[i] = pygame.image.load(f"images/move{i}.png").convert_alpha()
    print(f"✓ 加载 move{i}.png: {move_sprites[i].get_size()}")

# 加载待机帧
idle_sprites = {}
for i in range(1, 5):
    idle_sprites[i] = pygame.image.load(f"images/idle{i}.png").convert_alpha()
    print(f"✓ 加载 idle{i}.png: {idle_sprites[i].get_size()}")

# 加载跳跃帧
jump_sprites = {}
for i in [1, 2, 3, 4, 5, 7, 8, 9, 10]:
    try:
        jump_sprites[i] = pygame.image.load(f"images/jump{i}.png").convert_alpha()
        print(f"✓ 加载 jump{i}.png: {jump_sprites[i].get_size()}")
    except:
        print(f"✗ jump{i}.png 不存在")

print("✓ 所有精灵图加载完成")

# 加载墙砖纹理
brick_texture_original = pygame.image.load("demo墙砖.png").convert_alpha()
print(f"✓ 加载墙砖纹理: {brick_texture_original.get_size()}")

# 加载齿轮
gear_images = []
for i in range(1, 4):
    try:
        gear_img = pygame.image.load(f"齿轮{i}.png").convert_alpha()
        # 使用rotozoom(0度旋转)来应用NEAREST算法，保持像素风格
        gear_img = pygame.transform.rotozoom(gear_img, 0, 50 / gear_img.get_width())
        gear_images.append(gear_img)
        print(f"✓ 加载齿轮{i}.png: 50x50 (NEAREST)")
    except Exception as e:
        print(f"✗ 加载齿轮{i}.png 失败: {e}")
        gear_images.append(None)

# 缩小墙砖到合适大小（高度20像素，宽度按比例）
brick_target_height = 20
original_size = brick_texture_original.get_size()
scale_factor = brick_target_height / original_size[1]
brick_target_width = int(original_size[0] * scale_factor)
brick_texture = pygame.transform.scale(brick_texture_original, (brick_target_width, brick_target_height))
print(f"✓ 缩放墙砖纹理: {brick_texture.get_size()}")

# 粒子系统
particles = []

class Particle:
    """粒子特效类"""
    def __init__(self, x, y, vx, vy, color, size, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.lifetime = lifetime
        self.age = 0
    
    def update(self, dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 200 * dt  # 重力
        return self.age < self.lifetime
    
    def draw(self, surface):
        alpha = int(255 * (1 - self.age / self.lifetime))
        color_with_alpha = (*self.color, alpha)
        pygame.draw.circle(surface, color_with_alpha, (int(self.x), int(self.y)), int(self.size))

# 动画帧间隔配置（秒）
JUMP_INTERVALS = {
    1: 0.05,  # 蓄力1（快速开始）
    2: 0.05,  # 蓄力2（快速过渡）
    3: 0.05,  # 蓄力3（快速过渡）
    4: 0.2,   # 上升1
    5: 0.2,   # 上升2
    7: 0.2,   # 滞空
    8: 0.2,   # 下落
    9: 0.2,   # 落地1
    10: 0.2   # 落地2
}

player = {
    'x': 270,
    'y': 607,  # 680(平台) - 72(高度) - 1(偏移) = 607
    'width': 60,
    'height': 72,  # 所有帧统一高度
    'speed': 5,
    'vy': 0,
    'jump_force': -15,
    'gravity': 0.8,
    'is_jumping': False,
    'facing': 'right',
    # 动画状态
    'state': 'idle',  # 'idle', 'move', 'jump_charge', 'jump_rise', 'jump_air', 'jump_fall', 'jump_land'
    'anim_frame': 1,
    'anim_timer': 0,
    'idle_speed': 0.2,
    'move_speed': 0.15,
    # 生命系统
    'hp': 100,
    'max_hp': 100,
    'invincible': 0,  # 无敌时间（秒）
}

platforms = [
    Rect(0, 680, 600, 20),
    Rect(50, 560, 200, 20),   # 平台1：580→560（+20）
    Rect(250, 430, 200, 20),  # 平台2：480→430（+50）
    Rect(400, 300, 200, 20),  # 平台3：380→300（+80）
    Rect(100, 170, 200, 20),  # 平台4：280→170（+110）
]

# 齿轮配置（位置、动画帧、计时器、移动参数）
gears = [
    {'x': 50, 'y': 560 - 50, 'frame': 0, 'timer': 0, 'speed': 0.1,  # 平台1上方，动画0.1s
     'move_x': 50, 'move_speed': 3, 'move_direction': 1, 'move_range': 200},
    {'x': 250, 'y': 430 - 50, 'frame': 0, 'timer': 0, 'speed': 0.1,  # 平台2上方，动画0.1s
     'move_x': 250, 'move_speed': 3, 'move_direction': 1, 'move_range': 200},
    {'x': 100, 'y': 170 - 50, 'frame': 0, 'timer': 0, 'speed': 0.1,  # 平台4上方，动画0.1s
     'move_x': 100, 'move_speed': 3, 'move_direction': 1, 'move_range': 200},
]

last_time = time.time()

def get_y_offset(state, frame):
    """计算偏移使脚底紧贴平台（所有帧统一60x72）"""
    # 所有帧都是60x72，统一偏移1像素
    return 1

def draw_brick_platform(rect):
    """用墙砖纹理绘制平台"""
    brick_w = brick_texture.get_width()
    brick_h = brick_texture.get_height()
    
    # 平铺墙砖
    for y in range(rect.top, rect.bottom, brick_h):
        for x in range(rect.left, rect.right, brick_w):
            screen.surface.blit(brick_texture, (x, y))

def spawn_jump_particles():
    """生成跳跃粒子特效"""
    state = player['state']
    frame = player['anim_frame']
    
    # 粒子中心位置（玩家脚底）
    center_x = player['x'] + player['width'] // 2
    center_y = player['y'] + 72  # 脚底位置
    
    # 蓄力阶段（jump1-3）：地面蓄力粒子
    if state == 'jump_charge':
        if frame in [1, 2, 3]:
            # 黄色/橙色蓄力粒子
            for _ in range(8):
                vx = random.uniform(-100, 100)
                vy = random.uniform(-50, 50)
                color = random.choice([(255, 200, 50), (255, 150, 30), (255, 220, 100)])
                size = random.uniform(2, 5)
                lifetime = random.uniform(0.3, 0.6)
                particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))
    
    # 上升阶段（jump4-5）：向上喷射粒子
    elif state == 'jump_rise':
        if frame in [4, 5]:
            # 蓝/白色上升粒子
            for _ in range(6):
                vx = random.uniform(-50, 50)
                vy = random.uniform(-150, -50)
                color = random.choice([(100, 200, 255), (150, 220, 255), (200, 240, 255)])
                size = random.uniform(2, 4)
                lifetime = random.uniform(0.2, 0.4)
                particles.append(Particle(center_x, center_y + 20, vx, vy, color, size, lifetime))
    
    # 滞空阶段（jump7）：漂浮粒子
    elif state == 'jump_air':
        # 紫色/粉色漂浮粒子
        for _ in range(3):
            vx = random.uniform(-30, 30)
            vy = random.uniform(-30, 30)
            color = random.choice([(200, 150, 255), (255, 180, 220), (180, 130, 255)])
            size = random.uniform(1.5, 3)
            lifetime = random.uniform(0.3, 0.5)
            particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))
    
    # 落地阶段（jump9-10）：着陆冲击粒子
    elif state == 'jump_land':
        if frame in [9, 10]:
            # 黄/白色冲击粒子
            for _ in range(12):
                angle = random.uniform(0, 3.14)  # 上半圆
                speed = random.uniform(50, 150)
                vx = speed * random.uniform(-1, 1)
                vy = -abs(speed * 0.5)  # 向上
                color = random.choice([(255, 255, 200), (255, 220, 150), (255, 200, 100)])
                size = random.uniform(2, 6)
                lifetime = random.uniform(0.3, 0.7)
                particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))

def update():
    global last_time
    
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    
    # 更新粒子
    global particles
    particles = [p for p in particles if p.update(delta_time)]
    
    # 更新齿轮动画
    for gear in gears:
        gear['timer'] += delta_time
        if gear['timer'] >= gear['speed']:
            gear['timer'] = 0
            gear['frame'] = (gear['frame'] + 1) % 3  # 0, 1, 2 循环
        
        # 齿轮水平移动（变速：两端慢，中间快）
        # 计算齿轮在平台上的相对位置 (0.0 ~ 1.0)
        position_ratio = (gear['x'] - gear['move_x']) / (gear['move_range'] - 50)
        
        # 使用正弦函数实现加减速：中间快(1.0)，两端慢(0.15) - 刹车效果更明显
        import math
        speed_multiplier = 0.15 + 0.85 * math.sin(position_ratio * math.pi)
        
        gear['x'] += gear['move_speed'] * gear['move_direction'] * speed_multiplier
        
        # 检查是否超出平台边缘（齿轮不能超出平台）
        platform_left = gear['move_x']
        platform_right = gear['move_x'] + gear['move_range'] - 50  # 50是齿轮宽度
        
        if gear['x'] >= platform_right:
            gear['x'] = platform_right
            gear['move_direction'] = -1  # 向左移动
        elif gear['x'] <= platform_left:
            gear['x'] = platform_left
            gear['move_direction'] = 1  # 向右移动
    
    # 齿轮碰撞检测
    if player['invincible'] > 0:
        player['invincible'] -= delta_time
    else:
        # 玩家碰撞框
        player_rect = Rect(player['x'], player['y'], player['width'], player['height'])
        
        for gear in gears:
            # 齿轮碰撞框（50x50）
            gear_rect = Rect(gear['x'], gear['y'], 50, 50)
            
            if player_rect.colliderect(gear_rect):
                # 碰撞！玩家受伤
                player['hp'] -= 20
                player['invincible'] = 1.0  # 1秒无敌时间
                print(f"⚠️ 碰到齿轮！HP: {player['hp']}")
                
                if player['hp'] <= 0:
                    print("💀 玩家死亡！")
                    player['hp'] = 0
    
    # 生成跳跃粒子特效
    if player['is_jumping']:
        spawn_jump_particles()
    
    # 检测移动
    is_moving_key = False
    if keyboard.left or keyboard.a:
        player['x'] -= player['speed']
        player['facing'] = 'left'
        is_moving_key = True
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
        player['facing'] = 'right'
        is_moving_key = True
    
    player['x'] = max(0, min(WIDTH - player['width'], player['x']))
    
    # 跳跃输入
    if keyboard.space or keyboard.w or keyboard.up:
        if not player['is_jumping'] and player['state'] in ['idle', 'move']:
            player['is_jumping'] = True
            player['state'] = 'jump_charge'
            player['anim_frame'] = 1
            player['anim_timer'] = 0
            player['vy'] = player['jump_force']
    
    # 重力
    player['vy'] += player['gravity']
    player['y'] += player['vy']
    
    # 碰撞检测（所有帧统一高度72）
    on_ground = False
    current_height = 72  # 固定高度
    
    if player['vy'] > 0:
        player_feet = player['y'] + current_height
        for platform in platforms:
            if (player_feet >= platform.top and
                player_feet <= platform.bottom + 10 and
                player['x'] + player['width'] > platform.left and
                player['x'] < platform.right):
                
                player['y'] = platform.top - current_height
                player['vy'] = 0
                on_ground = True
                break
    
    # 状态转换：跳跃中落地
    if on_ground and player['is_jumping']:
        if player['state'] in ['jump_rise', 'jump_air', 'jump_fall']:
            # 开始落地动画
            player['state'] = 'jump_land'
            player['anim_frame'] = 9
            player['anim_timer'] = 0
        elif player['state'] == 'jump_land':
            # 落地动画播放完毕，根据移动状态切换
            if is_moving_key:
                player['state'] = 'move'
                player['anim_frame'] = 1
            else:
                player['state'] = 'idle'
                player['anim_frame'] = 1
            player['is_jumping'] = False
            player['anim_timer'] = 0
    
    # 动画状态机
    if player['state'] == 'idle':
        player['anim_timer'] += delta_time
        if player['anim_timer'] >= player['idle_speed']:
            player['anim_timer'] = 0
            player['anim_frame'] = (player['anim_frame'] % 4) + 1
        if is_moving_key:
            player['state'] = 'move'
            player['anim_frame'] = 1
            
    elif player['state'] == 'move':
        player['anim_timer'] += delta_time
        if player['anim_timer'] >= player['move_speed']:
            player['anim_timer'] = 0
            player['anim_frame'] = (player['anim_frame'] % 4) + 1
        if not is_moving_key and not player['is_jumping']:
            player['state'] = 'idle'
            player['anim_frame'] = 1
            
    elif player['state'] == 'jump_charge':
        # 蓄力动画 1→2→3
        player['anim_timer'] += delta_time
        interval = JUMP_INTERVALS[player['anim_frame']]
        if player['anim_timer'] >= interval:
            player['anim_timer'] = 0
            if player['anim_frame'] < 3:
                player['anim_frame'] += 1
            else:
                player['state'] = 'jump_rise'
                player['anim_frame'] = 4
                
    elif player['state'] == 'jump_rise':
        # 上升动画 4→5
        player['anim_timer'] += delta_time
        interval = JUMP_INTERVALS[player['anim_frame']]
        if player['anim_timer'] >= interval:
            player['anim_timer'] = 0
            if player['anim_frame'] == 4:
                player['anim_frame'] = 5
            # 不在这里切换状态，由物理决定
        
        # 检查速度变化
        if player['vy'] >= 0:
            # 开始下落
            player['state'] = 'jump_fall'
            player['anim_frame'] = 8
            player['anim_timer'] = 0
        elif is_moving_key:
            # 空中移动，播放滞空动画
            player['state'] = 'jump_air'
            player['anim_frame'] = 7
            player['anim_timer'] = 0
                    
    elif player['state'] == 'jump_air':
        # 滞空动画（空中移动时）
        player['anim_timer'] += delta_time
        interval = JUMP_INTERVALS[7]
        if player['anim_timer'] >= interval:
            player['anim_timer'] = 0
            # 快速切换，保持第7帧
        
        # 检查状态变化
        if player['vy'] >= 0:
            # 开始下落
            player['state'] = 'jump_fall'
            player['anim_frame'] = 8
            player['anim_timer'] = 0
        elif not is_moving_key:
            # 不再移动，回到上升/下落状态
            if player['vy'] < 0:
                player['state'] = 'jump_rise'
                player['anim_frame'] = 5
            else:
                player['state'] = 'jump_fall'
                player['anim_frame'] = 8
                
    elif player['state'] == 'jump_fall':
        # 下落动画
        player['anim_timer'] += delta_time
        interval = JUMP_INTERVALS[8]
        if player['anim_timer'] >= interval:
            player['anim_timer'] = 0
            # 保持第8帧直到落地
            
    elif player['state'] == 'jump_land':
        # 落地动画 9→10
        player['anim_timer'] += delta_time
        interval = JUMP_INTERVALS[player['anim_frame']]
        if player['anim_timer'] >= interval:
            player['anim_timer'] = 0
            if player['anim_frame'] == 9:
                player['anim_frame'] = 10
            else:
                # 落地动画完成，等待下一次update检测on_ground来切换状态
                pass

def draw():
    screen.fill((30, 30, 30))
    
    # 绘制平台（墙砖纹理）
    for platform in platforms:
        draw_brick_platform(platform)
    
    # 绘制齿轮（动画）
    for gear in gears:
        # 使用当前帧绘制齿轮
        frame_idx = gear['frame']
        if gear_images[frame_idx]:
            screen.surface.blit(gear_images[frame_idx], (gear['x'], gear['y']))
    
    # 绘制粒子特效
    for particle in particles:
        particle.draw(screen.surface)
    
    # 绘制精灵图
    try:
        if player['state'] == 'idle':
            sprite = idle_sprites[player['anim_frame']]
        elif player['state'] == 'move':
            sprite = move_sprites[player['anim_frame']]
        else:
            sprite = jump_sprites[player['anim_frame']]
        
        y_offset = get_y_offset(player['state'], player['anim_frame'])
        
        if player['facing'] == 'right':
            sprite = pygame.transform.flip(sprite, True, False)
        
        # 水平居中：对于宽度不同的帧（jump2/3有特效）
        sprite_width = sprite.get_width()
        x_offset = (player['width'] - sprite_width) // 2 if sprite_width != player['width'] else 0
        
        # 无敌闪烁效果
        if player['invincible'] > 0:
            import time
            if int(time.time() * 10) % 2 == 0:  # 快速闪烁
                screen.blit(sprite, (player['x'] + x_offset, player['y'] + y_offset))
        else:
            screen.blit(sprite, (player['x'] + x_offset, player['y'] + y_offset))
    except Exception as e:
        print(f"精灵图错误: {e}")
    
    # 调试信息
    screen.draw.text(f"状态: {player['state']}", (10, 10), fontsize=16, color="cyan")
    screen.draw.text(f"帧: {player['anim_frame']}", (10, 30), fontsize=16, color="yellow")
    screen.draw.text(f"vy: {player['vy']:.1f}", (10, 50), fontsize=16, color="white")
    screen.draw.text("A/D移动, SPACE跳跃", (10, 70), fontsize=16, color="white")
    
    # 血条显示
    hp_bar_width = 200
    hp_bar_height = 20
    hp_bar_x = WIDTH - hp_bar_width - 10
    hp_bar_y = 10
    
    # 血条背景
    hp_bg = Rect(hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height)
    screen.draw.filled_rect(hp_bg, (100, 0, 0))
    
    # 血条前景
    hp_ratio = player['hp'] / player['max_hp']
    hp_width = int(hp_bar_width * hp_ratio)
    if hp_width > 0:
        hp_rect = Rect(hp_bar_x, hp_bar_y, hp_width, hp_bar_height)
        screen.draw.filled_rect(hp_rect, (0, 255, 0))
    
    # 血条边框
    screen.draw.rect(hp_bg, (255, 255, 255))
    
    # HP文字
    screen.draw.text(f"HP: {player['hp']}/{player['max_hp']}", 
                    (hp_bar_x + 5, hp_bar_y + 2), fontsize=14, color="white")

print("\n游戏启动...")
pgzrun.go()
