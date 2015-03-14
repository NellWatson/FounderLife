screen qkey:
    if log.screen():
        key "q" action ShowMenu(log.screen())

screen qlog:
    if log.key():
        key "q" action [ Hide(log.screen()), Return() ]
        
    window:
        style "gm_root"
        background "ui/graphpaper.png"
    
    frame:
        style_group "mm_root"
        xfill True
        xmargin 10
        top_margin 10
        text "Action Items" align (0.5, 0.5)
        
    frame:
        style_group "mm_root"
        align (0.5, 0.5)

        
        frame:
            style_group "mm_root"
            align (0.5, 0.5)
            maximum (650, 500)
            yminimum 500
        
            vbox:
                xfill True
                textbutton "X" background None xalign 1.0 text_hover_color "#CCCCCC" text_color "#ffffff" text_font "ui/Comfortaa-Light.ttf" text_size 18 action [ Hide(log.screen()), Return() ]
#                text "" xalign 0.5   
#                spacing 10
                hbox:
                    for i in log.displayedtabs():
                        textbutton i action [ SetField(log, "tvar", i), log.newtab ]
                hbox:                
                    vbox:
                        xmaximum 200
                        xfill True
                        text "Name:"
                        for i in log.activetab():
                            textbutton i.title() text_hover_color "#CCCCCC" action SetField(log, "qvar", i) background None xpadding 0.0 text_size 18
                    vbox:
                        xmaximum 450
                        if log.activeimage():
                            add log.activeimage()
                        text "Description:"
                        fixed:
                            ymaximum 100
                            text log.activedescription() size 18
                        text "Progress:"
                        for i in log.activeprogress():
                            text formatgoal(i) size 18
                        null height 10
                        if log.trackable():
                            textbutton "Track this quest" text_size 18 action [ log.track, Return() ]
                            
screen tracker:
    fixed:
        align (1.0, 0.0)
        maximum (200,150)
        if log.tracked():
            textbutton "X" background None text_color "#000000" text_hover_color "#CCCCCC" text_font "ui/Comfortaa-Light.ttf" text_size 12 align (1.0, 0.0) action [ log.stoptracking, Hide(log.tracker()), Show(log.tracker()) ]
        vbox:
            xfill True
            spacing 3
            if log.tracked():                
                text log.trackedtitle() color "#000000" size 18
                for i in log.trackerprogress():
                    text formatgoal(i) color "#000000" size 12

image notification:
    align (0.5, 0.25)
    
    alpha 0.0
    Text(log.message(), color="#000000")
    linear 0.5 alpha 1.0
    pause 2.0
    linear 0.5 alpha 0.0

init python:
    
    def formatgoal(goal):
        str = ''
        
        if not goal.hidden():                                
            if goal.completed():
                str = "X {0}".format(goal.description())
            else:
                if goal.fetch():
                    str = "-{0}  {1}/{2}".format(goal.description(), goal.have(), goal.need())
                else:                                    
                    str = "-{0}".format(goal.description())
        else:
            if goal.required():
                str = "- ?????"
                
        return str                            
                                    
                                    
                                    
                                    
                                    
                                    