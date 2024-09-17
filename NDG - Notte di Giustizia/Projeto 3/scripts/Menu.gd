extends Control

func _on_jogar_pressed():
	get_tree().change_scene_to_file("res://cenas/jogar.tscn")


func _on_sair_pressed():
	get_tree().quit()


func _on_conta_pressed():
	get_tree().change_scene_to_file("res://cenas/cadastro.tscn")
