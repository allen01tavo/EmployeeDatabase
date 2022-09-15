'''
    Created on Jun 27, 2016
    
    @author: gmaturan
'''


#import Tkinter as tk
from tkinter import messagebox
#import Tkinter as tk


class errors:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def error_messages(self, choice):
        
        if choice == 1:
            messagebox.showinfo('Error 1:', 'Please enter a blood sugar level value')
        if choice == 2:
            messagebox.showinfo('Error 2:', 'Blood sugar level is too high')
        if choice == 3:
            messagebox.showinfo('Error 3:', 'Blood sugar level is too low')
        if choice == 4:
            messagebox.showinfo('Error 4:', 'There is not value')
        if choice == 5:
            messagebox.showinfo('UNABLE TO FETCH DATA:', 'Check Query algorithm')
        if choice == 6:
            messagebox.showinfo('Implementation needed')
        if choice == 7:
            messagebox.showinfo('Key value already exists')
        if choice == 8:
            messagebox.showinfo('SAVED','Record has been Updated')
        if choice == 9:
            messagebox.showinfo('SAVED','Candidate has been disposition')
        if choice == 10:
            messagebox.showinfo('Record has been restored')
        if choice == 11:
            messagebox.showinfo('Resume has not been uploaded')
    def hints(self, choice):
        
        if choice == 1:
            messagebox.showinfo("Hint 1:", 'Enter a correct value')
        if choice == 2:
            messagebox.showinfo("Hint 2:", 'Enter a numerical value')
    
    # specific messages
    def general_error_messages(self, st):
        
        message = 'Please enter a value for: ' + st
        messagebox.showinfo('Missing Information', message)
    
    # delete message
    def delete_message(self, st):
        message = st + ' has been deleted.'
        messagebox.showinfo('Deletion Confirmation', message)
    
    # delete confirmation message
    def delete_confirmation(self, st):
        message = 'Do you want to delete ' + st + '?'
        result = messagebox.askyesno('Confirm Deletion', message)
        
        return result
     
    # search message     
    def search_message(self, st):
        message = 'There is not record matching searching criteria: ' + st
        messagebox.showinfo('Search', message)
    
    # integer error
    def integer_error(self, st):
        message = st + ': Search value must be a number: '
        messagebox.showinfo('Search Error', message)
    
    def general_message(self, st):
        messagebox.showinfo('ERROR', st)

    def restore_message(self):
        message = 'In order to see the record information, the record must be restore'
        messagebox.showinfo('Deleted', message)


#End of Class
