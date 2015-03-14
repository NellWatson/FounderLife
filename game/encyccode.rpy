label encyccode:
    
#    show screen show_enc_button
    show screen show_enc_button
  
    "Do you want to add entries 4 and 6?" 

menu:
    "Yes":
        $ persistent.en6_locked = False
        $ encyclopaedia.unlockEntry(en6, persistent.en6_locked)
   
        $ persistent.en4_locked = False  
        $ encyclopaedia.unlockEntry(en4, persistent.en4_locked)
        "Ok, they're in. How about the sub-entries?" 
   
menu:
    "Add Sub-Entry 6-2 and 6-3":
        $ persistent.en6_2_locked = False   
        $ en6.unlockSubEntry(en6_2, persistent.en6_2_locked)
        $ persistent.en6_3_locked = False  
        $ en6.unlockSubEntry(en6_3, persistent.en6_3_locked)

    "Add Sub-Entry 2-3":
        $ persistent.en2_3_locked = False   
        $ en2.unlockSubEntry(en2_3, persistent.en2_3_locked)
   
    "Don't Add Sub-Entry":
        "Ok"  
   
    "No":
        "They weren't added." 
   
    "How about entry 7?"
menu:
    "Yes":
        $ persistent.en7_locked = False  
        $ encyclopaedia.unlockEntry(en7, persistent.en7_locked)
        "Done."
    "No":
        "How was it?"

jump desktop