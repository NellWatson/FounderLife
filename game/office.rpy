label office:
if hasbike:    
    $ myClock.add_time(0,10)
else:
    $ myClock.add_time(0,30)
    
    scene bg boardroom with dissolve
    show screen calendar
    show screen clock_screen
    $ location = "office"
    $ renpy.block_rollback()
    pov "Hmm, no-one else is here..."
    $renpy.transition(dissolve)
    call screen lookaroundoffice
    
label office2:
    scene bg boardroom with dissolve
    show screen calendar
    show screen clock_screen
    $renpy.transition(dissolve)
    call screen lookaroundoffice
    
    
label desk:
    scene bg desk with dissolve
    $ location = "desk"
    $ renpy.block_rollback()
if myClock.minutes >= 1080:
    pov "It's getting late."
    $renpy.transition(dissolve)
    call screen lookarounddesk
else:
    pass
    $renpy.transition(dissolve)
    call screen lookarounddesk

label work:
    $ myClock.add_time(0,30)
    call desk
    
    
label phone:
    pov "Who to call?"
menu:
    "Call Contact":
        jump calls
    "Never mind":
        jump desk
        
screen lookaroundoffice:
    on "hide" action Hide("displayTextScreen")

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
        
    imagebutton:
        xpos 700
        ypos 500
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("desk")
        hovered Show("displayTextScreen", displayText = "Take a seat") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("townmap")
        hovered Show("displayTextScreen", displayText = "Back") 
        unhovered Hide("displayTextScreen")
        
        
screen lookarounddesk:
    on "hide" action Hide("displayTextScreen")

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
        
    imagebutton:
        xpos 600
        ypos 350
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("work")
        hovered Show("displayTextScreen", displayText = "Work") 
        unhovered Hide("displayTextScreen") 

    imagebutton:
        xpos 320
        ypos 490
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("opencodex")
        hovered Show("displayTextScreen", displayText = "Contacts") 
        unhovered Hide("displayTextScreen") 

    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("office2")
        hovered Show("displayTextScreen", displayText = "Back") 
        unhovered Hide("displayTextScreen")
    