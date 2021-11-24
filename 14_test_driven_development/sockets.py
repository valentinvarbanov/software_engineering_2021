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