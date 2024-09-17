extends Node2D
class_name Fase
var jogador : Jogador
var inimigo_a = inimigo
var inimigos : Array = [] 
@onready var cronometro = $cronometro
@onready var timer = $Timer
@onready var loja = $Loja
@onready var spawner = $Spawner
@onready var start = $CanvasLayer/Button
@onready var label = $CanvasLayer/Label
@onready var dinheiro = $dinheiro

var jogo_pausado = false


func _ready():
	jogador = get_node("/root/Fase/Jogador")
	inimigo_a = inimigo_a.new()
	loja.visible = false
	dinheiro.visible = false
	start.visible = true
	
func _process(delta):
	pass
	
	
	
func novo_inimigo(novo_inimigo):
	inimigos.append(novo_inimigo) 

func inimigo_atacar():
	
	var player_combate = jogador.get_player()
	var inimigo_combate = inimigo_a.get_inimigo()
	inimigo_combate.atacar(player_combate)
	
				# Não remova o inimigo, pois ainda não foi derrotado
				


	
