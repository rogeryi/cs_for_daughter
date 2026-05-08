"""
裁剪并缩放所有4个待机精灵图
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def process_sprite(source_file, idle_num, target_width=60):
    """从原始文件裁剪并缩放"""
    path = f"/Users/roger/cs/CS101/week06/精灵图测试2/{source_file}"
    original = pygame.image.load(path).convert_alpha()
    print(f"\n处理 {source_file} -> idle{idle_num}.png")
    print(f"  原始尺寸: {original.get_size()}")
    
    width, height = original.get_size()
    
    # 找左边界
    left = 0
    for x in range(width):
        for y in range(height):
            if original.get_at((x, y))[3] > 0:
                left = x
                break
        else:
            continue
        break
    
    # 找右边界
    right = width - 1
    for x in range(width - 1, -1, -1):
        for y in range(height):
            if original.get_at((x, y))[3] > 0:
                right = x
                break
        else:
            continue
        break
    
    # 找上边界
    top = 0
    for y in range(height):
        for x in range(width):
            if original.get_at((x, y))[3] > 0:
                top = y
                break
        else:
            continue
        break
    
    # 找下边界（精确到像素）
    bottom = height - 1
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if original.get_at((x, y))[3] > 0:
                bottom = y
                break
        else:
            continue
        break
    
    # 裁剪
    cropped_width = right - left + 1
    cropped_height = bottom - top + 1
    cropped = original.subsurface((left, top, cropped_width, cropped_height))
    print(f"  裁剪后: {cropped.get_size()}")
    print(f"  裁剪: 左={left}, 右={width-right-1}, 上={top}, 下={height-bottom-1}")
    
    # 缩放
    scale = target_width / cropped.get_width()
    new_height = int(cropped.get_height() * scale)
    scaled = pygame.transform.scale(cropped, (target_width, new_height))
    print(f"  缩放后: {scaled.get_size()}")
    
    # 保存
    output = f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{idle_num}.png"
    pygame.image.save(scaled, output)
    print(f"  ✓ 已保存")

# 处理所有4个待机帧
for i in range(1, 5):
    process_sprite(f"demo待机{i}.png", i)

print("\n✓ 所有待机帧处理完成！")
pygame.quit()
