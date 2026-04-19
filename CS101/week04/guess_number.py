# 猜数字游戏 v2 - 进阶版
# Guess the Number Game - Advanced Version
# 包含难度选择和次数限制

import random

def guess_number_game():
    """猜数字游戏主函数"""
    print("=" * 50)
    print("          🎮 猜数字游戏 🎮")
    print("=" * 50)
    print()
    
    # 难度选择
    print("请选择难度：")
    print("1. 简单 (1-50, 最多10次)")
    print("2. 中等 (1-100, 最多7次)")
    print("3. 困难 (1-200, 最多10次)")
    print()
    
    difficulty = input("请输入选项 (1/2/3) [默认2]: ").strip()
    
    # 根据难度设置参数
    if difficulty == "1":
        max_num = 50
        max_attempts = 10
        difficulty_name = "简单"
    elif difficulty == "3":
        max_num = 200
        max_attempts = 10
        difficulty_name = "困难"
    else:
        max_num = 100
        max_attempts = 7
        difficulty_name = "中等"
    
    print(f"\n你选择了 {difficulty_name} 难度")
    print(f"我想了一个 1-{max_num} 之间的数字")
    print(f"你有 {max_attempts} 次机会")
    print()
    
    # 生成随机数
    secret = random.randint(1, max_num)
    guess_count = 0
    
    # 游戏循环
    while guess_count < max_attempts:
        # 显示剩余次数
        remaining = max_attempts - guess_count
        print(f"剩余机会: {remaining} 次")
        
        # 获取用户输入
        try:
            guess = int(input("请输入你的猜测: "))
        except ValueError:
            print("⚠️  请输入有效的数字！\n")
            continue
        
        # 检查输入范围
        if guess < 1 or guess > max_num:
            print(f"⚠️  请输入 1-{max_num} 之间的数字！\n")
            continue
        
        guess_count += 1
        
        # 判断猜测结果
        if guess == secret:
            print(f"\n{'=' * 50}")
            print(f"🎉 恭喜你猜对了！")
            print(f"{'=' * 50}")
            print(f"答案就是: {secret}")
            print(f"你总共猜了 {guess_count} 次")
            
            # 根据猜测次数给予评价
            if guess_count <= 3:
                print("🌟 太厉害了！你是猜数字大师！")
            elif guess_count <= 5:
                print("👏 非常棒！你的直觉很准！")
            elif guess_count <= max_attempts // 2:
                print("👍 不错！继续加油！")
            else:
                print("😊 终于猜对了！下次会更好！")
            
            print()
            break
        elif guess < secret:
            print("📈 太小了，再大一点！")
            # 给出更详细的提示
            if secret - guess <= 5:
                print("💡 提示：非常接近了！")
            print()
        else:
            print("📉 太大了，再小一点！")
            # 给出更详细的提示
            if guess - secret <= 5:
                print("💡 提示：非常接近了！")
            print()
    else:
        # 循环正常结束（没有 break），说明次数用完了
        print(f"\n{'=' * 50}")
        print(f"😢 很遗憾，机会用完了！")
        print(f"{'=' * 50}")
        print(f"答案是: {secret}")
        print(f"你猜了 {guess_count} 次")
        print()
    
    # 询问是否再玩一次
    print("=" * 50)
    play_again = input("想再玩一次吗？(yes/no): ").strip().lower()
    
    if play_again == 'yes' or play_again == 'y':
        print("\n" + "=" * 50)
        print("开始新游戏！")
        print("=" * 50 + "\n")
        guess_number_game()  # 递归调用，重新开始
    else:
        print("\n感谢游玩！再见！👋")
        print("=" * 50)


# 游戏入口
if __name__ == "__main__":
    guess_number_game()
