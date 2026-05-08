"""
重新处理所有精灵图，精确裁剪透明边框
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

def precise_crop(sprite_path, target_width=60):
    """精确裁剪透明边框并缩放"""
    original = pygame.image.load(sprite_path).convert_alpha()
    w, h = original.get_size()
    
    # 精确找到非透明像素的边界
    left, right, top, bottom = w, 0, h, 0
    has_pixel = False
    
    for y in range(h):
        for x in range(w):
            if original.get_at((x, y))[3] > 0:  # 透明度>0
                left = min(left, x)
                right = max(right, x)
                top = min(top, y)
                bottom = max(bottom, y)
                has_pixel = True
    
    if not has_pixel:
        print(f"  警告: {sprite_path} 完全是透明的!")
        return original
    
    # 裁剪
    cropped_w = right - left + 1
    cropped_h = bottom - top + 1
    cropped = original.subsurface((left, top, cropped_w, cropped_h))
    
    # 缩放
    scale = target_width / cropped_w
    new_h = int(cropped_h * scale)
    scaled = pygame.transform.scale(cropped, (target_width, new_h))
    
    return scaled

# 处理所有文件
files = {
    'images/move1.png': 'demo移动1.png',
    'images/move2.png': 'demo移动2.png',
    'images/move3.png': 'demo移动3.png',
    'images/move4.png': 'demo移动4.png',
    'images/idle1.png': 'demo待机1.png',
    'images/idle2.png': 'demo待机2.png',
    'images/idle3.png': 'demo待机3.png',
    'images/idle4.png': 'demo待机4.png',
    'images/jump1.png': 'demo跳跃1.png',
    'images/jump2.png': 'demo跳跃2.png',
    'images/jump3.png': 'demo跳跃3.png',
    'images/jump4.png': 'demo跳跃4.png',
    'images/jump5.png': 'demo跳跃5.png',
    'images/jump7.png': 'demo跳跃7.png',
    'images/jump8.png': 'demo跳跃8.png',
    'images/jump9.png': 'demo跳跃9.png',
    'images/jump10.png': 'demo跳跃10.png',
}

for output, input_file in files.items():
    print(f"处理: {input_file}")
    try:
        scaled = precise_crop(input_file)
        pygame.image.save(scaled, output)
        print(f"  ✓ 已保存 {output}: {scaled.get_size()}")
    except Exception as e:
        print(f"  ✗ 错误: {e}")

print("\n✓ 所有精灵图处理完成!")
pygame.quit()
