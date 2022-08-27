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

screen room1_pieces(room, clickable = True):

    for piece in room.pieces:
        if not piece.found:
            imagebutton:
                idle piece.idle
                xpos piece.pos[0]
                ypos piece.pos[1] 
                focus_mask True 
                action If(clickable, Return(piece.id))

label room1:
    $ room1 = Room(Piece("cerchio", "symbol 1", (100, 200)), Piece("triangolo", "symbol 2", (500, 400)))
    scene bg room1
    while True:
        call screen room1_pieces(room1, True)
        show screen room1_pieces(room1, False)

        $ room1.take_piece(_return)
        if _return == "cerchio":
            c "Sono un pazzone"
        elif _return == "triangolo":
            c "Sono una palla"
        else:
            c "Non so cosa sono"
        
        if room1.is_complete():
            c "Questo è tutto"
            jump room1_story

label room1_story:
    c "{i}Where am I?{/i}"
    c "{i}It looks like a living room...{/i}"
    c "{i}Ah, there is a door there!{/i}"
    c "{i}Let's see if I can...{/i}"
    c "{i}Wait...{/i}"
    c "{i}This door doesn't have a handle!{/i}"
    c "{i}That's weird, I've never seen something like this...{/i}"
    c "{i}It's not the only strange thing in this room...{/i}"
    c "{i}That frame...{/i}"
    c "{i}It doesn't contain any painting!{/i}"
    c "{i}I wonder why is it...{/i}"
    c "{i}{/i}"
