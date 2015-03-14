init:
    #Declare the images used in the clock
    image clockBase = im.Scale("clock/VintageClockBase450x450.png", 75, 75)
    image clockHour = im.Scale("clock/VintageClockHour450x450.png", 75, 75)
    image clockMin = im.Scale("clock/VintageClockMinute450x450.png", 75, 75) 

init -1 python:
    
    import math #We'll need this for the advanced math functions
    from datetime import datetime #This is to get the realtime datetime
    
    #as a UDD this needs to extend the Displayable class)
    class Clock(renpy.Displayable):
        minutes = 0
        auto_run = True
        realtime_run = False
        offset = 0
        
        #The clock class constructor
        def __init__(self, pix, baseImage, hourImage, minImage, h, m, **kwargs):
            super(Clock, self).__init__(**kwargs)
            self.bI = ImageReference(baseImage)
            self.hI = ImageReference(hourImage)
            self.mI = ImageReference(minImage)
            self.minutes = (h*60)+m
            self.width = pix
            self.height = pix
            hypotenuse = math.sqrt(pow(pix,2) + pow(pix,2))
            self.offset = (hypotenuse-pix)/2
            
        def render(self, width, height, st, at):
            # Create transform to rotate the second hand
            tM = Transform(child=self.mI, rotate=self.minutes*6)
            tH = Transform(child=self.hI, rotate=self.minutes*0.5)

            # Create a render from the child.
            base_render = renpy.render(self.bI, width, height, st, at)
            minute_render = renpy.render(tM, width, height, st, at)
            hour_render = renpy.render(tH, width, height, st, at)
            
            #This moves the hands automatically if the clock is set to active
            if self.auto_run:
                self.realtime_run = False
                mbase = st
                mcheck = st-1
                add = (mbase-mcheck)/60 
                self.minutes += add
#                if pastmidnight = False:
#                    if self.minutes == 1:
#                        Calendar.next()
#                        pastmidnight = True
#                else:
#                    pass
                #Add 1 min to the analog clock, and 1 min to the 24hr clock
                
            if self.realtime_run:
                self.auto_run = False
                t = datetime.today()
                self.minutes = 60 * t.hour + t.minute         
            
            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(base_render, (0, 0))
            render.blit(minute_render, (-self.offset, -self.offset))
            render.blit(hour_render, (-self.offset, -self.offset))
            
            #This makes sure our object redraws itself after it makes changes
            renpy.redraw(self, 1)

            # Return the render.
            return render

        #Returns a list of all the child displayables for this displayable...but be here
        def vist(self):
            return [self.bI, self.hI, self.mI]
  
        #Directly set the time of the watch
        def set_time(self, h, m):
            self.minutes = (h*60)+m       
 
        #Manually add a certain amount of time to the clock
        def add_time(self, h, m):
            self.minutes += (h*60)+m
 
        #Turn the automatic function of the clock on and off
        def autoclock_run(self, run=True):
            self.auto_run = run
            
        #Turn the real time function of the clock on and off
        def realclock_run(self, run=True):
            self.realtime_run = run
            
        #Spin the clock hands until a time is met
        def clockspin(self, h, m):
            rem = ((h*60)+m)-30
            decel = ((h*60)+m)-4
            self.minutes = rem
            while self.minutes <= decel:
                self.minutes += 1
                renpy.pause(0.05)
            while self.minutes <= (h*60)+m:
                self.minutes += 1
                renpy.pause(0.50)

        #Call an eventloop every minute
#        def eventloop(self, h, m):
#            if self.minutes == (0,01):
#                MyCalendar.next() 
#                pastmidnight = True