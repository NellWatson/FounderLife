##############################################################################
# Weekly Activities
#
# This file is used to store the players activity choice for each week. Events
# are called from within each activity.


## SCHOOL

label Art:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You go to the forest in the back of the school to draw."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Art
    
    hide screen calendar
    
    return
    
label Fencing:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You wander around back alleys hitting people with sticks."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Fencing
    
    hide screen calendar
    
    return
    
label Math:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You sit in the classroom doing practice problems from your math book."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Math
    
    hide screen calendar
    
    return
    
label Alchemy:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You drop by the church and study alchemy with the acolytes."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Alchemy
    
    hide screen calendar
    
    return
    
    
## WORK

label Church:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You visit the Church and volunteer."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Church
    
    hide screen calendar
    
    return
    
label Farm:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You work at the local farm."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Farm
    
    hide screen calendar
    
    return
    
label Store:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You man the front desk of a local shop."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Store
    
    hide screen calendar
    
    return
    
label Chores:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You stay at home and do chores."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Chores
    
    hide screen calendar
    
    return
    
    
## TRAVEL

label North:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You head north. For some reason you end up in a tunnel..."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump North
    
    hide screen calendar
    
    return
    
label East:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You head east. For some reason you end up in a tunnel..."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump East
    
    hide screen calendar
    
    return
    
label South:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You head south. For some reason you end up in a tunnel..."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump South
    
    hide screen calendar
    
    return
    
label West:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You head west. For some reason you end up in a tunnel..."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump West
    
    hide screen calendar
    
    return
    
    
## REST

label Home:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You stay at home. Good thing you have so many games to play or you might get bored."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Home
    
    hide screen calendar
    
    return
    
label Library:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You visit the library. So many books!"
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Library
    
    hide screen calendar
    
    return
    
label Vacation:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You go on vacation! Can't do this too often or you'll go broke..."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Vacation
    
    hide screen calendar
    
    return
    
label Hospital:
    
    $ calendar.next() #This will causes the calendar to advance by one day
    show screen calendar #Shows the date in the top right corner of the screen
    
    if current_day == 1: #This intro only shows on the first day of the week
        "You check into the hospital."
    
    call check_events #check to see if any events have been triggered.
    
    if current_day < 7 and not calendar.last_day_of_the_month:
        $ current_day += 1
        jump Hospital
    
    hide screen calendar
    
    return