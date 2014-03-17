from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Town Of River Head New York',
    'location': 'Town Of River Head, NY',

    'home_page_url': 'http://www.townofriverheadny.gov',
    'bids_page_url': 'http://www.townofriverheadny.gov/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
