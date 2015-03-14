# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

#Musicbox

init python:
    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=2.0)
    # Step 2. Add music files.
    mr.add("music/wholikestoparty.mp3", always_unlocked=True)
    mr.add("music/risinggame.mp3", always_unlocked=True)    
    mr.add("music/etherdisco.mp3", always_unlocked=True)     
    mr.add("music/stringeddisco.mp3", always_unlocked=True)
    mr.add("music/overcast.mp3", always_unlocked=True)
    mr.add("music/discocontutti.mp3", always_unlocked=True)
    mr.add("music/aureacarmina.mp3", always_unlocked=True)
    mr.add("music/electrodoodle.mp3", always_unlocked=True)
    mr.add("music/presenterator.mp3", always_unlocked=True)


##############################################################################
# Character Creation Screen - by Steamgirl
#
# A screen lets you distribute skill points.
# To use this screen initialise the various points
# Then use the following in your script:
# call screen character_creation
##############################################################################
# Example initialisation of points below. Move it where you want it.

init:
    #The number of maximum creation points
    $ init_creation_points = 30
    #The current number of creation points
    $ creation_points = init_creation_points

    #Skill 1 (in the example case, it's Intelligence)
    $ skill1_max = 10
    $ skill1_points = 0

    #Skill 2 (in the example case, it's Strength)
    $ skill2_max = 10
    $ skill2_points = 0
    
    #Skill 3 (in the example case, it's Prescence)
    $ skill3_max = 10
    $ skill3_points = 0
    
    #Skill 4 (in the example case, it's Wits)
    $ skill4_max = 10
    $ skill4_points = 0
    
    #Skill 5 (in the example case, it's Dexterity)
    $ skill5_max = 10
    $ skill5_points = 0
    
    #Skill 6 (in the example case, it's Manipulation)
    $ skill6_max = 10
    $ skill6_points = 0
    
    #Skill 7 (in the example case, it's Resolve)
    $ skill7_max = 10
    $ skill7_points = 0
    
    #Skill 8 (in the example case, it's Stamina)
    $ skill8_max = 10
    $ skill8_points = 0
    
    #Skill 9 (in the example case, it's Composure)
    $ skill9_max = 10
    $ skill9_points = 0
    
    #Skill 10 (in the example case, it's Wisdom)
    $ skill10_max = 00
    $ skill10_points = 0
    

screen character_creation:
    
    frame:
        has vbox
        hbox:
            text "Points available: [creation_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Intelligence") xminimum 200 action None
            else:
                textbutton ("Intelligence") xminimum 200 action [SetVariable("skill1_points", skill1_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill1_max value skill1_points xmaximum 200
        hbox:
            if creation_points == 0:
                textbutton ("Strength") xminimum 200 action None
            else:
                textbutton ("Strength") xminimum 200 action [SetVariable("skill2_points", skill2_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill2_max value skill2_points xmaximum 200
        hbox:
            if creation_points == 0:
                textbutton ("Presence") xminimum 200 action None
            else:
                textbutton ("Presence") xminimum 200 action [SetVariable("skill3_points", skill3_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill3_max value skill3_points xmaximum 200
        hbox:
            if creation_points == 0:
                textbutton ("Wits") xminimum 200 action None
            else:
                textbutton ("Wits") xminimum 200 action [SetVariable("skill4_points", skill4_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill4_max value skill4_points xmaximum 200
        hbox:
            if creation_points == 0:
                textbutton ("Dexterity") xminimum 200 action None
            else:
                textbutton ("Dexterity") xminimum 200 action [SetVariable("skill5_points", skill5_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill5_points xmaximum 200 
        hbox:
            if creation_points == 0:
                textbutton ("Manipulation") xminimum 200 action None
            else:
                textbutton ("Manipulation") xminimum 200 action [SetVariable("skill6_points", skill6_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill6_points xmaximum 200    
        hbox:
            if creation_points == 0:
                textbutton ("Resolve") xminimum 200 action None
            else:
                textbutton ("Resolve") xminimum 200 action [SetVariable("skill7_points", skill7_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill7_points xmaximum 200    
        hbox:
            if creation_points == 0:
                textbutton ("Stamina") xminimum 200 action None
            else:
                textbutton ("Stamina") xminimum 200 action [SetVariable("skill8_points", skill8_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill8_points xmaximum 200    
        hbox:
            if creation_points == 0:
                textbutton ("Composure") xminimum 200 action None
            else:
                textbutton ("Composure") xminimum 200 action [SetVariable("skill9_points", skill9_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill9_points xmaximum 200    
        hbox:
            if creation_points == 0:
                textbutton ("Wisdom") xminimum 200 action None
            else:
                textbutton ("Wisdom") xminimum 200 action [SetVariable("skill10_points", skill10_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill5_max value skill10_points xmaximum 200    
            
            
        hbox:
            textbutton ("Start Over") action [SetVariable("skill1_points", 0), SetVariable("skill2_points", 0), SetVariable("skill3_points", 0), SetVariable("skill4_points", 0), SetVariable("skill5_points", 0), SetVariable("skill6_points", 0), SetVariable("skill7_points", 0), SetVariable("skill8_points", 0), SetVariable("skill9_points", 0), SetVariable("skill10_points", 0), SetVariable("creation_points", init_creation_points)]
            if creation_points == 0:
                textbutton ("Finished") action Return()
            else:
                textbutton ("Finished") action None
                
screen extras:
    tag menu
    add "extras.png"

    frame:
        style_group "extras"
        xalign 0.5
        yalign 0.5

        has hbox

#        textbutton _("Contacts") action ShowMenu('codex', transition=dissolve) #text_style "extra" style "extra"
#        text("|") #style "extra"
        textbutton _("Gallery") action ShowMenu('bg_gallery', transition=dissolve) #text_style "extra" style "extra"
        text("|") #style "extra"
        textbutton _("FounderPedia") action ShowMenu('encyclopaedia_list', transition=dissolve) #text_style "extra" style "extra"
        text("|") #style "extra"
        textbutton _("Music Box") action ShowMenu('musicroom', transition=dissolve) #text_style "extra" style "extra"
        text("|") #style "extra"
        textbutton _("Credits") action ShowMenu('credits', transition=dissolve) #text_style "extra" style "extra"
        text("|") #style "extra"
        textbutton _("Back") action Return() #text_style "extra" style "extra"

init -2 python:
    style.extra = Style(style.default)
    style.extra.size=40
    style.extra.bold=True
#    style.extra.font="ui/PRESENCE_Regular.ttf"
    style.extra.outlines=[(3, "#ececec", 0, 0)]
    style.extra.color="fff"
    style.extra.idle_color = "#898989"
    style.extra.hover_color = "#c5c5c5"
    style.extra.selected_color = "#787878"
    style.extra.kerning = 5
                
##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    
init -2 python:
    style.say_label.bold = False
    style.say_label.font = "ui/Comfortaa-Bold.ttf"
    style.say_label.size = 28
#    style.say_label.size = 28

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    if reply_screen:
        # this is the menu for message replies
        frame:
            style_group "mailbox"

            vbox:
                label "Drafting Reply"
                text ("To: " + current_message.sender)
                text ("Subject: Re: " + current_message.subject)
                null  height 10

                for caption, action, chosen in items:

                    if action:
                        button:
                            action action
                            style "menu_choice_button" 
                            xalign 0.5


                            text caption text_align 0.5

                    else:
                        text caption style "menu_caption"
    else:
        # this is the default choice menu
        window:
            style "menu_window"
            xalign 0.5
            yalign 0.5

            vbox:
                style "menu"
                spacing 2

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True


    style.mailbox_text.font = "ui/Frontier.ttf"
    style.mailbox_button_text.drop_shadow = [(0, 0)]
    style.mailbox_button_text.font = "ui/Frontier.ttf"
#    style.mailbox_button_text.color = "fff"
    style.mailbox_button_text.yoffset=0
    style.mailbox_button_text.antialias = False
    style.mailbox_label_text.font = "ui/Frontier.ttf"
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.button_text.yoffset=1
#    style.menu_choice_button.xminimum = 650

#    style.menu_choice_button.xmaximum = 650

#    style.menu_choice.color = "#312c29"

#    style.menu_choice.size = 22

#    style.menu_choice.yoffset = 3

#    style.menu_choice.font = "bebas.ttf"

#    style.menu_choice.hover_color = "#63584b"

#    style.menu_choice.hover_drop_shadow = None

#    style.menu_choice_button.background = "ui/choice.png"

#    style.menu_choice_button.hover_background = "ui/choice_hover.png"

#    style.menu_choice_button.ymaximum = 73

#    style.menu_choice_button.yminimum = 73

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text" color "F00"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
#encyclopedia inits
init -1 python:
 #Function that creates the buttons for each entry.
 #It makes one button, based on the value "x".
 #Used in a "for loop" on a screen to generate the correct buttons for every entry 
 def generateEntryButton(x):  
  ui.hbox()
  if encyclopaedia.showLockedButtons:
   if encyclopaedia.all_entries[x][1].locked == False: #If the entry is unlocked, make the button to go to it. If it's locked, make an inactive "???" button
    ui.textbutton(encyclopaedia.all_entries[x][1].name, clicked= [ encyclopaedia.ChangeStatus(x), encyclopaedia.SetEntry(x), Show("encyclopaedia_entry")] )
    if encyclopaedia.all_entries[x][1].status == None or encyclopaedia.all_entries[x][1].status == False:
     ui.textbutton ("New!")
          
   else: #If locked entries should be shown in the list, the "???" button should go to the entry. If not, it's an inactive button
    if encyclopaedia.showLockedEntry:
     ui.textbutton("???", clicked=[ encyclopaedia.ChangeStatus(x), encyclopaedia.SetEntry(x), Show("encyclopaedia_entry")])
    else:
     ui.textbutton("???")
    
  if encyclopaedia.showLockedButtons == False: #Only showing unlocked entries in this case, no need for the "???" button
   ui.textbutton(encyclopaedia.unlocked_entries[x][1].name, clicked= [ encyclopaedia.ChangeStatus(x), encyclopaedia.SetEntry(x), Show("encyclopaedia_entry")] )
   if encyclopaedia.unlocked_entries[x][1].status == None or encyclopaedia.unlocked_entries[x][1].status == False:  
    ui.textbutton ("New!")
  ui.close()

##############################################################################
# Encyclopaedia List
#
# Screen that's used to display the list of entries 
screen encyclopaedia_list:
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
    text "FounderPedia"
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     text encyclopaedia.getPercentageUnlocked() + " Unlocked" #Percentage display

   frame:
    style_group "mm_root"  
    xmargin 10
    yfill True
    xmaximum 400
    bottom_margin 10
   
    viewport:
     scrollbars "vertical"
     mousewheel True
     draggable True
     
     vbox: 
      text encyclopaedia.sortingMode xalign 0.5 #Flavour text to display the current sorting mode.
     
      python:
       #If sorting by subject, display the subject heading and add an entry under it if it's the same subject
       if encyclopaedia.sortingMode == "Subject":
        for x in range(len(encyclopaedia.subjects) ):
         ui.text(encyclopaedia.subjects[x])
         for y in range(encyclopaedia.entry_list_size):  
          if encyclopaedia.getEntry(y).subject == encyclopaedia.subjects[x]:
           generateEntryButton(y)   
       
       #If sorting by number, add the number next to the entry
       elif encyclopaedia.sortingMode == "Number":    
        for x in range(encyclopaedia.entry_list_size):
         ui.hbox()
         ui.textbutton (str(encyclopaedia.getEntry(x).number))
         generateEntryButton(x)   
         ui.close()
      
       #If sorting Alphabetically or Reverse-Alphabetically, don't add anything before the entry
       else:
        for x in range(encyclopaedia.entry_list_size):
         generateEntryButton(x) 
    
 frame:
  xalign .98
  yalign .98
  vbox:
#   textbutton "Sort by Number" action [encyclopaedia.Sort(sorting_mode="Number")] #Buttons to sort entries
   textbutton "Sort A to Z" action [encyclopaedia.Sort(sorting_mode="A to Z")]
   textbutton "Sort Z to A" action [encyclopaedia.Sort(sorting_mode="Z to A")]
   textbutton "Sort by Subject" action [encyclopaedia.Sort(sorting_mode="Subject")]
   
   textbutton "Show/Hide Locked Buttons" action [encyclopaedia.ToggleShowLockedButtons()]
#   textbutton "Show/Hide Locked Entry" action [encyclopaedia.ToggleShowLockedEntry()]
   
   textbutton "Return"  action [encyclopaedia.Sort(sorting_mode="Subject"), encyclopaedia.SaveStatus(persistent.new_dict, "new_0"), Return()] #Sorting mode has to be number to save properly. "new_0" needs to be the prefix for the persistent dictionary.
  
##############################################################################
# Encyclopaedia Entry
#
# Screen that's used to display each entry 
screen encyclopaedia_entry:
 tag menu
 
 python: 
  #checkMin and checkMax return Boolean to see if we're at the first or last entry in the encyclopaedia
  cmin = checkMin(encyclopaedia.current_position, 0)
  cmax = checkMax(encyclopaedia.current_position, encyclopaedia.max_size-1)
  sub_cmin = checkMin(encyclopaedia.sub_current_position, 1)
  sub_cmax = checkMax(encyclopaedia.sub_current_position, encyclopaedia.getEntryData()[1].pages)

 window:
  style "gm_root"  

  xfill True
  yfill True
  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    $page_indicator = "0%d : %s" % (encyclopaedia.getEntryData()[1].number, encyclopaedia.getEntryData()[1].getName()) # Flavour text to indicate which page we're current on
    text page_indicator
  
   frame:
    id "entry_nav"
    style_group "mm_root"
    xfill True
    xmargin 10
    hbox:
     xfill True
     textbutton "Previous Entry" xalign .02 action encyclopaedia.PreviousEntry(cmin) #Relative to the sorting mode
     textbutton "Next Entry" xalign .98 action encyclopaedia.NextEntry(cmax) #Relative to the sorting mode  
       
   hbox:
    $ddd = config.screen_width
    $dd = config.screen_width/2
    $pp = config.screen_height/2
    if encyclopaedia.getEntryData()[1].hasImage: #If the entry or sub-entry has an image, add it to the screen   
     frame:
      xmargin 10
      yfill True
      xfill True
      
      xmaximum dd
      ymaximum pp  

      $current_image = encyclopaedia.getEntryData()[1].getImage()
      add current_image crop (0,10,dd-30,pp-10)
   
    window:
     id "entry_window"
     xmargin 10
     xfill True
     yfill True
     xalign 0.5
     xmaximum ddd
     ymaximum pp
     viewport:
      scrollbars "vertical"
      mousewheel True  
      draggable True
      xfill True
      yfill True  
      vbox:
       spacing 15
       for item in entry_text: #entry_text is a list of paragraphs from what whatever the current entry is
        text item

   frame:
    style_group "mm_root"  
    xfill True
    yfill False
    xmargin 10
   
    hbox:
     xfill True  
  
     if encyclopaedia.getEntryData()[1].hasSubEntry: #If there's a sub-entry, add Prev/Next Page buttons     
      textbutton "Previous Page" xalign .02 action encyclopaedia.PreviousPage(sub_cmin)

      text "Page %d / %d" % (encyclopaedia.sub_current_position, encyclopaedia.getEntryData()[1].pages) #Flavour text to indicate which sub-page is being viewed

      textbutton "Next Page" xalign .98 action encyclopaedia.NextPage(sub_cmax)  
 
     else:
      text("")
 
  frame:
   xfill True
   xmargin 10

   yalign .98
   hbox:
    xfill True
    text "Sorting Mode: %s" % (encyclopaedia.sortingMode,) #Flavour text that displays the current sorting mode
    textbutton "Close Entry" id "close_entry_button" xalign .98 clicked [encyclopaedia.ResetSubPage(), Show("encyclopaedia_list")] 

##############################################################################
# Encyclopaedia Button
#
# Contains a button to open the encyclopaedia at any time during the game
screen show_enc_button:
 textbutton "FounderPedia" xalign .82 yalign .00 action ShowMenu("encyclopaedia_list")




screen transitions_pref:
    add "launchsoup.png":
        xpos 424
        ypos 144

screen main_menu:
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/copyright.gif"
        hover "ui/copyright.gif"    
    
    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "ui/founderlifesoup.png"
        hover "ui/launchsoup.png"
        action Start()
        hovered Show("transitions_pref", transition=dissolve)
        unhovered Hide("transitions_pref", transition=dissolve)
        
    imagebutton:
        xpos 210
        ypos 430
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitprefs.png"
        hover "ui/postitprefs2.png"
        action ShowMenu("preferences")


    imagebutton:
        xpos 340
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitload.png"
        hover "ui/postitload2.png"
        action ShowMenu("load")

        
    imagebutton:
        xpos 940
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postithelp.png"
        hover "ui/postithelp2.png"
        action ShowMenu("helpfile")
 
        
    imagebutton:
        xpos 1070
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitquit.png"
        hover "ui/postitquit2.png"
        action Quit(confirm=False)
        
    imagebutton:
        xpos 1070
        ypos 430
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitextras.png"
        hover "ui/postitextras2.png"
        action ShowMenu("extras")



#    imagebutton:
#        xpos 640
#        ypos 700
#        xanchor 0.5
#        yanchor 0.5
#        idle "postitsmall.png"
#        hover "postitsmall.png"
#        action Jump("freewheel")
#        hovered Show("displayTextScreen", displayText = "Sleep") 
#        unhovered Hide("displayTextScreen") 
        
#    imagebutton:
#        xpos 860
#        ypos 545
#        xanchor 0.5
#        yanchor 0.5
#        idle "postitsmall.png"
#        hover "postitsmall.png"
#        action Jump("freewheel")
#        hovered Show("displayTextScreen", displayText = "Music") 
#        unhovered Hide("displayTextScreen") 
        
#    imagebutton:
#        xpos 575
#        ypos 85
#        xanchor 0.5
#        yanchor 0.5
#        idle "postitsmall.png"
#        hover "postitsmall.png"
#        action Jump("freewheel")
#        hovered Show("displayTextScreen", displayText = "Finances") at Position(xpos = 400, ypos=300)
#        unhovered Hide("displayTextScreen") 
  


#    # The main menu buttons.
#    frame:
#        style_group "mm"
#        xalign .98
#        yalign .98

#        has vbox

#        textbutton _("Start Game") action Start()
#        textbutton _("Load Game") action ShowMenu("load")
#        textbutton _("Preferences") action ShowMenu("preferences")
#        textbutton _("Extras") action ShowMenu("extras")
#        textbutton _("Help") action Help()
#        textbutton _("Quit") action Quit(confirm=False)
init -2 python:


    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"
    
    on "hide" action Hide("displayTextScreen")
    
    imagebutton:
        xpos 640
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/copyright.gif"
        hover "ui/copyright.gif"

    imagebutton:
        xpos 640
        ypos 360
        xanchor 0.5
        yanchor 0.5
        idle "ui/founderlifesoup.png"
        hover "ui/founderlifesoup.png"
#        action Start()
        
    imagebutton:
        xpos 210
        ypos 430
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitprefs.png"
        hover "ui/postitprefs2.png"
        action ShowMenu("preferences")


    imagebutton:
        xpos 340
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitload.png"
        hover "ui/postitload2.png"
        action ShowMenu("load")

        
    imagebutton:
        xpos 940
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postithelp.png"
        hover "ui/postithelp2.png"
        action ShowMenu("helpfile")
 
        
    imagebutton:
        xpos 1070
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitquit.png"
        hover "ui/postitquit2.png"
        action Quit(confirm=True)
        
    imagebutton:
        xpos 1070
        ypos 430
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitextras.png"
        hover "ui/postitextras2.png"
        action ShowMenu("extras")
        
    imagebutton:
        xpos 210
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitsave.png"
        hover "ui/postitsave2.png"
        action ShowMenu("save")

    imagebutton:
        xpos 340
        ypos 430
        xanchor 0.5
        yanchor 0.5
        idle "ui/postitback.png"
        hover "ui/postitback2.png"
        action Return()


#    # The various buttons.
#    frame:
#        style_group "gm_nav"
#        xalign .98
#        yalign .98

#        has vbox

#        textbutton _("Return") action Return()
#        textbutton _("Preferences") action ShowMenu("preferences")
#        textbutton _("Save Game") action ShowMenu("save")
#        textbutton _("Load Game") action ShowMenu("load")
#        textbutton _("Main Menu") action MainMenu()
#        textbutton _("Extras") action ShowMenu("extras")
#        textbutton _("Help") action Help()
#        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

#            textbutton _("Previous"):
#                action FilePagePrevious()

#            textbutton _("Auto"):
#                action FilePage("auto")

#            textbutton _("Quick"):
#                action FilePage("quick")

#            for i in range(1, 9):
#                textbutton str(i):
#                    action FilePage(i)

#            textbutton _("Next"):
#                action FilePageNext()

        $ columns = 1
        $ rows = 1

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)
    style.file_picker_nav_button_text.drop_shadow = [(0, 0)]
#    style.file_picker_nav_button_text.font = "ui/Comfortaa-Light.ttf"

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
#    style.file_picker_text.font = "ui/Comfortaa-Light.ttf"
    style.file_picker_text.drop_shadow = [(0, 0)]


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
