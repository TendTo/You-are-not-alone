screen door(is_open=False, jump_to=None):
    imagebutton at door_position:
        if is_open or jump_to:
            idle "door open"
            hover "door light"
        else:
            idle "door close"
        action If(jump_to is not None, [Jump(jump_to), Hide("door")])