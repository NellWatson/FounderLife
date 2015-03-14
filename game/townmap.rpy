label townmapzip:
    play sound "sfx/zipper1.ogg"
label townmap:
    show screen calendar
    show screen clock_screen
    scene bg townmap with dissolve
    $ location = "townmap"
    $ renpy.block_rollback()
    $ renpy.transition(dissolve)
menu:
    "Co-Working Space":
        jump office
    "Exercise":
        jump exercisemenu
    "Meetup":
        jump networkfunction
    "Supermarket":
        jump supermarket
    "Back home":
        jump lounge
  
label exercisemenu:
menu: 
        "'I want to to ride my bicycle...'" if hasbike:
            jump bikeride
        "The fancy gym nearby":
            if hasbike:
                $ myClock.add_time(0,5)
                jump fancygym
            else:
                $ myClock.add_time(0,15)
                jump fancygym
        "The cheap gym on the other side of town":
            if hasbike:
                $ myClock.add_time(0,15)
                jump cheapgym
            else:
                $ myClock.add_time(0,45)
                jump cheapgym
        "Never mind.":
            jump townmap
        