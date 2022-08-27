transform table_on_groud:
    yalign 0.9
transform wadrabe_on_groud:
    yalign 0.6
transform frame_position:
    xalign 0.5
    yalign 0.5

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
                focus_mask None
                idle piece.idle
                if piece.pos:
                    pos piece.pos
                else:
                    align piece.align
                action If(clickable, Return(piece.id))

screen room1_fifteen_classic(fifteen, clickable = True):
    for square in fifteen.squares:
        if square is not None:
            imagebutton:
                focus_mask None
                idle square.idle
                pos square.pos
                action fifteen.get_action_classic(square)

screen room1_fifteen_teleport(fifteen, clickable = True):
    for square in fifteen.squares:
        if square is not None:
            imagebutton:
                focus_mask None
                idle square.idle
                pos square.pos
                action fifteen.get_action_teleport(square)

screen room1_fifteen_no_error(fifteen, clickable = True):
    for square in fifteen.squares:
        if square is not None:
            imagebutton:
                focus_mask None
                idle square.idle
                pos square.pos
                action fifteen.get_action_no_error(square)

label room1:
    jump room1_fifteen

label room1_fifteen:
    python:
        oringin_pos = (778, 18)
        fifteen = Fifteen.from_file(filename="picture", origin_pos=oringin_pos, square_size=(80, 107), size=(4, 9))
        fifteen.shuffle(3)
    scene bg room1
    show highlight1

    call screen room1_fifteen_classic(fifteen, clickable = True)
    show picture 1:
        anchor (0, 0)
        pos oringin_pos
    c "FEST!"

    python:
        oringin_pos = (778, 18)
        fifteen = Fifteen.from_file(filename="picture", origin_pos=oringin_pos, square_size=(80, 107), size=(4, 9))
        fifteen.shuffle(5)
    scene bg room1

    call screen room1_fifteen_teleport(fifteen, clickable = True)
    show picture 1:
        anchor (0, 0)
        pos oringin_pos
    c "FEST!"

    python:
        oringin_pos = (778, 18)
        fifteen = Fifteen.from_file(filename="picture", origin_pos=oringin_pos, square_size=(80, 107), size=(4, 9))
        fifteen.shuffle(5)
    scene bg room1

    call screen room1_fifteen_no_error(fifteen, clickable = True)
    show picture 1:
        anchor (0, 0)
        pos oringin_pos
    c "FEST!"


label room1_pieces:
    $ room1 = Room(Piece("cerchio", "symbol 2", pos=(100, 200)), Piece("triangolo", "symbol 1", align=(0.57, 0.14)))
    scene bg room1

    while True:
        call screen room1_pieces(room1, True)
        show screen room1_pieces(room1, False)

        $ room1.take_piece(_return)
        $ n_pieces_found = room1.n_piece_found()
        if n_pieces_found == 1:
            c "Sono un pazzone"
        elif n_pieces_found == 2:
            c "E questo è il "
        else:
            c "Non so cosa sono"
        
        if room1.is_complete():
            c "Questo è tutto"
            jump room1_complete

label room1_complete:
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
