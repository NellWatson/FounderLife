label bed:
    
#if myClock <= (10,00):
    
menu:
    "Try to sleep":
        scene black with fade
        if myClock.minutes <= 1430:
            $ healthy += 5
        jump dayend
        
    "Phub about and relax.":
        $ myClock.add_time(0,30)
        $ energy += 10
        $ stress -= 10
        jump bed
    "Get up":
        jump freewheel

# $ Oblamov if 24 hours in bed