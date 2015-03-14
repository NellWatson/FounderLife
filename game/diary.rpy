label diary:
#    scene bg gmenu with dissolve
    n "If you like, you can do some self-reflection here. It should only take you 10-15 mins, but might help to make your key motivations clear."
    $ renpy.transition(dissolve)
    call screen purpose


    
#    Pick your most important values from the following list 
    
#    Write about why these matter to you:

#init:
#    personalvalues = renpy.input("These values are important to me because:")
#    personalvalues = personalvalues.strip()

#    if not povname:
#         povname = "Founder"
         
screen purpose:

 tag menu
 
 window:
  style "gm_root"

  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    text "Self Reflection" xalign 0.5
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     textbutton _("Purpose") action Show("purpose") xalign 0.2
     textbutton _("Confidence") action Show("confidence") xalign 0.4
     textbutton _("Conflct") action Show("conflict") xalign 0.6
     textbutton _("Happiness") action Show("happiness") xalign 0.8


   frame:
    style_group "mm_root"  
    xmargin 10
    xfill True
    yfill True
    top_margin 10
    bottom_margin 60
   
    viewport:
      scrollbars "vertical"
      mousewheel True
      draggable True
     
      vbox: 

        vbox: 
            text "{b}Following your purpose{/b}"
            text ""
            text "Understanding the reasons why you choose to undertake the more difficult, yet rewarding path in life is important."
            text ""
            text "Focus."
            text ""            
            text "Clarify what you want to sell, remembering: a) You can't be all things to all people and b) \"smaller is bigger.\" Your niche is not the same as the field in which you work. For example, a retail clothing business is not a niche but a field. A more specific niche may be \"maternity clothes for executive women.\" To begin this focusing process, Falkenstein suggests using these techniques to help you:"
            text ""
            text "Make a list of things you do best and the skills implicit in each of them."
            text ""
            text "List your achievements."
            text ""
            text "Identify the most important lessons you have learned in life."
            text ""
            text "Look for patterns that reveal your style or approach to resolving problems."
            text ""
            text" Your niche should arise naturally from your interests and experience. For example, if you spent 10 years working in a consulting firm, but also spent 10 years working for a small, family-owned business, you may decide to start a consulting business that specializes in small, family-owned companies."
            text ""
            text "Describe the customer's worldview."
            text ""
            text "A successful business uses what Falkenstein calls the Platinum Rule: \"Do unto others as they would do unto themselves.\" When you look at the world from your prospective customers' perspective, you can identify their needs or wants. The best way to do this is to talk to prospective customers and identify their main concerns."
            text ""
            text "Synthesize."
            text ""
            text "At this stage, your niche should begin to take shape as your ideas and the client's needs and wants coalesce to create something new. A good niche has five qualities:"
            text ""
            text "It takes you where you want to go -- in other words, it conforms to your long-term vision."
            text ""
            text "Somebody else wants it -- namely, customers."
            text ""
            text "It's carefully planned."
            text ""
            text "It's one-of-a-kind, the \'only game in town.\'"
            text ""
            text "It evolves, allowing you to develop different profit centers and still retain the core business, thus ensuring long-term success."



 frame:
  xmargin 10
  yalign .98
  vbox:
   textbutton _("Return") action Jump("desktop")
   
   
screen confidence:


 tag menu
 
 window:
  style "gm_root"

  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    text "Self Reflection" xalign 0.5
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     textbutton _("Purpose") action Show("purpose") xalign 0.2
     textbutton _("Confidence") action Show("confidence") xalign 0.4
     textbutton _("Conflct") action Show("conflict") xalign 0.6
     textbutton _("Happiness") action Show("happiness") xalign 0.8


   frame:
    style_group "mm_root"  
    xmargin 10
    xfill True
    yfill True
    top_margin 10
    bottom_margin 60
   
    viewport:
      scrollbars "vertical"
      mousewheel True
      draggable True
     
      vbox: 

        vbox: 
            
#            define pov purpose1("[povpurpose1]")

#            python:
#                povname = renpy.input("What skills do you want to master?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "The skills that I would like to master are..."

#            text "\n{b}{space=10}Purpose{/b}"
#            text "[povpurpose1]"
#            text "What worries you about this journey?"
            
#            define pov purpose1("[povconfidence1]")

#            python:
#                povname = renpy.input("What worries you about your entrepreneurial journey?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "I worry about..."
            
            text "Don't slouch! Regardless of your confidence level, slouching communicates you lack faith in yourself."
            text ""
            text "Try posting a note on the edge of your computer display with a reminder such as an up arrow in thick red marker or the words \"SIT UP STRAIGHT\". To correct yourself, roll your shoulders back and imagine someone just pulled a string from the top of your head, elongating your spine and raising your chin so it's in a neutral, forward-facing position."
            text ""
            text "Understand that most people aren't thinking about you. Self-conscious people worry too much about what others think about them. The thing is, usually other people aren't thinking about them--at all."
            text ""
            text "Imagine you had the magical power to read the thoughts of the people around you. You know what you'd hear a lot of? Stuff like this:"
            text ""
            text "\"Crap, I forgot to stop by the bank... I shouldn't have eaten that cake Susan brought to work, now I feel fat... I hope Sara flirts with me again tonight at volleyball like she did last week... Why should I have to clean the downstairs bathroom when Bill is the only one in the house who uses it?\""
#    text

 frame:
  xmargin 10
  yalign .98
  vbox:
   textbutton _("Return") action Jump("desktop")


screen conflict:


 tag menu
 
 window:
  style "gm_root"

  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    text "Self Reflection" xalign 0.5
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     textbutton _("Purpose") action Show("purpose") xalign 0.2
     textbutton _("Confidence") action Show("confidence") xalign 0.4
     textbutton _("Conflct") action Show("conflict") xalign 0.6
     textbutton _("Happiness") action Show("happiness") xalign 0.8


   frame:
    style_group "mm_root"  
    xmargin 10
    xfill True
    yfill True
    top_margin 10
    bottom_margin 60
   
    viewport:
      scrollbars "vertical"
      mousewheel True
      draggable True
     
      vbox: 

        vbox: 
            
#            define pov purpose1("[povpurpose1]")

#            python:
#                povname = renpy.input("What skills do you want to master?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "The skills that I would like to master are..."

#            text "\n{b}{space=10}Purpose{/b}"
#            text "[povpurpose1]"
#            text "What worries you about this journey?"
            
#            define pov purpose1("[povconfidence1]")

#            python:
#                povname = renpy.input("What worries you about your entrepreneurial journey?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "I worry about..."
            
            text "Managing Conflict within a startup team can be tough. Disputes among startup team members are quite common, and can potentially destroy a company."
            text ""

            text ""
            text ""
            text ""
#    text

 frame:
  xmargin 10
  yalign .98
  vbox:
   textbutton _("Return") action Jump("desktop")
   
   
   
screen happiness:


 tag menu
 
 window:
  style "gm_root"

  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    text "Self Reflection" xalign 0.5
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     textbutton _("Purpose") action Show("purpose") xalign 0.2
     textbutton _("Confidence") action Show("confidence") xalign 0.4
     textbutton _("Conflct") action Show("conflict") xalign 0.6
     textbutton _("Happiness") action Show("happiness") xalign 0.8


   frame:
    style_group "mm_root"  
    xmargin 10
    xfill True
    yfill True
    top_margin 10
    bottom_margin 60
   
    viewport:
      scrollbars "vertical"
      mousewheel True
      draggable True
     
      vbox: 

        vbox: 
            
#            define pov purpose1("[povpurpose1]")

#            python:
#                povname = renpy.input("What skills do you want to master?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "The skills that I would like to master are..."

#            text "\n{b}{space=10}Purpose{/b}"
#            text "[povpurpose1]"
#            text "What worries you about this journey?"
            
#            define pov purpose1("[povconfidence1]")

#            python:
#                povname = renpy.input("What worries you about your entrepreneurial journey?:")
#                povname = povname.strip()

#            if not povname:
#                povname = "I worry about..."
            
            text "Happiness comes from understanding what virtue is, and then living a life that aligns with it."
            text ""

            text ""
            text ""
            text ""
#    text

 frame:
  xmargin 10
  yalign .98
  vbox:
   textbutton _("Return") action Jump("desktop")

init python:
    #This controls minimum button length
    style.helpfile = Style(style.frame)
    style.helpfile_button.xmaximum = 200
    style.helpfile_button.xminimum = 200
    style.helpfile_button.yminimum = 55