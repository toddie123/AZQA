import pandas as pd

class Log(object):
    def __init__(self, filepath):
        self.filepath = ''
        self.usecount = 0

        self.df = pd.read_csv(self.filepath, encoding='unicode_escape')

        self.usecount = self.df.iloc[len(self.df.columns[3]), 3]