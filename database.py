'''
Created on August 3, 2022
filename: database.py
last update: August 23, 2022
@author: Gus_Maturana
'''

import sqlite3 as sql
import errors as ers
import string
#from numpy import record
#import numpy as np


class database:
    
    DB_NAME = 'candidate1.db'
    
    def __init__(self):
        
        '''
        '''
        
    def database(self, db_name = DB_NAME):
        # Create a database to store blood sugar levels of patient
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        # CREATES TABLE IF DOES NOT EXIST
        cursor.execute('''CREATE TABLE IF NOT EXISTS CANDIDATE (
                           ID                     KEY     NOT NULL,
                           NAME                   TEXT    NOT NULL,
                           LASTNAME               TEXT    NOT NULL,
                           DEGREE                 TEXT    NOT NULL,
                           REGNUMBER              TEXT    NOT NULL,
                           POSITION               TEXT    NOT NULL,
                           EMAILADDRESS           TEXT    NOT NULL,
                           CLEARANCE              TEXT    NOT NULL,
                           CONTACTINFO            TEXT    NOT NULL,
                           INTERVIEW              TEXT    NOT NULL,
                           JOBOFFER               TEXT    NOT NULL);''')
        table.commit()
        
        table.close()

    def candidate_tables(self, db_name):
        # Create a database to store blood sugar levels of patient
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        # CREATES TABLE IF DOES NOT EXIST        
        cursor.execute('''CREATE TABLE IF NOT EXISTS CANDIDATE_INTERVIEW (
                           CANDIDATE_ID                     KEY  NOT NULL,
                           PROGRAM                          TEXT  NOT NULL,
                           CLEARANCE_REQ                    INT   NOT NULL,
                           CLEARANCE_CAN                    TEXT  NOT NULL,
                           DATE_                            TEXT  NOT NULL,
                           TIME_                            TEXT  NOT NULL,
                           CURRENT_COMP                     TEXT  NOT NULL);''')
        
        # A table storing patient data
        cursor.execute('''CREATE TABLE IF NOT EXISTS PHONE_SCREENING (
                            ID_KEY_PRIMARY               KEY   NOT NULL,
                            NAME                         TEXT  NOT NULL,
                            LASTNAME                     TEXT  NOT NULL,
                            PHONE                        TEXT  NOT NULL,
                            INTERVIEWER                  TEXT  NOT NULL,
                            DIVISION                     TEXT  NOT NULL,
                            DATE_                        TEXT  NOT NULL,
                            CURRENTCOMPANY               TEXT  NOT NULL,
                            REASON                       TEXT  NOT NULL,
                            TECHNICAL                    TEXT  NOT NULL,
                            MANAGEMENT                   TEXT  NOT NULL,
                            MANAGEMMENT_COMM             TEXT  NOT NULL,
                            RECOMENDATION                TEXT  NOT NULL,
                            ASSESSMENT                   TEXT  NOT NULL,
                            ROLE                         TEXT  NOT NULL,
                            REQ                          TEXT  NOT NULL);''')
        table.commit()
        
        table.close()
        
    def insert_record_candidate(self, db_name, record):
        #insert items into CANDIDATE table
        table = sql.connect(db_name)
        table.execute('INSERT INTO CANDIDATE VALUES (?,?,?,?,?,?,?,?,?,?,?)', record)
        table.commit()
        
    def insert_record_recovery(self, db_name, record):
        #insert items into CANDIDATE table
        table = sql.connect(db_name)
        table.execute('INSERT INTO  RECOVERY_CANDIDATE VALUES (?,?,?,?,?,?,?,?,?,?,?)', record)
        table.commit()

    def insert_record_phone_screen(self, db_name, record):
        #insert items into CANDIDATE table
        table = sql.connect(db_name)
        table.execute('INSERT INTO  PHONE_SCREENING VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', record)
        table.commit()
    
    def insert_comments(self, db_name, record):
        #insert items into COMMENTS table
        table = sql.connect(db_name)
        table.execute('INSERT INTO CANDIDATE VALUES (?,?,?)', record)
        table.commit()
    
    # This function works correctly
    def update_candidate_record(self, db_name, record):
        table = sql.connect(db_name)
        statement = '''UPDATE CANDIDATE SET NAME = '%s', 
                                        LASTNAME = '%s',
                                          DEGREE = '%s',
                                       REGNUMBER = '%s', 
                                       POSITION  = '%s',
                                    EMAILADDRESS = '%s',
                                     CONTACTINFO = '%s',
                                       CLEARANCE = '%s',
                                       INTERVIEW = '%s',
                                        JOBOFFER = '%s' 
                                        WHERE ID = '%d' ''' %record
        table.execute(statement)
        table.commit()

    def update_phone_screen_record(self, db_name, record):
        table = sql.connect(db_name)
        statement = '''UPDATE PHONE_SCREENING SET NAME                 = '%s',                     
                                                  LASTNAME             = '%s',
                                                  PHONE                = '%s',
                                                  INTERVIEWER          = '%s',
                                                  DIVISION             = '%s',
                                                  DATE_                = '%s',
                                                  CURRENTCOMPANY       = '%s',
                                                  REASON               = '%s',
                                                  TECHNICAL            = '%s',
                                                  MANAGEMENT           = '%s',
                                                  MANAGEMMENT_COMM     = '%s',
                                                  RECOMENDATION        = '%s',
                                                  ASSESSMENT           = '%s',
                                                  ROLE                 = '%s',
                                                  REQ                  = '%s'
                                                  WHERE ID_KEY_PRIMARY = '%d' ''' %record
        table.execute(statement)
        table.commit()
            
    def general_search_query(self, db_name, record):
        table = sql.connect(db_name)
        curser = table.cursor()
        condition = "SELECT * \
                        FROM  CANDIDATE \
                        WHERE ID LIKE '%" + record  + "%'" +  \
                           "OR NAME LIKE ''%" + record  + "%'" +  \
                           "OR LASTNAME LIKE '%" + record  + "%'"  + \
                           "OR DEGREE LIKE '%" + record  + "%'"  + \
                           "OR REGNUMBER LIKE '%" + record  + "%'"  + \
                           "OR POSITION LIKE '%" + record + "%" + \
                           "OR EMAILADDRESS LIKE '%" + record  + "%'"  + \
                           "OR CLEARANCE LIKE '%" + record + "%" + \
                           "OR CONTACTINFO LIKE '%" + record  + "%'" + \
                           "OR INTERVIEW LIKE '%" + record + "%" + \
                           "OR OFFER LIKE '%" + record + "%"
        
    def remove_record(self, db_name, tbl, record):
        # Deletes item from Database
        table = sql.connect(db_name)
        query = 'DELETE FROM ' + tbl.upper() + ' WHERE ID=' + str(record)

        #table.execute(query)
        table.execute('DELETE FROM CANDIDATE WHERE ID=?', (record,))
        table.commit()
            
        table.close()
        
    def remove_record_item(self, db_name, item):
        # Deletes item from Database
        table = sql.connect(db_name)
        table.execute('DELETE FROM CANDIDATE WHERE VALUES (?,?,?,?)', (item,))
        table.commit()
        
    def db_print(self, db_name):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        # Prepare SQL query to INSERT a record into the database.
        condition = "SELECT * FROM CANDIDATE" # Displays all items stored in database

        # Creates a list to store output values
        data = [] 
        
        try:
            # Execute the SQL command
            cursor.execute(condition)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                data.append(row)
        except:
            ers.errors().error_messages(5)
            print('An Error Happen here')
        
        # disconnect from server
        table.close()
        return data
    
    def db_patient_history_print(self, db_name):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        # Prepare SQL query to INSERT a record into the database.
        condition = "SELECT * FROM PATIENT_HIST"

        # Creates a list to store output values
        data = [] 
        print('I am inside db_patient_history_print()')
        try:
            # Execute the SQL command
            cursor.execute(condition)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                id_ = row[0]
                gender_ = row[1]
                weight_= row[2]
                diagnosis_ = row[3]
                date_ = row[4]
                ethnicity_ = row[5]
                alergies_ = row[6]
                # Collects information an stores it into array
                #value = "%d,    %s,    %d,    %s" % (id_, name, age, birthday)
                value = ( id_, gender_, weight_, diagnosis_, date_, ethnicity_, alergies_)
                data.append(value)
        except:
            ers.errors().error_messages(5)
        
        # disconnect from server
        table.close()
        return data
    
    def db_patient_data_print(self, db_name):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        # Prepare SQL query to INSERT a record into the database.
        condition = "SELECT * FROM PATIENT_HISTORY"

        # Creates a list to store output values
        data = [] 
    
        try:
            # Execute the SQL command
            cursor.execute(condition)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                id_ = row[0]
                bsugar_ = row[1]
                bpressure_= row[2]
                exercise_ = row[3]
                frequency_ = row[4]
                hours_ = row[5]
                
                # Collects information an stores it into array
                #value = ( "%d,    %d,    %s,         %s,        %s,         %s"   )
                value = ( id_, bsugar_, bpressure_, exercise_, frequency_, hours_)
                data.append(value)
        except:
            ers.errors().error_messages(5)
        
        # disconnect from server
        table.close()
        return data
    
    # Navigation to the database possible   
    # Implementation needed
    def db_navagation(self):
        
        print('Implementation needed')
        
    # Deletes item from Database
    def remove_item_bsugar(self,db_name, record,):
        # Deletes item from Database
        table = sql.connect(db_name)
        #table.execute('DELETE FROM PATIENT VALUES (?,?,?,?)', record)
        table.execute('DELETE FROM CANDIDATE WHERE KEY=?', (record,))
        table.commit()
        
    # Retrieves the patient name
    def get_record(self, db_name, key):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM CANDIDATE \
               WHERE ID == '%d'" % (key)
        
        cursor.execute(condition)
        name_ = cursor.fetchone()
        # returns the patient name
        return name_[1]
    
    def get_record_bool(self, db_name, key):
        # This function does not work properly
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "IF EXIST (SELECT * FROM CANDIDATE WHERE ID == '%d' \
                    THEN RETURN TRUE \
                    ELSE RETURN FALSE END " %(key)
        
        #cursor.execute(condition)
        #name_ = cursor.fetchone()
        # returns the patient name
        #print(key)
        #print(name_[0])
        if cursor.execute(condition) == 1:
            name_ = cursor.fetchone()
            if name_[0] == key:
                return True
        if cursor.execute(condition) == 0:
            return False
    
    # Retrieves the patient record according matching a ID
    def get_candidate(self, db_name, ID):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM CANDIDATE \
               WHERE ID == '%d'" % (ID)
        
        cursor.execute(condition)
        record_ = cursor.fetchone()
        
        return record_
    
    def print_results(self, db_name, column, key):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        # Prepare SQL query to INSERT a record into the database.
        condition = "SELECT * FROM CANDIDATE \
               WHERE " + column + " LIKE '%" + (key) + "%'"

        # Creates a list to store output values
        data = []
        list_ = []
        
        try:
            cursor.execute(condition)        # Execute the SQL command   
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            
            for row in results:
                for n in range (0,len(row)):
                    list_.insert(n,row[n])  # the list is then converted into a tuple
                
                data.append(tuple(list_))
                #clears the list_
                for n in range (0, len(list_)):
                    list_.pop()
        except:
            ers.errors().error_messages(5)   
                
        # disconnect from server
        table.close()
        return data
    
    def db_general_print(self, db_name, condition):
        # prints information stored in the database
        table = sql.connect(db_name)
        # prepare a cursor object using cursor() method
        cursor = table.cursor()
        print ('Connecting to db')

        # Creates a list to store output values
        data = []
        list_ = []
        
        try:
            cursor.execute(condition)        # Execute the SQL command   
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            
            for row in results:
                for n in range (0,len(row)):
                    list_.insert(n,row[n])  # the list is then converted into a tuple
                
                data.append(tuple(list_))
                #clears the list_
                for n in range (0, len(list_)):
                    list_.pop()
        except:
            ers.errors().error_messages(5)   
                
        # disconnect from server
        table.close()
        return data

    def get_phone_screen(self, db_name, ID):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM PHONE_SCREENING \
               WHERE ID_KEY_PRIMARY == '%d'" % (ID)
        
        cursor.execute(condition)
        record_ = cursor.fetchone()

        return record_

    def get_phone_exist(self, db_name, ID):
        
        table = sql.connect(db_name)
        cursor = table.cursor()
        
        condition = "SELECT * FROM PHONE_SCREENING \
               WHERE ID_KEY_PRIMARY == '%d'" % (ID)
        
        cursor.execute(condition)
        record_ = cursor.fetchone()
        if record_ == None:
            return False
        else:
            return True
    '''
    def record_to_edit(self, record)
        new_record = []
    '''

    def is_record(self, db_, ID):

        table = sql.connect(db_)
        cursor = table.cursor()
        
        condition = "SELECT * FROM CANDIDATE \
               WHERE ID == '%d'" % (ID)
        
        cursor.execute(condition)
        record_ = cursor.fetchone()
        if record_ == None:
            return False
        else:
            return True

        

    
