extends Temporizador
class_name Rodada
var comecou = false
func _init(crono: int):
	super._init(crono)
	
	
	
func pausa_round():
	comecou = false
	iniciar_cronometro()
	if self.crono >= 0:
		comecou = true
	
