transform table_on_groud:
    yalign 0.9
transform wadrabe_on_groud:
    yalign 0.6
transform frame_position:
    xalign 0.5
    yalign 0.5

transform frame_opening:
    "frame 1"
    pause 0.4
    "frame 2"
    pause 0.4
    "frame 3"
    pause 0.4
    "frame 4"
    pause 0.4
    "frame 5"
    pause 0.4

image frame opening:
    contains frame_opening

screen room1_props(room):
    fixed:
        image "table vase" at table_on_groud:
            xalign 0.5
        image "wadrabe close" at wadrabe_on_groud:
            xalign 0.9
        if not room.is_piece_taken(0):
            image "symbol 2":
                align (0.9, 0.5)
        if not room.is_piece_taken(1):
            image "symbol 1":
                align (0.5, 0.5)


screen room1_pieces(room):
    fixed:
        if not room.is_piece_taken(0):
            imagebutton:
                focus_mask None
                align (0.9, 0.5)
                idle "symbol 2"
                action room.action_take_piece(0)
        if not room.is_piece_taken(1):
            imagebutton:
                focus_mask None
                align (0.5, 0.5)
                idle "symbol 1"
                action room.action_take_piece(1)

label room1:
    $ room1 = Room("Room 1", "This is room 1", 2)
    scene bg room1
    show screen room1_props(room1)
    show frame 1 at frame_position
    c "Trova i segni del pazzo lepes!"
    call screen room1_pieces(room1)
    show frame opening at frame_position
    c "Ma sei un pro!"
    ""
