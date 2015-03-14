label meetupschedule:
    
    scene bg desktopblank
    hide screen calendar
    hide screen clock_screen
    pov "Let's see when the next interesting meetup is."

label meetupschedule2:
    
menu:
    "Look for a tech meetup":
        call availablemeetupt
    "Look for a design meetup":
        call availablemeetupd
    "Look for a product meetup":
        call availablemeetupp
    "Look for a mentor meetup":
        call availablemeetupm
    "Look for a investor meetup":
        call availablemeetupi
    "Look for a startup meetup \(general\)":
        call availablemeetups
    "Never mind":
        jump desktop
    
label availablemeetupt:
    if not meetupdeniedt:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdeniedt = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail
        
label availablemeetupd:
    if not meetupdeniedd:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdeniedd = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail

label availablemeetupp:
    if not meetupdeniedp:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdeniedp = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail
            
label availablemeetupm:
    if not meetupdeniedm:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdeniedm = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail
            
label availablemeetupi:
    if not meetupdeniedi:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdeniedi = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail
            
label availablemeetups:
    if not meetupdenieds:
        $ meetupchance = renpy.random.randint (1, 3)
        if meetupchance <= 2:
            call meetuppass
        elif meetupchance == 1:
            $ meetupdenieds = "True"
            call meetupfail
    elif meetupscheduled:
        "Already scheduled a meetup for [meetuptimeset]"
        jump desktop
    else:
        call meetupfail
        
label meetuppass:
    call meetuptime
    
label meetuptime:
    $ meetuptimeset = renpy.random.choice (['18,00', '19,00', '20,00'])
    "There's a meetup tonight at [meetuptimeset]. Register to attend?"
menu:
    "Yes":
        #add to quest log
        $ meetupscheduled = "True"
#        $ log.assign("Scheduled Meetup")
        jump desktop
    "No":
        jump desktop
        
label meetupfail:
    "Nothing available."
    jump meetupschedule2
    
    
#    "$ lunchtype = renpy.random.choice([
#            "A baked potato",
#            "A tuna sandwich",
#            "A salad",
#            ]) 