class SocketAddress:
    __MIN_PORT = 0
    __MAX_PORT = 2 ** 16 - 1

    def __init__(self, address):
        assert isinstance(address, str)

        self.__address = address

        if len(self.address.split(':')) == 2 and self.address.split(':')[1]:
            self.__port = int(self.__address.split(':')[1])
        

    @property
    def address(self):
        return self.__address


    @property
    def port(self):
        return self.__port


    def is_valid(self):
        return SocketAddress.__MIN_PORT <= self.port <= SocketAddress.__MAX_PORT


    #def is_whole_socket_address(self):

    