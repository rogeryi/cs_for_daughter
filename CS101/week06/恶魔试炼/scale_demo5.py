"""
缩放 demo移动5 到合适大小
"""
import pygame

pygame.init()

# 加载原始精灵图
original_path = "/Users/roger/cs/CS101/week06/恶魔试炼/demo移动5.png"
original_image = pygame.image.load(original_path)
print(f"原始尺寸: {original_image.get_size()}")

# 缩放到 40x40 (平台宽度120的1/3)
target_size = 40
scaled_image = pygame.transform.scale(original_image, (target_size, target_size))
print(f"缩放后尺寸: {scaled_image.get_size()}")

# 保存为 player.png
output_path = "/Users/roger/cs/CS101/week06/恶魔试炼/images/player.png"
pygame.image.save(scaled_image, output_path)
print(f"✓ 已保存: {output_path}")

pygame.quit()
