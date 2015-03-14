##############################################################################
# Home Screen
#
# A kind of dashboard allowing the player to look at their stats.

screen home:
    tag menu2
    
    frame:
        style_group "home"
        xalign 1.0
        yalign 0.8
        
        grid 4 2:
            transpose False
            textbutton "Stats" action Show("stats")
            textbutton "Talk" action Show("talk")
            textbutton "Diet" action Show("diet")
            textbutton "Info" action Show("info")
            
            textbutton "Town" action Show("town")
            textbutton "Castle" action Show("castle")
            textbutton "Items" action Show("inventory_screen")
            textbutton "Save" action ShowMenu("save")
    
    frame:
        style_group "home2"
        xalign 1.0
        yalign 1.0
        vbox: 
            textbutton "Schedule" action Jump("month")
            
init python:
    #This controls minimum button length
    style.home = Style(style.frame)
    style.home_button.xmaximum = 100
    style.home_button.xminimum = 100
    style.home_button.yminimum = 100
    style.home_button.ymaximum = 100
    
init python:
    #This controls minimum button length
    style.home2 = Style(style.frame)
    style.home2_button.xmaximum = 400
    style.home2_button.xminimum = 400
    style.home2_button.yminimum = 100
    style.home2_button.ymaximum = 100
    
#STATS

screen stats:
    
    tag menu
    
    frame:
        xalign 0.3
        yalign 0.3
        
        vbox:
            text "Appearance: [APP]"
            text "Build: [BLD]"
            text "Fitness: [FIT]"
            text "Creativity: [CRE]"
            text "Influence: [INF]"
            text "Knowledge: [KNO]"
            text "Psyche: [PSY]"
            text "Perception: [PER]"
            text "Willpower: [WIL]"
            text "Stress: [Stress]"
            text "Money: [Money]"
            
            textbutton "Cancel" action Hide("menu") 

#TALK

screen talk:
    
    tag menu
    
    frame:
        style_group "talk"
        xalign 0.3
        yalign 0.3
        
        vbox:
            textbutton "Praise"
            textbutton "Small Talk"
            textbutton "Scold"
            textbutton "Pocket Money"
            
            textbutton "Cancel" action Hide("menu") 
            
init python:
    #This controls minimum button length
    style.talk_button.xminimum = 220
    style.talk_label.xalign = .5
    

#DIET

screen diet:
    
    tag menu
    
    frame:
        style_group "diet"
        xalign 0.3
        yalign 0.3
        
        vbox:
            textbutton "Normal Diet"
            textbutton "Robust Diet"
            textbutton "Slimming Diet"
            textbutton "Weight Loss Diet"
            
            textbutton "Cancel" action Hide("menu") 
            
init python:
    #This controls minimum button length
    style.diet_button.xminimum = 220
    style.diet_label.xalign = .5
    

#INFO

screen info:
    
    tag menu
    
    frame:
        xalign 0.3
        yalign 0.3
        
        vbox:
            text "First name: "
            text "Last name: "
            text "Blood type: "
            text "Age: "
            text "Birthday: "
            text "Sign: "
            text "Patron"
    
    frame: 
        xalign 0.3
        yalign 0.6
        
        vbox: 
            text "Sickness"
            text "Delinquency"
            text "Popularity"
            
            text "Diet: "
            
            textbutton "Cancel" action Hide("menu") 
    

#TOWN

screen town:
    
    tag menu
    
    frame:
        style_group "town"
        xalign 0.3
        yalign 0.3
            
        grid 2 3:
            transpose True
            
            textbutton "Armorer"
            textbutton "Restaurant"
            textbutton "Church"
            
            textbutton "Tailor"
            textbutton "Pawn Shop"
            textbutton "Hospital"
            
    frame: 
        xalign 0.42
        yalign 0.43
            
        textbutton "Cancel" action Hide("menu")
        
init python:
    #This controls minimum button length
    style.town_button.xminimum = 220
    style.town_label.xalign = .5
    

#CASTLE

screen castle:
    
    tag menu
    
    frame:
        style_group "castle"
        xalign 0.3
        yalign 0.3
        
        vbox:
            textbutton "Palace Guard"
            textbutton "Royal Knight"
            textbutton "General"
            textbutton "Minister of State"
            textbutton "Archbishop"
            textbutton "Royal Concubine"
            textbutton "Queen"
            textbutton "King"
            textbutton "Jester"
            
            textbutton "Cancel" action Hide("menu") 
            
init python:
    #This controls minimum button length
    style.castle_button.xminimum = 220
    style.castle_label.xalign = .5
    

#ITEMS

screen items:
    
    tag menu
    
    frame:
        style_group "items"
        xalign 0.3
        yalign 0.3
        
        vbox:
            textbutton "Remove Weapon"
            textbutton "Remove Armor"
            
            textbutton "Cancel" action Hide("menu") 
            
init python:
    #This controls minimum button length
    style.items_button.xminimum = 20
    style.items_label.xalign = .5
    
    