"""
统一所有跳跃帧大小为60x72
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

target_width = 60
target_height = 72

# 需要统一的跳跃帧
jump_frames = [1, 2, 3, 4, 5, 7, 8, 9, 10]

print("="*60)
print("统一跳跃帧大小为 60x72")
print("="*60)

for i in jump_frames:
    input_path = f"images/jump{i}.png"
    output_path = f"images/jump{i}.png"
    
    try:
        original = pygame.image.load(input_path).convert_alpha()
        w, h = original.get_size()
        
        if w == target_width and h == target_height:
            print(f"  jump{i}: 已经是 {w}x{h}，跳过")
            continue
        
        # 缩放到统一尺寸
        scaled = pygame.transform.scale(original, (target_width, target_height))
        pygame.image.save(scaled, output_path)
        print(f"  jump{i}: {w}x{h} → {scaled.get_size()} ✓")
    except Exception as e:
        print(f"  jump{i}: 错误 - {e}")

print("\n" + "="*60)
print("✓ 所有跳跃帧统一完成！")
print("="*60)
pygame.quit()
