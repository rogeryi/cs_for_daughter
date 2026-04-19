# 文字显示测试
import pgzrun
import pygame

pygame.font.init()

WIDTH = 800
HEIGHT = 400
TITLE = "文字测试"

def draw():
    screen.fill((50, 50, 50))
    
    # 测试不同的文字绘制方法
    screen.draw.text("测试1: 你好世界!", (50, 50), fontsize=30, color=(255, 255, 255))
    screen.draw.text("Test 2: Hello World!", (50, 100), fontsize=30, color=(255, 255, 0))
    screen.draw.text("测试3: 分数: 100", (50, 150), fontsize=24, color=(0, 255, 0))
    
    # 带描边的文字（使用阴影效果）
    screen.draw.text("带阴影", center=(400, 250), fontsize=40, 
                    color=(255, 255, 255))
    
    # 大标题
    screen.draw.text("文字显示测试", center=(400, 80), 
                    fontsize=50, color=(255, 215, 0))
    
    screen.draw.text("如果能看到这些文字，说明字体正常", center=(400, 350), 
                    fontsize=20, color=(200, 200, 200))

pgzrun.go()
