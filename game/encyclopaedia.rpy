# Encyclopaedia Framework for Ren'Py
# Copyright 2014 Joshua Fehler <jsfehler@gmail.com>
# Last Updated: 3/13/2014
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

init -1500 python:
 from operator import itemgetter
 from math import floor
 
 #Action that places the selected encyclopaedia entry into the frame
 class SetEntryAction(Action):
  def __init__(self, encyclopaedia, var):
   self.enc = encyclopaedia 
   self.var = var
   
  def __call__(self):
   self.given_entry = self.enc.getEntry(self.var)
   
   self.given_text = self.given_entry.getText()
  
   global entry_text #entry_text is the variable used on the encyclopaedia_entry screen for whatever entry's text we're displaying

   if type(self.given_text) is list: #If the text source is a list, pass it through. If not, turn it into a list
    entry_text = self.given_text
   
   else:
    entry_text = [self.given_text] #the desired entry's text
 
   if self.enc.showLockedEntry == False:
    self.target_position = self.enc.unlocked_entries.index([self.given_entry.number,self.given_entry]) #index the unlocked list to get what the current position should be

   if self.enc.showLockedEntry:
    self.target_position = self.enc.all_entries.index([self.given_entry.number,self.given_entry])
   
   self.enc.setEntryData(self.target_position) #The entry's data is based on the target position given
   
   self.enc.current_position = self.target_position #current_position is now the target position
  
 #Scroll through the current entry being viewed. 
 #Used by Encyclopaedia's PreviousEntry and NextEntry functions
 class ChangeEntryAction(Action):
  def __init__(self, encyclopaedia, direction, block):  
   self.enc = encyclopaedia
   self.block = block #If the button is active or not
   self.dir = direction  #Determines if it's going to the previous or next entry 
  
  def __call__(self):
   if self.block == False:
    global entry_text
  
    self.enc.setEntryData(self.enc.current_position+self.dir)
 
    if self.enc.showLockedEntry == False:
     self.enc.unlocked_entries[self.enc.current_position+self.dir][1].status = True 
     given_text = self.enc.unlocked_entries[self.enc.current_position + self.dir][1].getText()
    
    if self.enc.showLockedEntry: 
     self.enc.all_entries[self.enc.current_position+self.dir][1].status = True   
     given_text = self.enc.all_entries[self.enc.current_position + self.dir][1].getText()
 
    if type(given_text) is list: #If the text source is a list, pass it through. If not, turn it into a list
     entry_text = given_text
   
    else:
     entry_text = [given_text]
    
    self.enc.current_position += self.dir
      
    self.enc.sub_current_position = 1 #When changing an entry, the sub-entry page number is set back to 1
    renpy.restart_interaction()
   else:
    pass
    
  def get_sensitive(self):
   if self.block:
    return False
   return True 
 
 #Class to change the current sub-entry being viewed.
 class ChangePageAction(ChangeEntryAction):
  def __init__(self, encyclopaedia, dir1, dir2, block):
   self.enc = encyclopaedia
   self.dir1 = dir1
   self.dir2 = dir2
   self.block = block

  def __call__(self):
   if self.block == False: 
    global entry_text

    given_text = self.enc.getUnlockedEntry(self.enc.current_position).getSubEntry(self.enc.sub_current_position + self.dir1)
   
    if type(given_text) is list:
     entry_text = self.enc.getUnlockedEntry(self.enc.current_position).getSubEntry(self.enc.sub_current_position + self.dir1)
      
    else:
     entry_text = [self.enc.getUnlockedEntry(self.enc.current_position).getSubEntry(self.enc.sub_current_position + self.dir1)]
    self.enc.sub_current_position += self.dir2
    
    renpy.restart_interaction()
 
 #Action that sorts the entries
 class SortEncyclopaedia(Action):
  def __init__(self, encyclopaedia, sorting_mode="Number"):
   self.enc = encyclopaedia
   self.unlocked_entries = self.enc.unlocked_entries
   self.all_entries = self.enc.all_entries
   self.reverse = False
   if sorting_mode == "Z to A":
    self.reverse = True
   self.sortingMode = sorting_mode

  def getKey(self,item):
   if self.sortingMode == "Number":
    return item[0]
   else:
    return item[1].name

  def __call__(self):
   self.enc.unlocked_entries = sorted(self.unlocked_entries, reverse=self.reverse,key=self.getKey)
   self.enc.all_entries = sorted(self.all_entries, reverse=self.reverse,key=self.getKey)
   self.enc.sortingMode = self.sortingMode
   renpy.restart_interaction()
 
 #Action to save the "New!" status of every entry in an encyclopaedia 
 class SaveStatusAction(Action):
  def __init__(self, encyclopaedia, enc_dict, tag_string):
   self.enc = encyclopaedia
   self.enc_dict = enc_dict
   self.tag_string = tag_string
  def __call__(self):
   for x in range(self.enc.size_all):
    self.enc_dict[self.tag_string + str(x)] = self.enc.all_entries[x][1].status   
  
 #Action to call change the "New!" status of an EncEntry
 class ChangeStatusAction(Action): 
  def __init__(self, encyclopaedia, var):
   self.enc = encyclopaedia
   self.var = var
  def __call__(self):
   self.changed_entry = self.enc.getEntry(self.var)
   self.changed_entry.status = True
 
 #Resets the sub-page count to 1. Used when closing the entry screen
 class ResetSubPageAction(Action):
  def __init__(self, encyclopaedia):
   self.enc = encyclopaedia
  
  def __call__(self):
   self.enc.sub_current_position = 1
   renpy.restart_interaction()

 #Action that toggles if locked entries will be shown or not in the list or not.
 class ToggleShowLockedButtonsAction(Action):
  def __init__(self, encyclopaedia):
   self.enc = encyclopaedia
   
  def __call__(self):
   if self.enc.showLockedButtons:
    self.enc.showLockedButtons = False

   else:
    self.enc.showLockedButtons = True
  
   self.enc.setEntryListSize()
   renpy.restart_interaction()

 #Action that toggles if locked entries can be opened or not.
 class ToggleShowLockedEntryAction(Action):
  def __init__(self, encyclopaedia):
   self.enc = encyclopaedia
   
  def __call__(self):
   if self.enc.showLockedEntry:
    self.enc.showLockedEntry = False

   else:
    self.enc.showLockedEntry = True
  
   self.enc.setEntryListSize()
   renpy.restart_interaction()   
    
##############################################################################
# Encyclopaedia
#
# Holds all the EncEntries added to it and manages them 
 class Encyclopaedia(object): 
  def __init__(self, sortingMode = "Subject", showLockedButtons=False, showLockedEntry=False):
   self.subjects= [] #List of all subjects
   self.unlocked_entries = [] #List of unlocked entries
   self.all_entries = [] #List of all entries, regardless of if locked or not 
   self.size = 0  #Hold the length of self.unlocked_entries  
   self.size_all = 0 #Hold the length of self.all_entries  
   self.entry_list_size = 0 #Is either size or size_all, depending on if locked entries are shown
   self.max_size = 0
   
   self.sortingMode = sortingMode #Default type of sorting for list screen. Defaults to "Number"
   
   self.reverseSorting = False
   if sortingMode == "Z to A":
    self.reverseSorting = True
   
   self.showLockedButtons = showLockedButtons #If True, locked entries show "???" on the listing screen. Defaults to True
   self.showLockedEntry = showLockedEntry
  
   self.current_position = 0 #Indicates the current entry open. Is the current position based on the unlocked list.
   self.sub_current_position = 1 #1 because the main entry is the first page in the sub-entry list
  
   self.index_page = 0
   self.index = 0
  
  def setLockedImageTint(self, tint_amount):
   for itemA,itemB in self.all_entries:
    itemB.tintLockedImage((tint_amount[0],tint_amount[1],tint_amount[2]))
  
  def getPercentageUnlocked(self): #Returns string representation of the percentage of the encyclopaedia that's unlocked
   float_size = float(self.size)
   float_size_all = float(self.size_all)
   percentage = floor( (float_size / float_size_all) * 100 )
   return str(int(percentage)) + "%"
  
  def setEntryListSize(self):
   if self.showLockedButtons:
    self.entry_list_size = self.size_all
   else:
    self.entry_list_size = self.size
   
   if self.showLockedEntry:
    self.max_size = self.size_all
  
   else:
    self.max_size = self.size
  
  def getKey(self,item):
   return item[1].name
  
  def unlockEntry(self, item, unlock_flag):
   item.locked = unlock_flag
   self.addEntry(item)
   
  def addEntry(self, item): 
   if not [item.number,item] in self.all_entries:
    self.all_entries.append([item.number,item])
    
   if not [item.number,item] in self.unlocked_entries:
     if item.locked == False:
      self.unlocked_entries.append([item.number,item])
  
   if self.sortingMode == "Number":
    self.unlocked_entries = sorted(self.unlocked_entries,key=itemgetter(0))
    self.all_entries = sorted(self.all_entries,key=itemgetter(0))
   else:
    self.unlocked_entries = sorted(self.unlocked_entries,reverse=self.reverseSorting,key=self.getKey)
    self.all_entries = sorted(self.all_entries,reverse=self.reverseSorting,key=self.getKey)
    
   self.size = len(self.unlocked_entries)
   self.size_all = len(self.all_entries)
   self.setEntryListSize()
 
  def addEntries(self,*new_entries): #Adds multiple new entries at once
   for item in new_entries:
    self.addEntry(item)
   
  def addSubject(self,new_subject): #Adds a new subject to the Encyclopaedia, won't allow duplicates
   if not new_subject in self.subjects:
    self.subjects.append(new_subject)
  
  def addSubjects(self,*new_subjects): #Adds multiple new subjects at once
   for item in new_subjects:
    self.addSubject(item)
     
  def getEntry(self,entry_number): #Returns the entry of the specified entry_number. Used for displaying the buttons
   if self.showLockedButtons:
    return self.all_entries[entry_number][1]
   elif self.showLockedButtons == False:
    return self.unlocked_entries[entry_number][1]
  
  def getAllEntry(self,entry_number): #Returns the entry of entry_number from all_entries list
   return self.all_entries[entry_number][1]
  
  def getUnlockedEntry(self,entry_number): #Returns the entry of entry_number from unlocked_entries list
   return self.unlocked_entries[entry_number][1]
   
  def setEntryData(self, val): #Sets the current Entry Data to show on the entry screen
   if self.showLockedEntry == False:
    self.index_page, self.index = self.getUnlockedEntry(val).number, self.getUnlockedEntry(val)
  
   if self.showLockedEntry:
    self.index_page, self.index = self.getAllEntry(val).number, self.getAllEntry(val)
   
  def getEntryData(self):
   return self.index_page, self.index
  
  #The following all bind Actions to the Encyclopaedia Object
  def PreviousEntry(self, block):
   return ChangeEntryAction(self, -1, block)

  def NextEntry(self, block):
   return ChangeEntryAction(self, 1, block)

  def PreviousPage(self, block):
   return ChangePageAction(self, -2, -1, block)

  def NextPage(self, block):
   return ChangePageAction(self, 0, 1, block)

  def Sort(self, sorting_mode):
   return SortEncyclopaedia(self, sorting_mode)
  
  def SetEntry(self,given_entry):
   return SetEntryAction(self, given_entry) 

  def SaveStatus(self, enc_dict, tag_string):
   return SaveStatusAction(self, enc_dict, tag_string)
  
  def ChangeStatus(self,position):
   return ChangeStatusAction(self,position)
  
  def ResetSubPage(self):
   return ResetSubPageAction(self)
   
  def ToggleShowLockedButtons(self):
   return ToggleShowLockedButtonsAction(self) 

  def ToggleShowLockedEntry(self):
   return ToggleShowLockedEntryAction(self)  
   
##############################################################################
# EncEntry
# 
# Stores Entry content. Has to be added to an Encyclopaedia or else it will do nothing
 class EncEntry(object):
  def __init__(self, number=0, name="Entry Name", text="Entry Text", subject=None, status=None, locked=False, image=None, locked_image=None):  
   self.number = number
   self.name = name
   self.text = text
   self.status = status
   self.subject = subject
   self.locked = locked
   self.locked_name = "???"
   self.locked_text = "???"
   self.locked_image = locked_image
   self.locked_image_tint = (0.0,0.0,0.0) #Tuple used to set the numbers that tintLockedImage() uses to change the colour of a locked image 
   
   self.pages = 0 #holds an integer for the number of pages in the entry
  
   self.hasImage = False  
   if image != None: #If no image is specified, it's assumed the entry was meant to have no image
    self.image = image
    self.hasImage = True  

    if self.locked_image == None: #If no locked image is specified, take the entry image and tint it.
     self.tintLockedImage(self.locked_image_tint)
   
   self.sub_entry_list = [[1,self]]
   self.hasSubEntry = False #Default status for an Entry is to have no sub-entries
  
  def __repr__(self): #Used for debugging purposes.
   return str(self.name)
  
  def getName(self): #If the entry is locked, return "???" instead of the name
   if self.locked or self.locked == None:
    return self.locked_name
   return self.name
  
  def getText(self): #If the entry is locked, return "???" instead of the text
   if self.locked or self.locked == None:
    return self.locked_text
   return self.text
  
  def getImage(self): #If the entry is locked, return the lock image instead of the image
   if self.locked or self.locked == None:
    return self.locked_image
   return self.image   
  
  def tintLockedImage(self, tint_amount):
   if self.hasImage:
    matrix = im.matrix.tint(tint_amount[0],tint_amount[1],tint_amount[2] )
    self.locked_image = im.MatrixColor(self.image, matrix)
  
  def addSubEntry(self,sub_entry): #Adds multiple pages in the form of sub-entries
   if not [sub_entry.number,sub_entry] in self.sub_entry_list:
    if not sub_entry in self.sub_entry_list:
     if sub_entry.locked == False:
      self.sub_entry_list.append([sub_entry.number,sub_entry])
      self.sub_entry_list = sorted(self.sub_entry_list,key=itemgetter(0))
      self.hasSubEntry = True
  
    self.pages = len(self.sub_entry_list)
  
  def addSubEntries(self, *new_sub_entries): #Adds multiple new sub-entries at once
   for item in new_sub_entries:
    self.addSubEntry(item)
 
  def getSubEntry(self,page): #accepts Integer. returns the text on given page 
   return self.sub_entry_list[page][1].text
  
  def unlockSubEntry(self, item, unlock_flag):
   item.locked = unlock_flag
   self.addSubEntry(item)
   self.status = False #If an entry gets sub-entries unlocked, the unread status is restored
         
 #Checks to make sure the entries and pages buttons can't go outside their list index
 def checkMin(check_value, min):
  if check_value <= min:
   return True
  return False
 
 def checkMax(check_value, max):
  if check_value >= max:
   return True
  return False