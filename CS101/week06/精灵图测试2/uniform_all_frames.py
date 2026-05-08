"""
统一所有移动和待机帧的高度
"""
import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

# 目标尺寸
target_width = 60
target_height = 72  # 统一高度

def uniform_height(file_path, output_path):
    """统一高度到72像素"""
    original = pygame.image.load(file_path).convert_alpha()
    w, h = original.get_size()
    
    if h == target_height:
        print(f"  {file_path} 已经是 {w}x{h}，跳过")
        return
    
    # 缩放到统一尺寸
    scaled = pygame.transform.scale(original, (target_width, target_height))
    pygame.image.save(scaled, output_path)
    print(f"  {file_path} {w}x{h} → {scaled.get_size()}")

# 统一移动帧
print("="*60)
print("统一移动帧高度")
print("="*60)
for i in range(1, 5):
    uniform_height(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/move{i}.png"
    )

# 统一待机帧
print("\n" + "="*60)
print("统一待机帧高度")
print("="*60)
for i in range(1, 5):
    uniform_height(
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png",
        f"/Users/roger/cs/CS101/week06/精灵图测试2/images/idle{i}.png"
    )

print("\n" + "="*60)
print("✓ 所有帧统一完成！")
print("="*60)
pygame.quit()
