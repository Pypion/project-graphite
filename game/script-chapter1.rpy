# Chapter 2.

label chapter1:

    scene black with Dissolve(1.5)

    #play sound "sch-bell.wav"

    j "{i}For the first day back from class, there sure is a lot of homework.\
    {\i}"

    j "{i}This is ridiculous.{\i}"

    j "{i}Senior year is supposed to be a cakewalk…{\i}"

    scene loc-sch-ext with Dissolve(1.0)

    if jerk_off == True:

        j "Whatever,{w} parents are gonna be home for another hour or two,{w}\
        gives me plenty of time to go fire off some knuckle children."

        jump game_over

    elif chapter0_sub_route == "B" or chapter0_sub_route == 2:

        jump r3B0

    elif chapter0_sub_route == "C" or chapter0_sub_route == 1:

        jump r2C0


    label r3B0:

        j "{i}Whatever, it's not due this week, so I have time.{\i}"

        j "{i}I guess I could check out that club fair Emily was talking about.\
        {\i}"

        return #jump club_selection


    label r2C0:

        j "{i}How lame...{\i}"

        j "{i}At least it's a nice day, I can head to the cafe and sit on the\
        patio and finish reading manga.{\i}"

        # Celia enters, bumps into James, dropping something glass

        ce "Mierda!{w} That piece took me weeks!"

        j "Oh!{w} Sorry…"

        ce "(sighs) No, it was my fault, I was trying to carry too much."

        # Another piece drops

        ce "Damn it!"

        j "Here, let me help you."

        ce "Really?{w} Thanks! You're a Lifesaver!"

        j "Yeah, no problem. Where are you headed?"

        ce "To the student commons! I have to set up for the club fair."

        j "{i}There goes my cafe and manga idea…{\i}"

        ce "Are you in any clubs?"

        j "no, I never really-{nw}"

        #Celia excited expression

        ce "What!{w} You should totally join the art club then!"

        ce "We have soooo much fun, especially this year with the festival, a\
        girl is making plaaaaans."

        ce "I mean, when I say we,{w} I just mean me, at the moment,{w} but\
        that's all about to change right?"

        j "I’m sure--{nw}"

        ce "Oh!{w} Last year, we did that big mural on the side of the school,\
        by the teachers parking lot?"

        ce "We got hella push back because admi wanted some boring ass picture\
        of the mascot,"

        ce 'but we were like “no, fuck that” this is a working class community\
        with hella history and heritage right?'

        ce "So we wanted to put something that reflected that."

        j "Yeah, I reme-{nw}"

        ce "I wanted something a bit more avant garde, but we can’t win them\
        all right?"

        ce "We were able to settle on a really cool design."

        ce "We even made it onto an art zine."

        j "{i}Man, does this woman ever stop talking?{\i}"

        j "Wow, that's..."

        j "impressive."

        # Celia Proud/Smug expression

        ce "Mhmm.{w} But everyone graduated last year, so that was kind of like\
        our magnum opus."

        ce "My hope is that we can recruit enough new members to go out on an\
        even bigger bang this year!"

        ce "Oh, I'm a senior by the way, you?"

        j "Same. My name is James, in class 2-B."

        # Celia Suprised/Shocked expression

        ce "Ay Dios Mio!{w} I forgot to introduce myself!{p} I’m Celia, in\
        class 3-A, a pleasure to meet you."

        j "Nice to meet you too."

        ce "Oh! Looks like we’re here!"

        ce "Hey, so I gotta go set up, but drop by and sign up for the Art club\
        ok?"

        j "Well, I wasn’t really planning on--{nw}"

        ce "Alright then, see you later!"

        $ celia_points_love += 1

        #Celia exits

        j "{i}Damn it...how did I wind up here after all?{\i}"

    return #jump club_selection
