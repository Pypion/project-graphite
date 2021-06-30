# Game over screen.
label gameover:
    call screen gameover_screen

screen gameover_screen:
    vbox:
        xalign 0.5
        yalign 0.8
        textbutton "Retry" action Jump("start")
        textbutton "Quit" action Return()