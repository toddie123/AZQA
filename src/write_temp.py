class Temp(object):

    def __init__(self, status, logpath,gage_id, temp_path):

        self.gage_id = gage_id
        self.status = status
        self.logpath = str(logpath)
        self.temp_path = str(temp_path)

        def write_file():

            file = open(self.temp_path, "w")
            file.write(gage_id + ";" + status + ";" + logpath)
            file.close()

        write_file()