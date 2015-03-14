init python:

    # Message Styles

    style.messageWindow = Style(style.window)
    style.messageColumns = Style(style.hbox)
    style.messageListBox = Style(style.vbox)
    style.messageListViewport = Style(style.viewport)
    style.messageButton = Style(style.button)
    style.messageButtonText = Style(style.button_text)
    style.messageScrollBar = Style(style.vscrollbar)
    style.messageBodyScrollBar = Style(style.vscrollbar)
    style.messageBodyBox = Style(style.vbox)
    style.messageBodyViewport = Style(style.viewport)
    style.messageText = Style(style.say_dialogue)
    style.messageControls = Style(style.hbox)

    # Default style values...

    style.messageWindow.ymaximum = 600

    style.messageColumns.spacing = 10

    style.messageListViewport.xminimum = 280
    style.messageListViewport.xmaximum = 280

    style.messageListBox.yalign = 0.0

    style.messageButton["Message"].xfill = True
    style.messageButton["CurrentMessage"].xfill = True

    style.messageButtonText["Message"].color="#99A"
    style.messageButtonText["CurrentMessage"].color="#FFF"
    
    style.messageBodyViewport.xminimum = 460
    style.messageBodyViewport.xmaximum = 460
    style.messageBodyViewport.ymaximum = 550

    style.messageBodyScrollBar.ymaximum=550

    style.messageControls.spacing = 10

    def init_messages():
        if hasattr(store, "messages") == False:
            store.messages = []
        
    def add_message(subject, sender, message, condition=None):
        init_messages()
        store.messages.append( (subject, sender, message, condition) )

    def show_messages():
        message = None

        while message != -1:
            message = show_message_ui(message)

    def show_message_ui(currentMessage):
        
        init_messages()

        messageCount = count_messages()

        ui.window(style=style.messageWindow)
        ui.hbox(style=style.messageColumns) # For the three columns of controls

        vp = ui.viewport(style=style.messageListViewport)

        ui.window(style=style.messageListBox)
        ui.vbox() # For the mail list

        index = 0
        for message in store.messages:
            if (message[3] == None or eval(message[3]) == True):
                    styleIndex = "Message"
                    if (index == currentMessage):
                        styleIndex = "CurrentMessage"
                    ui.button(clicked=ui.returns(index),
                        style=style.messageButton[styleIndex])
                    ui.text(message[0] + " - " + message[1], style=style.messageButtonText[styleIndex])
            index = index + 1

        ui.close() # mail list vbox

        ui.bar(adjustment=vp.yadjustment, style=style.messageScrollBar)

        ui.window(style=style.messageBodyBox)
        ui.vbox() # For the right-hand stuff; message and buttons

        ui.hbox()
        vp2 = ui.viewport(style=style.messageBodyViewport)

        if (currentMessage >= 0) and (currentMessage < messageCount):
            hasMessage = True
            ui.text(store.messages[currentMessage][2], style=style.messageText)
        else:
            hasMessage = False
            ui.null()
        ui.bar(adjustment=vp2.yadjustment, style=style.messageBodyScrollBar)

        ui.close()

        ui.hbox(style=style.messageControls) # For the buttons

        ui.button(clicked=ui.returns(-1),
            style=style.messageButton["Close Messages"])
        ui.text("Close Messages", style = style.messageButtonText["Close Messages"])
        if hasMessage:
            ui.button(clicked=ui.returns(-2),
                style=style.messageButton["Delete Message"])
            t = ui.text("Delete Message", style = style.messageButtonText["Delete Message"])

        ui.close() # buttons hbox


        ui.close() # right-hand column vbox
        ui.close() # columns hbox

        result = ui.interact()

        if result == -2: #(delete current message)
            del store.messages[currentMessage]
            return None
        else:
            return result
            
    def count_messages():
        init_messages()
        return len(store.messages)

    def count_visible_messages():
        init_messages()
        
        count = 0
        
        for message in store.messages:
            if (message[3] == None or eval(message[3]) == True):
                count = count + 1
        return count

label fmail:
if fmailintroduced == 1:
    jump checkmail
else:
    n "I took the liberty of setting you up an with F-mail account."
    n "However, your inbox is currently empty."

    $ show_messages()

    n "See?"

    $ add_message("Welcome to F-mail", "Foofle",
        "This message verifies your Fmail inbox. You're all set up!")

    n "Now I've added a message for you."

    $ show_messages()
    
    n "Ok, I'll add a few more..."

    $ add_message("My Holiday Photos", "Bob", "Drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone " +
        "drone drone drone drone drone drone drone drone drone drone drone drone drone drone...")
    $ add_message("Where are you?", "Simon", "You've not been on ProcrastiBook for years! I mean,"
        " like, {i}ten minutes{/i}, dude! Where are you?!")
    $ add_message("Buy Stuff", "Mississippi", "Did you know that people who bought books in the"+
        " past also bought books? How about you buy some books?\n"+
        "Here are some books you might like:\n- {i}To Murder A Coot{/i}\n"+
        "- {i}The Girl with the Pirate Tattoo{/i}\n- {i}9Tail Cat{/i}")
    $ add_message("Tuesday", "Mum", "Did you remember you were coming to visit on Tuesday?" +
        " I hope you didn't forget.")
    $ add_message("Re: Tuesday", "Mum", "You haven't called. Are you still coming?"+
        " I'm making pie.")
    $ add_message("Park hangout", "Tom", "Hey [povname], want to come exercise with me?"+
        " I'm gonna head out in 5 mins."+
        " kthxbye")
            
    $ add_message("Re: Re: Tuesday", "Mum", "Why don't you let us know whether you're coming?" +
        " Have you checked your mail? Are you OK? I hope you haven't got into a car crash or" +
        " something. You see them on the news all the time. Are you really OK?" +
        " Please, let us know!")

    $ show_messages()
    
    n "Now we'll add some spam..."
    
    python:
        
        spam_filter = False
        
        #spam...
        for x in range(1):
            add_message("Billions of dollars!", "Prince Terence of Nigeria", "I am the" +
                " custodian of the Nigerian Central Bank, and I need a foreign account to" +
                " place billions of dollars in for a period of two (2) months for no apparent" +
                " reason. You could earn millions in interest, just mail me your credit card" +
                " and PIN today!",
                condition="spam_filter == False")

        for x in range(1):
            add_message("8UY |-|3R84L \/14@R4, (14L15", "Hugh G. Rection", " VERY CHEAP MAKE YOU VERY HAPPY " +
                " BUY TODAY",
                condition="spam_filter == False")
            
        for x in range(1):
            add_message("Lemons into Lemonade", "Jack Lemmon", "VOTE LEMONPARTY " +
                "FOR REAL CHANGE",
                condition="spam_filter == False")

    $ show_messages()
    
    n "Eep! OK, let's turn the spam filter on..."
    
    $ spam_filter = True
    $ show_messages()

    $ message_count = count_messages()
    $ visible_count = count_visible_messages()
    n "And after all that, you now have %(message_count)s messages,
        of which you can see %(visible_count)s."
    $ fmailintroduced = 1
    jump desktop

label checkmail:
    $ show_messages()
jump desktop  