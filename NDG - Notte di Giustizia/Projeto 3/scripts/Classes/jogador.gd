extends CharacterBody2D

class_name Jogador
#velocidade do player
const SPEED = 300.0
#pulo do player
const JUMP_VELOCITY = -500.0
var no_ar = false
#cooldown

#combate
var player: Combate
@onready var combo_timer = $combo_timer
var combo_count: int = 0
var atacando: bool = false

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

@onready var Animacao:= $AnimatedSprite2D as AnimatedSprite2D
@onready var node = get_tree().root.get_node("/root/Fase")
@onready var canvas_layer = $"../CanvasLayer/Label"
enum estado{
	ataque1,
	ataque2,
	ataque3
}








func _init():
	player = Combate.new(30, 200)

func _physics_process(delta):
	
	if not is_on_floor():
			velocity.y += gravity * delta
	elif atacando:
			Animacao.play("ataque1")
			return

	if player.vida > 0:
		
		
		if Input.is_action_just_pressed("atacar") and not no_ar:
			ataque_animacao()
			

		# Handle jump.
		if Input.is_action_just_pressed("pular") and is_on_floor():
			no_ar = true
			velocity.y = JUMP_VELOCITY
			
		elif is_on_floor():
			no_ar = false
		
		movimento_do_player()

		move_and_slide()
	else:
		pass

func get_posicao() -> float:
	return global_position.x





func ataque_animacao():
	atacando = true

	# Muda a animação com base no combo atual
	match combo_count:
		0:
			Animacao.play("ataque1")
		1:
			Animacao.play("ataque2")
		2:
			Animacao.play("ataque3")

	combo_count += 1

	# Reinicia o temporizador de combo
	if not combo_timer.is_stopped():
		combo_timer.start()

	await get_tree().create_timer(0.5).timeout

	atacando = false
	

func _on_hurtbox_body_entered(body):
	node.inimigo_atacar()	
	canvas_layer.text = str(player.vida)
	if player.vida <= 0:
		
		Animacao.stop()
		Animacao.play("derrotado") # Replace with function body.
		
func get_player():
	return player

func _on_combo_timer_timeout():
	combo_count = 0

func movimento_do_player():
	var direction = Input.get_axis("andar_para_esquerda", "andar_para_direita")
	if direction:
		Animacao.flip_h = direction < 0
			
		if Input.is_action_pressed("shift"):
			velocity.x = direction * 500.0
			Animacao.play("correndo")
				
				
		else:
			velocity.x = direction * SPEED
			if no_ar == false:
					Animacao.play("andando")
			else:
					Animacao.play("pulando")
				
		if direction > 0:
				$Golpe/CollisionShape2D.position.x = 5
				$Hurtbox/CollisionShape2D.position.x =  5
		else:
				$Golpe/CollisionShape2D.position.x = -115
				$Hurtbox/CollisionShape2D.position.x = -5
			
	else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
			Animacao.play("idle1")
		
func aumentar_vida():
	if player.vida <= 180:
		player.vida+=20
		canvas_layer.text = str(player.vida)
	else:
		pass
		
