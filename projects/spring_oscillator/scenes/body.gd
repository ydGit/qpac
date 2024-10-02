extends Sprite2D

@export var stiffness: float = 10.0  # Newton / m
@export var mass: float = 9  # kilogram, mass of the object
@export var stretch: float = 0.02  # initial stretch

var osc_freq = 2*PI*sqrt(stiffness/mass)
var time = 0
var phase = 0
var stretch_scale = 0

var draw_scale = 3200

var current_position
var current_scale

var initial_position

var spring_initial_scale
var spring_initial_position

# Called when the node enters the scene tree for the first time.
func _ready():
	initial_position = self.transform.get_origin()
	spring_initial_scale = get_parent().transform.get_scale()
	spring_initial_position = get_parent().transform.get_origin()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta
	phase = cos(osc_freq*time)
	# move body
	self.transform.origin = Vector2(initial_position[0]+draw_scale * stretch * phase, 
									initial_position[1])
	# move spring center
	get_parent().transform.origin = Vector2(spring_initial_position[0]+ draw_scale * stretch * phase/2.0, 
									spring_initial_position[1])
	# strech the spring
	stretch_scale = 1 + draw_scale * stretch * phase / initial_position[0]
	get_parent().scale = Vector2(spring_initial_scale[0]*stretch_scale, spring_initial_scale[1])
	
	
	
	
