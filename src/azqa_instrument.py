"""""
Aztech Locknut Company Tool Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries
Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Helper class for Aztech Instrument Tracker; Tool class
"""""
import __future__
import pandas as pd
from datetime import datetime
from date_check import Date

class Tool(object):

    """"
    Create tool instance variables
    """
    def __init__(self, ID, spreadsheet_path):

        self.ID = ID
        self.spreadsheet = spreadsheet_path
        self.tool_type = ""
        self.use_limit = ""
        self.cal_date = ""
        self.cal_exp = ""
        self.log_path = ""
        self.cert_path = ""
        # DONE CHANGE SHEETROW TO BLANK
        self.sheetrow = 0  # row that contains data for ID of interest
        self.use = ""
        self.location = ""
        self.exp_type = ""
        self.status = 'GOOD FOR USE'

        # DONE REMOVE BELOW

        self.ID_col = 2    # Col that contains IDs default from sheet as of 02/01/2021 can be set externally

        self.df = pd.read_csv(spreadsheet_path, encoding='UTF-8')  # big thank 6294 for selling me csv ;)

    def set_spreadsheet_path(self, spread_path_intput):
        self.spreadsheet = spread_path_intput

    def find_row(self):
        column = self.df['NEW ID NUMBER']

        for i in range(len(column)):
            # TODO ADD INTO IF  or (str(self.df.iloc[i, 1]) == str(self.ID))
            if (str(self.df.iloc[i, 2]) == str(self.ID)):
                print(str(self.df.iloc[i, 1]))
                self.sheetrow = i
                break

    def set_status(self):
        if self.use_limit.__contains__('/'):
            self.exp_type = 'DATE'

        else:
            self.exp_type = 'COUNT'

        #TODO COMPLETE BELOW
        """""
        if self.use_limit == 'DATE':
            date = datetime.today('%m/%d/%Y')
            if date  self.cal_exp
        """
        #instrument_date = Date(self.cal_exp)
        #instrument_date.chop()
        #instrument_date.chop_today()

        # TODO EDIT HERE?
        new_date_check = Date(self.cal_exp)
        new_date_check.chop_date()
        new_date_check.chop_today()

        #DONE remove below

        if self.exp_type == 'COUNT' and (self.use >= self.use_limit):
            print("used: " + self.use + "; out of " + self.use_limit)
            self.status = 'NOT GOOD FOR USE'
        else:
            if new_date_check.check() is True:
                self.status = 'GOOD FOR USE'
            else:
                self.status = 'NOT GOOD FOR USE'

        # TODO REMOVE BELOW
        print("my status is: " + self.status)
        #print("Today is: " + datetime.today('%m/%d/%y'))
    def set_tool_info(self):
        # Creating the name of the tool. Concatenates description (col E) and model (col G)
        # TODO create column variables for parameters
        self.set_status()
        self.log_path = str(self.df.iloc[self.sheetrow, 16])
        self.use_limit = int(self.df.iloc[self.sheetrow, 15])



        self.ID = str(self.df.iloc[self.sheetrow, 2])
        self.tool_type = str(self.df.iloc[self.sheetrow, 6] + " " + self.df.iloc[self.sheetrow, 4])


        # DONE remove below

        self.cal_date = str(self.df.iloc[self.sheetrow, 12])
        self.cal_exp = str(self.df.iloc[self.sheetrow, 11])

        #DONE uncomment below once PDF opener works
        self.cert_path = str(self.df.iloc[self.sheetrow, 31])
        self.location = str(self.df.iloc[self.sheetrow, 3])
