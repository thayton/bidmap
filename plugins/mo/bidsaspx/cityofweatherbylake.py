from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Weatherby Lake Missouri',
    'location': 'Weatherby Lake, MO',

    'home_page_url': 'http://www.cityofweatherbylake-mo.gov',
    'bids_page_url': 'http://www.cityofweatherbylake-mo.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



