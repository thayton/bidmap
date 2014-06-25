from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sugar Land Texas',
    'location': 'Sugar Land, TX',

    'home_page_url': 'http://www.sugarlandtx.gov',
    'bids_page_url': 'http://www.sugarlandtx.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



