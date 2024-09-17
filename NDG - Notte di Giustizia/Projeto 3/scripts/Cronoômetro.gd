extends Control
class_name  Tempo



func _init(crono):
	
	self.crono = crono
	self.texto = str(crono)
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	iniciar_cronometro()
	
	
func iniciar_cronometro():
	while self.crono > 0:
			await get_tree().create_timer(1).timeout
			diminuir_tempo(self.crono)
	pass


func diminuir_tempo(tempo):
	tempo -= 1
	print(tempo)
		
