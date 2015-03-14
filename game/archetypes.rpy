label archetypes:
    n "I've assembled a range of popular Founders for you to rollplay if you wish." with dissolve


label choosearchetype:
    n "There are many archetypes to choose from."
menu: 
    "Anita":
        jump anitaroddick
    "Arianna":
        jump ariannahuffington
    "Bill":
        jump billgates
    "Elon":
        jump elonmusk
    "Kiran":
        jump kiranmazamdarshaw
    "Mark":
        jump markzuckerberg
    "Peter":
        jump peterthiel
    "Rashmi":
        jump rashmi
    "Steve":
        jump stevejobs
    "Weili":
        jump weili
    "Ping Fu":
        jump pingfu
    "Actually, I'll create my own Founder":
        jump newfounder

label weilidai:

label ariannahuffington:
    
label stevejobs:
    show bg stevejobs with dissolve
    
    n "Steve blurb."
menu: 
    "Yes":
        jump stevejobsselected
    "No":
        jump choosearchetype 
    
    
label peterthiel:
    show bg stevejobs with dissolve
    
    n "Peter blurb."
menu: 
    "Yes":
        jump peterthielselected
    "No":
        jump choosearchetype 
        
        
label elonmusk:
    show bg stevejobs with dissolve
    
    n "Elon blurb."
menu: 
    "Yes":
        jump elonmuskselected
    "No":
        jump choosearchetype 
    
    
label billgates:
    show bg stevejobs with dissolve
    
    n "Bill blurb."
menu: 
    "Yes":
        jump billgatesselected
    "No":
        jump choosearchetype 


label anitaroddick:
    show bg stevejobs with dissolve
    
    n "Anita blurb."
menu: 
    "Yes":
        jump anitaroddickselected
    "No":
        jump choosearchetype 
        
label rashmi:
    show bg stevejobs with dissolve
    
    n "Rashmi blurb."
menu: 
    "Yes":
        jump rashmisinhaselected
    "No":
        jump choosearchetype
    
label mark:
    show bg stevejobs with dissolve
    
    n "Mark blurb."
menu: 
    "Yes":
        jump markzuckkerbergselected
    "No":
        jump choosearchetype    
        
label ping:
    show bg stevejobs with dissolve
    
    n "Ping Fu blurb."
menu: 
    "Yes":
        jump pingfuselected
    "No":
        jump choosearchetype  
    
label markszuckerbergselected:
    stop movie
    define pov = Character("[povname]")

python:
        povname = "Mark"
        povcurrency = "$"
        povage = "29"
jump homeoffice
    
label stevejobsselected:
    stop movie
    define pov = Character("[povname]")

python:
        povname = "Steve"
        povcurrency = "$"
        povage = "56"
jump homeoffice    

label peterthielselected:
    stop movie
    define pov = Character("[povname]")

python:
        povname = "Peter"
        povcurrency = "$"
        povage = "46"
jump homeoffice


    
label elonmuskselected:
    stop movie
    define pov = Character("[povname]")

python:
         povname = "Elon"
         povcurrency = "$"
         povage = "42"
jump homeoffice
    
    
    
    
label billgatesselected:
    stop movie
    define pov = Character("[povname]")

python:
         povname = "Bill"
         povcurrency = "$"
         povage = "58"
jump homeoffice
    
    
    
label pingfuselected:
    stop movie
    define pov = Character("[povname]")

python:
         povname = "Ping"
         povcurrency = "$"
         povage = "58"
jump homeoffice    
    
    
label anitaroddickselected:
    stop movie
    define pov = Character("[povname]")

python:
         povname = "Anita"
         povcurrency = "£"
         povage = "64"
         
jump homeoffice

label rashmisinhaselected:
    stop movie
    define pov = Character("[povname]")

python:
         povname = "Rashmi"
         povcurrency = "₨"
         povage = "43"
         
jump homeoffice