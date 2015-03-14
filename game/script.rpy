# You can place the script of your game in this file.
# 


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


# event.step() is a function that returns true while there are
# still events that need to be executed.

#while event.step():
#    pass

#headbob#
#scene woods at Pan((700, 0), (1000,0), 2.0, repeat=True, bounce=True, time_warp=None) with fade



#codebits
#jump imagemap random
#action Jump(renpy.random.choice(["event1", "event2", "event3"]))
#jump label random
#jump expression renpy.random.choice(["doors1", "doors2"])

#drop_shadow = [(1, 1)]





# Screen-Centering code

init 9999 python:
    wk = Character(None, kind = centered, what_color = "#003C78", what_outlines = [(3, "#FFFFFF", 0, 0)], what_bold = True, what_size = 34)

$ credit = Character("", what_size=44, what_suffix="{fast}{w=5}{nw}", window_yalign=1.0, window_xalign=0, window_left_padding=30, window_background=None, what_color="#000", what_drop_shadow_color=((0,0,0,64)))




#image cache
init python:
    renpy.cache_pin("ui/crate.jpg")
    renpy.cache_pin("ui/founderlifesoup.jpg")
    renpy.cache_pin("ui/launchsoup.jpg")
    renpy.cache_pin("ui/postitquit.jpg")
    renpy.cache_pin("ui/postitquit2.jpg")
    renpy.cache_pin("ui/postitsave.jpg")
    renpy.cache_pin("ui/postitsave2.jpg")
    renpy.cache_pin("ui/postitprefs.jpg")
    renpy.cache_pin("ui/postitprefs2.jpg")
    renpy.cache_pin("ui/postitback.jpg")
    renpy.cache_pin("ui/postitback2.jpg")
    renpy.cache_pin("ui/postitextras.jpg")
    renpy.cache_pin("ui/postitextras2.jpg")
    renpy.cache_pin("ui/postithelp.jpg")
    renpy.cache_pin("ui/postithelp2.jpg")
    renpy.cache_pin("ui/postitload.jpg")
    renpy.cache_pin("ui/postitload2.jpg")



#screencentering on bootup
init python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
#Renpy-Safe-Logger Version 2.7 by 'jghibiki'
init:
    python:
        import logger

#defining show positisions
init:
    $ midleft = Position(xpos=0.1, xanchor='left')

#Shake Code
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #
init:    
    $ sshake = Shake((0, 0, 0, 0), 3.0, dist=02)
#

init python:
    credits = ('Code and Design', 'Eleanor \'Nell\' Watson'), ('Additional Writing', 'Victoria Davies'), ('Music', 'Kevin MacLeod (Incompetech.com)'), ('Ren\'Py Framework', 'Tom \'Pytom\' Rothamel'), ('Code Contributors', 'Steam Girl (Character Stats)\nSusan The Cat (Jigsaw, Interaction)\nLeon (Character Costumes, Credits)\nTrooper6 (Clock)\nSaguaro (Clock)\nRabcor (Credits)\nUnin (Pirouetting CTC Triangle)\nDaikiraikimi (Scheduler)\nAlex (Jigsaw, Slide Puzzle, Randomiser)\nCounter Arts (Rising Vortex)\nLiude (Key Lookup)\nJw2pfd (QuestLog)\nJghibiki (Safe Logger)\nHuman Bolt Diary (Bestiary)\nPowerofvoid (Node-based Navigation)'), ('Art Contributors', 'Taxcredits.com (Job Classifieds)\nEnrique Flouret (Wood Crate Texture)\nJohan Aakerlund (Comfortaa Typeface)\nMike Cook (Frontier Font TTF 2.0 - after David Braben)\nPpppantsu (Geometric Dialogue Boxes)\nFreedesignfile (Spacious Bright Room)\nRidge Resorts (Meeting)\nWikimedia Commons (Post-It, Achievement Star, Grave)\nJohann Mynhardt (Clouds Stock Footage)\nFredericorama (PDA Icon set)\nRedkid.net (Soup Bowl Generator)\nSuperRaptor1 (Desktop Background)', 'Patrick Hoesly (Lounge, Co-working space)', 'Iain Watson (Couch Potato)'), ('Soundtrack by Kevin MacLeod (Incompetech.com)', '\"Who Likes to Party\"\n\"Ether Disco\"\n\"Stringed Disco\"\n\"Overcast\"\n\"Disco con Tutti\"\n\"Aurea Carmina\"\n\"Electrodoodle\"\n\"Our Story Begins\"\n\"Rising Game (Intro)\"\n\"Presenterator\"'), ('Inspiration and Shout-outs', 'Wing Commander Privateer (Chris Roberts & Origin)\nFrontier: Elite II (David Braben, Chris Sawyer)\nSystem Shock (Warren Spector & Looking Glass Studios)\nUplink (Chris, Tom, & Mark at Introversion Software)\nQuandaries (Bob Bates & Legend)\nSpycraft: The Great Game (Ken Berris & Activision)\nPrincess Maker II (Gainax & Softegg)\nDepression Quest (Zoe Quinn et al)\nDigital: A Love Story (Christine Love)\nStudio MugenJohnCel Oeuvre (Uncle Mugen)'), ('Testers', 'Amine Bouhaji\nPablo Valcárcel'), ('Made whilst listening to', 'Brothers in Arms - Dire Straights')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Made in {/s}{size=60}Python{/s}{size=40} with {/s}{size=60}PyGame{/s} and {size=60}\n" + renpy.version()
#    show screen credit("credits auteur","Histoire et textes : Korova\n\nsous licence\nCreative Commons\n{image=cc/Cc-by.png} {image=cc/Cc-sa.png}  {a=http://creativecommons.org/licenses/by-sa/2.0/fr/} CC-BY-SA{/a}")

#spinning ctc
init python:

    class spinningCTC(renpy.Displayable):
        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
# initiate variables
            self.xvar = 11
            self.yvar = 3


        def render(self, width, height, st, at):
#provides values by which to vary the X and Y coordinates of triangle's top two points
#this provides the 3D pirouetting illusion
#these values change every tenth of a second, and the whole thing loops after 1 second
            if st % 1 <= 0.2:
                self.xvar = 11
                self.yvar = 0
            elif st % 1 <= 0.3:
                self.xvar = 9
                self.yvar = 1
            elif st % 1 <= 0.4:
                self.xvar = 6
                self.yvar = 1
            elif st % 1 <= 0.5:
                self.xvar = 3
                self.yvar = 2
            elif st % 1 <= 0.6:
                self.xvar = 0
                self.yvar = 2
            elif st % 1 <= 0.7:
                self.xvar = -3
                self.yvar = 2
            elif st % 1 <= 0.8:
                self.xvar = -6
                self.yvar = 1
            elif st % 1 <= 0.9:
                self.xvar = -9
                self.yvar = 1
            elif st % 1 <= 1.0:
                self.xvar = -11
                self.yvar = 0



            render = renpy.Render(31, 23)
#set the size of the render
            canvas = render.canvas()
            canvas.polygon("000000", [(19-self.xvar,2+self.yvar), (19+self.xvar,2-self.yvar), (19,22)], 0)
#draw ctc indicator triangle shadow
            canvas.polygon("FFFFFF", [(16-self.xvar,2+self.yvar), (16+self.xvar,2-self.yvar), (16,22)], 0)
# draw ctc indicator triangle
            renpy.redraw(self, 0.1) #redraw the displayable ever tenth of a second to show animation
            return render

init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))

init python:
    
    import smtplib
    
    def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
#              login, password,
              smtpserver='aspmx.l.google.com:25'):
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
 
        server = smtplib.SMTP(smtpserver)
#        server.starttls()
#        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        return problems




#jigsawpuzzle
init python:

    def piece_dragged(drags, drop):


        if not drop:

            return



        p_x = drags[0].drag_name[0]

        p_y = drags[0].drag_name[1]

        t_x = drop.drag_name[0]

        t_y = drop.drag_name[1]

        

        a = []

        a.append(drop.drag_joined)

        a.append((drags[0], 3, 3))

        drop.drag_joined(a)

        

        if p_x == t_x and p_y == t_y:

            renpy.music.play("puzzle_pieces/Pat.mp3", channel="sound")

            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset

            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset

            drags[0].snap(my_x,my_y, delay=0.1)

            drags[0].draggable = False

            placedlist[int(p_x),int(p_y)] = True

            for i in range(0, grid_width):

                for j in range(0, grid_height):

                    if placedlist[i,j] == False:

                        return

            return True

        return
        

screen jigsaw:


    key "rollback" action [[]]

    key "rollforward" action [[]]

    add im.Scale("_puzzle_field.png", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset)
    
    draggroup:

        for i in range(0, grid_width):

            for j in range(0, grid_height):

                $ name = "%s%s"%(i,j)

                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset

                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset

                drag:

                    drag_name name

                    child im.Scale("_blank_space.png", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )

                    draggable False

                    xpos my_x ypos my_y
            

        for i in range(0, grid_width):

            for j in range(0, grid_height):

                $ name = "%s%s piece"%(i,j)

                drag:

                    drag_name name

                    child imagelist[i,j]

                    #droppable False

                    dragged piece_dragged

                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]



init:
    #This makes a clock and sets it to 8:00am
    $ myClock = Clock(75, "clockBase", "clockHour", "clockMin", 8, 0)

# UDD's as far as I can tell, need to be added to something (a screen, a vbox, a frame, etc)...so here I'm making
# a screen to add the clock to. I want the clock all in the center!
screen clock_screen:
    add myClock:
        xalign 0.17
        yalign 0.01


# screen time_overlay:
#   $ minutes = time_in_minutes % 60
#   $ hours = (time_in_minutes / 60) % 24 
#   text ("%d:%02d" % (hours, minutes)) pos (698, 24)



init:
   
    image bg logo = "logo.jpg"
    image bg main_menu = "titlescreen.png"
    image bg info = "info.png"
    image bg desk = "desk.jpg"
    image bg empty = "empty.png"
    image cg1 = "cg01.jpg"
    image cg2 = "cg02.jpg"
    image cg3 = "cg03.jpg"
    image cg4 = "cg04.jpg"
    image cg5 = "cg05.jpg"
    image cg6 = "cg06.jpg"
    image cg7 = "cg07.jpg"
    image cg8 = "cg08.jpg"
    image cg9 = "cg09.jpg"
    image cg10 = "cg10.jpg"
    image cg11 = "cg11.jpg"
    
# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
#label splashscreen:
#    show bg black
#    $ renpy.pause(0)
#    show bg logo
#    with dissolve
#    with Pause (1.5)
#    
#    show bg main_menu
#    with fade
#    with Pause(1.5)
#    
#    return    
    #    OkCupid addon for desktop
    $ KOErosP = Position(xpos=975, ypos=635)    





#image ctc_blink:
#       "arrow.png"
#       subpixel True
#       linear 0.75 alpha 1.0
#       linear 0.75 alpha 0.0
#       repeat


#weather effects
image rain:
    "rain1.png"
    0.14
    "rain2.png"
    0.13
    "rain3.png"
    0.11
    "rain4.png"
    0.12
    "rain2.png"
    0.15
    "rain1.png"
    0.1
    "rain4.png"
    0.11
    "rain3.png"
    0.12
    repeat

image lightning:
        choice 1.5:
            "lightning.png"
        choice:
            "lightning2.png"
        choice:
            "lightning3.png"
            
            
image overcast = "overcast.png"


transform withAdd:
        additive 1.0
image snowstorm = SnowBlossom(At("snowflake.png", withAdd), border=150, count=6000,start=0.00000000001, fast=False, yspeed=(60, 120), xspeed=(-300,300), horizontal=True) 

image sakura filmstrip = anim.Filmstrip("dollar.png", (20, 20), (2, 1), .15)
#image snowblossom = SnowBlossom("sakura filmstrip")
image snow = Snow("dollar.png")
image heart = "heart.png"
image sad = "sad.png"
image depressed = "depressed.png"
image bg circleiris = "id_circleiris.png"
image anon = "anon.png"
image bg mmenu = "challengemenu.png"
image bg gmenu = "graphpaper.png"
image bg crossroads:
    "crossroads.jpg"
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.50
    0.5
    easein 6.0 zoom 1.3 xalign 0.3 yalign 0.5
image bg graduationcaps:
    "graduationcaps.jpg"
    subpixel True
    zoom 4.0 xalign 0.3 yalign 0.12
    1.5
    easein 4.0 zoom 1.0 xalign 0.5 yalign 0.5
image bg handflick:
    "handflick.jpg"
    subpixel True
    zoom 3.5 xalign 0.65 yalign 0.50
    0.5
    easein 6.0 zoom 0.5 xalign 0.5 yalign 0.5
image bg taxcredits:
    "taxcredits.jpg"
    subpixel True
    zoom 2.5 xalign 0.45 yalign 0.45
    1.5
    easein 6.0 zoom 0.3 xalign 0.5 yalign 0.5
image bg watchingtv:    
    "watchingtv.jpg"
    subpixel True
    zoom 3.5 xalign 0.55 yalign 0.53
    0.5
    easein 6.0 zoom 0.5 xalign 0.5 yalign 0.5
    
image bg grave:    
    "grave.jpg"
    subpixel True
    zoom 1.5 xalign 0.40 yalign 0.55
    0.5
    easein 6.0 zoom 0.3 xalign 0.5 yalign 0.5

image bg successfailure:    
    "successfailure.jpg"
    subpixel True
    zoom 3.0 xalign 0.63 yalign 0.27
    0.5
    ease 6.0 zoom 0.5 xalign 0.5 yalign 0.5

image bg exuberance:    
    "exuberance.jpg"
    subpixel True
    zoom 3.5 xalign 0.50 yalign 0.58
    0.5
    easein 6.0 zoom 0.3 xalign 0.5 yalign 0.5


image founderbg = "founderbg.png"
    
image bg gym = "gym.jpg"
image bg stockvaultfitnesscenter ="stockvaultfitnesscenter.jpg"
image bg lounge = "lounge.jpg"
image bg boardroom = "boardroom.jpg"
image bg meetup = "meetup.jpg"
image bg bathroom = "bathroom.jpg"
image bg kitchen = "kitchen.jpg"
image bg fridge = "fridge.jpg"
image bg valkyrie = "valkyrie.jpg"
image bg supermarket = "supermarket.jpg"

image bg woods = "bg art.jpg"
image homeoffice = ConditionSwitch(
        "povmood <= 25", ImageReference ("homeoffice depressed"),
        "povmood <= 50", ImageReference ("homeoffice sad"),
        "healthy <= 25", ImageReference ("homeoffice diseased"),
        "healthy <= 50", ImageReference ("homeoffice sick"),
        "intoxicated >= 50", ImageReference ("homeoffice drunk"),
        "energy <= 25", ImageReference ("homeoffice tired"),
        "True", "homeoffice.jpg",
        )
image homeoffice sad = im.MatrixColor("homeoffice.jpg", im.matrix.saturation(0.5)*im.matrix.tint(.94,.94,.92)*im.matrix.brightness(-0.00))
image homeoffice depressed = im.MatrixColor("homeoffice.jpg", im.matrix.saturation(0.3)*im.matrix.tint(.86,.86,.88)*im.matrix.brightness(-0.00))
image homeoffice sick = im.MatrixColor("homeoffice.jpg", im.matrix.tint(.90,1,.90)*im.matrix.brightness(-0.00))
image homeoffice tired = im.MatrixColor("homeoffice.jpg", im.matrix.tint(1,1,1)*im.matrix.brightness(-0.30))
image homeoffice diseased: 
    contains:
        im.MatrixColor("homeoffice.jpg", im.matrix.tint(.80,1,.80)*im.matrix.brightness(-0.00))
        alpha 1.0
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate 0.5 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate -0.5 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate 1 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate -1 xalign 0.5 yalign 0.5
image homeoffice drunk:
    contains:
        "homeoffice.jpg"
        alpha 1.0
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate 0.5 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate -0.5 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate 1 xalign 0.5 yalign 0.5
    contains:
        "homeoffice.jpg"
        alpha 0.2 rotate -1 xalign 0.5 yalign 0.5
image bg townmap = "townmap.png"
image bg desktopblank ="Desktopblank.jpg"
image bg desktop = "Desktop.png"
image bg founder = "Founder.jpg"
image bg stevejobs = "stevejobs.jpg"
image bg stevedossier = "dossier.gif"
image bg white = Solid("#fff")
image nell happy = "happy nell.png"
image bg pink = "#ffb3b3"
image bg green = "#c3ffb1"
image bg yellow = "#fbffb7"
image bg blue = "#b1e3ff"
image vicneutral = "vicneutral.png"
#image naomi neutral = "naomi neutral.png"
#image naomi sad = "naomi sad.png"
#Achievements
image achieve1 = "achievestar1.png"

transform achieveanim:
    xalign 0.235  yalign 0.02 alpha 0.0
    easeout 0.5 alpha 1.0
    2.5 # Pause
    linear 3.0 alpha 0.0

transform achieveanimtext:
    xalign 0.335  yalign 0.035 alpha 0.0
    easeout 0.5 alpha 1.0
    2.5 # Pause
    linear 3.0 alpha 0.0


image movie = Movie(size=(1280,720), xpos=0, ypos=0, xanchor=0, yanchor=0)
#image movie = Movie(size=(320,240), xpos=475, ypos=50, xanchor=0, yanchor=0)
# Declare characters used by this game.
define pov = Character('[povname]', color="#81aeef", ctc = spinningCTC(), show_side_image=DynamicDisplayable(draw_char_side), window_background=Frame("ui/dialogboxblue.png", 6, 6), window_right_padding=45, window_top_padding=5, window_left_padding=180)
define n = Character('Nell Watson', color="#c14c52", ctc = spinningCTC(), show_side_image=ConditionSwitch('nellmood==0', 'nell neutral', 'nellmood==1', 'nell happy', 'nellmood==2', 'nell sad', xalign=0.0, yalign=1.0), window_background=Frame("ui/dialogboxred.png", 6, 6), window_right_padding=45, window_top_padding=5, window_left_padding=180) #adjust the left padding for your character size
define victoria = Character('Victoria Davies', color="#81aeef", ctc = spinningCTC(), show_side_image=DynamicDisplayable(draw_vicneutral_side), window_background=Frame("ui/dialogboxlightblue.png", 6, 6), window_right_padding=45, window_top_padding=5, window_left_padding=180)
define matt = Character('Matt Dippl', color="#81aeef", ctc = spinningCTC(), show_side_image=DynamicDisplayable(draw_mattdippl_side), window_background=Frame("ui/dialogboxyellow.png", 6, 6), window_right_padding=45, window_top_padding=5, window_left_padding=180)
define t = Character('Tom', color="#c8ffc8")
define e = Character('', color="#c8ffc8")
define cheapgymass = Character('FFF Assistant', color="#c8ffc8")
define fancygymass = Character('FL Fitness Assistant', color="#c8ffc8")
define pe = Character('Peter', color="#b62a2a")
define pa = Character('Paul', color="#bc9502")
define m = Character('Mary', color="#836cd0")
define anon = Character('[contact_to_show]', color="#81aeef", ctc = spinningCTC(), show_side_image=DynamicDisplayable(draw_anon_side), window_background=Frame("dialogboxblue.png", 6, 6), window_right_padding=45, window_top_padding=5, window_left_padding=180)

define numbers = "0123456789"



# The game starts here.
label start:

    call createlog


#clear_game_timer
#if player.energy > player.max_energy: # can't increase energy beyond max energy
 #                   player.energy = player.max_energy


    #NewLogInstance
    $FLLogger = logger.Logger(_config.gamedir + "\\logs\\FLLogger.log")

    call initialize_room_screen


    #Scheduler
    $ month = 0
    
    #$ _game_menu_screen = "game_menu" # This code activates the "pause menu" in screens.rpy
    $ calendar = Calendar(1, 1, 2014, 2016) # Calendar(day, month, year, first leap year (can be ignored))
    $ month_cnt = 0
    $ current_week = "None"

    $ AGI = 0 #Agility
    $ APP = 0 #Appearance
    $ BLD = 0 #Build
    $ FIT = 0 #Fitness
    $ CRE = 0 #Creativity
    $ INF = 0 #Influence
    $ KNO = 0 #Knowledge
    $ PSY = 0 #Psyche
    $ PER = 0 #Perception
    $ WIL = 0 #Willpower
    
    $ stress = 100
    $ money = 500
    $ energy = 100
    $ povmood = 100
    
    #Imagedissolve Transitions.
    $ circleirisout = ImageDissolve("id_circleiris.png", 1.0, 8)
    $ circleirisin = ImageDissolve("id_circleiris.png", 1.0, 8, reverse=True)


    #Flag Inits
    $ persistent.playedbefore = False
    $ createdafounder = False
    $ fmailintroduced = 0
  
    #CharacterHistory Inits
    $ male = False
    $ female = False
    $ othergender = False  
        
    $ ageunder18 = False
    $ age19to24 = False
    $ age25to29 = False
    $ age30to35 = False
    $ age36to45 = False
    $ age46to60 = False
    $ ageover61 = False
        
    $ childhoodgood = False
    $ childhoodneutral = False
    $ childhoodbad = False
                
    $ queer = True
        
    $ gay = False
    $ bi = False
    $ asexual = False
    $ othersexuality = False
    $ straight = False
        
    $ transgendered = False
    $ intersex = False
    $ genderqueer = False
    $ cisgender = False
        
    $ minority = False
        
    $ education = 0
        
    $ disability = 0

    $ health = 0
    
    $ cancode = 0
    $ canwords = 0
    $ candraw = 0
    
    #Virtues
    $ fiscal = 50
    $ autonomy = 50
    $ just = 50
    $ patience = 50
    $ courage = 50
    $ temperance = 50
    $ agency = 50
    $ industry = 50
    $ integrity = 50
    $ wittiness = 50
    $ friendliness = 50
    $ attitude = 50
    
    $ inboxfilled = False
    
    $ healthy = 60
    $ intoxicated = 20
    $ nellwatsoneegg = False    
    
    #Stats Inits
    
    #Power
    $ intelligence_points = 0
    $ bodystrength = 20
    $ charisma_points = 0
    
    #Projection
    $ wits_points = 0
    $ dexterity_points = 0
    $ manipulation_points = 0
    
    #Resistance
    $ resolve_points = 0
    $ stamina_points = 0
    $ composure_points = 0

    $ code_skill = 0
    $ arts_skill = 0
    $ words_skill = 0
    
    $ hygiene = 80
    $ dentalhygiene = 100
    $ clotheshygiene = 80
    
    $ satiety = 100
    $ groceries = 3
    $ readymeals = 3
    $ snacks = 4
    
    $ calories = 18001
    
    
    $ integrity = 50
    
    $ mettomlove = False
    $ tomexercised = False
    $ whatuperosunlocked = False
    $ hasquanta = False
    $ hasprocrastibook = False
    
    $ sambeta = False
    $ samignored = False
    
    $ simonignored = False
    
    $ exerciselevel = 50
    
    
    $ nellmood = 1
      
      
    #pre-flags
    $ meetupdenied = False
    $ meetupdeniedt = False
    $ meetupdeniedd = False
    $ meetupdeniedp = False
    $ meetupdeniedm = False
    $ meetupdeniedi = False
    $ meetupdenieds = False
    $ meetupontime = False
    
    $ meetupscheduled = False   
    $ hasbike = False
    $ cheapgymmember = False
    $ fancygymmember = False
    


    #cards
    $ cards = []
    $ showcards = False
    
    
    #calendarset
    $ daycounter = 1
    $ pastmidnight = False
    
    $ chapter = 1
    $ location = 0
    
#Mailbox
    
    $ new_messages = 0
    $ mail = []
    $ mail_later = []
    $ reply_screen = False


    $ add_later("Welcome to F-mail", "Foofle", "This is a test message from Foofle. If you see this, you can be certain that your account is functional!")
    $ add_later("Where are you?", "Simon", "You've not been on ProcrastiBook for years! I mean, like, {i}ten minutes!{/i} Where are you?!", "simon_reply")
    $ simonignored = True
    $ add_later("Info?", "Sam", "Hello. I saw your landing page. Looks interesting.", "samlandingpage_reply")
    $ samignored = True
    $ add_later("Overstock", "Valkyrie.com", "Check out these amazing offers!")
    $ add_later("Little jog?", "Tom", "Hey [povname], want to come exercise with me?", "tomexercise_reply")
    $ tomignored = True
    $ add_later("How dare you?!", "Slick McDouche", "You were mean to me.  I'm *so* butthurt!! You better apologize!", "slick_reply")
    hide screen mailbox_overlay


transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

transform fastdissolvein:
        on show:
            alpha 0.0
            linear 0.3 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

#transform kbe2:
#    subpixel True
#    zoom 1.5
#    size (1280, 720)
#    linear 5.0 (100, 100, 720, 540)
#    crop (0, 0, 1280, 720)




init python:   

    def display_cards_overlay():
        if showcards:
            inventory_show = "Contacts: "
            for i in range(0, len(cards)):
                card_name = cards[i].title()
                if i > 0:
                    inventory_show += ", "
                inventory_show += card_name
            ui.frame()
            ui.text(inventory_show)
    config.overlay_functions.append(display_cards_overlay)
 

init python:
    import renpy.store as store

    class Contacts(store.object):
        def __init__(self, subject, sender, body, reply_label, view=True, status=True):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.view = view
            self.status = status
            mail.insert(0, self)
            if reply_label:
                self.can_reply = True
            else:
                self.can_reply = False
            global new_messages
            new_messages = new_messages + 1    
    
    def add_message(subject, sender, body, reply_label=False):
        renpy.sound.play("mail.wav")
        message = Mail(subject, sender, body, reply_label)
        renpy.show_screen("mailbox_overlay")
        
    def add_later(subject, sender, body, reply_label=False):
        mail_later.append([subject, sender, body, reply_label])
        
    def add_now():
        for element in mail_later:
            add_message(element[0], element[1], element[2], element[3])
        global mail_later
        mail_later = []
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.status:
                    return False #message is marked as unread
                else:
                    return True # message is marked as read

init python:
    
    class Player(renpy.store.object):
        def __init__(self, name, max_hp=0, max_mp=0, element=None):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
            self.element=element
    player = Player("[povname]", 100, 50)
    
    class Item(store.object):
        def __init__(self, name, player=None, hp=0, mp=0, element="", image="", cost=0):
            self.name = name
            self.player=player # which character can use this item?
            self.hp = hp # does this item restore hp?
            self.mp = mp # does this item restore mp?
            self.element=element # does this item change elemental damage?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element=self.element #item to change elemental damage; we don't drop it, since it's not a consumable item
    
    class Inventory(store.object):
        def __init__(self, money=10):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
    
    player = Player("[povname]", 100, 50)
    player.hp = 50
    player.mp = 10
    chocolate = Item("Chocolate", hp=40, image="gui/inv_chocolate.png")
    banana = Item("Banana", mp=20, image="gui/inv_banana.png")    
    gun = Item("Gun", element="bullets", image="gui/inv_gun.png", cost=7)
    laser = Item("Laser Gun", element="laser", image="gui/inv_laser.png")
    inventory = Inventory()
    #add items to the initial inventory:
    inventory.add(chocolate)
    inventory.add(chocolate)
    inventory.add(chocolate)
    inventory.add(chocolate)
    inventory.add(banana)
    inventory.add(banana)
    inventory.add(banana)
    inventory.add(banana)
    inventory.add(gun)
    inventory.add(laser)

label go:
    jump setup
    
label home:

    #scene bg default
    show screen home
    show screen calendar
    $ renpy.music.play("AngelinaWarisDiri.mp3", fadein=2)
    $renpy.pause()
    
    while True: # This makes sure that we can toy with it without leaving the game.
        $ result = ui.interact()
   
label check_week:

    $ renpy.jump(current_week)
   
    return

label check_minute:
#    count minutes. 
#    reset at 10
#    If mins <9 = call entropy
    
#label entropywork:
#    $ energy -= 3
#    $ satiety -= 3
    
#label entropyrest:
#    $ energy -= 1
#    $ satiety -= 3
    
#label entropyplay:
#    $ energy -= 2
#    $ satiety -= 4
    
#label entropysick:
#    $ energy -= 5
#    $ satiety -= 1
    
label randomroll:
    $roll = random.randint(1, 6)
    
label check_events:
    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    $ save_name = "%d min %d sec" % (minutes, seconds)
#    if current_week != "None":
#        $ renpy.jump(current_week + "_evt")
    if stress <= 80:
        pov "I'm stressed"
        show bg empty with Shake((0, 0, 0, 0), 3.0, dist=30)
    if calendar.last_day_of_the_month:
        #Monthly Report
        "Monthly Report"
    if calendar.month == "December" and calendar.day == 25:
        jump Harvest_Festival
#Menstrual cycle
    if calendar.moonphase == "waxing moon":
        if female and povage <= 52:
            $ povmood -= 20
            $ stress += 10
    if calendar.moonphase == "full moon":
        if female and povage <= 52:
            $ energy -= 10
#Project an event forward and wait for zerohour            
#    $ eventhorizon = renpy.random.randint(2, 800)
#    $ deliverytime = myClock + %(eventhorizon)d
#    if myClock >= deliverytime:
    $ add_now()
    return
    
#label check_random:
#    $ add_now()
   
    return
   
label check_end:
   
    "This function will check to see what ending has been triggered."
   
    return
   
label month:
   
    $ month_cnt += 1
   
    scene bg default
   
    #Setting default values for the schedule
   
    $ week01 = None
    $ week02 = None
    $ week03 = None
    $ week04 = None
    $ show_date = False

label schedule_repeat:

    call screen schedule

    if week01 is None or week02 is None or week03 is None or week04 is None:

        "Please pick an activity for every week this month."

        jump schedule_repeat
   
label week01:
    
    $ current_day = 1
    $ current_week = week01
   
    $renpy.scene()
    $renpy.show("bg "+week01)
   
    wk "First Week Plan: [week01]"
   
    call check_week
    
    $ week01 = None
    $ show_date = False
   
label week02:
    
    $ current_day = 1
    $ current_week = week02
    
    $renpy.scene()
    $renpy.show("bg "+week02)
   
    wk "First Week Plan: [week02]"
   
    call check_week
    
    $ week02 = None
    $ show_date = False
   
label week03:
    
    $ current_day = 1
    $ current_week = week03
    
    $renpy.scene()
    $renpy.show("bg "+week03)
   
    wk "First Week Plan: [week03]"
   
    call check_week
    
    $ week03 = None
    $ show_date = False
   
label week04:
    
    $ current_day = 1
    $ current_week = week04
    
    $renpy.scene()
    $renpy.show("bg "+week04)
   
    wk "First Week Plan: [week04]"
   
    call check_week
    
    $ week04 = None
    $ show_date = False
   
label end_month:
   
    "The month is already over. Time sure does fly."
   
    if month_cnt < 3:
        stop music
        jump freewheel
       
label game_over:
   
    call check_end
    stop music
    "Game Over."
   
    jump freewheel


    
label setup:
    stop music fadeout 1.0
    
    scene black with fade
    pause 1.0
    play music "music/risinggame.mp3"
    e "I've had enough of being taken for a ride." with dissolve
    scene bg graduationcaps with dissolve
    e "\"Get an education\", they said. \"Get a good job\", they said."
    scene bg handflick with dissolve
    e "Well... I'm not happy. I'm not where I thought I'd be."
    scene bg taxcredits with dissolve
    e "I've half-heartedly looked at my 'employment' options."
    e "But you know what? If I'm honest with myself..."
    scene black with fade
    e "I don't want to work for someone else." with dissolve
    scene bg exuberance with dissolve
    e "I want to be in command of my own destiny."
    e "I want to create! I want to seize life!" 
    scene bg successfailure with dissolve
    e "To hell with 'risks'. What risks, really? The risk of failing? So what, if I learn something invaluable?"
    e "If I fail, I get better. Soon I'll get so good that I start winning all the time!"
    scene black with fade
    e "But what's the risk of doing {cps=5}n o t h i n g ?{/cps}" with dissolve
    scene bg watchingtv with dissolve
    e "Because I'd rather watch TV, and take my little comforts where I can?"
    e "But would I truly be living? Or would I remain hollow, somewhere inside?"
    scene bg grave with dissolve
    e "I might waste an opportunity to add meaning to my life."
    e "Every one will die. The question is: will we choose to live bravely, or waste the most precious gift?"
    scene black with fade
    e "I {u}want{/u} to live a different life, and I have a plan to make it mine." with dissolve
    scene bg crossroads with dissolve
    e "I'm comfortable with not knowing which path to take, so long as I follow where my heart needs to go."
    e "I choose, I {i}choose{/i}, to build myself into..."
    scene founderbg with dissolve
    e "A Founder!"
    scene black with fade
    stop music fadeout 1.0
    stop movie
    show movie behind nell
    play movie "clouds2.ogv" loop
    play music "music/electrodoodle.mp3" loop
    show nell happy at basicfade, left

#if playedbefore:
#    n "Welcome back kickass founder!"
#    jump createfounder
#else:    
    $ renpy.block_rollback()
    n "Hi! Welcome to the Founder Life!"
    n "To choose a life of entrepreneurship, means choosing to live life to the max."
    n "It's yours if you want it. And, well, it looks like you do! A brave choice, but the right one!"
    n "Truly {u}anyone{/u} can learn to be an entrepreneur, and live an entrepreneurial life. No kidding!" 
    n "However, to succeed at it takes discipline, learning, and practice."
    n "That means using the right tool in right situation. It also means learning to be comfortable with failure."
    n "I'm Nell. I'm here to help power-up your ability to consistently execute."
    n "You have spirit, grit, and a mission in mind. So let's get started!"

    jump createfounder
     
             
label videotest:
    scene bg desktop with dissolve
    show nell happy at left with dissolve
    show movie behind nell
    play movie "nellstake.ogv"
    n "Let's test a video here!"
    
    scene black
    with Pause(1)

    show nell happy at truecenter with dissolve
    show movie behind nell
    play movie "street_day_animated.ogv" loop
    n "I'm in front of an animated background!"
    hide movie with dissolve
    stop movie

label rainmoney:
    n "Let's make it rain money, bitches!"
    show snowblossom
    n "Woooo!"
    hide snowblossom
    show snow
    n "Hey, look! It's snowing."
    with dissolve


label credits:
    play music "music/wholikestoparty.mp3"
    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    image splash = Text("{size=100}Founder Life", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing...", text_align=0.5)
    $ credits_speed = 60 #scrolling speed in seconds
    scene black #replace this with a fancy background
    $renpy.transition(dissolve)
    show cred at Move((0.5, 5.5),#mess with the 5.5 to change position where it starts from
        (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
#    show theend:
#        yanchor 0.5 ypos 0.5
#        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend
    with dissolve
    with Pause(credits_speed - 3)
    pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    show splash:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    stop music fadeout 8.0
    with Pause(5)
    hide splash
    with dissolve
    with Pause(2)
#    n "It took you %(minutes)d minutes and %(seconds)d seconds to finish this episode."

return
#return