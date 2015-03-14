label createfounder:  
    n "All Founders have a self-made quality about them."
    n "It's important to have self-knowledge, and to understand the factors that make you as a person unique."
    n "However, you can also choose to rollplay a preset Founder archetype instead."
    hide nell with dissolve
    
menu: 
    "I'll create a new founder":
        jump newfounder
    "Let's select from a preset archetype":
        jump archetypes
    #"Load an existing founder":
        #jump loadfounder

        
label newfounder:
    n "Welcome, self-builder! What's your name?"
    define pov = Character("[povname]")
    hide nell with dissolve

python:
    povname = renpy.input("Please type your name:")
    povname = povname.strip()

    if not povname:
         povname = "Founder"

pov "My name is [povname]!" with dissolve
if povname == "Nell Watson":
    n "Oh, it {i}is{/i}, is it?" with hpunch
    $ nellwatsoneegg = True
     #set Nell stats
    stop movie
    jump homeoffice
    #call screen input_softkeyboard
else:    
    n "Howdy [povname]!" with dissolve
label mf:
    n "So, are you male, female?"
menu:
    "Female":
        $ female = True
        define povgendershorthanddiminutive = ("girl")
    "Male":
        $ male = True
        define povgendershorthanddiminutive = ("boy")
    "Other":
        $ othergender = True
        define povgendershorthanddiminutive = ("person")
        
label age:
    if othergender:
        n "Interesting. I'm going to assume that you're mostly organic." 
        
    n "How old are you?"
    hide nell with dissolve
    
python:
    povage = renpy.input("Please type your age:")
    povage = povage.strip()

    if not povage:
         povage = "30"

pov "I'm [povage] years old!" with dissolve
           
        
label childhood:
    if povage == 18:
        n "Welcome youngling!"
    if povage == 60:
        n "Welcome old-timer!" 
    else:
        pass
    
    n "Now, how was your childhood?" with dissolve
menu:
    "All things considered, I had a great childhood":
        $ childhoodgood = True
    "Kinda average, I guess":
        $ childhoodneutral = True
    "Ha! It was pretty tragic":
        $ childhoodbad = True
        
label queerquestion:   
    if childhoodbad:
        n "I'm sorry, that really sucks." with dissolve
   
    n "Do you consider yourself part of the Queer spectrum?" with dissolve
menu:
    "Yes, I do identify as 'Queer'":
        $ queer = True
    "No, I'm not Queer":
        jump minority

       
label queer:           
    if male:
        n "Loud and proud bro!"
    if female:
        n "Loud and proud sister!"
    if othergender:
        n "Figured you might be!"
            
label queerclassification:
        
    n "In terms of what floats your boat, might you classify yourself as:" with dissolve
menu: 
    "Lesbian or Gay":
        $ gay = True
    "Bisexual":
        $ bi = True
    "Asexual":
        $ asexual = True
    "Other":
        $ othersexuality = True
    "Straight actually":
        $ straight = True

label gender:
    n "Great, and would you happen to also be:" with dissolve
menu:                    
    "Transgendered":
        $ transgendered = True
    "Intersex":
        $ intersex = True
    "Genderqueer":
        $ genderqueer = True
    "Cisgender (i.e. always comfortable in your body and gender)":
        $ cisgender = True
 
label minority:
    n "Did you grow up as a minority ethnicity?" with dissolve
menu: 
    "Yes, I grew up as a minority":
        $ minority = True
    "No, I didn't":
        $ minority = False

label education:
    n "How about your formal education?" with dissolve
menu:
    "PhD":
        $ education = 4
    "Post-Grad":
        $ education = 3
    "Bachelor's or equivalent":
        $ education = 2
    "Graduated High School":
        $ education = 1
    "I learned wisdom from life instead":
        $ education = 0
       
label disability:
    n "How able-bodied are you?" with dissolve
menu:
    "Just fine":
        $ disability = 0
    "Some physical disability":
        $ disability = 1
    "Major physical disability":
        $ disability = 2

label health:
    n "Other than that, how is your health in general?" with dissolve
menu:    
    "Fit as a flea":
        $ health = 3
    "I need to take it easy sometimes":
        $ health = 2
    "It could be better":
        $ health = 1
    "Not good at all":
        $ health = 0
        


    
label canyoucode:
    
    n "Great, now we begin to see the measure of who you are!" with dissolve
    n "Now, let's learn about your skills."
    n "So, can you code?"
menu:    
    "0100001001001111010011110100110100100001":
        $ cancode = 3
    "#include \<stdio.h\>int main(void)\{puts(\"Oh yeah!\");return 0;\}":
        $ cancode = 2
    "trace/echo/msgbox/print (\"I script nicely\");":
        $ cancode = 1
    "Uhh...":
        $ cancode = 0
        
label canyouwords:
    n "And.. how are you with language in general?" with dissolve
menu:    
    "My language skills shine / never has a day gone by / with words found wanting":
        $ canwords = 3
    "\'Irrepressibly scintillating\'":
        $ canwords = 2
    "I both can spell and write":
        $ canwords = 1
    "knot zo gud":
        $ canwords = 0
        
label canyoudraw:
    n "Ok. Can you draw?" with dissolve
menu:    
    "I'm a true artist":
        $ candraw = 3
    "I make little sketches now and then":
        $ candraw = 2
    "I can do a doodle or two":
        $ candraw = 1
    "Can't draw a stick figure":
        $ candraw = 0

if candraw == 0:
    $ arts_skill = 0
if candraw == 1:
    $ arts_skill = 20
if candraw == 2:
    $ arts_skill = 40
if candraw == 3:
    $ arts_skill = 60
    



    n "Alright! Now I have a better idea of your capabilities, thank you." with dissolve
        
    n "Finally, what's your currency of choice ($, €, £, etc?)"
    hide nell with dissolve
python:
    povcurrency = renpy.input("Please type your currency symbol of choice:")
    povcurrency = povcurrency.strip()

    if not povcurrency:
         povcurrency = "$"

pov "I want it to rain [povcurrency]s!" with dissolve
label createdfounderdone:  
#    $FLLogger.writeTo("Created a founder")
    n "Me too, friend..."
    #call screen character_creation
    $ createdafounder = True
    $ renpy.block_rollback()
    stop music fadeout 1.0
    stop movie
    jump homeoffice