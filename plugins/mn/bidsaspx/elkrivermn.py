from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Elk River Minnesota',
    'location': 'Elk River, MN',

    'home_page_url': 'http://www.elkrivermn.gov',
    'bids_page_url': 'http://www.elkrivermn.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



