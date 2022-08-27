init python:
    from scripts import *

define char_name = ''
define c = Character("[char_name]", what_color="#6fff76")
define n = Character("", what_color="#6fa9ff")
define d = Character("Death", who_color="#fff", what_color="#6d0000")

label start:
    jump room1

label introduction:
    scene bg studio
    n "{i}You are not alone{/i}"
    e "{i}This sentence keeps running through my head.{/i}"
    e "{i}It is true.{/i}"
    e "{i}I'm not alone.{/i}"
    e "{i}This mansion feels familiar, but I can't put my finger on it.{/i}"
    e "{i}Something draws me here.{/i}"
    show girl faceaway at center with fade
    d "Welcome back!"
    e "{i}Back? From where?{/i}"
    e "{i}Have I already been here?{/i}"

    menu:
        "Move on":
            jump room1
        "Stay here":
            return

