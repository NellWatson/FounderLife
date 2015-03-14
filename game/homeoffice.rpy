init python:
    
    class Item:
        hover_image = None
        selected = False
        def __init__(self, name,image_name):
            self.name = name
            self.image_name = image_name
            self.hover_image = im.Composite((100, 100),
                                        (0, 0), "yellow.png",
                                        (0, 0), image_name)
            self.selected_image = im.Composite((100, 100),
                                        (0, 0), "red.png",
                                        (0, 0), image_name)
        def __eq__(self, other):
            return self.name == other.name
                                        

    #iMatch = Item("Match","match.png")
    #iFirewood = Item("Firewood","wood.png")
    #iFish = Item("Fish","herring_item.png")
              
    class testItem(Action):

        def __init__(self, item, switch, value, remove = True):
            self.item = item
            self.switch = switch
            self.value = value
            self.remove = remove
        
        def __call__(self):
            if store.active_item != None and store.active_item == self.item:
                setattr(store, self.switch, self.value)
                if self.remove:
                    store.inventory.remove(self.item)
                    store.active_item = None
            renpy.restart_interaction()


            
    class addItem(Action):

        def __init__(self, item):
            self.item = item
        
        def __call__(self):
            store.inventory.append(self.item)
            renpy.restart_interaction()
            
            
    class selectItem(Action):

        def __init__(self, object):
            self.object = object
        
        def __call__(self):
            new_value = not self.object.selected
            for item in store.inventory:
                setattr(item, "selected", False)
            store.active_item = None
            setattr(self.object, "selected", new_value)
            if (new_value):
                store.active_item = self.object
            renpy.restart_interaction()

        def get_selected(self):
            return self.object.selected


            
init python:
    def inventory_dragged(drags, drop):

        if not drop:
            return

        return True

screen displayTextScreen:  
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText

label homeoffice:
    call weather
    $ myClock.set_time(8,00)
    scene homeoffice with dissolve
    show screen calendar
    show screen clock_screen
    play music ["music/etherdisco.mp3", "music/stringeddisco.mp3", "music/aureacarmina.mp3", "music/discocontutti.mp3", "music/overcast.mp3", "music/presenterator.mp3" ] loop
#    call createlog
#    $ log.keyon()
#    $ log.assign("Settling In")
#    show screen tracker
    $ first_visit = { }
    $ first_visit['yellow'] = True
    $ first_visit['blue'] = True
    $ first_visit['green'] = True
    pause(1)
if nellwatsoneegg:
    pov "Hi!"
    n "Wh-whaaat?"
else:
    n "Now, it's time to settle in." with dissolve
    n "You have a PDA with which to organise your life, tolerable internet connection, and a warm and comfy environment."
    n "Along with your passion, drive, and determination, you have everything you need to begin."
#if playedbefore:
#    jump freewheel
if nellwatsoneegg:
    n "Uhhhh. Uh, Hi, uhhh, 'Nell'!"
    n "Uhh. Right, right. Ok..."
    n "So."
    pass
else:
    n "On your trusty PDA you can check your email, or buy stuff from ValkyriePrime."
    n "Take a walk and GOOB (Get out of the building), or Reflect out the window."
    n "You can also change your appearance in the closet, or read through some reference docs (FounderPedia) on the PDA (top-right corner)."
    n "Finally, notice that you're on the clock! Every action you take has a time consequence. So does just standing still."
#    $ playedbefore = True
    n "By the way, you can hit the 'F' key to switch between window and fullscreen."
    n  "From here on out, you're in full command."
if nellwatsoneegg:
    n "From here on out, you're in full command."
    n "I mean me."
    n "Well, no, rather YOU." 
    n "Uhhh... just... let's just play the game Ok? Jeeze..."
    $ add_now()
    pov "Let's take a look around!"
    n "Oh, {u}do{/u} shut up!"
    $ add_later("Mental Care Request", "Dr Nick", "Dear Nell,\n\nI read with much concern your message about 'hearing voices'.\n\nGiving oneself commands sounds like an admittedly disturbing development.\n\nI'm sorry to say this, but you may have developed signs of schizophrenia. The 'penchant for giving inane and unwanted advice' to yourself suggests some form of self-referential bicameralism, frequently experienced by mystics and such, who may act on orders from a 'higher power'.\n\nPlease get lots of rest, and try not to obey the voices if they suggest doing things that you know to be unwise or immoral.\n\nTake care Nell,\n\n\nDr. Nick\n\nP.S. - I keep a small supply of thorazine at my office if required...")
else:
    n "I'll be around, with tips to share as you progress."
    n "I'll lurk about, in the bottom right corner."
    n "Just click on me for help, and I can give you general advice on most situations you'll encounter."
    n "You don't need to listen to me, but my take on things is usually correct (I programmed it that way)!"
    $ add_now()
    pause 1.0
    hide screen mailbox_overlay
    n "My first suggestion is to check your F-mail on the computer..."
    show nell happy:
        ease 0.0 xalign 0.0, yalign 1.0
        ease 1.0 xalign 1.0
        pause 0.3
        easeout 1.0 yalign 1.5
    pause 2.5
    pov "Let's take a look around!" with dissolve
    hide pov with dissolve
    $ log.keyon()
#    $ log.assign("Attend Your First Meetup")

label freewheel:
    $ log.keyon()
    $ location = "bedroom"
    $ renpy.block_rollback()
    
    hide screen mailbox_overlay
    hide screen show_enc_button
    scene homeoffice
    show screen calendar
    show screen clock_screen
    with dissolve
    $renpy.transition(dissolve)
    call screen lookaroundhomeoffice

#    show im.MatrixColor(bg homeoffice, im.matrix.desaturate() * im.matrix.tint(0.6, 0.6, 1.0)) # pic is the supplied argument.  
#    $ myClock.set_time(3,00)
#    $ myClock.add_time(0,10)    
#    $ myClock.add_time(0,10)
#    $ myClock.autoclock_run(True)
#    $ myClock.autoclock_run(False)
#    $ myClock.realclock_run(True)
#    "So the real time clock is running now. Again, you have to wait a bit to see it change."
#    $ myClock.realclock_run(False)
#    "Okay...now I'm going to turn off the clock completely."


$renpy.transition(dissolve)    
screen lookaroundhomeoffice: 
    on "hide" action Hide("displayTextScreen")
#    imagebutton:
#        xpos 855
#        ypos 350
#        xanchor 0.5
#        yanchor 0.5
#        idle "ui/yellow2.png"
#        hover "ui/yellow.png"
#        action Jump("desktop")
#        hovered Show("displayTextScreen", displayText = "Use the computer") 
#        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 300
        ypos 330
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("dressup")
        hovered Show("displayTextScreen", displayText = "Change appearance") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 210
        ypos 570
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("lounge")
        hovered Show("displayTextScreen", displayText = "Lounge") 
        unhovered Hide("displayTextScreen") 
        
#    imagebutton:
#        xpos 580
#        ypos 400
#        xanchor 0.5
#        yanchor 0.5
#        idle "ui/yellow2.png"
#        hover "ui/yellow.png"
#        action Jump("home")
#        hovered Show("displayTextScreen", displayText = "Set Schedule") 
#        unhovered Hide("displayTextScreen") 

    imagebutton:
        xpos 780
        ypos 560
        xanchor 0.5
        yanchor 0.5
        idle "ui/yellow2.png"
        hover "ui/yellow.png"
        action Jump("bed")
        hovered Show("displayTextScreen", displayText = "Bed") 
        unhovered Hide("displayTextScreen") 
        
        
        
    imagebutton:
        xpos 1200
        ypos 50
        xanchor 0.5
        yanchor 0.5
        idle "ui/empty.png"
        hover "ui/pda.png"
        insensitive "ui/empty.png"
        #action
        action Jump("desktop")
        hovered Show("displayTextScreen", displayText = "PDA") 
        unhovered Hide("displayTextScreen") 
        
    imagebutton:
        xpos 1200
        ypos 700
        xanchor 0.5
        yanchor 0.5
        idle "ui/empty.png"
        hover "happy nell small.png"
        insensitive "ui/empty.png"
        #action
        action Jump("nelltip")
        hovered Show("displayTextScreen", displayText = "Nell") 
        unhovered Hide("displayTextScreen")