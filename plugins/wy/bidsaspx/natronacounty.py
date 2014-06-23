from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Natrona County Wyoming',
    'location': 'Casper, WY',

    'home_page_url': 'http://www.natronacounty-wy.gov',
    'bids_page_url': 'http://www.natronacounty-wy.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



