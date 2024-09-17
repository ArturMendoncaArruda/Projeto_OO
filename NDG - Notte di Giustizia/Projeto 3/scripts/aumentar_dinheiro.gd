extends Control

class_name Controle_dinheiro
@onready var http = $http
@onready var texture_rect = $TextureRect
var valor_inicial = Usuario.instancia
@onready var http_request = $HTTPRequest
@onready var label = $Label
var valor_no_texto: int 
var dinheiro_inicial: int
var url_ganhar_dinheiro = "http://127.0.0.1:8000/dinheiro"
var url_ver_dinheiro = "http://127.0.0.1:8000/get_dinheiro?user_id="

func _ready():
	var banco = valor_inicial.get_id_usuario()
	
	
func mudar_dinheiro(identificação_do_usuario, valor):
	var headers: Array = ["Content-Type: application/json"]
	var dinheiro_request: String = '{"user": ' + str(identificação_do_usuario) + ', "valor": ' + str(valor) +'}'
	var error = http.request(url_ganhar_dinheiro, headers, HTTPClient.METHOD_POST, dinheiro_request)

func ver_dinheiro():
	var user_id = valor_inicial.get_id_usuario()
	var url_ver_dinheiro_mesmo = url_ver_dinheiro + str(user_id)
	var error = http_request.request(url_ver_dinheiro_mesmo)
	
func _on_http_request_completed(result, response_code, headers, body):
	var json = body.get_string_from_utf8()

	if response_code == 200:
		print("recompensa tchim tchim", json)
	else:
		print("erro")
	
	


func _on_http_request_request_completed(result, response_code, headers, body):
	var resposta = body.get_string_from_utf8()
	valor_no_texto = int(resposta)
	if response_code == 200:
		label.text = str(valor_no_texto)
	elif response_code == 400:
		print("precisa do id")
	elif response_code == 404:
		print("não existe esse usuario")
	
