class file_logger:

    def __init__(self, log_level):
        self.__log_type__ = "file"
        self.__log_level__ = log_level

    #Print log output to a file
    def log(self, log_level, message, new_filename):

        if (self.__log_level__ >= log_level):

            file = open(new_filename, 'a')
            file.write(str(log_level))
            file.write(" "+message+"\n")
            file.close()

        return