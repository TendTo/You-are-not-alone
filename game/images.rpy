image highlight0:
    "_highlight"
    alpha 0
    linear .25 alpha .3
    pause .2
    "_highlight"
    linear .5 alpha 0.0

image highlight1:
    "_highlight"
    alpha 0
    linear .25 alpha .3
    pause .2
    "_highlight"
    linear .5 alpha 0.0

image highlight2:
    "_highlight"
    alpha 0
    linear .25 alpha .3
    pause .2
    "_highlight"
    linear .5 alpha 0.0

image highlight3:
    "_highlight"
    alpha 0
    linear .25 alpha .3
    pause .2
    "_highlight"
    linear .5 alpha 0.0

image frame opening:
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

transform door_position:
    align (0.84, 0.83)

image door close:
    "_door close"

image door open:
    "_door open"

image door light:
    "_door light"

image door opening:
    "_door close"
    pause 0.4
    "_door open"
    pause 0.4
    "_door light"

image intro slide:
    "intro"
    xalign 0.5
    yalign 0.5
    linear 30.0 yalign 0.1
    pause .1
    linear 30.0 yalign 0.5
    pause .1
    repeat