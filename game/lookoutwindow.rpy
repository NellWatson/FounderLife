label lookoutwindow:
if location == "lookoutwindow":
    show movie
    play movie "street_day_animated.ogv" loop
    jump lookoutwindow2
else:
    show movie
    play movie "street_day_animated.ogv" loop
    play sound "sfx/openwindow.ogg"
    $ location = "lookoutwindow"
    $ renpy.block_rollback()
    $renpy.transition(dissolve)
    pass
#    call show_room_screen


    if weather == "snowing":
        show overcast
        show snowstorm
        pov "It's snowing today." with dissolve
    elif weather == "rainy":
        show overcast
        show rain
        pause(0.7)
        $renpy.sound.play("sfx/rain.ogg", loop=True)
        pov "It's rainy today." with dissolve
    elif weather == "sunny":
        pov "It's sunny today." with dissolve
    elif weather == "overcast":
        show overcast 
        pov "It's overcast today." with dissolve
    $renpy.transition(dissolve)    
    call screen lookaroundwindow
#    call screen reflectoutwindow
    
    
    
screen lookaroundwindow: 
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("lookoutwindowhide")
        hovered Show("displayTextScreen", displayText = "Back") 
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
        action Jump("desktopjumpfromwindow")
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
        

label lookoutwindowhide:
    stop sound fadeout 1.0
    play sound "sfx/closewindow.ogg"
    hide snowstorm with dissolve
    hide rain with dissolve
    hide overcast with dissolve
    stop movie
    jump lounge
    
label lookoutwindow2:
    
    if weather == "snowing":
        show overcast
        show snowstorm
    elif weather == "rainy":
        show overcast
        show rain
    elif weather == "sunny":
        pass
    elif weather == "overcast":
        show overcast 
    $renpy.transition(dissolve)    
    call screen lookaroundwindow
    
label desktopjumpfromwindow:
    stop movie
    jump desktop
    