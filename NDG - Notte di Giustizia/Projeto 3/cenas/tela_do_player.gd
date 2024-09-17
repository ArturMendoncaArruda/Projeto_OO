extends CanvasLayer
@onready var label = $Label
@onready var http = $"../dinheiro/"
@onready var spawner = $/root/Fase/Spawner
@onready var botao = $Button
var valor_inicial = Usuario.instancia
@onready var conexao = $HTTPRequest

# Called when the node enters the scene tree for the first time.
func _ready():
	
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if spawner.acabou_spawner:
		botao.visible = true
	else:
		botao.visible = false


func _on_button_pressed():
	spawner.max_inimigos = 0
	spawner.acabou_spawner = false
	
