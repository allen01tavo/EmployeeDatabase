'''
    Created on December 19, 2023
    filename: setup_schedule.py
    @author: Gus_Maturana
'''

import tkinter as Tr
import tkinter.ttk as ttk #from Tkinter import Tk as ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import random
import database as db
import email as mainl
from datetime import datetime
from tktimepicker import AnalogPicker, AnalogThemes


class scheduler:

    def __init__(self, title):

        self.root = Tr.Tk()                         # creates a main application window
        self.root.title(title)                      # application window title
        self.root.minsize(width=400, height=200)    # application window size


        # Creates the lables for the text entries all labels will load before the text entry fields
        self.dateLbl = Tr.Label(self.root, text = 'INTERVIEW DATE: ', width = 15, justify = 'left')
        self.dateLbl.grid(row = 18, column = 3)
        
        self.timeLbl = Tr.Label(self.root, text = 'INTERVIEW TIME: ', width = 15, justify = 'left')
        self.timeLbl.grid(row = 20, column = 3)
        
        self.proLbl = Tr.Label(self.root, text = 'PROGRAM: ', width = 15, justify = 'left')
        self.proLbl.grid(row = 22, column = 3)
        
        self.proPocLbl = Tr.Label(self.root, text = 'PORGRAM POC: ', width = 15, justify = 'left')
        self.proPocLbl.grid(row = 24, column = 3)
        
        self.commentsLbl = Tr.Label(self.root, text = 'COMMENTS ', width = 15, justify = 'right')
        self.commentsLbl.grid(row = 26, column = 3)
        
        self.timeEntry = Tr.Entry(self.root, width = 14)
        self.timeEntry.bind("<Button-1>", self.OnClick_Time)
        self.timeEntry.grid(row = 20, column = 4)

        self.date_entry = Tr.Entry(self.root, width = 14)
        self.date_entry.bind("<Button-1>", self.OnClick_Date)
        self.date_entry.grid(row = 18, column = 4)

        self.root.bind("<Button-1>", self.Close_time_picker)
        Tr.mainloop()


    # destroys main window
    def destroy_root(self):
        self.root.destroy()

    # Calendar function 1
    def Calendar_Click(self, event):
        date = str(self.cal.get_date())
        self.date_entry.delete(0,END)
        self.date_entry.insert('end', date)
        self.cal_win.destroy()
        #self.cal.destroy()

    # Calendar function 2
    def OnClick_Date(self,event):
        self.cal_win = Tr.Tk()
        self.cal_win.title("Pick A Date")
        self.cal = Calendar(self.cal_win,pos_x=0, pos_y=0, foreground='white', background='red')
        #binds the mouse click to the selected date in the calendar
        self.cal.bind('<<CalendarSelected>>',self.Calendar_Click)
        self.cal.pack()
     
    # Selecting the times function 1   
    def OnClick_Time(self, event):
        self.time_picker = AnalogPicker(self.root)
        self.time_picker.pack()

    def Time_Click(self, event):
        time = str(self.time_picker.getHours()) + ":" + str(self.time_picker.getMinutes())
        self.timeEntry.delete(0,END)
        self.timeEntry.insert('end', time)

    def Close_time_picker(self, event):
        if self.time_picker.winfo_viewable():
            self.time_picker.destroy()
        else:
            pass

def main():
    scheduler('Setup Schedule')


if __name__ == '__main__':
    main()
