extends Sprite2D

var left_position
var right_position 
var source_particle = load("res://scenes/particle.tscn")

var launch_speed = 400

var is_mouse_over_button = false

var rng = RandomNumberGenerator.new()

var states = ["RRR", "RRG", "RGR", "RGG",
			  "GGG", "GGR", "GRG", "GRR"]

# Called when the node enters the scene tree for the first time.
func _ready():
	rng.seed = hash("quantum_mechanics")
	
	left_position = get_parent().get_node("emitter_left").position
	right_position = get_parent().get_node("emitter_right").position		
	
	#$collider.mouse_entered.connect(Callable(self, "_on_mouse_entered"))
	#$collider.mouse_exited.connect(Callable(self, "_on_mouse_exited"))
	#get_node("collider").connect("mouse_entered", _on_mouse_entered)
	#get_node("collider").connect("mouse_exited", _on_mouse_exited)
	$collider.connect("mouse_entered", _on_mouse_entered)
	$collider.connect("mouse_exited", _on_mouse_exited)
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func lmb_pressed(event: InputEvent) -> bool:
	return event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT


func emit_left_particle(state):
	var new_left_particle = source_particle.instantiate()
	new_left_particle.position = left_position		
	new_left_particle.visible = true
	new_left_particle.velocity = -launch_speed	
	new_left_particle.state = state
	new_left_particle.update_state(state)
	get_parent().add_child(new_left_particle)		
	
func emit_right_particle(state):
	var new_right_particle = source_particle.instantiate()
	new_right_particle.position = right_position		
	new_right_particle.visible = true
	new_right_particle.velocity = launch_speed	
	new_right_particle.state = state
	new_right_particle.update_state(state)
	get_parent().add_child(new_right_particle)
	

func _input(event: InputEvent) -> void:
	if lmb_pressed(event) and is_mouse_over_button:
		var idx = rng.randi_range(0, 7)
		var state = states[idx]
		emit_left_particle(state)
		emit_right_particle(state)
		
		#print(new_left_particle.position)
		
func _on_mouse_entered():
	is_mouse_over_button = true
	
func _on_mouse_exited():
	is_mouse_over_button = false
