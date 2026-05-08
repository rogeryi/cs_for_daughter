"""
替换 move1 为 demo移动5，move2 为 demo移动6
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def process_sprite(source_file, move_num, target_width=60):
    """从原始文件裁剪并缩放"""
    path = f"/Users/roger/cs/CS101/week06/精灵图测试2/{source_file}"
    original = pygame.image.load(path).convert_alpha()
    print(f"\n处理 {source_file} -> move{move_num}.png")
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
    output = f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{move_num}.png"
    pygame.image.save(scaled, output)
    print(f"  ✓ 已保存")

# 只替换 move1 和 move2
process_sprite("demo移动5.png", 1)
process_sprite("demo移动6.png", 2)

print("\n✓ 替换完成！")
print("注意：move1 和 move3 需要在代码中向下偏移1像素")
pygame.quit()
