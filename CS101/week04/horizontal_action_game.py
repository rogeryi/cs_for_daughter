# 横向闯关战斗游戏
# Side-Scroller Action Game

import pgzrun
import random

# ==================== 游戏设置 ====================
WIDTH = 900
HEIGHT = 500
TITLE = "像素勇士 - 横向闯关"

# ==================== 颜色 ====================
COLORS = {
    'sky': (135, 206, 235),
    'ground': (34, 139, 34),
    'ground_dark': (20, 100, 20),
    'player': (50, 100, 255),
    'enemy': (255, 50, 50),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gold': (255, 215, 0),
    'red': (255, 0, 0),
    'attack': (255, 255, 100),  # 攻击特效颜色
}

# ==================== 游戏变量 ====================
GROUND_Y = 400
score = 0
game_over = False
camera_x = 0

# ==================== 玩家类 ====================
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 50
        
        # 移动
        self.speed = 5
        self.facing_right = True
        
        # 跳跃
        self.jump_power = -15
        self.gravity = 0.8
        self.velocity_y = 0
        self.on_ground = False
        
        # 战斗
        self.max_hp = 100
        self.hp = 100
        self.attack_power = 20
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_duration = 15  # 攻击持续帧数
        self.attack_cooldown = 0  # 攻击冷却
        self.attack_range = 60  # 攻击范围
        self.invincible = False  # 无敌时间
        self.invincible_timer = 0
        
        # 连击
        self.combo = 0
        self.combo_timer = 0
        
    def update(self):
        """更新玩家状态"""
        global camera_x
        
        # 左右移动
        if keyboard.left:
            self.x -= self.speed
            self.facing_right = False
        if keyboard.right:
            self.x += self.speed
            self.facing_right = True
        
        # 跳跃
        if keyboard.up and self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False
        
        # 重力
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        
        # 地面碰撞
        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.on_ground = True
        
        # 攻击
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
        
        # 连击计时
        if self.combo_timer > 0:
            self.combo_timer -= 1
            if self.combo_timer <= 0:
                self.combo = 0
        
        # 无敌时间
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
        
        # 相机跟随
        camera_x = max(0, self.x - 300)
    
    def attack(self):
        """攻击"""
        if self.attack_cooldown > 0:
            return
        
        self.is_attacking = True
        self.attack_timer = self.attack_duration
        self.attack_cooldown = 20  # 冷却时间
        
        # 连击
        if self.combo_timer > 0:
            self.combo += 1
        else:
            self.combo = 1
        self.combo_timer = 60  # 1秒内连击有效
        
        # 计算实际伤害（连击加成）
        damage = self.attack_power * (1 + self.combo * 0.2)
        
        # 检测攻击范围内的敌人
        for enemy in enemies:
            if not enemy.alive:
                continue
            
            # 计算距离
            distance = abs(enemy.x - self.x)
            if distance < self.attack_range:
                # 检查方向
                if (self.facing_right and enemy.x > self.x) or \
                   (not self.facing_right and enemy.x < self.x):
                    enemy.take_damage(damage, self.facing_right)
    
    def take_damage(self, damage):
        """受到伤害"""
        if self.invincible:
            return
        
        self.hp -= damage
        self.invincible = True
        self.invincible_timer = 60  # 1秒无敌
        
        if self.hp <= 0:
            self.hp = 0
            global game_over
            game_over = True
    
    def draw(self):
        """绘制玩家"""
        screen_x = self.x - camera_x
        
        # 无敌时闪烁
        if self.invincible and self.invincible_timer % 10 < 5:
            return
        
        # 身体
        color = COLORS['player']
        screen.draw.filled_rect(
            Rect((screen_x, self.y), (self.width, self.height)),
            color
        )
        
        # 眼睛
        eye_x = screen_x + 28 if self.facing_right else screen_x + 8
        screen.draw.filled_circle((eye_x, self.y + 12), 4, COLORS['white'])
        screen.draw.filled_circle((eye_x + (2 if self.facing_right else -2), self.y + 12), 2, COLORS['black'])
        
        # 攻击特效
        if self.is_attacking:
            attack_x = screen_x + (self.width if self.facing_right else -self.attack_range)
            screen.draw.filled_rect(
                Rect((attack_x, self.y + 10), (self.attack_range, 30)),
                COLORS['attack']
            )
            
            # 连击显示
            if self.combo > 1:
                screen.draw.text(f"{self.combo} COMBO!", 
                               center=(screen_x + self.width//2, self.y - 30),
                               fontsize=20, color=COLORS['gold'])
        
        # 生命值条
        bar_width = 50
        hp_ratio = self.hp / self.max_hp
        screen.draw.filled_rect(
            Rect((screen_x, self.y - 15), (bar_width, 8)),
            (100, 100, 100)
        )
        screen.draw.filled_rect(
            Rect((screen_x, self.y - 15), (int(bar_width * hp_ratio), 8)),
            COLORS['red'] if hp_ratio < 0.3 else COLORS['gold']
        )


# ==================== 敌人类 ====================
class Enemy:
    def __init__(self, x, y, enemy_type='basic'):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.enemy_type = enemy_type
        self.alive = True
        
        # 根据类型设置属性
        if enemy_type == 'basic':
            self.max_hp = 40
            self.hp = 40
            self.attack_power = 10
            self.speed = 2
            self.color = COLORS['enemy']
        elif enemy_type == 'fast':
            self.max_hp = 30
            self.hp = 30
            self.attack_power = 8
            self.speed = 4
            self.color = (255, 150, 50)
        elif enemy_type == 'tank':
            self.max_hp = 80
            self.hp = 80
            self.attack_power = 15
            self.speed = 1
            self.color = (150, 50, 50)
        
        # AI
        self.start_x = x
        self.patrol_distance = 100
        self.direction = 1
        self.attack_cooldown = 0
        
        # 受击效果
        self.hit_timer = 0
        self.knockback = 0
        self.knockback_dir = 0
    
    def update(self):
        """更新敌人"""
        if not self.alive:
            return
        
        # 受击闪烁
        if self.hit_timer > 0:
            self.hit_timer -= 1
        
        # 击退
        if self.knockback != 0:
            self.x += self.knockback
            self.knockback *= 0.8
            if abs(self.knockback) < 1:
                self.knockback = 0
        
        # 简单巡逻AI
        self.x += self.direction * self.speed
        
        if self.x > self.start_x + self.patrol_distance:
            self.direction = -1
        elif self.x < self.start_x - self.patrol_distance:
            self.direction = 1
        
        # 攻击冷却
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        # 检测与玩家碰撞
        if self.attack_cooldown == 0:
            if abs(self.x - player.x) < 40 and abs(self.y - player.y) < 50:
                player.take_damage(self.attack_power)
                self.attack_cooldown = 60
    
    def take_damage(self, damage, facing_right):
        """受到伤害"""
        self.hp -= damage
        self.hit_timer = 10
        
        # 击退
        self.knockback = 8 if facing_right else -8
        
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            global score
            score += 100
    
    def draw(self):
        """绘制敌人"""
        if not self.alive:
            return
        
        screen_x = self.x - camera_x
        
        # 只绘制屏幕内的
        if screen_x < -50 or screen_x > WIDTH + 50:
            return
        
        # 身体（受击时闪烁白色）
        color = COLORS['white'] if self.hit_timer > 0 else self.color
        screen.draw.filled_rect(
            Rect((screen_x, self.y), (self.width, self.height)),
            color
        )
        
        # 眼睛
        screen.draw.filled_circle((screen_x + 12, self.y + 12), 4, (255, 255, 0))
        screen.draw.filled_circle((screen_x + 28, self.y + 12), 4, (255, 255, 0))
        screen.draw.filled_circle((screen_x + 12, self.y + 12), 2, COLORS['black'])
        screen.draw.filled_circle((screen_x + 28, self.y + 12), 2, COLORS['black'])
        
        # 生命值条
        if self.hp < self.max_hp:
            bar_width = 40
            hp_ratio = self.hp / self.max_hp
            screen.draw.filled_rect(
                Rect((screen_x, self.y - 10), (bar_width, 5)),
                (100, 100, 100)
            )
            screen.draw.filled_rect(
                Rect((screen_x, self.y - 10), (int(bar_width * hp_ratio), 5)),
                COLORS['red']
            )


# ==================== 创建游戏对象 ====================
player = Player(100, GROUND_Y - 50)
enemies = []

def init_level():
    """初始化关卡"""
    global enemies, score, game_over
    
    enemies.clear()
    score = 0
    game_over = False
    player.x = 100
    player.y = GROUND_Y - 50
    player.hp = player.max_hp
    
    # 创建敌人
    enemy_data = [
        (300, GROUND_Y - 40, 'basic'),
        (500, GROUND_Y - 40, 'basic'),
        (700, GROUND_Y - 40, 'fast'),
        (900, GROUND_Y - 40, 'tank'),
        (1100, GROUND_Y - 40, 'basic'),
        (1300, GROUND_Y - 40, 'fast'),
        (1500, GROUND_Y - 40, 'tank'),
    ]
    
    for x, y, etype in enemy_data:
        enemies.append(Enemy(x, y, etype))


# ==================== 绘制函数 ====================
def draw():
    # 天空
    screen.fill(COLORS['sky'])
    
    # 背景装饰
    draw_background()
    
    # 地面
    draw_ground()
    
    # 敌人
    for enemy in enemies:
        enemy.draw()
    
    # 玩家
    player.draw()
    
    # UI
    draw_ui()
    
    # 游戏结束
    if game_over:
        draw_game_over()

def draw_background():
    """绘制背景"""
    # 云朵
    for i in range(5):
        cloud_x = (i * 200 - camera_x * 0.3) % (WIDTH + 200)
        screen.draw.filled_circle((cloud_x, 80 + i * 20), 30, (255, 255, 255))
        screen.draw.filled_circle((cloud_x + 25, 70 + i * 20), 25, (255, 255, 255))

def draw_ground():
    """绘制地面"""
    screen.draw.filled_rect(
        Rect((0, GROUND_Y), (WIDTH, HEIGHT - GROUND_Y)),
        COLORS['ground']
    )
    
    # 草地纹理
    for i in range(0, WIDTH, 30):
        grass_x = i - (camera_x % 30)
        screen.draw.line((grass_x, GROUND_Y), (grass_x + 15, GROUND_Y - 8), COLORS['ground_dark'])

def draw_ui():
    """绘制UI"""
    screen.draw.text(f"分数: {score}", (10, 10), fontsize=24, color=COLORS['white'])
    screen.draw.text("← → 移动 | ↑ 跳跃 | X 攻击", (10, 40), fontsize=16, color=COLORS['white'])

def draw_game_over():
    """绘制游戏结束"""
    screen.draw.filled_rect(
        Rect((WIDTH//2 - 200, HEIGHT//2 - 100), (400, 200)),
        (0, 0, 0, 180)
    )
    screen.draw.text("游戏结束", center=(WIDTH//2, HEIGHT//2 - 40),
                    fontsize=50, color=COLORS['red'])
    screen.draw.text(f"最终分数: {score}", center=(WIDTH//2, HEIGHT//2 + 20),
                    fontsize=30, color=COLORS['white'])
    screen.draw.text("按 R 重新开始", center=(WIDTH//2, HEIGHT//2 + 70),
                    fontsize=24, color=COLORS['gold'])


# ==================== 更新函数 ====================
def update():
    if game_over:
        return
    
    player.update()
    
    for enemy in enemies:
        enemy.update()


# ==================== 输入处理 ====================
def on_key_down(key):
    global game_over
    
    if key == keys.X:
        player.attack()
    
    if key == keys.R and game_over:
        init_level()


# ==================== 启动 ====================
init_level()
pgzrun.go()
