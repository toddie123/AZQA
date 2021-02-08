import datetime

class Date(object):

    def __init__(self, exp_date):

        self.exp_date = exp_date

        self.exp_month = 0
        self.exp_day = 0
        self.exp_year = 0

        # DONE UNCOMMENT BELOW OR FIX

        self.today_month = 0
        self.today_year = 0
        self.today_day = 0

    # calling this will create substrings from the expiration date and assign them to their month, day, and year
    def chop_today(self):
        self.today_year = str(datetime.datetime.now().year)
        self.today_month = str(datetime.datetime.now().month)
        self.today_day = str(datetime.datetime.now().day)



    def chop_date(self):
        self.exp_month = self.exp_date[0:2]
        self.exp_day = self.exp_date[3:5]
        self.exp_year = self.exp_date[6:10]

    def check(self):

        """""
        Returning True means good to use
        """
        # TODO REMOVE BELOW
        print("DT CLASS Today chop date is: " + str(self.today_month) + " " + str(self.today_day) + " " + str(
            self.today_year)[2:4])
        print("DT CLASS Chop Date is: " + str(self.exp_month) + " " + str(self.exp_day) + " " + str(self.exp_year))

        if str(int(self.today_year) > int(self.exp_year)) == 'True':
            # TODO REMOVE BELOW
            return False
        if int(self.today_year) == int(self.exp_year):
            if int(self.today_month) > int(self.exp_month):
                return False
            if int(self.today_day) > int(self.exp_day):
                return False
            else:
                return True
        else:
            return True

