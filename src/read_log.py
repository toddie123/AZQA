import pandas as pd

class Log(object):
    def __init__(self, input_filepath):
        self.filepath = input_filepath
        self.usecount = 0

        #print("LOG IS: " + input_filepath)

        if self.filepath != 'nan':
            if self.filepath is None:
                print('No Log File Found')
            else:
                self.df = pd.read_csv(self.filepath, encoding='UTF-8', header=None)
                # self.usecount = self.df.iloc[len(self.df.columns[3]), 3]  # grabs length of the use column, minus 1
                self.usecount = self.df.iloc[1, 3]  # grabs length of the use column, minus 1
        else:
            self.usecount = 0

            # done REMOVE BELOW
        #print("USE COUNT IS: " + str(self.usecount))
            # TODO UNCOMMENT BELOW
