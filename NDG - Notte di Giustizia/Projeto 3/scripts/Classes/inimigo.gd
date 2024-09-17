extends CharacterBody2D
class_name inimigo
var direction = 0
const SPEED = 150.0
@onready var controle_de_dinheiro := get_tree().root.get_node("/root/Fase/dinheiro")
@onready var jogador := get_node("/root/Fase/Jogador")
@onready var node = get_tree().root.get_node("/root/Fase")
@onready var Animacao:= $AnimatedSprite2D as AnimatedSprite2D
var combate: Combate
var dinheiro = Usuario.instancia
var url_ganhar_dinheiro = "http://127.0.0.1:8000/dinheiro"
var din: int = 0
var forca_knockback = 1000.0
var knockback = 0.0
@onready var vida = $vida

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
func _init():
	
	combate = Combate.new(20, 100)
	

func _ready():
	din = dinheiro.get_id_usuario()
	vida._init_vida(combate.vida)

func _physics_process(delta):
	if combate.vida > 0:
		direcao_player_inimigo()
		
		velocity.x = direction * SPEED + knockback
		knockback = lerp(knockback, 0.0, 0.1)
		if not is_on_floor():
			velocity.y += gravity * delta
		
		move_and_slide()
	else:
		acabou()
func get_posicao():
	var posicao_global_inimigo = global_position.x
	return posicao_global_inimigo
	
func direcao_player_inimigo():
	if jogador != null:
		Animacao.play("andar")
		await get_tree().create_timer(1).timeout
		Animacao.flip_h = direction < 0
		
		if jogador.get_posicao() < get_posicao():
			direction = -1
			
			
		else:
			direction = 1
			
	


func _on_hitbox_area_entered(area):
	if area.is_in_group("a"):
		jogador.player.atacar(combate)
		if (area.global_position.x - global_position.x) > 0:
			knockback = -forca_knockback
		else:
			knockback = forca_knockback
		vida.vida = combate.vida
		Animacao.play("atacar")
	
	
func get_inimigo():
	return combate

func acabou():
	controle_de_dinheiro.mudar_dinheiro(din,50)
	controle_de_dinheiro.ver_dinheiro()
	Animacao.play("caido")
	await get_tree().create_timer(0.38).timeout
	
	
	queue_free()
	

