"""
《恶魔试炼》- 社畜的晋升之路
垂直向上平台跳跃游戏

开发者: Amos
日期: 2026
"""

import pgzrun
import random
import pygame

# ==================== 游戏设置 ====================
WIDTH = 600
HEIGHT = 700
TITLE = "恶魔试炼 - 社畜的晋升之路"
FPS = 60

# ==================== 加载中文字体 ====================
# macOS 系统字体路径 - 使用黑体不同字重
# 标题字体：黑体 Medium（加粗效果）
TITLE_FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
# 正文字体：黑体 Light（轻盈效果）
TEXT_FONT_PATH = "/System/Library/Fonts/STHeiti Light.ttc"

# 尝试加载字体
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
space_pressed = False  # 空格键按下标志
start_time = 0  # 游戏开始时间
game_time = 0  # 游戏用时

# ==================== 玩家属性 ====================
player = {
    'x': 300,              # 屏幕中央
    'y': 600,              # 从底部往上100像素（确保在屏幕内）
    'vx': 0,
    'vy': 0,
    'width': 40,
    'height': 40,
    'speed': 5,            # 移动速度
    'jump_force': -14,     # 统一跳跃力
    'gravity': 0.6,        # 重力
    'is_jumping': False,   # 是否在跳跃
    'attacking': False,    # 是否在攻击
    'hp': 100,             # 血量
    'max_hp': 100,         # 最大血量
}

# ==================== 平台列表 ====================
# 红色地狱砖平台，垂直分布
platforms = [
    Rect(0, 750, 600, 50),      # 地面（基层岗位）
    Rect(50, 650, 120, 20),     # 平台1
    Rect(250, 580, 120, 20),    # 平台2
    Rect(400, 500, 120, 20),    # 平台3
    Rect(100, 420, 120, 20),    # 平台4
    Rect(350, 340, 120, 20),    # 平台5
    Rect(200, 260, 120, 20),    # 平台6
    Rect(450, 180, 120, 20),    # 平台7
]

# ==================== 游戏函数 ====================

def update_player():
    """更新玩家位置和状态"""
    global max_height
    
    # 左右移动
    if keyboard.left or keyboard.a:
        player['x'] -= player['speed']
    if keyboard.right or keyboard.d:
        player['x'] += player['speed']
    
    # 边界限制（不能移出屏幕）
    player['x'] = max(0, min(WIDTH - player['width'], player['x']))
    
    # 跳跃（统一跳跃力）- 只在游戏进行中使用
    if game_state == 'playing' and not player['is_jumping']:
        if keyboard.w or keyboard.up or space_pressed:
            player['vy'] = player['jump_force']
            player['is_jumping'] = True
    
    # 应用重力
    player['vy'] += player['gravity']
    player['y'] += player['vy']

def check_platform_collision():
    """检测玩家与平台的碰撞（只在下落时检测）"""
    # 只在下落时检测碰撞
    if player['vy'] > 0:
        for platform in platforms:
            # 检测玩家的脚是否碰到平台顶部
            if (player['y'] + player['height'] >= platform.top and
                player['y'] + player['height'] <= platform.top + 15 and
                player['x'] + player['width'] > platform.left and
                player['x'] < platform.right):
                
                # 碰撞成功，站在平台上
                player['y'] = platform.top - player['height']
                player['vy'] = 0
                player['is_jumping'] = False

def update_camera():
    """相机跟随玩家上升"""
    global camera_y, max_height
    
    # 当玩家超过屏幕中线（400）时，相机跟随
    if player['y'] < 400:
        shift = 400 - player['y']
        camera_y += shift
        player['y'] = 400
        
        # 移动所有平台
        for platform in platforms:
            platform.y += shift
        
        # 更新最高高度记录
        max_height = max(max_height, int(camera_y / 10))

def generate_platforms():
    """在屏幕上方生成新平台"""
    # 找到最高的平台
    highest_platform = min(platforms, key=lambda p: p.y)
    
    # 如果最高平台离屏幕顶部太近，生成新平台
    while highest_platform.y > 100:
        # 随机生成新平台位置
        new_x = random.randint(0, WIDTH - 120)
        new_y = highest_platform.y - random.randint(80, 120)
        new_platform = Rect(new_x, new_y, 120, 20)
        platforms.append(new_platform)
        highest_platform = new_platform

def remove_off_screen_platforms():
    """删除屏幕下方的旧平台"""
    platforms_to_remove = [p for p in platforms if p.y > HEIGHT + 50]
    for p in platforms_to_remove:
        platforms.remove(p)

def check_game_over():
    """检测游戏是否结束（血量归零）"""
    global game_state
    if player['hp'] <= 0:
        game_state = 'gameover'

def check_win():
    """检测是否胜利（达到目标高度）"""
    global game_state, game_time
    if max_height >= TARGET_HEIGHT:
        game_state = 'win'
        game_time = (pygame.time.get_ticks() - start_time) / 1000  # 转换为秒

def update():
    """游戏主循环 - 每秒执行60次"""
    global game_state, start_time
    
    if game_state == 'playing':
        # 记录开始时间
        if start_time == 0:
            start_time = pygame.time.get_ticks()
        
        # 更新玩家
        update_player()
        
        # 检测碰撞
        check_platform_collision()
        
        # 更新相机
        update_camera()
        
        # 生成和删除平台
        generate_platforms()
        remove_off_screen_platforms()
        
        # 检测游戏状态
        check_game_over()
        check_win()

def draw():
    """绘制游戏画面"""
    # 深色背景（地狱氛围）
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

def draw_text_chinese(text, center, fontsize, color, font_type='text'):
    """绘制中文文本（使用系统字体）"""
    global title_font, text_font
    
    # 选择字体路径
    if font_type == 'title':
        font_path = TITLE_FONT_PATH
    else:
        font_path = TEXT_FONT_PATH
    
    try:
        # 使用自定义字体
        font = pygame.font.Font(font_path, fontsize)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        screen.surface.blit(text_surface, text_rect)
    except:
        # 如果失败，使用默认方法
        screen.draw.text(text, center=center, fontsize=fontsize, color=color)

def draw_menu():
    """绘制开始菜单"""
    # 标题（使用明朝体，更有艺术感）
    draw_text_chinese("恶魔试炼", (WIDTH/2, 200), 64, (220, 50, 50), 'title')
    draw_text_chinese("社畜的晋升之路", (WIDTH/2, 270), 28, (255, 140, 0), 'title')
    
    # 故事背景
    draw_text_chinese("西蒙是一只底层小恶魔，在地狱公司工作了100年还是最底层。", 
                    (WIDTH/2, 340), 18, (150, 150, 150))
    draw_text_chinese("今天，他终于迎来了晋升考核——不断向上跳跃，到达顶层！", 
                    (WIDTH/2, 365), 18, (150, 150, 150))
    
    # 操作说明
    draw_text_chinese("操作说明:", (WIDTH/2, 420), 22, (255, 255, 255))
    draw_text_chinese("A/D 或 ←/→: 左右移动", (WIDTH/2, 450), 18, (200, 200, 200))
    draw_text_chinese("Space/W/↑: 向上跳跃", (WIDTH/2, 475), 18, (200, 200, 200))
    draw_text_chinese("目标: 到达 3000m 高度", (WIDTH/2, 500), 18, (200, 200, 200))
    
    # 开始提示
    draw_text_chinese("按 ENTER 开始游戏", (WIDTH/2, 550), 24, (255, 255, 100))

def draw_game():
    """绘制游戏画面"""
    # 绘制平台（红色地狱砖）
    for platform in platforms:
        screen.draw.filled_rect(platform, (180, 50, 50))
        # 添加边框（使用正确的参数格式）
        rect_outline = Rect(platform.x, platform.y, platform.width, platform.height)
        screen.draw.rect(rect_outline, (220, 80, 80))
    
    # 绘制玩家 - 使用 demo移动1 精灵图
    # 调试：打印玩家位置
    print(f"绘制玩家: x={player['x']}, y={player['y']}")
    
    try:
        # 使用 Actor 类来显示（Pygame Zero 推荐方式）
        screen.blit('demo移动1', (player['x'], player['y']))
        print("✓ 精灵图绘制成功")
    except Exception as e:
        print(f"✗ 玩家精灵加载失败: {e}")
        # 如果加载失败，使用大一点的矩形代替
        player_rect = Rect(player['x'], player['y'], 
                          player['width'], player['height'])
        screen.draw.filled_rect(player_rect, (50, 255, 50))
        screen.draw.rect(player_rect, (100, 255, 100))
    
    # 绘制 UI
    draw_ui()

def draw_ui():
    """绘制用户界面"""
    # 血条
    draw_hp_bar()
    
    # 高度显示
    draw_text_chinese(f"高度: {max_height}m", (WIDTH/2, 25), 24, (255, 255, 255))

def draw_hp_bar():
    """绘制血条"""
    bar_x = 10
    bar_y = 10
    bar_width = 150
    bar_height = 25
    
    # 血条背景
    screen.draw.filled_rect(Rect(bar_x, bar_y, bar_width, bar_height), (80, 80, 80))
    
    # 血量
    hp_ratio = player['hp'] / player['max_hp']
    hp_width = int(bar_width * hp_ratio)
    
    # 根据血量改变颜色
    if hp_ratio > 0.5:
        hp_color = (50, 200, 50)  # 绿色
    elif hp_ratio > 0.25:
        hp_color = (255, 200, 0)  # 黄色
    else:
        hp_color = (255, 50, 50)  # 红色
    
    screen.draw.filled_rect(Rect(bar_x, bar_y, hp_width, bar_height), hp_color)
    
    # 血量文字
    draw_text_chinese(f"HP: {player['hp']}/{player['max_hp']}", 
                     (bar_x + bar_width/2, bar_y + bar_height/2), 
                     16, (255, 255, 255))

def draw_game_over():
    """绘制游戏结束画面"""
    # 半透明背景
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 180))
    
    draw_text_chinese("被辞退了！", (WIDTH/2, 200), 52, (220, 50, 50), 'title')
    draw_text_chinese(f"最终高度: {max_height}m", (WIDTH/2, 280), 28, (255, 255, 255))
    draw_text_chinese("血量耗尽，失去了工作...", (WIDTH/2, 320), 20, (200, 200, 200))
    draw_text_chinese("按 R 重新入职", (WIDTH/2, 380), 24, (255, 255, 100))

def get_rank(game_time):
    """根据用时获取职位等级"""
    if game_time < 60:
        return "地狱总裁", "金色"
    elif game_time < 120:
        return "地狱总监", "紫色"
    elif game_time < 180:
        return "地狱经理", "蓝色"
    elif game_time < 300:
        return "地狱主管", "绿色"
    else:
        return "地狱员工", "白色"

def draw_win():
    """绘制胜利画面"""
    # 半透明背景
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 180))
    
    draw_text_chinese("通过试用期！", (WIDTH/2, 150), 52, (50, 220, 50), 'title')
    draw_text_chinese(f"最终高度: {max_height}m", (WIDTH/2, 220), 28, (255, 255, 255))
    
    # 显示用时
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)
    draw_text_chinese(f"用时: {minutes}分{seconds}秒", (WIDTH/2, 260), 24, (255, 255, 100))
    
    # 显示职位
    rank_name, rank_color = get_rank(game_time)
    color_map = {
        "金色": (255, 215, 0),
        "紫色": (200, 100, 255),
        "蓝色": (100, 150, 255),
        "绿色": (100, 255, 100),
        "白色": (255, 255, 255)
    }
    rank_rgb = color_map.get(rank_color, (255, 255, 255))
    
    draw_text_chinese(f"上司给你的职位: {rank_name}", (WIDTH/2, 320), 30, rank_rgb)
    draw_text_chinese("恭喜你成为合格社畜！", (WIDTH/2, 380), 24, (255, 255, 100))
    draw_text_chinese("按 R 再次挑战", (WIDTH/2, 440), 24, (255, 255, 100))

def on_key_down(key):
    """按键事件处理"""
    global game_state, space_pressed
    
    # 记录空格键按下（用于跳跃）
    if key == keys.SPACE:
        space_pressed = True
    
    # 从菜单开始游戏（使用ENTER键）
    if key == keys.RETURN or key == keys.KP_ENTER:
        if game_state == 'menu':
            game_state = 'playing'
    
    # 重新开始
    if key == keys.R and game_state in ['gameover', 'win']:
        restart_game()

def on_key_up(key):
    """按键释放事件处理"""
    global space_pressed
    
    # 释放空格键
    if key == keys.SPACE:
        space_pressed = False

def restart_game():
    """重新开始游戏"""
    global game_state, max_height, camera_y, start_time, game_time
    
    game_state = 'playing'
    max_height = 0
    camera_y = 0
    start_time = 0
    game_time = 0
    
    # 重置玩家
    player['x'] = 300
    player['y'] = 700
    player['vx'] = 0
    player['vy'] = 0
    player['is_jumping'] = False
    player['hp'] = 100  # 重置血量
    
    # 重置平台
    platforms.clear()
    platforms.extend([
        Rect(0, 750, 600, 50),
        Rect(50, 650, 120, 20),
        Rect(250, 580, 120, 20),
        Rect(400, 500, 120, 20),
        Rect(100, 420, 120, 20),
        Rect(350, 340, 120, 20),
        Rect(200, 260, 120, 20),
        Rect(450, 180, 120, 20),
    ])

# ==================== 启动游戏 ====================
pgzrun.go()
