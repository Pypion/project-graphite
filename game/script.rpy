# Love points.
#label points_love:
#    $ points_love = 0

# Game over screen.
#label gameover:
#    call screen gameover_screen

#screen gameover_screen:
#    vbox:
#        xalign 0.5
#        yalign 0.8
#        textbutton "Retry" action Jump("start")
#        textbutton "Quit" action Return()

# Characters.
define j = Character("James")
define e = Character("Emily")
define c = Character("Caleb")

# Scene 0.
label start:

    scene bg room

    j "It's the first day of the final year of high school."

    j "I've always liked my childhood friend, Emily, but I haven't yet confessed
to her."

    j "I'm going to do it this year."

    show character-emily

    return

    #scene gameover with dissolve

    #jump gameover
