screen helpfile:

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
    text "Founder Life Help" xalign 0.5
    

   frame:
    style_group "mm_root"  
    xmargin 10
    xfill True
    yfill True
    bottom_margin 60
   
    viewport:
     scrollbars "vertical"
     mousewheel True
     draggable True
     
     vbox: 
        box_wrap True
        vbox:
            text "\n{b}{space=10}Basic Help{/b}"
            text "{space=10}To advance through the game, left-click or press the space or enter keys. When {space=10}at a menu, left-click to make a choice, or use the arrow keys to select a choice and {space=10}enter to activate it."


            text "\n\n{b}{space=10}Game Menu{/b}"

            text "{space=10}When playing a game, right-click or press the escape key to enter the game menu. {space=10}The game menu gives the following choices:"

            text "\n{b}{size=-5}{space=30}Return{/size}{/b}"
            text "{size=-5}{space=30}Returns to the game.{/size}"
            text "\n{b}{size=-5}{space=30}Save Game{/size}{/b}"
            text "{size=-5}{space=30}Allows you to save a game by clicking on the single save slot.{/size}"
            text "\n{b}{size=-5}{space=30}Load Game{/size}{/b}"
            text "{size=-5}{space=30}Allows you to load a game by clicking on the single slot.{/size}"
            text "\n{b}{size=-5}{space=30}Preferences{/size}{/b}"
            text "{size=-5}{space=30}Changes the game preferences (options/configuration):{/size}"
            text "\n{b}{size=-10}{space=60}Display{/size}{/b}"
            text "{size=-10}{space=60}Switches between fullscreen and windowed mode.{/size}"
            text "\n{b}{size=-10}{space=60}Transitions{/size}{/b}"
            text "{size=-10}{space=60}Controls the display of transitions between game screens.{/size}"
            text "\n{b}{size=-10}{space=60}Text Speed{/size}{/b}"
            text "{size=-10}{space=60}Controls the rate at which text displays. The further to the right this slider is, the faster the text will display. All the {space=60}way to the right causes text to be shown instantly.{/size}"
            text "\n{b}{size=-10}{space=60}Joystick{/size}{/b}"
            text "{size=-10}{space=60}Lets you control the game using a joystick.{/size}"
            text "\n{b}{size=-10}{space=60}Skip{/size}{/b}"
            text "{size=-10}{space=60}Chooses between skipping messages that have been already seen (in any play through the game), and skipping all {space=60}messages.{/size}"
            text "\n{b}{size=-10}{space=60}Begin Skipping{/size}{/b}"
            text "{size=-10}{space=60}Returns to the game, while skipping.{/size}"
            text "\n{b}{size=-10}{space=60}After Choices{/size}{/b}"
            text "{size=-10}{space=60}Controls if skipping stops upon reaching a menu.{/size}"
            text "\n{b}{size=-10}{space=60}Auto-Forward Time{/size}{/b}"
            text "{size=-10}{space=60}Controls automatic advance. The further to the left this slider is, the shorter the amount of time before the game {space=60}advances. All the way to the right means text will never auto-forward.{/size}"
            text "\n{b}{size=-10}{space=60}Music, Sound, and Voice Volume{/size}{/b}"
            text "{size=-10}{space=60}Controls the volume of the Music, Sound effect, and Voice channels, respectively. The further to the right these are, {space=60}the louder the volume.{/size}"
            text "\n{b}{size=-5}{space=30}Main Menu{/size}{/b}"
            text "{size=-5}{space=30}Returns to the main menu, ending the current game.{/size}"
            text "\n{b}{size=-5}{space=30}Extras{/size}{/b}"
            text "{size=-5}{space=30}Enables a quick reference to contacts, music, and FounderPedia content{/size}"
            text "\n{b}{size=-5}{/size}{space=30}Help{/b}"
            text "{size=-5}{space=30}Shows this help screen.{/size}"
            text "\n{b}{size=-5}{/size}{space=30}Quit{/b}"
            text "{size=-5}{space=30}Exits the game; the game will be closed and ended.{/size}"
            
            text "\n\n{b}{space=10}Key and Mouse Bindings{/b}"
            text "\n{b}{size=-5}{space=30}Left-click, Enter{/size}{/b}"
            text "{size=-5}{space=30}Advances through the game, activates menu choices, buttons, and sliders.{/size}"
            text "\n{b}{size=-5}{space=30}Space{/size}{/b}"
            text "{size=-5}{space=30}Advances through the game, but does not activate choices.{/size}"
            text "\n{b}{size=-5}{space=30}Arrow Keys{/size}{/b}"
            text "{size=-5}{space=30}Selects menu choices, buttons, and sliders.{/size}"
            text "\n{b}{size=-5}{space=30}Ctrl{/size}{/b}"
            text "{size=-5}{space=30}Causes skipping to occur while the ctrl key is held down.{/size}"
            text "\n{b}{size=-5}{space=30}Tab{/size}{/b}"
            text "{size=-5}{space=30}Toggles skipping, causing it to occur until tab is pressed again.{/size}"
            text "\n{b}{size=-5}{space=30}Mousewheel-Up, PageUp{/b}{/size}"
            text "{size=-5}{space=30}Causes rollback to occur. Rollback reverses the game back in time, showing prior text and even {space=30}allowing menu choices to be changed.{/size}"
            text "\n{b}{size=-5}{space=30}Mousewheel-Down, PageDown{/size}{/b}"
            text "{size=-5}{space=30}Causes rollforward to occur, cancelling out a previous rollback.{/size}"
            text "\n{b}{size=-5}{space=30}Right-click, Escape{/size}{/b}"
            text "{size=-5}{space=30}Enters the game menu. When in the game menu, returns to the game.{/size}"
            text "\n{b}{size=-5}{space=30}Middle-click, H{/size}{/b}"
            text "{size=-5}{space=30}Hides the text window and other transient displays.{/size}"
            text "\n{b}{size=-5}{space=30}F{/size}{/b}"
            text "{size=-5}{space=30}Toggles fullscreen mode{/size}"
            text "\n{b}{size=-5}{space=30}S{/size}{/b}"
            text "{size=-5}{space=30}Takes a screenshot, saving it in a file named {i}screenshot****.png{/i}, where {i}****{/i} is a serial number.{/size}"
            text "\n{b}{size=-5}{space=30}Alt-M, Command-H{/size}{/b}"
            text "{size=-5}{space=30}Hides (iconifies) the window.{/size}"
            text "\n{b}{size=-5}{space=30}Alt-F4, Command-Q{/size}{/b}"
            text "{size=-5}{space=30}Quits the game.{/size}"
            text "\n{b}{size=-5}{space=30}Delete{/size}{/b}"
            text "{size=-5}{space=30}When a save slot is selected, deletes that save slot.{/size}"
#            text "\n{b}{size=-5}{space=30}P{/size}{/b}"
#            text "{size=-5}{space=30}Brings up the PDA (your in-game smart device){/size}"
            text "\n{b}{size=-5}{space=30}Q{/size}{/b}"
            text "{size=-5}{space=30}Brings up the Questlog (your in-game to-do list){/size}"
            text "\n\n{b}{space=10}Legal Notice{/b}"
            text "{size=-5}{space=10}This game uses source code from a number of open source projects. For a list, and a location {space=10}where source code may be downloaded, please visit {a=http://renpy.org/wiki/renpy/License}www.renpy.org/wiki/renpy/License{/a}{/size}"

 frame:
  xmargin 10
  yalign .98
  vbox:
   textbutton _("Return") action Return()

init python:
    #This controls minimum button length
    style.helpfile = Style(style.frame)
    style.helpfile_button.xmaximum = 200
    style.helpfile_button.xminimum = 200
    style.helpfile_button.yminimum = 55