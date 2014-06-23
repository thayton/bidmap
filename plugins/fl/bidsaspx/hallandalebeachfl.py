from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Hallandalebeach Florida',
    'location': 'Hallandale Beach, FL',

    'home_page_url': 'http://www.hallandalebeachfl.gov',
    'bids_page_url': 'http://www.hallandalebeachfl.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



