extends Node2D

@export var stiffness: float = 10.0  # Newton / m
@export var mass: float = 9  # kilogram, mass of the object
@export var v0: float = 0.0  # initial speed
@export var x0: float = 0.02  # initial position
#@export var side: int = 1  # which side of the spring the body is on
var side: int

var amplitude: float

var draw_scale = 3200

var osc_freq = 2*PI*sqrt(stiffness/mass)
var time = 0
var dx = 0  # body displacement
var phase = 0


var stretch_scale = 0

var body_ini_pos
var body_curr_pos
var body_ini_vel
var wall_pos

var body_edge_ini_pos
var body_edge_pos

var spring_initial_length
var spring_current_length
var spring_ini_pos
var spring_curr_scl

# Called when the node enters the scene tree for the first time.
func _ready():
	# total energy and maximum displacement
	var E = mass*v0*v0/2 + stiffness*x0*x0/2
	amplitude = sqrt(2*E/stiffness)
	
	wall_pos = $wall_edge.transform.get_origin()
	body_edge_ini_pos = $body_edge.transform.get_origin()
	# determine on which side of the wall the body is moving
	if body_edge_ini_pos[0] > wall_pos[0]:
		side = 1
	else:
		side = -1
	spring_initial_length = abs(body_edge_ini_pos[0]-wall_pos[0])
	spring_ini_pos = $spring.transform.get_origin()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta  # update clock
	# calculate displacement
	dx = amplitude * cos(osc_freq*time)
	# move body
	body_curr_pos = body_edge_ini_pos + Vector2(side * draw_scale * dx, 0)
	$body_edge.transform.origin = body_curr_pos
	# stretch and move spring
	spring_current_length = abs((body_curr_pos-wall_pos)[0])
	spring_curr_scl = spring_current_length / spring_initial_length
	$spring.scale = Vector2(spring_curr_scl, 1)
#	# shift the spring's center
	$spring.transform.origin = spring_ini_pos + Vector2(side * draw_scale * dx/2, 0)
	
	
	
	
