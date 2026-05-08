"""
裁剪并替换 move4.png 为新的 demo移动6.png
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 加载新图片
path = "/Users/roger/cs/CS101/week06/精灵图测试2/demo移动6.png"
original = pygame.image.load(path).convert_alpha()
print(f"原始尺寸: {original.get_size()}")

# 裁剪所有透明边框
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

# 找下边界
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
print(f"裁剪后: {cropped.get_size()}")
print(f"  裁剪掉: 左={left}, 右={width-right-1}, 上={top}, 下={height-bottom-1}")

# 缩放（宽度60，高度按比例）
target_width = 60
scale = target_width / cropped.get_width()
new_height = int(cropped.get_height() * scale)
scaled = pygame.transform.scale(cropped, (target_width, new_height))
print(f"缩放后: {scaled.get_size()}")

# 保存（覆盖原有的 move4.png）
output = "/Users/roger/cs/CS101/week06/精灵图测试2/images/move4.png"
pygame.image.save(scaled, output)
print(f"✓ 已保存: {output}")

pygame.quit()
