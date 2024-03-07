'''
    written on: August 3, 2022
    filename: candidate_ui.py
    last update: September 20, 2022
    @author: Gus_Maturana
'''


import tkinter as Tr
import tkinter.ttk as ttk #from Tkinter import Tk as ttk
import database as db
import errors as ers
from tkinter.constants import VERTICAL
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date
import excel_export as ex
import random

class interview:  

    def __init__(self):
        '''
        '''

    # opens up the window with the interview form
    def perform_interview(self, record_, flag = True):
        if flag == True:
            title = db.database().get_record('candidate2.db', record_[1]) + '\'s Phone Screen'
        else:
            title = db.database().get_record('candidate2.db', record_[0]) + '\'s Phone Screen'
        self.interview_form = Tr.Tk()                     # creates a new window
        self.interview_form.minsize(800, 600)
        self.interview_form.title(title)
        self.leftFrame = Tr.Frame(self.interview_form, width =300)
        self.leftFrame.pack(side = 'left')
        self.topFrame = Tr.Frame(self.leftFrame, width = 110)
        self.topFrame.pack(side = 'top')
        self.rcFrame = Tr.LabelFrame(self.leftFrame,text = 'Overall')
        self.rightFrame = Tr.Frame(self.interview_form, width = 110, height = 600)
        self.rightFrame.pack(side = 'right')

        self.clabel = Tr.Label(self.topFrame, text = 'CANDIDATE NAME: ', width = 20, justify = LEFT)
        self.clabel.grid(row = 10, column = 0)
        self.nameInput = Tr.Entry(self.topFrame, width = 20, justify = LEFT)
        self.nameInput.grid(row = 10, column = 1)
        self.dateL = Tr.Label(self.topFrame, text = 'DATE: ', width = 16, justify = LEFT)
        self.dateL.grid(row = 10, column = 3)
        self.dateE = Tr.Entry(self.topFrame, width = 20, justify = LEFT)
        self.dateE.grid(row = 10, column = 4)
        self.interviewersLbl= Tr.Label(self.topFrame, text = 'INTERVIEWERS:', width = 20, justify = LEFT )
        self.interviewersLbl.grid(row = 11, column= 0)
        self.interviewersEntry = Tr.Entry(self.topFrame, width = 20, justify = LEFT)
        self.interviewersEntry.grid(row = 11, column = 1)
        self.reqL = Tr.Label(self.topFrame, text = 'REQUISITION #: ', width = 20, justify = LEFT)
        self.reqL.grid(row = 12, column = 0)
        self.reqE = Tr.Entry(self.topFrame, width = 20, justify = LEFT)
        self.reqE.grid(row = 12, column = 1)
        self.recommendationL = Tr.Label(self.topFrame, text = 'RECOMMENDATION FOR HIRE', width = 24, justify = RIGHT)
        self.recommendationL.grid(row = 16, column = 0)
        self.recommendationE = ttk.Combobox(self.topFrame, state = 'readonly', width = 18)
        self.recommendationE.grid(row = 16, column = 1)
        self.recommendationE['values'] = ('Select','Offer', 'No offer', 'Dispositon')
        self.recommendationE.current(0)
        self.levelRecomendation = Tr.Label(self.topFrame, text = 'LEVEL RECOMMENDATION:', width = 24, justify = RIGHT)
        self.levelRecomendation.grid(row = 17, column = 0)
        self.levelCombobox = ttk.Combobox(self.topFrame, state = 'readonly', width = 18)
        self.levelCombobox.grid(row = 17, column = 1)
        self.levelCombobox['values'] = ('Select', 'L1', 'L2', 'L3', 'L4','L5', 'L6', 'L7')
        self.levelCombobox.current(0)
        self.lable1Frame = Tr.LabelFrame(self.leftFrame,text = 'Candidate\'s Technical Strenghts')
        self.lable1Frame.pack(side = 'top')
        self.text1 = Tr.Text(self.lable1Frame, width = 100, heigh = 3)
        self.text1.pack(side = 'top')
        self.lable2Frame = Tr.LabelFrame(self.leftFrame,text = 'Candidate\'s Technical Needs')
        self.lable2Frame.pack(side = 'top')

        self.text2 = Tr.Text(self.lable2Frame, width = 100, heigh = 3)
        self.text2.pack(side = 'top')
        self.rcFrame.pack(side = 'top')
        self.middleFrame = Tr.Frame(self.leftFrame, width = 100)
        self.rExpLabel = Tr.Label(self.rcFrame, text = 'RELATABLE EXPERICE: ')
        self.rExpLabel.grid(row = 0, column = 0)
        self.rcExpComboBox = ttk.Combobox(self.rcFrame, state = 'readonly', width = 16)
        self.rcExpComboBox['values'] = ('Select', 'Outstanding', 'Satisfactory', 'Needs Improvement', 'Not Applicable')
        self.rcExpComboBox.grid(row = 0, column = 1)
        self.rcExpComboBox.current(0)
        self.commSkillsLabel = Tr.Label(self.rcFrame, text = 'COMMUNICATION SKILLS: ')
        self.commSkillsLabel.grid(row = 1, column = 0)
        self.commSkillsComboBox = ttk.Combobox(self.rcFrame, state = 'readonly', width = 16)
        self.commSkillsComboBox['values'] = ('Select', 'Outstanding', 'Satisfactory', 'Needs Improvement', 'Not Applicable')
        self.commSkillsComboBox.grid(row = 1, column = 1)
        self.commSkillsComboBox.current(0)
        self.techApSkillsLabel = Tr.Label(self.rcFrame, text = 'TECHNICAL APTITUDE/SKILLS: ')
        self.techApSkillsLabel.grid(row = 2, column = 0)
        self.techApSkillsComboBox = ttk.Combobox(self.rcFrame, state = 'readonly', width = 16)
        self.techApSkillsComboBox['values'] = ('Select', 'Outstanding', 'Satisfactory', 'Needs Improvement', 'Not Applicable')
        self.techApSkillsComboBox.grid(row = 2, column = 1)
        self.techApSkillsComboBox.current(0)
        self.knowLabel = Tr.Label(self.rcFrame, text = 'KNOWLEDGE OF INDUSTRY/ FUNCTION/EDUCATION: ')
        self.knowLabel.grid(row = 3, column = 0)
        self.knowComboBox = ttk.Combobox(self.rcFrame, state = 'readonly', width = 16)
        self.knowComboBox['values'] = ('Select', 'Outstanding', 'Satisfactory', 'Needs Improvement', 'Not Applicable')
        self.knowComboBox.grid(row = 3, column = 1)
        self.knowComboBox.current(0)

        str_label = 'PLEASE DISCUSS AT LEAST 2 OF THE FOLLOWING VALUE OBJECTIVES AND USE THESE QUESTIONS AS GUIDE\n' + \
                    'QUESTIONS AS GUIDE FOR YOUR BEHAVIORAL PORTION OF THE INTERVIEW'
        str_label2 = 'INTEGRITY - we never compromise our values in pursuit of business performance and sucess.\n' + \
                     'Discuss a time when your integrity was challenged. How did you handle it? Tell me about a\n' + \
                     'business situation when you felt honesty was inappropriate. Why? What did you do?'
        self.label3 = Tr.Label(self.leftFrame, text = str_label, justify = LEFT)
        self.label3.pack(side = 'top')
        self.lable3Frame = Tr.LabelFrame(self.leftFrame,text = str_label2)
        self.lable3Frame.pack(side = 'top')
        self.text3 = Tr.Text(self.lable3Frame, width = 100, heigh = 3)
        self.text3.pack(side = 'top')
        str_label3 = 'EXCELLENCE - we work relentlessly to obtain the highest quality result through continuous and flawles execution'
        str_label4 = 'Can you tell me about a time you made a mistake at work and how you recovered? When have you seen your \n' + \
                     'tenacity or resilience rally pay off in a professional setting? What was the outcome'
        self.label4 = Tr.Label(self.leftFrame, text = str_label3, justify = LEFT)
        self.label4.pack(side = 'top')
        self.lable4Frame = Tr.LabelFrame(self.leftFrame,text = str_label4)
        self.lable4Frame.pack(side = 'top')
        self.text4 = Tr.Text(self.lable4Frame, width = 100, heigh = 3)
        self.text4.pack(side = 'top')
        str_label5 = 'RESPECT - we realize that success comes from diverse ideas and talent working together to achieve our goals.\n' + \
                     'Describe a situation werhe others you were working with on a project disagreed with your ideas. What did you\n' + \
                     'do? Describe a situation in which you had to arrive at a compromise or help others to compromise. What was your\n' + \
                     'role? What steps did you take? What was the result?'
        self.label5 = Tr.LabelFrame(self.leftFrame, text = str_label5)
        self.label5.pack(side = 'top')
        self.text5 = Tr.Text(self.label5, width = 100, heigh = 3)
        self.text5.pack(side = 'top')
        str_label6 = 'NOTES'
        self.lable6Frame = Tr.LabelFrame(self.leftFrame,text = str_label6)
        self.lable6Frame.pack(side = 'top')
        self.text6 = Tr.Text(self.lable6Frame, width = 100, heigh = 3)
        self.text6.pack(side = 'top')

        if flag == True:
            self.savebtn = Tr.Button(self.rightFrame, width = 20, text = 'SAVE',
                                    command = lambda:self.save_interview_record('interview.db', key_, record_[1]))
        else:
            self.savebtn = Tr.Button(self.rightFrame, width = 20, text = 'SAVE',
                                    command = lambda:self.save_interview_record('interview.db', key_, record_[0]))
        self.savebtn.pack(side = 'top')
        self.sendForm_btn = Tr.Button(self.rightFrame, width = 20, text = 'SEND FORM')
        self.sendForm_btn.pack(side = 'top')
        self.openForm_btn = Tr.Button(self.rightFrame, width = 20, text = 'OPEN FORM',
                                      command = lambda:self.save_interview_record('interview.db',key_, record_[1]))
        self.openForm_btn.pack(side = 'top')
        self.vResume_btn = Tr.Button(self.rightFrame, width = 20, text = 'VIEW RESUME',
                                     command = lambda:self.view_resume(value_[0]))
        self.vResume_btn.pack(side = 'top')
        self.interClose_btn = Tr.Button(self.rightFrame, width = 20, text = 'CLOSE',
                                   command = lambda:self.close_window(self.interview_form))
        self.interClose_btn.pack(side = 'bottom')

        key_ = 0
        if flag == False:
            self.nameInput.insert('end',record_[1] + ' ' + record_[2])
            self.dateE.insert('end',self.format_date(str(date.today())))
            self.reqE.insert('end',record_[4])
            key_ = self.i_unique_key('interview.db')
        else:
            rcd_ = db.database().get_interview('interview.db',record_[0])
            key_ = rcd_[0]
            self.nameInput.insert('end',rcd_[2] + ' ' + rcd_[3])
            self.dateE.insert('end',rcd_[5])
            self.interviewersEntry.insert('end', rcd_[4])
            self.reqE.insert('end',rcd_[6])
            self.recommendationE.set(rcd_[7])
            self.levelCombobox.set(rcd_[8])
            self.text1.insert('end', rcd_[9])
            self.text2.insert('end', rcd_[10])
            self.rcExpComboBox.set(rcd_[11])
            self.commSkillsComboBox.set(rcd_[12])
            self.techApSkillsComboBox.set(rcd_[13])
            self.knowComboBox.set(rcd_[14])
            self.text3.insert('end', rcd_[15])
            self.text4.insert('end', rcd_[16])
            self.text5.insert('end', rcd_[17])
            self.text6.insert('end', rcd_[18])

        if db.database().get_interview_exist('interview.db', int(key_)) == False:
            self.sendForm_btn['state'] = 'disabled'
            self.openForm_btn['state'] = 'disabled'

    # saves the interveiw record
    def save_interview_record(self, db_name, key_, cNumber_):
        name_ = self.nameInput.get().split(' ')
        record_ = (int(key_), cNumber_, 
                    name_[0], name_[1], self.interviewersEntry.get(), self.dateE.get(), self.reqE.get(), self.recommendationE.get(),
                    self.levelCombobox.get(), self.text1.get("1.0","end-1c"), self.text2.get("1.0","end-1c"), 
                    self.rcExpComboBox.get(), self.commSkillsComboBox.get(), self.techApSkillsComboBox.get(),
                    self.knowComboBox.get(), self.text3.get("1.0","end-1c"),self.text4.get("1.0","end-1c"), 
                    self.text5.get("1.0","end-1c"), self.text6.get("1.0","end-1c"))

        # To update the candidate database
        mRecord_ = db.database().get_candidate('candidate2.db', cNumber_)

        if self.recommendationE.get() == 'w':
            offer_ = 'YES'
        else:
            offer_ = 'Dispositon'
        main_record_ = (mRecord_[1], mRecord_[2], mRecord_[3], mRecord_[4], mRecord_[5], mRecord_[6], mRecord_[8], 
                        mRecord_[7], mRecord_[9], offer_, mRecord_[0])
        #db.database().insert_record_interview(db_name, record_)
        if db.database().get_interview_exist('interview.db', int(key_)) == False:
            db.database().insert_record_interview(db_name, record_)
            #ex.export_to_excel().export_to_form(db_name,record_) # creates excel file
            self.sendBtn['state'] = 'active'
            self.openformBtn['state'] = 'active'
            db.database().update_candidate_record('candidate2.db',main_record_) 
            #self.clear_search()
            self.interview_records(int(cNumber_))
        else:
            # the format a record is different from record_ because the key is the last item in the edit record
            record = (int(cNumber_), 
                        name_[0], name_[1], self.interviewersEntry.get(), self.dateE.get(), self.reqE.get(), self.recommendationE.get(),
                        self.levelCombobox.get(), self.text1.get("1.0","end-1c"), self.text2.get("1.0","end-1c"), 
                        self.rcExpComboBox.get(), self.commSkillsComboBox.get(), self.techApSkillsComboBox.get(),
                        self.knowComboBox.get(), self.text3.get("1.0","end-1c"),self.text4.get("1.0","end-1c"), 
                        self.text5.get("1.0","end-1c"), self.text6.get("1.0","end-1c"), 
                        int(key_))

            db.database().update_interview_record(db_name,record)
            #ex.export_to_excel().export_to_form(db_name,record_)
            print("main record: ")
            print(main_record_)
            db.database().update_candidate_record('candidate2.db',main_record_) 
            #self.clear_search()
            #self.interview_records(int(cNumber_))

    def format_date(self, date):

        return date[5:7]+ "/" + date[8:10] + "/" + date[2:4]

    def close_window(self, obj):
        obj.destroy()

        # creates a four didit random number and then compares to keys in the db
    def i_unique_key(self, db_):
        key_ = random.randint(1047,9999)

        for item in db.database().db_print_interview_records(db_):
            if key_ == item[0]:
                self.i_unique_key(db_)

        return key_
