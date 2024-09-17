extends Control

@onready var senha = $Senha
@onready var api = $HTTPRequest
@onready var usuario = $Usuario
@onready var jogar_button = $Login
@onready var color_rect = $ColorRect
@onready var senha_ruim = $senha_ruim
@onready var usuario_nao_existe = $usuario_nao_existe
@onready var ok = $ok
@onready var usuario_banco = $Usuario_existente
var url_login = "http://127.0.0.1:8000/godot/"
var player_usuario = Usuario.new()

func _ready():
	
	senha_ruim.visible = false
	color_rect.visible = false
	usuario_nao_existe.visible = false
	ok.visible = false

	

func _on_login_pressed():
	login(usuario.text,senha.text)
	
func login(usuario,senha):
	var headers: Array = ["Content-Type: application/json"]
	var login_request: String = '{"usuario_nome": "' + usuario + '", "usuario_senha": "' + senha + '"}'
	
	var error = api.request(url_login, headers, HTTPClient.METHOD_POST, login_request)
	print(login_request)
	
func _on_http_request_request_completed(result, response_code, headers, body):
	var json = body.get_string_from_utf8()
	var json_result = JSON.parse_string(json)
	print(json)
	if response_code == 200:
		var user_id = json_result["user_id"]
		
		player_usuario.set_id_usuario(user_id)
		print(player_usuario.get_id_usuario())
		
		get_tree().change_scene_to_file("res://cenas/fase1.tscn")
	elif response_code == 401:
		senha_incorreta()
	elif response_code == 404:
		nao_tem_usuario()
func nao_tem_usuario():
	tela2()
	usuario_nao_existe.visible = true
	
func senha_incorreta():
	tela2()
	senha_ruim.visible = true
	
func tela2():
	color_rect.visible = true
	ok.visible = true
	

func _on_ok_pressed():
	senha_ruim.visible = false
	color_rect.visible = false
	usuario_nao_existe.visible = false
	ok.visible = false
	


func _on_voltar_pressed():
	get_tree().change_scene_to_file("res://cenas/menu.tscn")
