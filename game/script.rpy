# Chapter 1.
label start:

    scene loc-sch-ext

    j "The final year of high school starts today, my last chance at a lot of\n
    things. I feel like the best years of my life were wasted."

    j "I got good grades, teachers are quick to heap me with praise and\n
    offers of college recommendation letters, which is cool I guess, but I’ve\n
    never reached that one milestone, the right of passage for everyone on\n
    the cusp of adulthood. I never had a girlfriend."

    j "I mean, there’s been a girl I’ve liked, since forever, basically, but\n
    I've never had the guts to tell her. It never works out with friends, you\n
    either confess and ruin the friendship, or try to stay friends but slowly\n
    yet inevitably drift apart."

    show chr-emily-smile

    e "Oh! Good morning James!"

    j "{i}Shit! It's Emily! When I said I would shoot my shot this year, I\n
    didn’t mean right this moment!{/i}"

    j "Morning Emily, what’s up?"

    e "Oh you know, same old, same old. Were you planning on joining any clubs?"

    menu choice0:
        "Yeah... Clubs... Was just thinking about them.\n
        Which are you in, again?":
            jump route0
        "What? No. The less time I spend in school, the better.":
            jump route0
        "Yeah, actually; I had one in mind."
            jump route0

label route0:
    
    e "You completely forgot about the festival didn’t you? *giggles* that is\n
    so you. Anyway, I'm on the student committee, we oversee all the club\n
    activities. We’re holding a club fair after school. You should drop by."

    menu choice1:
        "Remind me. What’s this festival about?":
            jump route0a
        "Sounds like fun! You’ll be there, right?":
            jump route0a
        "After school? Yeah... No... I have plans. Doing other stuff, that’s\n
        not in school."
            jump route0a
        
label route0a:

    e "You know that big field and empty lot behind the school? It used to be\n
    a community market. People would come to sell their art, vendors would\n
    sell food, there were musicians, and even a farmers market."
    
return
