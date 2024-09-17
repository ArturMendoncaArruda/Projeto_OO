extends Area2D
@onready var loja = $"../Loja"
@onready var Animacao := $AnimatedSprite2D as AnimatedSprite2D
@onready var canvas_layer = $"../CanvasLayer"
@onready var spawner = $"../Spawner"
@onready var dinheiro = $"../dinheiro"

var entrou: bool = false
var loja_aberta = false
func _ready():
	Animacao.play("idle1")
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	player_perto()
	
	


func _on_body_entered(body):
	if spawner.get_rodada_acabou():
		entrou = true
		print(entrou)
		if body.is_in_group("Jogador"):
			Animacao.play("abrir")
		
func player_perto():
	if Input.is_action_just_pressed("atacar") and entrou:
		loja_aberta = true
		canvas_layer.visible = false
		dinheiro.visible = true
		abrir_loja()
			
			
	else:
		
		loja_aberta = false
		canvas_layer.visible = true
		dinheiro.visible = false
		

func _on_body_exited(body):
	Animacao.play("fechar")
	entrou = false
	

func _on_animated_sprite_2d_animation_finished():
	if Animacao.animation == "fechar":
		Animacao.play("idle1")
		
func abrir_loja():
	
	loja_aberta = true
	get_tree().paused = true
	Animacao.play("comprar")
	loja.visible = true

	
