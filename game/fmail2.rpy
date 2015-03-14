label fmail2:
    show screen mailbox_overlay
    $ renpy.transition(dissolve)
    show screen mailbox
#    hide screen mailbox_overlay
    $ renpy.transition(dissolve)
    jump desktop
label slick_reply(current_message):
    menu:
        "I won't apologize, Slick. You are an overblown entitled blowhard!":
            $ add_later("Fine then!", "Slick McDouche", "THIS MEANS WAR")
            $ current_message.can_reply = False
        "You're right. I'm sorry, Slick.  Let's be friends.":
            $ add_later("<3", "Slick McDouche", "Okay! BFFs!")
            $ current_message.can_reply = False
        "Don't reply yet":
            pass
    return
    
label samlandingpage_reply(current_message):
    menu:
        "Thanks for your support, that's great.":
            $ current_message.can_reply = False
            $ samignored = False
        "Great to hear, thank you! Would you like to help beta test?":
            $ add_message("Re: Info?", "Sam", "Sure, let me know who I have to sleep with to get access! ;)", "samlandingpage_reply2")
            $ current_message.can_reply = False
        "Dont' reply yet":
            pass
    return
    
label samlandingpage_reply2(current_message):
    menu:
        "Here's an early version. Bit embarrassing. Needs more work":
            $ add_message("Re: Re: Info?", "Sam", "Never be embarrassed about your first release. Gonna have fun with this!")
            $ sambeta = True
            $ samignored = False
            $ current_message.can_reply = False
        "Don't reply yet":
            $ samignored = True
            pass
    return
    
label simon_reply(current_message):
    menu:
        "Ha, Ok, maybe one little game of BoerTown":
            $ hasprocrastibook = True
            play sound "sfx/unlocked.ogg"
            pause(2)
            $ add_message("Yeah!", "Simon", "That's my [povname]!")
            $ current_message.can_reply = False
            $ simonignored = False
        "Sorry Simon, I have like a... mission to complete":
            $ add_message("Whatever!", "Simon", "Jeeze. You used to be cool [povname].")
            $ simonignored = False
            $ current_message.can_reply = False
        "Don't reply yet":
            pass
    return
    
label tomexercise_reply(current_message):
    menu:
        "Sounds awesome!":
            $ tomignored = False
            $ add_later(":D", "Tom", "That was fun!!!")
            $ current_message.can_reply = False
            call tomrun
        "Not today, sorry.":
            $ add_message(":-/", "Tom", "Awww. \n\nk")
            $ current_message.can_reply = False
            $ tomignored = False
        "Don't reply yet.":
            pass
    return

label tomlove_reply(current_message):
    menu:
        "Haha, Ok, thanks, I will!":
            $ tomloveignored = False
            $ whatuperosunlocked = True
            play sound "sfx/unlocked.ogg"
            if not persistent.whatuperosachieve:
                show achieve1 at achieveanim with hpunch
                show text"{color=#F00}{size=28}WhatUpEros Unlocked!{/size}{/color}"  at achieveanimtext
            $ persistent.whatuperosachieve = True
            "Dating unlocked!"
            $ add_message("<3", "Tom", "Do it doit doit!!!")
            $ current_message.can_reply = False
            jump desktop
        "I'm not THAT desperate, Tom!":
            $ tomloveignored = False
            $ add_message(":-/", "Tom", "Desperate? Nahhh. You're missing out...")
            $ current_message.can_reply = False
        "Don't reply yet.":
            pass
    return

label ichifanideal:
$ add_later("Please tell more", "Ichifani Corporation", "Dear [povname],\n\nI read with interesting 'hearing voices'.\n\nGiving oneself commands sounds like an admittedly disturbing development.\n\nI'm sorry to say this, but you may have developed signs of schizophrenia. The  required...")