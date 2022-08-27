transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

# Create a countdown bar, then go to the return label. It needs a '$ current_time' variable set to work properly.
screen countdown(max_time = 5, timeout_label = "start"):
    timer 0.01 repeat True action If(current_time > 0, true=SetVariable('current_time', current_time - 0.01), false=[Hide('countdown'), Jump(timeout_label)])
    bar value current_time range max_time xalign 0.5 yalign 0.8 xmaximum 300 at alpha_dissolve # This is the timer bar.

label textInput(prompt):

    # Let player type in
    $ typedIn = renpy.input(prompt).strip()

    # If they typed in nothing, repeat it.
    if typedIn == "":
        jump expression textInput(prompt)

    # Return the input, storing it in _return variable
    return typedIn

screen input_screen:
    frame:
        xalign 0.5
        yalign 0.5
        ypadding 50
        xpadding 100
        has vbox

        text "Input some text!"
        input default "Right in here!" value VariableInputValue("the_text")

        frame:
            top_margin 50
            xpadding 20
            ypadding 10
            textbutton "I'm done typing text" action Return(value="the_text")