##############################################################################
# Schedule
#
# Screen that's used to set a schedule for the month. 

screen schedule:
    
    tag menu
    modal True

    frame:
        style_group "schedule"       
        xalign .5
        yalign .40
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Daily Schedule"

        grid 4 5:
            transpose True
           
            label "First Block"
            textbutton "School" action Show("school_1")
            textbutton "Work" action Show("work_1")
            textbutton "Travel" action Show("travel_1")
            textbutton "Rest" action Show("rest_1")
           
            label "Second Block"
            textbutton "School" action Show("school_2")
            textbutton "Work" action Show("work_2")
            textbutton "Travel" action Show("travel_2")
            textbutton "Rest" action Show("rest_2")
           
            label "Third Block"
            textbutton "School" action Show("school_3")
            textbutton "Work" action Show("work_3")
            textbutton "Travel" action Show("travel_3")
            textbutton "Rest" action Show("rest_3")
           
            label "Fourth Block"
            textbutton "School" action Show("school_4")
            textbutton "Work" action Show("work_4")
            textbutton "Travel" action Show("travel_4")
            textbutton "Rest" action Show("rest_4")

        hbox:
            xalign 0.5
            textbutton "Done" action [Hide("menu2"), Return()]
            textbutton "Cancel" action Hide("menu") 

init python:
    #This controls minimum button length
    style.schedule_button.xminimum = 180
    style.schedule_label.xalign = .5

#WEEK 01

screen school_1:
    
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "What Would You Like To Study?"

        grid 1 4:
            transpose True
           
            textbutton "Art" action SetVariable("week01", "Art")
            textbutton "Fencing" action SetVariable("week01", "Fencing")
            textbutton "Math" action SetVariable("week01", "Math")
            textbutton "Alchemy" action SetVariable("week01", "Alchemy")

        textbutton "Select" action Hide("menu4") xalign .5
        
    
screen work_1:
    
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Work?"

        grid 1 4:
            transpose True
           
            textbutton "Church" action SetVariable("week01", "Church")
            textbutton "Farm" action SetVariable("week01", "Farm")
            textbutton "Store" action SetVariable("week01", "Store")
            textbutton "Chores" action SetVariable("week01", "Chores")

        textbutton "Select" action Hide("menu4") xalign .5
        

screen travel_1:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Go?"

        grid 1 4:
            transpose True
           
            textbutton "North" action SetVariable("week01", "North")
            textbutton "East" action SetVariable("week01", "East")
            textbutton "South" action SetVariable("week01", "South")
            textbutton "West" action SetVariable("week01", "West")

        textbutton "Select" action Hide("menu4") xalign .5


screen rest_1:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Rest?"

        grid 1 4:
            transpose True
           
            textbutton "Home" action SetVariable("week01", "Home")
            textbutton "Library" action SetVariable("week01", "Library")
            textbutton "Vacation" action SetVariable("week01", "Vacation")
            textbutton "Hospital" action SetVariable("week01", "Hospital")

        textbutton "Select" action Hide("menu4") xalign .5


#WEEK 02

screen school_2:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "What Would You Like To Study?"

        grid 1 4:
            transpose True
           
            textbutton "Art" action SetVariable("week02", "Art")
            textbutton "Fencing" action SetVariable("week02", "Fencing")
            textbutton "Math" action SetVariable("week02", "Math")
            textbutton "Alchemy" action SetVariable("week02", "Alchemy")

        textbutton "Select" action Hide("menu4") xalign .5
        
    
screen work_2:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Work?"

        grid 1 4:
            transpose True
           
            textbutton "Church" action SetVariable("week02", "Church")
            textbutton "Farm" action SetVariable("week02", "Farm")
            textbutton "Store" action SetVariable("week02", "Store")
            textbutton "Chores" action SetVariable("week02", "Chores")

        textbutton "Select" action Hide("menu4") xalign .5


screen travel_2:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Go?"

        grid 1 4:
            transpose True
           
            textbutton "North" action SetVariable("week02", "North")
            textbutton "East" action SetVariable("week02", "East")
            textbutton "South" action SetVariable("week02", "South")
            textbutton "West" action SetVariable("week02", "West")

        textbutton "Select" action Hide("menu4") xalign .5


screen rest_2:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Rest?"

        grid 1 4:
            transpose True
           
            textbutton "Home" action SetVariable("week02", "Home")
            textbutton "Library" action SetVariable("week02", "Library")
            textbutton "Vacation" action SetVariable("week02", "Vacation")
            textbutton "Hospital" action SetVariable("week02", "Hospital")

        textbutton "Select" action Hide("menu4") xalign .5
    
    
#WEEK 03

screen school_3:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "What Would You Like To Study?"

        grid 1 4:
            transpose True
           
            textbutton "Art" action SetVariable("week03", "Art")
            textbutton "Fencing" action SetVariable("week03", "Fencing")
            textbutton "Math" action SetVariable("week03", "Math")
            textbutton "Alchemy" action SetVariable("week03", "Alchemy")

        textbutton "Select" action Hide("menu4") xalign .5
    
screen work_3:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Work?"

        grid 1 4:
            transpose True
           
            textbutton "Church" action SetVariable("week03", "Church")
            textbutton "Farm" action SetVariable("week03", "Farm")
            textbutton "Store" action SetVariable("week03", "Store")
            textbutton "Chores" action SetVariable("week03", "Chores")

        textbutton "Select" action Hide("menu4") xalign .5


screen travel_3:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Go?"

        grid 1 4:
            transpose True
           
            textbutton "North" action SetVariable("week03", "North")
            textbutton "East" action SetVariable("week03", "East")
            textbutton "South" action SetVariable("week03", "South")
            textbutton "West" action SetVariable("week03", "West")

        textbutton "Select" action Hide("menu4") xalign .5


screen rest_3:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "How Would You Like To Rest?"

        grid 1 4:
            transpose True
           
            textbutton "Home" action SetVariable("week03", "Home")
            textbutton "Spa" action SetVariable("week03", "Library")
            textbutton "Vacation" action SetVariable("week03", "Vacation")
            textbutton "Clinic" action SetVariable("week03", "Hospital")

        textbutton "Select" action Hide("menu4") xalign .5


#WEEK 04

screen school_4:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "What Would You Like To Study?"

        grid 1 4:
            transpose True
           
            textbutton "Art" action SetVariable("week04", "Art")
            textbutton "Fencing" action SetVariable("week04", "Fencing")
            textbutton "Math" action SetVariable("week04", "Math")
            textbutton "Alchemy" action SetVariable("week04", "Alchemy")

        textbutton "Select" action Hide("menu4") xalign .5

    
screen work_4:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Work?"

        grid 1 4:
            transpose True
           
            textbutton "Church" action SetVariable("week04", "Church")
            textbutton "Farm" action SetVariable("week04", "Farm")
            textbutton "Store" action SetVariable("week04", "Store")
            textbutton "Chores" action SetVariable("week04", "Chores")

        textbutton "Select" action Hide("menu4") xalign .5


screen travel_4:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Go?"

        grid 1 4:
            transpose True
           
            textbutton "North" action SetVariable("week04", "North")
            textbutton "East" action SetVariable("week04", "East")
            textbutton "South" action SetVariable("week04", "South")
            textbutton "West" action SetVariable("week04", "West")

        textbutton "Select" action Hide("menu4") xalign .5


screen rest_4:
        
    tag menu4
    
    frame:
        style_group "schedule"       
        xalign .5
        yalign .33
       
        #This controls vertical spacing
        has vbox spacing 20

        label "Where Would You Like To Rest?"

        grid 1 4:
            transpose True
           
            textbutton "Home" action SetVariable("week04", "Home")
            textbutton "Library" action SetVariable("week04", "Library")
            textbutton "Vacation" action SetVariable("week04", "Vacation")
            textbutton "Hospital" action SetVariable("week04", "Hospital")

        textbutton "Select" action Hide("menu4") xalign .5