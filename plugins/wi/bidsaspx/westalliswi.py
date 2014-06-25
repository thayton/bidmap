from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'West Allis Wisconsin',
    'location': 'West Allis, WI',

    'home_page_url': 'http://www.westalliswi.gov',
    'bids_page_url': 'http://www.westalliswi.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



