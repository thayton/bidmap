from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'City Of Taft California',
    'location': 'Taft, CA',

    'home_page_url': 'http://cityoftaft.org',
    'bids_page_url': 'http://cityoftaft.org/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
