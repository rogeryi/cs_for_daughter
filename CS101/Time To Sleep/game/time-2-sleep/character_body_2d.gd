# 右键场景树 -> Add Child Node
# 选择 CharacterBody2D
# 添加以下脚本：

extends CharacterBody2D

@export var speed: int = 200
@export var jump_force: int = 400
const GRAVITY = 800

func _physics_process(delta):
	# 重力
	velocity.y += GRAVITY * delta
	
	# 跳跃
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = -jump_force
	
	# 移动
	var direction = Input.get_axis("ui_left", "ui_right")
	velocity.x = direction * speed
	
	# 移动
	move_and_slide()
