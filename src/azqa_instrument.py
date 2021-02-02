"""""
Aztech Locknut Company Tool Tracker Program
This program is licensed to Aztech Engineering Inc. and its subsidiaries

Written by Todd Kuebelbeck, 2021 developed at and for Aztech Locknut Company
--------------------------------------------------------------------------------
Helper class for Aztech Instrument Tracker; Tool class
"""""
import pandas as pd


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

        # DONE REMOVE BELOW

        self.ID_col = 2    # Col that contains IDs default from sheet as of 02/01/2021 can be set externally

        self.df = pd.read_csv(spreadsheet_path, encoding='unicode_escape')

    def set_spreadsheet_path(self, spread_path_intput):
        self.spreadsheet = spread_path_intput

    def find_row(self):
        column = self.df['NEW ID NUMBER']

        for i in range(len(column)):
            if str(self.df.iloc[i, 2]) == str(self.ID):
                self.sheetrow = i
                break

    def set_tool_info(self):
        # Creating the name of the tool. Concatenates description (col E) and model (col G)
        # TODO create column variables for parameters
        self.tool_type = str(self.df.iloc[self.sheetrow, 6] + " " + self.df.iloc[self.sheetrow, 4])

        self.use_limit = self.df.iloc[self.sheetrow, 15]
        self.cal_date = str(self.df.iloc[self.sheetrow, 12])
        self.cal_exp = str(self.df.iloc[self.sheetrow, 11])
        self.log_path = str(self.df.iloc[self.sheetrow, 16])
        #TODO uncomment below once PDF opener works
        #self.cert_path = self.df.iloc(self.sheetrow, 32)











