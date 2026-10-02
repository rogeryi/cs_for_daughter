import random


def roll_dice(sides=6, count=1):
    """
    投掷骰子

    参数：
        sides: 骰子面数（默认6面）
        count: 骰子数量（默认1个）

    返回：
        如果count=1，返回单个结果
        如果count>1，返回结果列表
    """
    if count == 1:
        return random.randint(1, sides)
    else:
        return [random.randint(1, sides) for _ in range(count)]


def roll_d6(count=1):
    """投掷6面骰子"""
    return roll_dice(6, count)


def roll_d20(count=1):
    """投掷20面骰子（常用于桌游）"""
    return roll_dice(20, count)


def calculate_total(results):
    """计算骰子结果总和"""
    if isinstance(results, list):
        return sum(results)
    return results


# 测试
print("=== 骰子模拟器 ===\n")

# 投掷1个6面骰子
result = roll_d6()
print(f"投掷1个D6：{result}")

# 投掷3个6面骰子
results = roll_d6(3)
print(f"投掷3个D6：{results}，总计：{calculate_total(results)}")

# 投掷1个20面骰子
result = roll_d20()
print(f"投掷1个D20：{result}")

# 自定义：投掷2个10面骰子
results = roll_dice(sides=10, count=2)
print(f"投掷2个D10：{results}，总计：{calculate_total(results)}")
