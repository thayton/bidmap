from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'West Valley City Utah',
    'location': 'West Valley City, UT',

    'home_page_url': 'http://www.wvc-ut.gov',
    'bids_page_url': 'http://www.wvc-ut.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



