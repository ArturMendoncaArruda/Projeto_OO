extends ProgressBar
@onready var dano = $dano
@onready var timer = $Timer

var vida := 100:
	set = _set_health
	
func _init_vida(_vida):
	vida = _vida
	max_value = vida
	value = vida
	dano.max_value = vida
	dano.value = vida
	
func _set_health(nova_vida):
	var vida_antiga = vida
	vida = min(max_value,nova_vida)
	value = vida
	if vida ==0:
		queue_free()
	if vida< vida_antiga:
		timer.start()
	else:
		dano.value = vida


func _on_timer_timeout():
	dano.value = vida
