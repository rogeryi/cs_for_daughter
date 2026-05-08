"""
重新裁剪待机和移动帧的底部透明边框
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def crop_bottom_precisely(file_path, output_path):
    """精确裁剪底部透明边框"""
    original = pygame.image.load(file_path).convert_alpha()
    print(f"\n处理: {file_path}")
    print(f"  原始尺寸: {original.get_size()}")
    
    width, height = original.get_size()
    
    # 从下往上扫描，找到第一个非透明行
    bottom = height - 1
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if original.get_at((x, y))[3] > 0:
                bottom = y
                break
        else:
            continue
        break
    
    # 裁剪底部
    new_height = bottom + 1
    cropped = original.subsurface((0, 0, width, new_height))
    print(f"  裁剪后: {cropped.get_size()}")
    print(f"  裁剪掉底部: {height - new_height} 像素")
    
    # 保存
    pygame.image.save(cropped, output_path)
    print(f"  ✓ 已保存")
    
    return cropped.get_size()

# 裁剪移动帧
print("="*60)
print("裁剪移动帧")
print("="*60)
for i in range(1, 5):
    crop_bottom_precisely(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{i}.png"
    )

# 裁剪待机帧
print("\n" + "="*60)
print("裁剪待机帧")
print("="*60)
for i in range(1, 5):
    crop_bottom_precisely(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png"
    )

print("\n" + "="*60)
print("✓ 所有帧裁剪完成！")
print("="*60)
pygame.quit()
