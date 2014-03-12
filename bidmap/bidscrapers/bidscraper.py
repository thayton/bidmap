from bidmap.browser.bidmap_browser import BidMapBrowser

class BidScraper(object):
    def __init__(self, govinfo=None):
        self.gov = govinfo
        self.br = BidMapBrowser()
        self.br.set_handle_robots(False)

    def scrape_bid_links(self, url):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        pass

    def prune_unlisted_bids(self, bid_list):
        ''' Remvoe bids from the database that are no longer 
        listed on the site '''
        pass

    def new_bids(self, bid_list):
        ''' Determine which bids on site are new when 
        compared to the database of bids already downloaded'''
        pass

    def scrape_bids(self):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        self.prune_unlisted_bids(bid_list)
        new_bids = self.new_bids(bid_list)
        for bid in new_bids:
            print bid


