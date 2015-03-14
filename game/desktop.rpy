label desktop:
    scene bg desktopblank
    call screen desktopselect
    hide screen calendar
    hide screen clock_screen 
    with dissolve
#    $ renpy.transition(dissolve)  
#    call screen desktopselect

screen desktopselect:     
    
    add "desktopblank.jpg"
    
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 1050
        ypos 350
        xanchor 0.5
        yanchor 0.5
        idle "mail_web.png"
        hover "mail_web.png"
        action Show("mailbox")
        hovered Show("displayTextScreen", displayText = "Mailbox ([new_messages] New)") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 145
        ypos 350
        xanchor 0.5
        yanchor 0.5
        idle "game_folder.png"
        hover "game_folder.png"
        action Jump("games")
        hovered Show("displayTextScreen", displayText = "Games") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 1240
        ypos 210
        xanchor 0.5
        yanchor 0.5
        idle "ui/tell_a_friend.png"
        hover "ui/tell_a_friend.png"
        action Jump("feedback")
        hovered Show("displayTextScreen", displayText = "Write Feedback") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 850
        ypos 120
        xanchor 0.5
        yanchor 0.5
        idle "shopping_cart.png"
        hover "shopping_cart.png"
        action Jump("valkyrie")
        hovered Show("displayTextScreen", displayText = "Valkyrie") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 258
        ypos 133
        xanchor 0.5
        yanchor 0.5
        idle "wiki2.png"
        hover "wiki2.png"
        action ShowMenu("encyclopaedia_list")
        hovered Show("displayTextScreen", displayText = "FounderPedia") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("desktopexit")
        hovered Show("displayTextScreen", displayText = "Sleep") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 860
        ypos 545
        xanchor 0.5
        yanchor 0.5
        idle "audio_x_generic.png"
        hover "audio_x_generic.png"
        action Show('musicroom')
        hovered Show("displayTextScreen", displayText = "Music") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 575
        ypos 85
        xanchor 0.5
        yanchor 0.5
        idle "checkout.png"
        hover "checkout.png"
        action Jump("desktopexit")
        hovered Show("displayTextScreen", displayText = "Finances") at Position(xpos = 400, ypos=300)
        unhovered Hide("displayTextScreen") 
  
    imagebutton:
        xpos 1075
        ypos 545
        xanchor 0.5
        yanchor 0.5
        idle "ui/event_viewer.png"
        hover "ui/event_viewer.png"
        action Jump("meetupschedule")
        hovered Show("displayTextScreen", displayText = "Events")
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 375
        ypos 545
        xanchor 0.5
        yanchor 0.5
        idle "ui/holiday_diary.png"
        hover "ui/holiday_diary.png"
        action Jump("diary")
        hovered Show("displayTextScreen", displayText = "Journal")
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 175
        ypos 585
        xanchor 0.5
        yanchor 0.5
        idle "ui/contacts.png"
        hover "ui/contacts.png"
        action Jump("opencodex")
        hovered Show("displayTextScreen", displayText = "Contacts")
        unhovered Hide("displayTextScreen") 
  
    if hasprocrastibook:
        imagebutton:
            xpos 325
            ypos 505
            xanchor 0.5
            yanchor 0.5
            idle "generic.png"
            hover "generic.png"
            action Jump("freewheel")
            hovered Show("displayTextScreen", displayText = "Procrastibook") 
            unhovered Hide("displayTextScreen")   

    if hasquanta:
        imagebutton:
            xpos 1055
            ypos 545
            xanchor 0.5
            yanchor 0.5
            idle "quantalogotrans.png"
            hover "quantalogotrans.png"
            action Jump("freewheel")
            hovered Show("displayTextScreen", displayText = "Quanta") 
            unhovered Hide("displayTextScreen") 

    if whatuperosunlocked:
        imagebutton:
            xpos 505
            ypos 545
            xanchor 0.5
            yanchor 0.5
            idle "heart.png"
            hover "heart.png"
            action Jump("freewheel")
            hovered Show("displayTextScreen", displayText = "WhatUpEros") 
            unhovered Hide("displayTextScreen") 
            
        
label desktopexit:
    
    if location == "bedroom":
        hide nell
        hide screen desktopselect
        jump freewheel
    elif location == "lounge":
        hide nell
        hide screen desktopselect
        jump lounge
    elif location == "kitchen": 
        hide nell
        hide screen desktopselect
        jump kitchen
    elif location == "bathroom":
        hide nell
        hide screen desktopselect
        jump bathroom
    elif location == "lookoutwindow":
        hide nell
        hide screen desktopselect
        jump lookoutwindow
    elif location == "townmap":
        hide nell
        hide screen desktopselect
        jump townmap
    elif location == "cheapgym":
        hide nell
        hide screen desktopselect
        jump cheapgym
    elif location == "fancygym":
        hide nell
        hide screen desktopselect
        jump fancygym
    elif location == "office":
        hide nell
        hide screen desktopselect
        jump office2
    elif location == "desk":
        hide nell
        hide screen desktopselect
        jump desk
    else:
        hide nell
        hide screen desktopselect
        jump freewheel