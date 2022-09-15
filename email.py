'''
    Created on August 26, 2022
    filename: database.py
    @author: Gus_Maturana
'''

from appscript import app, k
from tkinter import filedialog
import tkinter as ttk 
import os
import errors as ers 

class email:

    def __init__(self):
        '''
        '''

    def send_email(self, email_, name_, subject_):

        files = ['Pixie_Cat_Phone_Screen_Form.xlsx']
        for file in files:
            with open(file, 'rb') as f:
                file_data = f.read()
                ##file_tye = imaghdr.what(f.name)
                file_name = f.name

        outlook = app('Microsoft Outlook')
        msg = outlook.make(
            new=k.outgoing_message,
            with_properties={
                k.subject: subject_,
                k.plain_text_content: 'Test email body',
                k.attachment:file})

        msg.make(
            new=k.recipient,
            with_properties={
                k.email_address: {
                k.name: name_,
                k.address: email_}})

        msg.open()
        msg.activate()

# end class

class messages:

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

            cmd = 'mkdir -p ' + str(newFolder_)
            os.system(cmd)
            cmd = 'cp ' + fname + ' ' + str(newFolder_)
            os.system(cmd)

    def open_files(self, key_):
        path = str(key_)
        print(path)
        if os.path.exists(path):
            list_files = os.listdir(path)
            for i in list_files:
                extension = i.split('.')[1]
                if (extension == 'doc') or (extension == 'docx') or (extension == 'pdf'):
                    cmd = 'open ' + path + '/' + i
                    print(cmd)
                    os.system(cmd)
        else:
            ers.errors().error_messages(11)

def main():
    #email().send_email('gumaturana@gmail.com', 'Gustavo Maturana', 'Phone Screen with L3Harris')
    root = ttk.Tk()
    root.wm_title("Browser")
    broButton = ttk.Button(master = root, text = 'Browse', width = 6, command=lambda:messages().browse_file('Test'))
    broButton.pack(side=ttk.LEFT, padx = 2, pady=2)

    ttk.mainloop()


if __name__ == '__main__':
    main()
