init -1 python:
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"
            
screen inventory_screen:    
    add "gui/inventory.png" # the background
    tag menu
    #use battle_frame(char=player, position=(.97,.20)) # we show characters stats (mp, hp) on the inv. screen
    #use battle_frame(char=dog, position=(.97,.50))
    hbox align (.653,0.90) spacing 20:
        textbutton "Close" action Hide("inventory_screen")
    $ x = 59 # coordinates of the top left item position
    $ y = 361
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('element'), reverse=True) # we sort the items, so non-consumable items that change elemental damage (guns) are listed first
    $ next_inv_page = inv_page + 1            
    if next_inv_page > int(len(inventory.items)/16):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*16 and i+1>inv_page*16:
            $ x += 107
            if i%8==0:
                $ y += 101
                $ x = 59
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
            if player.element and (player.element==item.element): #indicate the selected gun
                add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>16:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos 0.475 ypos 0.863

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image information = Text("INFORMATION", style="tips_top")
    #Tooltips-inventory:
    image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))
    image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))
    image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An gun that looks like something a cop would\ncarry around. Most effective on humans.", style="tips_bottom"))
    image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on aliens.", style="tips_bottom"))
    
    image sidewalk = "Sidewalk.jpg"