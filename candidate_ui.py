'''
    written on: August 3, 2022
    filename: candidate_ui.py
    last update: August 23, 2022
    @author: Gus_Maturana
'''

import tkinter as Tr
import tkinter.ttk as ttk #from Tkinter import Tk as ttk
import database as db
import errors as ers
import excel_export as ex
from tkinter.constants import VERTICAL
from tkinter import *
from tkcalendar import *
import random


class candidate_ui:
    
    DB_NAME = 'candiate2'

    def __init__(self, title = 'Title'):
    
        # Create the main window Widget
        # Main application page
        self.dataCols = ('#', 'NAME', 'LAST NAME', 'DEGREE','REQ NUMBER','POSITION','EMAIL ADDRESS',\
                         'CONTACT INFO', 'CLEARANCE', 'INTREVIEW', 'OFFER')
 
        self.root = Tr.Tk()                         # creates a main application window
        self.root.title(title)                      # application window title
        self.root.minsize(width=700, height=500)    # application window size
        self.frame_1 = Tr.Frame(self.root)
        self.frame_2 = Tr.Frame(self.root)
        self.frame_5 = Tr.Frame(self.root)
        self.frame_3 = Tr.Frame(self.root)
        self.frame_4 = Tr.Frame(self.root)
        self.topFrame = Tr.LabelFrame(self.frame_1, text = 'OPTIONS:')
        self.internal_frame = Tr.Frame(self.frame_1)            # to include the search feature
        self.search_frame = Tr.Frame(self.internal_frame)       # to include the search feature
        
        self.records_lable = Tr.Label(self.frame_5, fg = 'blue', text = 'RECORDS')
        
        self.btn_new_candidate = Tr.Button(self.topFrame, \
                                       text  = 'NEW CANDIDATE', command = self.new_candidate_win, width = 12)
        self.btn_candidate_history = Tr.Button(self.topFrame,\
                                        text = 'DELETED', command = self.show_Deleted_history, width = 12)
        self.btn_candidate_data = Tr.Button(self.topFrame,\
                                        text = 'INTERVIEWS', command = self.candidate_interview, width = 12)
        self.btn_close = Tr.Button(self.frame_2,\
                                        text = 'CLOSE', command = self.root.quit)
        self.btn_disposition = Tr.Button(self.topFrame,\
                                        text = 'DISPOSITION', command = self.candidate_history, width = 12)
        
        self.search_entry_lbl = Tr.LabelFrame(self.search_frame, text = 'Criteria: ')

        self.btn_search = Tr.Button(self.search_entry_lbl, bg = "blue",\
                                        text = 'SEARCH', command = self.search_)
        
        self.clear_search_btn = Tr.Button(self.search_entry_lbl, \
                                        text = 'CLEAR', command = self.clear_search)
        

        self.candidatetLbl = Tr.LabelFrame(self.frame_4, text = 'CANDIDATE TABLE')
        self.recordListColumn = ttk.Treeview(self.candidatetLbl,height = 50,columns = self.dataCols, show = 'headings')
        
        # The following lines of codes format the width of the columns inside the treeview (self.recordLIstColumn)
        self.recordListColumn.column(self.dataCols[0], width = 60)
        self.recordListColumn.column(self.dataCols[1], width = 130)
        self.recordListColumn.column(self.dataCols[2], width = 130)
        self.recordListColumn.column(self.dataCols[3], width = 70)
        self.recordListColumn.column(self.dataCols[4], width = 100)
        self.recordListColumn.column(self.dataCols[5], width = 80, anchor='center')
        self.recordListColumn.column(self.dataCols[6], width = 180, anchor='center')
        self.recordListColumn.column(self.dataCols[7], width = 140, anchor='center')
        self.recordListColumn.column(self.dataCols[8], width = 140, anchor='center')
        self.recordListColumn.column(self.dataCols[9], width = 80, anchor='center')
        self.recordListColumn.column(self.dataCols[10], width = 80, anchor='center')
                
        self.search_lbl = Tr.LabelFrame(self.search_frame, text = 'Search By: ')
        choices = ('Select','Number', 'Name','Last Name','Degree','Reg Number','Phone')
        self.selection_box = ttk.Combobox(self.search_lbl, values = choices, state = 'readonly')
        self.selection_box.current(0)
        self.selection_box.grid(column = 0, row = 0)
        
        
        self.search_entry = Tr.Entry(self.search_entry_lbl, width = 40)
        
        # Binding the recordListColumn and search_entry to keyboard buttons
        self.recordListColumn.bind("<Double-Button-1>", self.OnClick)
        self.search_entry.bind("<Return>",self.Event_Driven_Search)
        self.recordListColumn.bind("<Button-2>", self.OnRightClick)
        
        self.candidatetLbl.pack(side = 'top')
        self.recordListColumn.pack(side = 'top')
        
        self.records_lable.pack(side = 'right')
        
        self.btn_new_candidate.pack(side = 'right')
        self.btn_candidate_data.pack(side = 'left')
        self.btn_candidate_history.pack(side = 'left')
        self.btn_disposition.pack(side = 'left')
        self.btn_close.pack(side = 'right')
        
        self.selection_box.pack(side = 'right')
        self.search_lbl.pack(side = 'left')
        self.search_entry_lbl.pack(side = 'right')
        self.clear_search_btn.pack(side = 'right')
        self.btn_search.pack(side = 'right')
        self.search_entry.pack(side = 'left')
        
        # Creates database if it does not exist or open database to connect to it
        db.database().database('candidate2.db')
        db.database().database('recovery.db')
        db.database().candidate_tables('interview.db')
        #inserting values into the record list
        count = 0
        for item in db.database().db_print('candidate2.db'):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue')
        self.yscroll_ = Tr.Scrollbar(orient = VERTICAL, command = self.recordListColumn.yview()) 
        self.yscroll_.grid(row = 0, column = 1, sticky = 'nse')
        self.yscroll_.pack(side = 'right', fill = 'y')
        #self.recordListColumn.configure(command= self.yscroll_.set())
        # the following lines add the name to the title to the columns
        for col in self.dataCols:
            self.recordListColumn.heading(col, text = col.title())
            
        self.frame_1.pack(side = 'top')
        self.frame_2.pack(side = 'bottom')
        self.frame_3.pack(side = 'bottom')
        self.frame_5.pack(side = 'top')
        self.frame_4.pack(side = 'bottom')
        self.topFrame.pack(side = 'top')
        self.internal_frame.pack(side = 'right')
        self.search_frame.pack(side = 'left')
        
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
        
        Tr.mainloop()
    
    # destroys main window
    def destroy_root(self):
        
        self.root.destroy()
    
    # This module creates a new patient
    def new_candidate_win(self, title = 'NEW CANDIDATE'):
        
        title_ = title
        
        self.new_candidate_window = Tr.Tk()                     # creates a new window
        self.new_candidate_window.minsize(700, 400)
        self.new_candidate_window.title(title)
        
        # Creates the lables for the text entries all labels will load before the text entry fields
        self.keyLbl = Tr.Label(self.new_candidate_window, text = 'CANDIDATE #: ', width = 15, justify = RIGHT)
        self.keyLbl.grid(row = 17, column = 0)
        self.nameLbl = Tr.Label(self.new_candidate_window, text = 'NAME: ', width = 15, justify = RIGHT)
        self.nameLbl.grid(row = 18, column = 0)
        self.lastLbl = Tr.Label(self.new_candidate_window, text = 'LAST NAME: ', width = 15, justify = RIGHT)
        self.lastLbl.grid(row = 19, column = 0)
        self.degreeLbl = Tr.Label(self.new_candidate_window, text = 'DEGREE: ', width = 15, justify = LEFT).grid(row = 20, column = 0)
        self.clLable= Tr.Label(self.new_candidate_window, text = 'CLEARANCE: ', width = 15, justify = LEFT).grid(row = 21, column = 0)
        self.reqNumberLbl = Tr.Label(self.new_candidate_window, text = 'REQ NUMBER: ', width = 15, justify = LEFT).grid(row = 22, column = 0)
        self.plevelLable = Tr.Label(self.new_candidate_window, text = 'POSITION LEVEL: ', width = 15, justify = LEFT).grid(row = 23, column= 0)
        self.emailLable = Tr.Label(self.new_candidate_window, text = 'EMAIL: ', width = 15, justify = LEFT).grid(row = 24, column = 0)
        self.cInfoLable = Tr.Label(self.new_candidate_window, text = 'PHONE: ', width = 15, justify = LEFT).grid(row = 25, column = 0)
        self.interviewLable = Tr.Label(self.new_candidate_window, text = 'INTERVIEW: ', width = 15, justify = LEFT).grid(row = 26, column = 0)
        self.offerLable = Tr.Label(self.new_candidate_window, text = 'JOB OFFER:', width = 15, justify = LEFT).grid(row = 27, column = 0)
        
        # Cereates text entries for window
        self.keyEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.keyEntry.grid(row = 17, column=1)
        self.nameEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.nameEntry.grid(row = 18, column =1)
        self.lnameEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.lnameEntry.grid(row = 19, column = 1)
        self.degreeEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.degreeEntry.grid(row = 20, column = 1)
        self.clearEntry = ttk.Combobox(self.new_candidate_window, state = 'readonly', width = 21)
        self.clearEntry.grid(row = 21, column = 1)
        self.clearEntry['values'] = ('Select','None','Secret', 'Top Secret', 'Top Secret/SCI')
        self.clearEntry.current(0)
        self.reqNumberEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.reqNumberEntry.grid(row = 22, column = 1)
        self.pLevelEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.pLevelEntry.grid(row = 23, column = 1)
        self.emailEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.emailEntry.grid(row = 24, column = 1)
        self.contactInfo = Tr.Entry(self.new_candidate_window, width = 23)
        self.contactInfo.grid(row = 25, column = 1)
        self.interviewEntry = ttk.Combobox(self.new_candidate_window, state = 'readonly', width = 21)
        self.interviewEntry.grid(row = 26, column = 1)
        self.interviewEntry['values'] = ('Select', 'YES', 'NO')
        self.interviewEntry.current(0)
        self.offerEntry = ttk.Combobox(self.new_candidate_window, state = 'readonly', width = 21)
        self.offerEntry.grid (row = 27, column = 1)
        self.offerEntry['values'] = ('Select', 'YES', 'NO', 'DISPOSITION','TRASNSFER')
        self.offerEntry.current(0)

        if title_ == 'NEW CANDIDATE':
            self.keyEntry.insert('end', self.unique_key('candidate2.db'))
    
        # Creates a save and close button
        self.save_btn = Tr.Button(self.new_candidate_window, text = 'SAVE', width = 10, command = lambda:self.save_record(title_)).grid(row = 52, column = 4)
        self.cancel_btn = Tr.Button(self.new_candidate_window, text = 'CANCEL', width = 10, command = self.cancel_).grid(row = 52, column = 5)

        # Note grid() won't allow entry fields to be focus()
        #key_= 1 + len(self.recordListColumn.get_children())
        #self.keyEntry.insert('end', key_)
        
    # This is section creates the edit window for the candidate record
    def editCandidate(self, key):
        # the candidate name will be displayed on window title
        title = db.database().get_record('candidate2.db', key)
        #store the value for the specific record that has been clicked
        record_ = db.database().get_candidate('candidate2.db', key)

        self.new_candidate_win(title)
        self.history_btn = Tr.Button(self.new_candidate_window, text = 'Setup Interview', width = 10, command = self.setup_interview).grid(row = 52, column = 3)
        self.delete_btn = Tr.Button(self.new_candidate_window, text = 'Delete', width = 10, command =self.delete_candidate).grid(row = 90, column = 3)
        self.pScreen_btn = Tr.Button(self.new_candidate_window, text = 'Phone Screen', width = 10, command =lambda:self.phone_screen_interview(record_))
        self.pScreen_btn.grid(row = 90, column = 4)

        self.keyEntry.delete(0, Tr.END)
        self.keyEntry.insert('end', record_[0])
        self.nameEntry.insert('end', record_[1])
        self.lnameEntry.insert('end', record_[2])
        self.degreeEntry.insert('end',record_[3])
        self.reqNumberEntry.insert('end', record_[4])
        self.pLevelEntry.insert('end', record_[5])
        self.emailEntry.insert('end', record_[6])
        self.clearEntry.set(record_[7])
        self.contactInfo.insert('end', record_[8])
        self.interviewEntry.set(record_[9])
        self.offerEntry.set(record_[10])
 
    # The following function saves the records to the database
    # The function also checks that none of the Entries are empty or null   
    def save_record(self,title = 'NEW CANDIDATE'):
        title_ = title
                
        if  self.keyEntry.get() == '' or  self.reqNumberEntry.get() == '' or \
            self.degreeEntry.get() == '' or self.emailEntry.get() == '' or \
            self.lnameEntry.get() == '' or self.contactInfo.get() == '':
            if self.nameEntry.get() == '' or self.lnameEntry.get() == '':
                ers.errors().general_error_messages('NAME')
                self.nameLbl.set('NAME:', fg = 'red')
            if self.lnameEntry.get() == '':
                ers.errors().general_error_messages('LAST NAME')
        else:
                key_ = int(self.keyEntry.get())
                name_ = self.nameEntry.get()
                deg_ = self.degreeEntry.get()
                lname_ = self.lnameEntry.get()
                degree_ = self.degreeEntry.get()
                reqn_ = self.reqNumberEntry.get()
                plev_ = self.pLevelEntry.get()
                clear_ = self.clearEntry.get()
                 # in case the phoen number is already formated
                if "(" in self.contactInfo.get():
                        cinfo_ = self.contactInfo.get() 
                else:
                        # formats phone to (###)-###-####
                        cinfo_ = self.phone_format(self.contactInfo.get()) 
                        self.contactInfo.delete(0, Tr.END)
                        self.contactInfo.insert('end', cinfo_)

                email_ = self.emailEntry.get()
                inter_ = self.interviewEntry.get()
                offer_ = self.offerEntry.get()

                if title_ == 'NEW CANDIDATE':
                        # saves the new candidate
                        db.database().insert_record_candidate('candidate2.db', (key_, name_, lname_, degree_, reqn_, \
                                                                                plev_, email_, clear_, cinfo_, inter_, offer_))
                        self.clear_()
                        self.clear_search() # refreshes the treeview to include the new record
                        self.keyEntry.insert('end',self.unique_key('candidate2.db'))
                        print('Saved Record')
                else:
                        # saves the edit
                        record_ = (name_, lname_, deg_, reqn_, plev_, email_, cinfo_, clear_, inter_, offer_, key_)
                        db.database().update_candidate_record('candidate2.db',record_)  
                        self.clear_search() # refreshes the treeview to include the new record
                        ers.errors().error_messages(8)

    # Clear all Entries and focus on nameEntry
    def clear_(self):
        
        self.keyEntry.delete(0, Tr.END)
        self.nameEntry.delete(0, Tr.END)
        self.lnameEntry.delete(0,Tr.END)
        self.degreeEntry.delete(0, Tr.END)
        self.reqNumberEntry.delete(0, Tr.END)
        self.contactInfo.delete(0, Tr.END)
        self.pLevelEntry.delete(0,Tr.END)
        self.nameEntry.focus()
        self.clearEntry.set('Select')
        self.interviewEntry.set('Select')
        self.offerEntry.set('Select')
        self.emailEntry.delete(0,Tr.END)
        self.column_headings()
        self.clear_list()
    
    # Cancels the new new_patient_win
    # This function can only be used with new patient
    def cancel_(self):
        # Destroys the new_candidate_window
        self.new_candidate_window.destroy()
    
    # Deletes candidate record    
    def delete_candidate(self):
        #this function also deletes the candidate personal database

        key_ = int(self.keyEntry.get())
        st = self.nameEntry.get()

        record_ = db.database().get_candidate('candidate2.db', key_)
        
        item = db.database().print_results('candidate2.db', 'ID', self.keyEntry.get())
        print(item)
        result = ers.errors().delete_confirmation(st)
        
        if result == True:
            db.database().insert_record_candidate('recovery.db',record_)
            db.database().remove_record('candidate2.db', 'CANDIDATE', key_)
            
            ers.errors().delete_message(st)
            self.new_candidate_window.destroy()      # Destroys the window
            self.clear_search()                     # Refresh candidate list 
        else:
            self.nameEntry.focus()             # Set focus on edit_nameEntery

    # Deletes canidate record by the use of the popup menu
    def delete_candidate_key(self, value):
 
        record_ = (value[0], value[1], value[2], value[3], value[4], value[5], value[6], 
                   value[7], value[8], value[9], value[10])

        result = ers.errors().delete_confirmation(value[1])
        
        if result == True:
            # saves record in backup database
            db.database().insert_record_candidate('recovery.db',record_)
            # deletes record from original database
            db.database().remove_record('candidate2.db', 'CANDIDATE', int(value[0]))
            ers.errors().delete_message(value[1])

            self.clear_search()                     # Refresh candidate list 
        else:
            print('')

            #self.nameEntry.focus()             # Set focus on edit_nameEntery

    # Cancel the edit
    def cancel_edit(self):
        # Destroys the edit_patient_window
        self.new_candidate_window.destroy()
    
    # Function saves changes made to the patient
    def save_edit(self):
        # Saves the edit record
        key_ = int(self.keyEntry.get())

        name_ = self.nameEntry.get() 
        lname_ = self.lnameEntry.get() 
        deg_ = self.degreeEntry.get()
        req_ = self.reqNumberEntry.get()
        email_ = self.emailEntry.get()

        # in case the phoen number is already formated
        if "(" in self.contactInfo.get():
                cinfo_ = self.contactInfo.get() 
        else:
                # formats phone to (###)-###-####
                cinfo_ = self.phone_format(self.contactInfo.get()) 

        inter_ = self.interviewEntry.get()
        offer_ = self.offerEntry.get()
        
        record_ = (name_, lname_, deg_, req_, email_, cinfo_, inter_, offer_, key_)
        db.database().update_candidate_record('candidate2.db',record_)  
        
        #self.clear_()
        self.clear_search() # refreshes the treeview to include the new record
        self.cancel_edit()
        
    # OnClick opens a new window when a record in the patient list is clicked 
    def OnClick(self, event):
        
        selection = self.recordListColumn.focus()
        value = self.recordListColumn.item(selection).get('values')
        # Opens the edit candidate window
        # and passes the candidate id#
        if db.database().is_record('recovery.db', value[0]) == True:
            ers.errors().restore_message()
        else:
            self.editCandidate(value[0])
        
    # OnRigthClick opens a menu items
    def OnRightClick(self, event):
        # .identify_row(event.y) gets the value store in the treeview
        selection = self.recordListColumn.identify_row(event.y)
        value = self.recordListColumn.item(selection).get('values')

        print(value[9])
        # creates a popup menu and its listed items
        self.my_menu = Menu(self.recordListColumn, tearoff=0)
        if db.database().is_record('recovery.db', value[0]) == True:
            self.my_menu.add_command(label = 'Re-store', command = lambda:self.restore_candidate(value))
            self.my_menu.add_command(label = 'Delete Permanently', command = lambda:self.delete_pernamently(value))
        else:
            self.my_menu.add_command(label = 'Edit', command = lambda:self.editCandidate(value[0]))
            self.my_menu.add_separator()
            if value[9] == 'Disposition':
                self.my_menu.add_command(label = 'Interview', command = lambda:self.setup_interview_tab(value[0]))
            else:
                self.my_menu.add_command(label = 'Dispositon', command = lambda:self.disposition_candidate(value))
            self.my_menu.add_separator()
            if value[9] == 'YES':
                self.my_menu.add_command(label = 'Perform Interview', command = lambda:self.perform_interview(value))
            else:
                self.my_menu.add_command(label = 'Perform Phone Screening', command = lambda:self.phone_screen_interview(value))
            self.my_menu.add_separator()
            self.my_menu.add_command(label = 'Delete', command = lambda:self.delete_candidate_key(value))

        try:
                self.my_menu.tk_popup(event.x_root, event.y_root)
        finally:
                self.my_menu.grab_release()

    # creates a phone screening invertview window
    def phone_screen_interview(self, record_):
        # the candidate name will be displayed on window title
        title = db.database().get_record('candidate2.db', record_[0]) + '\'s Phone Screen'

        self.phone_screen_window = Tr.Tk()                     # creates a new window
        self.phone_screen_window.minsize(700, 600)
        self.phone_screen_window.title(title)

        # Frames
        self.candidateInfo = Tr.Frame(self.phone_screen_window,height = 5)
        self.interviewerInfo = Tr.Frame(self.phone_screen_window)
        self.managementInfo = Tr.Frame(self.phone_screen_window, height = 5)
        self.roleInfo = Tr.Frame(self.phone_screen_window, height = 5)
        self.cCompanyFrame = Tr.Frame(self.phone_screen_window,height = 5)

        self.candidateLbl = Tr.Label(self.candidateInfo, text = 'NAME: ')
        self.candidateLbl.grid(row = 0, column = 0)
        self.candidateEntry = Tr.Entry(self.candidateInfo, width = 23)
        self.candidateEntry.grid(row = 0, column = 1)
        self.phoneLabel = Tr.Label(self.candidateInfo, text = 'PHONE: ')
        self.phoneLabel.grid(row = 0, column = 2)
        self.phoneEntry = Tr.Entry(self.candidateInfo, width = 18)
        self.phoneEntry.grid(row = 0, column = 3)

        self.interviewerLbl = Tr.Label(self.interviewerInfo, text = 'INTERVIEWER: ', width = 10, justify='left')
        self.interviewerLbl.pack(side = 'left')
        self.interviewerEntry = Tr.Entry(self.interviewerInfo, width = 18)
        self.interviewerEntry.pack(side = 'left')
        self.divisionLbl = Tr.Label(self.interviewerInfo, text = 'Sector: ', width = 10, justify = 'left').pack(side = 'left')
        self.divisionEntry = Tr.Entry(self.interviewerInfo, width = 8)
        self.divisionEntry.pack(side = 'left')
        self.dateLbl = Tr.Label(self.interviewerInfo, text = 'DATE: ', width = 10, justify = 'left').pack(side = 'left')
        self.dateEntry = Tr.Entry(self.interviewerInfo, width = 8)
        self.dateEntry.pack(side = 'left')

        self.cCompanyLbl = Tr.Label(self.cCompanyFrame, text = 'CURRENT EMPLOYER: ', width = 23, justify = LEFT)
        self.cCompanyLbl.pack(side = 'left')
        self.cCompanyEntry = Tr.Entry(self.cCompanyFrame, width = 18)
        self.cCompanyEntry.pack(side = 'left')

        self.notesFrame_1 = Tr.Frame(self.phone_screen_window, width = 100, height = 3)
        motivation = 'JOB MOTIVATION (Job Interest/Reason for Looking/Career Goals/Expectations for Position)'
        self.notesLbl_1 = Tr.Label(self.notesFrame_1, text = motivation)
        self.notesLbl_1.pack(side = 'left')
        self.notesEntry_1 = Tr.Text(self.phone_screen_window, width = 100, height = 6)
        self.notesFrame_2 = Tr.Frame (self.phone_screen_window, width = 100, height = 3)
        technical = 'TECHNICAL: Ask questions seeking the candidate\'s technical accomplishments in the last few years,' + \
                    '\nfocusing on completed tasks and achieved goals. Look for results as well as demonstrated skills.' + \
                    '\nIn which technical skills and tools are you most proficient? Examples? What level of independence' + \
                    '\nare you comfortable working with? Examples? What size projects/teams do you work with or lead?'
        self.notesLabl_2 = Tr.Label(self.notesFrame_2, text = technical, justify = LEFT)
        self.notesLabl_2.pack(side = 'left')
        self.notesEntry_2 = Tr.Text(self.phone_screen_window, width = 100, height = 6)
        self.notesFrame_3 = Tr.Frame (self.phone_screen_window, width = 100, height = 3)
        management = 'Determine whether the candidate has worked in groups and holds any kind of leadership' + \
                     '\nrole with one or more subordinates. Determine the nature/exent of the candidate\'s' + \
                     '\nleadership experience (administrative, technical etc).'
        self.notesLabl_3 = Tr.Label(self.notesFrame_3, text = management, justify = LEFT)
        self.notesLabl_3.pack(side = 'left')
        self.notesEntry_3 = Tr.Text(self.phone_screen_window, width = 100, height = 6)

        select = 'MANAGEMENT: Does the position require management skills/experience?: '
        self.managementLbl = Tr.Label(self.managementInfo, text = select)
        self.managementLbl.pack(side = 'left')
        self.managementEntry = ttk.Combobox(self.managementInfo, state = 'readonly', width = 10)
        self.managementEntry['value'] = ('Select','Yes', 'No')
        self.managementEntry.current(0)
        self.managementEntry.pack(side = 'left')
        self.roleLbl = Tr.Label(self.roleInfo, text = 'Potential Level/Role:')
        self.roleLbl.pack(side = 'left')
        self.role_ = ttk.Combobox(self.roleInfo, state = 'readonly', width = 10)
        self.role_['values'] = ('L1','L2','L3','L4','L5','L6','L7')
        self.role_.pack(side = 'left')
        self.reqLbl = Tr.Label(self.roleInfo, text = 'REQ#')
        self.reqLbl.pack(side = 'left')
        self.req_ = Tr.Entry(self.roleInfo, width = 18)
        self.req_.pack(side = 'left')

        self.notesFrame_4 = Tr.Frame(self.phone_screen_window, width = 100, height = 3)
        overall_ = 'OVERALL ASSESMENT OF THE CANDIDATE: Describe competencies, achievements and/or developmental' +\
                   '\nneeds for professional/experience background that support your recommendation'
        self.notesLbl_4 = Tr.Label(self.notesFrame_4, text = overall_, justify = LEFT)
        self.notesLbl_4.pack(side = 'top')
        self.notesEntry = Tr.Text(self.notesFrame_4,width = 100, height = 6)
        self.notesEntry.pack(side = 'bottom')

        self.recommendationSelect = ttk.Combobox(self.phone_screen_window, state = 'readonly', width = 21)
        self.recommendationSelect['values'] = ('Select','INTERVIEW','DISPOSITION')
        self.recommendationSelect.current(0)

        if self.find_phone_screen('interview.db', record_[0]) == False:   
            self.candidateEntry.insert('end', record_[1] + " " + record_[2])
            self.phoneEntry.insert('end', record_[8])
            self.req_.insert('end', record_[4])
            self.role_.set(record_[5])
        else:
            rcd_ = db.database().get_phone_screen('interview.db', record_[0])
            self.candidateEntry.insert('end', rcd_[1] + " " + rcd_[2])
            self.phoneEntry.insert('end', rcd_[3])
            self.interviewerEntry.insert('end',rcd_[4])
            self.req_.insert('end',rcd_[15])
            self.role_.set(rcd_[14])
            self.dateEntry.insert('end', rcd_[5])
            self.cCompanyEntry.insert('end',rcd_[7])
            self.divisionEntry.insert('end',rcd_[6])
            self.notesEntry_1.insert('end',rcd_[8])
            self.notesEntry_2.insert('end',rcd_[9])
            self.managementEntry.set(rcd_[10])
            self.notesEntry_3.insert('end',rcd_[11])
            self.recommendationSelect.set(rcd_[12])
            self.notesEntry.insert('end',rcd_[13])

        self.saveNotesBtn = Tr.Button(self.phone_screen_window, text = 'SAVE', width = 20, command = lambda:self.save_phone_screen('interview.db', record_[0]))

        self.saveNotesBtn.pack(side = 'bottom')
        self.recommendationSelect.pack(side = 'bottom')
        self.roleInfo.pack(side = 'bottom')
        self.notesFrame_4.pack(side = 'bottom')
        self.notesEntry_3.pack(side = 'bottom')
        self.notesFrame_3.pack(side = 'bottom')
        self.managementInfo.pack(side = 'bottom')
        self.notesEntry_2.pack(side = 'bottom')
        self.notesFrame_2.pack(side = 'bottom')
        self.notesEntry_1.pack(side = 'bottom')
        self.notesFrame_1.pack(side = 'bottom')
        self.cCompanyFrame.pack(side = 'bottom')
        self.interviewerInfo.pack(side = 'bottom')
        self.candidateInfo.pack(side = 'top') 

    # saves the phone screen form an creates a excel form
    def save_phone_screen(self, db_name, key_):
        name_ = self.candidateEntry.get().split(' ')
        record_ = (int(key_), 
                    name_[0], name_[1], self.phoneEntry.get(), self.interviewerEntry.get(), self.dateEntry.get(), 
                    self.divisionEntry.get(), self.cCompanyEntry.get(), self.notesEntry_1.get("1.0","end-1c"), 
                    self.notesEntry_2.get("1.0","end-1c"), self.managementEntry.get(), self.notesEntry_3.get("1.0","end-1c"),
                    self.recommendationSelect.get(), self.notesEntry.get("1.0","end-1c"), self.role_.get(), self.req_.get())
        
        if self.find_phone_screen('interview.db', int(key_)) == False:
            db.database().insert_record_phone_screen(db_name, record_)
            ex.export_to_excel().export_to_form(db_name,record_) # creates excel file
        else:
            # the format a record is different from record_ because the key is the last item in the edit record
            record = (name_[0], name_[1], self.phoneEntry.get(), self.interviewerEntry.get(), self.dateEntry.get(), 
                     self.divisionEntry.get(), self.cCompanyEntry.get(), self.notesEntry_1.get("1.0","end-1c"), 
                     self.notesEntry_2.get("1.0","end-1c"), self.managementEntry.get(), self.notesEntry_3.get("1.0","end-1c"),
                     self.recommendationSelect.get(), self.notesEntry.get("1.0","end-1c"), self.role_.get(), self.req_.get(),
                     int(key_))
            db.database().update_phone_screen_record(db_name,record)
            ex.export_to_excel().export_to_form(db_name,record_)
        
    # function needed to sets up interviews
    def setup_interview(self):

        # Creates calendar picker
        self.cal = DateEntry(self.new_candidate_window, selectmode = "day", width = 21)
        self.cal.grid(row = 17, column = 4 )

        # Creates the lables for the text entries all labels will load before the text entry fields
        self.dateLbl = Tr.Label(self.new_candidate_window, text = 'INTERVIEW DATE: ', width = 15, justify = 'left')
        self.dateLbl.grid(row = 17, column = 3)
        self.timeLbl = Tr.Label(self.new_candidate_window, text = 'INTERVIEW TIME: ', width = 15, justify = 'left')
        self.timeLbl.grid(row = 18, column = 3)
        self.proLbl = Tr.Label(self.new_candidate_window, text = 'PROGRAM: ', width = 15, justify = 'left')
        self.proLbl.grid(row = 19, column = 3)
        self.proPocLbl = Tr.Label(self.new_candidate_window, text = 'PORGRAM POC: ', width = 15, justify = 'left')
        self.proPocLbl.grid(row = 20, column = 3)
        self.commentsLbl = Tr.Label(self.new_candidate_window, text = 'COMMENTS ', width = 15, justify = 'right')
        self.commentsLbl.grid(row = 21, column = 3)
        self.timeEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.timeEntry.grid(row = 18, column =4)
        self.programEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.programEntry.grid(row = 19, column =4)
        self.pPocEntry = Tr.Entry(self.new_candidate_window, width = 23)        
        self.pPocEntry.grid(row = 20, column = 4)
        self.commentsEntry = Tr.Entry(self.new_candidate_window, width = 23)
        self.commentsEntry.grid(row = 21, column = 4)

    # opens up the window to set up an interview
    def setup_interview_tab(self, key_):
        self.editCandidate(key_)
        self.setup_interview()

    # opens up the window with the interview form
    def perform_interview(self, value_):
        title = value_[1] + " " + value_[2] + '\'s Interview'
        self.interview_form = Tr.Tk()                     # creates a new window
        self.interview_form.minsize(800, 600)
        self.interview_form.title(title)
        self.topFrame = Tr.Frame(self.interview_form, width = 110)
        self.topFrame.pack(side = 'top')

        self.clabel = Tr.Label(self.topFrame, text = 'CANDIDATE NAME: ', width = 20, justify = RIGHT)
        self.clabel.grid(row = 10, column = 0)
        self.nameInput = Tr.Entry(self.topFrame, width = 20, justify = RIGHT)
        self.nameInput.grid(row = 10, column = 1)
        self.dateL = Tr.Label(self.topFrame, text = 'DATE: ', width = 20, justify = RIGHT)
        self.dateL.grid(row = 10, column = 3)
        self.dateE = Tr.Entry(self.topFrame, width = 20, justify = RIGHT)
        self.dateE.grid(row = 10, column = 4)
        self.interviewersLbl= Tr.Label(self.topFrame, text = 'INTERVIEWERS:', width = 20, justify = RIGHT )
        self.interviewersLbl.grid(row = 11, column= 0)
        self.interviewersEntry = Tr.Entry(self.topFrame, width = 20, justify = RIGHT)
        self.interviewersEntry.grid(row = 11, column = 1)
        self.reqL = Tr.Label(self.topFrame, text = 'REQUISITION #: ', width = 20, justify = RIGHT)
        self.reqL.grid(row = 12, column = 0)
        self.reqE = Tr.Entry(self.topFrame, width = 20, justify = RIGHT)
        self.reqE.grid(row = 12, column = 1)
        self.recommendationL = Tr.Label(self.topFrame, text = 'RECOMMENDATION FOR HIRE', width = 24, justify = RIGHT)
        self.recommendationL.grid(row = 16, column = 0)
        self.recommendationE = ttk.Combobox(self.topFrame, state = 'readonly', width = 16)
        self.recommendationE.grid(row = 16, column = 1)
        self.recommendationE['values'] = ('Select','Offer', 'No offer', 'Dispositon')
        self.recommendationE.current(0)
        self.levelRecomendation = Tr.Label(self.topFrame, text = 'LEVEL RECOMMENDATION', width = 24, justify = RIGHT)
        self.levelRecomendation.grid(row = 17, column = 0)
        self.levelCombobox = ttk.Combobox(self.topFrame, state = 'readonly', width = 16)
        self.levelCombobox.grid(row = 17, column = 1)
        self.levelCombobox['values'] = ('Select', 'L1', 'L2', 'L3', 'L4','L5', 'L6', 'L7')
        self.levelCombobox.current(0)
        self.label1 = Tr.Label(self.interview_form, text = 'Candiate\'s Technical Strenghts', justify = LEFT)
        self.label1.pack(side = 'top')
        self.text1 = Tr.Text(self.interview_form, width = 100, heigh = 6)
        self.text1.pack(side = 'top')
        self.label2 = Tr.Label(self.interview_form, text = 'Needs inmplentation', justify = LEFT)
        self.label2.pack(side = 'top')
        self.text2 = Tr.Text(self.interview_form, width = 100, heigh =6)
        self.text2.pack(side = 'top')
        self.middleFrame = Tr.Frame(self.interview_form,)
        self.label3 = Tr.Label(self.interview_form, text = 'Needs inmplentation', justify = LEFT)
        self.label3.pack(side = 'top')
        self.text3 = Tr.Text(self.interview_form, width = 100, heigh =6)
        self.text3.pack(side = 'top')
        self.label4 = Tr.Label(self.interview_form, text = 'Needs inmplentation', justify = LEFT)
        self.label4.pack(side = 'top')
        self.label4 = Tr.Label(self.interview_form, text = 'Needs inmplentation', justify = LEFT)
        self.label4.pack(side = 'top')
        self.text4= Tr.Text(self.interview_form, width = 100, heigh =6)
        self.text4.pack(side = 'top')
        self.label5 = Tr.Label(self.interview_form, text = 'Needs inmplentation', justify = LEFT)
        self.label5.pack(side = 'top')
        self.text4 = Tr.Text(self.interview_form, width = 100, heigh =6)
        self.text4.pack(side = 'top')




    # candidate will be disposition
    def disposition_candidate(self, value_):
        # saves the new candidate
        record_ =(value_[1], value_[2], value_[3], value_[4], \
                 value_[5], value_[6], value_[8], value_[7], 'Disposition', 'NO', int(value_[0]))

        # saves the edit
        db.database().update_candidate_record('candidate2.db',record_)  
        self.clear_search() # refreshes the treeview to include the new record
        ers.errors().error_messages(9)

    # This particular function may not be needed
    def candidate_history(self):

        id_ = 'INTERVIEW'
        self.search_items(id_, 'DISPOSITION')

    # List candidates that have interviews to set up
    def candidate_interview(self):
        id_ = 'INTERVIEW'
        self.search_items(id_, 'YES')

    # List candidates that have been deleted
    def candidate_deleted(self):
        count = 0
        for item in db.database().db_print('recovery.db'):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))

    # restores the candidate that has been deleted
    def restore_candidate(self, record_):
        db.database().insert_record_candidate('candidate2.db',record_)
        db.database().remove_record('recovery.db', 'CANDIDATE', int(record_[0]))
        self.show_Deleted_history()

    # delte record permanently
    def delete_pernamently(self, record_):
        db.database().remove_record('recovery.db', 'CANDIDATE', int(record_[0]))
        ers.errors().delete_message(record_[1])
        self.show_Deleted_history()
    # Clears the recordListColum
    def clear_list(self):
    #this process can be done two ways
        # way # 1
        for item in self.recordListColumn.get_children():
            self.recordListColumn.delete(item)
        # way #2
        ''' self.reordListColumn.delete(*self.recordListColumn.get_children())
        '''
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))   

    # Opens the search window    
    def search_(self):
        #or  self.selection_box.get() == 'Select'
        if  self.search_entry.get() == '' : 
            if self.search_entry.get() == '':
                ers.errors().general_error_messages('NAME')
            if self.selection_box.get() == 'Select':
                ers.errors().general_error_messages('Please select a search criteria')
        else:
            if self.selection_box.get() == 'Number':
                #To check that patient number is integer
                if self.IsAnInt(self.search_entry.get()) == True:
                    id_ = 'ID'
                    self.search_items(id_, self.search_entry.get())
                else:
                    ers.errors().integer_error(self.search_entry.get())
            if self.selection_box.get() == 'Name':
                id_ = 'NAME'
                self.search_items(id_, self.search_entry.get())
            if self.selection_box.get() == 'Last Name':
                id_ = 'LASTNAME'
                self.search_items(id_, self.search_entry.get())
            if self.selection_box.get() == 'Degree':
                id_ = 'DEGREE'
                self.search_items(id_, self.search_entry.get())
            if self.selection_box.get() == 'Req Number':
                id_ = 'REQNUMBER'
                self.search_items(id_, self.search_entry.get())
            if self.selection_box.get() == 'Email':
                id_= 'EMAILADDRESS'
                self.search_items(id_, self.search_entry.get())
            if self.selection_box.get() == 'Phone':
                id_ = 'CONTACTINFO'
                if len(str(self.search_entry.get())) < 8:
                    self.search_items(id_, str(self.search_entry.get()))
                else:
                    self.search_items(id_,str(self.phone_format(self.search_entry.get())))
    
    #search_items function looks for specific items        
    def search_items(self, name, key):
        self.clear_list() # clear the list
        count = 0
        for item in db.database().print_results('candidate2.db', name, key):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
                        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue') 
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
        count = 0  
        
    def general_search_items(self, key):
        self.clear_list() # clear the list
        count = 0
        # This is just a test for my new function
        self.col_headers(self.general_query_statement_a())
        for item in db.database().db_general_print('candidate2.db', self.general_query_statement_a()):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
                        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue') 
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
        count = 0   
        
    def specific_search(self, key):
        self.clear_list() # clear the list
        count = 0
        # Names column headers to display results
        self.col_headers(key)
        
        # displays results
        for item in db.database().db_general_print('candidate2.db', key):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
                        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue') 
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
        count = 0    
    
    # Clears the search criteria 
    # this helper function can also be used to refresh the patient list after a patient
    # has been added or updated        
    def clear_search(self):
        
        self.selection_box.current(0)       #selection_box goes back to its default value
        self.search_entry.delete(0, Tr.END)
        self.clear_list()
        count = 0
        for item in db.database().db_print('candidate2.db'):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
                        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue') 
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
        count = 0
        self.column_headings()
    
    # The following helper function helps to check for integer
    def IsAnInt(self, key):
             
        try:
            int(key)
            return True
        except ValueError:
            return False
    
    # this functions splits any sentence and returns and array
    def sentence_split(self, phrase, where):
        
        wds = phrase.split(where)
        return wds
    
    # this is an even driven search, when the user presses enter        
    def Event_Driven_Search(self, event):
        self.search_()

    # show_patient_history will display the PATIENT_HIS table when the PATIENT HISTORY button is pressed
    def show_Deleted_history(self, db_ ='recovery.db'):
        self.clear_list() # clear the list
        cnt = 0
        for item in db.database().db_print(db_):
            cnt = cnt + 1
            if cnt % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))            
        self.recordListColumn.tag_configure('oddrow', background = 'yellow') 
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))
    
    # column_headings will display the database default table: CANDIDATE   
    def column_headings(self):
        # clear columns first
        self.clear_list()

        count = 0
        for item in db.database().db_print('candidate2.db'):
            count = count + 1
            if count % 2 != 0:
                self.recordListColumn.insert('', 'end', values=item, tags = ('oddrow',))
            else:
                self.recordListColumn.insert('', 'end', values=item, tags = ('evenrow',))
        
        #colors the row
        self.recordListColumn.tag_configure('oddrow', background = 'lightblue')   
        self.records_lable.config(text = "TOTAL RECORDS: " + str(len(self.recordListColumn.get_children())))

        # LAST NAME', 'NAME', 'DEGREE','REQ NUMBER','EMAIL ADDRESS', 'CONTACT INFO', 'INTERVIEW', 'OFFER')

    def general_query_candidate(self, key_):
        condition = "SELECT ID, NAME, LASTNAME, DEGREE, REQNUMBER, POSITION, EMAILADDRESS, CLEARANCE, CONTACTINFO, INTERVIEW, OFFER\
                        FROM  CANDIDATE \
                        WHERE UPPER(ID) LIKE '%" + (key_).upper() + "%'" +  \
                           "OR UPPER(NAME) LIKE ''%" + (key_).upper() + "%'" +  \
                           "OR UPPER(LASTNAME) LIKE '%" + (key_).upper() + "%'"  + \
                           "OR UPPER(DEGREE) LIKE '%" + (key_).upper()  + "%'"  + \
                           "OR UPPER(REQNUMBER) LIKE '%" + (key_).upper()  + "%'"  + \
                           "OR UPPER(POSITION) LIKE '%" +(key_).upper() + "%" + \
                           "OR UPPER(EMAILADDRESS) LIKE '%" + (key_).upper()  + "%'"  + \
                           "OR UPPER(CLEARANCE) LIKE '%" + (key_).upper() + "%" + \
                           "OR UPPER(CONTACTINFO) LIKE '%" + (key_).upper()  + "%'" + \
                           "OR UPPER(INTERVIEW) LIKE '%" + (key_).upper()  + "%'" +\
                           "OR UPPER(OFFER) LIKE '%" + (key_).upper()  + "%'"
                
        return condition
    
    def general_query_phone_screen(self, key_):
        condition = "SELECT * \
                        FROM PHONE_SCREENING \
                        WHERE ID_KEY_PRIMARY == '%d'" % (key_)
        return condition
        
    # col_headers gets the column headers from the statement
    def col_headers(self, statement):
        result = []
        list_ = statement.split(' ')
        
        # the following loop only adds the column names and ignore other characters inside the list
        for c in list_:
            if c == 'FROM':
                break
            if c == "":
                continue
            if c == "\n":
                continue
            else:
                result.append(c)
                 
        cnt = 0       
        # column titles
        for val in result[1:len(result)]:
            l_ = val.split('.')
            
            if cnt < (len(result) -1):
                self.recordListColumn.heading(self.dataCols[cnt], text = l_[1].replace(',', ''))
            else:
                self.recordListColumn.heading(self.dataCols[cnt], text = l_[1])
            cnt = cnt + 1
        
        # column widths
        if len(result) < 7:
            for n in range (0, len(result)):
                self.recordListColumn.column(self.dataCols[n], width = 100)
            for n in range(len(result)-1,len(result)+(7-len(result))):
                self.recordListColumn.heading(self.dataCols[n], text = '')
        else:
            for n in range(0, len(result)-1):
                self.recordListColumn.column(self.dataCols[n], width = 100)
     

    # formats phone to (###)-###-#### 
    def phone_format(self, str_):

        return "("+str_[0:3]+")-" + str_[3:6] + "-" + str_[6:10]

    # creates a four didit random number and then compares to keys in the db
    def unique_key(self, db_):

        key_ = random.randint(1047,9999)

        for item in db.database().db_print(db_):
            if key_ == item[0]:
                unique_key(db_)

        return key_    

    # returns true if the phone screening has been performed
    def find_phone_screen(self, db_name, key_):
        return db.database().get_phone_exist(db_name,key_)




