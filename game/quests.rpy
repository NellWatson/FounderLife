label createlog:



    python:



        quests = [ ]



        ####Quest1####

        goals = [ ]

        stages = [ ]
        
        goals.append(Goal("findmeetup", "Go and find a place where cool people hang out"))

        goals.append(Goal("attendmeetup", "Attend the scheduled meetup"))

        goals.append(Goal("finish", "Speak to someone new"))



        stages.append(Stage("peter,paul,mary", "atlast"))

        stages.append(Stage("finish"))

        

        quests.append(Quest("Attend Your First Meetup",

            "\"Go alone to go quickly, go with others to go far.\"\n\nFind out when the next meetup is happening on your computer, and then attend it on time.",

            "Tutorial",

            goals,

            stages))

        

        ####Quest2####

        goals = [ ]

        stages = [ ]

        

        goals.append(Goal("survey", "Talk to Mary"))

        goals.append(Goal("tattle", "Tell Mary that Paul sent you. {size=10}(optional){/size}", required=False))

        goals.append(Goal("truth", "Return to Paul with Mary's note"))

        goals.append(Goal("lie", "Return to Paul with the finished survey"))

    

    

        stages.append(Stage("survey,tattle", next="truth"))

        stages.append(Stage("truth", id="truth", next=False))

        stages.append(Stage("lie", id="lie", next=False))

    

        quests.append(Quest("Paul's Quest",

            "Help Paul out by taking the survey to Mary for him.  Paul is in the yellow room.",

            "Tutorial",

            goals,

            stages))

    

        ####Quest 3####

        goals = [ ]

        stages = [ ]

        

        goals.append(Goal("pinkbush", "Search the bushes in the pink room"))

        goals.append(Goal("greenbush", "Search the bushes in the green room"))

        goals.append(Goal("yellowbush", "Search the bushes in the yellow room"))

        goals.append(Goal("pinktalk", "Ask Eileen about Mary's glasses"))

        goals.append(Goal("greentalk", "Ask Peter about Mary's glasses"))

        goals.append(Goal("yellowtalk", "Ask Paul about Mary's glasses"))

        goals.append(Goal("marytalk", "Return to Mary and tell her the results of your search"))

        

        stages.append(Stage("pinkbush,greenbush,yellowbush","searchfailed"))

        stages.append(Stage("pinktalk,greentalk,yellowtalk",

            "failedagain",

            "Searching the bushes didn't turn anything up.  Talk to everyone to see if they have seen Mary's glasses."))

        stages.append(Stage("marytalk",

            "success",

            "Talking to people and searching the bushes have both been a fantastic waste of time.  It's time to return to Mary in the blue room."))

        

        quests.append(Quest("Mary's Quest",

            "Help Mary by finding her glasses.  Start by searching the bushes in each room.  Mary is in the blue room.",

            "Tutorial",

            goals,

            stages))



        

        ####Quest 4####

        goals = [ ]

        stages = [ ]

        

        goals.append(Goal("book", "Talk to Eileen to get Peter's math book", 0, 1))

        goals.append(Goal("return", "Return the book to Peter"))

        goals.append(Goal("math", "Solve 3 math problems for Peter", 0, 3))



        stages.append(Stage("book"))

        stages.append(Stage("return"))

        stages.append(Stage("math"))



        quests.append(Quest("Peter's Quest",

            "Peter wants you to help him find his math book.  Eileen may know where it is.  Peter hangs out in the green room.",

            "Tutorial",

            goals,

            stages))

    

        log = Questlog(quests, "qlog", "qkey")

        

        del goals

        del quests

        del stages

        

    return

