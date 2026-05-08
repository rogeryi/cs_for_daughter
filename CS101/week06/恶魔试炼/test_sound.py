"""
音效测试文件
测试所有音效是否正常播放，并在屏幕上显示状态
"""

WIDTH = 480
HEIGHT = 600
TITLE = "音效测试"

# 注意：PGZ不支持直接使用系统字体名
# 需要将字体文件放入 fonts/ 文件夹
# 这里使用默认字体（英文），中文可能显示为方块

# 音效播放状态
sound_status = {
    'jump': {'playing': False, 'timer': 0},
    'land': {'playing': False, 'timer': 0},
    'hurt': {'playing': False, 'timer': 0},
    'fail': {'playing': False, 'timer': 0},
    'menu': {'playing': False, 'timer': 0},
    'win': {'playing': False, 'timer': 0},
    'bgm': {'playing': False, 'timer': 0},
}

def update_sound_status():
    """更新音效状态计时器"""
    for sound_name in sound_status:
        if sound_status[sound_name]['playing']:
            sound_status[sound_name]['timer'] -= 1
            if sound_status[sound_name]['timer'] <= 0:
                sound_status[sound_name]['playing'] = False

# 播放音效函数
def play_jump():
    """跳跃音效"""
    try:
        sounds.jump.play()
        sound_status['jump']['playing'] = True
        sound_status['jump']['timer'] = 30  # 显示0.5秒
        print("✓ 播放 jump.wav")
    except:
        print("✗ jump.wav 不存在")
        sound_status['jump']['playing'] = False

def play_land():
    """落地音效"""
    try:
        sounds.land.play()
        sound_status['land']['playing'] = True
        sound_status['land']['timer'] = 30
        print("✓ 播放 land.wav")
    except:
        print("✗ land.wav 不存在")
        sound_status['land']['playing'] = False

def play_hurt():
    """受伤音效"""
    try:
        sounds.hurt.play()
        sound_status['hurt']['playing'] = True
        sound_status['hurt']['timer'] = 30
        print("✓ 播放 hurt.wav")
    except:
        print("✗ hurt.wav 不存在")
        sound_status['hurt']['playing'] = False

def play_fail():
    """失败音效"""
    try:
        sounds.fail.play()
        sound_status['fail']['playing'] = True
        sound_status['fail']['timer'] = 60  # 显示1秒
        print("✓ 播放 fail.wav")
    except:
        print("✗ fail.wav 不存在")
        sound_status['fail']['playing'] = False

def play_menu():
    """菜单音效"""
    try:
        sounds.menu.play()
        sound_status['menu']['playing'] = True
        sound_status['menu']['timer'] = 30
        print("✓ 播放 menu.wav")
    except:
        print("✗ menu.wav 不存在")
        sound_status['menu']['playing'] = False

def play_win():
    """胜利音效"""
    try:
        sounds.win.play()
        sound_status['win']['playing'] = True
        sound_status['win']['timer'] = 60
        print("✓ 播放 win.wav")
    except:
        print("✗ win.wav 不存在")
        sound_status['win']['playing'] = False

def play_bgm():
    """背景音乐"""
    try:
        sounds.bgm.play(-1)  # -1 表示循环播放
        sound_status['bgm']['playing'] = True
        sound_status['bgm']['timer'] = 9999  # 持续显示
        print("✓ 播放 bgm.wav (循环)")
    except:
        print("✗ bgm.wav 不存在")
        sound_status['bgm']['playing'] = False

# 按键触发测试
def on_key_down(key):
    if key == keys.SPACE:
        play_jump()
    if key == keys.L:
        play_land()
    if key == keys.H:
        play_hurt()
    if key == keys.F:
        play_fail()
    if key == keys.M:
        play_menu()
    if key == keys.W:
        play_win()
    if key == keys.B:
        play_bgm()

def update():
    """更新音效状态"""
    update_sound_status()

# 按键触发测试
def on_key_down(key):
    if key == keys.SPACE:
        play_jump()
    if key == keys.L:
        play_land()
    if key == keys.H:
        play_hurt()
    if key == keys.F:
        play_fail()
    if key == keys.M:
        play_menu()
    if key == keys.W:
        play_win()
    if key == keys.B:
        play_bgm()
    if key == keys.S:
        # 停止BGM
        try:
            sounds.bgm.stop()
            sound_status['bgm']['playing'] = False
            print("■ 停止 bgm.wav")
        except:
            pass

def draw():
    screen.fill((30, 30, 30))
    
    # 标题（使用英文+emoji）
    screen.draw.text("Sound Test", center=(WIDTH/2, 50), fontsize=40, color="white")
    screen.draw.text("Press keys to test sounds:", center=(WIDTH/2, 100), fontsize=18, color="yellow")
    
    # 按键列表（使用英文）
    keys_info = [
        ('SPACE', 'Jump Sound', 'jump'),
        ('L', 'Land Sound', 'land'),
        ('H', 'Hurt Sound', 'hurt'),
        ('F', 'Fail Sound', 'fail'),
        ('M', 'Menu Sound', 'menu'),
        ('W', 'Win Sound', 'win'),
        ('B', 'BGM', 'bgm'),
        ('S', 'Stop BGM', 'stop'),
    ]
    
    y = 150
    for key_name, desc, sound_name in keys_info:
        # 按键名
        screen.draw.text(f"[{key_name}]", (50, y), fontsize=18, color="cyan")
        
        # 描述
        screen.draw.text(f"{desc}", (170, y), fontsize=18, color="white")
        
        # 状态显示
        if sound_name != 'stop':
            if sound_status[sound_name]['playing']:
                # 正在播放 - 绿色闪烁
                import time
                alpha = int(200 + 55 * (time.time() % 1 > 0.5))
                screen.draw.text("PLAYING", (330, y), fontsize=18, color=(0, alpha, 0))
            else:
                screen.draw.text("READY", (330, y), fontsize=18, color="gray")
        else:
            screen.draw.text("READY", (330, y), fontsize=18, color="gray")
        
        y += 40
    
    # 分隔线
    screen.draw.line((30, 490), (WIDTH - 30, 490), (100, 100, 100))
    
    # 说明（使用英文）
    screen.draw.text("Tips:", (50, 500), fontsize=16, color="yellow")
    screen.draw.text("• Sound files should be in sounds/ folder", (50, 520), fontsize=14, color="gray")
    screen.draw.text("• Playing sounds show green flash", (50, 540), fontsize=14, color="gray")
    screen.draw.text("• Press S to stop BGM", (50, 560), fontsize=14, color="gray")

print("="*50)
print("音效测试程序启动")
print("请将音效文件放在 sounds/ 文件夹中")
print("="*50)
