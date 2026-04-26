# Godot 精灵表自动导入配置
# 将此文件放在 Godot 项目根目录，然后在编辑器中运行

extends EditorScript

func _run():
	print("🎨 开始自动导入精灵表...")
	
	# 精灵表配置
	var sprite_configs = [
		{
			"path": "res://assets/sprites/demo待机.png",
			"anim_name": "idle",
			"frame_size": Vector2i(56, 56),  # 假设 2x2 网格
			"fps": 8.0,
			"loop": true
		},
		{
			"path": "res://assets/sprites/demo移动.png",
			"anim_name": "run",
			"frame_size": Vector2i(56, 56),  # 假设 2x2 网格
			"fps": 10.0,
			"loop": true
		},
		{
			"path": "res://assets/sprites/demo跳跃.png",
			"anim_name": "jump",
			"frame_size": Vector2i(56, 56),  # 假设 3x3 网格
			"fps": 15.0,
			"loop": false
		}
	]
	
	print("✅ 精灵表导入配置完成！")
	print("请在 Godot 编辑器中手动切割精灵表（见 Pixel_Studio_导入步骤.md）")
