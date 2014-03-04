import time
from mechanize import Browser, _sockettimeout

class BidMapBrowser(Browser):
    def __init__(self,
                 factory=None,
                 history=None,
                 request_class=None,
                 ):

        Browser.__init__(self, factory, history, request_class)
        self.delay = 2
        self.addheaders = [('User-agent', 
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7')]


    def open(self, url, data=None,
             timeout=_sockettimeout._GLOBAL_DEFAULT_TIMEOUT):
        """
        Override base class open to enforce a delay in requests
        so that we don't overload servers we are scraping by 
        making requests too quickly.
        """
        time.sleep(self.delay)
        return self._mech_open(url, data, timeout=timeout)

