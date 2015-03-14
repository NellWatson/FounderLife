##############################################################################
# Codex
#
# Screen that's used to display character and setting information.

label opencodex:

#    scene bg desktopblank
    hide screen calendar
    hide screen clock_screen
    hide screen menu2
    hide screen menu3
    hide screen codex1
    hide screen codex2
    hide screen codex3
    hide screen codex4
    call screen codex


screen codex:
    
    # Ensure this replaces the main menu.
    tag menu
    add "ui/desktopblank.jpg"
    
#    add "info.png"
    
    frame:
        style_group "codex"
        xalign 1.0
        
        hbox:
            textbutton "Founders" action Show("codex1")
            textbutton "Mentors" action Show("codex2")
            textbutton "Investors" action Show("codex3")
            textbutton "Clients" action Show("codex4")
            textbutton "Return" action Jump("closecodex")
            
init python:
    #This controls minimum button length
    style.codex = Style(style.frame)
    style.codex_button.xmaximum = 200
    style.codex_button.xminimum = 200
    style.codex_button.yminimum = 55
            

screen codex1:
    
    tag menu2
    
    frame:
        style_group "codex2"
        xalign 0
        yalign 0.187
        vbox:
            if persistent.entry1:
                text "Entry 1"
                text "Blah blah, here is your info.  Below is your image."
                add "image.png"
            else:
                textbutton "Piyush Aggarwal" action Show("Piyush_Aggarwal")
                textbutton "Matt Dippl" action Show("Matt_Dippl")
                textbutton "Tanausú Hernández" action Show("Tana_Hernandez")
                textbutton "Marc Winn" action Show("Marc_Winn")
                textbutton "Ilse Gayl" action Show("Ilse_Gayl")
                textbutton "Victoria Davies" action Show("Victoria_Davies")
                textbutton "Tiffany Hart" action Show("Tiffany_Hart")
                textbutton "Anish Mohammed" action Show("Anish_Mohammed")
                textbutton "Pablo Valcárcel" action Show("Pablo_Valcarcel")
            
            
init python:
    #This controls minimum button length
    style.codex2 = Style(style.frame)
    style.codex2_button.xmaximum = 250
    style.codex2_button.xminimum = 250
            
            
screen codex2:
    
    tag menu2
    
    frame:
        style_group "codex2"
        xalign 0
        yalign 0.1
        vbox:
            if persistent.entry1:
                text "Entry 1"
                text "Blah blah, here is your info.  Below is your image."
                add "image.png"
#            else:
#                textbutton "Rashieve Nyarlathotep" action Show("Rashieve_Nyarlathotep")
#                textbutton "Takeem Brhavo" action Show("Takeem_Brhavo")
            
screen codex3:
    
    tag menu2
    
    frame:
        style_group "codex2"
        xalign 0
        yalign 0.1
        vbox:
            if persistent.entry1:
                text "Entry 1"
                text "Blah blah, here is your info.  Below is your image."
                add "image.png"
#            else:
#                textbutton "War of 1919" action Show("War_of_1919")
#                textbutton "Massacre of Moscow       " action Show("Massacre_of_Moscow")
            
screen codex4:
    
    tag menu2
    
    frame:
        style_group "codex2"
        xalign 0
        yalign 0.1
        vbox:
            if persistent.entry1:
                text "Entry 1"
                text "Blah blah, here is your info.  Below is your image."
                add "image.png"
#            else:
#                textbutton "Pump Action Rifle        " action Show("Pump_Action_Rifle")
#                textbutton "Hovercraft" action Show("Hovercraft")



##############################################################################
# Personnel Profiles
#
# Screen that's used to display information on the 72nd Peacekeeper Regiment.

screen Piyush_Aggarwal:
    
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09)        
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Piyush Aggarwal{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Founder, Hacker"
            text "Specialisations: Hardware, Health"
            text "Alma Mater:"
        
            text "Piyush is awesome"



screen Matt_Dippl:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Matt Dippl{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Speaker, Blogger, Health Expert"
            text "Specialisations: Health, Nutrition, Evangelism"
            text "Alma Mater: University of Technology, Sydney"
            text "Honors: German National Kung Fu Champion 1996"
        
            text "\nMatt is awesome. And this line is for checking that \ntext wrapping is functional."
        
        imagebutton:
            xpos 1050
            ypos 20
            xanchor 1.0
            yanchor 0.1
            idle "characters/mattdippl.jpg"
            hover "characters/mattdippl.jpg"
            action Jump("callmattdippl")
            hovered Show("displayTextScreen", displayText = "Call Matt") 
            unhovered Hide("displayTextScreen")


screen Tana_Hernandez:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Tanausú Cerdeña Hernandez{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Founder, Coder"
            text "Specialisations: Coder, Gaming"
            text "Alma Mater: ???"
        
            text "\nTana is awesome."

screen Marc_Winn:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Marc Winn{/size}{/b}"
            text ""        
            text "Superpower: Inspiration"
            text "Occupation: Founder, Social Entrepreneur"
            text "Specialisations: ???"
            text "Alma Mater: University of Bath, University of Dead Time"
        
            text "\nMarc is awesome."


screen Ilse_Gayl:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Ilse Gayl{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Founder, Social Entrepreneur"
            text "Specialisations: ???"
            text "Alma Mater: ???"
        
            text "\nIlse is awesome."
        
screen Victoria_Davies:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Victoria Davies{/size}{/b}"
            text ""
            text "Superpower: Perception"
            text "Occupation: Founder, Musician"
            text "Specialisations: Music"
            text "Alma Mater: Oxford, Conservatorium van Amsterdam"
            text ""
            text "Victoria gained entrepreneurial experience over many years \nhustling as a musician."
            text ""
            text "She then transferred those abilities into a new venture that merges \nclassical music with modern technologies."
      
        imagebutton:
            xpos 1050
            ypos 20
            xanchor 1.0
            yanchor 0.1
            idle "characters/victoriadavies.jpg"
            hover "characters/victoriadavies.jpg"
            action Jump("callvictoriadavies")
            hovered Show("displayTextScreen", displayText = "Call Victoria") 
            unhovered Hide("displayTextScreen")      
      
      
screen Tiffany_Hart:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Tiffany Hart{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Founder"
            text "Specialisations: ???"
            text "Alma Mater: ???"
        
            text "\nTiffany is awesome."
        
screen Anish_Mohammed:
        
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Anish Mohammed{/size}{/b}"
            text ""        
            text "Superpower: Analysis"
            text "Occupation: Consultant"
            text "Specialisations: Security (Cryptography), Hardware, Health"
            text "Alma Mater: ???"
        
            text "\nAnish is unafraid to describe a situation exactly as he sees it."
        
screen Pablo_Valcarcel: 
      
    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            box_wrap True
            label "{b}{size=+12}Pablo Valcárcel{/size}{/b}"
            text ""        
            text "Superpower: ???"
            text "Occupation: Founder"
            text "Specialisations: Law, Gaming"
            text "Alma Mater: ???"
        
            text "\nPablo is awesome."
        
#screen William_McSweeny:
        
#    tag menu3
    
#    frame:
#        style_group "info3"
#        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
#        vbox:
#            label "{b}{size=+12}William McSweeny{/size}{/b}"
        
#            text "Superpower: ???"
#            text "Occupation: ???"
#            text "Specialisations: ???"
#            text "Alma Mater: ???"
        
#            text "He comes from a very old and established family."
        
#screen Yuu_Spanakopita:
    
#    tag menu3
    
#    frame:
#        style_group "info3"
#        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
#        vbox:
#            label "{b}{size=+12}Yuu Spanakopita{/size}{/b}"
        
#            text "Superpower: ???"
#            text "Occupation: ???"
#            text "Specialisations: ???"
#            text "Alma Mater: ???"
        
#            text "Yuu is a bitch who likes terrible trideo."
        
        
##############################################################################
# Other Profiles
#
# Screen that's used to display information on people not with the 72nd.

screen Rashieve_Nyarlathotep:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}Rashieve Nyarlathotep{/size}{/b}"
        
            text "Superpower: ???"
            text "Occupation: ???"
            text "Specialisations: ???"
            text "Alma Mater: ???"
        
            text "REDACTED."
        
screen Takeem_Brhavo:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}Takeem Brhavo{/size}{/b}"
        
            text "Superpower: Civillian"
            text "Occupation: Actor"
            text "Specialisations: ???"
            text "Alma Mater: ???"
        
            text "Takeem is a famous trideo actor. He is one sexy beast."


##############################################################################
# Terra Novan History
#
# Screen that's used to display information on Terra Novan histroy.

screen War_of_1919:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}War of 1919{/size}{/b}"
        
            text "The War of 1919..."
        
screen Massacre_of_Moscow:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}Massacre of Moscow{/size}{/b}"
        
            text "The Massacre of Moscow..."
        

##############################################################################
# Terra Novan Technology
#
# Screen that's used to display information on Terra Novan technology.

screen Pump_Action_Rifle:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}Pump Action Rifle{/size}{/b}"
        
            text "The Pump Action Rifle..."
        
screen Hovercraft:

    tag menu3
    
    frame:
        style_group "info3"
        at Position(xanchor = 0.0,xpos = 0.21, yanchor = 0.0, ypos = 0.09) 
        
        vbox:
            label "{b}{size=+12}Hovercraft{/size}{/b}"
        
            text "Hovercraft on Terra Nova..."

label closecodex:
    
    hide screen calendar
    hide screen clock_screen
    hide screen menu2
    hide screen menu3
    hide screen codex1
    hide screen codex2
    hide screen codex3
    hide screen codex4
    jump desktop

