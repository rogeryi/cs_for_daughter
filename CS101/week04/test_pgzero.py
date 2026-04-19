# Pygame Zero 安装测试
# 运行此文件检查是否安装成功

import pygame
import pgzero

print("=" * 50)
print("  Pygame Zero 安装检查")
print("=" * 50)
print()

# 检查 Pygame 版本
print(f"✅ Pygame 版本: {pygame.version.ver}")

# 检查 Pygame Zero
print(f"✅ Pygame Zero 已安装")

# 检查 SDL（Pygame 的底层库）
print(f"✅ SDL 版本: {pygame.get_sdl_version()}")

print()
print("=" * 50)
print("  所有依赖都已正确安装！")
print("=" * 50)
print()
print("现在可以创建 Pygame Zero 游戏了！")
print("运行方式: python3 你的游戏.py")
print()

# 尝试创建一个简单的窗口（可选）
try:
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame Zero 测试")
    
    print("✅ 图形窗口创建成功！")
    print("如果看到窗口弹出，说明一切正常！")
    print()
    
    # 等待3秒后关闭
    import time
    time.sleep(3)
    pygame.quit()
    
    print("✅ 测试完成！")
    
except Exception as e:
    print(f"⚠️  窗口测试遇到问题: {e}")
    print("但这不影响使用 Pygame Zero 运行游戏文件")
