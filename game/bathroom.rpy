label bathroom:
    scene bg bathroom with dissolve
    $ location = "bathroom"
    $ renpy.block_rollback()
    $renpy.transition(dissolve)
    call screen lookaroundbathroom
    show heart:
        crop (0, 0, 64, 128)
        ease 3.0 crop (64, 0, 64, 128)
    
screen lookaroundbathroom: 
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 800
        ypos 230
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("mirror")
        hovered Show("displayTextScreen", displayText = "Look in Mirror") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 800
        ypos 400
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("brushteeth")
        hovered Show("displayTextScreen", displayText = "Brush your teeth") 
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
        xpos 1080
        ypos 500
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("shower")
        hovered Show("displayTextScreen", displayText = "Take a shower") 
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
        
label shower:
    pov "Ahhh, fresh and clean!"
if female or othergender:
    $ myClock.add_time(0,15)
    $ hygiene = 100
else:
    $ myClock.add_time(0,10)
    $ hygiene = 100
    jump bathroom
    
label mirror:
    if hygiene <= 50:
        pov "Ugh, I really need to bathe."
        jump bathroom
    elif hygiene <= 80:
        pov "Maybe I should take a shower."
        jump bathroom
    elif calories >= 30000: 
        pov "*cries* I'm morbidly obese!"
        jump bathroom
    elif calories >= 25000:
        pov "I'm really fat :("
        jump bathroom
    elif calories >= 22000:
        pov "I'm starting to put on weight"
        jump bathroom
    elif calories >= 18001:
        pov "I'm about perfect in weight."
        jump bathroom
    elif calories >= 16001, 18000:
        pov "Looking a little skinny."
        jump bathroom
    elif calories >= 14001, 16001:
        pov "I'm super bony :("
        jump bathroom
    elif calories <= 14000:
        pov "I'm wasting away!"
        jump bathroom
    else:
        pass
    jump bathroom
    
label brushteeth:
    play sound "sfx/brushteeth.ogg"
    $ dentalhygiene += 50
    $ myClock.add_time(0,02)
    jump bathroom