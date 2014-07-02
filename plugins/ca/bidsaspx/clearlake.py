from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Clearlake California',
    'location': 'Clearlake, CA',

    'home_page_url': 'http://clearlake.ca.us',
    'bids_page_url': 'http://clearlake.ca.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



