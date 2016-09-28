import requests


class myElsClient:
    """A class that implements a Python interface to api.elsevier.com"""

    # local variables
    __base_url = "https://api.elsevier.com/"

    # constructors
    def __init__(self, apiKey):
        """Instantiates a client with a given API Key."""
        self.apiKey = apiKey

    # configuration functions
    """Sets an institutional token for customer authentication"""
    def setInstToken(self, instToken):
        self.instToken = instToken

    # utility access functions
    def getBaseURL(self):
        """Returns the base URL currently configured for Elsevier's APIs"""
        return self.__base_url

    # request/response execution functions
    """Constructs and send the actual request"""
    def execRequest(self,path,params):
        headers = {
            "X-ELS-APIKey" : self.apiKey
            }
        r = requests.get(self.__base_url + path, headers = headers)
        return r
