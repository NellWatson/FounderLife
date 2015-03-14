label nelltiphomeoffice:
    call nelltip #since one cannot Call from an imagemap


label nelltip:
    $ randomnelltips_list = [
    "Make sure that you get enough rest.",
    "You don't need a tip, you need to follow-through! Keep going.",
    "Follow your instincts.",
    "Move through this world with a tender heart, championed by a valiant spirit.",
    "Keep your eye on the ball.",
    "Be a stone in the river. May your troubles wrap around you like water, and then drift on by.",
    "Sometimes humor is the one thing that keeps one sane.",
    "An army marches on its stomach. You're a general: Eat properly and profit."
    ]
    $ tip_to_show = renpy.random.choice(randomnelltips_list)

#if...:
#    n "All work and no play makes [povname] a dull [povgendershorthanddiminutive]."

    
    n "[tip_to_show]" with dissolve
    $renpy.transition(dissolve) 
    hide nell with dissolve
    call desktopexit

     
#call screen nelltips

#screen nelltips:


#window:
#  style "gm_root"

#  vbox:
#   spacing 10
  
#   frame:
#    style_group "mm_root"
#    xfill True
#    xmargin 10
#    top_margin 10
#    text "Founder Life Help"
    

#   frame:
#    style_group "mm_root"  
#    xmargin 10
#    xfill True
#    yfill True
#    bottom_margin 60
   
#    viewport:
#     scrollbars "vertical"
#     mousewheel True
#     draggable True
     
#     vbox: 

#        vbox: 
#            n "Here's a Test tip for this situation."

##frame:
##  xmargin 10
##  yalign .98
##  vbox:
##   textbutton _("Return") action Return()

#init python:
#    #This controls minimum button length
#    style.nelltips = Style(style.frame)
#    style.nelltips_button.xmaximum = 200
#    style.nelltips_button.xminimum = 200
#    style.nelltips_button.yminimum = 55

