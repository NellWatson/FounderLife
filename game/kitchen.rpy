label kitchen:
    scene bg kitchen with dissolve
    $ location = "kitchen"
    $ renpy.block_rollback()
    $renpy.transition(dissolve)
    call screen lookaroundkitchen

screen lookaroundkitchen: 
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 525
        ypos 420
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("fridge")
        hovered Show("displayTextScreen", displayText = "Look in Fridge") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("lounge")
        hovered Show("displayTextScreen", displayText = "Lounge") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 1200
        ypos 50
        xanchor 0.5
        yanchor 0.5
        idle "ui/empty.png"
        hover "ui/pda.png"
        insensitive "ui/empty.png"
        #action
        action Jump("desktop")
        hovered Show("displayTextScreen", displayText = "PDA") 
        unhovered Hide("displayTextScreen")
        
    imagebutton:
        xpos 1200
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/empty.png"
        hover "happy nell small.png"
        insensitive "ui/empty.png"
        #action
        action Jump("nelltip")
        hovered Show("displayTextScreen", displayText = "Nell") 
        unhovered Hide("displayTextScreen")
        
        
label fridge:
    scene bg fridge with dissolve
#    if minutes <= 600:
#        "Time for breakfast"
    if groceries == 1:
        "You have groceries sufficient for [groceries] home-cooked meal."
    elif groceries >= 1: 
        "You have groceries sufficient for [groceries] home-cooked meals."
    if readymeals == 1:
        "You have [readymeals] readymeal."
    elif readymeals >= 1:
        "You have [readymeals] readymeals."
    if snacks == 1:
        "You have [snacks] snack."
    elif snacks >= 1:
        "You have [snacks] snacks."
    if satiety >= 90:
        "You're full."
    elif satiety >= 70:
        "You could go for a snack."    
    elif satiety >= 31:
        "You're ready for a meal."
    elif satiety <= 30:
        "You're really hungry."
menu:
        "Cook breakfast" if myClock.minutes <= 660 and groceries >= 1:
            $ satiety += 30
            $ energy += 20
            $ health += 4
            $ calories += 500
            $ povmood += 10
            $ groceries -= 1
            $ myClock.add_time(0,15)
            $ breakfasttype = renpy.random.choice([
            "Waffles",
            "A fry-up",
            "A bowl of oatmeal",
            "A grapefruit",
            ])    
            if breakfasttype == "Waffles":          
                play sound "sfx/fryingpansizzle.ogg" 
            elif breakfasttype == "A fry-up":
                play sound "sfx/fryingpansizzle.ogg" 
            pov "%(breakfasttype)s for breakfast this morning."
            jump kitchen
            
        "Cook lunch" if myClock.minutes ==(661, 840) and groceries >= 1:
            $ satiety += 20
            $ energy += 10
            $ health += 4
            $ calories += 500
            $ povmood += 5
            $ groceries -= 1
            $ myClock.add_time(0,20)
            $ lunchtype = renpy.random.choice([
            "A baked potato",
            "A tuna sandwich",
            "A salad",
            ])    
            pov "%(lunchtype)s for lunch today."
            jump kitchen
    
        "Cook dinner" if myClock.minutes >= 1020 and groceries >= 1:
            play sound "sfx/cookingfood.ogg"
            $ satiety += 30
            $ energy += 20
            $ health += 4
            $ calories += 1000
            $ povmood += 10
            $ groceries -= 1
            $ myClock.add_time(0,30)
            $ dinnertype = renpy.random.choice([
            "Chilli",
            "Pasta",
            "Spaghetti Bolognese",
            "Fish & Potatoes",
            "Stew",
            "Stir fry",
            "Tandoori Curry",
            ])    
            pov "%(dinnertype)s for dinner tonight."
            jump kitchen

        "Cook a readymeal" if readymeals >= 1:
            $ satiety += 20
            $ energy += 20
            $ health += 2
            $ povmood += 15
            $ calories += 1000
            $ readymeals -= 1
            $ myClock.add_time(0,10)
            jump kitchen
        "Grab a snack" if snacks >= 1:
            play sound "sfx/sodacan.ogg"
            $ satiety += 10
            $ energy += 5
            $ health += 1
            $ calories += 500
            $ povmood += 5
            $ readymeals -= 1
            $ myClock.add_time(0,5)
            jump kitchen
        "Back to kichen":
            jump kitchen
    