extends Button
var jogador : Jogador
@onready var controle_de_dinheiro := get_tree().root.get_node("/root/Fase/dinheiro")
var singleton = Usuario.instancia
@onready var timer = $Timer
var botao_desativado = false
@onready var b_1 = $"."
var valor : int

func _ready():
	jogador = get_node("/root/Fase/Jogador")
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	valor = int(controle_de_dinheiro.valor_no_texto)






func _on_timer_timeout():
	b_1.visible = true


func _on_pressed():
	b_1.visible = false
	jogador.aumentar_vida()
	var texto = valor - 50
	controle_de_dinheiro.label.text = str(texto)
	controle_de_dinheiro.mudar_dinheiro(singleton.get_id_usuario(),-50)
	print("comprou")
	timer.start()
	
