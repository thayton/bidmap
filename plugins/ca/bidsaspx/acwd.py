from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Alameda County Water District California',
    'location': 'Fremont, CA',

    'home_page_url': 'http://www.acwd.org',
    'bids_page_url': 'http://www.acwd.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



