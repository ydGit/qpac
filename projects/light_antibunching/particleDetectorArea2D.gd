extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready():
	connect("body_entered", _on_body_entered)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func calc_color(pstate: String) -> String:
	var det_set = get_parent().knob_setting
	if 'R' == pstate[det_set-1]:
		return 'red'
	else:
		return 'green'

func _on_body_entered(body):
	if is_instance_valid(body):
		var particle = body.get_parent().get_parent()
		#print(body)
		particle.velocity = 0
		particle.visible = false
		particle.queue_free()
		
		if ("red" == calc_color(particle.state)):
			get_parent().detect_red()
		else:		
			get_parent().detect_green()
