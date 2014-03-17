from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Cape Charles Virginia',
    'location': 'Cape Charles, VA',

    'home_page_url': 'http://www.capecharles.org',
    'bids_page_url': 'http://www.capecharles.org/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
