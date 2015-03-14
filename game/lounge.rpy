label lounge:
    scene bg lounge with dissolve
    $ location = "lounge"
    $ renpy.block_rollback()
    $renpy.transition(dissolve)
    call screen lookaroundlounge


screen lookaroundlounge: 
    on "hide" action Hide("displayTextScreen")

    imagebutton:
        xpos 375
        ypos 450
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("bathroom")
        hovered Show("displayTextScreen", displayText = "Bathroom") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 775
        ypos 400
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("freewheel")
        hovered Show("displayTextScreen", displayText = "Bedroom Office") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 525
        ypos 450
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("kitchen")
        hovered Show("displayTextScreen", displayText = "Kitchen") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("townmapzip")
        hovered Show("displayTextScreen", displayText = "Go Outside") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 1150
        ypos 240
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("lookoutwindow")
        hovered Show("displayTextScreen", displayText = "Look out Window") 
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