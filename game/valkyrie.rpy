label valkyrie:
    scene bg valkyrie with dissolve
menu:
    "Bike" if hasbike == False:
        jump buybike
    "Get Quanta" if hasquanta == False:
        jump getquanta
        
    "Never mind":
        jump desktop
        
label buybike:
    "A 3-gear bike, a great little run-about."
    "A steal at only [povcurrency]400!"
    
menu:
     "Buy it":
        $ money -= 400
        if not persistent.quantaachieve:
            show achieve1 at achieveanim with hpunch
            show text"{color=#F00}{size=28}Quanta Unlocked!{/size}{/color}"  at achieveanimtext
        $ persistent.quantaachieve = True
        play sound "sfx/unlocked.ogg"
        "Congratulations on your purchase!"
        "The bike will be shipped to you super high priority."
        $ hasbike = True
        jump valkyrie
     
     "No":
         jump valkyrie
         
label getquanta:
    "Easily watch how your body changes over time just using a webcam."
    "Just [povcurrency]10 per month!"
menu:
     "Subscribe":
        $ money -= 10
        play sound "sfx/unlocked.ogg"
        "Congratulations on your purchase!"
        "Use the app any time from the desktop."
        $ hasquanta = True
        jump valkyrie
     
     "No":
         jump valkyrie