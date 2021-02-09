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
from config_class import Config

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
        self.legacyID_col = 1

        # DONE REMOVE BELOW

        self.ID_col = 2    # Col that contains IDs default from sheet as of 02/01/2021 can be set externally

        self.df = pd.read_csv(spreadsheet_path, encoding='UTF-8')  # big thank 6294 for selling me csv ;)
        self.config = Config()

    def set_spreadsheet_path(self, spread_path_intput):
        self.spreadsheet = spread_path_intput

    def find_row(self):
        column = self.df['NEW ID NUMBER']

        for i in range(len(column)):
            # TODO ADD INTO IF  or (str(self.df.iloc[i, 1]) == str(self.ID))
            if (str(self.df.iloc[i, self.ID_col]) == str(self.ID)) or (str(self.df.iloc[i, self.legacyID_col]) == str(self.ID)):
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
            self.status = 'NOT GOOD FOR USE'
        else:
            if new_date_check.check() is True:
                self.status = 'GOOD FOR USE'
            else:
                self.status = 'NOT GOOD FOR USE'

        # TODO REMOVE BELOW
        #print("Today is: " + datetime.today('%m/%d/%y'))
    def set_tool_info(self):
        # Creating the name of the tool. Concatenates description (col E) and model (col G)
        # TODO create column variables for parameters
        self.set_status()
        #print("IN INSTRUMENT CLASS LOG PATH IS: " + int(self.config.log))
        self.log_path = str(self.df.iloc[self.sheetrow, int(self.config.log)])
        self.use_limit = int(self.df.iloc[self.sheetrow, int(self.config.use_lim)])

        self.ID_col = str(self.df.iloc[self.sheetrow, int(self.config.ID_col)])
        self.legacyID_col = str(self.df.iloc[self.sheetrow, int(self.config.legacy_ID)])
        self.tool_type = str(self.df.iloc[self.sheetrow, int(self.config.instrument_description)] + " " + self.df.iloc[self.sheetrow, int(self.config.instrument_type)])


        # DONE remove below

        self.cal_date = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cal_date)])
        self.cal_exp = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cal_exp)])

        self.exp_type = str((self.df.iloc[self.sheetrow, int(self.config.instrument_exp_type)]))

        #DONE uncomment below once PDF opener works
        self.cert_path = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cert)])
        self.location = str(self.df.iloc[self.sheetrow, int(self.config.instrument_location)])
