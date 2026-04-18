# 天哪，是五彩缤纷的天降救世主😱
# Oh My, The Colorful Savior From The Sky 😱

import random
import time

def story_print(texts):
    """故事文本逐行显示（按回车继续）"""
    for line in texts:
        if line == "":
            print()
        else:
            print(line)
            input("▶ ")

class Character:
    """角色基类"""
    def __init__(self, name, hp, attack, defense, element, role="输出", is_boss=False):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.role = role
        self.is_boss = is_boss
        self.alive = True
        self.shield = 0  # 护盾
        self.buff_attack = 0  # 攻击增益
        self.debuff_defense = 0  # 防御削弱
        self.is_frozen = False  # 是否被冻结
        self.weakness_mark = None  # 弱点标记
        self.energy = 50  # 初始能量
        self.max_energy = 100  # 最大能量
        self.resurrection_used = False  # 复活恩典是否已使用（每关限一次）
        self.has_weakness_reveal = False  # 是否已显示弱点（生命之雨效果）
    
    def take_damage(self, damage, attack_element=None):
        """受到伤害"""
        if self.is_frozen:
            self.is_frozen = False
            print(f"  ❄️ {self.name} 被冻结，无法行动！")
            return 0
        
        # 元素克制
        if attack_element:
            multiplier = get_element_multiplier(attack_element, self.element)
            damage = int(damage * multiplier)
        
        # 弱点标记
        if self.weakness_mark:
            damage = int(damage * 1.3)
        
        # 防御计算
        actual_damage = max(1, damage - self.defense - self.debuff_defense)
        
        # 护盾吸收
        if self.shield > 0:
            if self.shield >= actual_damage:
                self.shield -= actual_damage
                print(f"  🛡️ 护盾吸收了 {actual_damage} 点伤害")
                actual_damage = 0
            else:
                actual_damage -= self.shield
                print(f"  🛡️ 护盾破碎！")
                self.shield = 0
        
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        
        return actual_damage
    
    def recover_energy(self, amount):
        """恢复能量"""
        self.energy = min(self.max_energy, self.energy + amount)
    
    def use_skill(self, energy_cost):
        """尝试使用技能"""
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            return True
        return False
    
    def attack_target(self, target, element_choice=None, skill_name="攻击"):
        """攻击目标"""
        attack_element = element_choice if element_choice else self.element
        damage = self.attack + self.buff_attack
        
        # 随机浮动 ±10%
        damage = int(damage * random.uniform(0.9, 1.1))
        
        actual_damage = target.take_damage(damage, attack_element)
        
        if actual_damage > 0:
            if attack_element and attack_element != "无":
                print(f"  ⚔️ {skill_name} 造成 {actual_damage} 点{attack_element}属性伤害")
            else:
                print(f"  ⚔️ {skill_name} 造成 {actual_damage} 点伤害")
        
        return actual_damage


class Game:
    def __init__(self):
        self.player = None
        self.player_name = ""
        self.player_gender = ""
        self.all_companions = []
        self.active_companions = []
        self.turn = 0
        self.enemies = []
        self.achievements = []
        self.colors_collected = []
        self.attack_count = 0  # 攻击计数（用于第二关Boss机制）
        
    def start(self):
        """游戏开始"""
        print("="*70)
        print(" "*15 + "🌈 天哪，是五彩缤纷的天降救世主 😱 🌈")
        print("="*70)
        print()
        
        story = [
            "曾经",
            "源彩大陆,还是一个五彩缤纷的世界。",
            "这里的居民热爱艺术、色彩和设计。",
            "",
            "直到有一天，一个黑白的影子出现，",
            "夺走了大陆上的所有色彩和创造。",
            "于是世界变成了黑白。"
        ]
        
        story_print(story)
        print()
        
        # 创建角色
        self.create_character()
        
        story = [
            "过了很久，在这个黑白世界中，",
            f"一个五彩的人突然到来——{self.player_name}",
            "",
            "「我一定会为大家夺回应有的颜色！」"
        ]
        
        story_print(story)
        print()
        input("按回车键开始冒险...")
        print()
        
        # 创建主角
        self.player = Character(self.player_name, 100, 15, 5, "黄", "输出")
        
        # 游戏流程（按plan.md）
        self.tutorial()  # 新手教程（3回合）
        self.rest_phase("序幕")  # 招募芙丽雅
        self.recruit_companion(1)
        
        self.battle_stage(1, "大地的回响", "黄", 5)  # 第一关（5回合）
        self.rest_phase("第一关后")  # 招募阿卡列
        self.recruit_companion(2)
        
        self.battle_stage(2, "火焰的怒嚎", "红", 6)  # 第二关（6回合）
        self.rest_phase("第二关后")  # 招募厄希斯
        self.recruit_companion(3)
        
        self.battle_stage(3, "大海的咆哮", "蓝", 7)  # 第三关（7回合）
        self.rest_phase("决战前夕")  # 招募莱因克雷德
        self.recruit_companion(4)
        
        # 最终决战
        self.final_battle()
        
        # 结算
        self.check_achievements()
    
    def create_character(self):
        """创建角色"""
        print("="*70)
        print("  📝 创建你的角色")
        print("="*70)
        print()
        
        self.player_name = input("请输入你的名字: ")
        self.player_gender = input("请选择性别 (男/女): ")
        
        print()
        print(f"欢迎你， {self.player_name}！")
        print(f"基础属性: HP: 100 | 攻击: 15 | 防御: 5")
        print()
        input("按回车键继续...")
        print()
    
    def tutorial(self):
        """新手教程（3回合，无Boss）"""
        print("-"*70)
        print("📖 新手教程")
        print("-"*70)
        print()
        
        # 询问是否跳过
        skip = input("是否跳过新手教程？(yes/no): ")
        if skip.lower() == "yes":
            print("已跳过教程")
            print()
            return
        
        story = [
            "【元素克制关系】",
            "  🔴 红 克制 🟡 黄",
            "  🟡 黄 克制 🔵 蓝",
            "  🔵 蓝 克制 🔴 红",
            "",
            "【战斗规则】",
            "- 回合制战斗，每回合选择行动和技能",
            "- 利用元素克制可以造成 1.5 倍伤害",
            "- 被克制只能造成 0.7 倍伤害",
            "- 场上最多4名友方同时作战",
            "- 使用技能需要消耗能量",
            "- 普攻恢复10能量，每回合自然恢复5能量",
            "",
            "【你的技能】",
            "  ⚔️ 利刃斩击 - 无属性普攻，不受克制影响",
            "  💪 力量祝福 - 增强指定队友的攻击力",
            "  😱 恐惧光环 - 削弱指定敌人的防御力",
            "  🌧️ 生命之雨 - 全员治疗并揭示敌人弱点"
        ]
        
        story_print(story)
        print()
        input("按回车键继续...")
        print()
        
        # 3个回合的新手战斗
        print("="*70)
        print("  新手训练战")
        print("="*70)
        print()
        
        for turn in range(1, 4):
            print(f"--- 回合 {turn}/3 ---")
            self.enemies = [Character(f"训练木桩{turn}", 30, 5, 2, "黄")]
            print(f"  出现了训练木桩！")
            print()
            
            while any(e.alive for e in self.enemies):
                self.battle_turn(is_tutorial=True)
            
            print(f"✅ 训练完成！")
            print()
    
    def rest_phase(self, phase_name):
        """休息时刻"""
        print()
        print("="*70)
        print(f"  ☕ 休息时刻 - {phase_name}")
        print("="*70)
        print()
        
        # 恢复生命
        heal = 30
        self.player.hp = min(self.player.max_hp, self.player.hp + heal)
        print(f"{self.player_name} 恢复了 {heal} 点生命，当前 HP: {self.player.hp}/{self.player.max_hp}")
        
        for companion in self.all_companions:
            companion.hp = min(companion.max_hp, companion.hp + heal)
            print(f"{companion.name} 恢复了 {heal} 点生命，当前 HP: {companion.hp}/{companion.max_hp}")
        
        print()
        input("按回车键继续...")
        print()
    
    def recruit_companion(self, stage):
        """招募伙伴"""
        print()
        print("="*70)
        print("  🤝 遇见新伙伴")
        print("="*70)
        print()
        
        companions_data = {
            1: {
                "name": "芙丽雅",
                "char": Character("芙丽雅", 70, 10, 5, "黄", "治疗"),
                "dialogue": [
                    "一个穿着白色长袍的女子站在你面前。",
                    "她双手合十，眼中闪烁着圣光。",
                    "",
                    "芙丽雅: 「我是侍奉圣光的神职人员，芙丽雅。」",
                    "芙丽雅: 「我能感受到你身上的色彩之力。」",
                    "芙丽雅: 「让我加入你吧，我会用圣愈之光守护大家。」",
                    "",
                    "「她的技能:」",
                    "  💚 圣愈之光 - 单体治疗",
                    "  ⚔️ 感恩吧 - 无属性攻击",
                    "  🙏 慈悲祷言 - 群体恢复",
                    "  🛡️ 神圣庇护 - 施加护盾",
                    "",
                    "「你的技能:」",
                    "  ⚔️ 利刃斩击 - 普攻，无属性",
                    "  💪 力量祝福 - 增强队友攻击",
                    "  😱 恐惧光环 - 削弱敌人防御",
                    "  🌧️ 生命之雨 - 全员治疗+显示弱点"
                ]
            },
            2: {
                "name": "阿卡列",
                "char": Character("阿卡列", 80, 18, 6, "红", "输出"),
                "dialogue": [
                    "一个身经百战的剑士靠在墙边，",
                    "他的剑上刻满了战斗的痕迹。",
                    "",
                    "阿卡列: 「我是阿卡列，流浪的剑士。」",
                    "阿卡列: 「这个世界失去色彩后，战斗也变得无趣。」",
                    "阿卡列: 「如果你想夺回颜色，我的剑愿意为你而战。」",
                    "",
                    "「他的技能:」",
                    "  ⚔️ 断钢斩 - 破甲一击",
                    "  💀 血偿 - 以伤换伤",
                    "  🔪 追命连斩 - 连续追击",
                    "  ⚡ 死线 - 蓄力必杀"
                ]
            },
            3: {
                "name": "厄希斯",
                "char": Character("厄希斯", 100, 12, 12, "蓝", "防御"),
                "dialogue": [
                    "一个神秘的魔女从阴影中走出，",
                    "她周身环绕着冰晶与魔法的辉光。",
                    "",
                    "厄希斯: 「我是厄希斯，隐居的魔女。」",
                    "厄希斯: 「我已经很久没有见过外人了。」",
                    "厄希斯: 「但你的使命让我感兴趣，我会用禁忌秘术助你。」",
                    "",
                    "「她的技能:」",
                    "  🔥 于火中焚烧 - 红色属性攻击",
                    "  ❄️ 霜骨壁垒 - 冰晶防护墙",
                    "  🧵 命运纺线 - 伤害转移",
                    "  🛡️ 终焉之茧 - 终极防御"
                ]
            },
            4: {
                "name": "莱因克雷德",
                "char": Character("莱因克雷德", 75, 11, 7, "黄", "辅助"),
                "dialogue": [
                    "一个戴着眼镜的学者从书堆中抬起头，",
                    "他的桌上摆满了古老的卷轴和炼金药剂。",
                    "",
                    "莱因克雷德: 「啊，你就是那位传说中的救世主？」",
                    "莱因克雷德: 「我是莱因克雷德，研究古代语的学者。」",
                    "莱因克雷德: 「我的知识和炼金术会在战场上帮助你们。」",
                    "",
                    "「他的技能:」",
                    "  🔍 解析之眼 - 洞察弱点",
                    "  🧪 活性秘药 - 强化药剂",
                    "  📚 知识共鸣 - 全队增益",
                    "  ⚓ 重力锚定 - 束缚敌人"
                ]
            }
        }
        
        if stage in companions_data:
            data = companions_data[stage]
            
            # 显示对话
            story_print(data["dialogue"])
            print()
            
            # 询问是否招募
            print("="*70)
            recruit = input(f"是否招募 {data['name']}？(yes/no): ")
            print("="*70)
            print()
            
            if recruit.lower() == "yes":
                companion = data["char"]
                self.all_companions.append(companion)
                
                if len(self.active_companions) < 4:
                    self.active_companions.append(companion)
                
                print(f"✅ {companion.name} 加入了队伍！")
                print(f"  定位: {companion.role}")
                print(f"  HP: {companion.hp} | 攻击: {companion.attack} | 防御: {companion.defense}")
                print(f"  元素: {companion.element}")
                print()
                
                dialogues_accept = {
                    1: "芙丽雅: 「感恩吧，我会尽全力治愈大家！」",
                    2: "阿卡列: 「好，那就让我们一起战斗！」",
                    3: "厄希斯: 「有趣的选择，我不会让你失望的。」",
                    4: "莱因克雷德: 「明智的决定，知识就是力量！」"
                }
                
                if stage in dialogues_accept:
                    print(dialogues_accept[stage])
            else:
                print(f"❌ 你决定不招募 {data['name']}。")
                print()
                
                dialogues_reject = {
                    1: "芙丽雅: 「没关系，愿圣光保佑你。」",
                    2: "阿卡列: 「哼，随你吧。保重。」",
                    3: "厄希斯: 「你会后悔的，但这是你的选择。」",
                    4: "莱因克雷德: 「理解，独自旅行确实需要勇气。」"
                }
                
                if stage in dialogues_reject:
                    print(dialogues_reject[stage])
            
            print()
            input("按回车键继续...")
            print()
    
    def battle_stage(self, stage_num, stage_name, element, max_turns):
        """关卡战斗"""
        print()
        print("="*70)
        print(f"  ⚔️ 第{stage_num}关：{stage_name}")
        print(f"  目标颜色: {element}")
        print("="*70)
        print()
        
        self.colors_collected.append(element)
        
        # 战斗开始前询问是否操控队友
        self.control_mode = "ai"  # 默认AI模式
        if self.active_companions:
            print("【战斗设置】")
            control = input("是否手动操控队友？(yes/no): ")
            if control.lower() == "yes":
                self.control_mode = "manual"
                print("✅ 已切换为手动操控模式")
            else:
                print("✅ 队友将由AI自动控制")
            print()
        
        # 定义每关的敌人
        enemies_data = self.get_enemies_by_stage(stage_num, element)
        
        for turn in range(1, max_turns + 1):
            self.turn = turn
            print(f"--- 回合 {turn}/{max_turns} ---")
            
            # 最后一个回合是Boss
            if turn == max_turns:
                self.enemies = [enemies_data["boss"]]
                print(f"  👑 Boss 出现了：{self.enemies[0].name}！")
            else:
                # 从普通敌人中随机选择
                normal_enemies = enemies_data["normal"]
                enemy_count = random.randint(1, min(3, len(normal_enemies)))
                self.enemies = []
                for i in range(enemy_count):
                    enemy = normal_enemies[(turn + i) % len(normal_enemies)]
                    self.enemies.append(Character(
                        enemy["name"], enemy["hp"], enemy["attack"], 
                        enemy["defense"], enemy["element"], "输出"
                    ))
                print(f"  出现了 {enemy_count} 个敌人！")
            
            print()
            
            # 战斗回合
            while any(e.alive for e in self.enemies) and self.player.alive:
                self.battle_turn()
            
            # 检查是否团灭
            if not self.player.alive and not any(c.alive for c in self.active_companions):
                print("\n💀 你被打败了...")
                print("但是色彩的力量让你重新站了起来！")
                self.player.hp = 50
                self.player.alive = True
                for c in self.active_companions:
                    c.hp = 30
                    c.alive = True
                print("全员复活！继续战斗！")
                input("按回车键继续...")
                return
        
        print(f"\n✅ 第{stage_num}关完成！获得颜色：{element}")
        input("按回车键继续...")
        print()
    
    def get_enemies_by_stage(self, stage_num, element):
        """根据关卡获取敌人数据"""
        if stage_num == 1:
            return {
                "normal": [
                    {"name": "岩壳甲虫", "hp": 40, "attack": 10, "defense": 8, "element": "黄"},
                    {"name": "砂尘精灵", "hp": 30, "attack": 12, "defense": 4, "element": "黄"},
                    {"name": "黄铜魔像", "hp": 50, "attack": 14, "defense": 10, "element": "黄"},
                ],
                "boss": Character("「亘古岩心」戈尔姆", 100, 20, 12, "黄", "输出", is_boss=True)
            }
        elif stage_num == 2:
            return {
                "normal": [
                    {"name": "烬灰小鬼", "hp": 35, "attack": 13, "defense": 3, "element": "红"},
                    {"name": "熔岩史莱姆", "hp": 45, "attack": 11, "defense": 6, "element": "红"},
                    {"name": "焦骨战士", "hp": 40, "attack": 15, "defense": 7, "element": "红"},
                ],
                "boss": Character("「焚世者」伊格尼图斯", 120, 22, 10, "红", "输出", is_boss=True)
            }
        else:
            return {
                "normal": [
                    {"name": "潮行鱼人", "hp": 38, "attack": 12, "defense": 5, "element": "蓝"},
                    {"name": "浮游水母群", "hp": 32, "attack": 14, "defense": 4, "element": "蓝"},
                    {"name": "沉船怨灵", "hp": 42, "attack": 13, "defense": 6, "element": "蓝"},
                ],
                "boss": Character("「深渊之主」塔拉萨", 140, 24, 11, "蓝", "输出", is_boss=True)
            }
    
    def battle_turn(self, is_tutorial=False):
        """战斗回合"""
        # 玩家回合
        print("\n【你的回合】")
        print(f"HP: {self.player.hp}/{self.player.max_hp} | 能量: {self.player.energy}/{self.player.max_energy}")
        print()
        
        alive_enemies = [e for e in self.enemies if e.alive]
        if not alive_enemies:
            return
        
        print("敌人：")
        for i, enemy in enumerate(alive_enemies):
            boss_tag = " 👑" if enemy.is_boss else ""
            print(f"  {i+1}. {enemy.name}{boss_tag} - HP: {enemy.hp} | 元素: {enemy.element}")
        print()
        
        # 选择行动
        print("选择行动：")
        print("  1. ⚔️ 利刃斩击（普攻，无属性）")
        print("  2. 💪 力量祝福（20能量，增强队友攻击力）")
        print("  3. 😱 恐惧光环（20能量，削弱敌人防御力）")
        print("  4. 🌧️ 生命之雨（30能量，全员治疗+显示敌人弱点）")
        print()
        
        action_choice = input("请选择 (1/2/3/4): ")
        
        if action_choice == "1":
            # 利刃斩击 - 普攻，无属性
            print("\n选择目标：")
            for i, enemy in enumerate(alive_enemies):
                boss_tag = " 👑" if enemy.is_boss else ""
                print(f"  {i+1}. {enemy.name}{boss_tag} - HP: {enemy.hp}")
            target_idx = int(input(f"选择目标 (1-{len(alive_enemies)}): ")) - 1
            target = alive_enemies[target_idx]
            
            # 无属性攻击，不受元素克制影响
            damage = self.player.attack + self.player.buff_attack
            damage = int(damage * random.uniform(0.9, 1.1))
            actual_damage = target.take_damage(damage)
            
            print(f"  ⚔️ 利刃斩击 - 造成 {actual_damage} 点无属性伤害")
            self.player.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量，当前: {self.player.energy}/{self.player.max_energy}")
            
            if not target.alive:
                print(f"  ✨ {target.name} 被击败了！")
        
        elif action_choice == "2":
            # 力量祝福 - 辅助，增强队友攻击力
            if self.player.use_skill(20):
                print("\n选择祝福目标：")
                targets = [self.player] + [c for c in self.active_companions if c.alive]
                for i, target in enumerate(targets):
                    self_tag = " (自己)" if target == self.player else ""
                    print(f"  {i+1}. {target.name}{self_tag} - 当前攻击: {target.attack + target.buff_attack}")
                target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
                target = targets[target_idx]
                
                target.buff_attack += 10
                print(f"  💪 力量祝福 - {target.name} 的攻击力提升 10 点！")
                print(f"  当前攻击力: {target.attack + target.buff_attack}")
            else:
                print("  能量不足！")
        
        elif action_choice == "3":
            # 恐惧光环 - 辅助，削弱敌人防御力
            if self.player.use_skill(20):
                print("\n选择恐惧目标：")
                for i, enemy in enumerate(alive_enemies):
                    boss_tag = " 👑" if enemy.is_boss else ""
                    print(f"  {i+1}. {enemy.name}{boss_tag}")
                target_idx = int(input(f"选择 (1-{len(alive_enemies)}): ")) - 1
                target = alive_enemies[target_idx]
                
                target.debuff_defense += 8
                print(f"  😱 恐惧光环 - {target.name} 的防御力降低 8 点！")
            else:
                print("  能量不足！")
        
        elif action_choice == "4":
            # 生命之雨 - 治疗全员+显示敌人弱点
            if self.player.use_skill(30):
                # 全员治疗
                heal_amount = 15
                all_targets = [self.player] + [c for c in self.active_companions if c.alive]
                for target in all_targets:
                    target.hp = min(target.max_hp, target.hp + heal_amount)
                    print(f"  🌧️ {target.name} 恢复了 {heal_amount} HP")
                
                # 显示敌人弱点
                print("\n  🔍 生命之雨揭示了敌人的弱点：")
                for enemy in alive_enemies:
                    if enemy.weakness_mark is None:
                        enemy.weakness_mark = random.choice(["红", "黄", "蓝"])
                        boss_tag = " 👑" if enemy.is_boss else ""
                        print(f"  {enemy.name}{boss_tag} 的弱点是: {enemy.weakness_mark}属性伤害+30%")
                    else:
                        boss_tag = " 👑" if enemy.is_boss else ""
                        print(f"  {enemy.name}{boss_tag} 的弱点已知: {enemy.weakness_mark}属性")
                
                print(f"  🌧️ 生命之雨 - 全员恢复了 {heal_amount} HP 并揭示了敌人弱点！")
            else:
                print("  能量不足！")
        
        else:
            print("  无效选择，执行普通攻击")
            target = alive_enemies[0]
            self.player.attack_target(target, skill_name="利刃斩击")
            self.player.recover_energy(10)
        
        # 伙伴回合
        for companion in self.active_companions:
            if companion.alive:
                print(f"\n【{companion.name} 的回合】")
                print(f"  HP: {companion.hp}/{companion.max_hp} | 能量: {companion.energy}/{companion.max_energy}")
                
                # 检查是否有队友阵亡，触发复活恩典
                self.check_resurrection(companion)
                
                # 根据控制模式决定
                if self.control_mode == "manual" and alive_enemies:
                    # 手动操控
                    self.player_control_companion(companion, alive_enemies)
                else:
                    # AI自动行动
                    self.companion_action(companion, alive_enemies)
                
                # 自然恢复5能量
                companion.recover_energy(5)
                
                alive_enemies = [e for e in self.enemies if e.alive]
                if not alive_enemies:
                    break
        
        # 敌人回合
        if any(e.alive for e in self.enemies):
            print("\n【敌人回合】")
            for enemy in self.enemies:
                if enemy.alive:
                    targets = [self.player] + [c for c in self.active_companions if c.alive]
                    if targets:
                        target = random.choice(targets)
                        print(f"{enemy.name} 攻击 {target.name}：")
                        enemy.attack_target(target, enemy.element)
                        if not target.alive:
                            print(f"  💀 {target.name} 倒下了！")
        
        print()
        time.sleep(0.5)
    
    def player_control_companion(self, companion, alive_enemies):
        """玩家手动操控队友"""
        print(f"\n选择 {companion.name} 的行动:")
        print("  1. ⚔️ 攻击")
        print("  2. 🎯 使用技能")
        print("  3. ⏸️ 防御（本回合受到的伤害减半）")
        print()
        
        choice = input("请选择 (1/2/3): ")
        
        if choice == "1":
            # 攻击
            print("选择攻击元素：")
            print("  1. 🔴 红")
            print("  2. 🟡 黄")
            print("  3. 🔵 蓝")
            element_choice = input("请选择 (1/2/3): ")
            
            element_map = {"1": "红", "2": "黄", "3": "蓝"}
            attack_element = element_map.get(element_choice, companion.element)
            
            print("\n选择目标：")
            for i, enemy in enumerate(alive_enemies):
                boss_tag = " 👑" if enemy.is_boss else ""
                print(f"  {i+1}. {enemy.name}{boss_tag} - HP: {enemy.hp} | 元素: {enemy.element}")
            
            target_idx = int(input(f"选择目标 (1-{len(alive_enemies)}): ")) - 1
            target = alive_enemies[target_idx]
            
            companion.attack_target(target, attack_element, "攻击")
            companion.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量，当前: {companion.energy}/{companion.max_energy}")
            
        elif choice == "2":
            # 使用技能（根据角色定位）
            if companion.role == "治疗":
                self.use_healer_skill(companion, alive_enemies)
            elif companion.role == "输出":
                self.use_dps_skill(companion, alive_enemies)
            elif companion.role == "防御":
                self.use_defender_skill(companion, alive_enemies)
            elif companion.role == "辅助":
                self.use_support_skill(companion, alive_enemies)
        elif choice == "3":
            # 防御
            companion.shield += 10
            print(f"  🛡️ {companion.name} 进入防御姿态，获得 10 点护盾")
            companion.recover_energy(5)
    
    def use_healer_skill(self, companion, alive_enemies):
        """治疗者技能"""
        print(f"\n{companion.name} 的技能:")
        print("  1. 💚 圣愈之光 (20能量) - 单体治疗（可对自己使用）")
        print("  2. 🛡️ 神圣庇护 (25能量) - 施加护盾（可对自己使用）")
        print("  3. 🔥 净化之焰 (20能量) - 驱散负面状态")
        print()
        
        skill = input("选择技能 (1/2/3): ")
        
        # 包括自己
        targets = [companion] + [self.player] + [c for c in self.active_companions if c.alive and c != companion]
        
        if skill == "1" and companion.use_skill(20):
            print("\n选择治疗目标：")
            for i, target in enumerate(targets):
                hp_bar = f"HP: {target.hp}/{target.max_hp}"
                self_tag = " (自己)" if target == companion else ""
                print(f"  {i+1}. {target.name}{self_tag} - {hp_bar}")
            target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
            target = targets[target_idx]
            
            heal = int(companion.attack * 1.5)
            target.hp = min(target.max_hp, target.hp + heal)
            print(f"  💚 圣愈之光 - 为 {target.name} 恢复了 {heal} HP")
            
        elif skill == "2" and companion.use_skill(25):
            print("\n选择护盾目标：")
            for i, target in enumerate(targets):
                self_tag = " (自己)" if target == companion else ""
                print(f"  {i+1}. {target.name}{self_tag}")
            target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
            target = targets[target_idx]
            
            target.shield += 25
            print(f"  🛡️ 神圣庇护 - 为 {target.name} 添加了 25 点护盾")
            
        elif skill == "3" and companion.use_skill(20):
            print("\n选择净化目标：")
            for i, target in enumerate(targets):
                self_tag = " (自己)" if target == companion else ""
                print(f"  {i+1}. {target.name}{self_tag}")
            target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
            target = targets[target_idx]
            
            # 清除负面状态
            target.is_frozen = False
            target.debuff_defense = 0
            print(f"  🔥 净化之焰 - 驱散了 {target.name} 的负面状态")
        else:
            print("  能量不足！")
            companion.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量")
    
    def use_dps_skill(self, companion, alive_enemies):
        """输出者技能"""
        print(f"\n{companion.name} 的技能:")
        print("  1. ⚔️ 断钢斩 (20能量) - 破甲一击")
        print("  2. 🔪 追命连斩 (30能量) - 连续攻击")
        print("  3. ⚡ 死线 (40能量) - 蓄力必杀")
        print()
        
        skill = input("选择技能 (1/2/3): ")
        
        print("\n选择目标：")
        for i, enemy in enumerate(alive_enemies):
            boss_tag = " 👑" if enemy.is_boss else ""
            print(f"  {i+1}. {enemy.name}{boss_tag} - HP: {enemy.hp}")
        target_idx = int(input(f"选择目标 (1-{len(alive_enemies)}): ")) - 1
        target = alive_enemies[target_idx]
        
        if skill == "1" and companion.use_skill(20):
            damage = int(companion.attack * 1.8)
            actual = target.take_damage(damage, companion.element)
            print(f"  ⚔️ 断钢斩 - 造成 {actual} 点伤害！")
        elif skill == "2" and companion.use_skill(30):
            for _ in range(3):
                damage = int(companion.attack * 0.7)
                target.take_damage(damage, companion.element)
            print(f"  🔪 追命连斩 - 三次连击！")
        elif skill == "3" and companion.use_skill(40):
            damage = int(companion.attack * 2.5)
            actual = target.take_damage(damage, companion.element)
            print(f"  ⚡ 死线 - 造成 {actual} 点巨额伤害！")
        else:
            print("  能量不足！")
            companion.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量")
    
    def use_defender_skill(self, companion, alive_enemies):
        """防御者技能"""
        print(f"\n{companion.name} 的技能:")
        print("  1. 🔥 于火中焚烧 (20能量) - 火焰攻击（无属性，无克制）")
        print("  2. ❄️ 霜骨壁垒 (30能量) - 全队共享护盾")
        print("  3. 🛡️ 终焉之茧 (35能量) - 终极防御（单体）")
        print()
        
        skill = input("选择技能 (1/2/3): ")
        
        if skill == "1" and companion.use_skill(20):
            print("\n选择目标：")
            for i, enemy in enumerate(alive_enemies):
                boss_tag = " 👑" if enemy.is_boss else ""
                print(f"  {i+1}. {enemy.name}{boss_tag}")
            target_idx = int(input(f"选择 (1-{len(alive_enemies)}): ")) - 1
            target = alive_enemies[target_idx]
            
            # 无属性攻击，不受克制影响
            damage = int(companion.attack * random.uniform(0.9, 1.1))
            actual = target.take_damage(damage)
            print(f"  🔥 于火中焚烧 - 造成 {actual} 点无属性伤害")
            
        elif skill == "2" and companion.use_skill(30):
            # 全队共享护盾
            all_targets = [companion, self.player] + [c for c in self.active_companions if c.alive and c != companion]
            for target in all_targets:
                target.shield += 15
            print(f"  ❄️ 霜骨壁垒 - 全队获得 15 点共享护盾！")
            
        elif skill == "3" and companion.use_skill(35):
            print("\n选择保护目标：")
            targets = [self.player] + [c for c in self.active_companions if c.alive and c != companion]
            for i, target in enumerate(targets):
                print(f"  {i+1}. {target.name}")
            target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
            target = targets[target_idx]
            
            target.shield += 40
            target.defense += 5
            print(f"  🛡️ 终焉之茧 - 为 {target.name} 添加 40 护盾并提升防御！")
        else:
            print("  能量不足！")
            companion.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量")
    
    def use_support_skill(self, companion, alive_enemies):
        """辅助者技能"""
        print(f"\n{companion.name} 的技能:")
        print("  1. 🔍 解析之眼 (25能量) - 标记一名敌人弱点")
        print("  2. 🧪 活性秘药 (30能量) - 强化一名队友")
        print("  3. ⚓ 重力锚定 (25能量) - 束缚一名敌人")
        print()
        
        skill = input("选择技能 (1/2/3): ")
        
        if skill == "1" and companion.use_skill(25):
            print("\n选择标记目标：")
            for i, enemy in enumerate(alive_enemies):
                boss_tag = " 👑" if enemy.is_boss else ""
                print(f"  {i+1}. {enemy.name}{boss_tag}")
            target_idx = int(input(f"选择 (1-{len(alive_enemies)}): ")) - 1
            target = alive_enemies[target_idx]
            
            target.weakness_mark = random.choice(["红", "黄", "蓝"])
            print(f"  🔍 解析之眼 - 标记了 {target.name} 的弱点（{target.weakness_mark}属性伤害+30%）！")
            
        elif skill == "2" and companion.use_skill(30):
            print("\n选择强化目标：")
            targets = [self.player] + [c for c in self.active_companions if c.alive and c != companion]
            for i, target in enumerate(targets):
                print(f"  {i+1}. {target.name}")
            target_idx = int(input(f"选择 (1-{len(targets)}): ")) - 1
            target = targets[target_idx]
            
            target.buff_attack += 8
            print(f"  🧪 活性秘药 - {target.name} 攻击力大幅提升！")
            
        elif skill == "3" and companion.use_skill(25):
            print("\n选择束缚目标：")
            for i, enemy in enumerate(alive_enemies):
                boss_tag = " 👑" if enemy.is_boss else ""
                print(f"  {i+1}. {enemy.name}{boss_tag}")
            target_idx = int(input(f"选择 (1-{len(alive_enemies)}): ")) - 1
            target = alive_enemies[target_idx]
            
            target.is_frozen = True
            print(f"  ⚓ 重力锚定 - {target.name} 下回合无法行动！")
        else:
            print("  能量不足！")
            companion.recover_energy(10)
            print(f"  ⚡ 普攻恢复 10 能量")
    
    def check_resurrection(self, healer):
        """检查并触发复活恩典（被动技能）"""
        if healer.name != "芙丽雅" or healer.resurrection_used:
            return
        
        # 检查是否有队友阵亡
        dead_targets = []
        if not self.player.alive:
            dead_targets.append(("玩家", self.player))
        for companion in self.active_companions:
            if not companion.alive and companion != healer:
                dead_targets.append((companion.name, companion))
        
        if dead_targets:
            # 复活第一个阵亡的队友
            name, target = dead_targets[0]
            target.hp = int(target.max_hp * 0.5)
            target.alive = True
            healer.resurrection_used = True
            print(f"\n  ✨ 被动触发：复活恩典！")
            print(f"  💚 芙丽雅将 {name} 从死亡边缘拉回！")
            print(f"  {name} 恢复了 50% HP")
            print()
    
    def companion_action(self, companion, alive_enemies):
        """伙伴行动"""
        if companion.role == "治疗":
            # 芙丽雅：治疗
            targets = [self.player] + [c for c in self.active_companions if c.alive and c != companion]
            wounded = [t for t in targets if t.hp < t.max_hp * 0.7]
            
            if wounded and companion.use_skill(20):
                target = min(wounded, key=lambda x: x.hp / x.max_hp)
                heal = int(companion.attack * 1.5)
                target.hp = min(target.max_hp, target.hp + heal)
                print(f"  💚 圣愈之光 (消耗20能量) - 为 {target.name} 恢复了 {heal} HP")
            elif alive_enemies:
                target = random.choice(alive_enemies)
                companion.attack_target(target, skill_name="感恩吧")
                companion.recover_energy(10)
                print(f"  ⚡ 普攻恢复 10 能量")
        
        elif companion.role == "输出":
            # 阿卡列：输出
            if alive_enemies:
                target = random.choice(alive_enemies)
                if companion.use_skill(25):
                    skill = random.choice(["断钢斩", "追命连斩"])
                    companion.attack_target(target, companion.element, skill)
                    print(f"  ⚡ 技能消耗 25 能量")
                else:
                    companion.attack_target(target, skill_name="流浪的剑士")
                    companion.recover_energy(10)
                    print(f"  ⚡ 普攻恢复 10 能量")
        
        elif companion.role == "防御":
            # 厄希斯：防御+攻击
            if random.random() > 0.5 and alive_enemies and companion.use_skill(20):
                target = random.choice(alive_enemies)
                companion.attack_target(target, "红", "于火中焚烧")
                print(f"  ⚡ 技能消耗 20 能量")
            else:
                # 给血量最低的队友加盾
                targets = [self.player] + [c for c in self.active_companions if c.alive and c != companion]
                wounded = min(targets, key=lambda x: x.hp / x.max_hp)
                wounded.shield += 15
                print(f"  🛡️ 霜骨壁垒 - 为 {wounded.name} 添加了护盾")
                companion.recover_energy(10)
                print(f"  ⚡ 普攻恢复 10 能量")
        
        elif companion.role == "辅助":
            # 莱因克雷德：辅助
            if alive_enemies and companion.use_skill(25):
                # 标记敌人弱点
                target = random.choice(alive_enemies)
                target.weakness_mark = random.choice(["红", "黄", "蓝"])
                print(f"  🔍 解析之眼 (消耗25能量) - 标记了 {target.name} 的弱点！")
                
                # 也给队友加buff
                targets = [self.player] + [c for c in self.active_companions if c.alive and c != companion]
                buff_target = random.choice(targets)
                buff_target.buff_attack += 3
                print(f"  📚 知识共鸣 - {buff_target.name} 攻击力提升！")
            else:
                companion.recover_energy(10)
                print(f"  ⚡ 普攻恢复 10 能量")
    
    def final_battle(self):
        """最终决战"""
        print()
        print("="*70)
        print("  👑 最终决战：黑白之主")
        print("="*70)
        print()
        
        story = [
            "黑白之主出现了！它是一个巨大的黑白漩涡，",
            "吞噬着世界上仅剩的色彩。",
            "",
            "「五彩的小虫子，你也想挑战我吗？」",
            "「那就让我把你变成永恒的黑白吧！」"
        ]
        
        story_print(story)
        print()
        input("按回车键开始最终决战...")
        print()
        
        # 三个阶段
        phases = [
            {"name": "第一阶段：黑白漩涡", "hp": 100, "attack": 20, "defense": 5, "element": "黄"},
            {"name": "第二阶段：黑白风暴", "hp": 120, "attack": 25, "defense": 8, "element": "红"},
            {"name": "第三阶段：黑白虚无", "hp": 150, "attack": 30, "defense": 10, "element": "蓝"}
        ]
        
        turn_count = 0
        
        for phase_data in phases:
            boss = Character(phase_data["name"], phase_data["hp"], 
                           phase_data["attack"], phase_data["defense"], 
                           phase_data["element"], "输出", is_boss=True)
            self.enemies = [boss]
            
            print(f"\n{'='*70}")
            print(f"  {phase_data['name']}")
            print(f"  HP: {boss.hp} | 元素: {boss.element}")
            print(f"{'='*70}")
            print()
            
            while boss.alive and self.player.alive:
                turn_count += 1
                self.turn = turn_count
                print(f"--- 回合 {turn_count} ---")
                
                self.battle_turn()
                
                if not self.player.alive and not any(c.alive for c in self.active_companions):
                    print("\n💀 你被打败了...")
                    return
            
            if boss.alive:
                print(f"\n{boss.name} 进入了下一阶段！")
            else:
                print(f"\n✅ {boss.name} 被击败了！")
        
        print("\n" + "="*70)
        print("  🎉 黑白之主被打败了！")
        print("="*70)
        print()
        
        story = [
            "色彩重新回到了源彩大陆！",
            "世界再次变得五彩缤纷，居民们欢呼雀跃。",
            "",
            "「谢谢你，五彩的救世主！」",
            "「你给了我们新的色彩，新的希望！」"
        ]
        
        story_print(story)
        print()
    
    def check_achievements(self):
        """检查成就"""
        print()
        print("="*70)
        print("  🏆 成就解锁")
        print("="*70)
        print()
        
        if self.player.alive:
            print("✅ 【天哪，是五彩缤纷的天降救世主😱】")
            print("   通关游戏，夺回三原色")
            print()
            self.achievements.append("天哪，是五彩缤纷的天降救世主😱")
        else:
            print("❌ 【殒落的五彩之星】")
            print("   未能通关")
            print()
            self.achievements.append("殒落的五彩之星")
        
        if len(self.all_companions) == 0:
            print("✅ 【我是一头绚烂的孤狼】")
            print("   没有招募任何伙伴通关")
            print()
            self.achievements.append("我是一头绚烂的孤狼")
        
        if len(self.all_companions) == 4:
            print("✅ 【叽里咕噜说什么呢，和我的羁绊说去吧】")
            print("   招募所有伙伴通关")
            print()
            self.achievements.append("叽里咕噜说什么呢，和我的羁绊说去吧")
        
        if self.turn <= 20 and self.player.alive:
            print("✅ 【我说艺术就是创造，你耳朵聋吗】")
            print("   最终决战在20回合内结束")
            print()
            self.achievements.append("我说艺术就是创造，你耳朵聋吗")
        
        print("="*70)
        print("  感谢游玩《天哪，是五彩缤纷的天降救世主😱》")
        print("="*70)


def get_element_multiplier(attacker, defender):
    """获取元素克制倍率"""
    if (attacker == "蓝" and defender == "红") or \
       (attacker == "红" and defender == "黄") or \
       (attacker == "黄" and defender == "蓝"):
        return 1.5
    elif (attacker == "红" and defender == "蓝") or \
         (attacker == "黄" and defender == "红") or \
         (attacker == "蓝" and defender == "黄"):
        return 0.7
    return 1.0


# 运行游戏
if __name__ == "__main__":
    game = Game()
    game.start()
