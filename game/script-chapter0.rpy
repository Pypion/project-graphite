# Chapter 1.
label start:

    scene loc-sch-ext

    j "The final year of high school starts today, my last chance at a lot of\
    things. I feel like the best years of my life were wasted."

    j "I got good grades, teachers are quick to heap me with praise and\
    offers of college recommendation letters, which is cool I guess, but I’ve\
    never reached that one milestone, the right of passage for everyone on\
    the cusp of adulthood. I never had a girlfriend."

    j "I mean, there’s been a girl I’ve liked, since forever, basically, but\
    I've never had the guts to tell her. It never works out with friends, you\
    either confess and ruin the friendship, or try to stay friends but slowly\
    yet inevitably drift apart."

    show chr-emily-smile:
        xalign 0.0

    e "Oh! Good morning James!"

    j "{i}Shit! It's Emily! When I said I would shoot my shot this year, I\
    didn’t mean right this moment!{/i}"

    j "Morning, Emily. What’s up?"

    e "Oh, you know, same old, same old. Were you planning on joining any\
    clubs?"

    menu choice0:
        "Yeah... Clubs... Was just thinking about them.\
        Which are you in, again?":
            jump route0
        "What? No. The less time I spend in school, the better.":
            jump route0
        "Yeah, actually; I had one in mind.":
            jump route0

label route0:
    
    e "You completely forgot about the festival didn’t you? *giggles* that is\
    so you. Anyway, I'm on the student committee, we oversee all the club\
    activities. We’re holding a club fair after school. You should drop by."

#label choice1:
    
    menu choice1:
        "Remind me. What’s this festival about?":
            jump route0a
        "Sounds like fun! You’ll be there, right?":
            jump route0b
        "After school? Yeah... No... I have plans. Doing other stuff, that’s\
        not in school.":
            jump route0c
        
label route0a:

    e "You know that big field and empty lot behind the school? It used to be\
    a community market. People would come to sell their art, vendors would\
    sell food, there were musicians, and even a farmers market."

    j "Really? It just looks like an abandoned lot."

    e "Well, yeah, now it is, but it wasn’t always. The city just got too\
    expensive and people who’ve been here for generations got displaced, and\
    the market kind of died out."

    j "Yeah, I heard about that. Gentrification or something right?"

    show chr-emily-smilebig

    e "Yes! That’s exactly it! And ever since the new train station got built,\
    the city wants to let some tech companies build offices and luxury condos\
    over the lot!"

    j "That's awful! ...Isn’t it?"

    e "It is because even more people will be displaced and this neighborhood\
    will lose the last of its character and charm. The festival is our last\
    chance to bring back a timeless tradition and cornerstone of our community!\
    People used to come from across the city to the market for art, music,\
    and food."

    j "Sounds like a big deal."

    e "It totally is! That’s why you’ll help out by joining a club, right?"

    jump choice1

label route0b:
    
    e "Great! I knew I could count on you! The fair is after last bell in the\
    student commons, okay?"

    j "Yeah, see you there."

    #play sound "sch-bell.wav"

    e "For sure, see you there!"

    # Love points +1

    jump chapter0_end
        
label route0c:

    show chr-emily-annoyed

    e "Really? Like what?"

    menu choice2:
        "I like to go to the park and people watch.":
            jump route0c0
        "New episodes of Pokemon are airing, tonight. I’m not missing that.":
            jump route0c1
        "I don’t know. Jerk off, maybe?":
            jump route0c2

label route0c0:
    
    e "Really? I didn’t know that about you. Well, I hope you reconsider;\
    we could use all the help we can get for the festival."

    #play sound "sch-bell.wav"

    jump chapter0_end

label route0c1:
    
    e "What are you, like 5? It's not like that show has changed in the, what,\
    25 years its been on TV? I’m sure you can miss one episode."

    # Love points -1

    #play sound "sch-bell.wav"

    jump chapter0_end

label route0c2:

    show chr-emily-disgust

    e "You know what, forget I asked."

    #play sound "sch-bell.wav"

    e "Oh shoot, I’m going to be late. Anyway, the club fair is after last bell\
    in the student commons. If you can break away from your oh so busy\
    schedule, I hope you can join us."

    jump chapter0_end
    
label chapter0_end:
    
    # If love points = 0
    #j "That went... some way..."

    # If love points = 1
    #j "That went... better than expected. I might actually stand a chance!"

    # If love points = -1
    #j "God, what the hell is wrong with me?"
       
return
