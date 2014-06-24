from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Watertown Massachusetts',
    'location': 'Watertown, MA',

    'home_page_url': 'http://www.watertown-ma.gov',
    'bids_page_url': 'http://www.watertown-ma.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



