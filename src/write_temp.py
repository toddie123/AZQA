class Temp(object):

    def __init__(self, status, logpath):

        self.status = status
        self.logpath = str(logpath)

        def write_file():

            file = open("AITtemp.txt", "w")
            file.write(status + ";" + logpath)
            file.close()

        write_file()