extends Timer
class_name Temporizador


var crono : int
var texto : String
var timer:Timer
func _init(crono: int):
	self.crono = crono
	self.texto = str(crono)
	
func iniciar_cronometro():
	if timer ==null:
		timer = Timer.new()
		add_child(timer)  # Adiciona o Timer como um filho do nó Fase
		timer.wait_time = 1.0  # Define o intervalo para 1 segundo
		timer.one_shot = false  # Define o Timer para repetir

	timer.start()  # Inicia o Timer

func _on_timer_timeout():
	if crono>0:
		_diminuir_tempo()
	else:
		timer.stop()
	
func _diminuir_tempo():
	
	print(crono)
	crono -= 1

