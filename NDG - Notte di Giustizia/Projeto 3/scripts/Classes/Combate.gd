extends Node2D
class_name Combate

var dano: int
var vida: int

func _init(dano: int, vida: int) -> void:
	self.dano = dano
	self.vida = vida

# Método para atacar o alvo
func atacar(alvo):
	alvo.receber_dano(dano)
		
			
func receber_dano(dano):
	self.vida -= dano
	print(self.vida)
	
