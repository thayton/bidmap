from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Beaver County Utah',
    'location': 'Beaver, UT',

    'home_page_url': 'http://beaver.utah.gov',
    'bids_page_url': 'http://beaver.utah.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



