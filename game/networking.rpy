label networkfunction:
if hasbike:    
    $ myClock.add_time(0,10)
else:
    $ myClock.add_time(0,30)
    
label network:
    
#    call initialize_room_screen
    scene bg meetup with dissolve
    if myClock.minutes == (1050, 1100):
        $ meetupontime = True
    else:
        pass

    if meetupontime:
        pov "Looks like a good crowd."
        pass
    else:
        pov "Hmm, no-one's here."
        jump townmap

#    show char at center with easeinright
    call show_room_screen


label room_common_action_look:
    $ temp_room_description = places[current_room]['description']
    "%(temp_room_description)s"
    show screen calendar
    show screen clock_screen
    show show_room_screen

label person_placeholder_talk:
    show char at right with ease
    show anon at midleft with easeinleft
    
    pov "Hello, how are you doing today?"
    anon "Okay, how about you?"
    pov "Same."
    
    hide anon with easeoutleft
    show char at center with ease
    jump show_room_screen

#menu:
#    "Network":
#        jump meetnewcontact
#    "Leave":
#        jump townmap
#label meetnewcontact:
#    $ myClock.add_time(0,10)
#    $ i = 2
#label meetnewcontact2:
#    $ contact_list = [
#    "Piyush Aggarwal",
#    "Matt Dippl",
#    "Tanausú Cerdeña Hernández",
#    "Marc Winn",
#    "Ilse Gayl",
#    "Victoria Davies",
#    "Tiffany Hart",
#    "Anish Mohammed",
#    "Pablo Valcárcel"
#    ]
#    $ contact_to_show = renpy.random.choice(contact_list)
#    "Piyush Aggarwal, Health & Hardware expert"
#    "Matt Dippl, Bio-Hacking expert"
#    "Tanausú Cerdeña Hernández, Founder& Developer"
#    "Marc Winn, Founder & mentor"
#    "Ilse Gayl, Founder"
#    "Victoria Davies, Musician"
#    "Tiffany Hart", Founder
#    "Anish Mohammed, Cryptography & Health Expert"
#    "Pablo Valcárcel, Founder, Gaming Expert,"

                                                  
                                                  
#if contact_to_show in cards:
#    pov "I saw [contact_to_show] again."
#    jump network
#else:
#    pov "I met someone new: [contact_to_show]."
##    $ contact_list.remove(contact_to_show)
#    $ cards.append(contact_to_show)
    jump network

