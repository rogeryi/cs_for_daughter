"""
裁剪透明边框并缩放精灵图
"""
import pygame

pygame.init()

# 设置一个隐藏的显示表面
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载原始精灵图
original_path = "/Users/roger/cs/CS101/week06/精灵图测试2/images/demo移动1.png"
original_image = pygame.image.load(original_path).convert_alpha()
print(f"原始尺寸: {original_image.get_size()}")

# 裁剪透明边框
def crop_transparent_borders(surface):
    """裁剪完全透明的边框"""
    # 获取非透明区域的边界
    mask = pygame.mask.from_surface(surface)
    bbox = mask.get_bounding_rects()
    
    if not bbox:
        return surface
    
    # 找到包含所有非透明像素的最小矩形
    min_x = min(r.x for r in bbox)
    min_y = min(r.y for r in bbox)
    max_x = max(r.x + r.width for r in bbox)
    max_y = max(r.y + r.height for r in bbox)
    
    # 裁剪
    cropped = surface.subsurface((min_x, min_y, max_x - min_x, max_y - min_y))
    print(f"裁剪后尺寸: {cropped.get_size()}")
    print(f"  裁剪掉: 左={min_x}, 上={min_y}, 右={original_image.get_width()-max_x}, 下={original_image.get_height()-max_y}")
    
    return cropped

# 裁剪
cropped_image = crop_transparent_borders(original_image)

# 缩放到目标大小（宽度为平台的一半 = 60）
target_size = 60
max_dim = max(cropped_image.get_width(), cropped_image.get_height())
scale_factor = target_size / max_dim

new_width = int(cropped_image.get_width() * scale_factor)
new_height = int(cropped_image.get_height() * scale_factor)

scaled_image = pygame.transform.scale(cropped_image, (new_width, new_height))
print(f"缩放后尺寸: {scaled_image.get_size()}")

# 创建一个正方形画布，居中放置精灵图
final_image = pygame.Surface((target_size, target_size), pygame.SRCALPHA)
offset_x = (target_size - new_width) // 2
offset_y = (target_size - new_height) // 2
final_image.blit(scaled_image, (offset_x, offset_y))

print(f"最终画布: {final_image.get_size()}")
print(f"  精灵图偏移: ({offset_x}, {offset_y})")

# 保存
output_path = "/Users/roger/cs/CS101/week06/精灵图测试2/images/player.png"
pygame.image.save(final_image, output_path)
print(f"✓ 已保存: {output_path}")

pygame.quit()
