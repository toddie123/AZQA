"""""
Aztech Locknut Company Tool Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries
Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Helper class for Aztech Instrument Tracker; Tool class
"""""
import __future__
import pandas as pd
import datetime

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
        self.status = 'GAGE READY FOR USE'

        # DONE REMOVE BELOW

        self.ID_col = 2    # Col that contains IDs default from sheet as of 02/01/2021 can be set externally

        self.df = pd.read_csv(spreadsheet_path, encoding='unicode_escape')  # big thank 6294 for selling me csv ;)

    def set_spreadsheet_path(self, spread_path_intput):
        self.spreadsheet = spread_path_intput

    def find_row(self):
        column = self.df['NEW ID NUMBER']

        for i in range(len(column)):
            if str(self.df.iloc[i, 2]) == str(self.ID):
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
        if self.use_limit == 'COUNT' and self.use >= self.use_limit:
            self.status = 'GAGE NEEDS RECALIBRATION'

    def set_tool_info(self):
        # Creating the name of the tool. Concatenates description (col E) and model (col G)
        # TODO create column variables for parameters
        self.ID = str(self.df.iloc[self.sheetrow, 2])
        self.tool_type = str(self.df.iloc[self.sheetrow, 6] + " " + self.df.iloc[self.sheetrow, 4])

        self.use_limit = int(self.df.iloc[self.sheetrow, 15])
        # DONE remove below

        self.cal_date = str(self.df.iloc[self.sheetrow, 12])
        self.cal_exp = str(self.df.iloc[self.sheetrow, 11])
        self.log_path = str(self.df.iloc[self.sheetrow, 16])
        #DONE uncomment below once PDF opener works
        self.cert_path = str(self.df.iloc[self.sheetrow, 31])
        self.location = str(self.df.iloc[self.sheetrow, 3])