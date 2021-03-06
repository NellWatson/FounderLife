##############################################################################
# Gallery
#
# Screen that's used to display unlocked CGs. This gallery was created by leon
# from the lemmasoft forums. Thanks, leon!

init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["cg1", "cg2", "cg3", "cg4", "cg5", "cg6", "cg7", "cg8", "cg9", "cg10", "cg11"]
    
    #list the BG gallery images here (do not include variations, such as night version):
    gallery_bg_items = ["bg default", "bg School", "bg gym", "bg Fencing", "bg Alchemy", "bg Math", "bg North", "bg East", "bg South", "bg West", "bg Home", "bg Library", "bg Vacation", "bg Hospital", "bg Farm", "bg Church", "bg Store", "bg Chores"]
    
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150
    
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_bg = Gallery()
    
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        
        #if BGs have variations, such as night version, uncomment the lines below and copy paste them for each BG with variations
#        if gal_item == "bg kitchen":
#            g_bg.image("bg kitchen dining")
#            g_bg.unlock("bg kitchen dining")
            
    g_bg.transition = fade
    bg_page=0
    
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))
        
screen cg_gallery:
    tag menu
    use navigation
    frame background None:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1            
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]

screen bg_gallery:
#The BG gallery screen is more or less copy pasted from the CG screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    frame background "crate.png":
        grid gal_rows gal_cols:
            xalign 0.5
            yalign 0.55
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            hbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]
                    textbutton _("Return") action Return()
                    