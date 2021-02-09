import pandas as pd

class Config(object):

    def __init__(self):
        self.config = pd.read_csv(r"config.csv", encoding='UTF-8')

        self.masterlist = str(self.config.iloc[0, 0])
        self.log = str(self.config.iloc[0, 1])
        self.use_lim = str(self.config.iloc[0, 2])
        self.ID_col = str(self.config.iloc[0, 3])
        self.legacy_ID = str(self.config.iloc[0, 4])
        self.instrument_description = str(self.config.iloc[0, 5])
        self.instrument_type = str(self.config.iloc[0, 6])
        self.instrument_cal_date = str(self.config.iloc[0, 7])
        self.instrument_cal_exp = str(self.config.iloc[0, 8])
        self.instrument_exp_type = str(self.config.iloc[0, 9])
        self.instrument_cert = str(self.config.iloc[0, 10])
        self.instrument_location = str(self.config.iloc[0, 11])
        self.temp_location = str(self.config.iloc[0, 12])


