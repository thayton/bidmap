from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'East Grand Rapids Michigan',
    'location': 'East Grand Rapids, MI',

    'home_page_url': 'http://www.eastgr.org',
    'bids_page_url': 'http://www.eastgr.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



