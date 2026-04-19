# 创建简单的游戏图片
import pygame
import os

# 初始化 pygame
pygame.init()

# 创建 images 目录
images_dir = "/Users/roger/cs/CS101/week04/images"
os.makedirs(images_dir, exist_ok=True)

# 创建篮子图片（棕色矩形）
basket_surface = pygame.Surface((80, 40))
basket_surface.fill((139, 69, 19))  # 棕色
pygame.draw.rect(basket_surface, (160, 82, 45), (5, 5, 70, 30), 3)
pygame.image.save(basket_surface, os.path.join(images_dir, "basket.png"))
print("✅ 创建 basket.png")

# 创建苹果图片（红色圆形）
apple_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.circle(apple_surface, (255, 0, 0), (20, 20), 18)
pygame.draw.circle(apple_surface, (0, 128, 0), (20, 5), 5)  # 叶子
pygame.image.save(apple_surface, os.path.join(images_dir, "apple.png"))
print("✅ 创建 apple.png")

pygame.quit()
print("\n✅ 所有图片创建完成！")
