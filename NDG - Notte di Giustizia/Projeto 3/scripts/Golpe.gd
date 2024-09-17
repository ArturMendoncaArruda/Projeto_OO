extends Area2D

var jogador : Jogador
var pode_golpear: bool = true
func _ready():
	monitoring = false
	monitorable = false
	var jogador_node = get_tree().root.get_node("/root/Fase/Jogador")
	jogador = jogador_node
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if pode_golpear:
		golpear()
		
	else:
		monitoring = false
		monitorable = false
	
	
func golpear():
	if jogador.player.vida > 0:
	
		if Input.is_action_just_pressed("atacar"):
			monitoring = true
			monitorable = true
			pode_golpear = false
			await get_tree().create_timer(0.5).timeout
			pode_golpear = true
			
		
