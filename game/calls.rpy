label calls:
    
label callmattdippl:
    scene bg desktopblank
    play sound "sfx/dialtone.wav"
    pause(1)
    matt "Hey [povname], how's it going?" with dissolve
    pov "Not bad at all Matt!"
    matt "Cool."
    hide matt with dissolve
    $ renpy.transition(dissolve)  
    jump closecodex
    
label callvictoriadavies:
    scene bg desktopblank
    play sound "sfx/dialtone.wav"
    pause(1)
    victoria "Hello [povname], how's it going?" with dissolve
    pov "Not bad at all Victoria!"
    victoria "Aces."
    hide victoria with dissolve
#    call ShowMenu('codex', transition=dissolve)
    $ renpy.transition(dissolve)  
    jump closecodex