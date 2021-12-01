import re

class IPAdress:

    def __init__(self, ip) -> None:
        self.ip = ip

    def is_valid(self):
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        return re.search(regex, self.ip)

    def is_private(self):
        # return self.is_valid() and (self.ip[0:3]=='10.' or self.ip[0:7]=='192.168' or self.ip[0:4]=='172.')
        regex = '^(10(\\.(25[0-5]|2[0-4][0-9]|1[0-9]{1,2}|[0-9]{1,2})){3}|((172\\.(1[6-9]|2[0-9]|3[01]))|192\\.168)(\\.(25[0-5]|2[0-4][0-9]|1[0-9]{1,2}|[0-9]{1,2})){2})$'
        return self.is_valid() and re.search(regex, self.ip)

    def is_public(self):
        return not self.is_private()

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

