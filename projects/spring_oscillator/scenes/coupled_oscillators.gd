extends Node2D

var left_osc_ini_pos: Vector2
var right_osc_ini_pos: Vector2
var spring_ini_scale
var spring_ini_length
var spring_ini_pos

var left_osc_pos
var right_osc_pos
var spring_length
var spring_scale
var spring_pos

var time: float = 0


# Called when the node enters the scene tree for the first time.
func _ready():
	left_osc_ini_pos = $oscillatorLeft/body_edge.get_global_position()
	right_osc_ini_pos = $oscillatorRight/body_edge.get_global_position()
	spring_ini_length = abs((left_osc_ini_pos-right_osc_ini_pos)[0])
	spring_ini_scale = $spring.get_global_scale()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta
	
	left_osc_pos = $oscillatorLeft/body_edge.get_global_position()
	right_osc_pos = $oscillatorRight/body_edge.get_global_position()
	spring_length = abs((left_osc_pos-right_osc_pos)[0])
	spring_scale = spring_length / spring_ini_length	
	$spring.set_global_scale(Vector2(spring_ini_scale[0]*spring_scale, 
									 spring_ini_scale[1]))
	
