from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Wilbraham Massachusetts',
    'location': 'Wilbraham, MA',

    'home_page_url': 'http://www.wilbraham-ma.gov',
    'bids_page_url': 'http://www.wilbraham-ma.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



