'''
    written on: September 20, 2022
    filename: onbard.py
    description: after the candidate has accepted the offer information is transfered to this table of the database
    last update: September 20, 2022
    @author: Gus_Maturana
'''

import tkinter as Tr
import tkinter.ttk as ttk #from Tkinter import Tk as ttk
import database as db
import errors as ers


class onboard:

	'''
		follows steps to onboard a new employee
		* Request a computer
		* The material needed for the computer
		* contact the project and let them know the employee start date
		* 
	'''
	def __init__(self):

		'''
		'''

	# creates the onbarding main window
	def onboarding_window(self, db_ = ''):
		
		titel_= 'Ready to Onboard'
		self.onboard_win = Tr.Tk()
		self.onboard_win.title(titel_)
		self.onboard_win.minsize(width=700, height=500)
		self.close_btn = Tr.Button(self.onboard_win, text = 'CLOSE', command = lambda:self.close_windows(self.onboard_win))
		self.close_btn.grid(row = 2, column=1)
		self.email_poc = Tr.Button(self.onboard_win, text = 'Email POC', command = lambda:self.close_windows(self.onbard_win))
		self.email_poc.grid(row = 1, column=1)

		self.onboard_win.mainloop()


	def save_record(self, record_):
		pass
		
	# Closes the window
	def close_windows(self, obj):
		obj.destroy()


	def infor_POC(self, obj):
		# implementation needed
		# This function will inform GL, Program POC, and Dept Admin of new hire start date
		# is the individual going to be remote or on site
		# provide options if the employee is remote
		pass

	def assign_training(self, obj):
		# this function will determine what task is available 

		# the program should a list of employees that L3Harris has extended an offer to them
		pass

	def advice_employee(self, obj):
		return obj



'''
	Delete after completing testing of class
'''
def main():
	onboard().onboarding_window('s')


if __name__ == '__main__':
	main()

