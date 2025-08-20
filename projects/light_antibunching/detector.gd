extends Node2D

var setting_in_focus = 0
var knob_setting = 1

var red1_count: int = 0
var green1_count: int = 0
var red2_count: int = 0
var green2_count: int = 0
var red3_count: int = 0
var green3_count: int = 0

var results = []

# Called when the node enters the scene tree for the first time.
func _ready():
	$light_red.visible = false
	$light_green.visible = false
	
	get_node("setting1").connect("mouse_entered", _update_setting1)
	get_node("setting2").connect("mouse_entered", _update_setting2)
	get_node("setting3").connect("mouse_entered", _update_setting3)
	
	get_node("setting1").connect("mouse_exited", _reset_setting)
	get_node("setting2").connect("mouse_exited", _reset_setting)
	get_node("setting3").connect("mouse_exited", _reset_setting)
	
	$knob.rotation_degrees = -45
	
	#var someColor = Color(1,0,0) 
	get_node("red1Count").text = str(red1_count)
	get_node("red2Count").text = str(red2_count)
	get_node("red3Count").text = str(red3_count)
	
	get_node("green1Count").text = str(green1_count)
	get_node("green2Count").text = str(green2_count)
	get_node("green3Count").text = str(green3_count)
	#$redCount.label_settings.set_font_color(someColor)
	#get_node("redCount").label_settings.font_color = someColor	
	#get_node("greenCount").text = str(green_count)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func lmb_pressed(event: InputEvent) -> bool:
	return event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT

func _input(event):
	if lmb_pressed(event):
		if 1 == setting_in_focus:
			$knob.rotation_degrees = -45
			knob_setting = 1
			$audio.play()
		if 2 == setting_in_focus:
			$knob.rotation_degrees = 0
			knob_setting = 2
			$audio.play()
		if 3 == setting_in_focus:
			$knob.rotation_degrees = 45
			knob_setting = 3
			$audio.play()


func _update_setting1():
	setting_in_focus = 1
	
func _update_setting2():
	setting_in_focus = 2
	
func _update_setting3():
	setting_in_focus = 3
	
func _reset_setting():
	setting_in_focus = 0
	
func detect_red():
	if 1 == knob_setting:
		red1_count += 1
		get_node("red1Count").text = str(red1_count)		
	if 2 == knob_setting:
		red2_count += 1
		get_node("red2Count").text = str(red2_count)	
	if 3 == knob_setting:
		red3_count += 1
		get_node("red3Count").text = str(red3_count)	
		
	get_node("light_green").visible = false
	get_node("light_red").visible = true
	
	results.append(str(knob_setting)+"R")
	print(results)
		
	
func detect_green():
	if 1 == knob_setting:
		green1_count += 1
		get_node("green1Count").text = str(green1_count)
	if 2 == knob_setting:
		green2_count += 1
		get_node("green2Count").text = str(green2_count)
	if 3 == knob_setting:
		green3_count += 1
		get_node("green3Count").text = str(green3_count)	
		
	get_node("light_green").visible = true
	get_node("light_red").visible = false
	
	results.append(str(knob_setting)+"G")
	print(results)
	
	
