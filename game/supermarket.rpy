label supermarket:
    scene bg supermarket with dissolve
if hasbike:    
        $ myClock.add_time(0,05)
else:
        $ myClock.add_time(0,15)
        
label supermarketbuy:
menu:
    "Groceries":
        $ groceries += 1 
        $ money -= 5
        jump supermarketbuy
    "Readymeeals":
        $ readymeals += 1 
        $ money -= 5
        jump supermarketbuy    
    "Snacks":
        $ money -= 2
        $ snacks += 1 
        jump supermarketbuy    
    "Leave":
        $ myClock.add_time(0,15)
        jump townmap