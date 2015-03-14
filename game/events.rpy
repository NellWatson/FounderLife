##############################################################################
# Events
#
# This file is used to store all the events triggered as you play through the
# game. Events can be triggered by a choice made by the player or by stats.

##SCHOOL EVENTS
label Art_evt:

    if CRE >= 100:
    
        "You are the god of art!"
        $ CRE += 5
        $ PSY += 5
        $ Money -= 5
        $ Stress += 1

    elif CRE >= 50:
    
        "You are the best in your class!"
        $ CRE += 5
        $ PSY += 3
        $ Money -= 3
        $ Stress += 1

    elif CRE >= 20:
    
        "You are getting pretty good at this."
        $ CRE += 3
        $ PSY += 2
        $ Money -= 2
        $ Stress += 1

    elif CRE >= 5:
        "You are starting to learn the basic concepts."
        $ CRE += 2
        $ PSY += 1
        $ Money -= 2
        $ Stress += 1

    else:
        "You have a hard time drawing and when class is over you aren't satisfied with your results."
        $ CRE += 1
        $ Money -= 1
        $ Stress += 1

return


label Fencing_evt:

    if AGI >= 100:
    
        "You are the god of blood!"
        $ AGI += 5
        $ FIT += 5
        $ Money -= 5
        $ Stress += 1

    elif AGI >= 50:
    
        "You are the undisputed leader of the alleys!"
        $ AGI += 5
        $ FIT += 3
        $ Money -= 3
        $ Stress += 1

    elif AGI >= 20:
    
        "You are getting pretty good at this."
        $ AGI += 3
        $ FIT += 2
        $ Money -= 2
        $ Stress += 1

    elif AGI >= 5:
        "You can now hold onto your stick. Still can't hit much with it."
        $ AGI += 2
        $ FIT += 1
        $ Money -= 1
        $ Stress += 1

    else:
        "You have a hard time keeping a hold of your stick. More often than not you get the tar beat out of you."
        $ AGI += 1
        $ Money -= 1
        $ Stress += 1

return


label Math_evt:

    if KNO >= 100:
    
        "You are the god of math!"
        $ KNO += 5
        $ WIL += 5
        $ Money -= 5
        $ Stress += 1

    elif KNO >= 50:
    
        "You are the best in your class!"
        $ KNO += 5
        $ WIL += 3
        $ Money -= 3
        $ Stress += 1

    elif KNO >= 20:
    
        "You can complete your workbook without having to ask for help."
        $ KNO += 3
        $ WIL += 2
        $ Money -= 2
        $ Stress += 1

    elif KNO >= 5:
        "After some thinking, the basic problems are starting to make sense."
        $ KNO += 1
        $ WIL += 1
        $ Money -= 1
        $ Stress += 1

    else:
        "You try to concentrate on the math problems, but keep getting distracted."
        $ KNO += 1
        $ Money -= 1
        $ Stress += 1

return


label Alchemy_evt:

    if KNO >= 100:
    
        "You are the god of transformation!"
        $ KNO += 5
        $ INF += 5
        $ Money -= 5
        $ Stress += 1

    elif KNO >= 50:
    
        "You are the best in your class!"
        $ KNO += 5
        $ INF += 3
        $ Money -= 3
        $ Stress += 1

    elif KNO >= 20:
    
        "You are now able to transmute some more complex materials."
        $ KNO += 3
        $ INF += 2
        $ Money -= 2
        $ Stress += 1

    elif KNO >= 5:
        "You can now transmute some basic materials."
        $ KNO += 2
        $ INF += 1
        $ Money -= 1
        $ Stress += 1

    else:
        "Somehow, the idea of equivalent exchange is lost on you. Everything keeps turning into greyish goop."
        $ KNO += 1
        $ Money -= 1
        $ Stress += 1

return


##WORK EVENTS
label Church_evt:

    if INF >= 100:
    
        "You are accepted as a god! The church is now dedicated to worshipping you."
        $ INF += 5
        $ PSY += 5
        $ Stress += 1

    elif INF >= 50:
    
        "Everyone in church loves you!"
        $ INF += 5
        $ PSY += 3
        $ Stress += 1

    elif INF >= 20:
    
        "You are actually a bit useful."
        $ INF += 3
        $ PSY += 2
        $ Stress += 1

    elif INF >= 5:
        "You manage to not disrupt mass."
        $ INF += 2
        $ PSY += 1
        $ Stress += 1

    else:
        "You go to work at the church. You insult the gods at the alter and get sent home early."
        $ INF += 1
        $ Stress += 1

return


label Farm_evt:

    if FIT >= 100:
    
        "You are the god of farmville-- I mean farming!"
        $ FIT += 5
        $ BLD += 5
        $ Money += 5
        $ Stress += 1

    elif FIT >= 50:
    
        "You are quite handy and the animals love you!"
        $ FIT += 5
        $ BLD += 3
        $ Money += 3
        $ Stress += 1

    elif FIT >= 20:
    
        "Farm life is growing on you."
        $ FIT += 3
        $ BLD += 2
        $ Money += 2
        $ Stress += 1

    elif FIT >= 5:
        "You can stay the whole day, but you're exhausted."
        $ FIT += 2
        $ BLD += 1
        $ Money += 1
        $ Stress += 1

    else:
        "Unused to the hard work, you have to go home early."
        $ FIT += 1
        $ Money += 1
        $ Stress += 1

return


label Store_evt:

    if PER >= 100:
    
        "You are the god of groceries!"
        $ PER += 5
        $ INF += 5
        $ Money += 5
        $ Stress += 1

    elif PER >= 50:
    
        "You win employee of the month!"
        $ PER += 5
        $ INF += 3
        $ Money += 3
        $ Stress += 1

    elif PER >= 20:
    
        "You are moderately competent and no longer require supervision."
        $ PER += 3
        $ INF += 2
        $ Money += 2
        $ Stress += 1

    elif PER >= 5:
        "You are now able to watch for theives and count back change."
        $ PER += 2
        $ INF += 1
        $ Money += 1
        $ Stress += 1

    else:
        "You suck at paying attention and someone steals your wares. It's docked from your pay."
        $ PER += 1
        $ Money += 1
        $ Stress += 1

return


label Chores_evt:

    if WIL >= 100:
    
        "You are the god of butlers!"
        $ WIL += 5
        $ FIT += 5
        $ Money += 5
        $ Stress += 1

    elif WIL >= 50:
    
        "Your house is spotless!"
        $ WIL += 5
        $ FIT += 3
        $ Money += 3
        $ Stress += 1

    elif WIL >= 20:
    
        "You make a rotating schedule of chorse and actually stick to it."
        $ WIL += 3
        $ FIT += 2
        $ Money += 2
        $ Stress += 1

    elif WIL >= 5:
        "You are able to keep the floor mostly clear."
        $ WIL += 2
        $ FIT += 1
        $ Money += 1
        $ Stress += 1

    else:
        "You are unable to keep yourself on task and get nothing done."
        $ WIL += 1
        $ Money += 1
        $ Stress += 1

return


##TRAVEL EVENTS
label North_evt:

    "It is cold in the north."

return


label East_evt:

    "You watch the sunrise."

return


label South_evt:

    "It's hot in the south."

return


label West_evt:

    "You watch the sunset."

return

##REST EVENTS
label Home_evt:

    "Resting at home is relaxing."
    $ Stress -= 2

return


label Library_evt:

    "If only the library rented apartments."
    $ Stress -= 1
    $ KNO += 1

return


label Vacation_evt:

    "You spent too much, but it was worth it."
    $ Stress -= 5
    $ Money -= 5

return


label Hospital_evt:

    "Your life is no longer in danger"
    $ Stress -= 1

return

##CALENDAR EVENTS

label Harvest_Festival:
    
    "It's the harvest festival!"
    
##TRIGGERED EVENTS
    
    return