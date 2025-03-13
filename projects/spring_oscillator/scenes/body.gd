extends Sprite2D

@export var stiffness: float = 10.0  # Newton / m
@export var mass: float = 9  # kilogram, mass of the object
@export var amplitude: float = 0.02  # initial stretch
@export var side: int = 1  # which side of the spring the body is on

var osc_freq = 2*PI*sqrt(stiffness/mass)
var time = 0
var phase = 0
var stretch_scale = 0
var d = 0

var draw_scale = 3200

var current_position
var current_scale

var initial_position

var spring_left_end
var spring_right_end

var spring_initial_scale
var spring_initial_position

# Called when the node enters the scene tree for the first time.
func _ready():
	initial_position = self.transform.get_origin()
	
	spring_initial_scale = get_parent().transform.get_scale()
	spring_initial_position = get_parent().transform.get_origin()
	
	spring_left_end = get_parent().get_node("spring_left_end").transform.get_origin()
	spring_right_end = get_parent().get_node("spring_right_end").transform.get_origin()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta
	phase = cos(osc_freq*time)
	d = draw_scale * amplitude * phase
	# move body
	self.transform.origin = Vector2(initial_position[0]+d, initial_position[1])
	# move spring center
	get_parent().transform.origin = Vector2(spring_initial_position[0]+ d/2.0, 
									spring_initial_position[1])
	# strech the spring
	stretch_scale = 1 + side * d / initial_position[0]
	get_parent().scale = Vector2(spring_initial_scale[0]*stretch_scale, spring_initial_scale[1])
	
	
	
	
