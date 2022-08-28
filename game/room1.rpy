screen room1_puzzle(fifteen, clickable = True):
    layer "master"
    for square in fifteen.squares:
        if square is not None:
            imagebutton:
                focus_mask None
                idle square.idle
                pos square.pos
                if clickable:
                    action fifteen.get_action_classic(square)

label room1:
    python:
        oringin_pos = (745, 336)
        room1_puzzle = Fifteen.from_file(filename="painting1", origin_pos=oringin_pos, square_size=(110, 125), size=(4, 2))
        room1_puzzle.shuffle(1)
    scene bg green
    show screen door
    show frame 1 zorder 1:
        align(0.5, 0.4)
    show screen room1_puzzle(room1_puzzle, False)

    p "There is a room there!\nLet's see if I can..."
    p "Wait, this door doesn't have a handle!\nI've never seen something like this before!"
    p "What place did I end up in?"
    p "Now that I look closer, it's not the only strange thing in this room"
    p "The painting on the wall is illegible"
    p "Maybe if I move the pieces around..."

    jump room1_puzzle

label room1_puzzle:
    call screen room1_puzzle(room1_puzzle, True)

    show painting1:
        anchor (0, 0)
        pos oringin_pos
    show frame opening
    with None

    jump room1_complete

label room1_complete:
    show donn still onlayer character
    with fade
    u "Do you like it?"
    p "Is it an habit of yours to scare people like that?"
    u "I have this effect on many."
    u "So, what do you think about it?"
    p "I don't know, let me think..."

    p "..."
    p "..."

    p "It is a somewhat distressing picture, to tell the truth.\nI've never been a huge Bosch fan"
    p "The painting of someone who has struggled to achieve something in his life and still loses it all upon the arrival of Death"
    p "I would never keep something like this in my house"
    t "{i}It would awaken too many memories...{/i}"
    u "Do you think you can escape the pain of Death for all your life?"
    p "No, but I don't see why I have to think about it now"
    u "..."
    p "You didn't tell me anything about you. What' your name?"
    u "I'm Donn"
    p "Can you tell me something about this mansion?"
    d ""

    hide donn still onlayer character
    show brush:
        align (.81, .45)
    show screen door
    with fade

    t "{i}I can see something on the door now...\nIt looks like a brush...{/i}"
    t "{i}I'm starting to remember something...{/i}"

    call screen door(jump_to="room2")
    jump room2