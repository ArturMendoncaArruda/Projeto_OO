extends Object
class_name  Usuario
var usuario_id: int = 0
#ESSE É MEU SINGLETON
static var instancia: Usuario = null
func _init():
	if instancia == null:
		instancia = self
	else:
		pass
	
	
func set_id_usuario(id_novo: int):
	self.usuario_id = id_novo

func get_id_usuario():
	return self.usuario_id
