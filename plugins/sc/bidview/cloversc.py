from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Clover South Carolina',
    'location': 'Clover, SC',

    'home_page_url': 'http://www.cloversc.org',
    'bids_page_url': 'http://www.cloversc.org/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
