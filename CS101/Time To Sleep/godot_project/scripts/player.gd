extends CharacterBody2D

# 移动参数
@export var speed: int = 200
@export var jump_force: int = -400
@export var gravity: int = 800

# 动画状态
var current_animation = "idle"
var facing_right = true

@onready var animated_sprite = $AnimatedSprite2D

func _ready():
	# 初始化
	print("Player initialized!")
	print("Controls: A/D or ←/→ to move, Space to jump")

func _physics_process(delta):
	# 应用重力
	if not is_on_floor():
		velocity.y += gravity * delta
	
	# 跳跃
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = jump_force
		play_animation("jump")
	
	# 水平移动
	var direction = Input.get_axis("move_left", "move_right")
	
	if direction != 0:
		velocity.x = direction * speed
		
		# 更新朝向
		if direction > 0 and not facing_right:
			facing_right = true
			animated_sprite.flip_h = false
		elif direction < 0 and facing_right:
			facing_right = false
			animated_sprite.flip_h = true
		
		# 播放移动动画（如果在空中则不播放）
		if is_on_floor():
			play_animation("run")
	else:
		velocity.x = 0
		# 在地面上时播放待机动画
		if is_on_floor():
			play_animation("idle")
	
	# 移动并处理碰撞
	move_and_slide()

func play_animation(anim_name: String):
	"""播放动画，避免重复播放相同动画"""
	if current_animation != anim_name:
		current_animation = anim_name
		animated_sprite.play(anim_name)
