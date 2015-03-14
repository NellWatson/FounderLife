label dayend:
    call check_events #check to see if any events have been triggered.
# event.step() is a function that returns true while there are
# still events that need to be executed.
#    while event.step():
#    pass
if calendar.weekday == "Friday":
    call midnightcheck
    $ myClock.clockspin(10,00)
    $ energy += 5
    $ povmood += 5
    "Ah the weekend! Fuck yeah, [calendar.weekday]"
    call weather
    jump stresscheck
#    jump clockspin2
elif calendar.weekday == "Saturday":
    call midnightcheck
    $ myClock.clockspin(10,00)
    $ energy += 5
    $ povmood += 5
    "Ah the weekend! Fuck yeah, [calendar.weekday]"
    call weather
    jump stresscheck

else:
    call midnightcheck
    $ myClock.clockspin(8,00)
    $ energy += 5
    $ povmood += 5
    call weather
    jump stresscheck
    
label midnightcheck:
    if pastmidnight == True:
        $ pastmidnight = False
        $ meetupdenied = False
        $ meetupdeniedt = False
        $ meetupdeniedd = False
        $ meetupdeniedp = False
        $ meetupdeniedm = False
        $ meetupdeniedi = False
        $ meetupdenieds = False
        $ meetupscheduled = False
        pass
    else:
        $ daycounter += 1
        $ calendar.next()
        $ meetupdenied = False
        $ meetupdeniedt = False
        $ meetupdeniedd = False
        $ meetupdeniedp = False
        $ meetupdeniedm = False
        $ meetupdeniedi = False
        $ meetupdenieds = False
        $ meetupscheduled = False

label weather:
    
if calendar.month == "January" or "February" or "March":
    $ weatherrand = renpy.random.randint (1, 100)
    if weatherrand >= 60:
        $ weather = "snowing"
    elif weatherrand >=30:
        $ weather = "overcast"
    elif weatherrand <=10:
        $ weather = "sunny"
    elif weatherrand <=29:
        $ weather = "rainy"
        
elif calendar.month == "April" or "May" or "June":
    $ weatherrand = renpy.random.randint (1, 100)
    if weatherrand >= 60:
        $ weather = "rainy"
    elif weatherrand >=30:
        $ weather = "sunny"
    elif weatherrand <=10:
        $ weather = "snowing"
    elif weatherrand <=29:
        $ weather = "overcast"

elif calendar.month == "July" or "August" or "September":
    $ weatherrand = renpy.random.randint (1, 100)
    if weatherrand >= 60:
        $ weather = "sunny"
    elif weatherrand >=30:
        $ weather = "overcast"
    elif weatherrand <=10:
        $ weather = "snowing"
    elif weatherrand <=29:
        $ weather = "rainy"

elif calendar.month == "October" or "November" or "December":
    $ weatherrand = renpy.random.randint (1, 100)
    if weatherrand >= 60:
        $ weather = "overcast"
    elif weatherrand >=30:
        $ weather = "snowing"
    elif weatherrand <=10:
        $ weather = "sunny"
    elif weatherrand <=29:
        $ weather = "rainy"
      
return
  
label stresscheck:
if stress <= 80: 
    $ energy += 15
    $ renpy.block_rollback()
#    "You slept badly."
    jump freewheel
elif stress <= 50:
    $ energy += 25
    $ renpy.block_rollback()
#    "You slept Ok."
    jump freewheel
else:
    $ energy += 30
#    "You slept well."
    $ renpy.block_rollback()
    jump freewheel

   
    