label cheapgym:
if hasbike:    
    $ myClock.add_time(0,15)
else:
    $ myClock.add_time(0,45)
    scene bg stockvaultfitnesscenter with dissolve
    $ location = "cheapgym"
    $ renpy.block_rollback()
    cheapgymass "Welcome to FitForFun."
if cheapgymmember:
    jump cheapgym2 
else:
    cheapgymass "Would you like to join? It's [povcurrency]30 per month."
menu:
    "Ok":
        $ money -= 30 
        $ myClock.add_time(0,5)
        $ cheapgymmember = True
        cheapgymass "Great! You're now a member."
        jump cheapgym2
    "No thanks":
        cheapgymass "Ok, maybe another time."
        jump townmap

label cheapgym2:
    cheapgymass "Go right ahead and use the machines."
label cheapgym3:
menu:
    "Running":
        $ myClock.add_time(0,20)
        $ energy -= 10
        $ exerciselevel += 10
        $ calories -= 50
        pov "Phew!"
        jump cheapgym3
    "Weights":
        $ myClock.add_time(0,20)
        $ energy -= 10
        $ exerciselevel += 5
        $ bodystrength += 5
        $ calories -= 25
        pov "*Grunt*"
        jump cheapgym3
    "Enough for today":
        jump townmap



label fancygym:
if hasbike:    
    $ myClock.add_time(0,5)
else:
    $ myClock.add_time(0,15)
    scene bg gym with dissolve
    $ location = "fancygym"
    $ renpy.block_rollback()
    fancygymass "Welcome to FL Fitness"
if fancygymmember:
    jump fancygym2 
else:
        fancygymass "Would you like to join? It's [povcurrency]80 per month."
menu:
    "Ok":
        $ money -= 80
        $ myClock.add_time(0,5)
        $ fancygymmember = True
        fancygymass "Great! You're now a member."
        jump fancygym2
    "No thanks":
        fancygymass "Ok, maybe another time."
        jump townmap

label fancygym2:
    cheapgymass "Go right ahead and use the machines."
label fancygym3:
menu:
    "Running":
        $ myClock.add_time(0,20)
        $ energy -= 10
        $ exerciselevel += 10
        $ calories -= 50
        pov "Phew!"
        jump fancygym3
    "Weights":
        $ myClock.add_time(0,20)
        $ energy -= 10
        $ exerciselevel += 5
        $ bodystrength += 5
        $ calories -= 25
        pov "*Grunt*"
        jump fancygym3
    "Cross-trainer":
        $ myClock.add_time(0,20)
        $ energy -= 20
        $ exerciselevel += 15
        $ bodystrength += 2
        $ calories -= 150
        pov "*Gasp*"
        jump fancygym3
    "Enough for today":
        jump townmap

label bikeride:

menu:
    "Round-the-block tour":
        pov "Wheeeeee!"
        $ energy -= 10
        $ exerciselevel += 10
        $ calories -= 50
        $ myClock.add_time(0,20)
        jump townmap
    "Explore the surroundings":
        pov "Wheeeeee!"
        $ energy -= 10
        $ exerciselevel += 10
        $ povmood += 5
        $ calories -= 200
        $ myClock.add_time(1,00)
        jump townmap