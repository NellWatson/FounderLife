label chooseroom:    
    
    menu:
        "Which room would you like to go to? You are currently in the [room] room."
                
        "Pink" if room != "pink":
            $ room = "pink"
            jump pink
        "Yellow" if room != "yellow":
            $ room = "yellow"
            jump yellow
        "Blue" if room != "blue":
            $ room = "blue"
            jump blue
        "Green" if room != "green":
            $ room = "green"
            jump green

label pink:
    
    scene bg pink with fade

label pinkmenu:

    menu:
        e "How can I help you?"
        
        "Search the bushes" if log.interactive("pinkbush"):
            "You can't believe that you're spending your time looking through the bushes for Mary's glasses..."
            
            "And your search turns up nothing."
            
            $ log.markdone("pinkbush")
            
        "Where's my reward?" if log.interactive("finish"):
            jump endgame
        
        "Ask Eileen about Mary's glasses" if log.interactive("pinktalk"):
            e "Hmm..."
            
            e "I think... maybe... nope.  Definitely haven't seen them."
            
            $ log.markdone("pinktalk")
            
        "Ask Eileen about Peter's book" if log.interactive("book"):
            e "Ah yes!  I do have the book right here.  I see that my friends are keeping you busy."
            
            $ log.find("book")
            
            "You have received the book.  You now have 1/1 math books."
            
            e "Tell Peter that I said 'Thanks!'"
            
        "Leave room":
            jump chooseroom
    
    jump pinkmenu
    

label yellow:

    scene bg yellow with fade

    if first_visit[room]:
        pa "Hi there.  My name is Paul!  I am sure that you're very excited about this tech demo."
        
        pa "Tech demos can help a programmer test features that he or she has programmed.  This helps
            determine what features need to be added or changed."
        
        pa "Feedback is always appreciated as well as it helps determine what functionality to add."
        
        pa "Thanks for listening to me babble on for a second there.{size=8}(as if you had a choice.){/size}
            I sure could use your help with a problem of mine here."
        
        pa "I am supposed to take a poll of the citizens of this colorful town on whether or not we should
            build a purple room."
        
        pa "I've talked to everyone except for Mary.  You see... it's kind of awkward for me to talk to her nowadays."
        
        pa "It's a long, uninteresting story really... but if you could take this survey to her to fill out it would help
            me out a lot."
        
        pa "And as far as I can gather, you're sort of stuck doing what I want if you have any desire at all to 'complete'
            the quest.  So, I'll go ahead and say thanks in advance!"
        
        $ log.assign("Paul's Quest")
        
        pa "One more thing, PLEASE don't tell her I sent you to do my work for me."
        
        $ first_visit[room] = False

label yellowmenu:

    menu:
        pa "So, anything I can do for you?"
        
        "Search the bushes" if log.interactive("yellowbush"):
            
            "You spend time looking through the bushes for Mary's glasses..."
            
            "But your search turns up nothing."
            
            $ log.markdone("yellowbush")
            
        "Ask Paul about Mary's glasses" if log.interactive("yellowtalk"):
            
            pa "Have I seen Mary's glasses?"
            
            if log.completed("truth"):
                
                pa "I spent the past while crying after that note YOU delivered to me."
                
                pa "I know you told her that I sent you."
                
                pa "Let's put it this way, I haven't seen her glasses and I don't want to see you or Mary ever again."
                
            else:
                pa "Like I said, I am trying to avoid Mary.  So, I can't say that I have seen her glasses."
            
            $ log.markdone("yellowtalk")
            
        "Deliver the survey to Paul" if log.interactive("lie"):
            jump delivery
            
        "Deliver Mary's note to Paul" if log.interactive("truth"):
            jump note
            
        "Leave room":
            jump chooseroom
            
    jump yellowmenu
    
label blue:

    scene bg blue with fade

    if first_visit[room]:
        m "Hello!  Mary's my name and standing around all day's my game."
        
        m "Seriously, I am not programmed to do much else.  I don't even have an image to represent me!"
        
        m "There is a decent reason for that though.  Art assets and such aren't really needed to test most
           of the code.  It makes it easier for a programmer to post their script files and not worry about
           additional assets."
        
        m "Anyway, I have a feeling that you stopped by just to help out lil' ol' me."
        
        m "There is one favor that I need to ask of you.  I lost my glasses the other day and I am pretty sure
           they landed in some bushes."
        
        m "The problem is that I don't know which room.  There are bushes in every room... just take my word for it."
        
        m "It'd be a great help if you could find my glasses and return them to me."
        
        $ log.assign("Mary's Quest")
        
        m "Another thing, you don't have to search here in the blue room as I have already extensively searched.  Good luck!"
        
        $ first_visit[room] = False

label bluemenu:

    menu:
        m "What can I do for you?"
        
        "Tell Mary about your search" if log.interactive("marytalk"):
            m "Oh... I am sorry to put you through all that trouble."
            
            m "It turned out my glasses were in their case inside my purse all along!  I am so scatterbrained sometimes."
            
            m "Thanks for trying so hard to help me out though.  I will let Eileen know that you were good to me."
               
            $ log.markdone("marytalk")
        
        "Talk to Mary about the survey" if log.interactive("survey"):
            
            jump survey
        
        "Leave room":
            jump chooseroom
            
    jump bluemenu
    
label green:
    
    scene bg green with fade

    if first_visit[room]:
        
        pe "Yeah, I'm going to give you a quest after I ramble for a bit.  It's just how it works."
        
        pe "There are two basic kinds of quests as I see it.  A 'fetch' quest involving acquiring multiple
            quantities of something and checkpoint kinds of quests."
        
        pe "Really they are all the same because a checkpoint quest is the equivalent a fetch quest that requires
            one object/action."
        
        pe "As a matter of fact, I need to get some math homework done before tomorrow, but I don't have my book."
        
        pe "You could say I have 0/1 math books.  I mean, it is kind of silly that way.  I loaned the book to Eileen,
            so I am pretty sure she'll have it."
        
        $ log.assign("Peter's Quest")
        
        pe "The sooner you find it, the sooner I... I mean, I need the book whenever you have time.  Thanks!"
        
        $ first_visit[room] = False

label greenmenu:
    
    menu:
        pe "What can I do for you?"
        
        "Search the bushes" if log.interactive("greenbush"):
            "You spend time looking through the bushes for Mary's glasses..."
            
            "But your search turns up nothing."
            
            $ log.markdone("greenbush")
            
        "Offer your help to do the math problems" if log.interactive("math"):
            
            jump mathjump
            
            
        "Give the book to Peter" if log.interactive("return"):
            
            pe "That's exactly the book I was looking for."
            
            pe "I am kind of in a rush to get this math homework done.  Do you think you could help me with a few problems?"
            
            pe "I promise that you are able to do them and they won't be hard for you.  I'd like you to help me with three of them."
            
            $ log.markdone("return")
            
            jump mathtime
            
        "Ask Peter about Mary's glasses" if log.interactive("greentalk"):
            pe "Yeah, I stole them..."
            
            pe "Just kidding!  I guess you have to keep looking.  I definitely do not envy you."
            
            $ log.markdone("greentalk")
        
        "Leave room":
            jump chooseroom
            
    jump greenmenu

label searchfailed:
    
    "You've looked through all the bushes, but you still haven't found Mary's glasses."
    
    "Maybe someone came across them and picked them up.  It's probably best to talk to everyone
     to see if they have seen Mary's glasses."
    
    return
    
label failedagain:
    
    "This search has definitely turned out to be a total waste of time."
    
    "I guess the only thing left to do is to return to Mary and tell her that you couldn't
     find her glasses."
    
    return
    
label success:
    
    $ log.markdone("mary")
    
    return
    
label survey:
    
    m "Hmm, this is odd.  Paul is usually in charge of all the town surveys.  Did he send you so he could avoid me?"

    menu:
        "How do you respond?"
        
        "(Truth) Yes, Paul sent me.":
            pass
            
        "(Lie) No, that's not it at all.":
            
            $ log.deactivate("tattle")
        
            m "I guess I'll just have to take your word for it."
               
            m "Paul has been a little awkward ever since we broke up last month."
            
            m "I want to be friends still, but I am not sure what he wants."
            
            m "Anyway, about this survey, it's no problem at all.  I can finish this thing before you know it."
        
            "You stand around while Mary finishes the survey; it doesn't take her long at all."
            
            m "There ya go!"
            
            if not log.completed("Mary's Quest"):
                m "And remember to please keep looking for my glasses when you have the time."
            
            m "Catch ya later!"
            
            $ log.setnext("lie")
            
            $ log.markdone("survey")
            
            jump bluemenu
        
    $ log.markdone("tattle")
            
    m "I figured as much."
        
    m "He has been trying so hard to avoid me ever since we broke up last month.  He doesn't even answer my calls!"
    
    m "Well, I have a message for him..."
    
    "Mary rips the survey out of your hand and begins to write furiously.  It's clear that she's not filling out the survey for
     its intended purpose."
    
    "Mary finishes up and seems somewhat relieved."
    
    m "Phew, there we go.  Now I want you to hand deliver this back to Paul."
    
    if not log.completed("Mary's Quest"):
        m "And don't even worry about looking for my glasses until you deliver that note."
    
    $ log.markdone("survey")    

    jump bluemenu    
        
label delivery:
    
    "You hand the finished survey to Paul as you begin to contemplate just how pointless all
     of these tasks are."
    
    pa "Thanks for doing this for me. It really helped me out."
    
    pa "I'll make sure that Eileen knows of your good deeds."
    
    $ log.markdone("lie")    
    $ log.markdone("paul")
    
    jump yellowmenu
        
label note:
    
    "You hand Paul the note knowing that it can't be a whole lot of good news to the person who
     reads it."
    
    pa "Thanks for doing this for me."
    
    "You nod and decide it might be best to give him some privacy while he reads the note."
    
    "Paul notices something's off by the way you're acting and begins to tentatively read the note."
    
    "A few seconds after you walk away, you being to hear whimpers and they grow more and more faint
     as you get further and further away."
    
    "Well, that didn't turn out well for Paul."
     
    $ log.markdone("truth")
    
    "I know what you're thinking.  How did that 'help' Paul out at all? It doesn't matter; it's marked
     completed in your quest log and that's way more important."
    
    "Time to move on."
    
    $ log.markdone("paul")
    
    jump yellowmenu
        
label mathtime:
    
    menu:
        "Would you like to help Peter right now with the math problems?"
        
        "Yes":
            pass
            
        "No":
            pe "That's okay.  I'll be hanging around here in the green room whenever you are ready."
            
            jump greenmenu

label mathjump:
    
    pe "Great! I'll give you a simple math problem and all you have to do is type in the answer."
    
    $ wrong = 0
    
    while not log.completed("Peter's Quest"):
    
        $ a = renpy.random.randint(1, 9)
        $ b = renpy.random.randint(1, 9)
        
        $ prompt = str(a) + ' + ' + str(b) + ' = ?'
        $ num = int(a) + int(b)
        
        $ ans = None
        
        while not ans:
            $ ans = renpy.input(prompt, allow=numbers)
    
        if int(ans) == num:
            
            $ log.find("math")
            
            $ num = log.have("math")
            
            if num == 1:
                
                pe "That's correct!  Huh?  You're asking why I needed your help in the first place?"
                
                pe "Look, it's only two more to go, just bear with me."
                
            elif num == 2:
                
                pe "Good job!  Almost done, so I don't want to hear any complaining."
                
            elif num == 3:
                
                pe "You see? That wasn't too hard."
            
        else:
            
            $ wrong += 1
            
            if wrong == 1:
                pe "Sorry, that's wrong...  I know, it's a little ironic that I am in the position to verify
                    the answer when I was the one who asked for help."
                
            elif wrong == 3:
                pe "Sooo, are you missing on purpose?"
                
            elif wrong == 10:                
                pe "Okay, now I know you're just messing with me."
            
            else:
                pe "Incorrect! Try again."
    
    $ del wrong, a, b, prompt, ans, num
    
    pe "Thanks for helping me out! It was a big help I assure you."
    
    $ log.markdone("peter")
    
    jump greenmenu
    
label atlast:
    
    "That completes all of Eileen's tasks.  Return to her for your reward now."
    
    return
    
label endgame:
    
    $ log.markdone("finish")
    
    e "First of all, thank you so much for playing through this little tech demo."
    
    e "Huh? What reward? Isn't my gratitude enough?"
    
    "The End"
    
    return
    
    
