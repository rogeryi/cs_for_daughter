"""
重新处理待机帧，统一高度为72
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

target_width = 60
target_height = 72  # 统一高度

for i in range(1, 5):
    path = f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png"
    original = pygame.image.load(path).convert_alpha()
    print(f"\n处理 idle{i}.png")
    print(f"  原始尺寸: {original.get_size()}")
    
    # 缩放到统一尺寸
    scaled = pygame.transform.scale(original, (target_width, target_height))
    print(f"  统一尺寸: {scaled.get_size()}")
    
    # 保存
    output = f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png"
    pygame.image.save(scaled, output)
    print(f"  ✓ 已保存")

print("\n✓ 所有待机帧统一完成！")
pygame.quit()
