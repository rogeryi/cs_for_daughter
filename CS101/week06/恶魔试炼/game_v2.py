"""
《恶魔试炼》- 像素爬塔版
垂直向上平台跳跃游戏 - 完整版

功能:
- 完整动画状态机（待机/移动/跳跃）
- 跳跃粒子特效系统
- 墙砖纹理平台
- 像素爬塔模式（无敌人）

开发者: Amos
日期: 2026
"""

import pgzrun
import pygame
import time
import random

# ==================== 游戏设置 ====================
WIDTH = 600
HEIGHT = 700
TITLE = "恶魔试炼 - 像素爬塔"
FPS = 60

# ==================== 音效系统 ====================
def play_jump():
    """播放跳跃音效"""
    try:
        sounds.jump.play()
    except:
        pass

def play_land():
    """播放落地音效"""
    try:
        sounds.land.play()
    except:
        pass

def play_fail():
    """播放失败音效"""
    try:
        sounds.fail.play()
    except:
        pass

def play_win():
    """播放胜利音效"""
    try:
        sounds.win.play()
    except:
        pass

def play_menu():
    """播放菜单音效"""
    try:
        sounds.menu.play()
    except:
        pass

def play_bgm():
    """播放背景音乐（循环）"""
    try:
        sounds.bgm.play(-1)
    except:
        pass

def stop_bgm():
    """停止背景音乐"""
    try:
        sounds.bgm.stop()
    except:
        pass

# ==================== 加载中文字体 ====================
TITLE_FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
TEXT_FONT_PATH = "/System/Library/Fonts/STHeiti Light.ttc"

try:
    title_font = pygame.font.Font(TITLE_FONT_PATH, 60)
    text_font = pygame.font.Font(TEXT_FONT_PATH, 30)
except:
    title_font = None
    text_font = None

# ==================== 游戏状态 ====================
game_state = 'menu'  # 'menu', 'playing', 'gameover', 'win'
max_height = 0
camera_y = 0
TARGET_HEIGHT = 3000
start_time = 0
game_time = 0

# ==================== 预加载精灵图 ====================
pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载移动帧
move_sprites = {}
for i in range(1, 5):
    try:
        move_sprites[i] = pygame.image.load(f"images/move{i}.png").convert_alpha()
        print(f"✓ 加载 move{i}.png: {move_sprites[i].get_size()}")
    except:
        print(f"✗ move{i}.png 不存在")

# 加载待机帧
idle_sprites = {}
for i in range(1, 5):
    try:
        idle_sprites[i] = pygame.image.load(f"images/idle{i}.png").convert_alpha()
        print(f"✓ 加载 idle{i}.png: {idle_sprites[i].get_size()}")
    except:
        print(f"✗ idle{i}.png 不存在")

# 加载跳跃帧
jump_sprites = {}
for i in [1, 2, 3, 4, 5, 7, 8, 9, 10]:
    try:
        jump_sprites[i] = pygame.image.load(f"images/jump{i}.png").convert_alpha()
        print(f"✓ 加载 jump{i}.png: {jump_sprites[i].get_size()}")
    except:
        print(f"✗ jump{i}.png 不存在")

# 加载墙砖纹理
brick_texture_original = pygame.image.load("demo墙砖.png").convert_alpha()
brick_target_height = 20
original_size = brick_texture_original.get_size()
scale_factor = brick_target_height / original_size[1]
brick_target_width = int(original_size[0] * scale_factor)
brick_texture = pygame.transform.scale(brick_texture_original, (brick_target_width, brick_target_height))
print(f"✓ 墙砖纹理: {brick_texture.get_size()}")

print("✓ 所有资源加载完成")

# ==================== 动画配置 ====================
JUMP_INTERVALS = {
    1: 0.05,  # 蓄力1
    2: 0.05,  # 蓄力2
    3: 0.05,  # 蓄力3
    4: 0.2,   # 上升1
    5: 0.2,   # 上升2
    7: 0.2,   # 滞空
    8: 0.2,   # 下落
    9: 0.2,   # 落地1
    10: 0.2   # 落地2
}

# ==================== 粒子系统 ====================
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
        self.vy += 200 * dt
        return self.age < self.lifetime
    
    def draw(self, surface):
        alpha = int(255 * (1 - self.age / self.lifetime))
        color_with_alpha = (*self.color, alpha)
        pygame.draw.circle(surface, color_with_alpha, (int(self.x), int(self.y)), int(self.size))

def spawn_jump_particles(player_state, player_frame, player_x, player_y):
    """生成跳跃粒子特效"""
    center_x = player_x + 30  # 玩家中心
    center_y = player_y + 72  # 脚底位置
    
    # 蓄力阶段
    if player_state == 'jump_charge' and player_frame in [1, 2, 3]:
        for _ in range(8):
            vx = random.uniform(-100, 100)
            vy = random.uniform(-50, 50)
            color = random.choice([(255, 200, 50), (255, 150, 30), (255, 220, 100)])
            size = random.uniform(2, 5)
            lifetime = random.uniform(0.3, 0.6)
            particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))
    
    # 上升阶段
    elif player_state == 'jump_rise' and player_frame in [4, 5]:
        for _ in range(6):
            vx = random.uniform(-50, 50)
            vy = random.uniform(-150, -50)
            color = random.choice([(100, 200, 255), (150, 220, 255), (200, 240, 255)])
            size = random.uniform(2, 4)
            lifetime = random.uniform(0.2, 0.4)
            particles.append(Particle(center_x, center_y + 20, vx, vy, color, size, lifetime))
    
    # 滞空阶段
    elif player_state == 'jump_air':
        for _ in range(3):
            vx = random.uniform(-30, 30)
            vy = random.uniform(-30, 30)
            color = random.choice([(200, 150, 255), (255, 180, 220), (180, 130, 255)])
            size = random.uniform(1.5, 3)
            lifetime = random.uniform(0.3, 0.5)
            particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))
    
    # 落地阶段
    elif player_state == 'jump_land' and player_frame in [9, 10]:
        for _ in range(12):
            vx = random.uniform(-150, 150)
            vy = -abs(random.uniform(50, 150) * 0.5)
            color = random.choice([(255, 255, 200), (255, 220, 150), (255, 200, 100)])
            size = random.uniform(2, 6)
            lifetime = random.uniform(0.3, 0.7)
            particles.append(Particle(center_x, center_y, vx, vy, color, size, lifetime))

# ==================== 玩家属性 ====================
player = {
    'x': 270,
    'y': 607,
    'width': 60,
    'height': 72,
    'speed': 5,
    'vy': 0,
    'jump_force': -15,
    'gravity': 0.8,
    'is_jumping': False,
    'facing': 'right',
    # 动画状态
    'state': 'idle',
    'anim_frame': 1,
    'anim_timer': 0,
    'idle_speed': 0.2,
    'move_speed': 0.15,
    # 游戏属性
    'hp': 100,
    'max_hp': 100,
}

# ==================== 平台列表 ====================
# 平台间距设计：确保玩家可以跳到
# 跳跃力-15，重力0.8，最大高度约140像素
# 垂直间距：60-100像素（保证可以跳到）
# 水平间距：平台宽度120，随机位置保证可达
platforms = [
    Rect(0, 680, 600, 20),      # 地面
    Rect(240, 600, 120, 20),    # 平台1：垂直80，水平中心
    Rect(100, 520, 120, 20),    # 平台2：垂直80，向左
    Rect(300, 440, 120, 20),    # 平台3：垂直80，向右
    Rect(150, 360, 120, 20),    # 平台4：垂直80，向左
    Rect(350, 280, 120, 20),    # 平台5：垂直80，向右
    Rect(200, 200, 120, 20),    # 平台6：垂直80，中心
    Rect(50, 120, 120, 20),     # 平台7：垂直80，向左
]

last_time = time.time()

# ==================== 辅助函数 ====================
def get_y_offset(state, frame):
    """计算偏移使脚底紧贴平台"""
    return 1

def draw_brick_platform(rect, screen_surface):
    """用墙砖纹理绘制平台"""
    brick_w = brick_texture.get_width()
    brick_h = brick_texture.get_height()
    
    for y in range(rect.top, rect.bottom, brick_h):
        for x in range(rect.left, rect.right, brick_w):
            screen_surface.blit(brick_texture, (x, y))

def draw_text_chinese(text, center, fontsize, color, font_type='text'):
    """绘制中文文本"""
    if font_type == 'title':
        font_path = TITLE_FONT_PATH
    else:
        font_path = TEXT_FONT_PATH
    
    try:
        font = pygame.font.Font(font_path, fontsize)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        screen.surface.blit(text_surface, text_rect)
    except:
        screen.draw.text(text, center=center, fontsize=fontsize, color=color)

# ==================== 游戏主循环 ====================
def update():
    global last_time, game_state, max_height, camera_y, start_time, game_time
    
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    
    # 更新粒子
    global particles
    particles = [p for p in particles if p.update(delta_time)]
    
    if game_state == 'playing':
        # 记录开始时间
        if start_time == 0:
            start_time = pygame.time.get_ticks()
        
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
                play_jump()  # 播放跳跃音效
        
        # 重力
        player['vy'] += player['gravity']
        player['y'] += player['vy']
        
        # 碰撞检测
        on_ground = False
        current_height = 72
        
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
                player['state'] = 'jump_land'
                player['anim_frame'] = 9
                player['anim_timer'] = 0
                play_land()  # 播放落地音效
        
        # 状态转换：落地动画完成
        if on_ground and player['state'] == 'jump_land':
            interval = JUMP_INTERVALS.get(player['anim_frame'], 0.2)
            player['anim_timer'] += delta_time
            
            if player['anim_timer'] >= interval:
                player['anim_timer'] = 0
                if player['anim_frame'] == 9:
                    player['anim_frame'] = 10
                elif player['anim_frame'] == 10:
                    player['is_jumping'] = False
                    player['state'] = 'idle' if not is_moving_key else 'move'
                    player['anim_frame'] = 1
                    player['anim_timer'] = 0
        
        # 状态转换：待机/移动切换
        if not player['is_jumping']:
            if is_moving_key:
                if player['state'] != 'move':
                    player['state'] = 'move'
                    player['anim_frame'] = 1
                    player['anim_timer'] = 0
            else:
                if player['state'] != 'idle':
                    player['state'] = 'idle'
                    player['anim_frame'] = 1
                    player['anim_timer'] = 0
        
        # 动画更新
        if player['state'] == 'idle':
            player['anim_timer'] += delta_time
            if player['anim_timer'] >= player['idle_speed']:
                player['anim_timer'] = 0
                player['anim_frame'] = (player['anim_frame'] % 4) + 1
        
        elif player['state'] == 'move':
            player['anim_timer'] += delta_time
            if player['anim_timer'] >= player['move_speed']:
                player['anim_timer'] = 0
                player['anim_frame'] = (player['anim_frame'] % 4) + 1
        
        elif player['state'] in ['jump_charge', 'jump_rise', 'jump_air', 'jump_fall', 'jump_land']:
            player['anim_timer'] += delta_time
            interval = JUMP_INTERVALS.get(player['anim_frame'], 0.2)
            
            if player['anim_timer'] >= interval:
                player['anim_timer'] = 0
                frame = player['anim_frame']
                
                if player['state'] == 'jump_charge':
                    if frame == 1:
                        player['anim_frame'] = 2
                    elif frame == 2:
                        player['anim_frame'] = 3
                    elif frame == 3:
                        player['state'] = 'jump_rise'
                        player['anim_frame'] = 4
                
                elif player['state'] == 'jump_rise':
                    if frame == 4:
                        player['anim_frame'] = 5
                    elif frame == 5:
                        player['state'] = 'jump_air'
                        player['anim_frame'] = 7
                
                elif player['state'] == 'jump_air':
                    if player['vy'] < 0:
                        pass
                    else:
                        player['state'] = 'jump_fall'
                        player['anim_frame'] = 8
                
                elif player['state'] == 'jump_fall':
                    pass
                
                elif player['state'] == 'jump_land':
                    if frame == 9:
                        player['anim_frame'] = 10
        
        # 生成跳跃粒子特效
        if player['is_jumping']:
            spawn_jump_particles(player['state'], player['anim_frame'], player['x'], player['y'])
        
        # 相机跟随（实时跟随玩家）
        # 当玩家超出屏幕范围时，相机跟随
        target_y = HEIGHT / 2  # 目标位置：屏幕中线
        
        if player['y'] < target_y - 100:
            # 玩家太靠上，相机向上移动
            shift = (target_y - 100) - player['y']
            camera_y += shift
            player['y'] = target_y - 100
            
            for platform in platforms:
                platform.y += shift
            
            max_height = max(max_height, int(camera_y / 10))
        
        elif player['y'] > target_y + 100:
            # 玩家太靠下，相机向下移动
            shift = player['y'] - (target_y + 100)
            camera_y -= shift
            player['y'] = target_y + 100
            
            for platform in platforms:
                platform.y -= shift
        
        # 生成新平台
        highest_platform = min(platforms, key=lambda p: p.y)
        while highest_platform.y > 100:
            # 垂直间距：80-120像素（保持原有的跳跃挑战）
            new_y = highest_platform.y - random.randint(80, 120)
            
            # 水平位置：增加挑战性，左右最多偏移200像素
            # 需要玩家在跳跃时精准控制方向
            min_x = max(0, highest_platform.x - 200)
            max_x = min(WIDTH - 120, highest_platform.x + 200)
            new_x = random.randint(min_x, max_x)
            
            new_platform = Rect(new_x, new_y, 120, 20)
            platforms.append(new_platform)
            highest_platform = new_platform
        
        # 不删除平台，保留所有平台以便玩家重新爬塔
        
        # 检测玩家是否掉出屏幕底部
        if player['y'] > HEIGHT + 100:
            game_state = 'gameover'
            game_time = (pygame.time.get_ticks() - start_time) / 1000
            play_fail()  # 播放失败音效
            stop_bgm()  # 停止背景音乐
        
        # 检测胜利
        if max_height >= TARGET_HEIGHT:
            game_state = 'win'
            game_time = (pygame.time.get_ticks() - start_time) / 1000
            play_win()  # 播放胜利音效
            stop_bgm()  # 停止背景音乐

def draw():
    screen.fill((30, 30, 30))
    
    if game_state == 'menu':
        draw_menu()
    elif game_state == 'playing':
        draw_game()
    elif game_state == 'gameover':
        draw_game()
        draw_game_over()
    elif game_state == 'win':
        draw_game()
        draw_win()

def draw_menu():
    """绘制开始菜单"""
    draw_text_chinese("恶魔试炼", (WIDTH/2, 200), 64, (220, 50, 50), 'title')
    draw_text_chinese("像素爬塔", (WIDTH/2, 270), 28, (255, 140, 0), 'title')
    
    draw_text_chinese("不断向上跳跃，到达塔顶！", 
                    (WIDTH/2, 340), 18, (150, 150, 150))
    
    draw_text_chinese("操作说明:", (WIDTH/2, 400), 22, (255, 255, 255))
    draw_text_chinese("A/D 或 ←/→: 左右移动", (WIDTH/2, 430), 18, (200, 200, 200))
    draw_text_chinese("Space/W/↑: 向上跳跃", (WIDTH/2, 455), 18, (200, 200, 200))
    draw_text_chinese("目标: 到达 3000m 高度", (WIDTH/2, 480), 18, (200, 200, 200))
    
    draw_text_chinese("按 ENTER 开始游戏", (WIDTH/2, 550), 24, (255, 255, 100))

def draw_game():
    """绘制游戏画面"""
    # 绘制平台（墙砖纹理）
    for platform in platforms:
        draw_brick_platform(platform, screen.surface)
    
    # 绘制粒子特效
    for particle in particles:
        particle.draw(screen.surface)
    
    # 绘制玩家精灵图
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
        
        sprite_width = sprite.get_width()
        x_offset = (player['width'] - sprite_width) // 2 if sprite_width != player['width'] else 0
        
        screen.blit(sprite, (player['x'] + x_offset, player['y'] + y_offset))
    except Exception as e:
        print(f"精灵图错误: {e}")
        player_rect = Rect(player['x'], player['y'], player['width'], player['height'])
        screen.draw.filled_rect(player_rect, (50, 255, 50))
    
    # 绘制 UI
    draw_text_chinese(f"高度: {max_height}m", (WIDTH/2, 25), 24, (255, 255, 255))
    
    # 血条
    bar_x = 10
    bar_y = 10
    bar_width = 150
    bar_height = 25
    
    screen.draw.filled_rect(Rect(bar_x, bar_y, bar_width, bar_height), (80, 80, 80))
    hp_ratio = player['hp'] / player['max_hp']
    hp_width = int(bar_width * hp_ratio)
    
    if hp_ratio > 0.5:
        hp_color = (50, 200, 50)
    elif hp_ratio > 0.25:
        hp_color = (255, 200, 0)
    else:
        hp_color = (255, 50, 50)
    
    screen.draw.filled_rect(Rect(bar_x, bar_y, hp_width, bar_height), hp_color)
    draw_text_chinese(f"HP: {player['hp']}/{player['max_hp']}", 
                     (bar_x + bar_width/2, bar_y + bar_height/2), 
                     16, (255, 255, 255))

def draw_game_over():
    """绘制游戏结束画面"""
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 180))
    
    draw_text_chinese("挑战失败！", (WIDTH/2, 200), 52, (220, 50, 50), 'title')
    draw_text_chinese(f"最终高度: {max_height}m", (WIDTH/2, 280), 28, (255, 255, 255))
    draw_text_chinese("按 R 重新开始", (WIDTH/2, 380), 24, (255, 255, 100))

def get_rank(game_time):
    """根据用时获取职位等级"""
    if game_time < 60:
        return "地狱总裁", (255, 215, 0)
    elif game_time < 120:
        return "地狱总监", (200, 100, 255)
    elif game_time < 180:
        return "地狱经理", (100, 150, 255)
    elif game_time < 300:
        return "地狱主管", (100, 255, 100)
    else:
        return "地狱员工", (255, 255, 255)

def draw_win():
    """绘制胜利画面"""
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 180))
    
    draw_text_chinese("登顶成功！", (WIDTH/2, 150), 52, (50, 220, 50), 'title')
    draw_text_chinese(f"最终高度: {max_height}m", (WIDTH/2, 220), 28, (255, 255, 255))
    
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)
    draw_text_chinese(f"用时: {minutes}分{seconds}秒", (WIDTH/2, 260), 24, (255, 255, 100))
    
    rank_name, rank_color = get_rank(game_time)
    draw_text_chinese(f"获得职位: {rank_name}", (WIDTH/2, 320), 30, rank_color)
    draw_text_chinese("恭喜你成为合格社畜！", (WIDTH/2, 380), 24, (255, 255, 100))
    draw_text_chinese("按 R 再次挑战", (WIDTH/2, 440), 24, (255, 255, 100))

def on_key_down(key):
    """按键事件处理"""
    global game_state
    
    if key == keys.RETURN or key == keys.KP_ENTER:
        if game_state == 'menu':
            game_state = 'playing'
            play_menu()  # 播放菜单音效
            play_bgm()  # 开始播放背景音乐
    
    if key == keys.R and game_state in ['gameover', 'win']:
        restart_game()
        play_menu()  # 播放菜单音效
        play_bgm()  # 重新开始播放背景音乐

def restart_game():
    """重新开始游戏"""
    global game_state, max_height, camera_y, start_time, game_time, particles
    
    game_state = 'playing'
    max_height = 0
    camera_y = 0
    start_time = 0
    game_time = 0
    particles = []
    
    player['x'] = 270
    player['y'] = 607
    player['vy'] = 0
    player['is_jumping'] = False
    player['state'] = 'idle'
    player['anim_frame'] = 1
    player['anim_timer'] = 0
    player['hp'] = 100
    
    platforms.clear()
    platforms.extend([
        Rect(0, 680, 600, 20),      # 地面
        Rect(240, 600, 120, 20),    # 平台1
        Rect(100, 520, 120, 20),    # 平台2
        Rect(300, 440, 120, 20),    # 平台3
        Rect(150, 360, 120, 20),    # 平台4
        Rect(350, 280, 120, 20),    # 平台5
        Rect(200, 200, 120, 20),    # 平台6
        Rect(50, 120, 120, 20),     # 平台7
    ])

# ==================== 启动游戏 ====================
print("\n游戏启动...")
pgzrun.go()
