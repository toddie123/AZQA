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
        self.sheetrow = None  # row that contains data for ID of interest
        self.use = ""
        self.use_limit = None
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

    def find_legacy_row(self):

        legacy_column = self.df['OLD ID NUMBER']
        #print(legacy_column)

        for i in range(len(legacy_column)):
            print((str(self.df.iloc[i, self.legacyID_col])))
            if (str(self.df.iloc[i, self.legacyID_col]) == str(self.ID)):
                self.sheetrow = i
                print("sheetrow is: " + str(self.sheetrow))
                break

        print("Legacy sheetrow is: " + str(self.sheetrow))

    def find_row(self):
        column = self.df['NEW ID NUMBER']

        for i in range(len(column)):
            # TODO ADD INTO IF  or (str(self.df.iloc[i, 1]) == str(self.ID))
            if (str(self.df.iloc[i, self.ID_col]) == str(self.ID)):
                self.sheetrow = i
                break
        print("In INSTRUMENT: my row is" + str(self.sheetrow))

        if self.sheetrow is None:
            print("FINDING LEGACY")
            self.find_legacy_row()


    def set_status(self):
        print("USE LIMIT IS: " + self.use_limit)
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

        #print("IN INSTRUMENT CLASS LOG PATH IS: " + int(self.config.log))
        print("log from instrument class is: " + str(self.df.iloc[self.sheetrow, int(self.config.log)]))
        if str(self.df.iloc[self.sheetrow, int(self.config.log)]) != 'nan':
            self.log_path = str(self.df.iloc[self.sheetrow, int(self.config.log)])
            self.use_limit = int(self.df.iloc[self.sheetrow, int(self.config.use_lim)])
        else:
            print("from instrument class, LOG IS nan")
            # TODO REMOVE ABOVE AND BELOW
        print('Made it to 122 of instrument class AND use limit is: ' + str(self.use_limit))

        if self.use_limit == 'nan':
            print("from instrument class, USE LIMIT IS ZERO")
            # TODO REMOVE ABOVE AND BELOW
            self.use_limit = 0
        elif self.use_limit is None:
            self.use_limit = 0


        #TODO REMOVE BELOW
        print('Made it out of ifs in instrument class')

        #self.set_status()
        self.ID_col = str(self.df.iloc[self.sheetrow, int(self.config.ID_col)])
        self.legacyID_col = str(self.df.iloc[self.sheetrow, int(self.config.legacy_ID)])
        self.tool_type = str(self.df.iloc[self.sheetrow, int(self.config.instrument_description)] + " " + self.df.iloc[self.sheetrow, int(self.config.instrument_type)])

        if (self.exp_type != 'DATE') or (self.exp_type != 'COUNT'):
            self.exp_type = 'COUNT'
        else:
            self.exp_type = str((self.df.iloc[self.sheetrow, int(self.config.instrument_exp_type)]))


        if self.cal_date == str('nan'):
            self.cal_date = 00/00/0000
        # DONE remove below
        else:
            self.cal_date = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cal_date)])

        self.cal_exp = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cal_exp)])



        #DONE uncomment below once PDF opener works
        self.cert_path = str(self.df.iloc[self.sheetrow, int(self.config.instrument_cert)])
        self.location = str(self.df.iloc[self.sheetrow, int(self.config.instrument_location)])
