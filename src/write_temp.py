class Temp(object):

    def __init__(self, status, logpath,gage_id):

        self.gage_id = gage_id
        self.status = status
        self.logpath = str(logpath)

        def write_file():

            file = open("AITtemp.txt", "w")
            file.write(gage_id + ";" + status + ";" + logpath)
            file.close()

        write_file()