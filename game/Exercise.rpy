label parkrun:
    scene bg woods at Pan((700, 0), (1000,0), 2.0, repeat=True, bounce=True, time_warp=None) with fade
    pov "Phew, that was fun, but tiring!"
    jump lounge
    
label tomrun:
    $ reply_screen = False
    hide screen mailbox
    hide screen mailbox_overlay
    show bg woods with dissolve
    
    if male:
        t "Hey buddy! Ready for a run?"
        pov "You bet!"
    if female:
        t "Hey chica! Ready for a run?"
        pov "You bet!"
    if othergender: 
        t "Hey there! Ready for a run?"
        pov "You bet!"
    $ tomexercised = True
    t "How's it going? What's this about a new direction?"
    pov "Yeah, pretty good."
    t "You should get a partner [povname], it would do you good. Help keep you on the right track."
    pov "Ha, I don't know..."
    t "Why not?"
menu:
    
    "Not my style Tom. I don't need anyone clinging to me right now.":
        $ autonomy += 10
        $ tomloveignored = True
        pass
    "Maybe someday, who knows? If it happens it happens.":
        $ agency -= 5
        $ add_later("Looking for love?", "Tom", "Hey, you should check out KOEros.com ;) \nGreat place to meet nice people!", "tomlove_reply")   
        $ tomloveignored = True
        pass
    "Y'know, actually, it would be nice to have someone I can lean on.":
        $ add_later("Looking for love?", "Tom", "Hey, you should check out WhatUpEros ;) \nGreat place to meet nice people!", "tomlove_reply")   
        $ tomloveignored = True
        $ autonomy -= 10
        pass
        
label tomend:
    t "Ok, cool."
    t "Anyhow, here we are. Don't be a stranger eh?"
    t "Catch you again soon!"
    $ add_now
    jump freewheel