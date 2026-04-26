"""
《Time To Sleep》- 类银河恶魔城 2D 横版游戏
开发引擎：Pygame Zero
版本：v0.1 原型
"""

import pgzrun
import random

# ==================== 游戏配置 ====================
TITLE = "Time To Sleep"
WIDTH = 960   # 游戏窗口宽度
HEIGHT = 540  # 游戏窗口高度
FPS = 60      # 帧率

# ==================== 玩家配置 ====================
PLAYER_SPEED = 4          # 移动速度
PLAYER_JUMP_FORCE = -12   # 跳跃力度
PLAYER_GRAVITY = 0.6      # 重力
PLAYER_MAX_FALL = 12      # 最大下落速度
PLAYER_HP = 50            # 初始生命值
PLAYER_MAX_HP = 50        # 最大生命值
PLAYER_ATTACK_DAMAGE = 5  # 攻击伤害
PLAYER_INVINCIBLE_TIME = 0.5  # 受击无敌时间（秒）

# ==================== 游戏状态 ====================
game_state = "playing"  # playing, paused, game_over
player = None
platforms = []
enemies = []
projectiles = []
particles = []
camera_x = 0  # 摄像机X偏移

# ==================== 玩家类 ====================
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 48
        self.vx = 0
        self.vy = 0
        self.hp = PLAYER_HP
        self.max_hp = PLAYER_MAX_HP
        self.on_ground = False
        self.facing_right = True
        self.attacking = False
        self.attack_timer = 0
        self.attack_combo = 0
        self.invincible = False
        self.invincible_timer = 0
        self.heals = 2  # 治疗次数
        self.max_heals = 4
        self.healing = False
        self.heal_timer = 0
        self.dash_cooldown = 0
        self.dashing = False
        self.dash_timer = 0
        self.dash_direction = 1
        self.animation_state = "idle"  # idle, run, jump, attack
        self.animation_frame = 0
        self.animation_timer = 0
        
    def update(self):
        # 更新无敌时间
        if self.invincible:
            self.invincible_timer -= 1 / FPS
            if self.invincible_timer <= 0:
                self.invincible = False
        
        # 更新冲刺
        if self.dashing:
            self.dash_timer -= 1 / FPS
            self.vx = self.dash_direction * 12  # 冲刺速度
            if self.dash_timer <= 0:
                self.dashing = False
        else:
            self.dash_cooldown = max(0, self.dash_cooldown - 1 / FPS)
        
        # 更新治疗
        if self.healing:
            self.heal_timer -= 1 / FPS
            self.vx = 0  # 治疗时不能移动
            if self.heal_timer <= 0:
                self.healing = False
                heal_amount = self.max_hp // 3
                self.hp = min(self.max_hp, self.hp + heal_amount)
        
        # 更新攻击
        if self.attacking:
            self.attack_timer -= 1 / FPS
            if self.attack_timer <= 0:
                self.attacking = False
                self.attack_combo = 0
        
        # 水平移动
        if not self.dashing and not self.healing:
            if keyboard.a or keyboard.left:
                self.vx = -PLAYER_SPEED
                self.facing_right = False
                self.animation_state = "run"
            elif keyboard.d or keyboard.right:
                self.vx = PLAYER_SPEED
                self.facing_right = True
                self.animation_state = "run"
            else:
                self.vx = 0
                if self.on_ground:
                    self.animation_state = "idle"
        
        # 应用重力
        if not self.dashing:
            self.vy += PLAYER_GRAVITY
            self.vy = min(self.vy, PLAYER_MAX_FALL)
        
        # 应用速度
        self.x += self.vx
        self.y += self.vy
        
        # 平台碰撞检测
        self.on_ground = False
        for platform in platforms:
            if self.collides_with(platform):
                # 从上方碰撞
                if self.vy > 0 and self.y < platform.y:
                    self.y = platform.y - self.height
                    self.vy = 0
                    self.on_ground = True
                # 从下方碰撞
                elif self.vy < 0 and self.y > platform.y:
                    self.y = platform.y + platform.height
                    self.vy = 0
                # 从左侧碰撞
                elif self.vx > 0 and self.x < platform.x:
                    self.x = platform.x - self.width
                # 从右侧碰撞
                elif self.vx < 0 and self.x > platform.x:
                    self.x = platform.x + platform.width
        
        # 边界限制
        self.x = max(0, self.x)
        
        # 更新动画
        self.update_animation()
    
    def update_animation(self):
        self.animation_timer += 1 / FPS
        if self.animation_timer >= 0.1:  # 每0.1秒切换一帧
            self.animation_frame = (self.animation_frame + 1) % 4
            self.animation_timer = 0
    
    def collides_with(self, rect):
        """检测与矩形的碰撞"""
        return (self.x < rect.x + rect.width and
                self.x + self.width > rect.x and
                self.y < rect.y + rect.height and
                self.y + self.height > rect.y)
    
    def jump(self):
        """跳跃"""
        if self.on_ground and not self.dashing and not self.healing:
            self.vy = PLAYER_JUMP_FORCE
            self.on_ground = False
            self.animation_state = "jump"
            # 创建跳跃粒子
            create_particles(self.x + self.width // 2, self.y + self.height, 5, "jump")
    
    def attack(self):
        """攻击"""
        if not self.attacking and not self.healing:
            self.attacking = True
            self.attack_timer = 0.3  # 攻击持续0.3秒
            self.attack_combo = (self.attack_combo + 1) % 3
            
            # 创建攻击判定框
            attack_range = 50 if self.facing_right else -50
            attack_x = self.x + (self.width if self.facing_right else -attack_range)
            attack_rect = Rect((attack_x, self.y + 10), (abs(attack_range), 30))
            
            # 检测击中敌人
            for enemy in enemies:
                if attack_rect.colliderect(Rect((enemy.x, enemy.y), (enemy.width, enemy.height))):
                    damage = PLAYER_ATTACK_DAMAGE * (1 + self.attack_combo * 0.2)
                    enemy.take_damage(damage)
                    # 创建击中粒子
                    create_particles(enemy.x + enemy.width // 2, enemy.y + enemy.height // 2, 8, "hit")
    
    def dash(self):
        """冲刺"""
        if self.dash_cooldown <= 0 and not self.healing:
            self.dashing = True
            self.dash_timer = 0.15  # 冲刺持续0.15秒
            self.dash_cooldown = 0.5  # 冲刺冷却0.5秒
            self.dash_direction = 1 if self.facing_right else -1
            # 创建冲刺粒子
            create_particles(self.x + self.width // 2, self.y + self.height // 2, 10, "dash")
    
    def heal(self):
        """治疗"""
        if self.heals > 0 and not self.healing and self.hp < self.max_hp:
            self.healing = True
            self.heal_timer = 1.5  # 治疗持续1.5秒
            self.heals -= 1
    
    def take_damage(self, damage):
        """受到伤害"""
        if not self.invincible and not self.dashing:
            self.hp -= damage
            self.invincible = True
            self.invincible_timer = PLAYER_INVINCIBLE_TIME
            # 创建受击粒子
            create_particles(self.x + self.width // 2, self.y + self.height // 2, 10, "damage")
            
            if self.hp <= 0:
                global game_state
                game_state = "game_over"
    
    def draw(self):
        """绘制玩家"""
        # 无敌时闪烁
        if self.invincible and int(self.invincible_timer * 10) % 2 == 0:
            return
        
        # 绘制玩家（临时使用矩形，后续替换为精灵）
        color = (100, 150, 255) if not self.healing else (100, 255, 150)
        screen.draw.filled_rect(
            Rect((self.x - camera_x, self.y), (self.width, self.height)),
            color
        )
        
        # 绘制眼睛（指示方向）
        eye_x = self.x + (24 if self.facing_right else 8) - camera_x
        screen.draw.filled_rect(
            Rect((eye_x, self.y + 10), (4, 4)),
            (255, 255, 255)
        )
        
        # 攻击动画
        if self.attacking:
            attack_range = 50 if self.facing_right else -50
            attack_x = self.x + (self.width if self.facing_right else -attack_range) - camera_x
            screen.draw.filled_rect(
                Rect((attack_x, self.y + 10), (abs(attack_range), 30)),
                (255, 255, 100, 128)
            )

# ==================== 敌人类 ====================
class Enemy:
    def __init__(self, x, y, enemy_type="patrol"):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.type = enemy_type
        self.hp = 20
        self.max_hp = 20
        self.speed = 2
        self.direction = 1
        self.patrol_start = x - 100
        self.patrol_end = x + 100
        self.attacking = False
        self.attack_timer = 0
        self.stunned = False
        self.stun_timer = 0
        self.dead = False
        
    def update(self):
        if self.dead:
            return
        
        # 更新眩晕状态
        if self.stunned:
            self.stun_timer -= 1 / FPS
            if self.stun_timer <= 0:
                self.stunned = False
            return
        
        # 巡逻型敌人
        if self.type == "patrol":
            self.x += self.speed * self.direction
            
            # 到达巡逻边界时转向
            if self.x <= self.patrol_start:
                self.direction = 1
            elif self.x >= self.patrol_end:
                self.direction = -1
        
        # 检测与玩家碰撞
        player_rect = Rect((player.x, player.y), (player.width, player.height))
        enemy_rect = Rect((self.x, self.y), (self.width, self.height))
        
        if player_rect.colliderect(enemy_rect):
            player.take_damage(10)
    
    def take_damage(self, damage):
        """受到伤害"""
        if self.stunned:
            return
        
        self.hp -= damage
        
        if self.hp <= 0:
            self.dead = True
            # 创建死亡粒子
            create_particles(self.x + self.width // 2, self.y + self.height // 2, 15, "death")
    
    def draw(self):
        """绘制敌人"""
        if self.dead:
            return
        
        # 眩晕时变灰
        if self.stunned:
            color = (150, 150, 150)
        else:
            color = (255, 100, 100)
        
        screen.draw.filled_rect(
            Rect((self.x - camera_x, self.y), (self.width, self.height)),
            color
        )
        
        # 绘制血条
        if self.hp < self.max_hp:
            bar_width = 30
            bar_height = 4
            bar_x = self.x - camera_x + (self.width - bar_width) // 2
            bar_y = self.y - 10
            
            # 背景
            screen.draw.filled_rect(
                Rect((bar_x, bar_y), (bar_width, bar_height)),
                (100, 100, 100)
            )
            
            # 血量
            hp_width = int(bar_width * (self.hp / self.max_hp))
            screen.draw.filled_rect(
                Rect((bar_x, bar_y), (hp_width, bar_height)),
                (255, 50, 50)
            )

# ==================== 平台类 ====================
class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        """绘制平台"""
        screen.draw.filled_rect(
            Rect((self.x - camera_x, self.y), (self.width, self.height)),
            (80, 80, 80)
        )
        # 顶部高亮
        screen.draw.filled_rect(
            Rect((self.x - camera_x, self.y), (self.width, 4)),
            (120, 120, 120)
        )

# ==================== 粒子系统 ====================
def create_particles(x, y, count, particle_type):
    """创建粒子效果"""
    for _ in range(count):
        particle = {
            "x": x,
            "y": y,
            "vx": (random.random() - 0.5) * 4,
            "vy": (random.random() - 0.5) * 4,
            "life": 0.5,
            "type": particle_type
        }
        particles.append(particle)

def update_particles():
    """更新粒子"""
    for particle in particles[:]:
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"]
        particle["life"] -= 1 / FPS
        
        if particle["life"] <= 0:
            particles.remove(particle)

def draw_particles():
    """绘制粒子"""
    for particle in particles:
        alpha = int(particle["life"] * 2 * 255)
        
        if particle["type"] == "hit":
            color = (255, 255, 100, alpha)
        elif particle["type"] == "death":
            color = (255, 100, 100, alpha)
        elif particle["type"] == "jump":
            color = (150, 150, 255, alpha)
        elif particle["type"] == "dash":
            color = (100, 255, 255, alpha)
        else:
            color = (255, 255, 255, alpha)
        
        screen.draw.filled_circle(
            (particle["x"] - camera_x, particle["y"]),
            3,
            color
        )

# ==================== 初始化游戏 ====================
def init_level():
    """初始化关卡"""
    global player, platforms, enemies
    
    # 创建玩家
    player = Player(100, 300)
    
    # 创建平台
    platforms = [
        Platform(0, 500, 800, 40),       # 地面
        Platform(300, 400, 200, 20),     # 平台1
        Platform(600, 320, 200, 20),     # 平台2
        Platform(900, 400, 300, 40),     # 地面2
        Platform(1000, 280, 150, 20),    # 平台3
        Platform(1300, 500, 500, 40),    # 地面3
    ]
    
    # 创建敌人
    enemies = [
        Enemy(500, 468, "patrol"),   # 地面敌人
        Enemy(1100, 468, "patrol"),  # 第二个地面敌人
    ]

# ==================== Pygame Zero 回调函数 ====================
def draw():
    """绘制游戏画面"""
    screen.fill((20, 20, 30))  # 深蓝色背景
    
    # 绘制平台
    for platform in platforms:
        platform.draw()
    
    # 绘制敌人
    for enemy in enemies:
        enemy.draw()
    
    # 绘制玩家
    if player:
        player.draw()
    
    # 绘制粒子
    draw_particles()
    
    # 绘制UI
    draw_ui()
    
    # 游戏结束画面
    if game_state == "game_over":
        screen.fill((0, 0, 0))
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 - 50),
            fontsize=60,
            color=(255, 50, 50)
        )
        screen.draw.text(
            "按 R 重新开始",
            center=(WIDTH // 2, HEIGHT // 2 + 20),
            fontsize=30,
            color=(200, 200, 200)
        )

def draw_ui():
    """绘制用户界面"""
    if not player:
        return
    
    # 左上角：生命值
    hp_bar_width = 200
    hp_bar_height = 20
    hp_bar_x = 20
    hp_bar_y = 20
    
    # 背景
    screen.draw.filled_rect(
        Rect((hp_bar_x, hp_bar_y), (hp_bar_width, hp_bar_height)),
        (50, 50, 50)
    )
    
    # 血量
    hp_width = int(hp_bar_width * (player.hp / player.max_hp))
    hp_color = (255, 50, 50) if player.hp > player.max_hp * 0.3 else (255, 150, 50)
    screen.draw.filled_rect(
        Rect((hp_bar_x, hp_bar_y), (hp_width, hp_bar_height)),
        hp_color
    )
    
    # 血量文字
    screen.draw.text(
        f"HP: {player.hp}/{player.max_hp}",
        topleft=(hp_bar_x + 5, hp_bar_y + 2),
        fontsize=14,
        color=(255, 255, 255)
    )
    
    # 右上角：治疗次数
    screen.draw.text(
        f"治疗: {'█' * player.heals}{'░' * (player.max_heals - player.heals)}",
        topright=(WIDTH - 20, 20),
        fontsize=16,
        color=(100, 255, 150)
    )
    
    # 左下角：操作提示
    screen.draw.text(
        "A/D: 移动 | Space: 跳跃 | J: 攻击 | K: 冲刺 | E: 治疗",
        bottomleft=(20, HEIGHT - 20),
        fontsize=12,
        color=(150, 150, 150)
    )

def update():
    """更新游戏逻辑"""
    global game_state, player, camera_x
    
    if game_state == "game_over":
        if keyboard.r:
            game_state = "playing"
            init_level()
        return
    
    if not player:
        return
    
    # 更新玩家
    player.update()
    
    # 更新敌人
    for enemy in enemies:
        enemy.update()
    
    # 更新粒子
    update_particles()
    
    # 更新摄像机（跟随玩家）
    target_camera_x = player.x - WIDTH // 3
    camera_x += (target_camera_x - camera_x) * 0.1

def on_key_down(key):
    """按键按下事件"""
    global game_state
    
    if game_state != "playing":
        return
    
    if key == keys.SPACE:
        player.jump()
    elif key == keys.J or key == keys.Z:
        player.attack()
    elif key == keys.K or key == keys.X:
        player.dash()
    elif key == keys.E:
        player.heal()

# ==================== 启动游戏 ====================
init_level()
pgzrun.go()
