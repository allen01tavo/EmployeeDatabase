'''
    Created on August 26, 2022
    filename: email.py
    @author: Gus_Maturana
    @last_update: January 31, 2024
'''

#from appscript import app, k
from tkinter import filedialog
from tkinter import messagebox
import win32com.client
import tkinter as ttk 
import os
from os import listdir
import shutil
import errors as ers 

class email:

    def __init__(self, subject_ = 'Mail subject'):
        # size of the new email
        self.olmailitem = 0x0
        self.subject = subject_
        self.outlook = win32com.client.Dispatch('outlook.application')


    def send_email(self, email_, message_, path_= ''):

        file_path = self.find_attachment(path_)
        mail = self.outlook.CreateItem(self.olmailitem)   
        mail.To = email_
        mail.Subject = self.subject
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        mail.Body = message_
        mail.Attachments.Add(os.path.join(os.getcwd(), file_path))  #word documnet donot seem to work in attachments
        #mail.Attachments.Add()
        mail.CC = 'gusmaturana@icloud.com'
        mail.Display()
        #mail.Send()

    def creat_and_send_form(self, email, database, message):
        pass
        # a copy of the form is created and attached to the email
        # the form will be deleted after the email is sent
        
    def send_reminder(self, email_, body_, subject_):
        mail = self.outlook.CreateItem(0)
        mail.To = email_
        mail.Subject = subject_
        mail.Body = 'This is a reminder that you have a task due'
        ers.notifications().notification(2)

    # Helper function to find the complete attachement path
    def find_attachment(self, path_):
        path = str(path_)
        print('Path:' + path)
        if os.path.exists(path):
            #list_files = os.listdir(path)
            for i in listdir(path):
                print(i)
                extension = i.split('.')[1]
                if (extension == 'xlsx') or (extension == 'xlx'):
                    file_= i
                    print("file_paht: " + i)
                    return file_
        else: 
            ers.errors().error_messages(13)

    def format_file_path(self, path_):
        tmp = path_.split('\\')
        size = len(tmp)
        print('Size of tmp: ' + tmp)
        tmp2 = ''
        for i in tmp:
            tmp2 = tmp2 + '\\' + i

        return '\\' + tmp2 
        
# end class

class browse:

    def __init__(self):
        '''
        '''
    def mesage_phone_screen(self, name_):
        message = "Phone screen for " + name_ + " has been completed." +\
                  "Please see attached Phone Screen Form"
        return message

    def message_interview(self, name_, date_, time_):
        message = " Please schedule virtual inteview with " + name_ + " for " + date_ + " at " + time_
        return message

    def browse_file(self, newFolder_):

        fname = filedialog.askopenfilename(filetypes = (("Template files", "*.*"), ("All files", "*")))
        if fname != '':
            extension = fname.split('.')[1]
            print(extension)
            # creates the directory and then copies the file in it
            os.mkdir(str(newFolder_))
            shutil.copy(fname,str(newFolder_))

    # Opens the stored document for viewing
    def open_files(self, key_):
        path = str(key_)
        if os.path.exists(path):
            list_files = os.listdir(path)
            for i in list_files:
                extension = i.split('.')[1]
                if (extension == 'doc') or (extension == 'docx') or (extension == 'pdf'):
                    os.chdir(path)
                    os.system('"'+i+'"') # Quotation marks are used in cased the document name has spaces
                    os.chdir('..')
        else:
            # Gives the user a change to upload a resume when one is not found
            msg = 'Would you like to add a resume?'
            rsl = messagebox.askyesno('No Resume On File',msg)
            if rsl == True:
                self.browse_file(key_)
            else:
                pass

# end of class

class setup_meeting:

    def __init__(self, info, recipients):
        self.Subject_ = info[0]
        self.Start_ = info[1]
        self.Location_ = info[2]
        self.Body_ = info[3]
        self.Recipients_ = recipients
        # create an outlook object
        outlook = win32com.client.Dispatch("Outlook.Application")
        self.outlook_appt = outlook.CreateItem(1) # 1 means appointment

    def setup_meeting(self):
        # set the meeting details
        self.outlook_appt.Subject = self.Subject_ # the meeting title
        self.outlook_appt.Start = self.Start_ # the meeting start time in yyyy-MM-dd hh:mm format
        self.outlook_appt.Duration = 60 # the meeting duration in minutes
        self.outlook_appt.Location = self.Location_ # the meeting location
        self.outlook_appt.Body = self.Body_ # the meeting body
        self.outlook_appt.ReminderSet = True # enable reminder
        self.outlook_appt.ReminderMinutesBeforeStart = 15 # set reminder to 15 minutes before start
        self.outlook_appt.MeetingStatus = 1
        # add attendees
        for i in self.Recipients_:
            self.outlook_appt.Recipients.Add(i)

        # send the meeting request
        self.outlook_appt.Display()
        #self.outlook_appt.Send()
        print(self.outlook_appt.Start)

# In order to test the classes
def main():
    #email().send_email('gumaturana@gmail.com', 'Gustavo Maturana', 'Phone Screen with L3Harris')
    message_ = 'this is email is just a test'
    root = ttk.Tk()
    root.wm_title("Browser")
    bButton = ttk.Button(master = root, text = 'Browse', width = 6, command=lambda:browse().browse_file('Test'))
    eButton = ttk.Button(master = root, text = 'Test1', width = 6, 
                         command=lambda:email('Test1').send_email(message_,'gus2234@hotmail.com' ))

    info_ = ('My Test Meeting', '2024-02-22 10:30', 'Online', 'This is just a test 1')  
    people = ('gusmaturana@icloud.com','gumaturana@gmail.com', 'tavocub101@yahoo.com')                                                                                            
                                                                                                        
    mButton = ttk.Button(master = root, text = 'Meeting', width = 7, 
                         command=lambda:setup_meeting(info_, people).setup_meeting())
    
    bButton.pack(side=ttk.RIGHT, padx = 2, pady =2)
    eButton.pack(side=ttk.LEFT, padx = 2, pady=2)
    mButton.pack(side=ttk.LEFT, padx =2, pady=2)

    

    ttk.mainloop()


if __name__ == '__main__':
    main()
