extends Control
@onready var cadastro = $cadastro
@onready var usuario = $Usuario
@onready var senha = $Senha
@onready var api = $HTTPRequest
@onready var color_rect = $ColorRect
@onready var cadastrado = $cadastrado
@onready var ja_existe = $ja_existe
@onready var ok = $ok
var url_cadastro = "http://127.0.0.1:8000/cadastro"  # Substitua pelo IP real do contêiner
var teste = Usuario.new()
func _ready():
	cadastrado.visible = false
	color_rect.visible = false
	ja_existe.visible = false
	ok.visible = false
	print(teste.get_id_usuario())


	
func cadastro_pro_banco(usuario,senha):
	var headers: Array = ["Content-Type: application/json"]
	var cadastro_request: String = '{"usuario_nome": "' + usuario + '", "usuario_senha": "' + senha + '"}'
	
	var error = api.request(url_cadastro, headers, HTTPClient.METHOD_POST, cadastro_request)
	print(cadastro_request)
	

func cadastrado_user():
	tela2()
	cadastrado.visible = true
	
func usuario_existe():
	tela2()
	ja_existe.visible = true
	
func tela2():
	color_rect.visible = true
	ok.visible = true
	

func _on_http_request_request_completed(result, response_code, headers, body):
	var json = body.get_string_from_utf8()
	print(json)
	if response_code == 201:
		cadastrado_user()
	elif response_code == 400:
		usuario_existe()

func _on_cadastro_pressed():
	cadastro_pro_banco(usuario.text,senha.text)


func _on_voltar_pressed():
	get_tree().change_scene_to_file("res://cenas/menu.tscn") 



	



func _on_ok_pressed():
	ja_existe.visible = false
	color_rect.visible = false
	cadastrado.visible = false
	ok.visible = false
