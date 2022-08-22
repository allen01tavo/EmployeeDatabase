import xlwt
import shutil
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy
import database as db
import openpyxl

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
	def export_to_form(self, record_, db_name):
		
		name_ = record_[1] + "_" + record_[2] # full name
		file = self.copyfile(name_)
		wb = openpyxl.load_workbook(file)	# open the file that was created fromt eh template to edit

		sheet = wb.active

		sheet["B1"] = record_[1] + " " + record_[2] # full name
		sheet["D1"] = record_[3]
		sheet["B3"] = record_[4]
		sheet["D3"] = record_[5]
		sheet["D4"] = record_[6]
		sheet["B5"] = record_[7]
		sheet["A8"] = record_[8]
		sheet["A15"] = record_[9]
		if record_[10] == 'YES' or record_[10] == 'yes' or record_[10] == 'Yes':
			sheet["E22"] = 'X'
		else:
			sheet["H22"] = 'X'
		sheet["A24"] = record_[11]
		if record_[12] == 'INTERVIEW':
			sheet["E31"] = 'X'
		else:
			sheet["H31"] = 'X'
		sheet["A34"] = record_[13]
		sheet["B39"] = record_[14]
		sheet["D39"] = record_[15]

		wb.save(file)

		# saves screening interview to the database
		db.database().insert_record_phone_screen(db_name, record_)

	# copies the template an creates a new xlsx file
	def copyfile(self, file_):
		file_name = file_ + "_Phone_Screen_Form.xlsx"
		shutil.copyfile('template.xlsx', file_name)

		return file_name



