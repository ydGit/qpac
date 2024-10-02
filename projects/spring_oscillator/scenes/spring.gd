extends Sprite2D

@export var stiffness: float = 10.0  # Newton / m
@export var mass: float = 9  # kilogram, mass of the object
@export var stretch: float = 0.02  # initial stretch

var draw_scale = 3200

var current_position
var current_scale

var initial_position
var initial_scale
var body_initial_position

var osc_freq = 2*PI*sqrt(stiffness/mass)
var time = 0
var phase = 0
var stretch_scale = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	initial_position = self.transform.get_origin()
	initial_scale = self.transform.get_scale()
	body_initial_position = $body.transform.get_origin()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta
	phase = cos(osc_freq*time)
	$body.transform.origin = Vector2(body_initial_position[0]+draw_scale * stretch * phase, body_initial_position[1])
	stretch_scale = 1 + draw_scale * stretch * phase / initial_position[0]
	self.scale = Vector2(initial_scale[0]*stretch_scale, initial_scale[1])
	self.transform.origin = Vector2(initial_position[0]+ draw_scale * stretch * phase/2.0, initial_position[1])
	
	
	
