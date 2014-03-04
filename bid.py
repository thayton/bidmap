class Bid(object):
    def __init__(self):
        self.title     = None
        self.url       = None
        self.url_data  = None

    def __str__(self):
        attribs = ['title', 'url', 'url_data']
        f = lambda o,a,d: hasattr(o, a) and getattr(o, a) or d
        v = [ f(self, a, '') for a in attribs ]
        return '\n'.join(['%s' % x.encode('utf8') for x in v])

if __name__ == '__main__':
    bid = Bid()
    bid.title = 'Bus Transfer Station - Downtown Norfolk'
    bid.url = 'http://www.norfolk.gov/bids.aspx?bidID=380'

    print bid
