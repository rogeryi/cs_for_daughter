"""
替换jump2和jump3的素材
jump2 ← demo跳跃10
jump3 ← demo跳跃9
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def process_jump_frame(source_file, output_file, target_height=72):
    """处理跳跃帧，保留特效，统一高度"""
    original = pygame.image.load(source_file).convert_alpha()
    w, h = original.get_size()
    
    print(f"\n处理: {source_file} → {output_file}")
    print(f"  原始: {w}x{h}")
    
    # 只裁剪上下透明边框，保留左右特效
    top = 0
    bottom = h - 1
    
    # 找上边界
    for y in range(h):
        for x in range(w):
            if original.get_at((x, y))[3] > 0:
                top = y
                break
        else:
            continue
        break
    
    # 找下边界
    for y in range(h-1, -1, -1):
        for x in range(w):
            if original.get_at((x, y))[3] > 0:
                bottom = y
                break
        else:
            continue
        break
    
    # 裁剪上下
    cropped_h = bottom - top + 1
    cropped = original.subsurface((0, top, w, cropped_h))
    print(f"  裁剪上下后: {cropped.get_size()}")
    
    # 缩放到目标高度，宽度按比例
    scale = target_height / cropped_h
    new_w = int(w * scale)
    scaled = pygame.transform.scale(cropped, (new_w, target_height))
    print(f"  缩放后: {scaled.get_size()}")
    
    # 保存
    pygame.image.save(scaled, output_file)
    print(f"  ✓ 已保存")
    
    return scaled.get_size()

# 替换jump2和jump3
print("="*60)
print("替换跳跃帧素材")
print("="*60)

# jump2 ← demo跳跃10
size2 = process_jump_frame(
    "demo跳跃10.png",
    "images/jump2.png",
    target_height=72
)

# jump3 ← demo跳跃9
size3 = process_jump_frame(
    "demo跳跃9.png",
    "images/jump3.png",
    target_height=72
)

print("\n" + "="*60)
print("✓ 替换完成！")
print(f"  jump2 (原demo跳跃10): {size2}")
print(f"  jump3 (原demo跳跃9): {size3}")
print("="*60)

pygame.quit()
