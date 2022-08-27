init python:
    from scripts import *

label start:
    jump introduction

label introduction:
    scene black

    u "Welcome back!"
    u "I'm Mike of the Desert!"
    p "Who... is talking? Where... am I?"

    scene bg brown
    show donn still
    show screen door(is_open=False)
    with fade

    p "Who are you?"
    p "Where am I?"
    p "I can't remember anything!"
    u "..."
    p "Ehi, I'm talking with you!"
    p "Can you tell me where we are?"
    u "..."
    t "{i}Is she pretending she can't hear me?{/i}"
    t "{i}At a closer look, she gives me chills...{/i}"
    t "{i}Maybe there is a way to leave this place...{/i}"
    u "The only way out is to cross the villa through the corridor behind me."
    t "{i}What? How did she... Was I thinking out loud?{/i}"
    p "Thank you!"
    t "{i}Better get out of this place as quickly as possible{/i}"

    # Il giocatore può cliccare sul corridoio per entrare nella STANZA N. 1
    call screen door(jump_to="room1")
