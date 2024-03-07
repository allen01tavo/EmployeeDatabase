'''
	Created on August 19, 2022
	filename: exel_export.py
	last update: August 23, 2022
	@author: Gus_Maturana
'''

import xlwt
import shutil
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy
import database as db
import openpyxl
import os
from pathlib import Path

class export_to_excel:

	def __init__(self):

		'''
		'''

	def export(self, name_, phone_, sector_, cc_, inter_, note1_, note2_, note3_, result_):
		
		file = self.copyfile(name_)
		rb = open_workbook(file)
		wb = copy(rb)

		s = wb.get_sheet('Sheet 1')

		s.write(0,1, name_)
		s.write(0,3, phone_)
		s.write(2,1, inter_)
		s.write(2,3, sector_)
		s.write(2,5, cc_)
		s.write(5,1, note1_)
		s.write(12,1, note2_)
		s.write(20,1, note3_)
		s.write(27,1, result_)

		wb.save(file)

	# export form to an excel file and saves the inputs to the database
	# it takes a array of the items and the database name
	def export_to_form(self, db_name, record_):
		
		name_ = record_[2] + "_" + record_[3] # full name
		file = self.copyfile(name_)
		wb = openpyxl.load_workbook(file)	# open the file that was created based on the template to edit

		sheet = wb.active

		sheet["B1"] = record_[2] + " " + record_[3] # full name
		sheet["D1"] = record_[4]
		sheet["B3"] = record_[5]
		sheet["D3"] = record_[6]
		sheet["D4"] = record_[7]
		sheet["B5"] = record_[8]
		sheet["A8"] = record_[9]
		sheet["A15"] = record_[10]
		if record_[11] == 'YES' or record_[11] == 'yes' or record_[11] == 'Yes':
			sheet["E22"] = 'X'
		else:
			sheet["H22"] = 'X'
		sheet["A24"] = record_[12]
		if record_[13] == 'INTERVIEW':
			sheet["E31"] = 'X'
		else:
			sheet["H31"] = 'X'
		sheet["A34"] = record_[14]
		sheet["B39"] = record_[15]
		sheet["D39"] = record_[16]

		wb.save(file)
		os.system(file)

	def export_to_interview_form(self, db_name, record_, name_):
		name = record_[3] + " " + record_[4] # full name
		file = self.copyfile(name_,2)
		wb = opnepyxl.load_workbook(file)	# open the file that was created from based on the template to edit

		
	# copies the template an creates a new xlsx file
	def copyfile(self, file_, opt = 1):
		path = Path(file_ + "__Phone_Screen_Form.xlsx")
		if opt == 1:
			file_name = file_ + "_Phone_Screen_Form.xlsx"
			shutil.copyfile('template.xlsx', file_name)
		else:
			file_name = file_ + "_Interview_Form.xlsx"
			shutil.copyfile('Interview_template.xlsx', file_name)

		return file_name
	
	# interview form template has to be created
	def copyfile_interview(self, file_, opt = 1):
		if opt == 1:
			file_name = file_ + "_Interview_Form.xlsx"
		else:
			file_name = file_ + "_Inter"


# class impport information from an excel
class import_from_excel:

	def __init__(self):
		'''
		'''
		pass

# end of import_from_excel class

# class exports the interview form to an excel
class export_interview_form:
	
	def __init__(self):
		'''
		'''
		pass
	def export_to_form(self):
		pass

# end of export_interview_form Calss

