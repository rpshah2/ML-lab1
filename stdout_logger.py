class stdout_logger:

    def __init__(self, log_level):
        self.__log_type__ = "stdout"
        self.__log_level__ = log_level

    #print log output
    def log(self, log_level, message):
        if( self.__log_level__ >= log_level):
            print (log_level,': ',message)

        return
