'''
Created on August 26, 2022
filename: database.py
@author: Gus_Maturana
'''

from appscript import app, k
from tkinter import filedialog
import tkinter as ttk 

# 
class email:

    def __init__(self):
        '''
        '''

    def send_email(self, email_, name_, subject_):

        outlook = app('Microsoft Outlook')

        msg = outlook.make(
            new=k.outgoing_message,
            with_properties={
                k.subject: subject_,
                k.plain_text_content: 'Test email body'})

        msg.make(
            new=k.recipient,
            with_properties={
                k.email_address: {
                    k.name: name_,
                    k.address: email_ }})

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

    def browse_file(self):

        fname = filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
        print (frame)

        root = Tk.Tk()
        root.wm_title("Browser")
        broButton = Tk.Button(master = root, text = 'Browse', width = 6, command=browse_file)
        broButton.pack(side=Tk.LEFT, padx = 2, pady=2)

        Tk.mainloop()


def main():
    #email().send_email('gumaturana@gmail.com', 'Gustavo Maturana', 'Phone Screen with L3Harris')
    messages().browse_file()


if __name__ == '__main__':
    main()