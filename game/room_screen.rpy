############################################################
# Node-based navigation framework for Ren'Py
#   by powerofvoid (exponents.in.space@gmail.com)
#
#   CC0 (http://creativecommons.org/publicdomain/zero/1.0/)
#
# 

init python:
    """
        ###################################################
        # Step 1: Initialize
        ###################################################
          #
          # add the following line at the beginning of "label start:"
          #################
    call initialize_room_screen
        
        ###################################################
        # Step 2: Define some people and places
        ###################################################
          #
          # See the documentation below
          ##################
        
        ###################################################
        # Step 3: Call the screen
        ###################################################
          #
          # Like so:
          ##################
    jump show_room_screen
        
        # Note that you must have defined the image "image player" to have the player show up. It might even throw an error if you don't have the image defined!
        
    """

init python:            
    """
        ###################################################
        # More detailed documentation:
        ###################################################
          # How to make rooms and people:
          #################################################
        
        ###################################################
        # Rooms:
        ###################################################
        
init:
    $ contact_to_show = renpy.random.choice(contact_list)
    # sample room:
    sample_room_actions = {                         # you can add multiple actions here
        "sample_action" : {
            "name" : "Action Name",                 # human-readable name for this action. Free to be misleading   
            "requirements" : "some > expression",   # this expression is evaluated to determine if this action is available. "True" means it always is
            "label" : "action_label",               # this label is jumped to when this action is chosen
        },
    }
            
    sample_room_connections = {                     # you can add multiple connections here
        "sample_connection" : {                     
            "name" : "Connection Name",             # human-readable name for the location you're going to. Free to be misleading
            "requirements" : "some > expression",   # this statement is evaluated to determine if this action is available. "True" means it always is
            "label" : "target_room_label"           # the label to jump to to get to the new room. It will need to activate the room_screen when it's ready.
        },
    }
    
    
    sample_room = { 
        "room_id" : "sample_room",                  # this is used as a variable to tell functions what room you're in
        "name" : "Sample Room",                     # a human-readable name to refer to the room. It is free to be misleading
        "description" : "A simple sample room",     # a human-readable description of the room. It is also free to be misleading
        "background" : "background_image",          # this image shows in the background of the scene
        "actions" : sample_room_actions,            # a dict of actions at this location
        "connections" : sample_room_connections,    # a dict of places you can go from here
    }
        
label sample_room_label:                                    # Jump to this label to "enter" this room
    if not sample_room["room_id"] in places:                # If this room hasn't been defined
        $ places[sample_room["room_id"]] = sample_room      # Add it to the dictionary
    $ current_room = sample_room["room_id"]                 # Set current room to this room
    
    # Stuff here happens whenever you enter the room
    
#    jump show_room_screen
        
        
        ############################################
        # People:
        ############################################
init:
    sample_person_data_initial = {
        "person_id" : "sample_person"                       # used to do things to and with this person
        "name" : "Sample McSamplikens",                     # a name for use in the room_screen
        "location" : "sample_room",                         # where this person is. Note: when this changes during gameplay, it should be done in people[person_id]['location']
        "label" : "sample_person_label",                    # the label to call to process this person
    }
    
label add_sample_person :                                   # do this to add this person to the game
    $ people[sample_person["person_id"]] = sample_person

label sample_person_label:                                  # This happens when you interact with this person
    # Stuff goes here
    """

init python:
    debug_room = {
        "room_id" : "debug_room",
        "name" : "Startup Meetup",
        "description" : "It looks like there might be a few cool people here.",
        "background" : "bg meetup",
        "actions" : {
            "look_around" : {
                "name" : "Look Around",
                "requirements" : True,
                "label" : "room_common_action_look",
            },
        },
        "connections" : {},
    }
    placeholder_person = {
        "person_id" : "placeholder_person",
        "name" : "Ann Onymous",
        "location" : debug_room['room_id'],
        "label" : "person_placeholder_talk",
    }


label initialize_room_screen:
    $ places = { debug_room['room_id'] : debug_room, }
    $ people = { placeholder_person['person_id'] : placeholder_person, }
    $ previous_room = debug_room['room_id']
    $ current_room = debug_room['room_id']
    return 

label show_room_screen:
    $renpy.transition(dissolve)
    call screen room_screen 
    pause
    jump show_room_screen

screen room_screen:
    add places[current_room]["background"]:
        xalign 0.5
        yalign 0.5
    add "char":
        xalign 0.5
        yalign 1.0
#    frame:
#        xpadding 10
#        ypadding 10
#        xalign 1.0
#        yalign 0.1
#        xmaximum 0.3
        
#        vbox:
            
#            text "Move To:" xalign 0.5
#            for this_place in sorted(places[current_room]["connections"]):
#                if eval(places[current_room]["connections"][this_place]["requirements"]):
#                    textbutton places[current_room]["connections"][this_place]["name"] :
#                        xfill True
#                        action [ 
#                            SetVariable("previous_room", current_room), 
#                            Jump(places[current_room]["connections"][this_place]["label"]),
#                        ]
    frame:
        xpadding 10
        ypadding 10
        xalign 1.0
        yalign 0.0
        xmaximum 0.3
        
        vbox:
            text places[current_room]["name"] xalign 0.5
            for this_action in sorted(places[current_room]["actions"]):
                if eval(places[current_room]["actions"][this_action]["requirements"]):
                    textbutton places[current_room]["actions"][this_action]["name"] : 
                        xfill True
                        action [
                            Jump(places[current_room]["actions"][this_action]["label"]),
                        ]
            
            textbutton "Mingle" :
                xfill True
                action [
                    Jump("meetnewcontact"),
                ]                        
                    
    
        
##        vbox:
#            for this_person in sorted(people):
#                if people[this_person]["location"] == current_room :
#                    textbutton people[this_person]["name"] :
#                        xfill True
#                        action [
#                            Jump(people[this_person]["label"]),
#                        ]

#        vbox:
            textbutton "Back" :
                xfill True
                action [
                    Jump("townmap"),
                ]