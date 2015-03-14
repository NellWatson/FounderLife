screen musicroom:


    frame:
        style_group "musicroom"
        xalign 1.0
        
        vbox:
            textbutton "Kevin Mcloud - Who Likes to Party - Main Title Theme" action mr.Play("music/wholikestoparty.mp3")
            textbutton "Kevin Mcloud - Rising Game - Intro" action mr.Play("music/risinggame.mp3")
            textbutton "Kevin Mcloud - Ether Disco" action mr.Play("music/etherdisco.mp3")
            textbutton "Kevin Mcloud - Stringed Disco" action mr.Play("music/stringeddisco.mp3")
            textbutton "Kevin Mcloud - Overcast" action mr.Play("music/overcast.mp3")
            textbutton "Kevin Mcloud - Disco con Tutti" action mr.Play("music/discocontutti.mp3")
            textbutton "Kevin Mcloud - Aurea Carmina" action mr.Play("music/aureacarmina.mp3")
            textbutton "Kevin Mcloud - Electrodoodle" action mr.Play("music/electrodoodle.mp3")
            textbutton "Kevin Mcloud - Presenterator" action mr.Play("music/presenterator.mp3")

            
            
            textbutton "Return" action [Hide("musicroom", transition=dissolve)]
            
init python:
    #This controls minimum button length
    style.musicroom = Style(style.frame)
    style.musicroom_button.xmaximum = 200
    style.musicroom_button.xminimum = 200
    style.musicroom_button.yminimum = 55


