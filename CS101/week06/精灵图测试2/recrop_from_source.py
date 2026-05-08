"""
从原始demo文件重新裁剪移动和待机帧，确保底部无透明边框
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def crop_and_scale(source_file, output_file, target_width=60):
    """裁剪所有透明边框并缩放"""
    original = pygame.image.load(source_file).convert_alpha()
    print(f"\n处理: {source_file}")
    print(f"  原始: {original.get_size()}")
    
    w, h = original.get_size()
    
    # 找四个边界
    left, right, top, bottom = 0, w-1, 0, h-1
    
    # 左
    for x in range(w):
        for y in range(h):
            if original.get_at((x, y))[3] > 0:
                left = x
                break
        else:
            continue
        break
    
    # 右
    for x in range(w-1, -1, -1):
        for y in range(h):
            if original.get_at((x, y))[3] > 0:
                right = x
                break
        else:
            continue
        break
    
    # 上
    for y in range(h):
        for x in range(w):
            if original.get_at((x, y))[3] > 0:
                top = y
                break
        else:
            continue
        break
    
    # 下
    for y in range(h-1, -1, -1):
        for x in range(w):
            if original.get_at((x, y))[3] > 0:
                bottom = y
                break
        else:
            continue
        break
    
    # 裁剪
    cropped_w = right - left + 1
    cropped_h = bottom - top + 1
    cropped = original.subsurface((left, top, cropped_w, cropped_h))
    print(f"  裁剪: {cropped.get_size()} (左={left}, 右={w-1-right}, 上={top}, 下={h-1-bottom})")
    
    # 缩放
    scale = target_width / cropped_w
    new_h = int(cropped_h * scale)
    scaled = pygame.transform.scale(cropped, (target_width, new_h))
    print(f"  缩放: {scaled.get_size()}")
    
    # 保存
    pygame.image.save(scaled, output_file)
    print(f"  ✓ 已保存")

# 处理移动帧
print("="*60)
print("处理移动帧")
print("="*60)
for i in range(1, 5):
    crop_and_scale(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/demo移动{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{i}.png"
    )

# 处理待机帧
print("\n" + "="*60)
print("处理待机帧")
print("="*60)
for i in range(1, 5):
    crop_and_scale(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/demo待机{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png"
    )

print("\n" + "="*60)
print("✓ 全部完成！")
print("="*60)
pygame.quit()
