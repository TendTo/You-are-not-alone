screen door(jump_to=None):
    layer 'master'
    imagebutton at door_position:
        idle "door close"
        action If(jump_to is not None, [Jump(jump_to), Hide("door")])
