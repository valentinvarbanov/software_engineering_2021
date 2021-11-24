

# this will not appear in the doxygen

##
# This is a class stores the endpoint of the user
# and its current cookies
# 
# Creating a session is done like:
# ```
#  s = Session("IP", "PORT", data)
# ```
class Session:
    
    ## test1
    self.ip = "" 

    ## test2
    self.port = "" 
    
    ## test3
    self.cookies = "" 

    def __init__(self, ip, port, cookies) -> None:
        pass

    def test(self) -> None:
        """
        @brief empty method 
        """
        pass

##
# @brief The same text gets recognized 
class SessionManager:


    ## This is how documentation is added to variables
    self.sessions = []

    ## 
    # @brief Documentation is classic Doxygen style
    #
    # @param session - the new session
    def add_session(self, session: Session):
        pass
    
    def close_session(self, session: Session) -> bool:
        """
        Python also allows the docstrings format to be used
        """
        pass