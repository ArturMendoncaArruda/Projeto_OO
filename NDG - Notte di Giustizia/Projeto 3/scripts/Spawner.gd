extends Node2D
class_name Spawner
var inimigos := preload("res://cenas/inimigo.tscn")
var lugares = []
@onready var main = get_node("/root/Fase")
var max_inimigos = 0
var acabou_spawner = false
func _init():
	pass
	
	
func _ready():
	for c in get_children():
		if c is Marker2D:
			lugares.append(c)


func _on_timer_timeout():
	spawnar_inimigo()
	
func get_rodada_acabou():
	return acabou_spawner
func spawnar_inimigo():
	if max_inimigos < 7:
		var spawn = lugares[randi() % lugares.size()]
		var inimigo_na_cena = inimigos.instantiate()
		inimigo_na_cena.position = spawn.position
		main.add_child(inimigo_na_cena)
		inimigo_na_cena.add_to_group("Inimigos")
		
		main.novo_inimigo(inimigo_na_cena)
		max_inimigos += 1
		acabou_spawner = false
	else:
		acabou_spawner = true
		
