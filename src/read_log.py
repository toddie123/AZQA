import pandas as pd

class Log(object):
    def __init__(self, input_filepath):
        self.filepath = input_filepath
        self.usecount = 0

        self.df = pd.read_csv(self.filepath, encoding='UTF-8', header=None)

        # TODO REMOVE BELOW
        print('cell is ' + str(self.df.iloc[0, 3]))

        # TODO UNCOMMENT BELOW
        #self.usecount = self.df.iloc[len(self.df.columns[3]), 3]  # grabs length of the use column, minus 1
        self.usecount = self.df.iloc[1, 3]  # grabs length of the use column, minus 1