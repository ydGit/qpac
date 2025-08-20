extends Node2D

var velocity: int = 0
var state = "rrr"

# Called when the node enters the scene tree for the first time.
func _ready():
	# velocity = 0
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if velocity != 0:
		position += delta * Vector2(velocity, 0)
		

func update_state(st : String) -> void:
	state = st
	$stateLabel.text = st
