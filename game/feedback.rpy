label feedback:
    
    
    $ renpy.transition(dissolve)        
    n "Thanks for playing my game!"
    n "I hope that you're enjoying it."
    n "This game is very much a prototype. Like any prototype, it needs feedback to improve."
    n "If you want to, you can send me a brief message of feedback (from inside the game)."
    n "Please will you spare a moment to write your thoughts?"
    menu:
        "Sure":
            pass
        "Not this time":
            $ renpy.transition(dissolve)
            jump desktop
                       
#python:
#    feedback = renpy.input("My feedback is the following:")
    
label aa: 
    
python:

    sendemail(from_addr  = 'founderlifeplayer@kickassfounder.net', 
            to_addr_list = ['nell@nellwatson.com'],
            cc_addr_list = [renpy.input("\"My email address is:\" (optional)")],
            subject      = renpy.input("\"My name is:\""), 
            message      = renpy.input("\"My feedback is the following:\"")#,
#            login        = 'pythonuser', 
#            password     = 'XXXXX'            
            )
label ab:   
    play sound "sfx/thanksalot.ogg"
    n "Thanks a lot!"
    $ renpy.transition(dissolve)
    jump desktop