# Game over screen.
init:
    screen gameover_screen:
        vbox:
            xalign 0.5
            yalign 0.5
            textbutton "Retry" action Jump("start") text_size 54
            textbutton "Quit" action Return() text_size 54

label game_over:

    scene black with Dissolve(3.0)

    call screen gameover_screen
