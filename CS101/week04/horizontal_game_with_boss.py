# 横向闯关战斗游戏 - 武器系统 + Boss战
# Side-Scroller Action Game with Weapons & Boss

import pgzrun
import random
import pygame
import math

# 初始化 pygame 字体
pygame.font.init()

# ==================== 游戏设置 ====================
WIDTH = 900
HEIGHT = 500
TITLE = "像素勇士 - 武器与Boss"

# 设置中文字体
import os
import platform

# 根据操作系统选择字体路径
def get_chinese_font():
    """获取中文字体路径"""
    system = platform.system()
    
    if system == 'Darwin':  # macOS
        # macOS 系统字体
        font_paths = [
            '/System/Library/Fonts/PingFang.ttc',  # 苹方
            '/System/Library/Fonts/STHeiti Light.ttc',  # 黑体
            '/Library/Fonts/Arial Unicode.ttf',
        ]
    elif system == 'Windows':
        font_paths = [
            'C:/Windows/Fonts/msyh.ttc',  # 微软雅黑
            'C:/Windows/Fonts/simsun.ttc',  # 宋体
        ]
    else:  # Linux
        font_paths = [
            '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        ]
    
    for path in font_paths:
        if os.path.exists(path):
            return path
    
    return None  # 使用默认

CHINESE_FONT = get_chinese_font()

# 创建自定义文字绘制函数
def draw_chinese_text(text, pos, fontsize=20, color=(255, 255, 255), center=None):
    """绘制中文文字"""
    if CHINESE_FONT:
        try:
            font = pygame.font.Font(CHINESE_FONT, fontsize)
            text_surface = font.render(text, True, color)
            if center:
                text_rect = text_surface.get_rect(center=center)
                screen.surface.blit(text_surface, text_rect)
            else:
                screen.surface.blit(text_surface, pos)
        except:
            # 如果失败，使用默认方法
            if center:
                screen.draw.text(text, center=center, fontsize=fontsize, color=color)
            else:
                screen.draw.text(text, pos, fontsize=fontsize, color=color)
    else:
        # 没有中文字体，使用默认
        if center:
            screen.draw.text(text, center=center, fontsize=fontsize, color=color)
        else:
            screen.draw.text(text, pos, fontsize=fontsize, color=color)

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
    'sword': (200, 200, 255),    # 剑 - 蓝色
    'axe': (255, 150, 50),       # 斧 - 橙色
    'spear': (150, 255, 150),    # 矛 - 绿色
    'boss': (150, 0, 150),       # Boss - 紫色
    'boss_angry': (255, 0, 100), # Boss狂暴 - 深红
}

# ==================== 武器系统 ====================
WEAPONS = {
    'sword': {
        'name': '剑',
        'damage': 20,
        'range': 60,
        'cooldown': 20,
        'speed': '快',
        'color': COLORS['sword'],
        'description': '快速攻击，平衡型',
    },
    'axe': {
        'name': '斧',
        'damage': 35,
        'range': 50,
        'cooldown': 35,
        'speed': '慢',
        'color': COLORS['axe'],
        'description': '高伤害，攻击范围小',
    },
    'spear': {
        'name': '矛',
        'damage': 15,
        'range': 90,
        'cooldown': 25,
        'speed': '中',
        'color': COLORS['spear'],
        'description': '超远攻击距离',
    },
}

# ==================== 游戏变量 ====================
GROUND_Y = 400
score = 0
game_over = False
game_won = False
camera_x = 0
current_weapon = 'sword'  # 当前武器
boss_fight = False  # 是否Boss战

# 平台列表
platforms = []

# 按键状态跟踪
jump_pressed = False  # 跳跃键是否按下（当前帧）
jump_was_pressed = False  # 跳跃键上一帧状态

# 粒子系统
particles = []  # 粒子列表

def create_double_jump_effect(x, y):
    """创建二段跳特效"""
    # 创建环形粒子效果
    for i in range(12):
        angle = (i / 12) * 3.14159 * 2
        vx = math.cos(angle) * 3
        vy = math.sin(angle) * 3
        
        # 白色和金色混合
        color = (255, 255, 255) if i % 2 == 0 else (255, 215, 0)
        particles.append(Particle(
            x + 20, y + 25,  # 从玩家中心
            vx, vy,
            color,
            lifetime=20,
            size=4
        ))
    
    # 向上的粒子流
    for i in range(8):
        vx = random.uniform(-1, 1)
        vy = random.uniform(-4, -2)
        particles.append(Particle(
            x + 20 + random.uniform(-10, 10),
            y + 25,
            vx, vy,
            (200, 200, 255),
            lifetime=15,
            size=3
        ))

class Particle:
    """粒子类"""
    def __init__(self, x, y, vx, vy, color, lifetime, size=3):
        self.x = x
        self.y = y
        self.vx = vx  # x方向速度
        self.vy = vy  # y方向速度
        self.color = color
        self.lifetime = lifetime  # 存活帧数
        self.max_lifetime = lifetime
        self.size = size
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # 轻微重力
        self.lifetime -= 1
    
    def draw(self, camera_x):
        screen_x = self.x - camera_x
        alpha = self.lifetime / self.max_lifetime  # 透明度
        color = tuple(int(c * alpha) for c in self.color)
        
        # 绘制粒子
        screen.draw.filled_circle(
            (screen_x, self.y),
            self.size * alpha,
            color
        )

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
        self.jump_power = -11  # 跳跃力（固定值）
        self.velocity_y = 0
        self.on_ground = False
        self.coyote_timer = 0  # 跳跃缓冲计时器
        self.can_double_jump = True  # 是否可以二段跳
        self.has_jumped = False  # 是否已经跳跃过
        
        # 战斗 - 基础属性
        self.max_hp = 100
        self.hp = 100
        self.base_attack = 20
        
        # 武器相关
        self.current_weapon = 'sword'
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_cooldown = 0
        
        # 状态
        self.invincible = False
        self.invincible_timer = 0
        self.combo = 0
        self.combo_timer = 0
        
    def update(self):
        """更新玩家状态"""
        global camera_x, jump_pressed, jump_was_pressed
        
        # 检测跳跃按键（只在按下瞬间触发）
        jump_pressed = keyboard.up
        jump_just_pressed = jump_pressed and not jump_was_pressed
        jump_was_pressed = jump_pressed
        
        # 移动
        if keyboard.left:
            self.x -= self.speed
            self.facing_right = False
        if keyboard.right:
            self.x += self.speed
            self.facing_right = True
        
        # 边界限制 - 防止快速移动越过敌人
        if self.x < 50:
            self.x = 50
        
        # 如果没有Boss，限制玩家不能跑太远
        if not boss_fight:
            # 找到最左边的活着的敌人
            alive_enemies = [e for e in enemies if e.alive]
            if alive_enemies:
                furthest_enemy = max(e.x for e in alive_enemies)
                # 玩家不能跑过最远的敌人超过200像素
                if self.x > furthest_enemy + 200:
                    self.x = furthest_enemy + 200
                    add_log("⚠️ 先消灭前面的敌人！")
        
        # 跳跃 - 统一为短按效果，添加二段跳
        # Coyote Time - 离开平台后仍可短暂跳跃
        if self.on_ground:
            self.coyote_timer = 8  # 8帧的缓冲时间
            self.has_jumped = False  # 在地面时重置
            self.can_double_jump = True  # 重置二段跳
        else:
            if self.coyote_timer > 0:
                self.coyote_timer -= 1
        
        # 跳跃输入检测（只在按下瞬间）
        if jump_just_pressed:
            # 一段跳：在地面或Coyote Time内
            if (self.on_ground or self.coyote_timer > 0) and not self.has_jumped:
                self.velocity_y = self.jump_power
                self.on_ground = False
                self.coyote_timer = 0
                self.has_jumped = True
            # 二段跳：在空中且可以二段跳
            elif self.can_double_jump and self.has_jumped:
                self.velocity_y = self.jump_power * 0.9  # 二段跳稍弱
                self.can_double_jump = False
                self.has_jumped = True
                
                # 创建二段跳特效
                create_double_jump_effect(self.x, self.y)
        
        # 重力系统
        if self.velocity_y < 0:
            # 上升阶段
            gravity = 0.7
        else:
            # 下落阶段
            gravity = 1.2
        
        # 快速下落（按下方向键下时）
        if keyboard.down and not self.on_ground:
            gravity = 2.5
        
        self.velocity_y += gravity
        self.y += self.velocity_y
        
        # 最大下落速度限制
        if self.velocity_y > 20:
            self.velocity_y = 20
        
        # 地面碰撞
        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.on_ground = True
        
        # 平台碰撞
        for plat in platforms:
            plat_x, plat_y, plat_w, plat_h = plat
            # 检查是否在平台上方下落
            if (self.x + self.width > plat_x and 
                self.x < plat_x + plat_w and
                self.y + self.height >= plat_y and 
                self.y + self.height <= plat_y + plat_h + 10 and
                self.velocity_y >= 0):
                self.y = plat_y - self.height
                self.velocity_y = 0
                self.on_ground = True
        
        # 攻击冷却
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
        
        # 连击
        if self.combo_timer > 0:
            self.combo_timer -= 1
            if self.combo_timer <= 0:
                self.combo = 0
        
        # 无敌
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
        
        # 相机
        camera_x = max(0, self.x - 300)
    
    @property
    def weapon(self):
        """获取当前武器属性"""
        return WEAPONS[self.current_weapon]
    
    @property
    def attack_power(self):
        """当前攻击力"""
        return self.base_attack + self.weapon['damage']
    
    @property
    def attack_range(self):
        """当前攻击范围"""
        return self.weapon['range']
    
    def attack(self):
        """攻击"""
        if self.attack_cooldown > 0:
            return
        
        weapon = self.weapon
        self.is_attacking = True
        self.attack_timer = 15
        self.attack_cooldown = weapon['cooldown']
        
        # 连击
        if self.combo_timer > 0:
            self.combo += 1
        else:
            self.combo = 1
        self.combo_timer = 60
        
        # 伤害计算
        damage = self.attack_power * (1 + self.combo * 0.2)
        
        # 检测敌人
        for enemy in enemies:
            if not enemy.alive:
                continue
            
            distance = abs(enemy.x - self.x)
            if distance < self.attack_range:
                if (self.facing_right and enemy.x > self.x) or \
                   (not self.facing_right and enemy.x < self.x):
                    enemy.take_damage(damage, self.facing_right)
    
    def take_damage(self, damage):
        """受到伤害"""
        if self.invincible:
            return
        
        self.hp -= damage
        self.invincible = True
        self.invincible_timer = 60
        
        if self.hp <= 0:
            self.hp = 0
            global game_over
            game_over = True
    
    def switch_weapon(self, weapon_name):
        """切换武器"""
        if weapon_name in WEAPONS:
            self.current_weapon = weapon_name
            self.attack_cooldown = 0  # 切换时重置冷却
    
    def draw(self):
        """绘制玩家"""
        screen_x = self.x - camera_x
        
        # 无敌闪烁
        if self.invincible and self.invincible_timer % 10 < 5:
            return
        
        # 身体
        screen.draw.filled_rect(
            Rect((screen_x, self.y), (self.width, self.height)),
            COLORS['player']
        )
        
        # 眼睛
        eye_x = screen_x + 28 if self.facing_right else screen_x + 8
        screen.draw.filled_circle((eye_x, self.y + 12), 4, COLORS['white'])
        screen.draw.filled_circle((eye_x + (2 if self.facing_right else -2), self.y + 12), 2, COLORS['black'])
        
        # 武器显示
        weapon_color = self.weapon['color']
        if self.facing_right:
            weapon_x = screen_x + self.width
        else:
            weapon_x = screen_x - 10
        screen.draw.filled_rect(
            Rect((weapon_x, self.y + 15), (10, 25)),
            weapon_color
        )
        
        # 攻击特效
        if self.is_attacking:
            attack_x = screen_x + (self.width if self.facing_right else -self.attack_range)
            screen.draw.filled_rect(
                Rect((attack_x, self.y + 10), (self.attack_range, 30)),
                (*weapon_color[:3], 150)  # 半透明
            )
            
            if self.combo > 1:
                screen.draw.text(f"{self.combo} COMBO!", 
                               center=(screen_x + self.width//2, self.y - 30),
                               fontsize=20, color=COLORS['gold'])
        
        # 武器名称
        screen.draw.text(f"{self.weapon['name']}", 
                        center=(screen_x + self.width//2, self.y - 15),
                        fontsize=12, color=weapon_color)
        
        # 生命值条
        bar_width = 50
        hp_ratio = self.hp / self.max_hp
        screen.draw.filled_rect(
            Rect((screen_x, self.y - 40), (bar_width, 8)),
            (100, 100, 100)
        )
        screen.draw.filled_rect(
            Rect((screen_x, self.y - 40), (int(bar_width * hp_ratio), 8)),
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
        
        # 平台追踪
        self.current_platform = None  # 当前所在的平台
        self.platform_left = x - 100  # 巡逻左边界
        self.platform_right = x + 100  # 巡逻右边界
    
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
        
        # 平台碰撞检测 - 让敌人站在平台上
        on_platform = False
        for plat in platforms:
            plat_x, plat_y, plat_w, plat_h = plat
            # 检查敌人是否在平台上方
            if (self.x + self.width > plat_x and 
                self.x < plat_x + plat_w and
                self.y + self.height >= plat_y and 
                self.y + self.height <= plat_y + plat_h + 10):
                self.y = plat_y - self.height
                on_platform = True
                
                # 更新当前平台信息
                self.current_platform = plat
                self.platform_left = plat_x + 5  # 留一点边距
                self.platform_right = plat_x + plat_w - self.width - 5
                break
        
        # 如果没有在平台上，检查地面
        if not on_platform:
            self.current_platform = None
            if self.y < GROUND_Y - self.height:
                # 重力效果（简单的）
                self.y += 5
                if self.y >= GROUND_Y - self.height:
                    self.y = GROUND_Y - self.height
        
        # 巡逻
        self.x += self.direction * self.speed
        
        # 根据是否在平台上使用不同的边界检测
        if on_platform:
            # 在平台上：使用平台边界
            if self.x > self.platform_right:
                self.x = self.platform_right
                self.direction = -1
            elif self.x < self.platform_left:
                self.x = self.platform_left
                self.direction = 1
        else:
            # 在地面上：使用固定巡逻距离
            if self.x > self.start_x + self.patrol_distance:
                self.direction = -1
            elif self.x < self.start_x - self.patrol_distance:
                self.direction = 1
        
        # 攻击冷却
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        # 碰撞玩家
        if self.attack_cooldown == 0:
            if abs(self.x - player.x) < 40 and abs(self.y - player.y) < 50:
                player.take_damage(self.attack_power)
                self.attack_cooldown = 60
    
    def take_damage(self, damage, facing_right):
        """受到伤害"""
        self.hp -= damage
        self.hit_timer = 10
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
        
        if screen_x < -50 or screen_x > WIDTH + 50:
            return
        
        # 身体
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
        
        # 血条 - 始终显示
        bar_width = 50
        bar_height = 8
        hp_ratio = self.hp / self.max_hp
        
        # 血条背景
        screen.draw.filled_rect(
            Rect((screen_x - 5, self.y - 15), (bar_width, bar_height)),
            (80, 80, 80)
        )
        
        # 当前血量
        hp_color = COLORS['red']
        if hp_ratio > 0.6:
            hp_color = (50, 205, 50)  # 绿色
        elif hp_ratio > 0.3:
            hp_color = (255, 255, 0)  # 黄色
        
        screen.draw.filled_rect(
            Rect((screen_x - 5, self.y - 15), (int(bar_width * hp_ratio), bar_height)),
            hp_color
        )
        
        # 血条边框
        screen.draw.rect(
            Rect((screen_x - 5, self.y - 15), (bar_width, bar_height)),
            COLORS['white']
        )
        
        # 血量数值
        screen.draw.text(f"{self.hp}/{self.max_hp}", 
                        center=(screen_x + 20, self.y - 28),
                        fontsize=12, color=COLORS['white'])


# ==================== Boss类 ====================
class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 100
        self.alive = True
        
        # Boss属性
        self.max_hp = 500
        self.hp = 500
        self.attack_power = 25
        self.speed = 3
        
        # 阶段系统
        self.phase = 1  # 1-3阶段
        self.max_phase = 3
        
        # AI状态
        self.state = 'patrol'  # patrol, chase, attack
        self.attack_pattern = 0  # 攻击模式
        self.attack_cooldown = 0
        self.state_timer = 0
        
        # 受击效果
        self.hit_timer = 0
        self.is_angry = False  # 狂暴状态
    
    def update(self):
        """更新Boss"""
        if not self.alive:
            return
        
        # 受击闪烁
        if self.hit_timer > 0:
            self.hit_timer -= 1
        
        # 更新阶段
        old_phase = self.phase
        if self.hp < self.max_hp * 0.3:
            self.phase = 3
            self.is_angry = True
            self.speed = 5
            self.attack_power = 35
        elif self.hp < self.max_hp * 0.6:
            self.phase = 2
            self.speed = 4
            self.attack_power = 30
        
        if self.phase > old_phase:
            battle_log.append(f"⚠️ Boss进入第{self.phase}阶段！")
        
        # AI状态机
        self.state_timer -= 1
        if self.state_timer <= 0:
            self.choose_new_state()
        
        # 执行状态
        if self.state == 'patrol':
            self.patrol()
        elif self.state == 'chase':
            self.chase_player()
        elif self.state == 'attack':
            self.perform_attack()
        
        # 攻击冷却
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        # 碰撞玩家
        if abs(self.x - player.x) < 60 and abs(self.y - player.y) < 80:
            if self.attack_cooldown == 0:
                player.take_damage(self.attack_power)
                self.attack_cooldown = 40
    
    def choose_new_state(self):
        """选择新状态"""
        distance = abs(self.x - player.x)
        
        if distance > 300:
            self.state = 'patrol'
            self.state_timer = 60
        elif distance > 100:
            self.state = 'chase'
            self.state_timer = 90
        else:
            self.state = 'attack'
            self.state_timer = 30
            self.attack_pattern = random.randint(0, 2)
    
    def patrol(self):
        """巡逻"""
        self.x += 2
        if self.x > 1800:
            self.x = 1800
    
    def chase_player(self):
        """追击玩家"""
        if player.x > self.x:
            self.x += self.speed
        else:
            self.x -= self.speed
    
    def perform_attack(self):
        """执行攻击"""
        if self.attack_cooldown > 0:
            return
        
        # 不同阶段有不同攻击模式
        if self.phase == 1:
            # 阶段1：普通攻击
            self.attack_dash()
        elif self.phase == 2:
            # 阶段2：冲撞或震地
            if self.attack_pattern == 0:
                self.attack_dash()
            else:
                self.attack_ground_slam()
        else:
            # 阶段3：狂暴连击
            if self.attack_pattern == 0:
                self.attack_dash()
            elif self.attack_pattern == 1:
                self.attack_ground_slam()
            else:
                self.attack_combo()
        
        self.attack_cooldown = 60
    
    def attack_dash(self):
        """冲撞攻击"""
        battle_log.append("🔴 Boss冲撞！")
        direction = 1 if player.x > self.x else -1
        self.x += direction * 100
        
        # 伤害检测
        if abs(self.x - player.x) < 80:
            player.take_damage(self.attack_power)
    
    def attack_ground_slam(self):
        """震地攻击"""
        battle_log.append("💥 Boss震地！")
        # 范围伤害
        if abs(self.x - player.x) < 150:
            player.take_damage(self.attack_power * 1.5)
    
    def attack_combo(self):
        """连击"""
        battle_log.append("⚡ Boss连击！")
        for _ in range(3):
            if abs(self.x - player.x) < 100:
                player.take_damage(self.attack_power * 0.8)
    
    def take_damage(self, damage, facing_right):
        """Boss受伤"""
        self.hp -= damage
        self.hit_timer = 10
        
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            global score, game_won, boss_fight
            score += 1000
            game_won = True
            boss_fight = False
            battle_log.append("🎉 Boss被击败了！")
    
    def draw(self):
        """绘制Boss"""
        if not self.alive:
            return
        
        screen_x = self.x - camera_x
        
        # 身体（阶段3狂暴时变红）
        if self.is_angry:
            body_color = COLORS['boss_angry'] if self.hit_timer == 0 else COLORS['white']
        else:
            body_color = COLORS['boss'] if self.hit_timer == 0 else COLORS['white']
        
        screen.draw.filled_rect(
            Rect((screen_x, self.y), (self.width, self.height)),
            body_color
        )
        
        # Boss标记
        screen.draw.text("BOSS", center=(screen_x + 40, self.y - 30),
                        fontsize=20, color=COLORS['gold'])
        
        # 阶段显示
        screen.draw.text(f"Phase {self.phase}", center=(screen_x + 40, self.y - 10),
                        fontsize=14, color=COLORS['white'])
        
        # 眼睛
        screen.draw.filled_circle((screen_x + 25, self.y + 30), 8, (255, 0, 0))
        screen.draw.filled_circle((screen_x + 55, self.y + 30), 8, (255, 0, 0))
        screen.draw.filled_circle((screen_x + 25, self.y + 30), 4, COLORS['black'])
        screen.draw.filled_circle((screen_x + 55, self.y + 30), 4, COLORS['black'])
        
        # Boss血条
        bar_width = 200
        hp_ratio = self.hp / self.max_hp
        screen.draw.filled_rect(
            Rect((screen_x - 60, self.y - 50), (bar_width, 15)),
            (100, 100, 100)
        )
        screen.draw.filled_rect(
            Rect((screen_x - 60, self.y - 50), (int(bar_width * hp_ratio), 15)),
            COLORS['red']
        )
        screen.draw.text(f"Boss HP: {self.hp}/{self.max_hp}", 
                        center=(screen_x + 40, self.y - 43),
                        fontsize=12, color=COLORS['white'])


# ==================== 游戏对象 ====================
player = Player(100, GROUND_Y - 50)
enemies = []
boss = None
battle_log = []

def add_log(message):
    """添加战斗日志"""
    battle_log.append(message)
    if len(battle_log) > 5:
        battle_log.pop(0)

def init_level():
    """初始化关卡"""
    global enemies, boss, score, game_over, game_won, boss_fight, platforms
    
    enemies.clear()
    boss = None
    score = 0
    game_over = False
    game_won = False
    boss_fight = False
    battle_log.clear()
    
    player.x = 100
    player.y = GROUND_Y - 50
    player.hp = player.max_hp
    player.current_weapon = 'sword'
    
    # 创建平台
    platforms = [
        # (x, y, width, height)
        (200, 320, 120, 20),   # 第1个平台
        (400, 260, 150, 20),   # 第2个平台
        (650, 300, 100, 20),   # 第3个平台
        (850, 240, 130, 20),   # 第4个平台
        (1050, 280, 140, 20),  # 第5个平台
        (1250, 220, 120, 20),  # 第6个平台
    ]
    
    # 创建普通敌人（放在平台上）
    enemy_data = [
        (300, GROUND_Y - 40, 'basic'),
        (450, 260 - 40, 'basic'),      # 在平台上
        (700, GROUND_Y - 40, 'fast'),
        (900, 240 - 40, 'tank'),       # 在平台上
        (1100, GROUND_Y - 40, 'basic'),
        (1300, 220 - 40, 'fast'),      # 在平台上
    ]
    
    for x, y, etype in enemy_data:
        enemies.append(Enemy(x, y, etype))
    
    add_log("🎮 游戏开始！消灭所有敌人！")
    add_log("💡 按 1/2/3 切换武器 | 利用平台跳跃！")

def start_boss_fight():
    """开始Boss战"""
    global boss, boss_fight
    
    boss_fight = True
    boss = Boss(1600, GROUND_Y - 100)
    add_log("⚠️ Boss出现了！")
    add_log("💀 准备战斗！")


# ==================== 绘制函数 ====================
def draw():
    # 天空
    screen.fill(COLORS['sky'])
    
    # 背景
    draw_background()
    draw_platforms()  # 绘制平台
    draw_ground()
    
    # 敌人
    for enemy in enemies:
        enemy.draw()
    
    # Boss
    if boss:
        boss.draw()
    
    # 玩家
    player.draw()
    
    # 粒子特效（在玩家上面）
    draw_particles()
    
    # UI
    draw_ui()
    
    # 战斗日志
    draw_battle_log()
    
    # 游戏结束
    if game_over:
        draw_game_over()
    elif game_won:
        draw_game_won()

def draw_background():
    """背景"""
    for i in range(5):
        cloud_x = (i * 200 - camera_x * 0.3) % (WIDTH + 200)
        screen.draw.filled_circle((cloud_x, 80 + i * 20), 30, (255, 255, 255))
        screen.draw.filled_circle((cloud_x + 25, 70 + i * 20), 25, (255, 255, 255))

def update_particles():
    """更新粒子"""
    global particles
    
    # 更新所有粒子
    for p in particles:
        p.update()
    
    # 移除死亡粒子
    particles = [p for p in particles if p.lifetime > 0]

def draw_particles():
    """绘制粒子"""
    for p in particles:
        p.draw(camera_x)

def draw_platforms():
    """绘制平台"""
    for plat in platforms:
        plat_x, plat_y, plat_w, plat_h = plat
        screen_x = plat_x - camera_x
        
        # 只绘制屏幕内的平台
        if screen_x + plat_w < 0 or screen_x > WIDTH:
            continue
        
        # 平台主体
        screen.draw.filled_rect(
            Rect((screen_x, plat_y), (plat_w, plat_h)),
            (139, 69, 19)  # 棕色
        )
        
        # 平台边框
        screen.draw.rect(
            Rect((screen_x, plat_y), (plat_w, plat_h)),
            (160, 82, 45)
        )

def draw_ground():
    """地面"""
    screen.draw.filled_rect(
        Rect((0, GROUND_Y), (WIDTH, HEIGHT - GROUND_Y)),
        COLORS['ground']
    )
    for i in range(0, WIDTH, 30):
        grass_x = i - (camera_x % 30)
        screen.draw.line((grass_x, GROUND_Y), (grass_x + 15, GROUND_Y - 8), COLORS['ground_dark'])

def draw_ui():
    """UI"""
    # 添加半透明背景让文字更清晰
    screen.draw.filled_rect(
        Rect((5, 5), (400, 60)),
        (0, 0, 0, 150)
    )
    
    draw_chinese_text(f"分数: {score}", (10, 10), fontsize=24, color=(255, 255, 255))
    draw_chinese_text(f"武器: {player.weapon['name']} [1/2/3切换]", (10, 35), 
                    fontsize=16, color=player.weapon['color'])
    
    # 任务提示
    draw_objective()
    
    # 操作提示背景
    screen.draw.filled_rect(
        Rect((5, HEIGHT - 35), (400, 30)),
        (0, 0, 0, 150)
    )
    draw_chinese_text("← → 移动 | ↑ 跳跃(可二段跳) | X 攻击", (10, HEIGHT - 30), 
                    fontsize=14, color=(255, 255, 255))

def draw_objective():
    """绘制目标任务"""
    if game_over or game_won:
        return
    
    # 确定当前目标
    if boss_fight:
        objective = "👹 击败Boss！"
        obj_color = (255, 0, 0)
    else:
        alive_count = sum(1 for e in enemies if e.alive)
        if alive_count > 0:
            objective = f"⚔️ 消灭敌人！剩余 {alive_count} 个"
            obj_color = (255, 215, 0)
        else:
            objective = "⚠️ Boss即将出现！"
            obj_color = (255, 0, 0)
    
    # 绘制在屏幕右上角
    draw_chinese_text(objective, (WIDTH - 350, 10), fontsize=18, color=obj_color)
    
    # 如果没有Boss，显示敌人方向指示
    if not boss_fight:
        alive_enemies = [e for e in enemies if e.alive]
        if alive_enemies:
            # 找到最近的敌人
            nearest = min(alive_enemies, key=lambda e: abs(e.x - player.x))
            
            # 如果敌人在屏幕外，显示箭头
            enemy_screen_x = nearest.x - camera_x
            if enemy_screen_x < 0 or enemy_screen_x > WIDTH:
                arrow_x = WIDTH - 50 if enemy_screen_x > WIDTH else 30
                arrow_dir = "→" if enemy_screen_x > WIDTH else "←"
                distance = int(abs(nearest.x - player.x) / 10)
                
                draw_chinese_text(f"{arrow_dir} {distance}m", 
                               center=(arrow_x, HEIGHT // 2),
                               fontsize=30, color=(255, 215, 0))

def draw_battle_log():
    """战斗日志"""
    log_y = 80
    for i, log in enumerate(battle_log):
        draw_chinese_text(log, (10, log_y + i * 20), fontsize=14, color=(255, 255, 255))

def draw_game_over():
    """游戏结束"""
    screen.draw.filled_rect(
        Rect((WIDTH//2 - 200, HEIGHT//2 - 100), (400, 200)),
        (0, 0, 0, 180)
    )
    draw_chinese_text("游戏结束", center=(WIDTH//2, HEIGHT//2 - 40),
                    fontsize=50, color=(255, 0, 0))
    draw_chinese_text(f"最终分数: {score}", center=(WIDTH//2, HEIGHT//2 + 20),
                    fontsize=30, color=(255, 255, 255))
    draw_chinese_text("按 R 重新开始", center=(WIDTH//2, HEIGHT//2 + 70),
                    fontsize=24, color=(255, 215, 0))

def draw_game_won():
    """游戏胜利"""
    screen.draw.filled_rect(
        Rect((WIDTH//2 - 200, HEIGHT//2 - 100), (400, 200)),
        (0, 0, 0, 180)
    )
    draw_chinese_text("🎉 胜利！", center=(WIDTH//2, HEIGHT//2 - 40),
                    fontsize=50, color=(255, 215, 0))
    draw_chinese_text(f"最终分数: {score}", center=(WIDTH//2, HEIGHT//2 + 20),
                    fontsize=30, color=(255, 255, 255))
    draw_chinese_text("按 R 重新开始", center=(WIDTH//2, HEIGHT//2 + 70),
                    fontsize=24, color=(255, 215, 0))


# ==================== 更新函数 ====================
def update():
    if game_over or game_won:
        return
    
    player.update()
    
    for enemy in enemies:
        enemy.update()
    
    if boss:
        boss.update()
    
    # 更新粒子
    update_particles()
    
    # 检查是否触发Boss战
    if not boss_fight and all(not e.alive for e in enemies):
        start_boss_fight()


# ==================== 输入处理 ====================
def on_key_down(key):
    global game_over
    
    # 攻击
    if key == keys.X:
        player.attack()
    
    # 切换武器
    if key == keys.K_1:
        player.switch_weapon('sword')
        add_log("🔵 切换武器：剑")
    if key == keys.K_2:
        player.switch_weapon('axe')
        add_log("🟠 切换武器：斧")
    if key == keys.K_3:
        player.switch_weapon('spear')
        add_log("🟢 切换武器：矛")
    
    # 重新开始
    if key == keys.R and (game_over or game_won):
        init_level()


# ==================== 启动 ====================
init_level()
pgzrun.go()
