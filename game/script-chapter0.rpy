# Chapter 1.
label start:

    #show screen varz

    scene loc-sch-ext

    j "The final year of high school starts today, my last chance at a lot of\
    things. I feel like the best years of my life were wasted."

    j "I got good grades, teachers are quick to heap me with praise and\
    offers of college recommendation letters, Which is cool I guess; but I’ve\
    never reached that one milestone, the right of passage for everyone on the\
    cusp of adulthood..."

    j "I've never had a girlfriend."

    j "I mean, there’s been a girl I’ve liked, since forever, basically, but\
    I've never had the guts to tell her."

    j "It never works out with friends.{w} You either confess and ruin the\
    friendship, or try and stay friends but slowly yet inevitably drift apart."

    show chr-emily-smile at truecenter

    e "Oh! Good morning James!"

    j "{i}Shit! It's Emily! When I said I would shoot my shot this year, I\
    didn’t mean right this moment!{\i}"

    j "Morning, Emily. What’s up?"

    e "Oh, you know, same old, same old. Were you planning on joining any\
    clubs?"

    menu choice0:
        "Yeah... Clubs... Was just thinking about them.\
        Which are you in, again?":
            # Already set to route 0 so there is no need to change.
            jump route0

        "What? No. The less time I spend in school, the better.":
            $ chapter0_main_route = 1
            jump route1

        "Yeah, actually; I had one in mind.":
            $ chapter0_main_route = 2
            jump route2


label route0:

    show chr-emily-giggle at truecenter

    e "You completely forgot about the festival didn’t you? *giggles* that is
     so you."

    # Set Emily expression back to default.

    e "Anyway, I'm on the student committee, we oversee all the club\
    activities."

    e "We’re holding a club fair after school. You should drop by."

    menu choice1:
        "Remind me. What’s this festival about?":
            jump route0a
        "Sounds like fun! You’ll be there, right?":
            jump route0b
        "After school? Yeah... No... I have plans. Doing other stuff, that’s\
        not in school.":
            jump route0c

    label route0a:

        e "You know that big field and empty lot behind the school?
         It used to be a community market."

        e "People would come to sell their art, vendors would\
        sell food, there were musicians, and even a farmers' market."

        j "Really? It just looks like an abandoned lot."

        e "Well, yeah, now it is, but it wasn’t always."

        e "The city just got too\
        expensive and people who’ve been here for generations got displaced,\
        and the market kind of died out."

        j "Yeah, I heard about that. Gentrification or something right?"

        show chr-emily-smile at truecenter

        e "Yes! That’s exactly it!"

        show chr-emily-neut at truecenter

        e "And ever since the new train station got built,\
        the city wants to let some tech companies build offices and luxury\
        condos over the lot!"

        j "That's awful! ...Isn’t it?"

        e "It is, because even more people will be displaced and this\
        neighborhood will lose the last of its character and charm."

        e "The festival is our last chance to bring back a timeless tradition\
        and cornerstone of our community!"

        e "People used to come from across the city to the market for art,\
        music, and food."

        j "Sounds like a big deal."

        e "It totally is! {p}That’s why you’ll help out by joining a club,\
        right?"

        if chapter0_main_route == 0:

            jump choice1

        else:

            jump choice3

    label route0b:

        show chr-emily-smile at truecenter

        e "Great! I knew I could count on you! The fair is after last\
        bell in the student commons, okay?"

        j "Yeah, see you there."

        #play sound "sch-bell.wav"

        e "For sure, see you there!"

        $ points_love += 1

        jump chapter0_end

    label route0c:

        show chr-emily-annoy at truecenter

        e "Really? Like what?"

        menu choice2:
            "I like to go to the park and people watch.":
                jump route0c0
            "New episodes of Pokemon are airing, tonight. I’m not missing\
            that.":
                jump route0c1
            "I don’t know. Jerk off, maybe?":
                jump route0c2

        label route0c0:

            e "Really? I didn’t know that about you."

            e "Well, I hope you reconsider; we could use all the help we\
            can get for the festival."

            #play sound "sch-bell.wav"

            jump option1_c_end

        label route0c1:

            e "What are you, like 5? It's not like that show has changed in\
            the, what, 25 years its been on TV? I’m sure you can miss one\
            episode."

            $ points_love -= 1

            #play sound "sch-bell.wav"

            jump option1_c_end

        label route0c2:

            show chr-emily-disgust at truecenter

            $ chapter0_main_route -= 1

            e "You know what, forget I asked."

            #play sound "sch-bell.wav"

            jump option1_c_end

        label option1_c_end:

            e "Oh shoot, I’m going to be late."

            e "Anyway, the club fair is after last bell in the student commons."

            e "If you can break away from your oh so busy schedule, I hope you\
            can join us."

            jump chapter0_end


label route1:

    show chr-emily-disap at truecenter

    e "I mean, I guess I understand, {w}but this is for a good cause and I\
    promise it will be really fun."

    e "Will you reconsider?"

    menu choice3:
        "Remind me. What’s this festival about?":
            jump route0a
            # We use the same route0a since it is basically the same thing.

        "I’ll think about it.":
            jump route1b

        "Yeah, no.":
            jump route1c


    label route1b:

        show chr-emily-annoy at truecenter

        e "It's not a no I guess."

        show chr-emily-neut at truecenter

        e "Anyway, if you want to join us, the club fair is after last bell in\
        the student commons."

        #play sound "sch-bell.wav"

        jump chapter0_end


    label route1c:

        show chr-emily-annoy at truecenter

        e "No need to be an ass about it."

        e "Anyway, if you do decide to join us, the club fair is after last\
        bell in the student commons."

        $ points_love -= 1

        #play sound "sch-bell.wav"

        jump chapter0_end


label route2:

    show chr-emily-supr at truecenter

    e "Really? {w}That's great!"

    e "then you know the club fair is after last bell in the student commons,\
    right?"

    j "Yeah, I’ll be there."

    show chr-emily-smile at truecenter

    e "Great, I’ll see you there then!"

    #play sound "sch-bell.wav"

    jump chapter0_end


label chapter0_end:

    if points_love == 0:
        j "{i}That went... some way...{\i}"

    elif points_love >= 1:
        j "{i}That went... better than expected. I might actually stand a\
        chance!{\i}"

    else:
        j "{i}God, what the hell is wrong with me?{\i}"

return
