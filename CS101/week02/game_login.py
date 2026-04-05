# 游戏初始登录界面
# Game Login System - 创建角色

print("========================================")
print("       欢迎来到 勇者传说 Online")
print("========================================")
print()

# ===== 输入玩家信息 =====

# 输入名字
name = input("请输入你的名字: ")

# 输入性别
gender = input("请选择性别 (男/女): ")

# 输入出生日期
birth_month = int(input("请输入出生月份: "))
birth_day = int(input("请输入出生日期: "))

# 输入游戏中的身份
print("\n请选择你的游戏身份:")
print("1. 战士 - 拥有强大的生命值和近战攻击力，是团队的前排守护者")
print("2. 法师 - 掌握强大的魔法力量，能造成范围伤害，但生命脆弱")
print("3. 刺客 - 擅长潜行和暗杀，暴击率高，行动敏捷")
print()
identity_choice = input("请输入选项编号 (1/2/3): ")

# 根据选择确定身份
if identity_choice == "1":
    identity = "战士"
elif identity_choice == "2":
    identity = "法师"
elif identity_choice == "3":
    identity = "刺客"
else:
    print("\n⚠️  无效选择，默认选择战士")
    identity = "战士"

# 定义不同身份的基本数值（每类不低于2点，总计不超过40点）
character_stats = {
    "战士": {"生命": 6, "攻击": 6, "防御": 6, "智力": 2, "魅力": 3, "灵巧": 2, "速度": 3},  # 总计28
    "法师": {"生命": 3, "攻击": 2, "防御": 2, "智力": 7, "魅力": 4, "灵巧": 3, "速度": 2},  # 总计23
    "刺客": {"生命": 4, "攻击": 4, "防御": 2, "智力": 3, "魅力": 3, "灵巧": 7, "速度": 6}   # 总计29
}

# 显示角色卡片
print()
print("========================================")
print("         ✨ 角色创建成功! ✨")
print("========================================")
print(f"名字: {name}")
print(f"性别: {gender}")
print(f"出生日期: {birth_month}月{birth_day}日")
print(f"游戏身份: {identity}")
print("========================================")

# 定义属性名称列表（在使用前定义）
stat_names = ["生命", "攻击", "防御", "智力", "魅力", "灵巧", "速度"]

# 获取对应身份的属性
stats = character_stats[identity]

# 计算职业基础点数总和
base_total = sum(stats.values())

# 固定可支配点数
available_points = 15

# 显示基本数值
print("\n【基本数值】")
print(f"  ❤️ 生命: {stats['生命']}")
print(f"  ⚔️ 攻击: {stats['攻击']}")
print(f"  🛡️ 防御: {stats['防御']}")
print(f"  📖 智力: {stats['智力']}")
print(f"  ✨ 魅力: {stats['魅力']}")
print(f"  🎯 灵巧: {stats['灵巧']}")
print(f"  💨 速度: {stats['速度']}")
print(f"\n  可支配点数: {available_points} (固定)")

# ===== 分配属性点 =====
print("\n" + "="*40)
print("       📊 属性点分配")
print("="*40)
print(f"你有 {available_points} 点可支配属性点")
print("每类属性满点为 10 点")
print("提示: 分配完成后可以重新调整")
print()

# 复制当前属性作为最终属性
final_stats = stats.copy()

while True:  # 允许多次调整
    remaining_points = available_points
    
    # 重置为职业基础属性
    for stat in stat_names:
        final_stats[stat] = stats[stat]
    
    # 让玩家分配每个属性
    for stat in stat_names:
        current = final_stats[stat]
        max_can_add = 10 - current  # 最多能加多少
        
        print(f"\n当前 {stat}: {current}/10")
        print(f"可分配: 0-{max_can_add} (剩余点数: {remaining_points})")
        
        if remaining_points > 0 and max_can_add > 0:
            add = int(input(f"要为 {stat} 分配几点? "))
            # 检查输入是否合法
            if add < 0:
                add = 0
            elif add > max_can_add:
                add = max_can_add
            elif add > remaining_points:
                add = remaining_points
            
            final_stats[stat] += add
            remaining_points -= add
        else:
            print("  无法分配")
    
    # 显示当前分配结果
    print("\n" + "="*40)
    print("       当前属性分配")
    print("="*40)
    for stat in stat_names:
        bar = "█" * final_stats[stat] + "░" * (10 - final_stats[stat])
        print(f"  {stat}: [{bar}] {final_stats[stat]}/10")
    
    print(f"\n  剩余点数: {remaining_points}")
    
    # 询问是否重新分配
    print()
    redo = input("是否重新分配属性? (yes/no): ")
    if redo.lower() != 'yes':
        break
    
    print("\n" + "="*40)
    print("  重新开始分配...")
    print("="*40)

# 欢迎来到游戏世界
print(f"\n欢迎来到游戏世界, {name}!")
print("冒险即将开始...")
