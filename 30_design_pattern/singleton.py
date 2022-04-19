
class Logger:
    __instance = None

    __logfile = None

    @staticmethod 
    def get():
        """ Static access method. """
        if Logger.__instance == None:
            Logger("log")
        return Logger.__instance

    def __init__(self, logfile):
        """ Virtually private constructor. """

        self.__logfile = open(logfile, "w")

        if Logger.__instance != None:
            raise Exception("This class is a Logger!")
        else:
            Logger.__instance = self

    def __del__(self):
        self.__logfile.close()

    def log(self, msg):

        self.__logfile.write(msg + '\n')

        print(msg)

        pass


Logger.get().log("It works...")

for i in range(10):
    Logger.get().log(str(i) + " pass")