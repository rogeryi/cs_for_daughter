"""
裁剪所有四边透明边框
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载原始精灵图
original_path = "/Users/roger/cs/CS101/week06/精灵图测试2/images/demo移动1.png"
original_image = pygame.image.load(original_path).convert_alpha()
print(f"原始尺寸: {original_image.get_size()}")

# 裁剪所有透明边框
def crop_all_borders(surface):
    """裁剪所有四边透明边框"""
    width, height = surface.get_size()
    
    # 从左扫描，找到第一个非透明列
    left = 0
    for x in range(width):
        for y in range(height):
            pixel = surface.get_at((x, y))
            if pixel[3] > 0:
                left = x
                break
        else:
            continue
        break
    
    # 从右扫描
    right = width - 1
    for x in range(width - 1, -1, -1):
        for y in range(height):
            pixel = surface.get_at((x, y))
            if pixel[3] > 0:
                right = x
                break
        else:
            continue
        break
    
    # 从上扫描
    top = 0
    for y in range(height):
        for x in range(width):
            pixel = surface.get_at((x, y))
            if pixel[3] > 0:
                top = y
                break
        else:
            continue
        break
    
    # 从下扫描
    bottom = height - 1
    for y in range(height - 1, -1, -1):
        for x in range(width):
            pixel = surface.get_at((x, y))
            if pixel[3] > 0:
                bottom = y
                break
        else:
            continue
        break
    
    # 裁剪
    cropped_width = right - left + 1
    cropped_height = bottom - top + 1
    cropped = surface.subsurface((left, top, cropped_width, cropped_height))
    
    print(f"裁剪后尺寸: {cropped.get_size()}")
    print(f"  裁剪掉: 左={left}, 右={width-right-1}, 上={top}, 下={height-bottom-1}")
    
    return cropped

# 裁剪
cropped_image = crop_all_borders(original_image)

# 缩放到目标大小（宽度60，高度按比例）
target_width = 60
scale_factor = target_width / cropped_image.get_width()
new_height = int(cropped_image.get_height() * scale_factor)

scaled_image = pygame.transform.scale(cropped_image, (target_width, new_height))
print(f"缩放后尺寸: {scaled_image.get_size()}")

# 创建一个画布，高度保持缩放后的大小
final_image = pygame.Surface((target_width, new_height), pygame.SRCALPHA)
final_image.blit(scaled_image, (0, 0))

print(f"最终画布: {final_image.get_size()}")

# 保存
output_path = "/Users/roger/cs/CS101/week06/精灵图测试2/images/player.png"
pygame.image.save(final_image, output_path)
print(f"✓ 已保存: {output_path}")

pygame.quit()
