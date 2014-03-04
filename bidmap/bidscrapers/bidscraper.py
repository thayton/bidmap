from bidmap.browser.bidmap_browser import BidMapBrowser

class BidScraper(object):
    def __init__(self, govinfo=None):
        self.gov = govinfo
        self.br = BidMapBrowser()
        self.br.set_handle_robots(False)

    def scrape_bids(self):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        pass

    def prune_unlisted_bids(self):
        ''' Remvoe bids from the database that are no longer 
        listed on the site '''
        pass

    def new_bids(self):
        ''' Determine which bids on site are new when 
        compared to the database of bids already downloaded'''
        pass
